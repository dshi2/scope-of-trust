"""Interval methods and simulator (spec §6, §9): boundary behaviour, known-null and known-effect
recovery, cluster handling, determinism. Stdlib only."""
import math
import random
import unittest
from statistics import NormalDist

from p2v3 import stats
from p2v3.simulate import cells, expit, intercept, rng_for, seed_for, simulate, _Q

Z = NormalDist().inv_cdf(0.975)


def summ(data):
    return stats.summarize(cells(data))


class TestBoundary(unittest.TestCase):
    def test_all_ones_both_arms_is_not_degenerate(self):
        for n in (30, 120, 1000):
            for r in (1, 5):
                s = summ([([1] * r, [1] * r) for _ in range(n)])
                for m in ("tango", "tango_c"):
                    lo, hi = stats.METHODS[m](s)
                    self.assertAlmostEqual(lo, -Z * Z / (n + Z * Z), places=9)  # closed form at b = c = 0
                    self.assertLess(lo, 0)
                    self.assertGreater(hi, 0)
                for m in ("tango_cc", "tango_c_cc"):  # continuity correction only widens
                    lo, hi = stats.METHODS[m](s)
                    self.assertLess(lo, -Z * Z / (n + Z * Z))
                    self.assertGreater(hi, Z * Z / (n + Z * Z))
                self.assertLess(stats.bayes(s)[0], 0)

    def test_all_zeros_mirror_all_ones(self):
        ones = stats.tango(summ([([1], [1])] * 60))
        zeros = stats.tango(summ([([0], [0])] * 60))
        self.assertAlmostEqual(ones[0], zeros[0])
        self.assertAlmostEqual(ones[1], zeros[1])

    def test_wald_collapses_where_score_does_not(self):
        s = summ([([1], [1])] * 120)
        self.assertEqual(stats.wald(s), (0.0, 0.0))  # the false certainty the spec rules out

    def test_repeats_do_not_become_cases(self):
        one = stats.METHODS["tango_c"](summ([([1], [1])] * 40))
        five = stats.METHODS["tango_c"](summ([([1] * 5, [1] * 5)] * 40))
        self.assertAlmostEqual(one[0], five[0])

    def test_arm_symmetry(self):
        data = [([1, 0, 1], [1, 1, 1])] * 7 + [([1, 1, 1], [1, 1, 1])] * 50 + [([1, 1, 0], [0, 1, 1])] * 3
        swapped = [(y, x) for x, y in data]
        for m in ("tango", "tango_cc", "tango_c", "tango_c_cc", "wald"):
            lo, hi = stats.METHODS[m](summ(data))
            lo2, hi2 = stats.METHODS[m](summ(swapped))
            self.assertAlmostEqual(lo, -hi2)
            self.assertAlmostEqual(hi, -lo2)


