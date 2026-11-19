# Periphery Expansion (MechWarrior 5: Mercenaries mod)

Conquer Periphery planets with your mercenary company through a five-mission
campaign per planet, then run them as a power base: mech and weapon
manufacturing, pilot academies, repair and re-mod discounts, and a visible
zone of control on the star map.

> **Status: pre-alpha scaffold.** Data definitions and tooling exist; the
> Blueprint/UI work (industries page, star-map overlay, options menu) has not
> been started. It requires the MechWarrior 5 Mod Editor (UE 4.26 build,
> via the Epic Games Launcher). Unreal Engine 5.x cannot be used.

## Features (planned)

- Take over adjacent Periphery planets (other factions selectable in options)
- Five escalating missions per planet: 35-ton recon up to a 400-ton assault
- Up to 5 planets by default (configurable)
- Industries page: mech manufacturing, weapon manufacturing, pilot academies
- Existing industries transfer to you on takeover
- Repair, re-mod and build time scale with planets held: 0.25x at 1 planet up to 1.25x at 5+
- Company logo and zone of control on the star map, perimeter and interior colours configurable

## Compatibility

Designed to sit alongside Yet Another MechLab, YAEC-R, Legendary Mech,
Weapon - Complete Edition, ModOptions and the MW5 Mod Compatibility pack.
The mod is additive: it uses a unique `PEX_` prefix and does not replace
other mods' files. See `docs/compatibility.md`.

## Repository layout

```
mod/            Mod package contents (mod.json + data)
  data/         options, modifiers, takeover chain, industries
docs/           design and compatibility notes
tools/          validate.py (data checks), package.py (zip for release)
scripts/        helper scripts for first-time git setup
.github/        CI workflow that runs the validator
```

## Development

```
python tools/validate.py      # check data files
python tools/package.py       # build dist/PeripheryExpansion-<version>.zip
```

Python 3.8+ with the standard library only; no third-party packages needed.

## Contributing and license

See `CONTRIBUTING.md`. Released under the MIT License (`LICENSE`).
Third-party material is listed in `THIRD_PARTY.md`.

MechWarrior, BattleTech and related names belong to their respective owners.
This is an unofficial fan project, not affiliated with Piranha Games or
Microsoft.
