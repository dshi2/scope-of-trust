# Rendered stimuli: `dev-turkey-darkness` (extension set)

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

### attribution context  `sha256:a3fa6b95d3d2d917`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Gorsey Bank Turkeys. Animals: turkeys.
The supplier states:
[P] Throughout 2025, every turkey house at Gorsey Bank Turkeys gave birds older than 7 days at least 6 hours of continuous darkness in every 24 hours.
[Q_obs] The recorded share of birds at Gorsey Bank Turkeys culled for leg disorders was lower for flocks depopulated in 2025 than for flocks depopulated in 2024.
[Q_welfare] The overall welfare of the turkeys at Gorsey Bank Turkeys improved from 2024 to 2025.
[Q_cause] This reduction in recorded leg-disorder culls was caused by the longer dark period.
[R] Gorsey Bank Turkeys passed its 2026 LPG installation safety inspection.
[S] Throughout 2025, every turkey house at Gorsey Bank Top, a sister site, also gave birds older than 7 days at least 6 hours of continuous darkness in every 24 hours.

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

### belief context  `sha256:7133503ea6d92388`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Gorsey Bank Turkeys. Animals: turkeys.
The supplier states:
[P] Throughout 2025, every turkey house at Gorsey Bank Turkeys gave birds older than 7 days at least 6 hours of continuous darkness in every 24 hours.
[Q_obs] The recorded share of birds at Gorsey Bank Turkeys culled for leg disorders was lower for flocks depopulated in 2025 than for flocks depopulated in 2024.
[Q_welfare] The overall welfare of the turkeys at Gorsey Bank Turkeys improved from 2024 to 2025.
[Q_cause] This reduction in recorded leg-disorder culls was caused by the longer dark period.
[R] Gorsey Bank Turkeys passed its 2026 LPG installation safety inspection.
[S] Throughout 2025, every turkey house at Gorsey Bank Top, a sister site, also gave birds older than 7 days at least 6 hours of continuous darkness in every 24 hours.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every turkey house at Gorsey Bank Turkeys gave birds older than 7 days at least 6 hours of continuous darkness in every 24 hours." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds culled for leg disorders between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds culled for leg disorders.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds culled for leg disorders at this facility.
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

### attribution context  `sha256:da70536dce4ba3ed`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Gorsey Bank Turkeys. Animals: turkeys.
The supplier states:
[Q_obs] The recorded share of birds at Gorsey Bank Turkeys culled for leg disorders was lower for flocks depopulated in 2025 than for flocks depopulated in 2024.
[Q_welfare] The overall welfare of the turkeys at Gorsey Bank Turkeys improved from 2024 to 2025.
[Q_cause] This reduction in recorded leg-disorder culls was caused by the longer dark period.
[R] Gorsey Bank Turkeys passed its 2026 LPG installation safety inspection.
[S] Throughout 2025, every turkey house at Gorsey Bank Top, a sister site, also gave birds older than 7 days at least 6 hours of continuous darkness in every 24 hours.

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

### belief context  `sha256:401f5942bbf01a43`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Gorsey Bank Turkeys. Animals: turkeys.
The supplier states:
[Q_obs] The recorded share of birds at Gorsey Bank Turkeys culled for leg disorders was lower for flocks depopulated in 2025 than for flocks depopulated in 2024.
[Q_welfare] The overall welfare of the turkeys at Gorsey Bank Turkeys improved from 2024 to 2025.
[Q_cause] This reduction in recorded leg-disorder culls was caused by the longer dark period.
[R] Gorsey Bank Turkeys passed its 2026 LPG installation safety inspection.
[S] Throughout 2025, every turkey house at Gorsey Bank Top, a sister site, also gave birds older than 7 days at least 6 hours of continuous darkness in every 24 hours.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every turkey house at Gorsey Bank Turkeys gave birds older than 7 days at least 6 hours of continuous darkness in every 24 hours." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of birds culled for leg disorders between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of birds culled for leg disorders.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of birds culled for leg disorders at this facility.
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

Hashes: attribution `sha256:d4038db401b3e4cb`; belief `sha256:9aef7f6f9bc7f0f4`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Item checked: Lighting programme in every house on every day of 2025 on which birds older than 7 days were present
Method: Review of lighting-controller logs downloaded from every house for the whole of 2025, checked against flock placement and depopulation dates
Finding: Controller logs for every house showed at least 6 hours of continuous darkness in every 24-hour period of 2025 on which birds older than 7 days were present.
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

Hashes: attribution `sha256:8fdfce0e1ff4329a`; belief `sha256:7bf99c218de08e37`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Item checked: Lighting programme in every house on every day of 2025 on which birds older than 7 days were present
Method: Review of lighting-controller logs downloaded from every house for the whole of 2025, checked against flock placement and depopulation dates
Finding: Controller logs for every house showed at least 6 hours of continuous darkness in every 24-hour period of 2025 on which birds older than 7 days were present.
Status: Confirmed

