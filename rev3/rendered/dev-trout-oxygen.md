# Rendered stimuli: `dev-trout-oxygen` (batch bb)

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

### attribution context  `sha256:b1b0a0240ad0b384`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Allt Beithe Trout Farm. Animals: rainbow trout (freshwater raceways).
The supplier states:
[P] Throughout 2025, every stocked raceway at Allt Beithe Trout Farm had a dissolved oxygen level of at least 7 mg/L at the outlet at every twice-daily reading.
[Q_obs] The recorded share of fish from Allt Beithe Trout Farm downgraded for skin lesions at harvest was lower for 2025 harvests than for 2024 harvests.
[Q_welfare] The overall welfare of the fish at Allt Beithe Trout Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded skin lesions was caused by the higher oxygen levels.
[R] Allt Beithe Trout Farm passed its 2026 water-abstraction meter inspection.
[S] Throughout 2025, every stocked raceway at Allt Beithe Upper, a sister site, also had a dissolved oxygen level of at least 7 mg/L at the outlet at every twice-daily reading.

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

### belief context  `sha256:e3cd9bde6bd95ff5`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Allt Beithe Trout Farm. Animals: rainbow trout (freshwater raceways).
The supplier states:
[P] Throughout 2025, every stocked raceway at Allt Beithe Trout Farm had a dissolved oxygen level of at least 7 mg/L at the outlet at every twice-daily reading.
[Q_obs] The recorded share of fish from Allt Beithe Trout Farm downgraded for skin lesions at harvest was lower for 2025 harvests than for 2024 harvests.
[Q_welfare] The overall welfare of the fish at Allt Beithe Trout Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded skin lesions was caused by the higher oxygen levels.
[R] Allt Beithe Trout Farm passed its 2026 water-abstraction meter inspection.
[S] Throughout 2025, every stocked raceway at Allt Beithe Upper, a sister site, also had a dissolved oxygen level of at least 7 mg/L at the outlet at every twice-daily reading.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every stocked raceway at Allt Beithe Trout Farm had a dissolved oxygen level of at least 7 mg/L at the outlet at every twice-daily reading." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of harvested fish downgraded for skin lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of harvested fish downgraded for skin lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of harvested fish downgraded for skin lesions at this facility.
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

### attribution context  `sha256:2a7ffced421515f5`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Allt Beithe Trout Farm. Animals: rainbow trout (freshwater raceways).
The supplier states:
[Q_obs] The recorded share of fish from Allt Beithe Trout Farm downgraded for skin lesions at harvest was lower for 2025 harvests than for 2024 harvests.
[Q_welfare] The overall welfare of the fish at Allt Beithe Trout Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded skin lesions was caused by the higher oxygen levels.
[R] Allt Beithe Trout Farm passed its 2026 water-abstraction meter inspection.
[S] Throughout 2025, every stocked raceway at Allt Beithe Upper, a sister site, also had a dissolved oxygen level of at least 7 mg/L at the outlet at every twice-daily reading.

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

### belief context  `sha256:92b79c7428c01248`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Allt Beithe Trout Farm. Animals: rainbow trout (freshwater raceways).
The supplier states:
[Q_obs] The recorded share of fish from Allt Beithe Trout Farm downgraded for skin lesions at harvest was lower for 2025 harvests than for 2024 harvests.
[Q_welfare] The overall welfare of the fish at Allt Beithe Trout Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded skin lesions was caused by the higher oxygen levels.
[R] Allt Beithe Trout Farm passed its 2026 water-abstraction meter inspection.
[S] Throughout 2025, every stocked raceway at Allt Beithe Upper, a sister site, also had a dissolved oxygen level of at least 7 mg/L at the outlet at every twice-daily reading.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every stocked raceway at Allt Beithe Trout Farm had a dissolved oxygen level of at least 7 mg/L at the outlet at every twice-daily reading." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of harvested fish downgraded for skin lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of harvested fish downgraded for skin lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of harvested fish downgraded for skin lesions at this facility.
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

