# Design summary

Condensed from the full design document (v0.1). Section numbers match the original.

## 4. Takeover
- Target must be a Periphery faction by default. The game has a `Periphery` faction plus many individual Periphery states (Canopus, Marian Hegemony, Taurian Concordat and others), so "Periphery" is a configurable group (`spec/factions.json`). Other factions can be enabled in options.
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

## 7. Zone and logo
Company logo and zone drawn on controlled planets; perimeter and interior colours are options.
Needs verification of how the base game draws mercenary zones. Leads: the `PlayerFaction` asset and the `RivalMercs` and `ClusterOwners` folders under `Content\Factions`.

## Open items
- Exact mission templates available in the base game
- First-planet eligibility rule
- Retry cooldown after failure
- Final zone default colours
