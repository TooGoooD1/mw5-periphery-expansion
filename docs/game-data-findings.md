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

## Clusters and hubs (Content/Campaign/Clusters)
Confirmed (asset details seen in the editor):
- Star systems are identified by **numeric system ids** (for example IndustrialHub_1 holds 911, 1049, 1057, 2131, 2143 and 2145), not by names.
- `IndustrialHub_1_ClusterAsset` is an `MWClusterDataAsset`: Is Legacy Cluster (checked), Priority 0, a Toi Data fragment, a **Cluster Faction Asset** (`RepairSystem_1`), a **Cluster Overlay** (`Safezone_1_Blob`), a **Cluster Constellation** (`Safezone_1`) and a set of **6 System Ids**.
- `RepairSystem_1` is an `MWFactionAsset` named "Safe Zone" ("This is a safe zone."), stencil Abandoned or Independent, Primary colour bright cyan, Secondary and Tertiary empty, wrench logo, no traits.
- `VacantWorlds_ClusterAsset` has the same structure (faction `EmptyWorlds`, overlay `9_2`, no constellation, 6 System Ids). It is a 6-system cluster, so it is probably not a list of all factionless planets.

Hypotheses:
- The teal areas seen around hubs may be cluster overlays drawn with the cluster faction asset's Primary colour (RepairSystem_1's cyan matches). If true, the user's early guess that faction colours affect the map is right for cluster faction assets, though not for ordinary faction paint.
- Hub bonuses (repair cost and time -15%, purchases -15%) probably come from the Toi Data fragment. Not yet inspected.
- A hub is one cluster of several systems, defined as static data. Per-planet clusters created at runtime for planets the player takes may not be possible without custom Blueprint logic.

## Merc circle Blueprints
- `StarMapInfluencers_CIA` (campaign instanced actor asset) auto-spawns `StarMapInfluencerManager` (server spawn).
- `StarMapInfluencerManager` is a Blueprint child of `MWCampaignInstancedActor`, implements the Area Interface (Notify Area Loaded, Notify Area Entered, Notify Unit Spawned) and has `GetStarMapActor`, `IsSetup` and `bHasSpawned`. Event Graph (now readable): on Notify Area Loaded it sets Has Spawned, then branches on an AND of two checks, Is Owned DLC (`DLC.DLC4`) and the merc company's reputation level >= Get Rival Merc Min Rep. If true it gets the Star Map actor, checks it is valid, then runs a For Each loop over **Get Assets by Type** (asset type name starts `MWStarMapRad...`). For each data asset it spawns a `RadialInfluenceActor`, casts to it and calls Initialize with the persistent model. If the area has no star map it just records that nothing spawned.
**Hypothesis:** each merc circle is one data asset of that type, so a mod might add a circle by adding one asset (if mod assets are picked up by Get Assets by Type). The DLC and reputation gate would still apply to our asset unless we spawn our own actor another way.
- `RadialInfluenceActor` is a Blueprint child of the native `MWStarMapRadialInfluence`. It has a radius indicator and a merc icon, and `RemoveIfClanConqueredArea` removes the area when a Clan controls the system, using Get Controlling Faction for Star System with the current date from the timeline model.

## Open questions
1. Where are the planets themselves (owner, position, industries) defined?
2. Can a mod add a RadialInfluenceActor for the player company, and how is the live company logo supplied?
3. What does the Toi Data fragment on a hub cluster contain, and can a mod add new clusters or change which systems a cluster holds at runtime?
3b. What are the fields of the `MWStarMapRad...` data asset (system id, radius, faction or merc company), where are the existing ones, and are mod-added assets picked up by Get Assets by Type?
3c. Is planet ownership a date-driven timeline in the persistent model, and can a mod change it during a campaign?
4. Does the Independent stencil really draw the teal fill?
