"""Offline tests for P4 audit reference; these are not empirical model results."""
import math
import unittest

from p4_bound_reference import Arm, CasePair, reference_lower_bound


def pair(i, *, e=(1, 1, 1), scoped=(1, 1, 1), model="m1"):
    return CasePair(str(i), model, Arm(*e), Arm(*scoped))


class P4ReferenceTests(unittest.TestCase):
    def test_ceiling_is_not_zero_width(self):
        r = reference_lower_bound([pair(i) for i in range(100)], alpha=.025, margin=.05)
        self.assertEqual(r["identification_interval"], (0.0, 0.0))
        self.assertLess(r["one_sided_lower"], -.05)
        self.assertFalse(r["noninferiority_supported"])

    def test_large_independent_ceiling_can_pass(self):
        r = reference_lower_bound([pair(i) for i in range(5000)], alpha=.025, margin=.05)
        self.assertGreater(r["one_sided_lower"], -.05)
        self.assertTrue(r["noninferiority_supported"])
        self.assertEqual(r["n_independent_cases"], 5000)

    def test_paired_sign_is_scope_minus_e(self):
        r = reference_lower_bound(
            [pair(i, e=(1, 1, 1), scoped=(1, 1, 0)) for i in range(10)],
            alpha=.025, margin=.05)
        self.assertEqual(r["identification_interval"], (-1.0, -1.0))
        self.assertFalse(r["noninferiority_supported"])

    def test_missing_all_outcomes_keeps_full_identification_range(self):
        r = reference_lower_bound(
            [pair(i, e=(2, 0, 0), scoped=(2, 0, 0)) for i in range(50)],
            alpha=.025, margin=.05)
        self.assertEqual(r["identification_interval"], (-1.0, 1.0))
        self.assertEqual(r["n_unscored_repeats"], 200)
        self.assertFalse(r["noninferiority_supported"])

    def test_partial_missingness_is_mnar_safe(self):
        r = reference_lower_bound(
            [pair(i, e=(4, 4, 3), scoped=(4, 2, 2)) for i in range(20)],
            alpha=.025, margin=.05)
        self.assertAlmostEqual(r["identification_interval"][0], -.25)
        self.assertAlmostEqual(r["identification_interval"][1], .25)
        self.assertEqual(r["n_unscored_repeats"], 40)

    def test_one_sided_missing_arm_does_not_automatically_lose(self):
        r = reference_lower_bound(
            [pair(i, e=(1, 0, 0), scoped=(1, 1, 1)) for i in range(100)],
            alpha=.025, margin=.05)
        self.assertEqual(r["identification_interval"], (0.0, 1.0))

    def test_repeats_do_not_inflate_case_n(self):
        r = reference_lower_bound(
            [pair(i, e=(200, 200, 200), scoped=(200, 200, 200)) for i in range(5)],
            alpha=.025, margin=.05)
        self.assertEqual(r["n_independent_cases"], 5)
        self.assertGreater(r["radius"], 1)

    def test_duplicate_case_or_mixed_model_rejected(self):
        with self.assertRaises(ValueError):
            reference_lower_bound([pair(1), pair(1)], alpha=.025, margin=.05)
        with self.assertRaises(ValueError):
            reference_lower_bound([pair(1), pair(2, model="m2")], alpha=.025, margin=.05)

    def test_bad_counts_and_settings_rejected(self):
        for arm in (Arm(0, 0, 0), Arm(1, 2, 1), Arm(1, 1, -1),
                    Arm(2, 1, 2), Arm(True, 1, 1)):
            with self.subTest(arm=arm), self.assertRaises(ValueError):
                arm.bounds()
        with self.assertRaises(ValueError):
            reference_lower_bound([], alpha=.025, margin=.05)
        with self.assertRaises(ValueError):
            reference_lower_bound([pair(0)], alpha=0, margin=.05)

    def test_radius_formula(self):
        n = 200
        r = reference_lower_bound([pair(i) for i in range(n)], alpha=.025, margin=.05)
        self.assertAlmostEqual(r["radius"], math.sqrt(2 * math.log(40) / n))


if __name__ == "__main__":
    unittest.main()
