# Rendered stimuli: `dev-donkey-load` (expansion batch bc)

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

### attribution context  `sha256:103e713925d04aee`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pellow Vale Donkey Treks. Animals: trekking donkeys.
The supplier states:
[P] Throughout 2025, no donkey at Pellow Vale Donkey Treks carried a rider or pack load heavier than 50 kg on any trek, as recorded on the trek weigh-in sheets.
[Q_obs] The recorded share of donkeys at Pellow Vale Donkey Treks with saddle or girth sores was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the donkeys at Pellow Vale Donkey Treks improved from 2024 to 2025.
[Q_cause] This reduction in recorded saddle and girth sores was caused by the load limit.
[R] Pellow Vale Donkey Treks passed its 2026 footbridge structural inspection.
[S] Throughout 2025, no donkey at Pellow Vale Upper Yard, a sister site, carried a rider or pack load heavier than 50 kg on any trek either, as recorded on the trek weigh-in sheets.

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

### belief context  `sha256:80cd55a0d97c5133`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pellow Vale Donkey Treks. Animals: trekking donkeys.
The supplier states:
[P] Throughout 2025, no donkey at Pellow Vale Donkey Treks carried a rider or pack load heavier than 50 kg on any trek, as recorded on the trek weigh-in sheets.
[Q_obs] The recorded share of donkeys at Pellow Vale Donkey Treks with saddle or girth sores was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the donkeys at Pellow Vale Donkey Treks improved from 2024 to 2025.
[Q_cause] This reduction in recorded saddle and girth sores was caused by the load limit.
[R] Pellow Vale Donkey Treks passed its 2026 footbridge structural inspection.
[S] Throughout 2025, no donkey at Pellow Vale Upper Yard, a sister site, carried a rider or pack load heavier than 50 kg on any trek either, as recorded on the trek weigh-in sheets.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, no donkey at Pellow Vale Donkey Treks carried a rider or pack load heavier than 50 kg on any trek, as recorded on the trek weigh-in sheets." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of donkeys with saddle or girth sores between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of donkeys with saddle or girth sores.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of donkeys with saddle or girth sores at this facility.
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

### attribution context  `sha256:b39feab436fa026e`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pellow Vale Donkey Treks. Animals: trekking donkeys.
The supplier states:
[Q_obs] The recorded share of donkeys at Pellow Vale Donkey Treks with saddle or girth sores was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the donkeys at Pellow Vale Donkey Treks improved from 2024 to 2025.
[Q_cause] This reduction in recorded saddle and girth sores was caused by the load limit.
[R] Pellow Vale Donkey Treks passed its 2026 footbridge structural inspection.
[S] Throughout 2025, no donkey at Pellow Vale Upper Yard, a sister site, carried a rider or pack load heavier than 50 kg on any trek either, as recorded on the trek weigh-in sheets.

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

### belief context  `sha256:d70d7db85f2d75ed`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pellow Vale Donkey Treks. Animals: trekking donkeys.
The supplier states:
[Q_obs] The recorded share of donkeys at Pellow Vale Donkey Treks with saddle or girth sores was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the donkeys at Pellow Vale Donkey Treks improved from 2024 to 2025.
[Q_cause] This reduction in recorded saddle and girth sores was caused by the load limit.
[R] Pellow Vale Donkey Treks passed its 2026 footbridge structural inspection.
[S] Throughout 2025, no donkey at Pellow Vale Upper Yard, a sister site, carried a rider or pack load heavier than 50 kg on any trek either, as recorded on the trek weigh-in sheets.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, no donkey at Pellow Vale Donkey Treks carried a rider or pack load heavier than 50 kg on any trek, as recorded on the trek weigh-in sheets." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of donkeys with saddle or girth sores between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of donkeys with saddle or girth sores.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of donkeys with saddle or girth sores at this facility.
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

Hashes: attribution `sha256:af66bb6fc72ee6ed`; belief `sha256:858fb58057c12dbe`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Item checked: Rider and pack-load weights for every donkey on every trek in 2025, as recorded on the trek weigh-in sheets
Method: Review of the 2025 trek weigh-in sheets for every trek, checked against the booking system and the scale calibration certificates
Finding: Weigh-in sheets for 2025 were complete; the heaviest rider or pack load recorded for any donkey on any trek was 48 kg.
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

Hashes: attribution `sha256:b2f5af1eed6f212e`; belief `sha256:b1bd5b6affbb1867`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Item checked: Rider and pack-load weights for every donkey on every trek in 2025, as recorded on the trek weigh-in sheets
Method: Review of the 2025 trek weigh-in sheets for every trek, checked against the booking system and the scale calibration certificates
Finding: Weigh-in sheets for 2025 were complete; the heaviest rider or pack load recorded for any donkey on any trek was 48 kg.
Status: Confirmed

Coverage: This audit assessed rider and pack-load weights only. It did not assess saddle and girth sore records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:627e1f4b88f89621`; belief `sha256:b7b46937485f374f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Item checked: Rider and pack-load weights for every donkey on every trek in 2025, as recorded on the trek weigh-in sheets
Method: Review of the 2025 trek weigh-in sheets for every trek, checked against the booking system and the scale calibration certificates
Finding: Weigh-in sheets for 2025 were complete; the heaviest rider or pack load recorded for any donkey on any trek was 48 kg.
Status: Confirmed

