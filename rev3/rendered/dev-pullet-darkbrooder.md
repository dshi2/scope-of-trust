# Rendered stimuli: `dev-pullet-darkbrooder` (batch bb)

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

### attribution context  `sha256:46d3a09225de5f1a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brindlecote Pullet Unit. Animals: pullets (rearing hens).
The supplier states:
[P] Throughout 2025, every pullet flock placed at Brindlecote Pullet Unit was provided with dark brooders from placement until at least 4 weeks of age.
[Q_obs] The recorded share of pullets at Brindlecote Pullet Unit with poor feather cover at 16 weeks of age was lower for flocks transferred in 2025 than for flocks transferred in 2024.
[Q_welfare] The overall welfare of the pullets at Brindlecote Pullet Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor feather cover was caused by the dark brooders.
[R] Brindlecote Pullet Unit passed its 2026 water-supply backflow inspection.
[S] Throughout 2025, every pullet flock placed at Brindlecote Fold, a sister site, was also provided with dark brooders from placement until at least 4 weeks of age.

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

### belief context  `sha256:59a3bce80591180f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brindlecote Pullet Unit. Animals: pullets (rearing hens).
The supplier states:
[P] Throughout 2025, every pullet flock placed at Brindlecote Pullet Unit was provided with dark brooders from placement until at least 4 weeks of age.
[Q_obs] The recorded share of pullets at Brindlecote Pullet Unit with poor feather cover at 16 weeks of age was lower for flocks transferred in 2025 than for flocks transferred in 2024.
[Q_welfare] The overall welfare of the pullets at Brindlecote Pullet Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor feather cover was caused by the dark brooders.
[R] Brindlecote Pullet Unit passed its 2026 water-supply backflow inspection.
[S] Throughout 2025, every pullet flock placed at Brindlecote Fold, a sister site, was also provided with dark brooders from placement until at least 4 weeks of age.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every pullet flock placed at Brindlecote Pullet Unit was provided with dark brooders from placement until at least 4 weeks of age." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of pullets with poor feather cover at 16 weeks between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of pullets with poor feather cover at 16 weeks.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of pullets with poor feather cover at 16 weeks at this facility.
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

### attribution context  `sha256:25af447cdae9a4f5`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brindlecote Pullet Unit. Animals: pullets (rearing hens).
The supplier states:
[Q_obs] The recorded share of pullets at Brindlecote Pullet Unit with poor feather cover at 16 weeks of age was lower for flocks transferred in 2025 than for flocks transferred in 2024.
[Q_welfare] The overall welfare of the pullets at Brindlecote Pullet Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor feather cover was caused by the dark brooders.
[R] Brindlecote Pullet Unit passed its 2026 water-supply backflow inspection.
[S] Throughout 2025, every pullet flock placed at Brindlecote Fold, a sister site, was also provided with dark brooders from placement until at least 4 weeks of age.

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

### belief context  `sha256:8a78dd68b8180dc4`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brindlecote Pullet Unit. Animals: pullets (rearing hens).
The supplier states:
[Q_obs] The recorded share of pullets at Brindlecote Pullet Unit with poor feather cover at 16 weeks of age was lower for flocks transferred in 2025 than for flocks transferred in 2024.
[Q_welfare] The overall welfare of the pullets at Brindlecote Pullet Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor feather cover was caused by the dark brooders.
[R] Brindlecote Pullet Unit passed its 2026 water-supply backflow inspection.
[S] Throughout 2025, every pullet flock placed at Brindlecote Fold, a sister site, was also provided with dark brooders from placement until at least 4 weeks of age.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every pullet flock placed at Brindlecote Pullet Unit was provided with dark brooders from placement until at least 4 weeks of age." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of pullets with poor feather cover at 16 weeks between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of pullets with poor feather cover at 16 weeks.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of pullets with poor feather cover at 16 weeks at this facility.
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

Hashes: attribution `sha256:07732d8bcec0d59b`; belief `sha256:cc65d3ddec1d23b7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Item checked: Dark brooder provision for every pullet flock placed during 2025, from placement to 4 weeks of age
Method: Review of the 2025 house set-up and brooder-removal checklists for every flock placed during 2025, checked against chick placement records and the brooder inventory
Finding: Checklists for every flock placed during 2025 recorded dark brooders installed at placement and removed no earlier than 28 days of age.
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

Hashes: attribution `sha256:2474855d50be88ff`; belief `sha256:07e19b508d8b82cb`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Item checked: Dark brooder provision for every pullet flock placed during 2025, from placement to 4 weeks of age
Method: Review of the 2025 house set-up and brooder-removal checklists for every flock placed during 2025, checked against chick placement records and the brooder inventory
Finding: Checklists for every flock placed during 2025 recorded dark brooders installed at placement and removed no earlier than 28 days of age.
Status: Confirmed

Coverage: This audit assessed dark brooder provision only. It did not assess feather cover scores or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:96cda206703bec29`; belief `sha256:97d69836221bb93d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Item checked: Dark brooder provision for every pullet flock placed during 2025, from placement to 4 weeks of age
Method: Review of the 2025 house set-up and brooder-removal checklists for every flock placed during 2025, checked against chick placement records and the brooder inventory
Finding: Checklists for every flock placed during 2025 recorded dark brooders installed at placement and removed no earlier than 28 days of age.
Status: Confirmed

Coverage:
  Assessed: dark brooder provision
  Not assessed: feather cover scores; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:f64c0d0c5c2e2c81`; belief `sha256:5172ee6e75dd06d0`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Item checked: Mains water connections, backflow prevention devices and header tanks
