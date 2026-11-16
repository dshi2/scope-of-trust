"""Regenerate the derived artifacts of case BATCH bb (p2v3/cases_bb.py). Deterministic.

    python3 generate_bb.py      (run from rev3/)

Same pattern as generate_ext.py: uses the frozen renderer (p2v3/render.py: system prompt,
task text, condition matrix, hashing), gold and rubric code of generate.py, so batch rows have
exactly the schema of stimuli_dev.jsonl / stimuli_ext.jsonl. Writes only batch-bb files and
never touches base or extension artifacts:
  rendered/<bb case>.md, stimuli_bb.jsonl, DESIGN_MATRIX_bb.csv, COVERAGE_bb.md, CLAIM_EVIDENCE_RUBRIC_bb.md
EXPERT_VERDICTS.csv is human-owned and never written here (batch-bb rows are not yet in it).
"""
import collections
import csv
import json
import os

import generate as g
from p2v3 import render as r
from p2v3.cases import CASES
from p2v3.cases_bb import BATCH, CASES_BB, PRACTICE_NOTES_BB
from p2v3.cases_ext import CASES_EXT
from p2v3.gold import belief_gold, gold

HERE = g.HERE
SUFFIX = f"_{BATCH}"
STIMULI = f"stimuli{SUFFIX}.jsonl"
BASE_SHA = "368e1d0e…8e67"
EXT_SHA = "c9d92a01…"


def rubric_rows(k):
    """generate.rubric_rows for a batch case. The builder notes live in cases_bb.py; they are lent to
    generate.PRACTICE_NOTES only for the call, so p2v3/rubric.py is neither edited nor left mutated."""
    notes = g.PRACTICE_NOTES
    assert k["id"] not in notes, f"{k['id']} already has base/extension notes"
    notes[k["id"]] = PRACTICE_NOTES_BB[k["id"]]
    try:
        return g.rubric_rows(k)
    finally:
        del notes[k["id"]]


def write_rendered():
    os.makedirs(os.path.join(HERE, "rendered"), exist_ok=True)
    rows = []
    for k in CASES_BB:
        out = [f"# Rendered stimuli: `{k['id']}` (batch {BATCH})", "",
               "Synthetic case; pending expert review. Contexts are separate conversations.",
               "A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block",
               f"shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: {STIMULI}.", "",
               "## System message (identical in every cell and context)", "", g.fence(r.SYSTEM), ""]
        for c, d in r.cells():
            label = c if d == "none" else f"{c} / {d}"
            gl = gold(c, d)
            bg = belief_gold(c, d)
            out += [f"## {label}  ({g.ROLE[c]})", "",
                    "| claim | gold | accepted | why |", "|---|---|---|---|"]
            out += [f"| {cid} | {g.SHORT[v['label']]} | {'/'.join(sorted(g.SHORT[a] for a in v['accept']))} | {v['why']} |"
                    for cid, v in gl.items()]
            out += ["", f"Belief gold p(Q_obs): {'excluded' if bg is None else bg}", ""]
            hashes = []
            for x in r.CONTEXTS:
                msgs = r.render(k, c, d, x)
                h = r.stimulus_hash(msgs)
                hashes.append(f"{x} `sha256:{h[:16]}`")
                rows.append({"item_id": k["id"], "condition": c, "direction": d, "context": x,
                             "stimulus_sha256": h, "messages": msgs})
                if c in g.FULL_CELLS:
                    out += [f"### {x} context  `sha256:{h[:16]}`", "", g.fence(msgs[1]["content"]), ""]
            if c not in g.FULL_CELLS:
                out += ["Hashes: " + "; ".join(hashes), "", g.fence(r.audit_core(k, c, d)), ""]
        with open(os.path.join(HERE, "rendered", f"{k['id']}.md"), "w") as f:
            f.write("\n".join(out))
    with open(os.path.join(HERE, STIMULI), "w") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    return rows


