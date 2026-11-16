# Rendered stimuli: `dev-pig-grouphousing`

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

### attribution context  `sha256:79b7dd90a7b092d1`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Thornfield Pig Unit. Animals: pigs (sows).
The supplier states:
[P] Throughout 2025, every sow at Thornfield Pig Unit that was pregnant at any time during the year, including sows served in late 2024, was kept in a group from four weeks after service until one week before farrowing.
[Q_obs] The recorded share of lame sows at Thornfield Pig Unit was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the sows at Thornfield Pig Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by group housing.
[R] Thornfield Pig Unit passed its 2026 slurry-store structural inspection.
[S] Throughout 2025, every sow at Thornfield East, a sister site, that was pregnant at any time during the year was also kept in a group from four weeks after service until one week before farrowing.

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

### belief context  `sha256:80038ddaf56931f3`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Thornfield Pig Unit. Animals: pigs (sows).
The supplier states:
[P] Throughout 2025, every sow at Thornfield Pig Unit that was pregnant at any time during the year, including sows served in late 2024, was kept in a group from four weeks after service until one week before farrowing.
[Q_obs] The recorded share of lame sows at Thornfield Pig Unit was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the sows at Thornfield Pig Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by group housing.
[R] Thornfield Pig Unit passed its 2026 slurry-store structural inspection.
[S] Throughout 2025, every sow at Thornfield East, a sister site, that was pregnant at any time during the year was also kept in a group from four weeks after service until one week before farrowing.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every sow at Thornfield Pig Unit that was pregnant at any time during the year, including sows served in late 2024, was kept in a group from four weeks after service until one week before farrowing." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of lame sows between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of lame sows.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of lame sows at this facility.
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

### attribution context  `sha256:26411999c5bd0b14`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Thornfield Pig Unit. Animals: pigs (sows).
The supplier states:
[Q_obs] The recorded share of lame sows at Thornfield Pig Unit was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the sows at Thornfield Pig Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by group housing.
[R] Thornfield Pig Unit passed its 2026 slurry-store structural inspection.
[S] Throughout 2025, every sow at Thornfield East, a sister site, that was pregnant at any time during the year was also kept in a group from four weeks after service until one week before farrowing.

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

### belief context  `sha256:0e7bb34ae0c77e81`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Thornfield Pig Unit. Animals: pigs (sows).
The supplier states:
[Q_obs] The recorded share of lame sows at Thornfield Pig Unit was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the sows at Thornfield Pig Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by group housing.
[R] Thornfield Pig Unit passed its 2026 slurry-store structural inspection.
[S] Throughout 2025, every sow at Thornfield East, a sister site, that was pregnant at any time during the year was also kept in a group from four weeks after service until one week before farrowing.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every sow at Thornfield Pig Unit that was pregnant at any time during the year, including sows served in late 2024, was kept in a group from four weeks after service until one week before farrowing." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of lame sows between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of lame sows.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of lame sows at this facility.
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

Hashes: attribution `sha256:e855736c7f310e23`; belief `sha256:6b277b959b0ca46a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Item checked: Housing of every sow pregnant at any time during 2025, including sows served from September 2024
Method: Review of sow movement records, pen allocation sheets and service records from September 2024 to December 2025 for every sow pregnant during 2025
Finding: Every sow pregnant at any time during 2025, including those served in late 2024, was recorded in group housing from four weeks after service until one week before farrowing; no individual stall use was recorded.
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

Hashes: attribution `sha256:8b725de3f6428de8`; belief `sha256:78ac81a9cb168da5`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Item checked: Housing of every sow pregnant at any time during 2025, including sows served from September 2024
Method: Review of sow movement records, pen allocation sheets and service records from September 2024 to December 2025 for every sow pregnant during 2025
Finding: Every sow pregnant at any time during 2025, including those served in late 2024, was recorded in group housing from four weeks after service until one week before farrowing; no individual stall use was recorded.
Status: Confirmed

Coverage: This audit assessed gestation housing only. It did not assess sow lameness records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:74a0dd7c57f4c0e1`; belief `sha256:70b6405e1532f7a6`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Item checked: Housing of every sow pregnant at any time during 2025, including sows served from September 2024
Method: Review of sow movement records, pen allocation sheets and service records from September 2024 to December 2025 for every sow pregnant during 2025
Finding: Every sow pregnant at any time during 2025, including those served in late 2024, was recorded in group housing from four weeks after service until one week before farrowing; no individual stall use was recorded.
Status: Confirmed

