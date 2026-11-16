# Rendered stimuli: `dev-feedlot-shade` (expansion batch ba)

Synthetic case; pending expert review. Contexts are separate conversations.
A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block
shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: stimuli_ba.jsonl.

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

### attribution context  `sha256:2163a2f073e4ffc9`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Red Mesa Feedyard. Animals: beef cattle (feedlot).
The supplier states:
[P] Throughout 2025, every occupied pen at Red Mesa Feedyard had shade structures giving at least 2.5 m² of shade per head at the head count in every weekly pen census.
[Q_obs] The recorded share of cattle at Red Mesa Feedyard with high panting scores on summer afternoons was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the cattle at Red Mesa Feedyard improved from 2024 to 2025.
[Q_cause] This reduction in recorded high panting scores was caused by the shade structures.
[R] Red Mesa Feedyard passed its 2026 stormwater runoff-control inspection.
[S] Throughout 2025, every occupied pen at Red Mesa South Yard, a sister site, also had shade structures giving at least 2.5 m² of shade per head at the head count in every weekly pen census.

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

### belief context  `sha256:60fa82c64e20427c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Red Mesa Feedyard. Animals: beef cattle (feedlot).
The supplier states:
[P] Throughout 2025, every occupied pen at Red Mesa Feedyard had shade structures giving at least 2.5 m² of shade per head at the head count in every weekly pen census.
[Q_obs] The recorded share of cattle at Red Mesa Feedyard with high panting scores on summer afternoons was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the cattle at Red Mesa Feedyard improved from 2024 to 2025.
[Q_cause] This reduction in recorded high panting scores was caused by the shade structures.
[R] Red Mesa Feedyard passed its 2026 stormwater runoff-control inspection.
[S] Throughout 2025, every occupied pen at Red Mesa South Yard, a sister site, also had shade structures giving at least 2.5 m² of shade per head at the head count in every weekly pen census.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every occupied pen at Red Mesa Feedyard had shade structures giving at least 2.5 m² of shade per head at the head count in every weekly pen census." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of cattle with high panting scores on summer afternoons between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of cattle with high panting scores on summer afternoons.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of cattle with high panting scores on summer afternoons at this facility.
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

### attribution context  `sha256:c92efe71041756e9`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Red Mesa Feedyard. Animals: beef cattle (feedlot).
The supplier states:
[Q_obs] The recorded share of cattle at Red Mesa Feedyard with high panting scores on summer afternoons was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the cattle at Red Mesa Feedyard improved from 2024 to 2025.
[Q_cause] This reduction in recorded high panting scores was caused by the shade structures.
[R] Red Mesa Feedyard passed its 2026 stormwater runoff-control inspection.
[S] Throughout 2025, every occupied pen at Red Mesa South Yard, a sister site, also had shade structures giving at least 2.5 m² of shade per head at the head count in every weekly pen census.

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

### belief context  `sha256:87a28aebcf49d665`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Red Mesa Feedyard. Animals: beef cattle (feedlot).
The supplier states:
[Q_obs] The recorded share of cattle at Red Mesa Feedyard with high panting scores on summer afternoons was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the cattle at Red Mesa Feedyard improved from 2024 to 2025.
[Q_cause] This reduction in recorded high panting scores was caused by the shade structures.
[R] Red Mesa Feedyard passed its 2026 stormwater runoff-control inspection.
[S] Throughout 2025, every occupied pen at Red Mesa South Yard, a sister site, also had shade structures giving at least 2.5 m² of shade per head at the head count in every weekly pen census.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every occupied pen at Red Mesa Feedyard had shade structures giving at least 2.5 m² of shade per head at the head count in every weekly pen census." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of cattle with high panting scores on summer afternoons between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of cattle with high panting scores on summer afternoons.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of cattle with high panting scores on summer afternoons at this facility.
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

Hashes: attribution `sha256:635bff3ae8c8e942`; belief `sha256:3d87efade1f45686`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Item checked: Shade area per head in every occupied pen in every weekly pen census for 2025
Method: Review of the 52 weekly pen census sheets for 2025, compared with shade-structure drawings giving the shaded area of each pen and with the 2025 shade-cloth repair log
Finding: In every weekly pen census for 2025, each occupied pen had at least 2.7 m² of shade per head; the 2025 repair log recorded no occupied pen with damaged or removed shade cloth.
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

Hashes: attribution `sha256:e8d25af1af5df693`; belief `sha256:a915524bfd7e3aae`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Item checked: Shade area per head in every occupied pen in every weekly pen census for 2025
Method: Review of the 52 weekly pen census sheets for 2025, compared with shade-structure drawings giving the shaded area of each pen and with the 2025 shade-cloth repair log
Finding: In every weekly pen census for 2025, each occupied pen had at least 2.7 m² of shade per head; the 2025 repair log recorded no occupied pen with damaged or removed shade cloth.
Status: Confirmed

