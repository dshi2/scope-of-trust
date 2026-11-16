# Rendered stimuli: `dev-buffalo-bedding` (expansion batch ba)

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

### attribution context  `sha256:845b247b45ba98ac`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ferrabyn Buffalo Dairy. Animals: dairy water buffalo.
The supplier states:
[P] Throughout 2025, every cubicle in use for lactating buffalo at Ferrabyn Buffalo Dairy had sand bedding at least 10 cm deep at every weekly bedding check.
[Q_obs] The recorded share of lactating buffalo at Ferrabyn Buffalo Dairy with hock lesions was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the buffalo at Ferrabyn Buffalo Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded hock lesions was caused by the deeper sand bedding.
[R] Ferrabyn Buffalo Dairy passed its 2026 milk-room drainage inspection.
[S] Throughout 2025, every cubicle in use for lactating buffalo at Ferrabyn Marsh Unit, a sister site, also had sand bedding at least 10 cm deep at every weekly bedding check.

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

### belief context  `sha256:bfc6b13f50dc4856`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ferrabyn Buffalo Dairy. Animals: dairy water buffalo.
The supplier states:
[P] Throughout 2025, every cubicle in use for lactating buffalo at Ferrabyn Buffalo Dairy had sand bedding at least 10 cm deep at every weekly bedding check.
[Q_obs] The recorded share of lactating buffalo at Ferrabyn Buffalo Dairy with hock lesions was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the buffalo at Ferrabyn Buffalo Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded hock lesions was caused by the deeper sand bedding.
[R] Ferrabyn Buffalo Dairy passed its 2026 milk-room drainage inspection.
[S] Throughout 2025, every cubicle in use for lactating buffalo at Ferrabyn Marsh Unit, a sister site, also had sand bedding at least 10 cm deep at every weekly bedding check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every cubicle in use for lactating buffalo at Ferrabyn Buffalo Dairy had sand bedding at least 10 cm deep at every weekly bedding check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of lactating buffalo with hock lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of lactating buffalo with hock lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of lactating buffalo with hock lesions at this facility.
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

### attribution context  `sha256:44fdfa1ee4900015`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ferrabyn Buffalo Dairy. Animals: dairy water buffalo.
The supplier states:
[Q_obs] The recorded share of lactating buffalo at Ferrabyn Buffalo Dairy with hock lesions was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the buffalo at Ferrabyn Buffalo Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded hock lesions was caused by the deeper sand bedding.
[R] Ferrabyn Buffalo Dairy passed its 2026 milk-room drainage inspection.
[S] Throughout 2025, every cubicle in use for lactating buffalo at Ferrabyn Marsh Unit, a sister site, also had sand bedding at least 10 cm deep at every weekly bedding check.

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

### belief context  `sha256:5fa5bf8c78eaf1f4`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ferrabyn Buffalo Dairy. Animals: dairy water buffalo.
The supplier states:
[Q_obs] The recorded share of lactating buffalo at Ferrabyn Buffalo Dairy with hock lesions was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the buffalo at Ferrabyn Buffalo Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded hock lesions was caused by the deeper sand bedding.
[R] Ferrabyn Buffalo Dairy passed its 2026 milk-room drainage inspection.
[S] Throughout 2025, every cubicle in use for lactating buffalo at Ferrabyn Marsh Unit, a sister site, also had sand bedding at least 10 cm deep at every weekly bedding check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every cubicle in use for lactating buffalo at Ferrabyn Buffalo Dairy had sand bedding at least 10 cm deep at every weekly bedding check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of lactating buffalo with hock lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of lactating buffalo with hock lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of lactating buffalo with hock lesions at this facility.
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

Hashes: attribution `sha256:19f4ba17efe6870e`; belief `sha256:787592dce2a2352a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Item checked: Sand bedding depth in every cubicle in use for lactating buffalo at every weekly bedding check during 2025
Method: Review of the 52 weekly bedding-check sheets for 2025, on which the depth at the rear of each cubicle is measured with a marked probe, compared with the shed plans and 2025 sand delivery records
Finding: Every weekly bedding-check sheet for 2025 recorded sand at least 10 cm deep in every cubicle in use for lactating buffalo; the shallowest recorded depth was 11 cm, and sand deliveries matched recorded top-ups.
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

Hashes: attribution `sha256:f4c333d76cac0541`; belief `sha256:fd6c4c1d13125903`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Item checked: Sand bedding depth in every cubicle in use for lactating buffalo at every weekly bedding check during 2025
Method: Review of the 52 weekly bedding-check sheets for 2025, on which the depth at the rear of each cubicle is measured with a marked probe, compared with the shed plans and 2025 sand delivery records
Finding: Every weekly bedding-check sheet for 2025 recorded sand at least 10 cm deep in every cubicle in use for lactating buffalo; the shallowest recorded depth was 11 cm, and sand deliveries matched recorded top-ups.
Status: Confirmed

Coverage: This audit assessed cubicle bedding depth only. It did not assess hock lesion records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:e811086112f5019e`; belief `sha256:19a2fc13bb7f1e1d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Item checked: Sand bedding depth in every cubicle in use for lactating buffalo at every weekly bedding check during 2025
Method: Review of the 52 weekly bedding-check sheets for 2025, on which the depth at the rear of each cubicle is measured with a marked probe, compared with the shed plans and 2025 sand delivery records
Finding: Every weekly bedding-check sheet for 2025 recorded sand at least 10 cm deep in every cubicle in use for lactating buffalo; the shallowest recorded depth was 11 cm, and sand deliveries matched recorded top-ups.
Status: Confirmed

Coverage:
  Assessed: cubicle bedding depth
  Not assessed: hock lesion records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:262c0db8a4d32c05`; belief `sha256:bf8bacb01493cd15`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Item checked: Milk-room and parlour wash-water drains, interceptor and soakaway