def write_matrix(rows):
    cols = ["item_id", "template_family", "species", "practice_type", "indicator_type", "issuer", "condition",
            "direction", "context", "role", "model", "repeat", "phase", "n_user_turns", "tools", "stimulus_sha256"]
    by_id = {k["id"]: k for k in CASES_BB}
    with open(os.path.join(HERE, f"DESIGN_MATRIX{SUFFIX}.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for row in rows:
            k = by_id[row["item_id"]]
            w.writerow({"item_id": k["id"], "template_family": g.TEMPLATE_FAMILY, "species": k["species"],
                        "practice_type": k["practice_type"], "indicator_type": k["indicator_type"],
                        "issuer": k["issuer"], "condition": row["condition"], "direction": row["direction"],
                        "context": row["context"], "role": g.ROLE[row["condition"]], "model": "TBD",
                        "repeat": "TBD", "phase": f"dev-{BATCH}", "n_user_turns": 1, "tools": "none",
                        "stimulus_sha256": row["stimulus_sha256"]})


def write_coverage():
    n_cells = len(r.cells())
    prior = CASES + CASES_EXT
    allc = prior + CASES_BB
    fam = lambda ks: {(k["species"], k["practice_type"], k["indicator_type"]) for k in ks}
    out = [f"# Case-coverage report (batch {BATCH})", "",
           f"Generated by `generate_bb.py`. Describes prespecified case categories and eligibility only. "
           "It contains no model results, and cases are never added or dropped based on model behaviour.", "",
           f"**Separately declared batch run.** Batch {BATCH} is one of three batches (ba, bb, bc; 8 cases each) that expand "
           "the development set from 12 to 36 cases. The expansion was approved for precision: with 12 independent cases "
           "the case-clustered intervals are wide. The batch was authored after the base and extension stimuli were frozen "
           f"(`stimuli_dev.jsonl` sha256 `{BASE_SHA}`, `stimuli_ext.jsonl` sha256 `{EXT_SHA}`), and is run separately with "
           "the same frozen model configuration (`configs/p2_dev_eval_v1.json`), renderer, system prompt, task text and "
           "condition matrix. Batch cases were not selected or edited based on any model output.", "",
           f"- Independent batch-{BATCH} cases: **{len(CASES_BB)}** (all synthetic, authored by the builder; pending expert review)",
           f"- With the base and extension sets: **{len(allc)}** cases, {len(fam(allc))} distinct species × practice × indicator "
           "families (batches ba and bc are counted in their own reports)",
           f"- Families shared with the base or extension set: {len(fam(CASES_BB) & fam(prior))}",
           f"- Cells per case: {n_cells} (10 conditions; E and E_scope crossed with 3 outcome directions)",
           f"- Contexts per cell: {len(r.CONTEXTS)} ({', '.join(r.CONTEXTS)})",
           f"- Eligibility: every case is eligible for every cell by construction "
           f"({len(CASES_BB)} × {n_cells} = {len(CASES_BB) * n_cells} cells, all filled)", ""]
    for dim in ("species", "practice_type", "indicator_type", "issuer"):
        cnt = collections.Counter(k[dim] for k in CASES_BB)
        out += [f"## By {dim}", "", "| value | cases |", "|---|---|"]
        out += [f"| {v} | {n} |" for v, n in sorted(cnt.items())] + [""]
    out += ["## Outcome audit method per case", "", "| case | outcome item | outcome method |", "|---|---|---|"]
    out += [f"| {k['id']} | {k['outcome_item']} | {k['outcome_method']} |" for k in CASES_BB] + [""]
    out += ["## Section 2 length per cell (characters)", "",
            "Lengths are not padded. Every cell ends with the same fixed filing notes, so differences equal "
            "the audit content that defines the condition (ledger P1, P3, P4).", "",
            "| case | " + " | ".join(f"{c}/{d[:3]}" if d != "none" else c for c, d in r.cells()) + " |",
            "|---|" + "---|" * len(r.cells())]
    out += [f"| {k['id']} | " + " | ".join(str(len(r.audit_section(k, c, d))) for c, d in r.cells()) + " |"
            for k in CASES_BB] + [""]
    out += [f"## What batch {BATCH} adds", "",
            "- **Species:** rainbow trout, Nile tilapia, whiteleg shrimp (broodstock), European sea bass, broiler breeders, "
            "pullets, Japanese quail, meat geese (base: broilers, laying hens, pigs; extension: dairy cows, Atlantic salmon, "
            "turkeys, Pekin ducks, rabbits, dairy calves).",
            "- **Practice types:** water oxygen level, emergency oxygen backup, no eyestalk ablation, crowding duration, "
            "mating ratio, dark brooders, soft ceilings, pasture access.",
            "- **Outcome evidence sources:** processing-plant grading (sampled per harvest batch; every carcass), "
            "daily mortality logs against delivery and harvest counts, mortality logs against veterinary reports, "
            "a contracted fish health assessor (four visits a year), the attending vet's monthly visit reports, "
            "an external scorer at a fixed age (16 weeks), daily mortality and cull sheets per bird placed.",
            "- **Measurement windows:** calendar year, harvest year, batch-harvest year, stocking year with a 60-day "
            "follow-up, transfer year, depletion year, slaughter year.",
            "- **Issuers:** eight new fictional issuers (none shared with the base or extension set).", "",
            "## Not covered (known gaps, unchanged by this batch)", "",
            "- **Template diversity: one family.** Batch cases use the same audit-record layout (`kv-record-v1`) and dossier "
            "layout as the base cases, by design (same renderer). Format-specific behaviour still cannot be separated from the effect.",
            "- **Period and population scope.** No condition varies the audited period or audits a subset of the population.",
            "- **Independence.** All cases come from one author (builder). Analysis must cluster on case.",
            "- **Realism.** Thresholds, indicators and methods are unreviewed placeholders (spec §8.6); "
            f"`EXPERT_VERDICTS.csv` has no rows for batch {BATCH} yet (human-owned; add blank rows from "
            f"`CLAIM_EVIDENCE_RUBRIC{SUFFIX}.md` row ids).", ""]
    with open(os.path.join(HERE, f"COVERAGE{SUFFIX}.md"), "w") as f:
        f.write("\n".join(out))


def write_rubric():
    out = [f"# Claim-evidence rubric for expert review (batch {BATCH})", "",
           "Generated by `generate_bb.py`. Same structure as `CLAIM_EVIDENCE_RUBRIC.md`. **Builder rationale is not "
           "validation.** Expert verdicts go in `EXPERT_VERDICTS.csv`, keyed by row id; that file is human-owned and never "
           "written by a generator.", ""]
    for k in CASES_BB:
        out += [f"## {k['id']} ({k['species']}; issuer {k['issuer']})", "",
                "| Row id | Claim (cells where gold = T/F) | Claim text | Record: item / method / finding | Builder: scope and residual risk |",
                "|---|---|---|---|---|"]
        out += ["| " + " | ".join(row) + " |" for row in rubric_rows(k)] + [""]
    with open(os.path.join(HERE, f"CLAIM_EVIDENCE_RUBRIC{SUFFIX}.md"), "w") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    rows = write_rendered()
    write_matrix(rows)
    write_coverage()
    write_rubric()
    print(f"{len(rows)} stimuli, {len(CASES_BB)} batch-{BATCH} cases, {len(r.cells())} cells")
