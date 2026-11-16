# Rendered stimuli: `dev-dairy-cubicle` (extension set)

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

### attribution context  `sha256:bf3ee1ee23bc36a1`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Penhallow Dairy. Animals: dairy cows.
The supplier states:
[P] Throughout 2025, no housed group of lactating cows at Penhallow Dairy contained more cows than it had usable cubicles in any weekly group list.
[Q_obs] The recorded share of lame cows at Penhallow Dairy was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the cows at Penhallow Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by giving every cow a cubicle.
[R] Penhallow Dairy passed its 2026 pressure-system inspection.
[S] Throughout 2025, no housed group of lactating cows at Penhallow Moor, a sister site, contained more cows than it had usable cubicles in any weekly group list either.

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

### belief context  `sha256:e427cb2230ccc2e3`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Penhallow Dairy. Animals: dairy cows.
The supplier states:
[P] Throughout 2025, no housed group of lactating cows at Penhallow Dairy contained more cows than it had usable cubicles in any weekly group list.
[Q_obs] The recorded share of lame cows at Penhallow Dairy was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the cows at Penhallow Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by giving every cow a cubicle.
[R] Penhallow Dairy passed its 2026 pressure-system inspection.
[S] Throughout 2025, no housed group of lactating cows at Penhallow Moor, a sister site, contained more cows than it had usable cubicles in any weekly group list either.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, no housed group of lactating cows at Penhallow Dairy contained more cows than it had usable cubicles in any weekly group list." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of lame cows between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of lame cows.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of lame cows at this facility.
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

### attribution context  `sha256:cc5c22a86a6ee2e2`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Penhallow Dairy. Animals: dairy cows.
The supplier states:
[Q_obs] The recorded share of lame cows at Penhallow Dairy was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the cows at Penhallow Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by giving every cow a cubicle.
[R] Penhallow Dairy passed its 2026 pressure-system inspection.
[S] Throughout 2025, no housed group of lactating cows at Penhallow Moor, a sister site, contained more cows than it had usable cubicles in any weekly group list either.

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

### belief context  `sha256:4bb2f6205023b854`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Penhallow Dairy. Animals: dairy cows.
The supplier states:
[Q_obs] The recorded share of lame cows at Penhallow Dairy was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the cows at Penhallow Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by giving every cow a cubicle.
[R] Penhallow Dairy passed its 2026 pressure-system inspection.
[S] Throughout 2025, no housed group of lactating cows at Penhallow Moor, a sister site, contained more cows than it had usable cubicles in any weekly group list either.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, no housed group of lactating cows at Penhallow Dairy contained more cows than it had usable cubicles in any weekly group list." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of lame cows between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of lame cows.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of lame cows at this facility.
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

Hashes: attribution `sha256:737c15dc45808b9a`; belief `sha256:f759a46cac4ed348`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Item checked: Cow numbers and usable cubicles in every housed lactating group in every weekly group list for 2025
Method: Review of the 52 weekly group lists exported from the 2025 parlour software, compared with cubicle counts from the shed plans and the 2025 cubicle repair log
Finding: In every weekly group list for 2025, each housed lactating group had no more cows than usable cubicles; the highest ratio in any group was 0.96 cows per cubicle.
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

Hashes: attribution `sha256:38e2cdf875c3976e`; belief `sha256:99300f3b56d62f96`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Item checked: Cow numbers and usable cubicles in every housed lactating group in every weekly group list for 2025
Method: Review of the 52 weekly group lists exported from the 2025 parlour software, compared with cubicle counts from the shed plans and the 2025 cubicle repair log
Finding: In every weekly group list for 2025, each housed lactating group had no more cows than usable cubicles; the highest ratio in any group was 0.96 cows per cubicle.
Status: Confirmed

