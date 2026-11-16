"""Design-adherence checks (Master Checklist v3, Gate 3; addendum: design-adherence report).

audit_planned: is the planned matrix complete, balanced and free of unintended setting differences?
reconcile: does an execution log account for every planned trial, with nothing outside the matrix
and the same retry policy everywhere? Both return a report; callers refuse to proceed if not ok.
"""
import csv
from collections import Counter, defaultdict

KEY = ("item_id", "condition", "direction", "context", "model", "repeat")
CELL = ("condition", "direction", "context")
FIXED = ("n_user_turns", "tools", "phase")  # must not vary within the matrix


def load(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def _key(r):
    return tuple(r[k] for k in KEY)


def audit_planned(rows):
    issues = []
    dup = [k for k, n in Counter(map(_key, rows)).items() if n > 1]
    if dup:
        issues.append(f"duplicate trial keys: {dup[:3]}")
    cells_by_item = defaultdict(set)
    for r in rows:
        cells_by_item[r["item_id"]].add(tuple(r[c] for c in CELL))
    all_cells = set().union(*cells_by_item.values()) if cells_by_item else set()
    for item, cells in sorted(cells_by_item.items()):
        if cells != all_cells:
            issues.append(f"{item} lacks cells {sorted(all_cells - cells)[:3]}")
    per_cell = Counter(tuple(r[c] for c in CELL) for r in rows)
    if len(set(per_cell.values())) > 1:
        issues.append(f"unequal rows per cell: {sorted(set(per_cell.values()))}")
    for f in FIXED:
        vals = {r[f] for r in rows}
        if len(vals) > 1:
            issues.append(f"{f} varies across the matrix: {sorted(vals)}")
    shared = defaultdict(set)
    for r in rows:
        shared[(r["item_id"],) + tuple(r[c] for c in CELL)].add(r["stimulus_sha256"])
    if any(len(v) > 1 for v in shared.values()):
        issues.append("one cell maps to more than one stimulus hash")
    return {"ok": not issues, "issues": issues, "n_items": len(cells_by_item),
            "n_cells": len(all_cells), "rows_per_cell": dict(per_cell)}


def reconcile(planned, observed, max_attempts):
    """observed rows: KEY fields + status ('ok'|'malformed'|'provider_error'|...) + attempts (int)."""
    plan = {_key(r): r for r in planned}
    obs = defaultdict(list)
    for r in observed:
        obs[_key(r)].append(r)
    issues = []
    outside = [k for k in obs if k not in plan]
    if outside:
        issues.append(f"{len(outside)} runs outside the frozen matrix")
    missing = [k for k in plan if k not in obs]
    repeated = [k for k, v in obs.items() if len(v) > 1]
    if repeated:
        issues.append(f"{len(repeated)} trials logged more than once")
    over = [k for k, v in obs.items() if any(int(r["attempts"]) > max_attempts for r in v)]
    if over:
        issues.append(f"{len(over)} trials exceed the retry limit")
    by_cell = defaultdict(Counter)
    retries = defaultdict(int)
    for k, v in obs.items():
        if k in plan:
            cell = tuple(plan[k][c] for c in CELL)
            for r in v:
                by_cell[cell][r["status"]] += 1
                retries[plan[k]["condition"]] += int(r["attempts"]) - 1
    return {"ok": not issues, "issues": issues, "missing": len(missing), "missing_keys": missing[:20],
            "status_by_cell": {c: dict(s) for c, s in by_cell.items()}, "retries_by_condition": dict(retries)}
