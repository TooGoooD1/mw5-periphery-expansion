"""Reference implementation of Periphery Expansion rules.

This is the single source of truth for the numbers and logic. The in-game
Blueprint implementation (built later in the MW5 Mod Editor) must match it,
and tests/test_rules.py pins the behaviour. Standard library only.
"""
import re

HEX_COLOR = re.compile(r"^#[0-9A-Fa-f]{8}$")  # #RRGGBBAA
CHAIN_LENGTH = 5


def valid_color(value):
    """True if value looks like #RRGGBBAA."""
    return isinstance(value, str) and bool(HEX_COLOR.match(value))


def speed_multiplier(planets_held, table, cap):
    """Facility speed vs normal hubs (1.0 = same as a normal hub).

    Returns None when no planet is held (the mod grants nothing).
    Counts above the largest table entry use that entry; never exceeds cap.
    """
    if planets_held < 1:
        return None
    keys = sorted(int(k) for k in table)
    key = min(planets_held, keys[-1])
    return min(table[str(key)], cap)


def time_multiplier(planets_held, table, cap):
    """Repair/build time vs normal hubs (4.0 = four times longer)."""
    speed = speed_multiplier(planets_held, table, cap)
    return None if speed is None else 1.0 / speed


def discount_percent(planets_held, per_planet, cap):
    """Repair/re-mod discount in percent."""
    if planets_held < 1:
        return 0
    return min(per_planet * planets_held, cap)


def eligible_targets(owned, adjacency, planet_factions, eligible_factions,
                     max_planets, campaign_in_progress=False):
    """Planets the player may start a takeover on.

    owned:            set/list of planet ids the player controls
    adjacency:        {planet_id: [neighbour ids]} from the star map
    planet_factions:  {planet_id: faction name}
    Rule for the first planet (no owned planets yet) is still undecided in
    the design doc; for now every planet of an eligible faction qualifies.
    """
    owned = set(owned)
    if campaign_in_progress or len(owned) >= max_planets:
        return []
    if owned:
        candidates = set()
        for planet in owned:
            candidates.update(adjacency.get(planet, []))
        candidates -= owned
    else:
        candidates = set(planet_factions)
    return sorted(p for p in candidates
                  if planet_factions.get(p) in eligible_factions)


def next_stage(completed_count):
    """Order (1..5) of the next mission, or None when the chain is complete."""
    if completed_count < 0:
        raise ValueError("completed_count cannot be negative")
    return None if completed_count >= CHAIN_LENGTH else completed_count + 1
