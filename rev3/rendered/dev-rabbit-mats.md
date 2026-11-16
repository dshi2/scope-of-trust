# Rendered stimuli: `dev-rabbit-mats` (extension set)

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

### attribution context  `sha256:db50f669d6276889`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Larkspur Rabbitry. Animals: rabbits (breeding does).
The supplier states:
[P] Throughout 2025, every breeding doe at Larkspur Rabbitry was kept in a pen with a plastic foot-rest mat covering at least 40% of the floor.
[Q_obs] The recorded share of does at Larkspur Rabbitry with sore hocks was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the rabbits at Larkspur Rabbitry improved from 2024 to 2025.
[Q_cause] This reduction in recorded sore hocks was caused by the foot-rest mats.
[R] Larkspur Rabbitry passed its 2026 standby-generator inspection.
[S] Throughout 2025, every breeding doe at Larkspur Hollow, a sister site, was also kept in a pen with a plastic foot-rest mat covering at least 40% of the floor.

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

### belief context  `sha256:24744bb391907b85`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Larkspur Rabbitry. Animals: rabbits (breeding does).
The supplier states:
[P] Throughout 2025, every breeding doe at Larkspur Rabbitry was kept in a pen with a plastic foot-rest mat covering at least 40% of the floor.
[Q_obs] The recorded share of does at Larkspur Rabbitry with sore hocks was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the rabbits at Larkspur Rabbitry improved from 2024 to 2025.
[Q_cause] This reduction in recorded sore hocks was caused by the foot-rest mats.
[R] Larkspur Rabbitry passed its 2026 standby-generator inspection.
[S] Throughout 2025, every breeding doe at Larkspur Hollow, a sister site, was also kept in a pen with a plastic foot-rest mat covering at least 40% of the floor.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every breeding doe at Larkspur Rabbitry was kept in a pen with a plastic foot-rest mat covering at least 40% of the floor." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of does with sore hocks between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of does with sore hocks.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of does with sore hocks at this facility.
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

### attribution context  `sha256:e261961f39aa478c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Larkspur Rabbitry. Animals: rabbits (breeding does).
The supplier states:
[Q_obs] The recorded share of does at Larkspur Rabbitry with sore hocks was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the rabbits at Larkspur Rabbitry improved from 2024 to 2025.
[Q_cause] This reduction in recorded sore hocks was caused by the foot-rest mats.
[R] Larkspur Rabbitry passed its 2026 standby-generator inspection.
[S] Throughout 2025, every breeding doe at Larkspur Hollow, a sister site, was also kept in a pen with a plastic foot-rest mat covering at least 40% of the floor.

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

### belief context  `sha256:eb4a932dd38208cb`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Larkspur Rabbitry. Animals: rabbits (breeding does).
The supplier states:
[Q_obs] The recorded share of does at Larkspur Rabbitry with sore hocks was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the rabbits at Larkspur Rabbitry improved from 2024 to 2025.
[Q_cause] This reduction in recorded sore hocks was caused by the foot-rest mats.
[R] Larkspur Rabbitry passed its 2026 standby-generator inspection.
[S] Throughout 2025, every breeding doe at Larkspur Hollow, a sister site, was also kept in a pen with a plastic foot-rest mat covering at least 40% of the floor.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every breeding doe at Larkspur Rabbitry was kept in a pen with a plastic foot-rest mat covering at least 40% of the floor." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of does with sore hocks between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of does with sore hocks.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of does with sore hocks at this facility.
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

Hashes: attribution `sha256:de24b225f670c1bd`; belief `sha256:f5cacf403bbf517a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Item checked: Foot-rest mats in every pen used for breeding does during 2025
Method: Review of 2025 pen inventories, mat purchase invoices and the weekly pen maintenance log for every doe pen, with mat areas taken from the supplier's specifications and pen floor plans
Finding: Every doe pen in use during 2025 was fitted with a foot-rest mat covering at least 45% of the floor; the maintenance log recorded no doe pen without a mat at any time in 2025.
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

Hashes: attribution `sha256:5eac1377c9cbb3c0`; belief `sha256:2425782617d6c83e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Item checked: Foot-rest mats in every pen used for breeding does during 2025
Method: Review of 2025 pen inventories, mat purchase invoices and the weekly pen maintenance log for every doe pen, with mat areas taken from the supplier's specifications and pen floor plans
Finding: Every doe pen in use during 2025 was fitted with a foot-rest mat covering at least 45% of the floor; the maintenance log recorded no doe pen without a mat at any time in 2025.
Status: Confirmed

