#!/usr/bin/env python3
"""Zip the mod/ folder into dist/PeripheryExpansion-<version>.zip."""
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
mod_dir = ROOT / "mod"
version = json.loads((mod_dir / "mod.json").read_text(encoding="utf-8"))["version"]
out = ROOT / "dist" / f"PeripheryExpansion-{version}.zip"
out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(mod_dir.rglob("*")):
        if f.is_file():
            z.write(f, Path("PeripheryExpansion") / f.relative_to(mod_dir))
print(f"Wrote {out}")
