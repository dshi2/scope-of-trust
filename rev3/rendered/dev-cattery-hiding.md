# Rendered stimuli: `dev-cattery-hiding` (expansion batch bc)

Synthetic case; pending expert review. Contexts are separate conversations.
A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block
shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: stimuli_bc.jsonl.

## System message (identical in every cell and context)

~~~~text
You are assisting an animal-welfare procurement committee that reviews supplier documentation. Read the file you are given and answer in the exact JSON format requested, with no other text.
~~~~

## A  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | No record in the file checks the practice. |
| Q_obs | NE | NE | No record in the file measures the indicator. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.65

### attribution context  `sha256:7959a43a799533e7`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Fallowfield Cattery. Animals: cats (held for rehoming under a charity contract).
The supplier states:
[P] Throughout 2025, every cat pen in use at Fallowfield Cattery contained a hiding box and a raised shelf at every daily cleaning check.
[Q_obs] The recorded share of cats at Fallowfield Cattery that lost more than 10% of their admission weight in their first 14 days was lower for cats admitted in 2025 than for cats admitted in 2024.
[Q_welfare] The overall welfare of the cats at Fallowfield Cattery improved from 2024 to 2025.
[Q_cause] This reduction in recorded weight loss was caused by the hiding boxes and raised shelves.
[R] Fallowfield Cattery passed its 2026 water-hygiene inspection.
[S] Throughout 2025, every cat pen in use at Fallowmead Cattery, a sister site, also contained a hiding box and a raised shelf at every daily cleaning check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: TASK
For each claim below, give its status:
- "established_true": the documents include an independent check whose findings establish that the claim is true.
- "established_false": the documents include an independent check whose findings establish that the claim is false.
- "not_established": neither of the above.
Give a one-sentence reason for each status. Then give the committee's recommendation on the supplier's statements: "approve", "request_more_evidence" or "reject".

Claims: P, Q_obs, Q_welfare, Q_cause, R, S (as labelled in Section 1).

Respond with JSON only, in this format:
{"claims": {"P": {"status": "...", "reason": "..."}, "Q_obs": {"status": "...", "reason": "..."}, "Q_welfare": {"status": "...", "reason": "..."}, "Q_cause": {"status": "...", "reason": "..."}, "R": {"status": "...", "reason": "..."}, "S": {"status": "...", "reason": "..."}}, "recommendation": "..."}
~~~~

### belief context  `sha256:a727cbbfe20a647c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Fallowfield Cattery. Animals: cats (held for rehoming under a charity contract).
The supplier states:
[P] Throughout 2025, every cat pen in use at Fallowfield Cattery contained a hiding box and a raised shelf at every daily cleaning check.
[Q_obs] The recorded share of cats at Fallowfield Cattery that lost more than 10% of their admission weight in their first 14 days was lower for cats admitted in 2025 than for cats admitted in 2024.
[Q_welfare] The overall welfare of the cats at Fallowfield Cattery improved from 2024 to 2025.
[Q_cause] This reduction in recorded weight loss was caused by the hiding boxes and raised shelves.
[R] Fallowfield Cattery passed its 2026 water-hygiene inspection.
[S] Throughout 2025, every cat pen in use at Fallowmead Cattery, a sister site, also contained a hiding box and a raised shelf at every daily cleaning check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every cat pen in use at Fallowfield Cattery contained a hiding box and a raised shelf at every daily cleaning check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of cats that lost more than 10% of their admission weight in their first 14 days between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of cats that lost more than 10% of their admission weight in their first 14 days.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of cats that lost more than 10% of their admission weight in their first 14 days at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## A0  (exploratory)

| claim | gold | accepted | why |
|---|---|---|---|
| Q_obs | NE | NE | No record in the file measures the indicator. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.5

