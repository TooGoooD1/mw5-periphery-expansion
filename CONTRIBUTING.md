# Contributing

- Branches: `main` is stable, `develop` is active work, one feature branch per system.
- Run `python tools/validate.py` before opening a pull request.
- Keep every new asset and data id under the `PEX_` prefix.
- Never edit or override base-game files or other mods' files; hook in additively.
- Large Unreal binaries go through Git LFS (`git lfs install`).
- Only add open-source libraries with MIT-compatible licenses and list them in `THIRD_PARTY.md`.
