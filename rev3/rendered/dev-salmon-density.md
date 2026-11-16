# Rendered stimuli: `dev-salmon-density` (extension set)

Synthetic case; pending expert review. Contexts are separate conversations.
A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block
shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: stimuli_ext.jsonl.

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

### attribution context  `sha256:9e5c35017f0e4fd0`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Camas Ruadh Marine Site. Animals: Atlantic salmon (marine grow-out).
The supplier states:
[P] Throughout 2025, the monthly recorded stocking density in every pen at Camas Ruadh Marine Site was at or below 15 kg/m³.
[Q_obs] The recorded share of fish from Camas Ruadh Marine Site with severe fin damage at harvest was lower for 2025 harvests than for 2024 harvests.
[Q_welfare] The overall welfare of the fish at Camas Ruadh Marine Site improved from 2024 to 2025.
[Q_cause] This reduction in recorded fin damage was caused by the lower stocking density.
[R] Camas Ruadh Marine Site passed its 2026 navigational marking inspection.
[S] Throughout 2025, the monthly recorded stocking density in every pen at Camas Ruadh North, a sister site, was also at or below 15 kg/m³.

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

### belief context  `sha256:cca21b8c1bf1c995`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Camas Ruadh Marine Site. Animals: Atlantic salmon (marine grow-out).
The supplier states:
[P] Throughout 2025, the monthly recorded stocking density in every pen at Camas Ruadh Marine Site was at or below 15 kg/m³.
[Q_obs] The recorded share of fish from Camas Ruadh Marine Site with severe fin damage at harvest was lower for 2025 harvests than for 2024 harvests.
[Q_welfare] The overall welfare of the fish at Camas Ruadh Marine Site improved from 2024 to 2025.
[Q_cause] This reduction in recorded fin damage was caused by the lower stocking density.
[R] Camas Ruadh Marine Site passed its 2026 navigational marking inspection.
[S] Throughout 2025, the monthly recorded stocking density in every pen at Camas Ruadh North, a sister site, was also at or below 15 kg/m³.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, the monthly recorded stocking density in every pen at Camas Ruadh Marine Site was at or below 15 kg/m³." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of fish with severe fin damage at harvest between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of fish with severe fin damage at harvest.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of fish with severe fin damage at harvest at this facility.
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

### attribution context  `sha256:389f3cc6a0ca737f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Camas Ruadh Marine Site. Animals: Atlantic salmon (marine grow-out).
The supplier states:
[Q_obs] The recorded share of fish from Camas Ruadh Marine Site with severe fin damage at harvest was lower for 2025 harvests than for 2024 harvests.
[Q_welfare] The overall welfare of the fish at Camas Ruadh Marine Site improved from 2024 to 2025.
[Q_cause] This reduction in recorded fin damage was caused by the lower stocking density.
[R] Camas Ruadh Marine Site passed its 2026 navigational marking inspection.
[S] Throughout 2025, the monthly recorded stocking density in every pen at Camas Ruadh North, a sister site, was also at or below 15 kg/m³.

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

### belief context  `sha256:a74af4ad5bab8cca`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Camas Ruadh Marine Site. Animals: Atlantic salmon (marine grow-out).
The supplier states:
[Q_obs] The recorded share of fish from Camas Ruadh Marine Site with severe fin damage at harvest was lower for 2025 harvests than for 2024 harvests.
[Q_welfare] The overall welfare of the fish at Camas Ruadh Marine Site improved from 2024 to 2025.
[Q_cause] This reduction in recorded fin damage was caused by the lower stocking density.
[R] Camas Ruadh Marine Site passed its 2026 navigational marking inspection.
[S] Throughout 2025, the monthly recorded stocking density in every pen at Camas Ruadh North, a sister site, was also at or below 15 kg/m³.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, the monthly recorded stocking density in every pen at Camas Ruadh Marine Site was at or below 15 kg/m³." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of fish with severe fin damage at harvest between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of fish with severe fin damage at harvest.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of fish with severe fin damage at harvest at this facility.
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

Hashes: attribution `sha256:59ceb205ce10d54b`; belief `sha256:36d49e4dae9b2449`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Item checked: Monthly recorded stocking density in every stocked pen for each month of 2025
Method: Review of 2025 monthly biomass estimates from fish-counter and sample-weighing records, and of pen net volumes, for every pen, checked against feed delivery and harvest weight records
Finding: The highest monthly stocking density recorded in any pen during 2025 was 13.6 kg/m³, at or below the 15 kg/m³ limit.
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

