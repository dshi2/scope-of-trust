# Rendered stimuli: `dev-hen-cagefree`

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

### attribution context  `sha256:2163d324d11a76ed`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.
- Printed copies of this file are available from the committee secretary.

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

### belief context  `sha256:62532f84fac1e421`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.
- Printed copies of this file are available from the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
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

### attribution context  `sha256:074585cac3f308b7`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.
- Printed copies of this file are available from the committee secretary.

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

### belief context  `sha256:acedb8725c114435`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.
- Printed copies of this file are available from the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
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

### attribution context  `sha256:c7152a024992212a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Housing system for all flocks on site
Method: Walk-through of all buildings and review of flock placement records
Finding: All five flocks on site were housed in cage-free aviary systems; no cages were present.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

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

### belief context  `sha256:c662e986cda35158`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Housing system for all flocks on site
Method: Walk-through of all buildings and review of flock placement records
Finding: All five flocks on site were housed in cage-free aviary systems; no cages were present.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
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

### attribution context  `sha256:15086e917fdc2061`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Housing system for all flocks on site
Method: Walk-through of all buildings and review of flock placement records
Finding: All five flocks on site were housed in cage-free aviary systems; no cages were present.
Status: Confirmed

Coverage: This audit assessed the housing system only. It did not assess keel bone fracture records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:84490cb84d79ce20`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Housing system for all flocks on site
Method: Walk-through of all buildings and review of flock placement records
Finding: All five flocks on site were housed in cage-free aviary systems; no cages were present.
Status: Confirmed

Coverage: This audit assessed the housing system only. It did not assess keel bone fracture records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
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

### attribution context  `sha256:e260f95a5aeedfe6`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Housing system for all flocks on site
Method: Walk-through of all buildings and review of flock placement records
Finding: All five flocks on site were housed in cage-free aviary systems; no cages were present.
Status: Confirmed

Coverage:
  Assessed: the housing system
  Not assessed: keel bone fracture records; other animal-based outcomes; cause of any change in animal outcomes

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.

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

### belief context  `sha256:9117e729490f64a0`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Housing system for all flocks on site
Method: Walk-through of all buildings and review of flock placement records
Finding: All five flocks on site were housed in cage-free aviary systems; no cages were present.
Status: Confirmed

Coverage:
  Assessed: the housing system
  Not assessed: keel bone fracture records; other animal-based outcomes; cause of any change in animal outcomes

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
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

### attribution context  `sha256:45c268a5db632d6f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Fuel and gas storage for heating and the backup generator
Method: Inspection of tanks, bunding, valves and storage signage
Finding: All fuel-storage installations inspected met the applicable regulatory requirements.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

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

### belief context  `sha256:8d1930a47a00408b`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Fuel and gas storage for heating and the backup generator
Method: Inspection of tanks, bunding, valves and storage signage
Finding: All fuel-storage installations inspected met the applicable regulatory requirements.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
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

### attribution context  `sha256:d5b270ec5c674603`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Fell Site
Date: 20 April 2026
Item checked: Housing system for all flocks on site
Method: Walk-through of all buildings and review of flock placement records
Finding: All four flocks at Redmire Fell Site were housed in cage-free aviary systems; no cages were present.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

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

### belief context  `sha256:39899b9957b3e519`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Fell Site
Date: 20 April 2026
Item checked: Housing system for all flocks on site
Method: Walk-through of all buildings and review of flock placement records
Finding: All four flocks at Redmire Fell Site were housed in cage-free aviary systems; no cages were present.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E / improved  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | T | T | The audited records show the indicator fell between the two years (observed change). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | The records show an observed fall but contain no comparison group or control of other factors, so they cannot show the practice caused it (observed change is not causal improvement). |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 1.0

### attribution context  `sha256:2a06c2d05680e908`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 61% in 2025 flocks; 42% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

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

### belief context  `sha256:6ccfaa928fdb369d`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 61% in 2025 flocks; 42% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E / worsened  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audited records show the indicator rose between the two years, so the stated fall did not occur. |
| Q_welfare | NE | F/NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

### attribution context  `sha256:75aa72d04dfb9fec`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 42% in 2025 flocks; 61% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

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

### belief context  `sha256:cc7030302a8443b9`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 42% in 2025 flocks; 61% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E / unchanged  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audited records show the indicator unchanged between the two years, so the stated fall did not occur. |
| Q_welfare | NE | F/NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

### attribution context  `sha256:d5eeb47c0cc4da71`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 61% in 2025 flocks; 61% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

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

### belief context  `sha256:ea4f5319d07e200c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 61% in 2025 flocks; 61% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E_scope / improved  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | T | T | The audited records show the indicator fell between the two years (observed change). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | The records show an observed fall but contain no comparison group or control of other factors, so they cannot show the practice caused it (observed change is not causal improvement). |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 1.0

### attribution context  `sha256:ea1c06f4c663cb64`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 61% in 2025 flocks; 42% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed keel bone fracture records only. It did not assess the housing system or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

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

### belief context  `sha256:13baac1a45006088`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 61% in 2025 flocks; 42% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed keel bone fracture records only. It did not assess the housing system or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E_scope / worsened  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audited records show the indicator rose between the two years, so the stated fall did not occur. |
| Q_welfare | NE | F/NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

### attribution context  `sha256:ef7ca10a7b47aa9e`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 42% in 2025 flocks; 61% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed keel bone fracture records only. It did not assess the housing system or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

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

### belief context  `sha256:59caa88870310a72`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 42% in 2025 flocks; 61% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed keel bone fracture records only. It did not assess the housing system or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E_scope / unchanged  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audited records show the indicator unchanged between the two years, so the stated fall did not occur. |
| Q_welfare | NE | F/NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

### attribution context  `sha256:3b375edcf4b45f12`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 61% in 2025 flocks; 61% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed keel bone fracture records only. It did not assess the housing system or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

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

### belief context  `sha256:cf3da58b3fd66201`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Item checked: Keel bone fractures at end of lay, 2025 and 2026 flocks
Method: Review of end-of-lay palpation records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with palpable keel bone fractures at end of lay: 61% in 2025 flocks; 61% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed keel bone fracture records only. It did not assess the housing system or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
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

### attribution context  `sha256:2233146eb6e59d8f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Status: Verified ✓

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.

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

### belief context  `sha256:ff9fd5fe875fcd7f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Redmire Eggs. Animals: laying hens.
The supplier states:
[P] All laying hens at Redmire Eggs are housed in cage-free aviary systems.
[Q_obs] The share of hens with keel bone fractures at end of lay at Redmire Eggs fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Redmire Eggs improved between 2025 and 2026.
[Q_cause] This fall in keel bone fractures was caused by the cage-free aviary housing.
[R] Redmire Eggs passed its 2026 fuel-storage safety inspection.
[S] Redmire Fell Site, a sister site, also houses all hens in cage-free aviary systems.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0926-33
Site: Redmire Eggs
Date: 20 April 2026
Status: Verified ✓

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All laying hens at Redmire Eggs are housed in cage-free aviary systems." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in keel bone fractures between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about keel bone fractures.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to keel bone fractures at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~