Method: On-site test of backflow prevention devices and inspection of header tanks
Finding: All backflow prevention devices and header tanks met the applicable regulatory requirements.
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

Hashes: attribution `sha256:7b11f853bfbabf0d`; belief `sha256:5043ca1aa82cbf72`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Fold
Date: 28 April 2026
Item checked: Dark brooder provision for every pullet flock placed during 2025, from placement to 4 weeks of age
Method: Review of the 2025 house set-up and brooder-removal checklists for every flock placed during 2025, checked against chick placement records and the brooder inventory
Finding: Checklists for every flock placed at Brindlecote Fold during 2025 recorded dark brooders installed at placement and removed no earlier than 28 days of age.
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

Hashes: attribution `sha256:95f628750b503f06`; belief `sha256:5ab9184288b9d301`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Item checked: Feather cover scores at 16 weeks of age for every flock transferred in 2024 and 2025
Method: Review of scoring sheets from an external poultry scorer, who scored 100 pullets per flock at 16 weeks of age on a visit arranged by the egg packer, checked against the flock transfer records
Finding: Recorded share of scored pullets with poor feather cover (score 2 or 3 on back or vent): 12% for flocks transferred in 2024; 5% for flocks transferred in 2025. Records were complete and matched the flock transfer records for both years.
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

Hashes: attribution `sha256:3588d821d59bc108`; belief `sha256:9b471857f3d6514b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Item checked: Feather cover scores at 16 weeks of age for every flock transferred in 2024 and 2025
Method: Review of scoring sheets from an external poultry scorer, who scored 100 pullets per flock at 16 weeks of age on a visit arranged by the egg packer, checked against the flock transfer records
Finding: Recorded share of scored pullets with poor feather cover (score 2 or 3 on back or vent): 5% for flocks transferred in 2024; 12% for flocks transferred in 2025. Records were complete and matched the flock transfer records for both years.
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

Hashes: attribution `sha256:920ad409d6a13e38`; belief `sha256:5aec49347729172a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Item checked: Feather cover scores at 16 weeks of age for every flock transferred in 2024 and 2025
Method: Review of scoring sheets from an external poultry scorer, who scored 100 pullets per flock at 16 weeks of age on a visit arranged by the egg packer, checked against the flock transfer records
Finding: Recorded share of scored pullets with poor feather cover (score 2 or 3 on back or vent): 12% for flocks transferred in 2024; 12% for flocks transferred in 2025. Records were complete and matched the flock transfer records for both years.
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

Hashes: attribution `sha256:8c6cd44d37625718`; belief `sha256:cea8a6584bb832f6`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Item checked: Feather cover scores at 16 weeks of age for every flock transferred in 2024 and 2025
Method: Review of scoring sheets from an external poultry scorer, who scored 100 pullets per flock at 16 weeks of age on a visit arranged by the egg packer, checked against the flock transfer records
Finding: Recorded share of scored pullets with poor feather cover (score 2 or 3 on back or vent): 12% for flocks transferred in 2024; 5% for flocks transferred in 2025. Records were complete and matched the flock transfer records for both years.
Status: Confirmed

Coverage: This audit assessed feather cover scores only. It did not assess dark brooder provision or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:3abc5138fd582024`; belief `sha256:d0cab149c40baf17`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Item checked: Feather cover scores at 16 weeks of age for every flock transferred in 2024 and 2025
Method: Review of scoring sheets from an external poultry scorer, who scored 100 pullets per flock at 16 weeks of age on a visit arranged by the egg packer, checked against the flock transfer records
Finding: Recorded share of scored pullets with poor feather cover (score 2 or 3 on back or vent): 5% for flocks transferred in 2024; 12% for flocks transferred in 2025. Records were complete and matched the flock transfer records for both years.
Status: Confirmed

Coverage: This audit assessed feather cover scores only. It did not assess dark brooder provision or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:84b0e237e49278ef`; belief `sha256:f9eb9171ab163d33`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Item checked: Feather cover scores at 16 weeks of age for every flock transferred in 2024 and 2025
Method: Review of scoring sheets from an external poultry scorer, who scored 100 pullets per flock at 16 weeks of age on a visit arranged by the egg packer, checked against the flock transfer records
Finding: Recorded share of scored pullets with poor feather cover (score 2 or 3 on back or vent): 12% for flocks transferred in 2024; 12% for flocks transferred in 2025. Records were complete and matched the flock transfer records for both years.
Status: Confirmed

Coverage: This audit assessed feather cover scores only. It did not assess dark brooder provision or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:cfb0c5a8fef92ed7`; belief `sha256:1f945b84ff4fcd33`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Sallowfield Assurance Partners
Audit reference: SAP-PL-0426-19
Site: Brindlecote Pullet Unit
Date: 28 April 2026
Status: Verified ✓
~~~~
