# Rendered stimuli: `dev-duck-water` (extension set)

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

### attribution context  `sha256:8a79a93f388b18bc`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Fenmoor Duck Farm. Animals: Pekin ducks.
The supplier states:
[P] Throughout 2025, every house at Fenmoor Duck Farm holding ducks aged 14 days or older had open water troughs at least 10 cm deep at every daily check.
[Q_obs] The recorded share of ducks at Fenmoor Duck Farm with dirty or crusted eyes at 35 days of age was lower for 2025 flocks than for 2024 flocks.
[Q_welfare] The overall welfare of the ducks at Fenmoor Duck Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded eye problems was caused by the open water troughs.
[R] Fenmoor Duck Farm passed its 2026 lifting-equipment inspection.
[S] Throughout 2025, every house at Fenmoor Drove, a sister site, holding ducks aged 14 days or older also had open water troughs at least 10 cm deep at every daily check.

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

### belief context  `sha256:c15822c33ac26615`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Fenmoor Duck Farm. Animals: Pekin ducks.
The supplier states:
[P] Throughout 2025, every house at Fenmoor Duck Farm holding ducks aged 14 days or older had open water troughs at least 10 cm deep at every daily check.
[Q_obs] The recorded share of ducks at Fenmoor Duck Farm with dirty or crusted eyes at 35 days of age was lower for 2025 flocks than for 2024 flocks.
[Q_welfare] The overall welfare of the ducks at Fenmoor Duck Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded eye problems was caused by the open water troughs.
[R] Fenmoor Duck Farm passed its 2026 lifting-equipment inspection.
[S] Throughout 2025, every house at Fenmoor Drove, a sister site, holding ducks aged 14 days or older also had open water troughs at least 10 cm deep at every daily check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every house at Fenmoor Duck Farm holding ducks aged 14 days or older had open water troughs at least 10 cm deep at every daily check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of ducks with dirty or crusted eyes between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of ducks with dirty or crusted eyes.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of ducks with dirty or crusted eyes at this facility.
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

### attribution context  `sha256:178075e2e728e772`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Fenmoor Duck Farm. Animals: Pekin ducks.
The supplier states:
[Q_obs] The recorded share of ducks at Fenmoor Duck Farm with dirty or crusted eyes at 35 days of age was lower for 2025 flocks than for 2024 flocks.
[Q_welfare] The overall welfare of the ducks at Fenmoor Duck Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded eye problems was caused by the open water troughs.
[R] Fenmoor Duck Farm passed its 2026 lifting-equipment inspection.
[S] Throughout 2025, every house at Fenmoor Drove, a sister site, holding ducks aged 14 days or older also had open water troughs at least 10 cm deep at every daily check.

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

### belief context  `sha256:df11e8668aec07e0`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Fenmoor Duck Farm. Animals: Pekin ducks.
The supplier states:
[Q_obs] The recorded share of ducks at Fenmoor Duck Farm with dirty or crusted eyes at 35 days of age was lower for 2025 flocks than for 2024 flocks.
[Q_welfare] The overall welfare of the ducks at Fenmoor Duck Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded eye problems was caused by the open water troughs.
[R] Fenmoor Duck Farm passed its 2026 lifting-equipment inspection.
[S] Throughout 2025, every house at Fenmoor Drove, a sister site, holding ducks aged 14 days or older also had open water troughs at least 10 cm deep at every daily check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every house at Fenmoor Duck Farm holding ducks aged 14 days or older had open water troughs at least 10 cm deep at every daily check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of ducks with dirty or crusted eyes between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of ducks with dirty or crusted eyes.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of ducks with dirty or crusted eyes at this facility.
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

Hashes: attribution `sha256:a4fd06759d7acda0`; belief `sha256:0b80d51231d63e74`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Item checked: Open water troughs in every house holding ducks aged 14 days or older during 2025
Method: Review of 2025 trough installation records, daily stockperson check sheets recording trough water depth, and flock placement records for every house
Finding: Daily check sheets for 2025 were complete and recorded open water troughs at least 10 cm deep in every house holding ducks aged 14 days or older, at every check.
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

Hashes: attribution `sha256:8f8b9ac5178da405`; belief `sha256:ec9e7a8bf17f1113`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Item checked: Open water troughs in every house holding ducks aged 14 days or older during 2025
Method: Review of 2025 trough installation records, daily stockperson check sheets recording trough water depth, and flock placement records for every house
Finding: Daily check sheets for 2025 were complete and recorded open water troughs at least 10 cm deep in every house holding ducks aged 14 days or older, at every check.
Status: Confirmed

