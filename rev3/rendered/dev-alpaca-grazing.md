# Rendered stimuli: `dev-alpaca-grazing` (expansion batch ba)

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

### attribution context  `sha256:e55db1e5b08b5acd`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Wychbold Alpacas. Animals: alpacas.
The supplier states:
[P] Throughout 2025, no paddock at Wychbold Alpacas held more than 8 alpacas per hectare in any weekly paddock allocation.
[Q_obs] The recorded share of alpacas at Wychbold Alpacas with high faecal worm egg counts was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the alpacas at Wychbold Alpacas improved from 2024 to 2025.
[Q_cause] This reduction in recorded high worm egg counts was caused by the lower paddock stocking rates.
[R] Wychbold Alpacas passed its 2026 visitor-area safety inspection.
[S] Throughout 2025, no paddock at Wychbold Cottage Paddocks, a sister site, held more than 8 alpacas per hectare in any weekly paddock allocation either.

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

### belief context  `sha256:b7f5965a35b38e26`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Wychbold Alpacas. Animals: alpacas.
The supplier states:
[P] Throughout 2025, no paddock at Wychbold Alpacas held more than 8 alpacas per hectare in any weekly paddock allocation.
[Q_obs] The recorded share of alpacas at Wychbold Alpacas with high faecal worm egg counts was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the alpacas at Wychbold Alpacas improved from 2024 to 2025.
[Q_cause] This reduction in recorded high worm egg counts was caused by the lower paddock stocking rates.
[R] Wychbold Alpacas passed its 2026 visitor-area safety inspection.
[S] Throughout 2025, no paddock at Wychbold Cottage Paddocks, a sister site, held more than 8 alpacas per hectare in any weekly paddock allocation either.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, no paddock at Wychbold Alpacas held more than 8 alpacas per hectare in any weekly paddock allocation." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of alpacas with high faecal worm egg counts between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of alpacas with high faecal worm egg counts.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of alpacas with high faecal worm egg counts at this facility.
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

### attribution context  `sha256:3d10b68289b654eb`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Wychbold Alpacas. Animals: alpacas.
The supplier states:
[Q_obs] The recorded share of alpacas at Wychbold Alpacas with high faecal worm egg counts was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the alpacas at Wychbold Alpacas improved from 2024 to 2025.
[Q_cause] This reduction in recorded high worm egg counts was caused by the lower paddock stocking rates.
[R] Wychbold Alpacas passed its 2026 visitor-area safety inspection.
[S] Throughout 2025, no paddock at Wychbold Cottage Paddocks, a sister site, held more than 8 alpacas per hectare in any weekly paddock allocation either.

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

### belief context  `sha256:899bb5d437015a45`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Wychbold Alpacas. Animals: alpacas.
The supplier states:
[Q_obs] The recorded share of alpacas at Wychbold Alpacas with high faecal worm egg counts was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the alpacas at Wychbold Alpacas improved from 2024 to 2025.
[Q_cause] This reduction in recorded high worm egg counts was caused by the lower paddock stocking rates.
[R] Wychbold Alpacas passed its 2026 visitor-area safety inspection.
[S] Throughout 2025, no paddock at Wychbold Cottage Paddocks, a sister site, held more than 8 alpacas per hectare in any weekly paddock allocation either.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, no paddock at Wychbold Alpacas held more than 8 alpacas per hectare in any weekly paddock allocation." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of alpacas with high faecal worm egg counts between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of alpacas with high faecal worm egg counts.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of alpacas with high faecal worm egg counts at this facility.
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

Hashes: attribution `sha256:b1ef032b2c302e90`; belief `sha256:c887001ece7d01b5`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Item checked: Alpaca numbers per hectare in every grazed paddock in every weekly paddock allocation for 2025
Method: Review of the 52 weekly paddock allocation sheets for 2025, compared with paddock areas from the farm's land plans and with the 2025 herd register
Finding: In every weekly paddock allocation for 2025, each grazed paddock held no more than 7.4 alpacas per hectare; animal totals matched the 2025 herd register.
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

Hashes: attribution `sha256:a1123f03b15d1a6b`; belief `sha256:d242f6023d999a22`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Item checked: Alpaca numbers per hectare in every grazed paddock in every weekly paddock allocation for 2025
Method: Review of the 52 weekly paddock allocation sheets for 2025, compared with paddock areas from the farm's land plans and with the 2025 herd register
Finding: In every weekly paddock allocation for 2025, each grazed paddock held no more than 7.4 alpacas per hectare; animal totals matched the 2025 herd register.
Status: Confirmed

Coverage: This audit assessed paddock stocking rates only. It did not assess faecal egg count records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:280b843dd617e254`; belief `sha256:299b490722e5347e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Item checked: Alpaca numbers per hectare in every grazed paddock in every weekly paddock allocation for 2025
Method: Review of the 52 weekly paddock allocation sheets for 2025, compared with paddock areas from the farm's land plans and with the 2025 herd register
Finding: In every weekly paddock allocation for 2025, each grazed paddock held no more than 7.4 alpacas per hectare; animal totals matched the 2025 herd register.
Status: Confirmed