Coverage: This audit assessed shade area per head only. It did not assess panting score records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:ed80dece27f70de5`; belief `sha256:340cff514873b5fb`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Item checked: Shade area per head in every occupied pen in every weekly pen census for 2025
Method: Review of the 52 weekly pen census sheets for 2025, compared with shade-structure drawings giving the shaded area of each pen and with the 2025 shade-cloth repair log
Finding: In every weekly pen census for 2025, each occupied pen had at least 2.7 m² of shade per head; the 2025 repair log recorded no occupied pen with damaged or removed shade cloth.
Status: Confirmed

Coverage:
  Assessed: shade area per head
  Not assessed: panting score records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:f46ebe4e85b0f043`; belief `sha256:63bff43cc101b4e6`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Item checked: Runoff holding ponds, settling basins and diversion berms
Method: On-site inspection of pond liners, freeboard markers and berms, and review of the discharge log
Finding: All runoff-control structures inspected met the applicable regulatory requirements.
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

Hashes: attribution `sha256:9e352241f867fae6`; belief `sha256:da7ced08522a0c6f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa South Yard
Date: 14 January 2026
Item checked: Shade area per head in every occupied pen in every weekly pen census for 2025
Method: Review of the 52 weekly pen census sheets for 2025, compared with shade-structure drawings giving the shaded area of each pen and with the 2025 shade-cloth repair log
Finding: In every weekly pen census for 2025, each occupied pen at Red Mesa South Yard had at least 2.6 m² of shade per head; the 2025 repair log recorded no occupied pen with damaged or removed shade cloth.
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

Hashes: attribution `sha256:aa00fa70f8e06588`; belief `sha256:5d01cd07945638ee`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Item checked: Panting score records for every occupied pen from June to September of 2024 and 2025
Method: Review of the panting scores logged at 15:00 each day by the yard's camera-based pen monitoring system, for every occupied pen from June to September of both years, checked against the system's stored image logs and the pen census
Finding: Recorded share of cattle with panting score 2 or higher at 15:00, June to September: 19% in 2024; 11% in 2025. Records were complete and matched the stored image logs for both years.
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

Hashes: attribution `sha256:7591c472854f26cb`; belief `sha256:6a90aa9f3f2e1dcb`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Item checked: Panting score records for every occupied pen from June to September of 2024 and 2025
Method: Review of the panting scores logged at 15:00 each day by the yard's camera-based pen monitoring system, for every occupied pen from June to September of both years, checked against the system's stored image logs and the pen census
Finding: Recorded share of cattle with panting score 2 or higher at 15:00, June to September: 11% in 2024; 19% in 2025. Records were complete and matched the stored image logs for both years.
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

Hashes: attribution `sha256:47e5a73b152feecb`; belief `sha256:a5c6b17d6f35dca9`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Item checked: Panting score records for every occupied pen from June to September of 2024 and 2025
Method: Review of the panting scores logged at 15:00 each day by the yard's camera-based pen monitoring system, for every occupied pen from June to September of both years, checked against the system's stored image logs and the pen census
Finding: Recorded share of cattle with panting score 2 or higher at 15:00, June to September: 19% in 2024; 19% in 2025. Records were complete and matched the stored image logs for both years.
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

Hashes: attribution `sha256:5bf88a9616498efd`; belief `sha256:7578bf36172ca946`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Item checked: Panting score records for every occupied pen from June to September of 2024 and 2025
Method: Review of the panting scores logged at 15:00 each day by the yard's camera-based pen monitoring system, for every occupied pen from June to September of both years, checked against the system's stored image logs and the pen census
Finding: Recorded share of cattle with panting score 2 or higher at 15:00, June to September: 19% in 2024; 11% in 2025. Records were complete and matched the stored image logs for both years.
Status: Confirmed

Coverage: This audit assessed panting score records only. It did not assess shade area per head or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:e1d0f4c2943c0307`; belief `sha256:15263bbee4d7cc57`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Item checked: Panting score records for every occupied pen from June to September of 2024 and 2025
Method: Review of the panting scores logged at 15:00 each day by the yard's camera-based pen monitoring system, for every occupied pen from June to September of both years, checked against the system's stored image logs and the pen census
Finding: Recorded share of cattle with panting score 2 or higher at 15:00, June to September: 11% in 2024; 19% in 2025. Records were complete and matched the stored image logs for both years.
Status: Confirmed

Coverage: This audit assessed panting score records only. It did not assess shade area per head or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:f554622814eeeded`; belief `sha256:8604cf938bd5330f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Item checked: Panting score records for every occupied pen from June to September of 2024 and 2025
Method: Review of the panting scores logged at 15:00 each day by the yard's camera-based pen monitoring system, for every occupied pen from June to September of both years, checked against the system's stored image logs and the pen census
Finding: Recorded share of cattle with panting score 2 or higher at 15:00, June to September: 19% in 2024; 19% in 2025. Records were complete and matched the stored image logs for both years.
Status: Confirmed

Coverage: This audit assessed panting score records only. It did not assess shade area per head or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:0ffe906926ad6455`; belief `sha256:25db1af8413236a0`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Plainsview Beef Audit Services
Audit reference: PBAS-2026-1146
Site: Red Mesa Feedyard
Date: 14 January 2026
Status: Verified ✓
~~~~