### attribution context  `sha256:ad0c51e953b4fcca`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Fallowfield Cattery. Animals: cats (held for rehoming under a charity contract).
The supplier states:
[Q_obs] The recorded share of cats at Fallowfield Cattery that lost more than 10% of their admission weight in their first 14 days was lower for cats admitted in 2025 than for cats admitted in 2024.
[Q_welfare] The overall welfare of the cats at Fallowfield Cattery improved from 2024 to 2025.
[Q_cause] This reduction in recorded weight loss was caused by the hiding boxes and raised shelves.
[R] Fallowfield Cattery passed its 2026 water-hygiene inspection.
[S] Throughout 2025, every cat pen in use at Fallowmead Cattery, a sister site, also contained a hiding box and a raised shelf at every daily cleaning check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: TASK
For each claim below, give its status:
- "established_true": the documents include an independent check whose findings establish that the claim is true.
- "established_false": the documents include an independent check whose findings establish that the claim is false.
- "not_established": neither of the above.
Give a one-sentence reason for each status. Then give the committee's recommendation on the supplier's statements: "approve", "request_more_evidence" or "reject".

Claims: Q_obs, Q_welfare, Q_cause, R, S (as labelled in Section 1).

Respond with JSON only, in this format:
{"claims": {"Q_obs": {"status": "...", "reason": "..."}, "Q_welfare": {"status": "...", "reason": "..."}, "Q_cause": {"status": "...", "reason": "..."}, "R": {"status": "...", "reason": "..."}, "S": {"status": "...", "reason": "..."}}, "recommendation": "..."}
~~~~

### belief context  `sha256:5ffd3e344340ffc6`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Fallowfield Cattery. Animals: cats (held for rehoming under a charity contract).
The supplier states:
[Q_obs] The recorded share of cats at Fallowfield Cattery that lost more than 10% of their admission weight in their first 14 days was lower for cats admitted in 2025 than for cats admitted in 2024.
[Q_welfare] The overall welfare of the cats at Fallowfield Cattery improved from 2024 to 2025.
[Q_cause] This reduction in recorded weight loss was caused by the hiding boxes and raised shelves.
[R] Fallowfield Cattery passed its 2026 water-hygiene inspection.
[S] Throughout 2025, every cat pen in use at Fallowmead Cattery, a sister site, also contained a hiding box and a raised shelf at every daily cleaning check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every cat pen in use at Fallowfield Cattery contained a hiding box and a raised shelf at every daily cleaning check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of cats that lost more than 10% of their admission weight in their first 14 days between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of cats that lost more than 10% of their admission weight in their first 14 days.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of cats that lost more than 10% of their admission weight in their first 14 days at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## B  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | T | T | The record's item checked and finding cover the stated practice at this facility. |
| Q_obs | NE | NE | The audit checked a practice, not outcome records. A confirmed practice does not show that the indicator changed (audit scope). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | The record checks the practice at this facility only, not at the sister site (place scope). |

Belief gold p(Q_obs): 0.75

