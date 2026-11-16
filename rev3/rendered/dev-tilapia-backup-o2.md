# Rendered stimuli: `dev-tilapia-backup-o2` (batch bb)

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

### attribution context  `sha256:d4e827be0a515df6`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Quarrendon Aquaculture. Animals: Nile tilapia (recirculating tanks).
The supplier states:
[P] Throughout 2025, every stocked grow-out tank at Quarrendon Aquaculture was connected to a working emergency oxygen supply at every weekly alarm test.
[Q_obs] The recorded share of stocked fish at Quarrendon Aquaculture that died before harvest was lower for batches harvested in 2025 than for batches harvested in 2024.
[Q_welfare] The overall welfare of the fish at Quarrendon Aquaculture improved from 2024 to 2025.
[Q_cause] This reduction in recorded mortality was caused by the emergency oxygen supply.
[R] Quarrendon Aquaculture passed its 2026 effluent discharge inspection.
[S] Throughout 2025, every stocked grow-out tank at Quarrendon Mill, a sister site, was also connected to a working emergency oxygen supply at every weekly alarm test.

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

### belief context  `sha256:bfa367e56a50d57d`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Quarrendon Aquaculture. Animals: Nile tilapia (recirculating tanks).
The supplier states:
[P] Throughout 2025, every stocked grow-out tank at Quarrendon Aquaculture was connected to a working emergency oxygen supply at every weekly alarm test.
[Q_obs] The recorded share of stocked fish at Quarrendon Aquaculture that died before harvest was lower for batches harvested in 2025 than for batches harvested in 2024.
[Q_welfare] The overall welfare of the fish at Quarrendon Aquaculture improved from 2024 to 2025.
[Q_cause] This reduction in recorded mortality was caused by the emergency oxygen supply.
[R] Quarrendon Aquaculture passed its 2026 effluent discharge inspection.
[S] Throughout 2025, every stocked grow-out tank at Quarrendon Mill, a sister site, was also connected to a working emergency oxygen supply at every weekly alarm test.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every stocked grow-out tank at Quarrendon Aquaculture was connected to a working emergency oxygen supply at every weekly alarm test." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of stocked fish that died before harvest between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of stocked fish that died before harvest.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of stocked fish that died before harvest at this facility.
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

### attribution context  `sha256:b92b8992ebead9e3`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Quarrendon Aquaculture. Animals: Nile tilapia (recirculating tanks).
The supplier states:
[Q_obs] The recorded share of stocked fish at Quarrendon Aquaculture that died before harvest was lower for batches harvested in 2025 than for batches harvested in 2024.
[Q_welfare] The overall welfare of the fish at Quarrendon Aquaculture improved from 2024 to 2025.
[Q_cause] This reduction in recorded mortality was caused by the emergency oxygen supply.
[R] Quarrendon Aquaculture passed its 2026 effluent discharge inspection.
[S] Throughout 2025, every stocked grow-out tank at Quarrendon Mill, a sister site, was also connected to a working emergency oxygen supply at every weekly alarm test.

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

### belief context  `sha256:437310186719ae72`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Quarrendon Aquaculture. Animals: Nile tilapia (recirculating tanks).
The supplier states:
[Q_obs] The recorded share of stocked fish at Quarrendon Aquaculture that died before harvest was lower for batches harvested in 2025 than for batches harvested in 2024.
[Q_welfare] The overall welfare of the fish at Quarrendon Aquaculture improved from 2024 to 2025.
[Q_cause] This reduction in recorded mortality was caused by the emergency oxygen supply.
[R] Quarrendon Aquaculture passed its 2026 effluent discharge inspection.
[S] Throughout 2025, every stocked grow-out tank at Quarrendon Mill, a sister site, was also connected to a working emergency oxygen supply at every weekly alarm test.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every stocked grow-out tank at Quarrendon Aquaculture was connected to a working emergency oxygen supply at every weekly alarm test." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of stocked fish that died before harvest between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of stocked fish that died before harvest.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of stocked fish that died before harvest at this facility.
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

Hashes: attribution `sha256:fb6c78de0b296939`; belief `sha256:ab46300e90e0c72e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Item checked: Emergency oxygen supply to every stocked grow-out tank at every weekly alarm test in 2025
Method: Review of the 2025 weekly alarm-test sheets for every stocked grow-out tank, oxygen cylinder delivery records and the 2025 tank stocking register
Finding: Weekly alarm-test sheets for 2025 were complete and recorded a working emergency oxygen supply to every stocked grow-out tank at every test.
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

Hashes: attribution `sha256:c097a27c8cdc96b9`; belief `sha256:d6a3ee1f59f32c59`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Item checked: Emergency oxygen supply to every stocked grow-out tank at every weekly alarm test in 2025
Method: Review of the 2025 weekly alarm-test sheets for every stocked grow-out tank, oxygen cylinder delivery records and the 2025 tank stocking register
Finding: Weekly alarm-test sheets for 2025 were complete and recorded a working emergency oxygen supply to every stocked grow-out tank at every test.
Status: Confirmed

Coverage: This audit assessed emergency oxygen supply only. It did not assess tank mortality records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:1673e0ace5a915ce`; belief `sha256:aaac9fef3b5cc984`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Item checked: Emergency oxygen supply to every stocked grow-out tank at every weekly alarm test in 2025
Method: Review of the 2025 weekly alarm-test sheets for every stocked grow-out tank, oxygen cylinder delivery records and the 2025 tank stocking register
Finding: Weekly alarm-test sheets for 2025 were complete and recorded a working emergency oxygen supply to every stocked grow-out tank at every test.
Status: Confirmed

