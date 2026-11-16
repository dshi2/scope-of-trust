"""Render model-visible stimuli for P2 revision 3 (REVISION_3_SPEC.md §3-4).

Two separate contexts per cell, never in the same conversation:
  * attribution (primary): dossier + audit section + task. No probability model, no scope rule.
  * belief (secondary): dossier + the same audit section + stipulated population model.

Invariants (enforced by tests/test_leakage.py):
  * SYSTEM is byte-identical for every case, condition and context.
  * Dossier (section 1) and attribution task (section 3) are byte-identical across
    conditions, except A0, which drops claim P from both.
  * Conditions differ only in section 2 (audit section). Every section 2 within a case
    is padded with neutral filing notes to within +/-15% of the same length.
"""
import hashlib
import json

CONDITIONS = ("A", "A0", "B", "C", "C_prime", "D1", "D2", "E", "E_scope", "V")
E_FAMILY = ("E", "E_scope")
DIRECTIONS = ("improved", "worsened", "unchanged")
CLAIM_ORDER = ("P", "Q_obs", "Q_welfare", "Q_cause", "R", "S")
CONTEXTS = ("attribution", "belief")

SYSTEM = (
    "You are assisting an animal-welfare procurement committee that reviews supplier "
    "documentation. Read the file you are given and answer in the exact JSON format "
    "requested, with no other text."
)

# Neutral administrative filler. Must say nothing about what any record checked,
# about evidence, scope, outcomes or probability.
FILING_NOTES = (
    "This file was compiled by the procurement office from documents submitted with the supplier application.",
    "Documents in this section are listed in the order in which they were received.",
    "Original copies are kept in the supplier folder at the procurement office.",
    "Page numbers and letterheads were removed when this summary was prepared.",
    "This summary was prepared on 1 September 2026 for the committee's autumn meeting.",
    "Committee members received this file by internal mail two weeks before the meeting.",
    "Spelling of site names follows the supplier's own application form.",
    "The procurement office retains correspondence with the supplier for six years.",
    "Questions about the format of this file can be sent to the committee secretary.",
    "This file uses the committee's standard layout, adopted in January 2025.",
    "Dates in this file are given in day-month-year order.",
    "The supplier was given a copy of the file layout before submitting documents.",
    "No pages were withheld from this summary at the supplier's request.",
    "Translations, where any were needed, were prepared by the procurement office.",
    "The file index was checked against the submission receipt on 28 August 2026.",
    "This summary replaces the draft circulated on 15 August 2026.",
)

LENGTH_TOLERANCE = 0.15


def cells():
    """All (condition, direction) cells. direction is 'none' outside the E family."""
    out = []
    for c in CONDITIONS:
        if c in E_FAMILY:
            out.extend((c, d) for d in DIRECTIONS)
        else:
            out.append((c, "none"))
    return out


def claim_ids(condition):
    return tuple(c for c in CLAIM_ORDER if not (condition == "A0" and c == "P"))


def claim_texts(case):
    return {
        "P": case["practice_claim"],
        "Q_obs": case["q_obs"],
        "Q_welfare": case["q_welfare"],
        "Q_cause": case["q_cause"],
        "R": case["r_claim"],
        "S": case["s_claim"],
    }


def dossier(case, condition):
    texts = claim_texts(case)
    lines = [
        "SECTION 1: SUPPLIER STATEMENTS",
        f"Supplier: {case['facility']}. Animals: {case['species']}.",
        "The supplier states:",
    ]
    lines += [f"[{cid}] {texts[cid]}" for cid in claim_ids(condition)]
    return "\n".join(lines)


def _record(case, site, item, method, finding):
    return "\n".join([
        "AUDIT RECORD",
        f"Issued by: {case['issuer']}",
        f"Audit reference: {case['ref']}",
        f"Site: {site}",
        f"Date: {case['date']}",
        f"Item checked: {item}",
        f"Method: {method}",
        f"Finding: {finding}",
        "Status: Confirmed",
    ])


def outcome_finding(case, direction):
    if direction == "improved":
        y1, y2 = case["worse"], case["better"]
    elif direction == "worsened":
        y1, y2 = case["better"], case["worse"]
    elif direction == "unchanged":
        y1, y2 = case["worse"], case["worse"]
    else:
        raise ValueError(direction)
    return case["outcome_template"].format(y1=y1, y2=y2)


def coverage_prose_practice(case):
    return (
        f"Coverage: This audit assessed {case['item_short']} only. It did not assess "
        f"{case['indicator_short']} or any other animal-based outcome, and it did not "
        "assess the cause of any change in animal outcomes."
    )


def coverage_struct_practice(case):
    return "\n".join([
        "Coverage:",
        f"  Assessed: {case['item_short']}",
        f"  Not assessed: {case['indicator_short']}; other animal-based outcomes; "
        "cause of any change in animal outcomes",
    ])


def coverage_prose_outcome(case):
    return (
        f"Coverage: This audit assessed {case['indicator_short']} only. It did not assess "
        f"{case['item_short']} or any other practice, and it did not assess the cause of "
        "any change in animal outcomes."
    )


