# Rendered stimuli: `dev-sheep-lameness` (expansion batch ba)

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

### attribution context  `sha256:fd97717fa2a9a746`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Glenmorvan Farm. Animals: sheep (breeding ewes).
The supplier states:
[P] Throughout 2025, every ewe at Glenmorvan Farm recorded as lame at a weekly flock check was treated within 3 days of that check.
[Q_obs] The recorded share of ewes at Glenmorvan Farm scored lame was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the ewes at Glenmorvan Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by the prompt treatment of lame ewes.
[R] Glenmorvan Farm passed its 2026 private water supply inspection.
[S] Throughout 2025, every ewe at Glenmorvan Hill, a sister site, recorded as lame at a weekly flock check was also treated within 3 days of that check.

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

### belief context  `sha256:330aadfd7a062750`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Glenmorvan Farm. Animals: sheep (breeding ewes).
The supplier states:
[P] Throughout 2025, every ewe at Glenmorvan Farm recorded as lame at a weekly flock check was treated within 3 days of that check.
[Q_obs] The recorded share of ewes at Glenmorvan Farm scored lame was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the ewes at Glenmorvan Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by the prompt treatment of lame ewes.
[R] Glenmorvan Farm passed its 2026 private water supply inspection.
[S] Throughout 2025, every ewe at Glenmorvan Hill, a sister site, recorded as lame at a weekly flock check was also treated within 3 days of that check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every ewe at Glenmorvan Farm recorded as lame at a weekly flock check was treated within 3 days of that check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of ewes scored lame between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of ewes scored lame.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of ewes scored lame at this facility.
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

### attribution context  `sha256:2d3c4c60a0dfadf2`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Glenmorvan Farm. Animals: sheep (breeding ewes).
The supplier states:
[Q_obs] The recorded share of ewes at Glenmorvan Farm scored lame was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the ewes at Glenmorvan Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by the prompt treatment of lame ewes.
[R] Glenmorvan Farm passed its 2026 private water supply inspection.
[S] Throughout 2025, every ewe at Glenmorvan Hill, a sister site, recorded as lame at a weekly flock check was also treated within 3 days of that check.

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

### belief context  `sha256:d1bc45901d4e02ed`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Glenmorvan Farm. Animals: sheep (breeding ewes).
The supplier states:
[Q_obs] The recorded share of ewes at Glenmorvan Farm scored lame was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the ewes at Glenmorvan Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness was caused by the prompt treatment of lame ewes.
[R] Glenmorvan Farm passed its 2026 private water supply inspection.
[S] Throughout 2025, every ewe at Glenmorvan Hill, a sister site, recorded as lame at a weekly flock check was also treated within 3 days of that check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every ewe at Glenmorvan Farm recorded as lame at a weekly flock check was treated within 3 days of that check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of ewes scored lame between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of ewes scored lame.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of ewes scored lame at this facility.
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

Hashes: attribution `sha256:bc4ebb270c50a4fd`; belief `sha256:7e60f5879117c485`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Item checked: Treatment of every ewe recorded as lame at any weekly flock check during 2025
Method: Review of the 52 weekly flock-check sheets for 2025, the 2025 lameness treatment log and the medicine book, matched ewe by ewe on ear-tag number
Finding: Every ewe recorded as lame at a weekly flock check during 2025 had a logged treatment within 3 days of that check; the longest recorded interval was 2 days, and treatments matched medicine-book entries.
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

Hashes: attribution `sha256:02478bf559aae01d`; belief `sha256:17c46e8734fa1c12`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Item checked: Treatment of every ewe recorded as lame at any weekly flock check during 2025
Method: Review of the 52 weekly flock-check sheets for 2025, the 2025 lameness treatment log and the medicine book, matched ewe by ewe on ear-tag number
Finding: Every ewe recorded as lame at a weekly flock check during 2025 had a logged treatment within 3 days of that check; the longest recorded interval was 2 days, and treatments matched medicine-book entries.
Status: Confirmed

Coverage: This audit assessed treatment of lame ewes only. It did not assess locomotion score records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:b34db43a1f708fea`; belief `sha256:04fe909f98b5adf8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Item checked: Treatment of every ewe recorded as lame at any weekly flock check during 2025
Method: Review of the 52 weekly flock-check sheets for 2025, the 2025 lameness treatment log and the medicine book, matched ewe by ewe on ear-tag number
Finding: Every ewe recorded as lame at a weekly flock check during 2025 had a logged treatment within 3 days of that check; the longest recorded interval was 2 days, and treatments matched medicine-book entries.
Status: Confirmed