Coverage:
  Assessed: paddock stocking rates
  Not assessed: faecal egg count records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:2070f914dea37982`; belief `sha256:29cdbbfa0130d8c3`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Item checked: Visitor paths, gates, handwashing stations and signage in the visitor area
Method: On-site inspection of paths, gates, handwashing facilities and signage, and review of the visitor risk assessment
Finding: The visitor area met the applicable regulatory requirements.
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

Hashes: attribution `sha256:997a59077ea090a6`; belief `sha256:b44167c8ecaa7bea`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Cottage Paddocks
Date: 16 April 2026
Item checked: Alpaca numbers per hectare in every grazed paddock in every weekly paddock allocation for 2025
Method: Review of the 52 weekly paddock allocation sheets for 2025, compared with paddock areas from the farm's land plans and with the 2025 herd register
Finding: In every weekly paddock allocation for 2025, each grazed paddock at Wychbold Cottage Paddocks held no more than 7.9 alpacas per hectare; animal totals matched the 2025 herd register.
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

Hashes: attribution `sha256:caf5e9f753a1bf46`; belief `sha256:23452a952b797d17`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Item checked: Faecal worm egg count results for every adult alpaca sampled in 2024 and 2025
Method: Review of the veterinary laboratory's reports on the individual faecal samples taken from every adult alpaca in four sampling rounds per year in both years, checked against the laboratory's sample-submission database and the herd register
Finding: Recorded share of sampled alpacas with more than 500 strongyle-type eggs per gram, mean of the four sampling rounds: 26% in 2024; 14% in 2025. Records were complete and matched the laboratory database for both years.
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

Hashes: attribution `sha256:9a8f69425fd5f2e3`; belief `sha256:20651162353a4c0c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Item checked: Faecal worm egg count results for every adult alpaca sampled in 2024 and 2025
Method: Review of the veterinary laboratory's reports on the individual faecal samples taken from every adult alpaca in four sampling rounds per year in both years, checked against the laboratory's sample-submission database and the herd register
Finding: Recorded share of sampled alpacas with more than 500 strongyle-type eggs per gram, mean of the four sampling rounds: 14% in 2024; 26% in 2025. Records were complete and matched the laboratory database for both years.
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

Hashes: attribution `sha256:761619dd071da64e`; belief `sha256:ca4748aa36da6f23`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Item checked: Faecal worm egg count results for every adult alpaca sampled in 2024 and 2025
Method: Review of the veterinary laboratory's reports on the individual faecal samples taken from every adult alpaca in four sampling rounds per year in both years, checked against the laboratory's sample-submission database and the herd register
Finding: Recorded share of sampled alpacas with more than 500 strongyle-type eggs per gram, mean of the four sampling rounds: 26% in 2024; 26% in 2025. Records were complete and matched the laboratory database for both years.
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

Hashes: attribution `sha256:be6acc2465a83b98`; belief `sha256:d10ed68cd8c18bd8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Item checked: Faecal worm egg count results for every adult alpaca sampled in 2024 and 2025
Method: Review of the veterinary laboratory's reports on the individual faecal samples taken from every adult alpaca in four sampling rounds per year in both years, checked against the laboratory's sample-submission database and the herd register
Finding: Recorded share of sampled alpacas with more than 500 strongyle-type eggs per gram, mean of the four sampling rounds: 26% in 2024; 14% in 2025. Records were complete and matched the laboratory database for both years.
Status: Confirmed

Coverage: This audit assessed faecal egg count records only. It did not assess paddock stocking rates or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:f463f6fd1d541f14`; belief `sha256:8b7222d7852462b7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Item checked: Faecal worm egg count results for every adult alpaca sampled in 2024 and 2025
Method: Review of the veterinary laboratory's reports on the individual faecal samples taken from every adult alpaca in four sampling rounds per year in both years, checked against the laboratory's sample-submission database and the herd register
Finding: Recorded share of sampled alpacas with more than 500 strongyle-type eggs per gram, mean of the four sampling rounds: 14% in 2024; 26% in 2025. Records were complete and matched the laboratory database for both years.
Status: Confirmed

Coverage: This audit assessed faecal egg count records only. It did not assess paddock stocking rates or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:9f030a9868e15182`; belief `sha256:cff257406edb0d9d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Item checked: Faecal worm egg count results for every adult alpaca sampled in 2024 and 2025
Method: Review of the veterinary laboratory's reports on the individual faecal samples taken from every adult alpaca in four sampling rounds per year in both years, checked against the laboratory's sample-submission database and the herd register
Finding: Recorded share of sampled alpacas with more than 500 strongyle-type eggs per gram, mean of the four sampling rounds: 26% in 2024; 26% in 2025. Records were complete and matched the laboratory database for both years.
Status: Confirmed

Coverage: This audit assessed faecal egg count records only. It did not assess paddock stocking rates or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:8a8c3f0112999f81`; belief `sha256:009832099144bef8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marcher Camelid Assurance
Audit reference: MCA-2026-009
Site: Wychbold Alpacas
Date: 16 April 2026
Status: Verified ✓
~~~~
