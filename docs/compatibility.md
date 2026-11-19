# Compatibility

## Target mod stack
- Yet Another MechLab (YAML)
- YAEC-R (Yet Another Equipment Collection Revived)
- Legendary Mech
- Weapon - Complete Edition
- ModOptions (used for in-game option menus)
- MW5 Mod Compatibility pack

## Rules
1. Additive only: new files under the `PEX_` prefix; never replace others' files.
2. Hook repair, re-mod and build timing through mod-owned entries, not by overriding shared tables.
3. Declare soft dependencies and document load order in the README.
4. Options are exposed through ModOptions where possible, with a config-file fallback.

## Audit checklist (to do once the Mod Editor is installed)
- [ ] List every file YAML, YAEC-R, Legendary Mech and Weapon CE override or add that touches repair, re-mod, build time, mission or planet data.
- [ ] Record overlaps with this mod's files and how each is avoided.
- [ ] Check how the Compatibility pack merges data, and whether PEX entries need registering with it.
- [ ] Confirm the ModOptions registration format.

## Test matrix
Vanilla, vanilla + YAML, YAML + each other mod individually, then the full stack.