Coverage:
  Assessed: treatment of lame ewes
  Not assessed: locomotion score records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:287a00de8f6d06a3`; belief `sha256:027e538230e42c02`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Item checked: The private borehole water supply serving the farmhouse and steading
Method: On-site sampling at the borehole and at two outlets, and review of the laboratory results
Finding: The private water supply met the applicable regulatory requirements.
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

Hashes: attribution `sha256:6304217ef4a84003`; belief `sha256:c80bca667fc3153f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Hill
Date: 11 March 2026
Item checked: Treatment of every ewe recorded as lame at any weekly flock check during 2025
Method: Review of the 52 weekly flock-check sheets for 2025, the 2025 lameness treatment log and the medicine book, matched ewe by ewe on ear-tag number
Finding: Every ewe recorded as lame at a weekly flock check at Glenmorvan Hill during 2025 had a logged treatment within 3 days of that check; the longest recorded interval was 3 days, and treatments matched medicine-book entries.
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

Hashes: attribution `sha256:af237d462b70a910`; belief `sha256:ba5f212193dccffa`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Item checked: Locomotion score records for the breeding flock in 2024 and 2025
Method: Review of the reports from four visits per year by a contracted locomotion scorer, each scoring every ewe gathered on the day, checked against the flock register and the gathering records
Finding: Recorded share of scored ewes lame (locomotion score 2 or 3), mean of the four visits: 8.5% in 2024; 3.8% in 2025. Records were complete and matched the flock register for both years.
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

Hashes: attribution `sha256:07ed3a25bec42d6c`; belief `sha256:8c6c204e6e07835b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Item checked: Locomotion score records for the breeding flock in 2024 and 2025
Method: Review of the reports from four visits per year by a contracted locomotion scorer, each scoring every ewe gathered on the day, checked against the flock register and the gathering records
Finding: Recorded share of scored ewes lame (locomotion score 2 or 3), mean of the four visits: 3.8% in 2024; 8.5% in 2025. Records were complete and matched the flock register for both years.
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

Hashes: attribution `sha256:18309f2250777ea5`; belief `sha256:ef571d0280ed0b8a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Item checked: Locomotion score records for the breeding flock in 2024 and 2025
Method: Review of the reports from four visits per year by a contracted locomotion scorer, each scoring every ewe gathered on the day, checked against the flock register and the gathering records
Finding: Recorded share of scored ewes lame (locomotion score 2 or 3), mean of the four visits: 8.5% in 2024; 8.5% in 2025. Records were complete and matched the flock register for both years.
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

Hashes: attribution `sha256:9076fc4820dbf37f`; belief `sha256:a4e0c3dd442f556a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Item checked: Locomotion score records for the breeding flock in 2024 and 2025
Method: Review of the reports from four visits per year by a contracted locomotion scorer, each scoring every ewe gathered on the day, checked against the flock register and the gathering records
Finding: Recorded share of scored ewes lame (locomotion score 2 or 3), mean of the four visits: 8.5% in 2024; 3.8% in 2025. Records were complete and matched the flock register for both years.
Status: Confirmed

Coverage: This audit assessed locomotion score records only. It did not assess treatment of lame ewes or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:495b1d728868e34a`; belief `sha256:35a4af060f55d2b8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Item checked: Locomotion score records for the breeding flock in 2024 and 2025
Method: Review of the reports from four visits per year by a contracted locomotion scorer, each scoring every ewe gathered on the day, checked against the flock register and the gathering records
Finding: Recorded share of scored ewes lame (locomotion score 2 or 3), mean of the four visits: 3.8% in 2024; 8.5% in 2025. Records were complete and matched the flock register for both years.
Status: Confirmed

Coverage: This audit assessed locomotion score records only. It did not assess treatment of lame ewes or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:e06bedfbb8db6026`; belief `sha256:b8cbf323741ae95d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Item checked: Locomotion score records for the breeding flock in 2024 and 2025
Method: Review of the reports from four visits per year by a contracted locomotion scorer, each scoring every ewe gathered on the day, checked against the flock register and the gathering records
Finding: Recorded share of scored ewes lame (locomotion score 2 or 3), mean of the four visits: 8.5% in 2024; 8.5% in 2025. Records were complete and matched the flock register for both years.
Status: Confirmed

Coverage: This audit assessed locomotion score records only. It did not assess treatment of lame ewes or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:b5db1724318b2e19`; belief `sha256:65caf3de8eb33ed6`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Tweedsmuir Livestock Assurance Ltd.
Audit reference: TLA-26-0233
Site: Glenmorvan Farm
Date: 11 March 2026
Status: Verified ✓
~~~~
