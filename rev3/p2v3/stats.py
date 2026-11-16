"""Paired, case-clustered interval methods for P1-P4 (spec §6, §9). Stdlib only; no model calls.

Data: for each independent case, the repeats of the two compared arms are paired by repeat index
(arm X = the first-named cell, e.g. E_scope in P4 or B in P1; arm Y = the comparison cell). A pair
with either outcome missing is dropped (complete pairs). Per case the counts are
(n11, n10, n01, n00), where n10 = X 1 and Y 0.

Estimand: Delta = mean over independent cases of (case rate in X - case rate in Y). Cases are weighted
equally; repeats are averaged within case (SCORING_SPEC §7). Each case therefore contributes its four
cell *proportions* f_i = counts / m_i (m_i = its complete pairs), and D = sum_i (f10_i - f01_i) / K.
A case with no complete pair cannot enter D; `Summary.dropped` counts such cases so they stay visible,
and the scheduled-denominator bounds (`pair_counts(..., fill=...)`) keep them in.
(Revision of 63e4789, which pooled pairs and so weighted cases by their complete-pair count.)

Methods (each returns a one-sided 1 - alpha lower and upper bound; a two-sided 1 - 2*alpha interval):
  wald     Obuchowski (1998) cluster-robust variance, Wald interval. Collapses to zero width when every
           pair agrees; kept only as the failing baseline the spec warns about.
  tango    Tango (1998) score interval for paired proportions, with its null variance multiplied by the
           Obuchowski-type design effect deff = var_cluster(D) / var_multinomial(D), where the multinomial
           variance treats each case as one pair. deff is clamped to [mean(1 / m_i), 1]: 1 means repeats add
           nothing, mean(1 / m_i) means repeats are independent. With no discordant pair, deff = 1.
  tango_c  As tango with deff fixed at 1: repeats never narrow the interval (conservative).
  tango_cc, tango_c_cc  As tango / tango_c with a continuity correction of 0.5 on the effective-count
           scale (|b - c - N d0| / deff reduced by 0.5). Added after the first grid run showed both
           uncorrected variants exceed 3% non-coverage near the ceiling (PRECISION_REPORT.md §3).
  bayes    Jeffreys-Dirichlet posterior for the four pair cells, counts divided by deff (as tango);
           bounds are posterior quantiles of p10 - p01, by quadrature.
"""
import math
from collections import namedtuple
from statistics import NormalDist

_N = NormalDist()
Summary = namedtuple("Summary", "K b c n11 sdd inv_m dropped")

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
    """Equal-case sufficient statistics from per-case (n11, n10, n01, n00)."""
    K = dropped = 0
    b = c = n11 = sdd = inv_m = 0.0
    for a11, a10, a01, a00 in cells:
        m = a11 + a10 + a01 + a00
        if m == 0:
            dropped += 1
            continue
        K += 1
        b += a10 / m; c += a01 / m; n11 += a11 / m
        sdd += ((a10 - a01) / m) ** 2
        inv_m += 1 / m
    if K < 2:
        raise ValueError("need at least two cases with a complete pair")
    return Summary(K, b, c, n11, sdd, inv_m / K, dropped)


def estimate(s):
    return (s.b - s.c) / s.K


def var_cluster(s):
    """Variance of D from the spread of case-level differences (cases independent)."""
    d = estimate(s)
    return max(s.sdd - s.K * d * d, 0.0) / (s.K - 1) / s.K


def design_effect(s, conservative=False):
    if conservative:
        return 1.0
    d = estimate(s)
    vnv = ((s.b + s.c) / s.K - d * d) / s.K
    if vnv <= 0:
        return 1.0
    return min(max(var_cluster(s) / vnv, s.inv_m), 1.0)


def _tango_z(b, c, n, d0, deff, cc=0.0):
    """Tango's score statistic for H0: Delta = d0 (restricted MLE of the p01 cell), variance times deff.
    cc: continuity correction, in effective-count units (b - c is divided by deff first)."""
    A = 2 * n
    B = -b - c + (2 * n - b + c) * d0
    C = -c * d0 * (1 - d0)
    p01 = (-B + math.sqrt(max(B * B - 4 * A * C, 0.0))) / (2 * A)
    v = n * (2 * p01 + d0 - d0 * d0) * deff
    num = b - c - n * d0
    if cc:
        num = math.copysign(max(abs(num) / deff - cc, 0.0) * deff, num)
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


def tango_z(s, d0, conservative=False, cc=0.0):
    return _tango_z(s.b, s.c, s.K, d0, design_effect(s, conservative), cc)


def tango(s, alpha=0.025, conservative=False, cc=0.0):
    z = _N.inv_cdf(1 - alpha)
    deff = design_effect(s, conservative)
    f = lambda d0: _tango_z(s.b, s.c, s.K, d0, deff, cc)
    d = estimate(s)
    e = 1e-12
    lo = -1.0 if f(-1 + e) <= z else _solve(f, -1 + e, d, z)
    hi = 1.0 if f(1 - e) >= -z else _solve(f, d, 1 - e, -z)
    return lo, hi


def wald(s, alpha=0.025):
    z = _N.inv_cdf(1 - alpha)
    d, se = estimate(s), math.sqrt(var_cluster(s))
    return max(-1.0, d - z * se), min(1.0, d + z * se)


TANGO = {"tango": {}, "tango_cc": {"cc": 0.5}, "tango_c": {"conservative": True},
         "tango_c_cc": {"conservative": True, "cc": 0.5}}


def p_noninferiority(s, margin, method="tango_cc"):
    """One-sided p-value for H0: Delta <= -margin (Tango score variant `method`)."""
    return 1 - _N.cdf(tango_z(s, -margin, **TANGO[method]))


def p_two_sided(s, method="tango_cc"):
    """Two-sided p-value for H0: Delta = 0 (Tango score variant; McNemar-type when deff = 1)."""
    return 2 * (1 - _N.cdf(abs(tango_z(s, 0.0, **TANGO[method]))))


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
    a0 = (s.K - s.b - s.c) / f + 1.0
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


METHODS = {"wald": wald, "bayes": bayes,
           **{k: (lambda kw: lambda s, alpha=0.025: tango(s, alpha, **kw))(kw) for k, kw in TANGO.items()}}
