# Mod Editor workflow

Based on Piranha Games' Mod Editor Guide (v2). Confirmed against the folder
the editor actually created.

## How the mod is structured
The editor creates `MW5Mercs\Plugins\PeripheryExpansion\` containing:
- `Content\` : **new** assets (nothing that replaces a base-game asset)
- `ModOverride\` : modified copies of base-game assets, in the same folder
  structure as the original (for example `ModOverride\Objects\Weapons\Gauss\...`)
- `Config\`, `Resources\`, `ActiveMod.txt`, `PeripheryExpansion.uplugin` : editor files

The game reads Unreal assets, not our JSON files. The files in `spec/` are
design specs and test fixtures; the real implementation is built from assets
in `Content` and `ModOverride`.

## Editing a base-game asset
Open it in the Content Browser, click **Save To Mod**, and edit the copy that
lands in `ModOverride`. Never edit the original. Only override what we must.

## Packaging and testing
1. Click **Manage Mod**, set Version Num and Load Order (keep 0 unless the mod
   must work in relation to another mod), then **Package Mod**.
2. The default output is `<Mod Editor>\MW5Mercs\Mods`.
3. Copy the packaged folder into the game's `Mods` folder, enable it in the
   in-game Mods screen, apply, and restart the game.
4. The packaged `mod.json` has a `loadOrder` line players can edit.

## Version control
Piranha recommends version control. The plan: move the plugin folder into
`mod/PeripheryExpansion` in this repo and leave a Windows directory junction at
the old location so the editor still finds it:

```
move "D:\\Program Files\\Epic Games\\MechWarrior5Editor\\MW5Mercs\\Plugins\\PeripheryExpansion" "<repo>\\mod\\PeripheryExpansion"
mklink /J "D:\\Program Files\\Epic Games\\MechWarrior5Editor\\MW5Mercs\\Plugins\\PeripheryExpansion" "<repo>\\mod\\PeripheryExpansion"
```

Close the Mod Editor first. Use the folder where GitHub Desktop keeps the repo
in place of `<repo>`.
