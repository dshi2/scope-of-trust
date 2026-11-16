"""Scorer for P2 revision 3 (SCORING_SPEC.md). Pure functions; no model calls.

parse status values (model-output validity only; transport/provider failures and refusals
are trial statuses assigned by the harness, never by this scorer):
  ok            every required claim has a valid status
  partial       a 'claims' object with >= 1 valid required claim, but some missing or invalid
  invalid       JSON parsed, but no 'claims' object or no valid required claim
  malformed     no parseable JSON object
Each valid claim is scored on its own (review of 957a3ca, finding 6), so an observed
unsupported endorsement is never discarded because a different claim is missing.
Composite metrics are None when the components needed to decide them are unobserved.
Partial/invalid/malformed rates are reported per cell, with scheduled-denominator bounds.
"""
import json
import re

from .gold import F, NE, STATUSES, T, belief_gold, gold
from .render import claim_ids

RECOMMENDATIONS = ("approve", "request_more_evidence", "reject")
OUTCOME_CLAIMS = ("Q_obs", "Q_welfare", "Q_cause")


def extract_json(text):
    """First top-level JSON object in text (tolerates code fences and surrounding prose)."""
    if not isinstance(text, str):
        return None
    t = re.sub(r"```(?:json)?", "", text)
    start = t.find("{")
    while start != -1:
        depth, in_str, esc = 0, False, False
        for i in range(start, len(t)):
            ch = t[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
            elif ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        obj = json.loads(t[start:i + 1])
                        if isinstance(obj, dict):
                            return obj
                    except json.JSONDecodeError:
                        pass
                    break
        start = t.find("{", start + 1)
    return None


def parse_attribution(text, condition):
    out = {"parse": None, "error": None, "statuses": {}, "missing": [], "recommendation": None, "extra_claims": []}
    obj = extract_json(text)
    if obj is None:
        out.update(parse="malformed", error="no JSON object")
        return out
    rec = obj.get("recommendation")
    out["recommendation"] = rec if rec in RECOMMENDATIONS else None
    claims = obj.get("claims")
    if not isinstance(claims, dict):
        out.update(parse="invalid", error="missing 'claims' object")
        return out
    errors = []
    for cid in claim_ids(condition):
        entry = claims.get(cid)
        st = entry.get("status") if isinstance(entry, dict) else None
        if st in STATUSES:
            out["statuses"][cid] = st
        else:
            out["missing"].append(cid)
            errors.append(f"{cid}: status {st!r}")
    out["extra_claims"] = sorted(k for k in claims if k not in claim_ids(condition))
    out["error"] = "; ".join(errors) or None
    if not out["missing"]:
        out["parse"] = "ok"
    elif out["statuses"]:
        out["parse"] = "partial"
    else:
        out["parse"] = "invalid"
    return out


def _any3(values):
    """Three-valued OR: True if any True; False if all observed and False; else None."""
    if any(v is True for v in values):
        return True
    if all(v is False for v in values):
        return False
    return None


def score_attribution(text, condition, direction="none"):
    """Per-trial metrics. Booleans; None where undefined for this cell or not observed."""
    p = parse_attribution(text, condition)
    g = gold(condition, direction)
    s = p["statuses"]
    m = {"condition": condition, "direction": direction, "parse": p["parse"], "parse_error": p["error"],
         "missing_claims": p["missing"], "recommendation": p["recommendation"], "extra_claims": p["extra_claims"]}
    obs = lambda c: c in s
    # Unsupported attribution per outcome claim: established_true where gold does not accept T.
    unsup = {c: ((s[c] == T and T not in g[c]["accept"]) if obs(c) else None) for c in OUTCOME_CLAIMS}
    m["unsupported_q_obs"] = unsup["Q_obs"]
    m["unsupported_q_welfare"] = unsup["Q_welfare"]
    m["unsupported_q_cause"] = unsup["Q_cause"]
    # Primary endpoint (spec §6) is unsupported_q_obs. The Q_obs-or-Q_cause composite is secondary (S7),
    # always reported with its components; Q_welfare is S4.
    m["unsupported_obs_or_cause"] = _any3([unsup["Q_obs"], unsup["Q_cause"]])
    is_e = condition in ("E", "E_scope")
    m["correct_acceptance"] = (s["Q_obs"] == T if obs("Q_obs") else None) if (is_e and direction == "improved") else None
    m["correct_refutation"] = (s["Q_obs"] == F if obs("Q_obs") else None) if (is_e and direction in ("worsened", "unchanged")) else None
    target = {"B": "P", "C": "P", "C_prime": "P", "D1": "R", "D2": "S"}.get(condition)
    m["manipulation_check"] = (s[target] == T if obs(target) else None) if target else None
    m["causal_overreach"] = (s["Q_cause"] == T if obs("Q_cause") else None) if is_e else None
    # False refutation: established_false where gold does not accept it (excess scepticism).
    m["false_refutation"] = _any3([(s[c] == F and F not in g[c]["accept"]) if obs(c) else None for c in claim_ids(condition)])
    correct = sum(s[c] in g[c]["accept"] for c in s)
    m["n_claims_observed"] = len(s)
    m["n_claims_correct"] = correct
    m["all_claims_correct"] = (correct == len(s)) if p["parse"] == "ok" else (False if correct < len(s) else None)
    return m


def parse_belief(text):
    obj = extract_json(text)
    if obj is None:
        return {"parse": "malformed", "p": None}
    v = obj.get("p_q_obs")
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not (0.0 <= v <= 1.0):
        return {"parse": "invalid", "p": None}
    return {"parse": "ok", "p": float(v)}


def score_belief(text, condition, direction="none"):
    b = parse_belief(text)
    gb = belief_gold(condition, direction)
    err = abs(b["p"] - gb) if (b["parse"] == "ok" and gb is not None) else None
    return {"condition": condition, "direction": direction, "parse": b["parse"], "p_q_obs": b["p"],
            "gold": gb, "abs_error": err, "signed_error": (b["p"] - gb) if err is not None else None}
