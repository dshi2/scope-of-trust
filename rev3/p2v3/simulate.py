"""Simulator of the paired case x condition design (spec §6, §9). Stdlib only; no model calls.

Generative model for one contrast (arms X and Y, e.g. E_scope and E), per model j and case i:
  u_i ~ N(0, sd^2)                     case-level logit random effect, shared by both arms and all models
  y_ijak ~ Bernoulli(expit(mu_ja + u_i)), repeats k = 1..r nested in cases
  mu_ja is calibrated so the *marginal* rate E[expit(mu_ja + u)] equals the target rate exactly, so
  the true Delta = mean over models of (p_jX - p_jY) at every sd. Rates 0 and 1 are exact floors/ceilings.
  Missing (parse failure) per scheduled response: "mcar" at rate m in both arms; "arm" at rate 2m in
  arm X only (same overall rate, arm-dependent); "mnar" at rate 2m for arm-X failures only (stress test,
  not part of the §6 grid: complete-case analysis is biased under it); "case" at rate 2m * Phi(-u_i / sd)
  in both arms, so harder cases (low u) lose more responses, and whole cases can be lost (stress test).
Model heterogeneity: several models with different rates per arm; analysed per model or pooled with the
case as the cluster.
"""
import math
import random
from functools import lru_cache
from statistics import NormalDist

from .stats import pair_counts

_Q = [NormalDist().inv_cdf((k + 0.5) / 2000) for k in range(2000)]
_PHI = NormalDist().cdf


def expit(x):
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    e = math.exp(x)
    return e / (1 + e)


@lru_cache(maxsize=None)
def intercept(p, sd):
    """Logit intercept whose marginal rate under N(0, sd^2) case effects is p."""
    if p <= 0:
        return -math.inf
    if p >= 1:
        return math.inf
    if sd == 0:
        return math.log(p / (1 - p))
    lo, hi = -50.0, 50.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if sum(expit(mid + sd * q) for q in _Q) / len(_Q) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def _rate(mu, u):
    if mu == math.inf:
        return 1.0
    if mu == -math.inf:
        return 0.0
    return expit(mu + u)


def simulate(rng, n, reps, rates, sd, miss=0.0, mode="mcar"):
    """Raw outcomes. rates = [(p_arm0, p_arm1, ...), ...], one tuple per model (arm 0 = X).
    Returns, per case, one outcome list per arm (models concatenated, paired by repeat index)."""
    mus = [tuple(intercept(p, sd) for p in model) for model in rates]
    k = len(rates[0])
    m0 = 2 * miss if mode in ("arm", "mnar") else miss
    mo = miss if mode == "mcar" else 0.0  # "case" sets both per case below
    out = []
    rnd = rng.random
    for _ in range(n):
        u = rng.gauss(0.0, sd) if sd else 0.0
        if mode == "case":
            m0 = mo = 2 * miss * (_PHI(-u / sd) if sd else 0.5)
        arms = [[] for _ in range(k)]
        for model in mus:
            ps = [_rate(mu, u) for mu in model]
            for _ in range(reps):
                for a, p in enumerate(ps):
                    y = int(rnd() < p)
                    m = m0 if a == 0 else mo
                    if m and (mode != "mnar" or y == 0) and rnd() < m:
                        y = None
                    arms[a].append(y)
        out.append(arms)
    return out


def cells(data, i=0, j=1, fill=None):
    """Per-case pair counts for arm i versus arm j."""
    return [pair_counts(arms[i], arms[j], fill) for arms in data]


def truth(rates, i=0, j=1):
    return sum(m[i] - m[j] for m in rates) / len(rates)


def seed_for(*key):
    """Deterministic per-task seed (independent of process scheduling and hash randomisation)."""
    h = 1469598103934665603
    for ch in repr(key).encode():
        h = ((h ^ ch) * 1099511628211) % 2 ** 64
    return h


def rng_for(base_seed, *key):
    return random.Random(seed_for(base_seed, *key))
