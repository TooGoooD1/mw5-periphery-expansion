# Game data findings (Mod Editor and in-game star map)

Everything here comes from screenshots of the MW5 Mod Editor (UE 4.26) and the
in-game star map. "Confirmed" means seen directly; "Hypothesis" means inferred
from names and not yet tested.

## Faction assets (Content/Factions)
| Asset | Type | Name shown | Star Map Stencil Id |
|---|---|---|---|
| NoFaction | FactionType.Briefing | Factionless | None |
| Independent | FactionType.Faction | Independents | Abandoned or Independent |
| Periphery | FactionType.Faction | Periphery Realms | Periphery |
| TaurianConcordat | (faction) | Taurian Concordat | Periphery |
| WolfsDragoons | FactionType.Mercenary | Wolf's Dragoons | Abandoned or Independent |
| PlayerFaction | FactionType.Briefing | Nik's Cavaliers (default) | Periphery |

Confirmed:
- Stencil Id is a fixed dropdown: None, Capellan Confederation, Draconis Combine, Federated Commonwealth, Free Rasalhague Republic, Federated Suns, Free Worlds League, Lyran Commonwealth, Com Star, Periphery, Abandoned or Independent.
- Paint Theme and Primary/Secondary/Tertiary are mech paint scheme colours, not star-map colours.
- PlayerFaction is only the default starting company; the player renames it and picks a logo in-game, so live data is elsewhere (save or runtime).

## Star map (in game)
Confirmed:
- Houses, Clans and Com Star have a coloured territory fill with a border.
- Periphery states and Factionless planets have no fill. Independent-owned and merc-owned planets (for example Outreach) sit in a teal area, which matches the shared "Abandoned or Independent" stencil (hypothesis for the colour link).
- Merc companies have a dashed circle centred on a planet with the company logo.
- Selecting a planet shows an overlay with its owner; hubs show bonuses (for example repair cost and repair time -15% at Mercenary's Star).

## Content/Campaign
- `TimelineEvents`: random event types (Finance, MechRefit, MechTraitsRefit, Mission, PilotRecovery, PilotTraining, PreTravelBriefing, Travel). These are NOT planet ownership.
- `RivalMercs`: DashedCircle material and instance, MF_DashedCircleSDF, RadialInfluenceActor, RadialInfluenceIcon materials, StarMapInfluencerManager, StarMapInfluencers_CIA, MercFriendly/Hostile encounter assets. **Hypothesis:** this is how merc circles are drawn, and our company circle could reuse the same actor.
- `Clusters`: 79 folders, including IndustrialHub_1 to _31, Outreach, MercenaryRow, VacantWorlds, Rogue, PiratesLair and border zones. **Hypothesis:** hubs and their bonuses are defined here; VacantWorlds may list unowned planets.
- `Areas`: only EmptyArea; not planet data.

## StarMap assets (search "StarMap", 212 items)
- StarMapBorderActor per year (3015, 3025, 3029 to 3060, including 3050 waves and 3059/3060 events) and BorderDAVION/KURITA/LIAO/MARIK/STEINER pieces: territory borders appear to be authored per date.
- Enable/Disable/Lock StarMap ArcActions: story arcs switch map features on and off.
- StarMapInfluencerManager and StarMapInfluencers_CIA: see RivalMercs.

## Open questions
1. Where are the planets themselves (owner, position, industries) defined?
2. Can a mod add a RadialInfluenceActor for the player company, and how is the live company logo supplied?
3. How do industrial hubs in `Clusters` apply their bonuses, and can a mod add new ones?
4. Does the Independent stencil really draw the teal fill?
