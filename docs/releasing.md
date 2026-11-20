# Releasing

1. Update `CHANGELOG.md` and run `python tools/validate.py` and
   `python -m unittest discover -s tests`.
2. In the Mod Editor: Manage Mod, set the Version Num, Load Order (0 by
   default), tick/untick beta, and **Package Mod**.
3. Zip the packaged `PeripheryExpansion` folder from `MW5Mercs\Mods`.
4. Tag the commit (`v0.1.0`) and attach the zip to a GitHub Release.
5. Test in-game with the full mod stack (see `docs/compatibility.md`).
