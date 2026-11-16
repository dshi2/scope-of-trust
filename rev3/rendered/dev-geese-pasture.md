# Rendered stimuli: `dev-geese-pasture` (batch bb)

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

### attribution context  `sha256:2d640a77b5351d34`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ellerholt Goose Farm. Animals: geese (meat).
The supplier states:
[P] Throughout 2025, every flock of geese older than 4 weeks at Ellerholt Goose Farm had daytime access to pasture at every daily check.
[Q_obs] The recorded share of carcasses from Ellerholt Goose Farm downgraded for pecking wounds was lower for birds slaughtered in 2025 than for birds slaughtered in 2024.
[Q_welfare] The overall welfare of the geese at Ellerholt Goose Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded pecking wounds was caused by the pasture access.
[R] Ellerholt Goose Farm passed its 2026 machinery-guarding inspection.
[S] Throughout 2025, every flock of geese older than 4 weeks at Ellerholt Marsh, a sister site, also had daytime access to pasture at every daily check.

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

### belief context  `sha256:5fa4d0e6a0d96885`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ellerholt Goose Farm. Animals: geese (meat).
The supplier states:
[P] Throughout 2025, every flock of geese older than 4 weeks at Ellerholt Goose Farm had daytime access to pasture at every daily check.
[Q_obs] The recorded share of carcasses from Ellerholt Goose Farm downgraded for pecking wounds was lower for birds slaughtered in 2025 than for birds slaughtered in 2024.
[Q_welfare] The overall welfare of the geese at Ellerholt Goose Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded pecking wounds was caused by the pasture access.
[R] Ellerholt Goose Farm passed its 2026 machinery-guarding inspection.
[S] Throughout 2025, every flock of geese older than 4 weeks at Ellerholt Marsh, a sister site, also had daytime access to pasture at every daily check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock of geese older than 4 weeks at Ellerholt Goose Farm had daytime access to pasture at every daily check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of carcasses downgraded for pecking wounds between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of carcasses downgraded for pecking wounds.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of carcasses downgraded for pecking wounds at this facility.
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

### attribution context  `sha256:667a64038918146f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ellerholt Goose Farm. Animals: geese (meat).
The supplier states:
[Q_obs] The recorded share of carcasses from Ellerholt Goose Farm downgraded for pecking wounds was lower for birds slaughtered in 2025 than for birds slaughtered in 2024.
[Q_welfare] The overall welfare of the geese at Ellerholt Goose Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded pecking wounds was caused by the pasture access.
[R] Ellerholt Goose Farm passed its 2026 machinery-guarding inspection.
[S] Throughout 2025, every flock of geese older than 4 weeks at Ellerholt Marsh, a sister site, also had daytime access to pasture at every daily check.

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

### belief context  `sha256:b71981447afdd765`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ellerholt Goose Farm. Animals: geese (meat).
The supplier states:
[Q_obs] The recorded share of carcasses from Ellerholt Goose Farm downgraded for pecking wounds was lower for birds slaughtered in 2025 than for birds slaughtered in 2024.
[Q_welfare] The overall welfare of the geese at Ellerholt Goose Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded pecking wounds was caused by the pasture access.
[R] Ellerholt Goose Farm passed its 2026 machinery-guarding inspection.
[S] Throughout 2025, every flock of geese older than 4 weeks at Ellerholt Marsh, a sister site, also had daytime access to pasture at every daily check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock of geese older than 4 weeks at Ellerholt Goose Farm had daytime access to pasture at every daily check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of carcasses downgraded for pecking wounds between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of carcasses downgraded for pecking wounds.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of carcasses downgraded for pecking wounds at this facility.
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

Hashes: attribution `sha256:3b64ce7bc01dc07a`; belief `sha256:46826fcdb22771a0`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Item checked: Daytime pasture access for every flock older than 4 weeks at every daily check in 2025
Method: Review of the 2025 daily stockperson check sheets recording pop-hole opening and paddock use for every flock, checked against gosling placement records and the 2025 paddock rotation plan
Finding: Daily check sheets for 2025 were complete and recorded open pop-holes and pasture access for every flock older than 4 weeks at every check.
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

Hashes: attribution `sha256:ca26ab03f41d840e`; belief `sha256:969adbde6e2ef1a9`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Item checked: Daytime pasture access for every flock older than 4 weeks at every daily check in 2025
Method: Review of the 2025 daily stockperson check sheets recording pop-hole opening and paddock use for every flock, checked against gosling placement records and the 2025 paddock rotation plan
Finding: Daily check sheets for 2025 were complete and recorded open pop-holes and pasture access for every flock older than 4 weeks at every check.
Status: Confirmed

Coverage: This audit assessed pasture access only. It did not assess carcass grading records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:49303b9f7cf15c21`; belief `sha256:28bd3241201f043c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Item checked: Daytime pasture access for every flock older than 4 weeks at every daily check in 2025
Method: Review of the 2025 daily stockperson check sheets recording pop-hole opening and paddock use for every flock, checked against gosling placement records and the 2025 paddock rotation plan
Finding: Daily check sheets for 2025 were complete and recorded open pop-holes and pasture access for every flock older than 4 weeks at every check.
Status: Confirmed