Coverage: This audit assessed lighting programmes only. It did not assess leg-disorder cull records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:cf800d69624e2561`; belief `sha256:3f7c48a8d302736f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Item checked: Lighting programme in every house on every day of 2025 on which birds older than 7 days were present
Method: Review of lighting-controller logs downloaded from every house for the whole of 2025, checked against flock placement and depopulation dates
Finding: Controller logs for every house showed at least 6 hours of continuous darkness in every 24-hour period of 2025 on which birds older than 7 days were present.
Status: Confirmed

Coverage:
  Assessed: lighting programmes
  Not assessed: leg-disorder cull records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:99ac529297f8e224`; belief `sha256:1e944b463a5f7fb7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Item checked: LPG tanks, pipework and gas brooders in all five houses
Method: On-site inspection of tanks, pipework, regulators and gas-detection alarms
Finding: All LPG installations inspected met the applicable regulatory requirements.
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

Hashes: attribution `sha256:8c0ec251365ec854`; belief `sha256:82b33c49525d33fb`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Top
Date: 18 May 2026
Item checked: Lighting programme in every house on every day of 2025 on which birds older than 7 days were present
Method: Review of lighting-controller logs downloaded from every house for the whole of 2025, checked against flock placement and depopulation dates
Finding: Controller logs for every house at Gorsey Bank Top showed at least 6 hours of continuous darkness in every 24-hour period of 2025 on which birds older than 7 days were present.
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

Hashes: attribution `sha256:75f52bb3c97aacf3`; belief `sha256:838169dc60d75993`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Item checked: Cull records for all flocks depopulated in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded cull reason, for every flock in both years, checked against placement numbers and processing-plant intake records
Finding: Recorded share of placed birds culled for leg disorders: 3.8% for flocks depopulated in 2024; 2.1% for flocks depopulated in 2025. Records were complete and matched placement and intake records for both years.
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

Hashes: attribution `sha256:28b433114a9ec37f`; belief `sha256:c51e81ddee8e861c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Item checked: Cull records for all flocks depopulated in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded cull reason, for every flock in both years, checked against placement numbers and processing-plant intake records
Finding: Recorded share of placed birds culled for leg disorders: 2.1% for flocks depopulated in 2024; 3.8% for flocks depopulated in 2025. Records were complete and matched placement and intake records for both years.
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

Hashes: attribution `sha256:a952ec195c85b562`; belief `sha256:e41d18216510a290`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Item checked: Cull records for all flocks depopulated in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded cull reason, for every flock in both years, checked against placement numbers and processing-plant intake records
Finding: Recorded share of placed birds culled for leg disorders: 3.8% for flocks depopulated in 2024; 3.8% for flocks depopulated in 2025. Records were complete and matched placement and intake records for both years.
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

Hashes: attribution `sha256:eaa502d3e979ad4f`; belief `sha256:888830a27a837eb3`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Item checked: Cull records for all flocks depopulated in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded cull reason, for every flock in both years, checked against placement numbers and processing-plant intake records
Finding: Recorded share of placed birds culled for leg disorders: 3.8% for flocks depopulated in 2024; 2.1% for flocks depopulated in 2025. Records were complete and matched placement and intake records for both years.
Status: Confirmed

Coverage: This audit assessed leg-disorder cull records only. It did not assess lighting programmes or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:5f9e473461a98a04`; belief `sha256:c12f78df9e0e4cb4`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Item checked: Cull records for all flocks depopulated in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded cull reason, for every flock in both years, checked against placement numbers and processing-plant intake records
Finding: Recorded share of placed birds culled for leg disorders: 2.1% for flocks depopulated in 2024; 3.8% for flocks depopulated in 2025. Records were complete and matched placement and intake records for both years.
Status: Confirmed

Coverage: This audit assessed leg-disorder cull records only. It did not assess lighting programmes or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:3edd7e1474ad2b9f`; belief `sha256:d0fe213aaf803ddb`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Item checked: Cull records for all flocks depopulated in 2024 and 2025
Method: Review of daily mortality and cull sheets, with the recorded cull reason, for every flock in both years, checked against placement numbers and processing-plant intake records
Finding: Recorded share of placed birds culled for leg disorders: 3.8% for flocks depopulated in 2024; 3.8% for flocks depopulated in 2025. Records were complete and matched placement and intake records for both years.
Status: Confirmed

Coverage: This audit assessed leg-disorder cull records only. It did not assess lighting programmes or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:260057ec1a77450a`; belief `sha256:9a84bf761cc0daa8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Calloway & Reid Farm Audit LLP
Audit reference: CR/TK/2026/22
Site: Gorsey Bank Turkeys
Date: 18 May 2026
Status: Verified ✓
~~~~
