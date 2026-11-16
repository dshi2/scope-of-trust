# Rendered stimuli: `dev-livery-forage` (expansion batch ba)

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

### attribution context  `sha256:80a7d7883d7744d5`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ormsgill Livery. Animals: horses (livery yard).
The supplier states:
[P] Throughout 2025, the daily feed sheets at Ormsgill Livery recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day.
[Q_obs] The recorded share of resident horses at Ormsgill Livery with at least one vet-attended colic episode was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the horses at Ormsgill Livery improved from 2024 to 2025.
[Q_cause] This reduction in recorded colic was caused by the larger forage rations.
[R] Ormsgill Livery passed its 2026 manure-store inspection.
[S] Throughout 2025, the daily feed sheets at Ormsgill Lower Yard, a sister site, also recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day.

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

### belief context  `sha256:cfebf9f8bb1dec82`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ormsgill Livery. Animals: horses (livery yard).
The supplier states:
[P] Throughout 2025, the daily feed sheets at Ormsgill Livery recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day.
[Q_obs] The recorded share of resident horses at Ormsgill Livery with at least one vet-attended colic episode was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the horses at Ormsgill Livery improved from 2024 to 2025.
[Q_cause] This reduction in recorded colic was caused by the larger forage rations.
[R] Ormsgill Livery passed its 2026 manure-store inspection.
[S] Throughout 2025, the daily feed sheets at Ormsgill Lower Yard, a sister site, also recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, the daily feed sheets at Ormsgill Livery recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of resident horses with at least one vet-attended colic episode between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of resident horses with at least one vet-attended colic episode.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of resident horses with at least one vet-attended colic episode at this facility.
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

### attribution context  `sha256:c98acfb675a9772f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ormsgill Livery. Animals: horses (livery yard).
The supplier states:
[Q_obs] The recorded share of resident horses at Ormsgill Livery with at least one vet-attended colic episode was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the horses at Ormsgill Livery improved from 2024 to 2025.
[Q_cause] This reduction in recorded colic was caused by the larger forage rations.
[R] Ormsgill Livery passed its 2026 manure-store inspection.
[S] Throughout 2025, the daily feed sheets at Ormsgill Lower Yard, a sister site, also recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day.

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

### belief context  `sha256:bd9c768f8ff3becc`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ormsgill Livery. Animals: horses (livery yard).
The supplier states:
[Q_obs] The recorded share of resident horses at Ormsgill Livery with at least one vet-attended colic episode was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the horses at Ormsgill Livery improved from 2024 to 2025.
[Q_cause] This reduction in recorded colic was caused by the larger forage rations.
[R] Ormsgill Livery passed its 2026 manure-store inspection.
[S] Throughout 2025, the daily feed sheets at Ormsgill Lower Yard, a sister site, also recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, the daily feed sheets at Ormsgill Livery recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of resident horses with at least one vet-attended colic episode between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of resident horses with at least one vet-attended colic episode.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of resident horses with at least one vet-attended colic episode at this facility.
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

Hashes: attribution `sha256:6eb479c941682a07`; belief `sha256:4e9535da811b3b4b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Item checked: Daily forage ration of every horse resident at any time during 2025, as recorded on the daily feed sheets
Method: Review of the 365 daily feed sheets for 2025, compared with the 2025 livery register of arrivals and departures, the 2025 weigh-tape body-weight log and 2025 forage delivery records
Finding: The daily feed sheets for 2025 were complete and recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day; the lowest recorded ration was 1.6 kg per 100 kg, and forage deliveries matched recorded use.
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

Hashes: attribution `sha256:e3a79651ce17e900`; belief `sha256:41f5a6983f135d98`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Item checked: Daily forage ration of every horse resident at any time during 2025, as recorded on the daily feed sheets
Method: Review of the 365 daily feed sheets for 2025, compared with the 2025 livery register of arrivals and departures, the 2025 weigh-tape body-weight log and 2025 forage delivery records
Finding: The daily feed sheets for 2025 were complete and recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day; the lowest recorded ration was 1.6 kg per 100 kg, and forage deliveries matched recorded use.
Status: Confirmed

Coverage: This audit assessed daily forage rations only. It did not assess colic records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:bdb534a47d2e50f7`; belief `sha256:aeb24f0a5ba3229c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Item checked: Daily forage ration of every horse resident at any time during 2025, as recorded on the daily feed sheets
Method: Review of the 365 daily feed sheets for 2025, compared with the 2025 livery register of arrivals and departures, the 2025 weigh-tape body-weight log and 2025 forage delivery records
Finding: The daily feed sheets for 2025 were complete and recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day; the lowest recorded ration was 1.6 kg per 100 kg, and forage deliveries matched recorded use.
Status: Confirmed

Coverage:
  Assessed: daily forage rations
  Not assessed: colic records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:54e3d5bfeb27206e`; belief `sha256:bc00254ac9a1e631`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Item checked: The muck heap, its concrete base and the dirty-water drain
