# Rendered stimuli: `dev-seabass-crowding` (batch bb)

Synthetic case; pending expert review. Contexts are separate conversations.
A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block
shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: stimuli_bb.jsonl.

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

### attribution context  `sha256:bab8585b9f0a7df1`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pelagon Bay Marine Farm. Animals: European sea bass (sea cages).
The supplier states:
[P] Throughout 2025, every crowding of fish for grading or harvest at Pelagon Bay Marine Farm lasted no longer than 2 hours, as recorded in the crowding log.
[Q_obs] The recorded share of fish at Pelagon Bay Marine Farm with skin or snout damage was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the fish at Pelagon Bay Marine Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded skin and snout damage was caused by the shorter crowding times.
[R] Pelagon Bay Marine Farm passed its 2026 mooring-system inspection.
[S] Throughout 2025, every crowding of fish for grading or harvest at Pelagon Bay East, a sister site, also lasted no longer than 2 hours, as recorded in the crowding log.

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

### belief context  `sha256:de5df23e9129f605`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pelagon Bay Marine Farm. Animals: European sea bass (sea cages).
The supplier states:
[P] Throughout 2025, every crowding of fish for grading or harvest at Pelagon Bay Marine Farm lasted no longer than 2 hours, as recorded in the crowding log.
[Q_obs] The recorded share of fish at Pelagon Bay Marine Farm with skin or snout damage was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the fish at Pelagon Bay Marine Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded skin and snout damage was caused by the shorter crowding times.
[R] Pelagon Bay Marine Farm passed its 2026 mooring-system inspection.
[S] Throughout 2025, every crowding of fish for grading or harvest at Pelagon Bay East, a sister site, also lasted no longer than 2 hours, as recorded in the crowding log.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every crowding of fish for grading or harvest at Pelagon Bay Marine Farm lasted no longer than 2 hours, as recorded in the crowding log." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of fish with skin or snout damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of fish with skin or snout damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of fish with skin or snout damage at this facility.
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

### attribution context  `sha256:2d4c0bb453f1bce6`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pelagon Bay Marine Farm. Animals: European sea bass (sea cages).
The supplier states:
[Q_obs] The recorded share of fish at Pelagon Bay Marine Farm with skin or snout damage was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the fish at Pelagon Bay Marine Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded skin and snout damage was caused by the shorter crowding times.
[R] Pelagon Bay Marine Farm passed its 2026 mooring-system inspection.
[S] Throughout 2025, every crowding of fish for grading or harvest at Pelagon Bay East, a sister site, also lasted no longer than 2 hours, as recorded in the crowding log.

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

### belief context  `sha256:4d5c5e8431472634`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pelagon Bay Marine Farm. Animals: European sea bass (sea cages).
The supplier states:
[Q_obs] The recorded share of fish at Pelagon Bay Marine Farm with skin or snout damage was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the fish at Pelagon Bay Marine Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded skin and snout damage was caused by the shorter crowding times.
[R] Pelagon Bay Marine Farm passed its 2026 mooring-system inspection.
[S] Throughout 2025, every crowding of fish for grading or harvest at Pelagon Bay East, a sister site, also lasted no longer than 2 hours, as recorded in the crowding log.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every crowding of fish for grading or harvest at Pelagon Bay Marine Farm lasted no longer than 2 hours, as recorded in the crowding log." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of fish with skin or snout damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of fish with skin or snout damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of fish with skin or snout damage at this facility.
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

Hashes: attribution `sha256:9fe0c40f8ae2cd35`; belief `sha256:dda22a846dff1375`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Item checked: Duration of every crowding of fish for grading or harvest, as recorded in the 2025 crowding log
Method: Review of the 2025 crowding log for every cage, with start and release times, checked against the 2025 grading and harvest schedules and well-boat delivery notes
Finding: Every grading and harvest in the 2025 schedules had a crowding log entry; the longest crowding recorded in 2025 lasted 1 hour 40 minutes.
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

Hashes: attribution `sha256:c8811072a3914847`; belief `sha256:97fc6e7d84d5f32c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Item checked: Duration of every crowding of fish for grading or harvest, as recorded in the 2025 crowding log
Method: Review of the 2025 crowding log for every cage, with start and release times, checked against the 2025 grading and harvest schedules and well-boat delivery notes
Finding: Every grading and harvest in the 2025 schedules had a crowding log entry; the longest crowding recorded in 2025 lasted 1 hour 40 minutes.
Status: Confirmed

Coverage: This audit assessed crowding duration only. It did not assess skin and snout condition scores or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:b1a2fdf729564776`; belief `sha256:bc35b02ab23ef06f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Item checked: Duration of every crowding of fish for grading or harvest, as recorded in the 2025 crowding log
Method: Review of the 2025 crowding log for every cage, with start and release times, checked against the 2025 grading and harvest schedules and well-boat delivery notes
Finding: Every grading and harvest in the 2025 schedules had a crowding log entry; the longest crowding recorded in 2025 lasted 1 hour 40 minutes.
Status: Confirmed

Coverage:
  Assessed: crowding duration
  Not assessed: skin and snout condition scores; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:fb08cbc2b9b3d0e7`; belief `sha256:b69b7aaccd682436`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Item checked: Cage moorings, anchor lines and the mooring grid
