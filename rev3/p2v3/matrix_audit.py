"""Design-adherence checks (Master Checklist v3, Gate 3; addendum: design-adherence report).

audit_planned: the planned matrix against an independently declared design (spec §3), not against
cells inferred from the matrix itself. reconcile: an execution log against the planned matrix.
Callers refuse to proceed unless the relevant flag is True. Whether an incomplete but valid log is
suitable for the primary analysis is decided by the prespecified missing-data rule (SCORING_SPEC §2),
not here.
"""
import csv
from collections import Counter, defaultdict

KEY = ("item_id", "condition", "direction", "context", "model", "repeat")
CELL = ("condition", "direction", "context")
FIXED = ("n_user_turns", "tools", "phase")  # must not vary within the matrix

# Declared from REVISION_3_SPEC.md §3, by hand: 10 conditions, 14 cells per case, 2 contexts.
_E_DIRS = ("improved", "worsened", "unchanged")
DECLARED_CELLS = frozenset(
    (c, d, x)
    for c, dirs in {"A": ("none",), "A0": ("none",), "B": ("none",), "C": ("none",), "C_prime": ("none",),
                    "D1": ("none",), "D2": ("none",), "V": ("none",), "E": _E_DIRS, "E_scope": _E_DIRS}.items()
    for d in dirs for x in ("attribution", "belief"))


def load(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def _key(r):
    return tuple(r[k] for k in KEY)


def audit_planned(rows, expected_cells=DECLARED_CELLS, expected_models=None, expected_repeats=None,
                  *, expected_items=None):
    """Audit against independently declared, nonempty item/model/repeat sets.

    Never derive those sets from the matrix being audited: that hides whole missing groups.
    This checks matrix structure, not scientific validity or live-run readiness.
    """
    issues = []
    for name, values in (("items", expected_items), ("models", expected_models),
                         ("repeats", expected_repeats), ("cells", expected_cells)):
        if not values:
            issues.append(f"expected {name} must be independently declared and nonempty")
    required = KEY + FIXED + ("stimulus_sha256",)
    if any(any(k not in r or r[k] in (None, "") for k in required) for r in rows):
        issues.append("planned row missing required values")
    if issues:
        return {"ok": False, "issues": issues}
    keys = Counter(map(_key, rows))
    dup = [k for k, n in keys.items() if n > 1]
    if dup:
        issues.append(f"duplicate trial keys: {dup[:3]}")
    items = sorted(expected_items)
    models = sorted(expected_models)
    repeats = sorted(expected_repeats)
    expected = {(i, c, d, x, m, rp) for i in items for (c, d, x) in expected_cells for m in models for rp in repeats}
    missing, extra = expected - set(keys), set(keys) - expected
    if missing:
        issues.append(f"{len(missing)} declared trials absent, e.g. {sorted(missing)[:2]}")
    if extra:
        issues.append(f"{len(extra)} trials outside the declared design, e.g. {sorted(extra)[:2]}")
    for f in FIXED:
        vals = {r[f] for r in rows}
        if len(vals) > 1:
            issues.append(f"{f} varies across the matrix: {sorted(vals)}")
    hashes = defaultdict(set)
    for r in rows:
        hashes[(r["item_id"],) + tuple(r[c] for c in CELL)].add(r["stimulus_sha256"])
    if any(len(v) > 1 for v in hashes.values()):
        issues.append("one cell maps to more than one stimulus hash")
    return {"ok": not issues, "issues": issues, "n_items": len(items), "n_cells": len(expected_cells),
            "n_models": len(models), "n_repeats": len(repeats)}


def _attempt_count(value):
    """Accept positive integers and canonical CSV decimal strings, never floats or booleans."""
    if type(value) is int and value > 0:
        return value
    if isinstance(value, str) and value.isascii() and value.isdecimal() and not value.startswith("0"):
        return int(value)
    return None


def reconcile(planned, observed, max_attempts, *, terminal_statuses):
    """observed rows: KEY fields + terminal status + attempts + stimulus_sha256.

    valid_log: nothing outside the matrix, no duplicate records, attempts well formed and within the
    limit, stimuli as planned. fully_observed: every scheduled trial has a declared terminal record.
    ok = valid_log and fully_observed.

    The caller supplies the frozen execution-status vocabulary (not grader parse statuses), and
    must separately pass audit_planned. This does not validate model settings or manifest identity.
    """
    if type(max_attempts) is not int or max_attempts < 1:
        raise ValueError("max_attempts must be a positive integer")
    if (not terminal_statuses or isinstance(terminal_statuses, str)
            or any(not isinstance(s, str) or not s.strip() for s in terminal_statuses)):
        raise ValueError("terminal_statuses must be a nonempty collection of status names")
    if not planned or any(any(k not in r or r[k] in (None, "")
                             for k in KEY + ("stimulus_sha256",)) for r in planned):
        raise ValueError("planned matrix must be nonempty and contain trial keys and hashes")
    plan = {_key(r): r for r in planned}
    if len(plan) != len(planned):
        raise ValueError("planned matrix contains duplicate trial keys")
    obs = defaultdict(list)
    log_issues = []
    for r in observed:
        required = KEY + ("status", "attempts", "stimulus_sha256")
        if any(k not in r for k in required):
            log_issues.append(f"record missing required fields: {sorted(set(required) - set(r))}")
            continue
        obs[_key(r)].append(r)
    outside = [k for k in obs if k not in plan]
    if outside:
        log_issues.append(f"{len(outside)} runs outside the frozen matrix")
    repeated = [k for k, v in obs.items() if len(v) > 1]
    if repeated:
        log_issues.append(f"{len(repeated)} trials logged more than once")

    def bad_attempts(r):
        count = _attempt_count(r["attempts"])
        return count is None or count > max_attempts
    bad = [k for k, v in obs.items() if any(bad_attempts(r) for r in v)]
    if bad:
        log_issues.append(f"{len(bad)} trials with malformed or over-limit attempt counts")
    drift = [k for k, v in obs.items() if k in plan and any(
        r["stimulus_sha256"] != plan[k]["stimulus_sha256"] for r in v)]
    if drift:
        log_issues.append(f"{len(drift)} trials ran a stimulus other than the planned one")
    nonterminal = [k for k, v in obs.items() if any(r["status"] not in terminal_statuses for r in v)]
    if nonterminal:
        log_issues.append(f"{len(nonterminal)} trials with undeclared or nonterminal statuses")
    missing = [k for k in plan if k not in obs or k in nonterminal]
    by_cell = defaultdict(Counter)
    retries = defaultdict(int)
    for k, v in obs.items():
        if k in plan and k not in bad and k not in nonterminal:
            cell = (plan[k]["model"],) + tuple(plan[k][c] for c in CELL)
            for r in v:
                by_cell[cell][r["status"]] += 1
                retries[(plan[k]["model"], plan[k]["condition"])] += int(r["attempts"]) - 1
    valid, full = not log_issues, not missing
    issues = log_issues + ([f"{len(missing)} scheduled trials have no declared terminal record"] if missing else [])
    return {"ok": valid and full, "valid_log": valid, "fully_observed": full, "issues": issues,
            "missing": len(missing), "missing_keys": missing[:20],
            "status_by_model_cell": {c: dict(s) for c, s in by_cell.items()},
            "retries_by_model_condition": dict(retries)}