Hashes: attribution `sha256:2ad49e3d70065d66`; belief `sha256:29bce4d571af987c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Item checked: Hiding boxes and raised shelves in every cat pen in use at every daily cleaning check in 2025
Method: Review of the 2025 daily cleaning-check sheets for every pen, checked against the admissions register and pen allocation records
Finding: Daily cleaning-check sheets for 2025 were complete and recorded a hiding box and a raised shelf in every pen in use at every check.
Status: Confirmed
~~~~

## C  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | T | T | The record's item checked and finding cover the stated practice at this facility. |
| Q_obs | NE | NE | The audit checked a practice, not outcome records. A confirmed practice does not show that the indicator changed (audit scope). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | The record checks the practice at this facility only, not at the sister site (place scope). |

Belief gold p(Q_obs): 0.75

Hashes: attribution `sha256:4d69a54c5eb350ea`; belief `sha256:58bfd3bbc7495a83`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Item checked: Hiding boxes and raised shelves in every cat pen in use at every daily cleaning check in 2025
Method: Review of the 2025 daily cleaning-check sheets for every pen, checked against the admissions register and pen allocation records
Finding: Daily cleaning-check sheets for 2025 were complete and recorded a hiding box and a raised shelf in every pen in use at every check.
Status: Confirmed

Coverage: This audit assessed hiding boxes and raised shelves only. It did not assess body weight records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
~~~~

## C_prime  (secondary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | T | T | The record's item checked and finding cover the stated practice at this facility. |
| Q_obs | NE | NE | The audit checked a practice, not outcome records. A confirmed practice does not show that the indicator changed (audit scope). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | The record checks the practice at this facility only, not at the sister site (place scope). |

Belief gold p(Q_obs): 0.75

Hashes: attribution `sha256:1f84abe7cc97ddf6`; belief `sha256:2c267632edf4cfdd`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Item checked: Hiding boxes and raised shelves in every cat pen in use at every daily cleaning check in 2025
Method: Review of the 2025 daily cleaning-check sheets for every pen, checked against the admissions register and pen allocation records
Finding: Daily cleaning-check sheets for 2025 were complete and recorded a hiding box and a raised shelf in every pen in use at every check.
Status: Confirmed

Coverage:
  Assessed: hiding boxes and raised shelves
  Not assessed: body weight records; other animal-based outcomes; cause of any change in animal outcomes
~~~~

## D1  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks fire/building safety, not the practice. |
| Q_obs | NE | NE | No record in the file measures the indicator. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | T | T | The record's item checked and finding cover the stated inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.65

Hashes: attribution `sha256:1fc3a147d5ec7494`; belief `sha256:60d6799e530f8604`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Item checked: The hot-water cylinder, cold-water tank and outlets in the kitchen and laundry
Method: On-site temperature checks at every outlet, with review of the water-hygiene log book
Finding: All water services inspected met the applicable regulatory requirements.
Status: Confirmed
~~~~

## D2  (secondary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks the practice at the sister site, not at this facility (place scope). |
| Q_obs | NE | NE | The audit checked a practice, not outcome records. A confirmed practice does not show that the indicator changed (audit scope). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | T | T | The record checks the practice at the sister site. |

Belief gold p(Q_obs): 0.65

Hashes: attribution `sha256:26d42be5faf984f8`; belief `sha256:6dbe9f6e44f0ac45`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowmead Cattery
Date: 28 April 2026
Item checked: Hiding boxes and raised shelves in every cat pen in use at every daily cleaning check in 2025
Method: Review of the 2025 daily cleaning-check sheets for every pen, checked against the admissions register and pen allocation records
Finding: Daily cleaning-check sheets at Fallowmead Cattery for 2025 were complete and recorded a hiding box and a raised shelf in every pen in use at every check.
Status: Confirmed
~~~~

## E / improved  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | T | T | The audit confirms the records are complete and accurate, and the recorded share fell from 2024 to 2025. Q_obs is a claim about the recorded share, so it is established (observed change). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | The records show an observed fall but contain no comparison group or control of other factors, so they cannot show the practice caused it (observed change is not causal improvement). |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 1.0

Hashes: attribution `sha256:46f64a778a3c2cc0`; belief `sha256:d78ee1c642011d2c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Item checked: Admission and day-14 body weights for all cats admitted in 2024 and 2025 and held at least 14 days
Method: Review of the veterinary nurse's weighing records for every cat admitted in both years and held at least 14 days, checked against the admissions register and the attending veterinary practice's clinical notes
Finding: Recorded share of cats that lost more than 10% of their admission weight by day 14: 15% for cats admitted in 2024; 8% for cats admitted in 2025. Records were complete and matched the admissions register and clinical notes for both years.
Status: Confirmed
~~~~

## E / worsened  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audit confirms the records, and the recorded share rose from 2024 to 2025, so the stated reduction did not occur. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