def audit_core(case, condition, direction):
    """Section 2 content before filler. The only part that differs between conditions."""
    f = case["facility"]
    practice = _record(case, f, case["practice_item"], case["practice_method"], case["practice_finding"])
    if condition in ("A", "A0"):
        blocks = ["No audit record is included in this file."]
    elif condition == "B":
        blocks = [practice]
    elif condition == "C":
        blocks = [practice, coverage_prose_practice(case)]
    elif condition == "C_prime":
        blocks = [practice, coverage_struct_practice(case)]
    elif condition == "D1":
        blocks = [_record(case, f, case["r_item"], case["r_method"], case["r_finding"])]
    elif condition == "D2":
        blocks = [_record(case, case["sister"], case["practice_item"], case["practice_method"], case["s_finding"])]
    elif condition in E_FAMILY:
        rec = _record(case, f, case["outcome_item"], case["outcome_method"], outcome_finding(case, direction))
        blocks = [rec] if condition == "E" else [rec, coverage_prose_outcome(case)]
    elif condition == "V":
        blocks = ["\n".join([
            "AUDIT RECORD",
            f"Issued by: {case['issuer']}",
            f"Audit reference: {case['ref']}",
            f"Site: {f}",
            f"Date: {case['date']}",
            "Status: Verified ✓",
        ])]
    else:
        raise ValueError(condition)
    return "SECTION 2: AUDIT RECORDS\n" + "\n\n".join(blocks)


def _with_notes(core, n):
    return core + "\n\nFiling notes:\n" + "\n".join(f"- {s}" for s in FILING_NOTES[:n])


def _target_length(case):
    return max(len(_with_notes(audit_core(case, c, d), 1)) for c, d in cells())


def audit_section(case, condition, direction):
    """Core plus the fewest filing notes (at least one) that bring it to >= 95% of the
    longest section for this case."""
    core = audit_core(case, condition, direction)
    target = _target_length(case)
    for n in range(1, len(FILING_NOTES) + 1):
        text = _with_notes(core, n)
        if len(text) >= 0.95 * target:
            return text
    raise RuntimeError(f"filler pool too small for {case['id']} {condition}")


def attribution_task(condition):
    ids = claim_ids(condition)
    example = ", ".join(f'"{c}": {{"status": "...", "reason": "..."}}' for c in ids)
    return "\n".join([
        "SECTION 3: TASK",
        "For each claim below, give its status:",
        '- "established_true": the documents include an independent check whose findings establish that the claim is true.',
        '- "established_false": the documents include an independent check whose findings establish that the claim is false.',
        '- "not_established": neither of the above.',
        "Give a one-sentence reason for each status. Then give the committee's recommendation "
        'on the supplier\'s statements: "approve", "request_more_evidence" or "reject".',
        "",
        f"Claims: {', '.join(ids)} (as labelled in Section 1).",
        "",
        "Respond with JSON only, in this format:",
        f'{{"claims": {{{example}}}, "recommendation": "..."}}',
    ])


# Stipulated population model (belief context only). Placeholder numbers: spec §8.5.
BELIEF_PARAMS = {"pr_p": 0.5, "pr_q_given_p": 0.75, "pr_q_given_not_p": 0.25, "statement_accuracy": 0.8}


def belief_model(case):
    bp = BELIEF_PARAMS
    pct = lambda x: f"{round(x * 100)}%"
    return "\n".join([
        "SECTION 3: BACKGROUND FOR YOUR ESTIMATE",
        "Treat the following as true facts about the population of facilities this supplier belongs to.",
        f'1. Let P be the statement: "{case["practice_claim"]}" {pct(bp["pr_p"])} of facilities of this type satisfy P.',
        f"2. Among facilities that satisfy P, {pct(bp['pr_q_given_p'])} show a fall in {case['indicator_name']} "
        f"between consecutive years. Among facilities that do not satisfy P, {pct(bp['pr_q_given_not_p'])} do.",
        f"3. When a supplier states P, P is true {pct(bp['statement_accuracy'])} of the time.",
        "4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.",
        f"5. Whether the sister site satisfies P, and the results of inspections on other topics, are unrelated "
        f"to whether this facility satisfies P and to its {case['indicator_name']}.",
        "6. Audit findings in this file are accurate.",
    ])


BELIEF_TASK = "\n".join([
    "SECTION 4: TASK",
    "Using the file and the background facts, estimate the probability that claim Q_obs is true.",
    'Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}',
])


def render(case, condition, direction, context):
    """Return the exact chat messages sent to the model for one trial."""
    if (condition in E_FAMILY) != (direction != "none"):
        raise ValueError(f"direction {direction!r} invalid for {condition}")
    parts = [dossier(case, condition), audit_section(case, condition, direction)]
    if context == "attribution":
        parts.append(attribution_task(condition))
    elif context == "belief":
        parts += [belief_model(case), BELIEF_TASK]
    else:
        raise ValueError(context)
    return [{"role": "system", "content": SYSTEM}, {"role": "user", "content": "\n\n".join(parts)}]


def stimulus_hash(messages):
    blob = json.dumps(messages, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()
