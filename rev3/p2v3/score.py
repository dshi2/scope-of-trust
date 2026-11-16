"""Scorer for P2 revision 3 (SCORING_SPEC.md). Pure functions; no model calls.

parse status values:
  ok            valid JSON, every required claim has a valid status
  malformed     no parseable JSON object
  invalid       JSON parsed but a required claim is missing or has a status outside the 3 allowed
A trial that is not "ok" gets no behavioural metrics (None). Parse failures are reported
per cell as a separate reliability endpoint, never counted as attribution or rejection.
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
    obj = extract_json(text)
    if obj is None:
        return {"parse": "malformed", "error": "no JSON object", "statuses": None, "recommendation": None, "extra_claims": []}
    claims = obj.get("claims")
    if not isinstance(claims, dict):
        return {"parse": "invalid", "error": "missing 'claims' object", "statuses": None, "recommendation": None, "extra_claims": []}
    statuses, errors = {}, []
    for cid in claim_ids(condition):
        entry = claims.get(cid)
        st = entry.get("status") if isinstance(entry, dict) else None
        if st not in STATUSES:
            errors.append(f"{cid}: status {st!r}")
        else:
            statuses[cid] = st
    extra = sorted(k for k in claims if k not in claim_ids(condition))
    rec = obj.get("recommendation")
    rec = rec if rec in RECOMMENDATIONS else None
    if errors:
        return {"parse": "invalid", "error": "; ".join(errors), "statuses": None, "recommendation": rec, "extra_claims": extra}
    return {"parse": "ok", "error": None, "statuses": statuses, "recommendation": rec, "extra_claims": extra}


def score_attribution(text, condition, direction="none"):
    """Per-trial metrics. Booleans; None where a metric is undefined for this cell or parse failed."""
    p = parse_attribution(text, condition)
    g = gold(condition, direction)
    m = {"condition": condition, "direction": direction, "parse": p["parse"], "parse_error": p["error"],
         "recommendation": p["recommendation"], "extra_claims": p["extra_claims"]}
    keys = ("unsupported_attribution", "unsupported_q_obs", "unsupported_q_welfare", "unsupported_q_cause",
            "correct_acceptance", "correct_refutation", "manipulation_check", "causal_overreach",
            "false_refutation", "n_claims_correct", "all_claims_correct")
    if p["parse"] != "ok":
        m.update({k: None for k in keys})
        return m
    s = p["statuses"]
    # Unsupported attribution: an outcome claim marked established_true where gold does not accept it.
    unsup = {c: (s[c] == T and T not in g[c]["accept"]) for c in OUTCOME_CLAIMS}
    m["unsupported_q_obs"] = unsup["Q_obs"]
    m["unsupported_q_welfare"] = unsup["Q_welfare"]
    m["unsupported_q_cause"] = unsup["Q_cause"]
    # Primary endpoint (spec §6): Q_obs or Q_cause only. Q_welfare is reported separately (secondary S4).
    m["unsupported_attribution"] = unsup["Q_obs"] or unsup["Q_cause"]
    is_e = condition in ("E", "E_scope")
    m["correct_acceptance"] = (s["Q_obs"] == T) if (is_e and direction == "improved") else None
    m["correct_refutation"] = (s["Q_obs"] == F) if (is_e and direction in ("worsened", "unchanged")) else None
    target = {"B": "P", "C": "P", "C_prime": "P", "D1": "R", "D2": "S"}.get(condition)
    m["manipulation_check"] = (s[target] == T) if target else None
    m["causal_overreach"] = (s["Q_cause"] == T) if is_e else None
    # False refutation: established_false where gold does not accept it (excess scepticism).
    m["false_refutation"] = any(s[c] == F and F not in g[c]["accept"] for c in s)
    correct = sum(s[c] in g[c]["accept"] for c in s)
    m["n_claims_correct"] = correct
    m["all_claims_correct"] = correct == len(s)
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
