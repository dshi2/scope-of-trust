"""Paired, case-clustered interval methods for P1-P4 (spec §6, §9). Stdlib only; no model calls.

Data: for each independent case, the repeats of the two compared arms are paired by repeat index
(arm X = the first-named cell, e.g. E_scope in P4 or B in P1; arm Y = the comparison cell). A pair
with either outcome missing is dropped (complete pairs). Per case the counts are
(n11, n10, n01, n00), where n10 = X 1 and Y 0. The estimand is the difference of marginal rates
Delta = p_X - p_Y, estimated by the ratio estimator D = (b - c) / N over all complete pairs.

Methods (each returns a one-sided 1 - alpha lower and upper bound; a two-sided 1 - 2*alpha interval):
  wald     Obuchowski (1998) cluster-robust variance, Wald interval. Collapses to zero width when every
           pair agrees; kept only as the failing baseline the spec warns about.
  tango    Tango (1998) score interval for paired proportions, with its null variance multiplied by the
           Obuchowski design effect deff = var_cluster / var_multinomial, clamped to [1, sum m_i^2 / N].
           When no pair is discordant the design effect is set to its maximum (the case is the unit).
  tango_c  As tango with deff fixed at its maximum: the case is always the unit (conservative).
  bayes    Jeffreys-Dirichlet posterior for the four pair cells, counts divided by deff (as tango);
           bounds are posterior quantiles of p10 - p01, by quadrature.
"""
import math
from collections import namedtuple
from statistics import NormalDist

_N = NormalDist()
Summary = namedtuple("Summary", "K N b c n11 sdd sdm smm")


def pair_counts(x, y, fill=None):
    """Per-case (n11, n10, n01, n00) from two equal-length outcome lists (0, 1 or None = missing).
    fill=(fx, fy) imputes missing outcomes instead of dropping the pair (scheduled-denominator bounds:
    (0, 1) is the worst case for Delta = p_X - p_Y, (1, 0) the best case)."""
    if len(x) != len(y):
        raise ValueError("arms must have the same scheduled repeats")
    if fill is not None:
        x = [fill[0] if a is None else a for a in x]
        y = [fill[1] if b is None else b for b in y]
    n = [0, 0, 0, 0]
    for a, b in zip(x, y):
        if a is None or b is None:
            continue
        if a not in (0, 1) or b not in (0, 1):
            raise ValueError("outcomes must be 0, 1 or None")
        n[(1 - a) * 2 + (1 - b)] += 1
    return tuple(n)


def summarize(cells):
    """Sufficient statistics from per-case (n11, n10, n01, n00); cases with no complete pair drop out."""
    K = N = b = c = n11 = sdd = sdm = smm = 0
    for a11, a10, a01, a00 in cells:
        m = a11 + a10 + a01 + a00
        if m == 0:
            continue
        d = a10 - a01
        K += 1; N += m; b += a10; c += a01; n11 += a11
        sdd += d * d; sdm += d * m; smm += m * m
    if K < 2:
        raise ValueError("need at least two cases with a complete pair")
    return Summary(K, N, b, c, n11, sdd, sdm, smm)


def estimate(s):
    return (s.b - s.c) / s.N


def var_cluster(s):
    """Obuchowski ratio-estimator variance of D, with the K/(K-1) small-sample factor."""
    d = estimate(s)
    ss = s.sdd - 2 * d * s.sdm + d * d * s.smm
    return max(ss, 0.0) * s.K / (s.K - 1) / s.N ** 2


def design_effect(s, conservative=False):
    mmax = s.smm / s.N  # = mean cluster size when sizes are equal; deff under perfect within-case correlation
    if conservative:
        return mmax
    d = estimate(s)
    vnv = ((s.b + s.c) / s.N - d * d) / s.N
    if vnv <= 0:
        return mmax
    return min(max(var_cluster(s) / vnv, 1.0), mmax)


def _tango_z(b, c, n, d0, deff):
    """Tango's score statistic for H0: Delta = d0 (restricted MLE of the p01 cell), variance times deff."""
    A = 2 * n
    B = -b - c + (2 * n - b + c) * d0
    C = -c * d0 * (1 - d0)
    p01 = (-B + math.sqrt(max(B * B - 4 * A * C, 0.0))) / (2 * A)
    v = n * (2 * p01 + d0 - d0 * d0) * deff
    num = b - c - n * d0
    if v <= 0:
        return math.copysign(math.inf, num) if num else 0.0
    return num / math.sqrt(v)


