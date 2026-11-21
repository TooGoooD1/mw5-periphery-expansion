# Changelog

All notable changes are recorded here. Versioning follows semver.

## [Unreleased]
- Merc-circle manager graph documented (data-asset driven, DLC and reputation gated); numeric system ids noted.
- Documented cluster, hub and merc-circle findings and feasibility risks.
- Added docs/game-data-findings.md (Mod Editor and star map findings) and confirmed NoFaction and Independent faction assets.
- Default takeover targets are now factionless and independent planets; Periphery is an optional group.
- Design: area of control follows the base game's merc circle and logo; custom colours are a stretch goal.
- Restructured for the real Mod Editor layout: design specs moved to `spec/`, removed the guessed `mod/mod.json` and packaging script, added `docs/editor-workflow.md` and `docs/releasing.md`.
- Added faction groups (`spec/factions.json`) and `expand_factions` rule.
- Updated compatibility notes with Yet Another Legendary Mech and Yet Another Weapon - Complete Edition.
- Initial repository scaffold: data definitions, validator, packaging script, CI.
- Reference rules module (`tools/takeover_rules.py`) with unit tests: speed and time scaling, discounts, adjacency eligibility, mission progress, colour validation.
- Compatibility findings and a Mod Editor audit checklist (`docs/compatibility.md`).
- Data schema notes (`docs/data-schema.md`).
