# Design summary (v0.2)

Condensed from the full design document; updated after inspecting the game's star map and faction data.

## 4. Takeover
- Default eligible targets: **factionless and independent planets** (owner NoFaction or Independent, to be verified). Periphery states and other factions can be added in options. The map shows Periphery states with no territory fill, like factionless planets, so they look the same on the map.
- Target must be adjacent on the star map to an already controlled planet.
- Max planets controlled: 5 by default (option).
- Five missions per planet, in order; each unlocks the next:

| # | Type (proposed) | Weight limit |
|---|---|---|
| 1 | Recon | one light mech, 35 t or less |
| 2 | Sabotage / supply raid | 100 t |
| 3 | Ambush / convoy interdiction | 200 t |
| 4 | Base assault | 300 t |
| 5 | Full planet assault (hardest existing mission) | 400 t |

Weights for 2 to 4 are proposals. On success the planet's industries transfer to the player.

## 6. Balance
Speed vs normal hubs: 1 planet 0.25x, 2 planets 0.5x, 3 planets 0.75x, 4 planets 1.0x, 5+ planets 1.25x (cap).
Discounts (placeholder): 10% per planet, capped at 40%.
The base game shows hub bonuses such as repair cost and repair time -15% on a planet's overlay; we should present ours the same way.

## 7. Area of control and logo
What the star map actually shows (from in-game screenshots):
- Great houses, Clans and Com Star get a coloured territory fill with a border, tied to the faction's Star Map Stencil Id, a fixed list.
- Mercenary companies get a **dashed blue circle centred on a planet with the company logo at the centre**; selecting a planet inside shows the owner and the assigned merc company.
- Periphery and factionless planets have no fill.

Plan: copy the merc circle and logo for our company. Custom perimeter and interior colours are a stretch goal; they probably need custom star-map UI.
The company name and logo are chosen by the player at the start of a campaign, so the overlay must read the live player data, not the default `PlayerFaction` asset. How the game stores that is still unknown.

## Feasibility risks (as of v0.2)
- Planet ownership appears to be a date-driven timeline; changing it at runtime in a mod is unproven.
- Hubs and merc areas are static data assets plus Blueprint actors. A mod that works on any planet the player takes may need custom campaign Blueprint logic, not just new data.
- Native (C++) base classes cannot be changed; we can only subclass or add Blueprints.
- Custom colours are probably not possible without custom UI.
Plan: prove the smallest pieces first (a mod-added cluster that shows up in game; a mod-added merc circle) before building the five-mission chain.

## Open items
- Where merc areas are defined (leads: `Campaign\RivalMercs`, `Campaign\Clusters`, `Factions\ClusterOwners`)
- How planet ownership changes over time (lead: `Campaign\TimelineEvents`)
- Confirm NoFaction and Independent are the owners behind Factionless and Independents
- Exact mission templates available in the base game
- First-planet eligibility rule and retry cooldown
