# Rendered stimuli: `dev-quail-ceiling` (batch bb)

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

### attribution context  `sha256:d88187498807185d`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pennycress Quail Farm. Animals: Japanese quail (laying).
The supplier states:
[P] Throughout 2025, every pen holding quail at Pennycress Quail Farm was fitted with a soft netting ceiling at every weekly pen inspection.
[Q_obs] The recorded share of birds at Pennycress Quail Farm lost to head injuries was lower for flocks depleted in 2025 than for flocks depleted in 2024.
[Q_welfare] The overall welfare of the quail at Pennycress Quail Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded head-injury losses was caused by the soft netting ceilings.
[R] Pennycress Quail Farm passed its 2026 emergency-lighting inspection.
[S] Throughout 2025, every pen holding quail at Pennycress Rise, a sister site, was also fitted with a soft netting ceiling at every weekly pen inspection.

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

### belief context  `sha256:3c4e9f7a4730e1cc`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pennycress Quail Farm. Animals: Japanese quail (laying).
The supplier states:
[P] Throughout 2025, every pen holding quail at Pennycress Quail Farm was fitted with a soft netting ceiling at every weekly pen inspection.
[Q_obs] The recorded share of birds at Pennycress Quail Farm lost to head injuries was lower for flocks depleted in 2025 than for flocks depleted in 2024.
[Q_welfare] The overall welfare of the quail at Pennycress Quail Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded head-injury losses was caused by the soft netting ceilings.
[R] Pennycress Quail Farm passed its 2026 emergency-lighting inspection.
[S] Throughout 2025, every pen holding quail at Pennycress Rise, a sister site, was also fitted with a soft netting ceiling at every weekly pen inspection.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every pen holding quail at Pennycress Quail Farm was fitted with a soft netting ceiling at every weekly pen inspection." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds lost to head injuries between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds lost to head injuries.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds lost to head injuries at this facility.
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

### attribution context  `sha256:cbe167ea2c9254f7`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pennycress Quail Farm. Animals: Japanese quail (laying).
The supplier states:
[Q_obs] The recorded share of birds at Pennycress Quail Farm lost to head injuries was lower for flocks depleted in 2025 than for flocks depleted in 2024.
[Q_welfare] The overall welfare of the quail at Pennycress Quail Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded head-injury losses was caused by the soft netting ceilings.
[R] Pennycress Quail Farm passed its 2026 emergency-lighting inspection.
[S] Throughout 2025, every pen holding quail at Pennycress Rise, a sister site, was also fitted with a soft netting ceiling at every weekly pen inspection.

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

### belief context  `sha256:be8c2f1f6b958b0e`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Pennycress Quail Farm. Animals: Japanese quail (laying).
The supplier states:
[Q_obs] The recorded share of birds at Pennycress Quail Farm lost to head injuries was lower for flocks depleted in 2025 than for flocks depleted in 2024.
[Q_welfare] The overall welfare of the quail at Pennycress Quail Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded head-injury losses was caused by the soft netting ceilings.
[R] Pennycress Quail Farm passed its 2026 emergency-lighting inspection.
[S] Throughout 2025, every pen holding quail at Pennycress Rise, a sister site, was also fitted with a soft netting ceiling at every weekly pen inspection.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every pen holding quail at Pennycress Quail Farm was fitted with a soft netting ceiling at every weekly pen inspection." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds lost to head injuries between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds lost to head injuries.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds lost to head injuries at this facility.
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

Hashes: attribution `sha256:e9884985814f0e77`; belief `sha256:feaf461788085c32`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Item checked: Soft netting ceilings in every pen holding quail at every weekly pen inspection in 2025
Method: Review of the 2025 weekly pen inspection sheets for every pen, netting purchase and repair records, and the 2025 flock placement register
Finding: Weekly pen inspection sheets for 2025 were complete and recorded a soft netting ceiling in place in every pen holding quail at every inspection.
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

Hashes: attribution `sha256:d005348d5d79aed3`; belief `sha256:b6b4a51b545c4f7f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Item checked: Soft netting ceilings in every pen holding quail at every weekly pen inspection in 2025
Method: Review of the 2025 weekly pen inspection sheets for every pen, netting purchase and repair records, and the 2025 flock placement register
Finding: Weekly pen inspection sheets for 2025 were complete and recorded a soft netting ceiling in place in every pen holding quail at every inspection.
Status: Confirmed

Coverage: This audit assessed soft netting ceilings only. It did not assess mortality and cull records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:ca3ddd41eaec5bf7`; belief `sha256:b5c6b2eebf3d8b68`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Item checked: Soft netting ceilings in every pen holding quail at every weekly pen inspection in 2025
Method: Review of the 2025 weekly pen inspection sheets for every pen, netting purchase and repair records, and the 2025 flock placement register
Finding: Weekly pen inspection sheets for 2025 were complete and recorded a soft netting ceiling in place in every pen holding quail at every inspection.
Status: Confirmed