Coverage:
  Assessed: gestation housing
  Not assessed: sow lameness records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:9c421476aef29c4b`; belief `sha256:e8b80eebad8f3013`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Item checked: Structural integrity of the two slurry stores
Method: On-site inspection of walls, joints and covers, and review of the engineer's report
Finding: Both slurry stores inspected met the applicable regulatory requirements.
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

Hashes: attribution `sha256:150df44f1537ada3`; belief `sha256:894d041946eefb8d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield East
Date: 17 June 2026
Item checked: Housing of every sow pregnant at any time during 2025, including sows served from September 2024
Method: Review of sow movement records, pen allocation sheets and service records from September 2024 to December 2025 for every sow pregnant during 2025
Finding: Every sow pregnant at Thornfield East at any time during 2025, including those served in late 2024, was recorded in group housing from four weeks after service until one week before farrowing; no individual stall use was recorded.
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

Hashes: attribution `sha256:63f3f1f7314f85f2`; belief `sha256:679e87135c98eea3`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Item checked: Sow lameness records for 2024 and 2025
Method: Review of quarterly lameness scoring sheets for all sows in both years, checked against the herd health plan
Finding: Recorded share of sows scored lame (score 2 or higher), averaged over quarterly scorings: 15% in 2024; 8% in 2025. Records were complete and matched the herd health plan for both years.
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

Hashes: attribution `sha256:486a8dc5cc25cb63`; belief `sha256:054b0e48104bd368`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Item checked: Sow lameness records for 2024 and 2025
Method: Review of quarterly lameness scoring sheets for all sows in both years, checked against the herd health plan
Finding: Recorded share of sows scored lame (score 2 or higher), averaged over quarterly scorings: 8% in 2024; 15% in 2025. Records were complete and matched the herd health plan for both years.
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

Hashes: attribution `sha256:6c0daff5de53ce78`; belief `sha256:554a4f8c29e01181`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Item checked: Sow lameness records for 2024 and 2025
Method: Review of quarterly lameness scoring sheets for all sows in both years, checked against the herd health plan
Finding: Recorded share of sows scored lame (score 2 or higher), averaged over quarterly scorings: 15% in 2024; 15% in 2025. Records were complete and matched the herd health plan for both years.
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

Hashes: attribution `sha256:2b5795021f013ee4`; belief `sha256:a266ea42a3e60d4c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Item checked: Sow lameness records for 2024 and 2025
Method: Review of quarterly lameness scoring sheets for all sows in both years, checked against the herd health plan
Finding: Recorded share of sows scored lame (score 2 or higher), averaged over quarterly scorings: 15% in 2024; 8% in 2025. Records were complete and matched the herd health plan for both years.
Status: Confirmed

Coverage: This audit assessed sow lameness records only. It did not assess gestation housing or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:54b45dee1bdbd10b`; belief `sha256:b4480a18755d38c7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Item checked: Sow lameness records for 2024 and 2025
Method: Review of quarterly lameness scoring sheets for all sows in both years, checked against the herd health plan
Finding: Recorded share of sows scored lame (score 2 or higher), averaged over quarterly scorings: 8% in 2024; 15% in 2025. Records were complete and matched the herd health plan for both years.
Status: Confirmed

Coverage: This audit assessed sow lameness records only. It did not assess gestation housing or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:84916b322bcf19bb`; belief `sha256:0c2ed08816559c8c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Item checked: Sow lameness records for 2024 and 2025
Method: Review of quarterly lameness scoring sheets for all sows in both years, checked against the herd health plan
Finding: Recorded share of sows scored lame (score 2 or higher), averaged over quarterly scorings: 15% in 2024; 15% in 2025. Records were complete and matched the herd health plan for both years.
Status: Confirmed

Coverage: This audit assessed sow lameness records only. It did not assess gestation housing or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:4ac139d3088c0ca0`; belief `sha256:db7213b9cbbd54eb`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-2041
Site: Thornfield Pig Unit
Date: 17 June 2026
Status: Verified ✓
~~~~