Hashes: attribution `sha256:6dd64cde7d8c11ff`; belief `sha256:848d4ea214d0291b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Item checked: Monthly recorded stocking density in every stocked pen for each month of 2025
Method: Review of 2025 monthly biomass estimates from fish-counter and sample-weighing records, and of pen net volumes, for every pen, checked against feed delivery and harvest weight records
Finding: The highest monthly stocking density recorded in any pen during 2025 was 13.6 kg/m³, at or below the 15 kg/m³ limit.
Status: Confirmed

Coverage: This audit assessed stocking density in pens only. It did not assess fin condition records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:1eb052e572ea9a3c`; belief `sha256:082fbbd6c6ca8b4b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Item checked: Monthly recorded stocking density in every stocked pen for each month of 2025
Method: Review of 2025 monthly biomass estimates from fish-counter and sample-weighing records, and of pen net volumes, for every pen, checked against feed delivery and harvest weight records
Finding: The highest monthly stocking density recorded in any pen during 2025 was 13.6 kg/m³, at or below the 15 kg/m³ limit.
Status: Confirmed

Coverage:
  Assessed: stocking density in pens
  Not assessed: fin condition records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:daa64ee52e7cdfcd`; belief `sha256:0a461b2725e9b200`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Item checked: Navigation lights, marker buoys and site boundary markings
Method: On-site inspection from a survey vessel, with review of the navigation-light maintenance log
Finding: All navigational markings inspected met the applicable regulatory requirements.
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

Hashes: attribution `sha256:6c1fbe0daccb3e76`; belief `sha256:af7c65e196b7e1d5`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh North
Date: 9 April 2026
Item checked: Monthly recorded stocking density in every stocked pen for each month of 2025
Method: Review of 2025 monthly biomass estimates from fish-counter and sample-weighing records, and of pen net volumes, for every pen, checked against feed delivery and harvest weight records
Finding: The highest monthly stocking density recorded in any pen at Camas Ruadh North during 2025 was 14.1 kg/m³, at or below the 15 kg/m³ limit.
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

Hashes: attribution `sha256:9a9356062a9ccef9`; belief `sha256:80cc2dcf1f94fdfd`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Item checked: Fin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's quality grading reports (200 fish graded per harvest batch) for every batch in both years, checked against the plant's grading database
Finding: Recorded share of graded fish with severe fin damage (score 3 or 4 on any fin): 13.2% for 2024 harvests; 7.5% for 2025 harvests. Records were complete and matched the grading database for both years.
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

Hashes: attribution `sha256:e9feaf7bdc1c194d`; belief `sha256:4dd691b90506fc8f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Item checked: Fin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's quality grading reports (200 fish graded per harvest batch) for every batch in both years, checked against the plant's grading database
Finding: Recorded share of graded fish with severe fin damage (score 3 or 4 on any fin): 7.5% for 2024 harvests; 13.2% for 2025 harvests. Records were complete and matched the grading database for both years.
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

Hashes: attribution `sha256:18d6da75cb58cdc2`; belief `sha256:9e513e7c70a3cbc3`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Item checked: Fin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's quality grading reports (200 fish graded per harvest batch) for every batch in both years, checked against the plant's grading database
Finding: Recorded share of graded fish with severe fin damage (score 3 or 4 on any fin): 13.2% for 2024 harvests; 13.2% for 2025 harvests. Records were complete and matched the grading database for both years.
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

Hashes: attribution `sha256:beed893b178db0f3`; belief `sha256:4c3737704dca1f6d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Item checked: Fin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's quality grading reports (200 fish graded per harvest batch) for every batch in both years, checked against the plant's grading database
Finding: Recorded share of graded fish with severe fin damage (score 3 or 4 on any fin): 13.2% for 2024 harvests; 7.5% for 2025 harvests. Records were complete and matched the grading database for both years.
Status: Confirmed

Coverage: This audit assessed fin condition records only. It did not assess stocking density in pens or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:078b0c771e348b59`; belief `sha256:d2c131513d5d8b9e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Item checked: Fin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's quality grading reports (200 fish graded per harvest batch) for every batch in both years, checked against the plant's grading database
Finding: Recorded share of graded fish with severe fin damage (score 3 or 4 on any fin): 7.5% for 2024 harvests; 13.2% for 2025 harvests. Records were complete and matched the grading database for both years.
Status: Confirmed

Coverage: This audit assessed fin condition records only. It did not assess stocking density in pens or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:7c5635d37a432779`; belief `sha256:eb1f3a107aeb41fa`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Item checked: Fin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's quality grading reports (200 fish graded per harvest batch) for every batch in both years, checked against the plant's grading database
Finding: Recorded share of graded fish with severe fin damage (score 3 or 4 on any fin): 13.2% for 2024 harvests; 13.2% for 2025 harvests. Records were complete and matched the grading database for both years.
Status: Confirmed

Coverage: This audit assessed fin condition records only. It did not assess stocking density in pens or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:a2cc1335ae7fa0b5`; belief `sha256:3d7066aa46793aa1`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordlys Aquaculture Certification AS
Audit reference: NAC-SAL-2026-0081
Site: Camas Ruadh Marine Site
Date: 9 April 2026
Status: Verified ✓
~~~~