Coverage:
  Assessed: pasture access
  Not assessed: carcass grading records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:1327a0dcdb7e16a8`; belief `sha256:2c1f2f438cf144e7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Item checked: Guards on the feed mill, mixer and grain conveyor
Method: On-site inspection of guards, interlocks and emergency stops
Finding: All machinery guards inspected met the applicable regulatory requirements.
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

Hashes: attribution `sha256:094bf96002b6d46b`; belief `sha256:a3d138c4694880dc`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Marsh
Date: 7 July 2026
Item checked: Daytime pasture access for every flock older than 4 weeks at every daily check in 2025
Method: Review of the 2025 daily stockperson check sheets recording pop-hole opening and paddock use for every flock, checked against gosling placement records and the 2025 paddock rotation plan
Finding: Daily check sheets at Ellerholt Marsh for 2025 were complete and recorded open pop-holes and pasture access for every flock older than 4 weeks at every check.
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

Hashes: attribution `sha256:ed191a8081c6ba33`; belief `sha256:1e63dd5b508749c1`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Item checked: Carcass grading records for every goose slaughtered in 2024 and 2025
Method: Review of the processing plant's carcass grading sheets for every batch in both years, on which every downgraded carcass is logged with the reason, checked against the plant's kill records
Finding: Recorded share of carcasses downgraded for pecking wounds: 7.9% for birds slaughtered in 2024; 3.5% for birds slaughtered in 2025. Records were complete and matched the plant's kill records for both years.
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

Hashes: attribution `sha256:784ba5787fc1e94b`; belief `sha256:55c174e6eeb27b27`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Item checked: Carcass grading records for every goose slaughtered in 2024 and 2025
Method: Review of the processing plant's carcass grading sheets for every batch in both years, on which every downgraded carcass is logged with the reason, checked against the plant's kill records
Finding: Recorded share of carcasses downgraded for pecking wounds: 3.5% for birds slaughtered in 2024; 7.9% for birds slaughtered in 2025. Records were complete and matched the plant's kill records for both years.
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

Hashes: attribution `sha256:e0f2ff2a52d9c273`; belief `sha256:886dc224c8c13c01`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Item checked: Carcass grading records for every goose slaughtered in 2024 and 2025
Method: Review of the processing plant's carcass grading sheets for every batch in both years, on which every downgraded carcass is logged with the reason, checked against the plant's kill records
Finding: Recorded share of carcasses downgraded for pecking wounds: 7.9% for birds slaughtered in 2024; 7.9% for birds slaughtered in 2025. Records were complete and matched the plant's kill records for both years.
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

Hashes: attribution `sha256:3e7e8235286114e0`; belief `sha256:d54306eda54e803a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Item checked: Carcass grading records for every goose slaughtered in 2024 and 2025
Method: Review of the processing plant's carcass grading sheets for every batch in both years, on which every downgraded carcass is logged with the reason, checked against the plant's kill records
Finding: Recorded share of carcasses downgraded for pecking wounds: 7.9% for birds slaughtered in 2024; 3.5% for birds slaughtered in 2025. Records were complete and matched the plant's kill records for both years.
Status: Confirmed

Coverage: This audit assessed carcass grading records only. It did not assess pasture access or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:4685158b6450208d`; belief `sha256:7876166a3ce336df`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Item checked: Carcass grading records for every goose slaughtered in 2024 and 2025
Method: Review of the processing plant's carcass grading sheets for every batch in both years, on which every downgraded carcass is logged with the reason, checked against the plant's kill records
Finding: Recorded share of carcasses downgraded for pecking wounds: 3.5% for birds slaughtered in 2024; 7.9% for birds slaughtered in 2025. Records were complete and matched the plant's kill records for both years.
Status: Confirmed

Coverage: This audit assessed carcass grading records only. It did not assess pasture access or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:04a60a7d82370699`; belief `sha256:c58d29708ffbe92d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Item checked: Carcass grading records for every goose slaughtered in 2024 and 2025
Method: Review of the processing plant's carcass grading sheets for every batch in both years, on which every downgraded carcass is logged with the reason, checked against the plant's kill records
Finding: Recorded share of carcasses downgraded for pecking wounds: 7.9% for birds slaughtered in 2024; 7.9% for birds slaughtered in 2025. Records were complete and matched the plant's kill records for both years.
Status: Confirmed

Coverage: This audit assessed carcass grading records only. It did not assess pasture access or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:ea94480d30df08b2`; belief `sha256:77c2cfa8b58d48ee`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wendmore Farm Assurance CIC
Audit reference: WFA-GS-26-0230
Site: Ellerholt Goose Farm
Date: 7 July 2026
Status: Verified ✓
~~~~