def _solve(f, lo, hi, target, tol=1e-10):
    """f decreasing on [lo, hi]; the point where f crosses target."""
    for _ in range(200):
        if hi - lo < tol:
            break
        mid = (lo + hi) / 2
        if f(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def tango_z(s, d0, conservative=False):
    return _tango_z(s.b, s.c, s.N, d0, design_effect(s, conservative))


def tango(s, alpha=0.025, conservative=False):
    z = _N.inv_cdf(1 - alpha)
    deff = design_effect(s, conservative)
    f = lambda d0: _tango_z(s.b, s.c, s.N, d0, deff)
    d = estimate(s)
    e = 1e-12
    lo = -1.0 if f(-1 + e) <= z else _solve(f, -1 + e, d, z)
    hi = 1.0 if f(1 - e) >= -z else _solve(f, d, 1 - e, -z)
    return lo, hi


def tango_c(s, alpha=0.025):
    return tango(s, alpha, conservative=True)


def wald(s, alpha=0.025):
    z = _N.inv_cdf(1 - alpha)
    d, se = estimate(s), math.sqrt(var_cluster(s))
    return max(-1.0, d - z * se), min(1.0, d + z * se)


def p_noninferiority(s, margin, method="tango"):
    """One-sided p-value for H0: Delta <= -margin (Tango score)."""
    return 1 - _N.cdf(tango_z(s, -margin, method == "tango_c"))


def p_two_sided(s, method="tango"):
    """Two-sided p-value for H0: Delta = 0 (Tango score; McNemar-type when deff = 1)."""
    return 2 * (1 - _N.cdf(abs(tango_z(s, 0.0, method == "tango_c"))))


# ---- Bayesian Jeffreys-Dirichlet alternative -------------------------------------------------

def _gauss_legendre(n):
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-15:
                break
        xs.append(x)
        ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws


_GL = _gauss_legendre(64)


def _betacf(a, b, x):
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1 - qab * x / qap
    d = 1 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 1000):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d; d = 1 / (d if abs(d) > tiny else tiny)
        c = 1 + aa / c; c = c if abs(c) > tiny else tiny
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d; d = 1 / (d if abs(d) > tiny else tiny)
        c = 1 + aa / c; c = c if abs(c) > tiny else tiny
        de = d * c
        h *= de
        if abs(de - 1) < 1e-13:
            break
    return h


def betainc(a, b, x):
    """Regularized incomplete beta I_x(a, b)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lf = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x)
    if x < (a + 1) / (a + b + 2):
        return math.exp(lf) * _betacf(a, b, x) / a
    return 1 - math.exp(lf) * _betacf(b, a, 1 - x) / b


def _post_cdf_neg(t, a1, a2, a0):
    """P(p10 - p01 <= t) for t < 0 under Dirichlet(a1, a2, a0) on (p10, p01, rest).
    Write s = p10 + p01 ~ Beta(a1 + a2, a0) and w = p10 / s ~ Beta(a1, a2), independent.
    Then p10 - p01 = s (2w - 1) <= t iff w < 1/2 and s >= |t| / (1 - 2w)."""
    u = -t
    wmax = (1 - u) / 2
    if wmax <= 0:
        return 0.0
    A = a1 + a2
    mu = a1 / A
    sd = math.sqrt(a1 * a2 / (A * A * (A + 1)))
    wlo = max(0.0, mu - 14 * sd)
    if wlo >= wmax:
        return 0.0
    lbeta = math.lgamma(a1) + math.lgamma(a2) - math.lgamma(A)
    xs, ws = _GL
    total = 0.0
    if wlo == 0.0:  # w = wmax * v^2 removes the w^(a1 - 1) singularity at 0
        vmax = 1.0
        for x, wt in zip(xs, ws):
            v = (x + 1) / 2 * vmax
            w = wmax * v * v
            if w <= 0:
                continue
            dens = math.exp((a1 - 1) * math.log(w) + (a2 - 1) * math.log1p(-w) - lbeta) * 2 * wmax * v
            total += wt / 2 * vmax * dens * (1 - betainc(A, a0, u / (1 - 2 * w)))
    else:
        half = (wmax - wlo) / 2
        for x, wt in zip(xs, ws):
            w = wlo + (x + 1) * half
            dens = math.exp((a1 - 1) * math.log(w) + (a2 - 1) * math.log1p(-w) - lbeta)
            total += wt * half * dens * (1 - betainc(A, a0, u / (1 - 2 * w)))
    return min(max(total, 0.0), 1.0)


def bayes_lower(s, alpha=0.025, start=None):
    """Lower 100*alpha% posterior quantile of p10 - p01 (Jeffreys prior, counts / deff)."""
    f = design_effect(s)
    a1, a2 = s.b / f + 0.5, s.c / f + 0.5
    a0 = (s.N - s.b - s.c) / f + 1.0
    mean = (a1 - a2) / (a1 + a2 + a0)
    hi = min(mean, -1e-12)
    if _post_cdf_neg(hi, a1, a2, a0) <= alpha:
        # quantile is above min(mean, 0); only reached when the evidence is strongly positive
        return hi
    lo = -1.0 + 1e-9
    if start is not None and lo < start < hi:  # bracket around a starting guess to save evaluations
        g = start
        while g > lo and _post_cdf_neg(g, a1, a2, a0) > alpha:
            hi, g = g, max(lo, g - 0.5 * abs(g) - 1e-4)
        lo = g
    for _ in range(60):
        if hi - lo < 1e-7:
            break
        mid = (lo + hi) / 2
        if _post_cdf_neg(mid, a1, a2, a0) > alpha:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def bayes(s, alpha=0.025):
    """Lower bound only (P4 candidate); the upper bound is not computed."""
    return bayes_lower(s, alpha, start=tango(s, alpha)[0]), math.nan


METHODS = {"wald": wald, "tango": tango, "tango_c": tango_c, "bayes": bayes}