Coverage:
  Assessed: rider and pack-load weights
  Not assessed: saddle and girth sore records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:9767651c92c89d94`; belief `sha256:ffc002c7529f3229`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Item checked: The timber footbridge over the stream and the car-park retaining wall
Method: On-site structural examination of the footbridge deck, beams and handrails and of the retaining wall
Finding: The footbridge and retaining wall met the applicable regulatory requirements.
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

Hashes: attribution `sha256:42002636b21fdcca`; belief `sha256:c3f35fad333e22d4`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Upper Yard
Date: 22 January 2026
Item checked: Rider and pack-load weights for every donkey on every trek in 2025, as recorded on the trek weigh-in sheets
Method: Review of the 2025 trek weigh-in sheets for every trek, checked against the booking system and the scale calibration certificates
Finding: Weigh-in sheets at Pellow Vale Upper Yard for 2025 were complete; the heaviest rider or pack load recorded for any donkey on any trek was 49 kg.
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

Hashes: attribution `sha256:4f6b7f30df0b4f02`; belief `sha256:90d62e997c486ad9`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Item checked: Saddle and girth sore records for all working donkeys in 2024 and 2025
Method: Review of the quarterly yard-visit reports of the regional animal health officer, who examined the back and girth area of every working donkey at each visit, checked against the herd register
Finding: Recorded share of examined donkeys with a saddle or girth sore (open wound or hairless swelling under the saddle or girth), mean of the four quarterly visits: 16% in 2024; 7% in 2025. Records were complete and matched the herd register for both years.
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

Hashes: attribution `sha256:8d48f726cd7dbb2b`; belief `sha256:44aef3c7271f9a7f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Item checked: Saddle and girth sore records for all working donkeys in 2024 and 2025
Method: Review of the quarterly yard-visit reports of the regional animal health officer, who examined the back and girth area of every working donkey at each visit, checked against the herd register
Finding: Recorded share of examined donkeys with a saddle or girth sore (open wound or hairless swelling under the saddle or girth), mean of the four quarterly visits: 7% in 2024; 16% in 2025. Records were complete and matched the herd register for both years.
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

Hashes: attribution `sha256:9379821547679a6b`; belief `sha256:e6b84494bcb0ab0c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Item checked: Saddle and girth sore records for all working donkeys in 2024 and 2025
Method: Review of the quarterly yard-visit reports of the regional animal health officer, who examined the back and girth area of every working donkey at each visit, checked against the herd register
Finding: Recorded share of examined donkeys with a saddle or girth sore (open wound or hairless swelling under the saddle or girth), mean of the four quarterly visits: 16% in 2024; 16% in 2025. Records were complete and matched the herd register for both years.
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

Hashes: attribution `sha256:75fe536843bd4ff6`; belief `sha256:bdb8971cc8345db5`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Item checked: Saddle and girth sore records for all working donkeys in 2024 and 2025
Method: Review of the quarterly yard-visit reports of the regional animal health officer, who examined the back and girth area of every working donkey at each visit, checked against the herd register
Finding: Recorded share of examined donkeys with a saddle or girth sore (open wound or hairless swelling under the saddle or girth), mean of the four quarterly visits: 16% in 2024; 7% in 2025. Records were complete and matched the herd register for both years.
Status: Confirmed

Coverage: This audit assessed saddle and girth sore records only. It did not assess rider and pack-load weights or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:42af0a703c5be1e8`; belief `sha256:d855a9dc92ae13a0`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Item checked: Saddle and girth sore records for all working donkeys in 2024 and 2025
Method: Review of the quarterly yard-visit reports of the regional animal health officer, who examined the back and girth area of every working donkey at each visit, checked against the herd register
Finding: Recorded share of examined donkeys with a saddle or girth sore (open wound or hairless swelling under the saddle or girth), mean of the four quarterly visits: 7% in 2024; 16% in 2025. Records were complete and matched the herd register for both years.
Status: Confirmed

Coverage: This audit assessed saddle and girth sore records only. It did not assess rider and pack-load weights or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:44c104dde8f10db3`; belief `sha256:37461c3c4b72e03e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Item checked: Saddle and girth sore records for all working donkeys in 2024 and 2025
Method: Review of the quarterly yard-visit reports of the regional animal health officer, who examined the back and girth area of every working donkey at each visit, checked against the herd register
Finding: Recorded share of examined donkeys with a saddle or girth sore (open wound or hairless swelling under the saddle or girth), mean of the four quarterly visits: 16% in 2024; 16% in 2025. Records were complete and matched the herd register for both years.
Status: Confirmed

Coverage: This audit assessed saddle and girth sore records only. It did not assess rider and pack-load weights or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:6c529cfe415fe9a1`; belief `sha256:d8a12fdfe8e25b7c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Beaumont Equestrian Audit Services
Audit reference: BEAS/26/0093
Site: Pellow Vale Donkey Treks
Date: 22 January 2026
Status: Verified ✓
~~~~