Hashes: attribution `sha256:ebd09a225169ba5f`; belief `sha256:930c9743ad55d68b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Item checked: Dissolved oxygen at the outlet of every stocked raceway at every twice-daily reading in 2025
Method: Review of the 2025 water-quality log of twice-daily outlet readings for every stocked raceway, checked against oxygen-probe calibration records and the 2025 stocking register
Finding: The 2025 log was complete for every stocked raceway; the lowest outlet reading recorded at any twice-daily reading in 2025 was 7.4 mg/L.
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

Hashes: attribution `sha256:5081b0ec8cc2ef37`; belief `sha256:7234ad4948cf9df1`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Item checked: Dissolved oxygen at the outlet of every stocked raceway at every twice-daily reading in 2025
Method: Review of the 2025 water-quality log of twice-daily outlet readings for every stocked raceway, checked against oxygen-probe calibration records and the 2025 stocking register
Finding: The 2025 log was complete for every stocked raceway; the lowest outlet reading recorded at any twice-daily reading in 2025 was 7.4 mg/L.
Status: Confirmed

Coverage: This audit assessed dissolved oxygen in raceways only. It did not assess skin condition grading records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:3d564cfe5dfb8c47`; belief `sha256:76ce0a35beabf36e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Item checked: Dissolved oxygen at the outlet of every stocked raceway at every twice-daily reading in 2025
Method: Review of the 2025 water-quality log of twice-daily outlet readings for every stocked raceway, checked against oxygen-probe calibration records and the 2025 stocking register
Finding: The 2025 log was complete for every stocked raceway; the lowest outlet reading recorded at any twice-daily reading in 2025 was 7.4 mg/L.
Status: Confirmed

Coverage:
  Assessed: dissolved oxygen in raceways
  Not assessed: skin condition grading records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:3dc95a57bebae3f8`; belief `sha256:9926b3c99183829a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Item checked: Abstraction flow meters on the river intake and the borehole
Method: On-site calibration check of both meters and review of the meter reading returns
Finding: Both abstraction meters examined met the applicable regulatory requirements.
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

Hashes: attribution `sha256:366954729bcce9bd`; belief `sha256:87cadcf2a7919844`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Upper
Date: 14 April 2026
Item checked: Dissolved oxygen at the outlet of every stocked raceway at every twice-daily reading in 2025
Method: Review of the 2025 water-quality log of twice-daily outlet readings for every stocked raceway, checked against oxygen-probe calibration records and the 2025 stocking register
Finding: The 2025 log was complete for every stocked raceway at Allt Beithe Upper; the lowest outlet reading recorded at any twice-daily reading in 2025 was 7.2 mg/L.
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

Hashes: attribution `sha256:5c8b7a94f37e19a6`; belief `sha256:7af767bc861de152`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Item checked: Skin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's grading reports (100 fish inspected per harvest batch for ulcers, wounds and skin erosion) for every batch in both years, checked against the plant's intake records
Finding: Recorded share of inspected fish downgraded for skin lesions: 8.9% for 2024 harvests; 4.2% for 2025 harvests. Records were complete and matched the plant's intake records for both years.
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

Hashes: attribution `sha256:36c47b4f3f1c3452`; belief `sha256:0adf1d584f986985`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Item checked: Skin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's grading reports (100 fish inspected per harvest batch for ulcers, wounds and skin erosion) for every batch in both years, checked against the plant's intake records
Finding: Recorded share of inspected fish downgraded for skin lesions: 4.2% for 2024 harvests; 8.9% for 2025 harvests. Records were complete and matched the plant's intake records for both years.
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

Hashes: attribution `sha256:92f763b4e63521b3`; belief `sha256:b5ff67d2ee976846`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Item checked: Skin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's grading reports (100 fish inspected per harvest batch for ulcers, wounds and skin erosion) for every batch in both years, checked against the plant's intake records
Finding: Recorded share of inspected fish downgraded for skin lesions: 8.9% for 2024 harvests; 8.9% for 2025 harvests. Records were complete and matched the plant's intake records for both years.
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

Hashes: attribution `sha256:565a1093583c36ca`; belief `sha256:f03f8c09d76ffc6e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Item checked: Skin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's grading reports (100 fish inspected per harvest batch for ulcers, wounds and skin erosion) for every batch in both years, checked against the plant's intake records
Finding: Recorded share of inspected fish downgraded for skin lesions: 8.9% for 2024 harvests; 4.2% for 2025 harvests. Records were complete and matched the plant's intake records for both years.
Status: Confirmed

Coverage: This audit assessed skin condition grading records only. It did not assess dissolved oxygen in raceways or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:96218929742f9b4f`; belief `sha256:7ce261cefa09398d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Item checked: Skin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's grading reports (100 fish inspected per harvest batch for ulcers, wounds and skin erosion) for every batch in both years, checked against the plant's intake records
Finding: Recorded share of inspected fish downgraded for skin lesions: 4.2% for 2024 harvests; 8.9% for 2025 harvests. Records were complete and matched the plant's intake records for both years.
Status: Confirmed

Coverage: This audit assessed skin condition grading records only. It did not assess dissolved oxygen in raceways or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:1f1c45cec6abcd95`; belief `sha256:33576501638d93dd`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Item checked: Skin condition grading records for every harvest batch in 2024 and 2025
Method: Review of the processing plant's grading reports (100 fish inspected per harvest batch for ulcers, wounds and skin erosion) for every batch in both years, checked against the plant's intake records
Finding: Recorded share of inspected fish downgraded for skin lesions: 8.9% for 2024 harvests; 8.9% for 2025 harvests. Records were complete and matched the plant's intake records for both years.
Status: Confirmed

Coverage: This audit assessed skin condition grading records only. It did not assess dissolved oxygen in raceways or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:bf31dd0a392659e0`; belief `sha256:5c2cd88771e819b0`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tarnside Aquatic Assurance Ltd.
Audit reference: TAA-RT-2026-0139
Site: Allt Beithe Trout Farm
Date: 14 April 2026
Status: Verified ✓
~~~~
