# Data schema

These are design specs and test fixtures in `spec/`. The game itself reads
Unreal assets built in the Mod Editor (see `editor-workflow.md`); the in-game
logic must match `tools/takeover_rules.py`. All ids use the `PEX_` prefix.

## options.default.json (spec/)
| Key | Meaning |
|---|---|
| maxPlanetsControlled | Cap on planets held (default 5) |
| eligibleFactions | Faction groups or single factions that can be targeted (default groups `Factionless` and `Independent`, see factions.json; `Periphery` can be added) |
| retryCooldownEnabled | Cooldown after a failed mission |
| speedScaling.capMultiplier | Max facility speed (1.25) |
| discount.perPlanetPercent / capPercent | Repair and re-mod discount |
| zone.perimeterColor / interiorColor | Zone colours, `#RRGGBBAA`. Stretch goal: the base game draws merc areas as a fixed dashed circle |

Where the game's options UI is needed, these are exposed through ModOptions
(see compatibility.md); the values above are the defaults.

## modifiers.json
`speedMultiplierByPlanetsHeld`: planets held to speed vs a normal hub
(0.25 up to 1.25). Time taken is the inverse. 5 or more planets use the last entry.

## takeover_chain.json
Five ordered stages. Stage 1 is one light mech, 35 t or less. Stage 5 is a
400 t full planet assault and must point at the hardest existing mission
template (`baseMissionTemplate`, currently a placeholder). Weights must not
decrease and difficulty must strictly increase.

## industries.json
Mech manufacturing, weapon manufacturing and pilot academies. Ownership of
existing planet industries transfers on takeover.

## factions.json
Faction groups used by `eligibleFactions`: `Factionless` (NoFaction), `Independent`,
and a draft `Periphery` group of the individual states seen in the editor's
`Content\Factions` folder. Also records stencil ids observed on faction assets
and leads to inspect.

## Still to define (needs the Mod Editor)
- Planet ids and star-map adjacency taken from the game's own planet data
- Real mission template ids for stages 1 to 5
- Industry ids matching the game's own
