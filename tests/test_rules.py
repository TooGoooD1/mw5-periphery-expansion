import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import takeover_rules as r  # noqa: E402

MODS = json.loads((ROOT / "spec/modifiers.json").read_text())
TABLE, CAP = MODS["speedMultiplierByPlanetsHeld"], MODS["capMultiplier"]
OPTS = json.loads((ROOT / "spec/options.default.json").read_text())

# Placeholder star map: A-B-C-D in a line, E is off on its own.
ADJ = {"A": ["B"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C"], "E": []}
FACTIONS = {"A": "Periphery", "B": "Periphery", "C": "Periphery",
            "D": "Inner Sphere", "E": "Periphery"}


class SpeedTests(unittest.TestCase):
    def test_table_steps(self):
        expected = {1: 0.25, 2: 0.5, 3: 0.75, 4: 1.0, 5: 1.25}
        for n, speed in expected.items():
            self.assertEqual(r.speed_multiplier(n, TABLE, CAP), speed)

    def test_five_or_more_is_capped(self):
        self.assertEqual(r.speed_multiplier(9, TABLE, CAP), 1.25)

    def test_cap_wins_over_table(self):
        self.assertEqual(r.speed_multiplier(5, TABLE, 1.0), 1.0)

    def test_no_planets_no_effect(self):
        self.assertIsNone(r.speed_multiplier(0, TABLE, CAP))

    def test_time_is_inverse(self):
        self.assertEqual(r.time_multiplier(1, TABLE, CAP), 4.0)
        self.assertAlmostEqual(r.time_multiplier(5, TABLE, CAP), 0.8)


class DiscountTests(unittest.TestCase):
    def test_discount_scales_and_caps(self):
        d = OPTS["discount"]
        self.assertEqual(r.discount_percent(1, d["perPlanetPercent"], d["capPercent"]), 10)
        self.assertEqual(r.discount_percent(3, d["perPlanetPercent"], d["capPercent"]), 30)
        self.assertEqual(r.discount_percent(5, d["perPlanetPercent"], d["capPercent"]), 40)
        self.assertEqual(r.discount_percent(0, 10, 40), 0)


class EligibilityTests(unittest.TestCase):
    def targets(self, owned, **kw):
        args = dict(adjacency=ADJ, planet_factions=FACTIONS,
                    eligible_factions=["Periphery"], max_planets=5)
        args.update(kw)
        return r.eligible_targets(owned, **args)

    def test_adjacent_and_periphery_only(self):
        self.assertEqual(self.targets(["A"]), ["B"])
        self.assertEqual(self.targets(["B"]), ["A", "C"])

    def test_non_periphery_excluded_until_enabled(self):
        self.assertEqual(self.targets(["C"]), ["B"])
        self.assertEqual(
            self.targets(["C"], eligible_factions=["Periphery", "Inner Sphere"]),
            ["B", "D"])

    def test_cap_blocks_new_targets(self):
        self.assertEqual(self.targets(["A"], max_planets=1), [])

    def test_campaign_in_progress_blocks(self):
        self.assertEqual(self.targets(["A"], campaign_in_progress=True), [])

    def test_isolated_planet_not_reachable(self):
        self.assertNotIn("E", self.targets(["A", "B", "C"]))

    def test_first_planet_any_eligible(self):
        self.assertEqual(self.targets([]), ["A", "B", "C", "E"])


GROUPS = json.loads((ROOT / "spec/factions.json").read_text())["factionGroups"]


class FactionGroupTests(unittest.TestCase):
    def test_periphery_group_expands(self):
        out = r.expand_factions(["Periphery"], GROUPS)
        self.assertIn("Periphery", out)
        self.assertIn("MagistracyOfCanopus", out)
        self.assertGreater(len(out), 5)

    def test_plain_names_pass_through(self):
        self.assertEqual(r.expand_factions(["Pirate"], GROUPS), ["Pirate"])

    def test_mixed(self):
        out = r.expand_factions(["Pirate", "Periphery"], GROUPS)
        self.assertIn("Pirate", out)
        self.assertIn("TaurianConcordat", out)


class ChainTests(unittest.TestCase):
    def test_next_stage(self):
        self.assertEqual(r.next_stage(0), 1)
        self.assertEqual(r.next_stage(4), 5)
        self.assertIsNone(r.next_stage(5))

    def test_chain_file_matches_length(self):
        chain = json.loads((ROOT / "spec/takeover_chain.json").read_text())
        self.assertEqual(len(chain["stages"]), r.CHAIN_LENGTH)


class ColorTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(r.valid_color("#FFB000FF"))
        self.assertTrue(r.valid_color("#ffb00040"))

    def test_invalid(self):
        for bad in ["#FFB000", "FFB000FF", "#GGGGGGGG", "", None, 5]:
            self.assertFalse(r.valid_color(bad))

    def test_defaults_are_valid(self):
        self.assertTrue(r.valid_color(OPTS["zone"]["perimeterColor"]))
        self.assertTrue(r.valid_color(OPTS["zone"]["interiorColor"]))


if __name__ == "__main__":
    unittest.main()
