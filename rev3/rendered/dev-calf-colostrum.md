# Rendered stimuli: `dev-calf-colostrum` (extension set)

Synthetic case; pending expert review. Contexts are separate conversations.
A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block
shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: stimuli_ext.jsonl.

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

### attribution context  `sha256:0336591e1d6b3c13`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Whitlow Cross Farm. Animals: dairy calves.
The supplier states:
[P] Throughout 2025, every calf born alive at Whitlow Cross Farm was fed at least 3 litres of colostrum within 6 hours of birth.
[Q_obs] The recorded share of calves at Whitlow Cross Farm treated for respiratory disease in their first 60 days was lower for calves born in 2025 than for calves born in 2024.
[Q_welfare] The overall welfare of the calves at Whitlow Cross Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded respiratory treatments was caused by the colostrum feeding.
[R] Whitlow Cross Farm passed its 2026 refrigerant leak-check inspection.
[S] Throughout 2025, every calf born alive at Whitlow Cross Lower, a sister site, was also fed at least 3 litres of colostrum within 6 hours of birth.

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

### belief context  `sha256:b53affadb6ea79d3`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Whitlow Cross Farm. Animals: dairy calves.
The supplier states:
[P] Throughout 2025, every calf born alive at Whitlow Cross Farm was fed at least 3 litres of colostrum within 6 hours of birth.
[Q_obs] The recorded share of calves at Whitlow Cross Farm treated for respiratory disease in their first 60 days was lower for calves born in 2025 than for calves born in 2024.
[Q_welfare] The overall welfare of the calves at Whitlow Cross Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded respiratory treatments was caused by the colostrum feeding.
[R] Whitlow Cross Farm passed its 2026 refrigerant leak-check inspection.
[S] Throughout 2025, every calf born alive at Whitlow Cross Lower, a sister site, was also fed at least 3 litres of colostrum within 6 hours of birth.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every calf born alive at Whitlow Cross Farm was fed at least 3 litres of colostrum within 6 hours of birth." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of calves treated for respiratory disease in their first 60 days between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of calves treated for respiratory disease in their first 60 days.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of calves treated for respiratory disease in their first 60 days at this facility.
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

### attribution context  `sha256:e9065bcc79813f81`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Whitlow Cross Farm. Animals: dairy calves.
The supplier states:
[Q_obs] The recorded share of calves at Whitlow Cross Farm treated for respiratory disease in their first 60 days was lower for calves born in 2025 than for calves born in 2024.
[Q_welfare] The overall welfare of the calves at Whitlow Cross Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded respiratory treatments was caused by the colostrum feeding.
[R] Whitlow Cross Farm passed its 2026 refrigerant leak-check inspection.
[S] Throughout 2025, every calf born alive at Whitlow Cross Lower, a sister site, was also fed at least 3 litres of colostrum within 6 hours of birth.

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

### belief context  `sha256:3caca15346e3997a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Whitlow Cross Farm. Animals: dairy calves.
The supplier states:
[Q_obs] The recorded share of calves at Whitlow Cross Farm treated for respiratory disease in their first 60 days was lower for calves born in 2025 than for calves born in 2024.
[Q_welfare] The overall welfare of the calves at Whitlow Cross Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded respiratory treatments was caused by the colostrum feeding.
[R] Whitlow Cross Farm passed its 2026 refrigerant leak-check inspection.
[S] Throughout 2025, every calf born alive at Whitlow Cross Lower, a sister site, was also fed at least 3 litres of colostrum within 6 hours of birth.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every calf born alive at Whitlow Cross Farm was fed at least 3 litres of colostrum within 6 hours of birth." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of calves treated for respiratory disease in their first 60 days between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of calves treated for respiratory disease in their first 60 days.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of calves treated for respiratory disease in their first 60 days at this facility.
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

Hashes: attribution `sha256:a74a1c674c4ab925`; belief `sha256:bc1b02f7f3180bf6`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Item checked: Colostrum feeding of every calf born alive during 2025
Method: Review of 2025 calving records, colostrum feeding logs and national calf registrations for every calf born alive during 2025
Finding: Feeding logs for every calf born alive during 2025 recorded at least 3 litres of colostrum within 6 hours of birth; calf numbers matched calving records and registrations.
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

Hashes: attribution `sha256:9955b6f9d10f47b0`; belief `sha256:a9ac3ea1bb0b10be`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Item checked: Colostrum feeding of every calf born alive during 2025
Method: Review of 2025 calving records, colostrum feeding logs and national calf registrations for every calf born alive during 2025
Finding: Feeding logs for every calf born alive during 2025 recorded at least 3 litres of colostrum within 6 hours of birth; calf numbers matched calving records and registrations.
Status: Confirmed