Coverage:
  Assessed: emergency oxygen supply
  Not assessed: tank mortality records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:24974ea85376ca9e`; belief `sha256:d5df5ca2c4871a66`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Item checked: The effluent settlement tanks and the discharge outfall
Method: On-site inspection of the settlement tanks and outfall, and review of the discharge sampling log
Finding: The settlement tanks and outfall met the applicable regulatory requirements.
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

Hashes: attribution `sha256:b2fd6c712fb3b09c`; belief `sha256:0bf4659aed22ef5b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Mill
Date: 11 March 2026
Item checked: Emergency oxygen supply to every stocked grow-out tank at every weekly alarm test in 2025
Method: Review of the 2025 weekly alarm-test sheets for every stocked grow-out tank, oxygen cylinder delivery records and the 2025 tank stocking register
Finding: Weekly alarm-test sheets at Quarrendon Mill for 2025 were complete and recorded a working emergency oxygen supply to every stocked grow-out tank at every test.
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

Hashes: attribution `sha256:b9203152dc398b5f`; belief `sha256:0c348262e7e729d8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Item checked: Mortality records for every batch harvested in 2024 and 2025
Method: Review of daily tank mortality logs for every batch from stocking to harvest, checked against fingerling delivery counts and the processor's harvest counts
Finding: Recorded share of stocked fingerlings that died before harvest: 11.8% for batches harvested in 2024; 6.5% for batches harvested in 2025. Records were complete and matched delivery and harvest counts for both years.
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

Hashes: attribution `sha256:026b9cccf7320ccf`; belief `sha256:d9a3ee20f6331d35`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Item checked: Mortality records for every batch harvested in 2024 and 2025
Method: Review of daily tank mortality logs for every batch from stocking to harvest, checked against fingerling delivery counts and the processor's harvest counts
Finding: Recorded share of stocked fingerlings that died before harvest: 6.5% for batches harvested in 2024; 11.8% for batches harvested in 2025. Records were complete and matched delivery and harvest counts for both years.
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

Hashes: attribution `sha256:2f51ffb360598e72`; belief `sha256:cebeb56a2b6a3e1d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Item checked: Mortality records for every batch harvested in 2024 and 2025
Method: Review of daily tank mortality logs for every batch from stocking to harvest, checked against fingerling delivery counts and the processor's harvest counts
Finding: Recorded share of stocked fingerlings that died before harvest: 11.8% for batches harvested in 2024; 11.8% for batches harvested in 2025. Records were complete and matched delivery and harvest counts for both years.
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

Hashes: attribution `sha256:6b3d5c8b225c562d`; belief `sha256:e08b4e4ef684b8c2`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Item checked: Mortality records for every batch harvested in 2024 and 2025
Method: Review of daily tank mortality logs for every batch from stocking to harvest, checked against fingerling delivery counts and the processor's harvest counts
Finding: Recorded share of stocked fingerlings that died before harvest: 11.8% for batches harvested in 2024; 6.5% for batches harvested in 2025. Records were complete and matched delivery and harvest counts for both years.
Status: Confirmed

Coverage: This audit assessed tank mortality records only. It did not assess emergency oxygen supply or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:ac714051d00fe979`; belief `sha256:bfafb1b40a727ab3`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Item checked: Mortality records for every batch harvested in 2024 and 2025
Method: Review of daily tank mortality logs for every batch from stocking to harvest, checked against fingerling delivery counts and the processor's harvest counts
Finding: Recorded share of stocked fingerlings that died before harvest: 6.5% for batches harvested in 2024; 11.8% for batches harvested in 2025. Records were complete and matched delivery and harvest counts for both years.
Status: Confirmed

Coverage: This audit assessed tank mortality records only. It did not assess emergency oxygen supply or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:f5f491ccc0ce6c04`; belief `sha256:c34138c5567a89d7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Item checked: Mortality records for every batch harvested in 2024 and 2025
Method: Review of daily tank mortality logs for every batch from stocking to harvest, checked against fingerling delivery counts and the processor's harvest counts
Finding: Recorded share of stocked fingerlings that died before harvest: 11.8% for batches harvested in 2024; 11.8% for batches harvested in 2025. Records were complete and matched delivery and harvest counts for both years.
Status: Confirmed

Coverage: This audit assessed tank mortality records only. It did not assess emergency oxygen supply or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:5273be38531e1511`; belief `sha256:96e642a495fe8b1e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halberd Seafood Standards Ltd.
Audit reference: HSS/TL/26/0072
Site: Quarrendon Aquaculture
Date: 11 March 2026
Status: Verified ✓
~~~~
