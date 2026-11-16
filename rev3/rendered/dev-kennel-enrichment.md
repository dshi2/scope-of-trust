# Rendered stimuli: `dev-kennel-enrichment` (expansion batch bc)

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

### attribution context  `sha256:8e5445abbd72144f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ottery Brook Kennels. Animals: dogs (strays held under a council kennelling contract).
The supplier states:
[P] Throughout 2025, every dog held at Ottery Brook Kennels had a raised bed and a food-dispensing toy in its kennel at every morning care check.
[Q_obs] The recorded share of dogs at Ottery Brook Kennels showing repetitive behaviour at their day-7 assessment was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the dogs at Ottery Brook Kennels improved from 2024 to 2025.
[Q_cause] This reduction in recorded repetitive behaviour was caused by the raised beds and food-dispensing toys.
[R] Ottery Brook Kennels passed its 2026 gas-appliance safety inspection.
[S] Throughout 2025, every dog held at Ottery Brook Lodge, a sister site, also had a raised bed and a food-dispensing toy in its kennel at every morning care check.

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

### belief context  `sha256:73c89907c85025c0`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ottery Brook Kennels. Animals: dogs (strays held under a council kennelling contract).
The supplier states:
[P] Throughout 2025, every dog held at Ottery Brook Kennels had a raised bed and a food-dispensing toy in its kennel at every morning care check.
[Q_obs] The recorded share of dogs at Ottery Brook Kennels showing repetitive behaviour at their day-7 assessment was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the dogs at Ottery Brook Kennels improved from 2024 to 2025.
[Q_cause] This reduction in recorded repetitive behaviour was caused by the raised beds and food-dispensing toys.
[R] Ottery Brook Kennels passed its 2026 gas-appliance safety inspection.
[S] Throughout 2025, every dog held at Ottery Brook Lodge, a sister site, also had a raised bed and a food-dispensing toy in its kennel at every morning care check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every dog held at Ottery Brook Kennels had a raised bed and a food-dispensing toy in its kennel at every morning care check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of dogs showing repetitive behaviour at their day-7 assessment between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of dogs showing repetitive behaviour at their day-7 assessment.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of dogs showing repetitive behaviour at their day-7 assessment at this facility.
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

### attribution context  `sha256:f2b8b93bc20ec784`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ottery Brook Kennels. Animals: dogs (strays held under a council kennelling contract).
The supplier states:
[Q_obs] The recorded share of dogs at Ottery Brook Kennels showing repetitive behaviour at their day-7 assessment was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the dogs at Ottery Brook Kennels improved from 2024 to 2025.
[Q_cause] This reduction in recorded repetitive behaviour was caused by the raised beds and food-dispensing toys.
[R] Ottery Brook Kennels passed its 2026 gas-appliance safety inspection.
[S] Throughout 2025, every dog held at Ottery Brook Lodge, a sister site, also had a raised bed and a food-dispensing toy in its kennel at every morning care check.

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

### belief context  `sha256:bf13a1098848cbfb`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ottery Brook Kennels. Animals: dogs (strays held under a council kennelling contract).
The supplier states:
[Q_obs] The recorded share of dogs at Ottery Brook Kennels showing repetitive behaviour at their day-7 assessment was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the dogs at Ottery Brook Kennels improved from 2024 to 2025.
[Q_cause] This reduction in recorded repetitive behaviour was caused by the raised beds and food-dispensing toys.
[R] Ottery Brook Kennels passed its 2026 gas-appliance safety inspection.
[S] Throughout 2025, every dog held at Ottery Brook Lodge, a sister site, also had a raised bed and a food-dispensing toy in its kennel at every morning care check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every dog held at Ottery Brook Kennels had a raised bed and a food-dispensing toy in its kennel at every morning care check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of dogs showing repetitive behaviour at their day-7 assessment between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of dogs showing repetitive behaviour at their day-7 assessment.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of dogs showing repetitive behaviour at their day-7 assessment at this facility.
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

Hashes: attribution `sha256:77465ebb39a529e0`; belief `sha256:b0625e3cbea0ec26`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Item checked: Raised beds and food-dispensing toys in every occupied kennel at every morning care check in 2025
Method: Review of the 2025 morning care-check sheets for every kennel block, checked against the kennel occupancy register and equipment purchase records
Finding: Morning care-check sheets for 2025 were complete and recorded a raised bed and a food-dispensing toy in every occupied kennel at every check.
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

Hashes: attribution `sha256:ad149ef0aa6dfa29`; belief `sha256:7292f0a323ff773f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Item checked: Raised beds and food-dispensing toys in every occupied kennel at every morning care check in 2025
Method: Review of the 2025 morning care-check sheets for every kennel block, checked against the kennel occupancy register and equipment purchase records
Finding: Morning care-check sheets for 2025 were complete and recorded a raised bed and a food-dispensing toy in every occupied kennel at every check.
Status: Confirmed

Coverage: This audit assessed kennel beds and food-dispensing toys only. It did not assess behaviour assessment records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:a6165549533e82d7`; belief `sha256:e28748889d9f7385`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Item checked: Raised beds and food-dispensing toys in every occupied kennel at every morning care check in 2025
Method: Review of the 2025 morning care-check sheets for every kennel block, checked against the kennel occupancy register and equipment purchase records
Finding: Morning care-check sheets for 2025 were complete and recorded a raised bed and a food-dispensing toy in every occupied kennel at every check.
Status: Confirmed

