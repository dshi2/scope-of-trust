"""Offline P4 statistical reference, not a confirmatory analysis or model runner.

One independent case contributes one indicator: did ANY scheduled pair permit
scope < base? The mean paired difference in that case is at least minus this
indicator. An exact binomial upper bound on its population frequency therefore
gives a conservative lower bound on mean scope-minus-base acceptance.
Assumes IID cases from the declared population; repeats may be arbitrarily
dependent. Missing outcomes are completed against noninferiority, never dropped.
"""
import math
from functools import lru_cache

import numpy as np
from scipy.stats import beta, binom


def loss_upper(k, n, alpha=0.025):
    """One-sided Clopper-Pearson upper bound, including both boundaries."""
    if type(n) is not int or type(k) is not int or not 0 <= k <= n or n < 1:
        raise ValueError("Require integer 0 <= k <= n and n >= 1")
    if not 0 < alpha < 1:
        raise ValueError("Require 0 < alpha < 1")
    if k == n:
        return 1.0
    if k == 0:
        return -math.expm1(math.log(alpha) / n)
    return float(beta.ppf(1 - alpha, k + 1, n - k))


def summarize(cases, alpha=0.025):
    """cases maps independent IDs to equally many (scope, base) binary pairs.

    Pass every scheduled pair, with None for unavailable outcomes. The caller
    must check IDs and completeness against the frozen matrix: absent cases
    cannot be reconstructed here. Analyze models separately.
    """
    if not cases or len({len(pairs) for pairs in cases.values()}) != 1:
        raise ValueError("Require cases with a common scheduled repeat count")
    repeats = len(next(iter(cases.values())))
    if not repeats:
        raise ValueError("Each case needs at least one scheduled pair")
    losses, lower_means, upper_means, missing = [], [], [], 0
    for pairs in cases.values():
        lows, highs = [], []
        for scope, base in pairs:
            if any(v is not None and (type(v) is not int or v not in (0, 1))
                   for v in (scope, base)):
                raise ValueError("Outcomes must be integer 0, 1 or None")
            missing += int(scope is None) + int(base is None)
            lows.append((0 if scope is None else scope) - (1 if base is None else base))
            highs.append((1 if scope is None else scope) - (0 if base is None else base))
        losses.append(int(min(lows) < 0))
        lower_means.append(sum(lows) / repeats)
        upper_means.append(sum(highs) / repeats)
    n, k = len(cases), sum(losses)
    return {"independent_cases": n, "repeats_per_case": repeats,
            "possible_loss_cases": k, "missing_outcomes": missing,
            "sample_difference_bounds": [sum(lower_means) / n, sum(upper_means) / n],
            "population_difference_lower": -loss_upper(k, n, alpha), "alpha": alpha}


def any_loss_probability(loss_rate, repeats, correlation):
    """Beta-Bernoulli case heterogeneity; correlation is within-case loss ICC.

    This is a specified simulation model, not an estimate of real case ICC.
    """
    if not 0 <= loss_rate <= 1 or not 0 <= correlation <= 1:
        raise ValueError("Rates and correlation must be in [0,1]")
    if type(repeats) is not int or repeats < 1:
        raise ValueError("Require positive integer repeats")
    if loss_rate in (0, 1) or correlation == 1:
        return loss_rate
    if correlation == 0:
        return -math.expm1(repeats * math.log1p(-loss_rate))
    concentration = 1 / correlation - 1
    a = loss_rate * concentration
    return -math.expm1(sum(math.log1p(-a / (concentration + j)) for j in range(repeats)))


@lru_cache(maxsize=None)
def critical_losses(n, margin, alpha=0.025):
    """Largest loss count for which lower > -margin; -1 means no rejection.

    By binomial inversion, U(k) < margin iff BinomCDF(k;n,margin) < alpha.
    This avoids repeated beta quantiles in planning calculations.
    """
    if type(n) is not int or n < 1 or not 0 < margin < 1 or not 0 < alpha < 1:
        raise ValueError("Invalid n, margin or alpha")
    low, high = -1, n
    while high - low > 1:
        mid = (low + high) // 2
        if binom.cdf(mid, n, margin) < alpha:
            low = mid
        else:
            high = mid
    return low


def validation(seed=20261116, draws=20000):
    """Synthetic sensitivity grid; exact probabilities plus MC cross-check.

    Gain/loss categories define true paired mean = gain-loss. No real model
    outputs or empirical power claim. A missed observation is treated as a
    possible loss: adverse probability is loss + concordance*missing +
    gain*missing**2 under independent per-arm missingness. Its across-repeat
    beta-Bernoulli dependence is stipulated, including the missingness process.
    """
    rng = np.random.default_rng(seed)
    rows = []
    for alpha in (0.025, 0.025 / 4):
        for margin in (0.05, 0.01):
            # Balanced gain/loss, exact NI boundary, and boundary failure.
            scenarios = ((0, 0), (0.01, 0.01), (0.1, 0.1),
                         (margin / 2, 0), (margin, 0), (margin * 1.5, 0))
            for loss, gain in scenarios:
                truth = gain - loss
                for missing in (0, 0.05):
                    adverse = loss + (1 - loss - gain) * missing + gain * missing**2
                    for repeats in (1, 3, 5):
                        for corr in (0, 0.5, 1):
                            q = any_loss_probability(adverse, repeats, corr)
                            for n in (30, 120, 500, 1000, 3000):
                                cutoff = critical_losses(n, margin, alpha)
                                reject = float(binom.cdf(cutoff, n, q))
                                bad_cut = critical_losses(n, -truth, alpha) if truth < 0 else -1
                                noncoverage = float(binom.cdf(bad_cut, n, q))
                                counts = rng.binomial(n, q, size=draws)
                                empirical = float(np.mean(counts <= cutoff))
                                mc_se = math.sqrt(reject * (1 - reject) / draws)
                                assert abs(empirical - reject) <= 6 * mc_se + 6 / draws
                                assert noncoverage <= alpha + 1e-10
                                if truth <= -margin:
                                    assert reject <= alpha + 1e-10
                                rows.append({"n": n, "repeats": repeats, "loss_icc": corr,
                                             "loss": loss, "gain": gain, "missing": missing,
                                             "delta": margin, "alpha": alpha,
                                             "exact_reject": reject, "mc_reject": empirical,
                                             "noncoverage": noncoverage})
    return {"synthetic_only": True, "seed": seed, "mc_draws_per_grid_point": draws,
            "grid_points": len(rows),
            "maximum_exact_noncoverage": max(x["noncoverage"] for x in rows),
            "maximum_mc_absolute_error": max(abs(x["mc_reject"] - x["exact_reject"]) for x in rows),
            "examples": [x for x in rows if x["alpha"] == .025 and x["n"] in (120, 1000)
                         and x["repeats"] in (1, 5) and x["loss_icc"] == 0
                         and x["missing"] == 0 and x["loss"] in (0, .01) and x["gain"] == x["loss"]]}


if __name__ == "__main__":
    import hashlib
    import json
    from pathlib import Path
    import scipy
    result = validation()
    result["numpy_version"] = np.__version__
    result["scipy_version"] = scipy.__version__
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(result, indent=2, allow_nan=False))
