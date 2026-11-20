# Changelog

All notable changes are recorded here. Versioning follows semver.

## [Unreleased]
- Restructured for the real Mod Editor layout: design specs moved to `spec/`, removed the guessed `mod/mod.json` and packaging script, added `docs/editor-workflow.md` and `docs/releasing.md`.
- Added faction groups (`spec/factions.json`) and `expand_factions` rule.
- Updated compatibility notes with Yet Another Legendary Mech and Yet Another Weapon - Complete Edition.
- Initial repository scaffold: data definitions, validator, packaging script, CI.
- Reference rules module (`tools/takeover_rules.py`) with unit tests: speed and time scaling, discounts, adjacency eligibility, mission progress, colour validation.
- Compatibility findings and a Mod Editor audit checklist (`docs/compatibility.md`).
- Data schema notes (`docs/data-schema.md`).
