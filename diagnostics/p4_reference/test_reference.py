import itertools
import math
import unittest

from scipy.stats import binom, binomtest
from reference import any_loss_probability, critical_losses, loss_upper, summarize


class TestReference(unittest.TestCase):
    def test_zero_losses_do_not_give_certainty(self):
        for n in (6, 30, 120, 1000):
            self.assertAlmostEqual(loss_upper(0, n), 1 - .025**(1/n))
            self.assertGreater(loss_upper(0, n), 0)

    def test_binomial_library_crosscheck(self):
        for n in (6, 30, 120):
            for k in (0, 1, n // 2, n):
                expected = binomtest(k, n, alternative="less").proportion_ci(.975).high
                self.assertAlmostEqual(loss_upper(k, n), expected, places=10)

    def test_repeats_do_not_become_cases(self):
        r = summarize({str(i): [(1, 1)] * 5 for i in range(6)})
        self.assertEqual(r["independent_cases"], 6)
        self.assertAlmostEqual(r["population_difference_lower"], -loss_upper(0, 6))

    def test_exhaustive_missing_pair_completions(self):
        for pair in itertools.product((0, 1, None), repeat=2):
            r = summarize({"case": [pair]})
            possible = [s-b for s in (0,1) for b in (0,1)
                        if (pair[0] is None or s == pair[0]) and (pair[1] is None or b == pair[1])]
            self.assertEqual(r["sample_difference_bounds"], [min(possible), max(possible)])
            self.assertEqual(r["possible_loss_cases"], int(min(possible) < 0))

    def test_gains_do_not_cancel_loss_envelope(self):
        r = summarize({"case": [(1, 0), (0, 1)]})
        self.assertEqual(r["sample_difference_bounds"], [0, 0])
        self.assertEqual(r["population_difference_lower"], -1)

    def test_invalid_and_unbalanced_input(self):
        for cases in ({}, {"a": []}, {"a": [(1,1)], "b": [(1,1)]*2},
                      {"a": [(0.5, 1)]}, {"a": [(1, 2)]}):
            with self.assertRaises(ValueError):
                summarize(cases)
        for args in ((-1, 6), (7, 6), (0, 0), (0, 6, 0)):
            with self.assertRaises(ValueError):
                loss_upper(*args)

    def test_repeat_dependence_limits(self):
        self.assertAlmostEqual(any_loss_probability(.1, 5, 0), 1-.9**5)
        self.assertEqual(any_loss_probability(.1, 5, 1), .1)
        for r in (1, 3, 5):
            self.assertEqual(any_loss_probability(0, r, .5), 0)
            self.assertEqual(any_loss_probability(1, r, .5), 1)
        self.assertAlmostEqual(any_loss_probability(.1, 1, .5), .1)

    def test_inversion_and_small_n_exact_coverage(self):
        for n in (6, 30):
            for p in (.001, .01, .05, .1, .5, .95):
                failures = [k for k in range(n+1) if loss_upper(k, n) < p]
                self.assertEqual(critical_losses(n, p), max(failures, default=-1))
                mass = sum(binom.pmf(k, n, p) for k in failures)
                self.assertLessEqual(mass, .025 + 1e-12)


if __name__ == "__main__":
    unittest.main()
