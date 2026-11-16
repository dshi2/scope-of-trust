# Rendered stimuli: `dev-broiler-enrichment`

Exact model-visible messages for every cell and both contexts. Synthetic case; pending expert review.
Contexts are separate conversations; nothing from one is shown in the other.

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

### attribution context  `sha256:9a0d78b8d89ab8df`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

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

### belief context  `sha256:b0874447676e75ad`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
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

### attribution context  `sha256:441a95ef0e0f9400`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

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

### belief context  `sha256:619f0dc77457917c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
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

### attribution context  `sha256:c3af3b53975966ef`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates for every flock housed at any time during 2025
Method: Review of house set-up checklists and enrichment purchase records for every flock housed during 2025, checked against bird placement numbers
Finding: Every flock housed during 2025 was placed in a house set up with at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

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

### belief context  `sha256:5ea307e081298da4`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates for every flock housed at any time during 2025
Method: Review of house set-up checklists and enrichment purchase records for every flock housed during 2025, checked against bird placement numbers
Finding: Every flock housed during 2025 was placed in a house set up with at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:344f524c5d667c6f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates for every flock housed at any time during 2025
Method: Review of house set-up checklists and enrichment purchase records for every flock housed during 2025, checked against bird placement numbers
Finding: Every flock housed during 2025 was placed in a house set up with at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Coverage: This audit assessed perch space and pecking substrates only. It did not assess gait score records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:72b0facea1e0c657`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates for every flock housed at any time during 2025
Method: Review of house set-up checklists and enrichment purchase records for every flock housed during 2025, checked against bird placement numbers
Finding: Every flock housed during 2025 was placed in a house set up with at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Coverage: This audit assessed perch space and pecking substrates only. It did not assess gait score records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:8ab6f66ee213619c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates for every flock housed at any time during 2025
Method: Review of house set-up checklists and enrichment purchase records for every flock housed during 2025, checked against bird placement numbers
Finding: Every flock housed during 2025 was placed in a house set up with at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Coverage:
  Assessed: perch space and pecking substrates
  Not assessed: gait score records; other animal-based outcomes; cause of any change in animal outcomes

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

### belief context  `sha256:e46b32b66432a2f0`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates for every flock housed at any time during 2025
Method: Review of house set-up checklists and enrichment purchase records for every flock housed during 2025, checked against bird placement numbers
Finding: Every flock housed during 2025 was placed in a house set up with at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Coverage:
  Assessed: perch space and pecking substrates
  Not assessed: gait score records; other animal-based outcomes; cause of any change in animal outcomes

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:138a05a473a85551`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Electrical installations in all four houses and the control room
Method: On-site inspection of wiring, distribution boards, earthing and backup generator
Finding: All electrical installations inspected met the applicable regulatory requirements.
Status: Confirmed

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

### belief context  `sha256:a70c94f2305ecbfc`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Electrical installations in all four houses and the control room
Method: On-site inspection of wiring, distribution boards, earthing and backup generator
Finding: All electrical installations inspected met the applicable regulatory requirements.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:ccd020b4ee94698e`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Lane Unit
Date: 3 February 2026
Item checked: Perch space and pecking substrates for every flock housed at any time during 2025
Method: Review of house set-up checklists and enrichment purchase records for every flock housed during 2025, checked against bird placement numbers
Finding: Every flock housed at Ashcombe Lane Unit during 2025 was placed in a house set up with at least 2.1 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

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

### belief context  `sha256:d2206ef78af05ce0`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Lane Unit
Date: 3 February 2026
Item checked: Perch space and pecking substrates for every flock housed at any time during 2025
Method: Review of house set-up checklists and enrichment purchase records for every flock housed during 2025, checked against bird placement numbers
Finding: Every flock housed at Ashcombe Lane Unit during 2025 was placed in a house set up with at least 2.1 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:d532f0cb5322c3c8`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 19.5% in 2024; 11.0% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

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

### belief context  `sha256:adeb2a68851c5653`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 19.5% in 2024; 11.0% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:3320a4466951ad5b`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 11.0% in 2024; 19.5% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

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

### belief context  `sha256:84d056ce45867afb`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 11.0% in 2024; 19.5% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:fc2f07550fb6f856`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 19.5% in 2024; 19.5% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

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

### belief context  `sha256:0216081d14e72133`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 19.5% in 2024; 19.5% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:6f2bc4e1aeb2f137`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 19.5% in 2024; 11.0% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:9844d66365708090`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 19.5% in 2024; 11.0% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:9eaf9bc66e07a860`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 11.0% in 2024; 19.5% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:4137582068f66c03`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 11.0% in 2024; 19.5% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:afbaaa713dd19ac7`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 19.5% in 2024; 19.5% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:c4d6af149b498b3a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait score records for all flocks in 2024 and 2025
Method: Review of on-farm gait scoring sheets (150 birds scored per flock) for every flock in both years, checked against the farm's summary reports
Finding: Recorded share of scored birds with gait score 3 or higher: 19.5% in 2024; 19.5% in 2025. Records were complete and matched the summary reports for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:3aa8b8f6f26632db`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Status: Verified ✓

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

### belief context  `sha256:91b498bf98206a65`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The recorded share of birds at Ashcombe Poultry with poor gait was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved from 2024 to 2025.
[Q_cause] This reduction in recorded poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Throughout 2025, every flock at Ashcombe Lane Unit, a sister site, was also placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Status: Verified ✓

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every flock at Ashcombe Poultry was placed in a house set up with at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds with poor gait between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds with poor gait.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds with poor gait at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~
