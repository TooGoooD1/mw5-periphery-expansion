# Compatibility

Findings from public mod pages and changelogs (Nexus, Steam Workshop). Treat
them as leads: each must be confirmed against the installed copies once the
MW5 Mod Editor is running.

## Target mod stack
| Mod | What we found |
|---|---|
| Yet Another Mechlab (YAML) | Fully unlocked MWO-style mechlab. Most "Yet Another" mods require it. Controls repair and refit cost/time through its equipment properties; has Mechlab Permission Levels and a minimum refit cost multiplier. |
| YAEC-R (Yet Another Equipment Collection Revived) | Continuation of the YAEC/HarJel equipment mod, adjusted to tabletop values. Builds on YAML's equipment property system. |
| Weapon - Complete Edition | Not found in searches. Need the exact mod name and link. |
| Legendary Mech | Not found in searches (a "Yet Another Legendary Mech" is listed as a YAML add-on). Need to confirm which one is installed. |
| ModOptions (Bobbert) | Adds mod settings to the in-game Options menu. Mods register their own settings; values are stored in the game's `Game.ini` under a section named for the mod. |
| MW5 Mod Compatibility Pack | Community package for compatibility between mods. Its default load order sits below mods that depend on it, and it should load before them. It ships a modder's guide and source assets for integration. |

## Key constraints
1. **No merging.** MW5 does not merge overridden assets; if two mods touch the same file, the one with the higher load order wins. So we never override base-game or other mods' files.
2. **Load order is fragile.** YAML-family mods ship carefully chosen default load orders, and a reported YAML conflict was fixed only by working through file conflicts. We keep a unique `PEX_` prefix and a moderate default load order (`mod.json` is currently 100; to be confirmed).
3. **YAML owns refit/repair math.** Because YAML computes repair and refit cost and time itself, our speed and discount modifiers must be applied as multipliers on top of its result through our own hook, not by replacing its tables.
4. **Options.** Register our options through ModOptions rather than a custom menu, with the default values in `options.default.json` as fallback. The Compatibility Pack's modder's guide also covers adding settings.
5. **Replacement mods.** Some YAML-family mods are meant to replace each other (for example Yet Another Revamped Weapon replaces Yet Another Weapon rather than sitting beside it). We make no assumptions about which of these the player runs.

## Audit checklist (once the Mod Editor is installed)
- [ ] Read the Mod Editor Guide (v2) from Piranha's docs: porting a mod to the new framework, and compatibility of mods made in v1.
- [ ] Open YAML, YAEC-R, Legendary Mech and Weapon CE pak/manifest data; list every asset touching repair, refit, market, mission or planet data.
- [ ] Record overlaps with `PEX_` files and how each is avoided.
- [ ] Find how YAML exposes repair/refit cost and time so our multipliers can hook in.
- [ ] Check how the Compatibility Pack integrates new mods, and whether PEX needs registering.
- [ ] Confirm the ModOptions registration format and where values are stored.
- [ ] Confirm the exact names of "Weapon - Complete Edition" and "Legendary Mech".

## Test matrix
Vanilla, vanilla + YAML, YAML + each other mod individually, then the full stack
(YAML, YAEC-R, Legendary Mech, Weapon CE, ModOptions, Compatibility Pack).