Coverage: This audit assessed open water troughs only. It did not assess eye condition records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:40268a3a54758ba1`; belief `sha256:9adfc9d4531189f0`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Item checked: Open water troughs in every house holding ducks aged 14 days or older during 2025
Method: Review of 2025 trough installation records, daily stockperson check sheets recording trough water depth, and flock placement records for every house
Finding: Daily check sheets for 2025 were complete and recorded open water troughs at least 10 cm deep in every house holding ducks aged 14 days or older, at every check.
Status: Confirmed

Coverage:
  Assessed: open water troughs
  Not assessed: eye condition records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:0ee32cb6b546bb45`; belief `sha256:5a755fa9727a1a9e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Item checked: Lifting equipment: the forklift, telehandler and feed-bin hoist
Method: On-site thorough examination of chains, hydraulics, brakes and load-rating plates
Finding: All lifting equipment examined met the applicable regulatory requirements.
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

Hashes: attribution `sha256:e37d5a2c0a242665`; belief `sha256:5d5afc3377975ad3`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Drove
Date: 2 June 2026
Item checked: Open water troughs in every house holding ducks aged 14 days or older during 2025
Method: Review of 2025 trough installation records, daily stockperson check sheets recording trough water depth, and flock placement records for every house
Finding: Daily check sheets at Fenmoor Drove for 2025 were complete and recorded open water troughs at least 10 cm deep in every house holding ducks aged 14 days or older, at every check.
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

Hashes: attribution `sha256:66ad9f71f24f73ee`; belief `sha256:f160999f1709d129`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Item checked: Eye condition scores at 35 days of age for all flocks placed in 2024 and 2025
Method: Review of eye and nostril scoring sheets (60 ducks scored per house per flock) for every flock in both years, checked against the farm's flock summary sheets
Finding: Recorded share of scored ducks with dirty or crusted eyes (score 2 or 3): 17% for 2024 flocks; 6% for 2025 flocks. Records were complete and matched the flock summary sheets for both years.
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

Hashes: attribution `sha256:b43d4e9f4a77ef5b`; belief `sha256:cdef49b6ae01ef2d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Item checked: Eye condition scores at 35 days of age for all flocks placed in 2024 and 2025
Method: Review of eye and nostril scoring sheets (60 ducks scored per house per flock) for every flock in both years, checked against the farm's flock summary sheets
Finding: Recorded share of scored ducks with dirty or crusted eyes (score 2 or 3): 6% for 2024 flocks; 17% for 2025 flocks. Records were complete and matched the flock summary sheets for both years.
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

Hashes: attribution `sha256:afc32177f04d2ec9`; belief `sha256:1b948ad61ce399c1`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Item checked: Eye condition scores at 35 days of age for all flocks placed in 2024 and 2025
Method: Review of eye and nostril scoring sheets (60 ducks scored per house per flock) for every flock in both years, checked against the farm's flock summary sheets
Finding: Recorded share of scored ducks with dirty or crusted eyes (score 2 or 3): 17% for 2024 flocks; 17% for 2025 flocks. Records were complete and matched the flock summary sheets for both years.
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

Hashes: attribution `sha256:ca6a12142c1dfd45`; belief `sha256:225937c50e45f694`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Item checked: Eye condition scores at 35 days of age for all flocks placed in 2024 and 2025
Method: Review of eye and nostril scoring sheets (60 ducks scored per house per flock) for every flock in both years, checked against the farm's flock summary sheets
Finding: Recorded share of scored ducks with dirty or crusted eyes (score 2 or 3): 17% for 2024 flocks; 6% for 2025 flocks. Records were complete and matched the flock summary sheets for both years.
Status: Confirmed

Coverage: This audit assessed eye condition records only. It did not assess open water troughs or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:e2258d6b2c4b0661`; belief `sha256:13e2f0253d30093e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Item checked: Eye condition scores at 35 days of age for all flocks placed in 2024 and 2025
Method: Review of eye and nostril scoring sheets (60 ducks scored per house per flock) for every flock in both years, checked against the farm's flock summary sheets
Finding: Recorded share of scored ducks with dirty or crusted eyes (score 2 or 3): 6% for 2024 flocks; 17% for 2025 flocks. Records were complete and matched the flock summary sheets for both years.
Status: Confirmed

Coverage: This audit assessed eye condition records only. It did not assess open water troughs or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:ab93558f831945ab`; belief `sha256:b0c8b6fb68a894ef`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Item checked: Eye condition scores at 35 days of age for all flocks placed in 2024 and 2025
Method: Review of eye and nostril scoring sheets (60 ducks scored per house per flock) for every flock in both years, checked against the farm's flock summary sheets
Finding: Recorded share of scored ducks with dirty or crusted eyes (score 2 or 3): 17% for 2024 flocks; 17% for 2025 flocks. Records were complete and matched the flock summary sheets for both years.
Status: Confirmed

Coverage: This audit assessed eye condition records only. It did not assess open water troughs or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:0ecc63a544d0fa5f`; belief `sha256:b7f5e6bf14eaa312`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Anglian Livestock Audit Cooperative
Audit reference: ALAC 2026-114
Site: Fenmoor Duck Farm
Date: 2 June 2026
Status: Verified ✓
~~~~
