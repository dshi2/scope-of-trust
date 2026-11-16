# Rendered stimuli: `dev-broiler-density`

Synthetic case; pending expert review. Contexts are separate conversations.
A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block
shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: stimuli_dev.jsonl.

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

### attribution context  `sha256:bc1ffb68b52a4c38`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Hollin Brook Farm was stocked at no more than 30 kg/m².
[Q_obs] The recorded share of birds from Hollin Brook Farm with footpad lesions was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Throughout 2025, every flock at Hollin Brook North, a sister site, was also stocked at no more than 30 kg/m².

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

### belief context  `sha256:e6ffb9c3cceb6087`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Hollin Brook Farm was stocked at no more than 30 kg/m².
[Q_obs] The recorded share of birds from Hollin Brook Farm with footpad lesions was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Throughout 2025, every flock at Hollin Brook North, a sister site, was also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Hollin Brook Farm was stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with footpad lesions at this facility.
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

### attribution context  `sha256:03e9842f19d1c6d0`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[Q_obs] The recorded share of birds from Hollin Brook Farm with footpad lesions was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Throughout 2025, every flock at Hollin Brook North, a sister site, was also stocked at no more than 30 kg/m².

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

### belief context  `sha256:ccbab83291485965`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[Q_obs] The recorded share of birds from Hollin Brook Farm with footpad lesions was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Throughout 2025, every flock at Hollin Brook North, a sister site, was also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Hollin Brook Farm was stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with footpad lesions at this facility.
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

Hashes: attribution `sha256:92058cb68eef68cf`; belief `sha256:5658d5dedf4bb38a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Stocking density of every flock housed at any time during 2025
Method: Review of placement, mortality and slaughter-weight records for every flock housed during 2025, checked against feed and delivery invoices
Finding: The highest stocking density recorded for any flock housed during 2025 was 29.1 kg/m², within the 30 kg/m² limit.
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

Hashes: attribution `sha256:81982d0105a2d7ff`; belief `sha256:5f6242706ace0a1b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Stocking density of every flock housed at any time during 2025
Method: Review of placement, mortality and slaughter-weight records for every flock housed during 2025, checked against feed and delivery invoices
Finding: The highest stocking density recorded for any flock housed during 2025 was 29.1 kg/m², within the 30 kg/m² limit.
Status: Confirmed

Coverage: This audit assessed stocking density only. It did not assess footpad lesion records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:6ea61a786438f34f`; belief `sha256:490fad4aaec22f68`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Stocking density of every flock housed at any time during 2025
Method: Review of placement, mortality and slaughter-weight records for every flock housed during 2025, checked against feed and delivery invoices
Finding: The highest stocking density recorded for any flock housed during 2025 was 29.1 kg/m², within the 30 kg/m² limit.
Status: Confirmed

Coverage:
  Assessed: stocking density
  Not assessed: footpad lesion records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:753319effe6e5b08`; belief `sha256:1272b4bbf7ae977a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Fire-safety systems in all six houses and the feed store
Method: On-site inspection of alarms, extinguishers, emergency exits and electrical panels
Finding: All fire-safety systems inspected met the applicable regulatory requirements.
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

Hashes: attribution `sha256:bd39d4f67d0b9a69`; belief `sha256:870f0c5fc0a5ee50`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook North
Date: 12 March 2026
Item checked: Stocking density of every flock housed at any time during 2025
Method: Review of placement, mortality and slaughter-weight records for every flock housed during 2025, checked against feed and delivery invoices
Finding: The highest stocking density recorded for any flock housed at Hollin Brook North during 2025 was 28.7 kg/m², within the 30 kg/m² limit.
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

Hashes: attribution `sha256:e2c3f24ef6fe34c0`; belief `sha256:889d0156516c9749`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion records for all flocks slaughtered in 2024 and 2025
Method: Review of processing-plant footpad scoring reports for every flock in both years, checked against the plant's own records
Finding: Recorded share of birds with footpad lesions (score 1–2): 18.0% in 2024; 9.4% in 2025. Records were complete and matched the plant's records for both years.
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

Hashes: attribution `sha256:c268db6d42f1d2fb`; belief `sha256:bccd1f5a40e60c25`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion records for all flocks slaughtered in 2024 and 2025
Method: Review of processing-plant footpad scoring reports for every flock in both years, checked against the plant's own records
Finding: Recorded share of birds with footpad lesions (score 1–2): 9.4% in 2024; 18.0% in 2025. Records were complete and matched the plant's records for both years.
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

Hashes: attribution `sha256:f69613224a464e11`; belief `sha256:0296ed09e819f353`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion records for all flocks slaughtered in 2024 and 2025
Method: Review of processing-plant footpad scoring reports for every flock in both years, checked against the plant's own records
Finding: Recorded share of birds with footpad lesions (score 1–2): 18.0% in 2024; 18.0% in 2025. Records were complete and matched the plant's records for both years.
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

Hashes: attribution `sha256:3238a99efc70e6ac`; belief `sha256:e0f856164a4d6cfc`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion records for all flocks slaughtered in 2024 and 2025
Method: Review of processing-plant footpad scoring reports for every flock in both years, checked against the plant's own records
Finding: Recorded share of birds with footpad lesions (score 1–2): 18.0% in 2024; 9.4% in 2025. Records were complete and matched the plant's records for both years.
Status: Confirmed

Coverage: This audit assessed footpad lesion records only. It did not assess stocking density or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:bfabff0b267e6f56`; belief `sha256:4a057f824c536ae6`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion records for all flocks slaughtered in 2024 and 2025
Method: Review of processing-plant footpad scoring reports for every flock in both years, checked against the plant's own records
Finding: Recorded share of birds with footpad lesions (score 1–2): 9.4% in 2024; 18.0% in 2025. Records were complete and matched the plant's records for both years.
Status: Confirmed

Coverage: This audit assessed footpad lesion records only. It did not assess stocking density or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:a13446a0717bb71d`; belief `sha256:a78e6afbdcb49533`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion records for all flocks slaughtered in 2024 and 2025
Method: Review of processing-plant footpad scoring reports for every flock in both years, checked against the plant's own records
Finding: Recorded share of birds with footpad lesions (score 1–2): 18.0% in 2024; 18.0% in 2025. Records were complete and matched the plant's records for both years.
Status: Confirmed

Coverage: This audit assessed footpad lesion records only. It did not assess stocking density or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:873af9a7c039ac9e`; belief `sha256:6b552e05f774b869`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Status: Verified ✓
~~~~
