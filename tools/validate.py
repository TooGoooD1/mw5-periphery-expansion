#!/usr/bin/env python3
"""Validate Periphery Expansion data files. Standard library only."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import takeover_rules  # noqa: E402

errors = []


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON ({exc})")
        return None


def check(cond, msg):
    if not cond:
        errors.append(msg)


for p in sorted((ROOT / "mod").rglob("*.json")):
    load(p)

chain = load(ROOT / "mod/data/takeover_chain.json")
if chain:
    stages = chain.get("stages", [])
    check(len(stages) == 5, "takeover chain must have exactly 5 stages")
    if len(stages) == 5:
        weights = [s.get("weightLimitTons", 0) for s in stages]
        diffs = [s.get("difficulty", 0) for s in stages]
        check(stages[0].get("maxMechs") == 1, "stage 1 must allow exactly 1 mech")
        check(weights[0] <= 35, "stage 1 weight limit must be 35 tons or less")
        check(weights[-1] == 400, "stage 5 weight limit must be 400 tons")
        check(weights == sorted(weights), "weight limits must not decrease")
        check(diffs == sorted(diffs) and len(set(diffs)) == 5,
              "difficulty must strictly increase")
        check([s.get("order") for s in stages] == [1, 2, 3, 4, 5],
              "stage order must be 1..5")

mods = load(ROOT / "mod/data/modifiers.json")
if mods:
    table = mods.get("speedMultiplierByPlanetsHeld", {})
    cap = mods.get("capMultiplier", 0)
    vals = [table[k] for k in sorted(table, key=int)]
    check(bool(vals) and vals == sorted(vals), "speed multipliers must not decrease")
    check(bool(vals) and vals[0] == 0.25, "1 planet must be 0.25x")
    check(bool(vals) and max(vals) <= cap, "speed table exceeds capMultiplier")
    check(cap <= 1.25, "capMultiplier must not exceed 1.25")

opts = load(ROOT / "mod/data/options.default.json")
if opts:
    check(opts.get("maxPlanetsControlled", 0) >= 1, "maxPlanetsControlled must be >= 1")
    check(opts.get("speedScaling", {}).get("capMultiplier", 0) <= 1.25,
          "option capMultiplier must not exceed 1.25")
    zone = opts.get("zone", {})
    check(takeover_rules.valid_color(zone.get("perimeterColor")),
          "zone.perimeterColor must be #RRGGBBAA")
    check(takeover_rules.valid_color(zone.get("interiorColor")),
          "zone.interiorColor must be #RRGGBBAA")

if errors:
    print("Validation failed:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("All checks passed.")