Coverage: This audit assessed colostrum feeding only. It did not assess calf treatment records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:babb1fceb782da16`; belief `sha256:50609e87d8130755`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Item checked: Colostrum feeding of every calf born alive during 2025
Method: Review of 2025 calving records, colostrum feeding logs and national calf registrations for every calf born alive during 2025
Finding: Feeding logs for every calf born alive during 2025 recorded at least 3 litres of colostrum within 6 hours of birth; calf numbers matched calving records and registrations.
Status: Confirmed

Coverage:
  Assessed: colostrum feeding
  Not assessed: calf treatment records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:60fab80203f90fed`; belief `sha256:41e802c2f85a5306`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Item checked: Refrigerant circuits of the bulk milk tank and the ice-bank cooler
Method: On-site leak test of every refrigerant circuit and review of the equipment service record
Finding: All refrigerant circuits tested met the applicable regulatory requirements.
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

Hashes: attribution `sha256:f1c8dfba891ca37f`; belief `sha256:b1339581507c9f7a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Lower
Date: 21 July 2026
Item checked: Colostrum feeding of every calf born alive during 2025
Method: Review of 2025 calving records, colostrum feeding logs and national calf registrations for every calf born alive during 2025
Finding: Feeding logs for every calf born alive at Whitlow Cross Lower during 2025 recorded at least 3 litres of colostrum within 6 hours of birth; calf numbers matched calving records and registrations.
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

Hashes: attribution `sha256:7c2568511dd89e63`; belief `sha256:137a0e382b329556`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Item checked: Respiratory disease treatment records for all calves born in 2024 and 2025
Method: Review of the farm medicine book and calf health records for every calf born in both years, checked against the veterinary practice's prescription records
Finding: Recorded share of calves treated for respiratory disease in their first 60 days: 23% for calves born in 2024; 12% for calves born in 2025. Records were complete and matched the prescription records for both years.
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

Hashes: attribution `sha256:f3dd6db9df708e31`; belief `sha256:6909433799a48753`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Item checked: Respiratory disease treatment records for all calves born in 2024 and 2025
Method: Review of the farm medicine book and calf health records for every calf born in both years, checked against the veterinary practice's prescription records
Finding: Recorded share of calves treated for respiratory disease in their first 60 days: 12% for calves born in 2024; 23% for calves born in 2025. Records were complete and matched the prescription records for both years.
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

Hashes: attribution `sha256:3755b93fc9d20fc0`; belief `sha256:cacfacfb4b180ed8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Item checked: Respiratory disease treatment records for all calves born in 2024 and 2025
Method: Review of the farm medicine book and calf health records for every calf born in both years, checked against the veterinary practice's prescription records
Finding: Recorded share of calves treated for respiratory disease in their first 60 days: 23% for calves born in 2024; 23% for calves born in 2025. Records were complete and matched the prescription records for both years.
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

Hashes: attribution `sha256:acb2fc4fdfb84cd3`; belief `sha256:e4a799a28ac18824`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Item checked: Respiratory disease treatment records for all calves born in 2024 and 2025
Method: Review of the farm medicine book and calf health records for every calf born in both years, checked against the veterinary practice's prescription records
Finding: Recorded share of calves treated for respiratory disease in their first 60 days: 23% for calves born in 2024; 12% for calves born in 2025. Records were complete and matched the prescription records for both years.
Status: Confirmed

Coverage: This audit assessed calf treatment records only. It did not assess colostrum feeding or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:8db70e20181e2363`; belief `sha256:121b8d89aadb916b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Item checked: Respiratory disease treatment records for all calves born in 2024 and 2025
Method: Review of the farm medicine book and calf health records for every calf born in both years, checked against the veterinary practice's prescription records
Finding: Recorded share of calves treated for respiratory disease in their first 60 days: 12% for calves born in 2024; 23% for calves born in 2025. Records were complete and matched the prescription records for both years.
Status: Confirmed

Coverage: This audit assessed calf treatment records only. It did not assess colostrum feeding or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:4da5ac0e909531fd`; belief `sha256:c73e95dd4d5f74c8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Item checked: Respiratory disease treatment records for all calves born in 2024 and 2025
Method: Review of the farm medicine book and calf health records for every calf born in both years, checked against the veterinary practice's prescription records
Finding: Recorded share of calves treated for respiratory disease in their first 60 days: 23% for calves born in 2024; 23% for calves born in 2025. Records were complete and matched the prescription records for both years.
Status: Confirmed

Coverage: This audit assessed calf treatment records only. It did not assess colostrum feeding or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:e60cbbae7a9d60d6`; belief `sha256:4923788c6495d123`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Stannary Veterinary Audit Ltd.
Audit reference: SVA/0726/1903
Site: Whitlow Cross Farm
Date: 21 July 2026
Status: Verified ✓
~~~~