Coverage:
  Assessed: kennel beds and food-dispensing toys
  Not assessed: behaviour assessment records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:b22ecd8da983b5dc`; belief `sha256:69da3afe18d8f3a7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Item checked: Gas boilers and cookers in the staff building and laundry
Method: On-site examination of each appliance, flue and gas supply, with combustion analysis
Finding: All gas appliances examined met the applicable regulatory requirements.
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

Hashes: attribution `sha256:1f34ff3859e46aad`; belief `sha256:32ffdc8dea73667b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Lodge
Date: 6 May 2026
Item checked: Raised beds and food-dispensing toys in every occupied kennel at every morning care check in 2025
Method: Review of the 2025 morning care-check sheets for every kennel block, checked against the kennel occupancy register and equipment purchase records
Finding: Morning care-check sheets at Ottery Brook Lodge for 2025 were complete and recorded a raised bed and a food-dispensing toy in every occupied kennel at every check.
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

Hashes: attribution `sha256:0a889c5d760a698f`; belief `sha256:5c6e0ec0074ca570`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Item checked: Day-7 behaviour assessments for all dogs held 7 days or longer in 2024 and 2025
Method: Review of the day-7 behaviour scoring sheets completed by a contracted canine behaviourist for every dog held 7 days or longer, checked against the kennel intake and release register
Finding: Recorded share of assessed dogs showing repetitive behaviour (circling, pacing or wall-bouncing) during the 10-minute observation: 26% in 2024; 14% in 2025. Records were complete and matched the intake and release register for both years.
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

Hashes: attribution `sha256:0ad29af3e6cefee7`; belief `sha256:91902a489ff496ba`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Item checked: Day-7 behaviour assessments for all dogs held 7 days or longer in 2024 and 2025
Method: Review of the day-7 behaviour scoring sheets completed by a contracted canine behaviourist for every dog held 7 days or longer, checked against the kennel intake and release register
Finding: Recorded share of assessed dogs showing repetitive behaviour (circling, pacing or wall-bouncing) during the 10-minute observation: 14% in 2024; 26% in 2025. Records were complete and matched the intake and release register for both years.
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

Hashes: attribution `sha256:2ba7bd58e0f06f6a`; belief `sha256:613550ff13ed3d39`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Item checked: Day-7 behaviour assessments for all dogs held 7 days or longer in 2024 and 2025
Method: Review of the day-7 behaviour scoring sheets completed by a contracted canine behaviourist for every dog held 7 days or longer, checked against the kennel intake and release register
Finding: Recorded share of assessed dogs showing repetitive behaviour (circling, pacing or wall-bouncing) during the 10-minute observation: 26% in 2024; 26% in 2025. Records were complete and matched the intake and release register for both years.
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

Hashes: attribution `sha256:71ef77dfd0eedbe6`; belief `sha256:7c91067bc195c35a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Item checked: Day-7 behaviour assessments for all dogs held 7 days or longer in 2024 and 2025
Method: Review of the day-7 behaviour scoring sheets completed by a contracted canine behaviourist for every dog held 7 days or longer, checked against the kennel intake and release register
Finding: Recorded share of assessed dogs showing repetitive behaviour (circling, pacing or wall-bouncing) during the 10-minute observation: 26% in 2024; 14% in 2025. Records were complete and matched the intake and release register for both years.
Status: Confirmed

Coverage: This audit assessed behaviour assessment records only. It did not assess kennel beds and food-dispensing toys or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:52f0b4fa687079f9`; belief `sha256:d02bb0f207073c2a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Item checked: Day-7 behaviour assessments for all dogs held 7 days or longer in 2024 and 2025
Method: Review of the day-7 behaviour scoring sheets completed by a contracted canine behaviourist for every dog held 7 days or longer, checked against the kennel intake and release register
Finding: Recorded share of assessed dogs showing repetitive behaviour (circling, pacing or wall-bouncing) during the 10-minute observation: 14% in 2024; 26% in 2025. Records were complete and matched the intake and release register for both years.
Status: Confirmed

Coverage: This audit assessed behaviour assessment records only. It did not assess kennel beds and food-dispensing toys or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:9b35cf253fc1d8a1`; belief `sha256:affc99a4dbb9862e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Item checked: Day-7 behaviour assessments for all dogs held 7 days or longer in 2024 and 2025
Method: Review of the day-7 behaviour scoring sheets completed by a contracted canine behaviourist for every dog held 7 days or longer, checked against the kennel intake and release register
Finding: Recorded share of assessed dogs showing repetitive behaviour (circling, pacing or wall-bouncing) during the 10-minute observation: 26% in 2024; 26% in 2025. Records were complete and matched the intake and release register for both years.
Status: Confirmed

Coverage: This audit assessed behaviour assessment records only. It did not assess kennel beds and food-dispensing toys or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:9aaf46fa0b86258e`; belief `sha256:7e865a8cbdfae216`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Penrose Companion Animal Audit Ltd.
Audit reference: PCAA-K-2026-077
Site: Ottery Brook Kennels
Date: 6 May 2026
Status: Verified ✓
~~~~
