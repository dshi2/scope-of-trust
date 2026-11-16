"""Gold labels by construction (REVISION_3_SPEC.md §5).

Each condition is described by an *evidence profile*: what the audit record actually
checked. Gold labels are derived from the profile by explicit rules, so every label
has a stated reason that separates:
  * audit scope (which proposition, facility and period the record checked),
  * observed change (did an outcome measurement show the indicator fell?),
  * overall welfare (one indicator never establishes overall welfare),
  * causal improvement (no record contains a design that could show causation).
tests/test_gold.py cross-checks the derived labels against the hand table in the spec.

A gold entry is a set of acceptable statuses. Most sets have one member. Two-member
sets are used only where a presupposition fails (see SCORING_SPEC.md §3).
"""
from .render import BELIEF_PARAMS, claim_ids

T, F, NE = "established_true", "established_false", "not_established"
STATUSES = (T, F, NE)

# proposition: which claim's content the record checks (None = no item checked)
# site: "target" | "sister" | None ; outcome_change: "fell" | "rose" | "unchanged" | None
_CHANGE = {"improved": "fell", "worsened": "rose", "unchanged": "unchanged"}


def evidence_profile(condition, direction="none"):
    base = {"proposition": None, "site": None, "period": None,
            "outcome_measured": False, "outcome_change": None, "causal_design": False,
            "coverage_stated": condition in ("C", "C_prime", "E_scope"), "unscoped_stamp": condition == "V"}
    if condition in ("B", "C", "C_prime"):
        base.update(proposition="P", site="target", period="2026 (current)")
    elif condition == "D1":
        base.update(proposition="R", site="target", period="2026 (current)")
    elif condition == "D2":
        base.update(proposition="P", site="sister", period="2026 (current)")
    elif condition in ("E", "E_scope"):
        base.update(proposition="Q_obs", site="target", period="2025 vs 2026",
                    outcome_measured=True, outcome_change=_CHANGE[direction])
    return base


def gold(condition, direction="none"):
    """Return {claim: {"accept": set, "label": str, "why": str}} for one cell."""
    prof = evidence_profile(condition, direction)
    prop, site, change = prof["proposition"], prof["site"], prof["outcome_change"]
    out = {}

    def put(cid, accept, why):
        if cid in claim_ids(condition):
            label = accept[0]
            out[cid] = {"accept": set(accept), "label": label, "why": why}

    # P: practice at the target facility
    if prop == "P" and site == "target":
        put("P", [T], "The record's item checked and finding cover the stated practice at this facility.")
    elif prop == "P" and site == "sister":
        put("P", [NE], "The record checks the practice at the sister site, not at this facility (place scope).")
    elif prof["unscoped_stamp"]:
        put("P", [NE], "The stamp names no item checked, method or finding, so it establishes no specific claim.")
    elif prop == "Q_obs":
        put("P", [NE], "The record checks outcome records, not the practice.")
    elif prop == "R":
        put("P", [NE], "The record checks fire/building safety, not the practice.")
    else:
        put("P", [NE], "No record in the file checks the practice.")

    # Q_obs: observed indicator change
    if prof["outcome_measured"]:
        if change == "fell":
            put("Q_obs", [T], "The audited records show the indicator fell between the two years (observed change).")
        else:
            put("Q_obs", [F], f"The audited records show the indicator {change} between the two years, so the stated fall did not occur.")
    elif prop == "P":
        put("Q_obs", [NE], "The audit checked a practice, not outcome records. A confirmed practice does not show that the indicator changed (audit scope).")
    else:
        put("Q_obs", [NE], "No record in the file measures the indicator.")

    # Q_welfare: overall welfare
    why_w = ("Overall welfare is not established by any record: at most one indicator was measured, "
             "and one indicator does not establish overall welfare.")
    put("Q_welfare", [NE, F] if change in ("rose", "unchanged") else [NE], why_w)

    # Q_cause: causal improvement
    if prof["outcome_measured"] and change == "fell":
        why_c = ("The records show an observed fall but contain no comparison group or control of other "
                 "factors, so they cannot show the practice caused it (observed change is not causal improvement).")
        put("Q_cause", [NE], why_c)
    elif prof["outcome_measured"]:
        put("Q_cause", [NE, F], "The claim presupposes a fall that the audited records show did not happen; "
                                "'false' (failed presupposition) and 'not established' are both accepted.")
    else:
        put("Q_cause", [NE], "No record assesses outcomes or their causes.")

    # R: other-topic inspection
    if prop == "R":
        put("R", [T], "The record's item checked and finding cover the stated inspection.")
    else:
        put("R", [NE], "No record checks the fire/building safety inspection.")

    # S: practice at sister facility
    if prop == "P" and site == "sister":
        put("S", [T], "The record checks the practice at the sister site.")
    elif prop == "P":
        put("S", [NE], "The record checks the practice at this facility only, not at the sister site (place scope).")
    else:
        put("S", [NE], "No record checks the sister site.")
    return out


def belief_gold(condition, direction="none"):
    """Normative Pr(Q_obs) under the stipulated model in the belief context. None = excluded."""
    bp = BELIEF_PARAMS
    q_p, q_np = bp["pr_q_given_p"], bp["pr_q_given_not_p"]
    if condition == "V":
        return None
    if condition in ("E", "E_scope"):
        return 1.0 if direction == "improved" else 0.0
    if condition in ("B", "C", "C_prime"):
        p = 1.0
    elif condition == "A0":
        p = bp["pr_p"]
    else:  # A, D1, D2: supplier statement of P only
        p = bp["statement_accuracy"]
    return round(p * q_p + (1 - p) * q_np, 6)