class TestFormulas(unittest.TestCase):
    def test_tango_restricted_mle(self):
        """The closed-form restricted MLE of the p01 cell maximises the constrained likelihood."""
        b, c, n = 7, 12, 90
        for d0 in (-0.15, -0.05, 0.0, 0.04):
            s = stats.Summary(K=n, b=b, c=c, n11=n - b - c, sdd=b + c, inv_m=1.0, dropped=0)
            z = stats.tango_z(s, d0)
            ll = lambda x: b * math.log(x + d0) + c * math.log(x) + (n - b - c) * math.log(1 - 2 * x - d0)
            grid = [i / 200000 for i in range(1, 100000) if i / 200000 + d0 > 0 and 1 - 2 * i / 200000 - d0 > 0]
            x = max(grid, key=ll)
            zz = (b - c - n * d0) / math.sqrt(n * (2 * x + d0 - d0 * d0))
            self.assertAlmostEqual(z, zz, places=3)

    def test_bound_is_root_of_score(self):
        s = summ([([1], [0])] * 4 + [([0], [1])] * 9 + [([1], [1])] * 80)
        lo, hi = stats.tango(s)
        self.assertAlmostEqual(stats.tango_z(s, lo), Z, places=6)
        self.assertAlmostEqual(stats.tango_z(s, hi), -Z, places=6)

    def test_design_effect_limits(self):
        clustered = summ([([0] * 4, [1] * 4)] * 3 + [([1] * 4, [1] * 4)] * 37)
        self.assertAlmostEqual(stats.design_effect(clustered), 1.0)  # repeats add nothing
        spread = summ([([0, 1, 1, 1], [1, 1, 1, 1])] * 12 + [([1] * 4, [1] * 4)] * 28)
        self.assertAlmostEqual(stats.design_effect(spread), 0.25)  # as if repeats were independent

    def test_cases_weighted_equally_not_by_complete_pairs(self):
        """Known effect with unequal complete pairs per case: case 1 has one complete pair (a loss),
        case 2 has five (no change). Equal-case D = (-1 + 0) / 2; the pooled-pair ratio would be -1/6."""
        data = [([0, None, None, None, None], [1, 1, 1, 1, 1]), ([1] * 5, [1] * 5)]
        c = cells(data)
        ratio = sum(n10 - n01 for _, n10, n01, _ in c) / sum(map(sum, c))
        self.assertAlmostEqual(ratio, -1 / 6)
        self.assertAlmostEqual(stats.estimate(stats.summarize(c)), -0.5)
        # a wholly missing case stays visible, and enters the scheduled-denominator bound
        c3 = c + cells([([None] * 5, [1] * 5)])
        self.assertEqual(stats.summarize(c3).dropped, 1)
        worst = stats.summarize(cells(data + [([None] * 5, [1] * 5)], fill=(0, 1)))
        self.assertEqual((worst.K, worst.dropped), (3, 0))
        self.assertAlmostEqual(stats.estimate(worst), (-1 + 0 - 1) / 3)

    def test_missing_pairs_dropped_or_bounded(self):
        x, y = [1, None, 0, 1], [1, 1, None, 0]
        self.assertEqual(stats.pair_counts(x, y), (1, 1, 0, 0))
        self.assertEqual(stats.pair_counts(x, y, fill=(0, 1)), (1, 1, 2, 0))  # worst case for x - y
        self.assertEqual(stats.pair_counts(x, y, fill=(1, 0)), (2, 1, 0, 1))

    def test_bayes_matches_monte_carlo_posterior(self):
        s = summ([([1], [0])] * 3 + [([0], [1])] * 8 + [([1], [1])] * 100)
        rng = random.Random(7)
        draws = []
        for _ in range(40000):
            g = [rng.gammavariate(a, 1) for a in (s.b + 0.5, s.c + 0.5, s.K - s.b - s.c + 1)]
            draws.append((g[0] - g[1]) / sum(g))
        draws.sort()
        self.assertAlmostEqual(stats.bayes(s)[0], draws[int(0.025 * len(draws))], delta=0.004)

    def test_marginal_calibration(self):
        for p in (0.05, 0.9, 0.99):
            mu = intercept(p, 1.5)
            self.assertAlmostEqual(sum(expit(mu + 1.5 * q) for q in _Q) / len(_Q), p, places=6)
        self.assertEqual(intercept(1.0, 0.5), math.inf)


class TestRecovery(unittest.TestCase):
    def test_known_null(self):
        rng = rng_for(1, "null")
        hits = 0
        for _ in range(200):
            lo, hi = stats.METHODS["tango_c"](summ(simulate(rng, 120, 3, [(0.9, 0.9)], 0.5)))
            hits += lo <= 0 <= hi
        self.assertGreaterEqual(hits / 200, 0.92)

    def test_known_effect(self):
        rng = rng_for(1, "effect")
        s = summ(simulate(rng, 400, 3, [(0.7, 0.9)], 0.5, 0.05, "arm"))
        lo, hi = stats.METHODS["tango_c"](s)
        self.assertLess(hi, 0)
        self.assertLess(lo, -0.2)
        self.assertGreater(hi, -0.2)
        self.assertAlmostEqual(stats.estimate(s), -0.2, delta=0.04)

    def test_noninferiority_decided_only_with_enough_cases(self):
        perfect = lambda n: stats.METHODS["tango_c"](summ([([1], [1])] * n))[0]
        self.assertLess(perfect(72), -0.05)
        self.assertGreater(perfect(74), -0.05)  # n > z^2 (1 - delta) / delta = 72.99


class TestDeterminism(unittest.TestCase):
    def test_seed_is_stable(self):
        self.assertEqual(seed_for(20261116, "grid", (0.95, -0.05)), seed_for(20261116, "grid", (0.95, -0.05)))
        self.assertEqual(seed_for("x"), 10946750079282925220)  # FNV-1a, independent of PYTHONHASHSEED

    def test_same_seed_same_data(self):
        a = simulate(rng_for(5, "k"), 50, 3, [(0.95, 1.0), (0.8, 0.9)], 1.5, 0.05, "mcar")
        b = simulate(rng_for(5, "k"), 50, 3, [(0.95, 1.0), (0.8, 0.9)], 1.5, 0.05, "mcar")
        self.assertEqual(a, b)
        self.assertEqual(len(a[0][0]), 6)  # two models x three repeats, concatenated per case


if __name__ == "__main__":
    unittest.main()