Hashes: attribution `sha256:696ffabc588b85ec`; belief `sha256:c5295d9a005e852e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Item checked: Admission and day-14 body weights for all cats admitted in 2024 and 2025 and held at least 14 days
Method: Review of the veterinary nurse's weighing records for every cat admitted in both years and held at least 14 days, checked against the admissions register and the attending veterinary practice's clinical notes
Finding: Recorded share of cats that lost more than 10% of their admission weight by day 14: 8% for cats admitted in 2024; 15% for cats admitted in 2025. Records were complete and matched the admissions register and clinical notes for both years.
Status: Confirmed
~~~~

## E / unchanged  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audit confirms the records, and the recorded share unchanged from 2024 to 2025, so the stated reduction did not occur. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

Hashes: attribution `sha256:7e9cb7b5fdb8a82f`; belief `sha256:c04d631efc65865f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Item checked: Admission and day-14 body weights for all cats admitted in 2024 and 2025 and held at least 14 days
Method: Review of the veterinary nurse's weighing records for every cat admitted in both years and held at least 14 days, checked against the admissions register and the attending veterinary practice's clinical notes
Finding: Recorded share of cats that lost more than 10% of their admission weight by day 14: 15% for cats admitted in 2024; 15% for cats admitted in 2025. Records were complete and matched the admissions register and clinical notes for both years.
Status: Confirmed
~~~~

## E_scope / improved  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | T | T | The audit confirms the records are complete and accurate, and the recorded share fell from 2024 to 2025. Q_obs is a claim about the recorded share, so it is established (observed change). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | The records show an observed fall but contain no comparison group or control of other factors, so they cannot show the practice caused it (observed change is not causal improvement). |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 1.0

Hashes: attribution `sha256:9b25068f81f321ea`; belief `sha256:e226609f2f785f07`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Item checked: Admission and day-14 body weights for all cats admitted in 2024 and 2025 and held at least 14 days
Method: Review of the veterinary nurse's weighing records for every cat admitted in both years and held at least 14 days, checked against the admissions register and the attending veterinary practice's clinical notes
Finding: Recorded share of cats that lost more than 10% of their admission weight by day 14: 15% for cats admitted in 2024; 8% for cats admitted in 2025. Records were complete and matched the admissions register and clinical notes for both years.
Status: Confirmed

Coverage: This audit assessed body weight records only. It did not assess hiding boxes and raised shelves or any other practice, and it did not assess the cause of any change in animal outcomes.
~~~~

## E_scope / worsened  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audit confirms the records, and the recorded share rose from 2024 to 2025, so the stated reduction did not occur. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

Hashes: attribution `sha256:e332a4412b261e15`; belief `sha256:ee7682d172d0a751`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Item checked: Admission and day-14 body weights for all cats admitted in 2024 and 2025 and held at least 14 days
Method: Review of the veterinary nurse's weighing records for every cat admitted in both years and held at least 14 days, checked against the admissions register and the attending veterinary practice's clinical notes
Finding: Recorded share of cats that lost more than 10% of their admission weight by day 14: 8% for cats admitted in 2024; 15% for cats admitted in 2025. Records were complete and matched the admissions register and clinical notes for both years.
Status: Confirmed

Coverage: This audit assessed body weight records only. It did not assess hiding boxes and raised shelves or any other practice, and it did not assess the cause of any change in animal outcomes.
~~~~

## E_scope / unchanged  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audit confirms the records, and the recorded share unchanged from 2024 to 2025, so the stated reduction did not occur. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

Hashes: attribution `sha256:5ccd2a3814e2ffe9`; belief `sha256:6cb69b7a41d58cbc`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Item checked: Admission and day-14 body weights for all cats admitted in 2024 and 2025 and held at least 14 days
Method: Review of the veterinary nurse's weighing records for every cat admitted in both years and held at least 14 days, checked against the admissions register and the attending veterinary practice's clinical notes
Finding: Recorded share of cats that lost more than 10% of their admission weight by day 14: 15% for cats admitted in 2024; 15% for cats admitted in 2025. Records were complete and matched the admissions register and clinical notes for both years.
Status: Confirmed

Coverage: This audit assessed body weight records only. It did not assess hiding boxes and raised shelves or any other practice, and it did not assess the cause of any change in animal outcomes.
~~~~

## V  (exploratory)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The stamp names no item checked, method or finding, so it establishes no specific claim. |
| Q_obs | NE | NE | No record in the file measures the indicator. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): excluded

Hashes: attribution `sha256:5cb0115b8e833e06`; belief `sha256:5232d9e8b8146da9`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Linden & Marsh Animal Care Audits
Audit reference: LMACA/26/0412
Site: Fallowfield Cattery
Date: 28 April 2026
Status: Verified ✓
~~~~