Method: On-site inspection of drains, the interceptor and the soakaway, with a dye test of the outfall
Finding: All drainage installations inspected met the applicable regulatory requirements.
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

Hashes: attribution `sha256:37fc205a9d1d629d`; belief `sha256:849fb60939159f4a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Marsh Unit
Date: 28 April 2026
Item checked: Sand bedding depth in every cubicle in use for lactating buffalo at every weekly bedding check during 2025
Method: Review of the 52 weekly bedding-check sheets for 2025, on which the depth at the rear of each cubicle is measured with a marked probe, compared with the shed plans and 2025 sand delivery records
Finding: Every weekly bedding-check sheet at Ferrabyn Marsh Unit for 2025 recorded sand at least 10 cm deep in every cubicle in use for lactating buffalo; the shallowest recorded depth was 10 cm, and sand deliveries matched recorded top-ups.
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

Hashes: attribution `sha256:d0d0ce27c0484e3a`; belief `sha256:c6038af0a81a8b53`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Item checked: Hock lesion records for every lactating buffalo in 2024 and 2025
Method: Review of the hock scores recorded by the milk-recording organisation's technician at the four quarterly recording visits per year, covering every buffalo in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored buffalo with a hock lesion (swelling or broken skin on either hock), mean of the four quarterly visits: 18% in 2024; 9% in 2025. Records were complete and matched the herd lists for both years.
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

Hashes: attribution `sha256:a7805fa8ce3b65e4`; belief `sha256:a697ebbb4e401c32`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Item checked: Hock lesion records for every lactating buffalo in 2024 and 2025
Method: Review of the hock scores recorded by the milk-recording organisation's technician at the four quarterly recording visits per year, covering every buffalo in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored buffalo with a hock lesion (swelling or broken skin on either hock), mean of the four quarterly visits: 9% in 2024; 18% in 2025. Records were complete and matched the herd lists for both years.
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

Hashes: attribution `sha256:e55aded262e51652`; belief `sha256:0f1fac2daaef4a82`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Item checked: Hock lesion records for every lactating buffalo in 2024 and 2025
Method: Review of the hock scores recorded by the milk-recording organisation's technician at the four quarterly recording visits per year, covering every buffalo in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored buffalo with a hock lesion (swelling or broken skin on either hock), mean of the four quarterly visits: 18% in 2024; 18% in 2025. Records were complete and matched the herd lists for both years.
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

Hashes: attribution `sha256:70f29c6496d92e32`; belief `sha256:91bdaf5dd368cc00`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Item checked: Hock lesion records for every lactating buffalo in 2024 and 2025
Method: Review of the hock scores recorded by the milk-recording organisation's technician at the four quarterly recording visits per year, covering every buffalo in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored buffalo with a hock lesion (swelling or broken skin on either hock), mean of the four quarterly visits: 18% in 2024; 9% in 2025. Records were complete and matched the herd lists for both years.
Status: Confirmed

Coverage: This audit assessed hock lesion records only. It did not assess cubicle bedding depth or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:b37239c11acc2074`; belief `sha256:a19a3bdf404847e8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Item checked: Hock lesion records for every lactating buffalo in 2024 and 2025
Method: Review of the hock scores recorded by the milk-recording organisation's technician at the four quarterly recording visits per year, covering every buffalo in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored buffalo with a hock lesion (swelling or broken skin on either hock), mean of the four quarterly visits: 9% in 2024; 18% in 2025. Records were complete and matched the herd lists for both years.
Status: Confirmed

Coverage: This audit assessed hock lesion records only. It did not assess cubicle bedding depth or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:ff022e0126bf8422`; belief `sha256:9664338d1b0060d6`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Item checked: Hock lesion records for every lactating buffalo in 2024 and 2025
Method: Review of the hock scores recorded by the milk-recording organisation's technician at the four quarterly recording visits per year, covering every buffalo in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored buffalo with a hock lesion (swelling or broken skin on either hock), mean of the four quarterly visits: 18% in 2024; 18% in 2025. Records were complete and matched the herd lists for both years.
Status: Confirmed

Coverage: This audit assessed hock lesion records only. It did not assess cubicle bedding depth or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:307b7da64fccc050`; belief `sha256:a317a48c9cadc3fe`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Lindqvist Dairy Certification AB
Audit reference: LDC-WB-2026-0193
Site: Ferrabyn Buffalo Dairy
Date: 28 April 2026
Status: Verified ✓
~~~~