Method: On-site inspection of the base, retaining walls and drain, and of the distance to the nearest watercourse
Finding: The manure store met the applicable regulatory requirements.
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

Hashes: attribution `sha256:7f1b4667e84fd65d`; belief `sha256:c71f1b90803cbfaa`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Lower Yard
Date: 9 June 2026
Item checked: Daily forage ration of every horse resident at any time during 2025, as recorded on the daily feed sheets
Method: Review of the 365 daily feed sheets for 2025, compared with the 2025 livery register of arrivals and departures, the 2025 weigh-tape body-weight log and 2025 forage delivery records
Finding: The daily feed sheets at Ormsgill Lower Yard for 2025 were complete and recorded at least 1.5 kg of hay or haylage per 100 kg of body weight for every resident horse on every day; the lowest recorded ration was 1.5 kg per 100 kg, and forage deliveries matched recorded use.
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

Hashes: attribution `sha256:306dd2ed8885c5c1`; belief `sha256:6ecec78514541692`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Item checked: Colic records for every horse resident at any time in 2024 and 2025
Method: Review of the yard's veterinary call-out log and the attending practices' visit records for every resident horse in both years, checked against the livery register
Finding: Recorded share of resident horses with at least one vet-attended colic episode: 11% in 2024; 5% in 2025. Records were complete and matched the practices' visit records for both years.
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

Hashes: attribution `sha256:dbfbadcdab997873`; belief `sha256:28ad05e539fb5eb3`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Item checked: Colic records for every horse resident at any time in 2024 and 2025
Method: Review of the yard's veterinary call-out log and the attending practices' visit records for every resident horse in both years, checked against the livery register
Finding: Recorded share of resident horses with at least one vet-attended colic episode: 5% in 2024; 11% in 2025. Records were complete and matched the practices' visit records for both years.
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

Hashes: attribution `sha256:1b76aba0d26b3a30`; belief `sha256:09d09e8f1f5d27c1`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Item checked: Colic records for every horse resident at any time in 2024 and 2025
Method: Review of the yard's veterinary call-out log and the attending practices' visit records for every resident horse in both years, checked against the livery register
Finding: Recorded share of resident horses with at least one vet-attended colic episode: 11% in 2024; 11% in 2025. Records were complete and matched the practices' visit records for both years.
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

Hashes: attribution `sha256:688f48ae400005e9`; belief `sha256:02cd1fdca6f8d068`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Item checked: Colic records for every horse resident at any time in 2024 and 2025
Method: Review of the yard's veterinary call-out log and the attending practices' visit records for every resident horse in both years, checked against the livery register
Finding: Recorded share of resident horses with at least one vet-attended colic episode: 11% in 2024; 5% in 2025. Records were complete and matched the practices' visit records for both years.
Status: Confirmed

Coverage: This audit assessed colic records only. It did not assess daily forage rations or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:708ee32a0f2de3d9`; belief `sha256:d199333632c48151`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Item checked: Colic records for every horse resident at any time in 2024 and 2025
Method: Review of the yard's veterinary call-out log and the attending practices' visit records for every resident horse in both years, checked against the livery register
Finding: Recorded share of resident horses with at least one vet-attended colic episode: 5% in 2024; 11% in 2025. Records were complete and matched the practices' visit records for both years.
Status: Confirmed

Coverage: This audit assessed colic records only. It did not assess daily forage rations or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:469a2c8156f7716b`; belief `sha256:dc5d0b75576a4195`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Item checked: Colic records for every horse resident at any time in 2024 and 2025
Method: Review of the yard's veterinary call-out log and the attending practices' visit records for every resident horse in both years, checked against the livery register
Finding: Recorded share of resident horses with at least one vet-attended colic episode: 11% in 2024; 11% in 2025. Records were complete and matched the practices' visit records for both years.
Status: Confirmed

Coverage: This audit assessed colic records only. It did not assess daily forage rations or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:5543e32bd46ce935`; belief `sha256:4a422b6baf99ddcf`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Ridgeway Equine Standards Ltd.
Audit reference: RES-L-2026-0412
Site: Ormsgill Livery
Date: 9 June 2026
Status: Verified ✓
~~~~
