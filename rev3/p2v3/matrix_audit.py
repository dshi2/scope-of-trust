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


def audit_planned(rows, expected_cells=DECLARED_CELLS, expected_models=None, expected_repeats=None):
    """Every item x expected cell x model x repeat appears exactly once; nothing else appears."""
    issues = []
    keys = Counter(map(_key, rows))
    dup = [k for k, n in keys.items() if n > 1]
    if dup:
        issues.append(f"duplicate trial keys: {dup[:3]}")
    items = sorted({r["item_id"] for r in rows})
    models = sorted(expected_models or {r["model"] for r in rows})
    repeats = sorted(expected_repeats or {r["repeat"] for r in rows})
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


def reconcile(planned, observed, max_attempts):
    """observed rows: KEY fields + status + attempts (int >= 1), optionally stimulus_sha256.

    valid_log: nothing outside the matrix, no duplicate records, attempts well formed and within the
    limit, stimuli as planned. fully_observed: every scheduled trial has a terminal record.
    ok = valid_log and fully_observed.
    """
    plan = {_key(r): r for r in planned}
    obs = defaultdict(list)
    log_issues = []
    for r in observed:
        if any(k not in r for k in KEY + ("status", "attempts")):
            log_issues.append(f"record missing required fields: {sorted(set(KEY + ('status', 'attempts')) - set(r))}")
            continue
        obs[_key(r)].append(r)
    outside = [k for k in obs if k not in plan]
    if outside:
        log_issues.append(f"{len(outside)} runs outside the frozen matrix")
    repeated = [k for k, v in obs.items() if len(v) > 1]
    if repeated:
        log_issues.append(f"{len(repeated)} trials logged more than once")

    def bad_attempts(r):
        try:
            return not 1 <= int(r["attempts"]) <= max_attempts
        except (TypeError, ValueError):
            return True
    bad = [k for k, v in obs.items() if any(bad_attempts(r) for r in v)]
    if bad:
        log_issues.append(f"{len(bad)} trials with malformed or over-limit attempt counts")
    drift = [k for k, v in obs.items() if k in plan and any(
        r.get("stimulus_sha256") not in (None, plan[k]["stimulus_sha256"]) for r in v)]
    if drift:
        log_issues.append(f"{len(drift)} trials ran a stimulus other than the planned one")
    missing = [k for k in plan if k not in obs]
    by_cell = defaultdict(Counter)
    retries = defaultdict(int)
    for k, v in obs.items():
        if k in plan and k not in bad:
            cell = (plan[k]["model"],) + tuple(plan[k][c] for c in CELL)
            for r in v:
                by_cell[cell][r["status"]] += 1
                retries[(plan[k]["model"], plan[k]["condition"])] += int(r["attempts"]) - 1
    valid, full = not log_issues, not missing
    issues = log_issues + ([f"{len(missing)} scheduled trials have no record"] if missing else [])
    return {"ok": valid and full, "valid_log": valid, "fully_observed": full, "issues": issues,
            "missing": len(missing), "missing_keys": missing[:20],
            "status_by_model_cell": {c: dict(s) for c, s in by_cell.items()},
            "retries_by_model_condition": dict(retries)}