Coverage: This audit assessed foot-rest mats only. It did not assess hock condition records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:5aefc4b9c05f4557`; belief `sha256:09993cf624749e99`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Item checked: Foot-rest mats in every pen used for breeding does during 2025
Method: Review of 2025 pen inventories, mat purchase invoices and the weekly pen maintenance log for every doe pen, with mat areas taken from the supplier's specifications and pen floor plans
Finding: Every doe pen in use during 2025 was fitted with a foot-rest mat covering at least 45% of the floor; the maintenance log recorded no doe pen without a mat at any time in 2025.
Status: Confirmed

Coverage:
  Assessed: foot-rest mats
  Not assessed: hock condition records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:b7fbf6af5da7c352`; belief `sha256:0468d160dfc9b9ef`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Item checked: The standby generator, its fuel tank and the automatic changeover switch
Method: On-site load test of the generator and inspection of the fuel tank and changeover switch
Finding: The generator, fuel tank and changeover switch met the applicable regulatory requirements.
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

Hashes: attribution `sha256:8c1537e021c4fba7`; belief `sha256:a50693a6eb6c1b03`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Hollow
Date: 30 March 2026
Item checked: Foot-rest mats in every pen used for breeding does during 2025
Method: Review of 2025 pen inventories, mat purchase invoices and the weekly pen maintenance log for every doe pen, with mat areas taken from the supplier's specifications and pen floor plans
Finding: Every doe pen in use at Larkspur Hollow during 2025 was fitted with a foot-rest mat covering at least 42% of the floor; the maintenance log recorded no doe pen without a mat at any time in 2025.
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

Hashes: attribution `sha256:703d366bf3629c33`; belief `sha256:346a68ed547f246d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Item checked: Hock condition records for all breeding does in 2024 and 2025
Method: Review of the monthly health-check sheets, on which both hind feet of every doe present are scored, for every month of both years, checked against the doe register
Finding: Recorded share of does with sore hocks (lesion score 2 or higher on either hind foot), averaged over the twelve monthly checks: 16% in 2024; 9% in 2025. Records were complete and matched the doe register for both years.
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

Hashes: attribution `sha256:b87ee64cfc7b1438`; belief `sha256:fd6a946a82a3fe43`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Item checked: Hock condition records for all breeding does in 2024 and 2025
Method: Review of the monthly health-check sheets, on which both hind feet of every doe present are scored, for every month of both years, checked against the doe register
Finding: Recorded share of does with sore hocks (lesion score 2 or higher on either hind foot), averaged over the twelve monthly checks: 9% in 2024; 16% in 2025. Records were complete and matched the doe register for both years.
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

Hashes: attribution `sha256:3c8e1442d651f9cd`; belief `sha256:201fcd1f68ea18d5`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Item checked: Hock condition records for all breeding does in 2024 and 2025
Method: Review of the monthly health-check sheets, on which both hind feet of every doe present are scored, for every month of both years, checked against the doe register
Finding: Recorded share of does with sore hocks (lesion score 2 or higher on either hind foot), averaged over the twelve monthly checks: 16% in 2024; 16% in 2025. Records were complete and matched the doe register for both years.
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

Hashes: attribution `sha256:8632a47427bd6035`; belief `sha256:11d5a75a6db4668b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Item checked: Hock condition records for all breeding does in 2024 and 2025
Method: Review of the monthly health-check sheets, on which both hind feet of every doe present are scored, for every month of both years, checked against the doe register
Finding: Recorded share of does with sore hocks (lesion score 2 or higher on either hind foot), averaged over the twelve monthly checks: 16% in 2024; 9% in 2025. Records were complete and matched the doe register for both years.
Status: Confirmed

Coverage: This audit assessed hock condition records only. It did not assess foot-rest mats or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:0b1f882be916864a`; belief `sha256:93c5aa7fd85e2d5a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Item checked: Hock condition records for all breeding does in 2024 and 2025
Method: Review of the monthly health-check sheets, on which both hind feet of every doe present are scored, for every month of both years, checked against the doe register
Finding: Recorded share of does with sore hocks (lesion score 2 or higher on either hind foot), averaged over the twelve monthly checks: 9% in 2024; 16% in 2025. Records were complete and matched the doe register for both years.
Status: Confirmed

Coverage: This audit assessed hock condition records only. It did not assess foot-rest mats or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:bfbfd61266efceb6`; belief `sha256:748cfb24b8b16918`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Item checked: Hock condition records for all breeding does in 2024 and 2025
Method: Review of the monthly health-check sheets, on which both hind feet of every doe present are scored, for every month of both years, checked against the doe register
Finding: Recorded share of does with sore hocks (lesion score 2 or higher on either hind foot), averaged over the twelve monthly checks: 16% in 2024; 16% in 2025. Records were complete and matched the doe register for both years.
Status: Confirmed

Coverage: This audit assessed hock condition records only. It did not assess foot-rest mats or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:dc9f9289d140197f`; belief `sha256:741c5c54904296e2`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Corvane Livestock Inspection Bureau
Audit reference: CLIB-R-26-0045
Site: Larkspur Rabbitry
Date: 30 March 2026
Status: Verified ✓
~~~~