Coverage: This audit assessed cow numbers per cubicle only. It did not assess mobility score records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:fce13ba3556af2f8`; belief `sha256:bbf36a5b870a2002`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Item checked: Cow numbers and usable cubicles in every housed lactating group in every weekly group list for 2025
Method: Review of the 52 weekly group lists exported from the 2025 parlour software, compared with cubicle counts from the shed plans and the 2025 cubicle repair log
Finding: In every weekly group list for 2025, each housed lactating group had no more cows than usable cubicles; the highest ratio in any group was 0.96 cows per cubicle.
Status: Confirmed

Coverage:
  Assessed: cow numbers per cubicle
  Not assessed: mobility score records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:00ebe007eb251cfb`; belief `sha256:355b0c5c0fc961f7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Item checked: The milking-plant vacuum system, air compressor and hot-water boiler
Method: On-site examination of pressure vessels and relief valves, and review of the written scheme of examination
Finding: All pressure systems examined met the applicable regulatory requirements.
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

Hashes: attribution `sha256:57f30acfa727ef27`; belief `sha256:31c9af6aa4f3aa99`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Moor
Date: 24 February 2026
Item checked: Cow numbers and usable cubicles in every housed lactating group in every weekly group list for 2025
Method: Review of the 52 weekly group lists exported from the 2025 parlour software, compared with cubicle counts from the shed plans and the 2025 cubicle repair log
Finding: In every weekly group list for 2025, each housed lactating group at Penhallow Moor had no more cows than usable cubicles; the highest ratio in any group was 0.98 cows per cubicle.
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

Hashes: attribution `sha256:b5d01201de1e7767`; belief `sha256:3289243e4c8c4ba5`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Item checked: Mobility score records for all lactating cows in 2024 and 2025
Method: Review of the contracted mobility scorer's reports from six scoring sessions per year, each covering every cow in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored cows lame (mobility score 2 or 3), mean of the six sessions: 32% in 2024; 21% in 2025. Records were complete and matched the herd lists for both years.
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

Hashes: attribution `sha256:89776f216eaa2231`; belief `sha256:5c79d0a188b73dbc`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Item checked: Mobility score records for all lactating cows in 2024 and 2025
Method: Review of the contracted mobility scorer's reports from six scoring sessions per year, each covering every cow in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored cows lame (mobility score 2 or 3), mean of the six sessions: 21% in 2024; 32% in 2025. Records were complete and matched the herd lists for both years.
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

Hashes: attribution `sha256:2bb7923cedfa482a`; belief `sha256:9672c9d4164ae711`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Item checked: Mobility score records for all lactating cows in 2024 and 2025
Method: Review of the contracted mobility scorer's reports from six scoring sessions per year, each covering every cow in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored cows lame (mobility score 2 or 3), mean of the six sessions: 32% in 2024; 32% in 2025. Records were complete and matched the herd lists for both years.
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

Hashes: attribution `sha256:50ea60be56649a30`; belief `sha256:a6daacd75a44cf02`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Item checked: Mobility score records for all lactating cows in 2024 and 2025
Method: Review of the contracted mobility scorer's reports from six scoring sessions per year, each covering every cow in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored cows lame (mobility score 2 or 3), mean of the six sessions: 32% in 2024; 21% in 2025. Records were complete and matched the herd lists for both years.
Status: Confirmed

Coverage: This audit assessed mobility score records only. It did not assess cow numbers per cubicle or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:f156527295209368`; belief `sha256:bc0caccb2ad589da`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Item checked: Mobility score records for all lactating cows in 2024 and 2025
Method: Review of the contracted mobility scorer's reports from six scoring sessions per year, each covering every cow in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored cows lame (mobility score 2 or 3), mean of the six sessions: 21% in 2024; 32% in 2025. Records were complete and matched the herd lists for both years.
Status: Confirmed

Coverage: This audit assessed mobility score records only. It did not assess cow numbers per cubicle or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:791409e80c4e328c`; belief `sha256:9deb9577c5a12874`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Item checked: Mobility score records for all lactating cows in 2024 and 2025
Method: Review of the contracted mobility scorer's reports from six scoring sessions per year, each covering every cow in milk on the day, checked against the milk-recording herd lists
Finding: Recorded share of scored cows lame (mobility score 2 or 3), mean of the six sessions: 32% in 2024; 32% in 2025. Records were complete and matched the herd lists for both years.
Status: Confirmed

Coverage: This audit assessed mobility score records only. It did not assess cow numbers per cubicle or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:4f0b72dc13623c38`; belief `sha256:67963c2a432baf9a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Fernleigh Dairy Standards Board
Audit reference: FDSB/26/0317
Site: Penhallow Dairy
Date: 24 February 2026
Status: Verified ✓
~~~~
