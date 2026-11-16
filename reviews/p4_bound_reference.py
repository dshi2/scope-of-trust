"""Independent, deliberately conservative P2 P4 noninferiority reference.

This is an audit comparator, not the proposed final estimator. It uses one
independent *case* as one statistical observation, regardless of model repeats.
Run tests from repository root:
    python3 -m unittest discover -s reviews -p test_p4_bound_reference.py

Assumptions: case-level independence for the chosen *single model*, each
repetition's correct-acceptance outcome is in [0, 1], and all planned repeats
are included in the denominator. Missing outcomes may be arbitrary (MNAR).

P4 = mean(correct_acceptance(E_scope improved) - correct_acceptance(E improved)).
A one-sided lower bound above -margin supports noninferiority. The Hoeffding
radius is large and does not model case-family dependence; it is intentionally
a stress-test comparator, NEVER a sample-size recommendation.
"""
from dataclasses import dataclass
from math import log, sqrt


@dataclass(frozen=True)
class Arm:
    planned: int
    scored: int
    accepted: int

    def bounds(self):
        if any(type(x) is not int for x in (self.planned, self.scored, self.accepted)):
            raise ValueError("counts must be integers")
        if not (self.planned > 0 and 0 <= self.accepted <= self.scored <= self.planned):
            raise ValueError("invalid counts")
        # No outcome is imputed for unscored scheduled responses.
        return (self.accepted / self.planned,
                (self.accepted + self.planned - self.scored) / self.planned)


@dataclass(frozen=True)
class CasePair:
    case_id: str
    model: str
    e: Arm
    e_scope: Arm


def reference_lower_bound(pairs, *, alpha, margin):
    """Conservative one-sided P4 bound from independent case-level pairs.

    Aggregate *within each case* first. Do not pass repeats as separate pairs.
    Evaluate model-specific effects separately. The family-wise alpha assigned
    to P4 must be passed by the governing multiplicity procedure.

    Returns identification limits for the observed case sample and a
    Hoeffding-based one-sided lower confidence bound for its population mean.
    Does not cover dependence among related case families.
    """
    pairs = list(pairs)
    if not pairs or not (0 < alpha < 1) or not (0 < margin < 1):
        raise ValueError("nonempty pairs, 0<alpha<1 and 0<margin<1 required")
    if any(not p.case_id or not p.model for p in pairs):
        raise ValueError("case ID and model are required")
    if len({p.model for p in pairs}) != 1:
        raise ValueError("analyze models separately")
    if len({p.case_id for p in pairs}) != len(pairs):
        raise ValueError("repeats or duplicate cases cannot count as independent cases")

    lower_sum = upper_sum = 0.0
    unscored = 0
    for p in pairs:
        e_lo, e_hi = p.e.bounds()
        s_lo, s_hi = p.e_scope.bounds()
        lower_sum += s_lo - e_hi
        upper_sum += s_hi - e_lo
        unscored += (p.e.planned - p.e.scored) + (p.e_scope.planned - p.e_scope.scored)
    n = len(pairs)
    identification_lower = lower_sum / n
    identification_upper = upper_sum / n
    # Hoeffding: P(sample_mean - population_mean >= t) <= exp(-n*t²/2)
    # because the paired case difference is in [-1, 1].
    radius = sqrt(2 * log(1 / alpha) / n)
    lower = max(-1.0, identification_lower - radius)
    return {
        "n_independent_cases": n,
        "n_unscored_repeats": unscored,
        "identification_interval": (identification_lower, identification_upper),
        "one_sided_lower": lower,
        "radius": radius,
        "margin": margin,
        "noninferiority_supported": lower > -margin,
    }