Method: Diver survey of anchors and mooring lines, with review of the mooring maintenance log
Finding: All moorings and anchor lines examined met the applicable regulatory requirements.
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

Hashes: attribution `sha256:e0a16a452f6a64c2`; belief `sha256:8b3b67cd5f8ddac1`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay East
Date: 23 June 2026
Item checked: Duration of every crowding of fish for grading or harvest, as recorded in the 2025 crowding log
Method: Review of the 2025 crowding log for every cage, with start and release times, checked against the 2025 grading and harvest schedules and well-boat delivery notes
Finding: Every grading and harvest in the 2025 schedules at Pelagon Bay East had a crowding log entry; the longest crowding recorded in 2025 lasted 1 hour 55 minutes.
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

Hashes: attribution `sha256:224f34727f66154e`; belief `sha256:d31b10fb3e4f127c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Item checked: Skin and snout condition scores for every stocked cage in 2024 and 2025
Method: Review of a contracted fish health assessor's reports from four visits per year, at each of which 50 fish per stocked cage were netted and scored, checked against the farm's cage stocking register
Finding: Recorded share of scored fish with skin or snout damage (score 2 or higher), mean of the four visits: 19% in 2024; 11% in 2025. Records were complete and matched the cage stocking register for both years.
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

Hashes: attribution `sha256:f31d9695bc17dacf`; belief `sha256:2d2421dbffc41427`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Item checked: Skin and snout condition scores for every stocked cage in 2024 and 2025
Method: Review of a contracted fish health assessor's reports from four visits per year, at each of which 50 fish per stocked cage were netted and scored, checked against the farm's cage stocking register
Finding: Recorded share of scored fish with skin or snout damage (score 2 or higher), mean of the four visits: 11% in 2024; 19% in 2025. Records were complete and matched the cage stocking register for both years.
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

Hashes: attribution `sha256:568d1d69e7600365`; belief `sha256:92a098a1b38db482`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Item checked: Skin and snout condition scores for every stocked cage in 2024 and 2025
Method: Review of a contracted fish health assessor's reports from four visits per year, at each of which 50 fish per stocked cage were netted and scored, checked against the farm's cage stocking register
Finding: Recorded share of scored fish with skin or snout damage (score 2 or higher), mean of the four visits: 19% in 2024; 19% in 2025. Records were complete and matched the cage stocking register for both years.
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

Hashes: attribution `sha256:7392ab1ba61a9e97`; belief `sha256:70ce3ba5c53cfd27`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Item checked: Skin and snout condition scores for every stocked cage in 2024 and 2025
Method: Review of a contracted fish health assessor's reports from four visits per year, at each of which 50 fish per stocked cage were netted and scored, checked against the farm's cage stocking register
Finding: Recorded share of scored fish with skin or snout damage (score 2 or higher), mean of the four visits: 19% in 2024; 11% in 2025. Records were complete and matched the cage stocking register for both years.
Status: Confirmed

Coverage: This audit assessed skin and snout condition scores only. It did not assess crowding duration or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:604a5e1ddd2e5878`; belief `sha256:a2ccec055751738b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Item checked: Skin and snout condition scores for every stocked cage in 2024 and 2025
Method: Review of a contracted fish health assessor's reports from four visits per year, at each of which 50 fish per stocked cage were netted and scored, checked against the farm's cage stocking register
Finding: Recorded share of scored fish with skin or snout damage (score 2 or higher), mean of the four visits: 11% in 2024; 19% in 2025. Records were complete and matched the cage stocking register for both years.
Status: Confirmed

Coverage: This audit assessed skin and snout condition scores only. It did not assess crowding duration or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:eb0c94622e650bfa`; belief `sha256:5cc3a25ff3d2a8b7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Item checked: Skin and snout condition scores for every stocked cage in 2024 and 2025
Method: Review of a contracted fish health assessor's reports from four visits per year, at each of which 50 fish per stocked cage were netted and scored, checked against the farm's cage stocking register
Finding: Recorded share of scored fish with skin or snout damage (score 2 or higher), mean of the four visits: 19% in 2024; 19% in 2025. Records were complete and matched the cage stocking register for both years.
Status: Confirmed

Coverage: This audit assessed skin and snout condition scores only. It did not assess crowding duration or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:e4cbf6c84445f83a`; belief `sha256:3093d91df762eb1e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halcyon Marine Standards S.A.
Audit reference: HMS-DL-2026-047
Site: Pelagon Bay Marine Farm
Date: 23 June 2026
Status: Verified ✓
~~~~