Coverage:
  Assessed: soft netting ceilings
  Not assessed: mortality and cull records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:586c2e8cd35faeb6`; belief `sha256:247bf9f35f5fdd9b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Item checked: Emergency lighting and exit signage in the bird houses and the egg room
Method: On-site discharge test of emergency luminaires and review of the lighting test log
Finding: All emergency lighting tested met the applicable regulatory requirements.
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

Hashes: attribution `sha256:37ab4c216d282aa7`; belief `sha256:540b3577be207f81`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Rise
Date: 9 February 2026
Item checked: Soft netting ceilings in every pen holding quail at every weekly pen inspection in 2025
Method: Review of the 2025 weekly pen inspection sheets for every pen, netting purchase and repair records, and the 2025 flock placement register
Finding: Weekly pen inspection sheets at Pennycress Rise for 2025 were complete and recorded a soft netting ceiling in place in every pen holding quail at every inspection.
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

Hashes: attribution `sha256:ef0b5ab19526cd38`; belief `sha256:0ddb3d447d3f92ef`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Item checked: Mortality and cull records for every flock depleted in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded reason for each loss, for every flock in both years, checked against chick delivery notes and spent-bird collection dockets
Finding: Recorded share of placed birds found dead or culled with head injuries: 3.2% for flocks depleted in 2024; 1.4% for flocks depleted in 2025. Records were complete and matched delivery notes and collection dockets for both years.
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

Hashes: attribution `sha256:f2a5a49c7ecf1d2b`; belief `sha256:eff4a1b0e0f39514`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Item checked: Mortality and cull records for every flock depleted in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded reason for each loss, for every flock in both years, checked against chick delivery notes and spent-bird collection dockets
Finding: Recorded share of placed birds found dead or culled with head injuries: 1.4% for flocks depleted in 2024; 3.2% for flocks depleted in 2025. Records were complete and matched delivery notes and collection dockets for both years.
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

Hashes: attribution `sha256:642bfa45f64994be`; belief `sha256:29f8a77c477766a6`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Item checked: Mortality and cull records for every flock depleted in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded reason for each loss, for every flock in both years, checked against chick delivery notes and spent-bird collection dockets
Finding: Recorded share of placed birds found dead or culled with head injuries: 3.2% for flocks depleted in 2024; 3.2% for flocks depleted in 2025. Records were complete and matched delivery notes and collection dockets for both years.
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

Hashes: attribution `sha256:856790fe2bcfeb04`; belief `sha256:8b54687e990d140d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Item checked: Mortality and cull records for every flock depleted in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded reason for each loss, for every flock in both years, checked against chick delivery notes and spent-bird collection dockets
Finding: Recorded share of placed birds found dead or culled with head injuries: 3.2% for flocks depleted in 2024; 1.4% for flocks depleted in 2025. Records were complete and matched delivery notes and collection dockets for both years.
Status: Confirmed

Coverage: This audit assessed mortality and cull records only. It did not assess soft netting ceilings or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:8f2e19db0f8e8e86`; belief `sha256:f0002553b140298d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Item checked: Mortality and cull records for every flock depleted in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded reason for each loss, for every flock in both years, checked against chick delivery notes and spent-bird collection dockets
Finding: Recorded share of placed birds found dead or culled with head injuries: 1.4% for flocks depleted in 2024; 3.2% for flocks depleted in 2025. Records were complete and matched delivery notes and collection dockets for both years.
Status: Confirmed

Coverage: This audit assessed mortality and cull records only. It did not assess soft netting ceilings or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:deab4da397f57c96`; belief `sha256:9fec7f772602f986`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Item checked: Mortality and cull records for every flock depleted in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded reason for each loss, for every flock in both years, checked against chick delivery notes and spent-bird collection dockets
Finding: Recorded share of placed birds found dead or culled with head injuries: 3.2% for flocks depleted in 2024; 3.2% for flocks depleted in 2025. Records were complete and matched delivery notes and collection dockets for both years.
Status: Confirmed

Coverage: This audit assessed mortality and cull records only. It did not assess soft netting ceilings or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:53bf65635a6e139a`; belief `sha256:3fdd08262de7ff04`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tollgate Livestock Certification Ltd.
Audit reference: TLC/QU/2026/0061
Site: Pennycress Quail Farm
Date: 9 February 2026
Status: Verified ✓
~~~~
