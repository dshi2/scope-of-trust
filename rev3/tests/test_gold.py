"""Derived gold labels must match the hand table in REVISION_3_SPEC.md §5."""
import unittest

from p2v3 import render as r
from p2v3.gold import F, NE, T, belief_gold, gold

# Hand table: primary label per claim (spec §5). Independent of gold.py's rules.
HAND = {
    "A":       {"P": NE, "Q_obs": NE, "Q_welfare": NE, "Q_cause": NE, "R": NE, "S": NE},
    "A0":      {"Q_obs": NE, "Q_welfare": NE, "Q_cause": NE, "R": NE, "S": NE},
    "B":       {"P": T, "Q_obs": NE, "Q_welfare": NE, "Q_cause": NE, "R": NE, "S": NE},
    "C":       {"P": T, "Q_obs": NE, "Q_welfare": NE, "Q_cause": NE, "R": NE, "S": NE},
    "C_prime": {"P": T, "Q_obs": NE, "Q_welfare": NE, "Q_cause": NE, "R": NE, "S": NE},
    "D1":      {"P": NE, "Q_obs": NE, "Q_welfare": NE, "Q_cause": NE, "R": T, "S": NE},
    "D2":      {"P": NE, "Q_obs": NE, "Q_welfare": NE, "Q_cause": NE, "R": NE, "S": T},
    "V":       {"P": NE, "Q_obs": NE, "Q_welfare": NE, "Q_cause": NE, "R": NE, "S": NE},
}
for _c in r.E_FAMILY:
    HAND[(_c, "improved")] = {"P": NE, "Q_obs": T, "Q_welfare": NE, "Q_cause": NE, "R": NE, "S": NE}
    HAND[(_c, "worsened")] = {"P": NE, "Q_obs": F, "Q_welfare": NE, "Q_cause": NE, "R": NE, "S": NE}
    HAND[(_c, "unchanged")] = {"P": NE, "Q_obs": F, "Q_welfare": NE, "Q_cause": NE, "R": NE, "S": NE}

BELIEF = {"A": 0.65, "D1": 0.65, "D2": 0.65, "B": 0.75, "C": 0.75, "C_prime": 0.75, "A0": 0.5, "V": None}


class TestGold(unittest.TestCase):
    def test_matches_hand_table(self):
        for c, d in r.cells():
            hand = HAND[(c, d)] if c in r.E_FAMILY else HAND[c]
            g = gold(c, d)
            self.assertEqual(set(g), set(r.claim_ids(c)), c)
            self.assertEqual({k: v["label"] for k, v in g.items()}, hand, f"{c} {d}")
            for k, v in g.items():
                self.assertIn(v["label"], v["accept"])
                self.assertTrue(v["why"])

    def test_welfare_and_cause_never_established_true(self):
        for c, d in r.cells():
            g = gold(c, d)
            self.assertNotIn(T, g["Q_welfare"]["accept"])
            self.assertNotIn(T, g["Q_cause"]["accept"])

    def test_two_member_sets_only_for_q_cause_failed_presupposition(self):
        for c, d in r.cells():
            for k, v in gold(c, d).items():
                if len(v["accept"]) > 1:
                    self.assertIn(c, r.E_FAMILY)
                    self.assertIn(d, ("worsened", "unchanged"))
                    self.assertEqual(v["accept"], {NE, F})
                    self.assertEqual(k, "Q_cause")

    def test_belief_gold(self):
        for c, d in r.cells():
            if c in r.E_FAMILY:
                self.assertEqual(belief_gold(c, d), 1.0 if d == "improved" else 0.0)
            else:
                self.assertEqual(belief_gold(c, d), BELIEF[c], c)


if __name__ == "__main__":
    unittest.main()
