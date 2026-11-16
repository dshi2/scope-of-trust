# P2 pilot analysis

**DIAGNOSTIC PILOT on development cases (one author, one template family). Interval method provisional; P4 margin unapproved; not confirmatory evidence.**

## deepseek-v3.2

Calls 1120, spend $1.0440. Status {'ok': 1120}. Parse {'ok': 1119, 'malformed': 1}. Truncated 0. Served provider {'AtlasCloud': 1120}; served model {'deepseek/deepseek-v3.2': 1120}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.402, +0.402] | no decision (margin not fixed); one-sided 97.5% LB -0.402 | +0.000 to +0.000 | 8 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |
| P2 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |
| P3 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 40 | 0.000 | 40 |
| A0/none | 0.000 | 40 | 0.000 | 40 |
| B/none | 0.000 | 40 | 0.005 | 40 |
| C/none | 0.000 | 40 | 0.000 | 40 |
| C_prime/none | 0.000 | 40 | 0.000 | 40 |
| D1/none | 0.000 | 40 | 0.000 | 40 |
| D2/none | 0.000 | 40 | 0.000 | 40 |
| E/improved | 0.000 | 40 | 0.079 | 40 |
| E/unchanged | 0.000 | 40 | 0.016 | 40 |
| E/worsened | 0.000 | 40 | 0.033 | 40 |
| E_scope/improved | 0.000 | 40 | 0.044 | 40 |
| E_scope/unchanged | 0.000 | 40 | 0.000 | 40 |
| E_scope/worsened | 0.000 | 40 | 0.016 | 40 |
| V/none | 0.000 | 39 | nan | 0 |

## gpt-oss-120b

Calls 1120, spend $0.1557. Status {'ok': 1120}. Parse {'ok': 1120}. Truncated 0. Served provider {'DeepInfra': 1120}; served model {'openai/gpt-oss-120b': 1120}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.402, +0.402] | no decision (margin not fixed); one-sided 97.5% LB -0.402 | +0.000 to +0.000 | 8 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |
| P2 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |
| P3 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 40 | 0.000 | 40 |
| A0/none | 0.000 | 40 | 0.000 | 40 |
| B/none | 0.000 | 40 | 0.012 | 40 |
| C/none | 0.000 | 40 | 0.010 | 40 |
| C_prime/none | 0.000 | 40 | 0.000 | 40 |
| D1/none | 0.000 | 40 | 0.000 | 40 |
| D2/none | 0.000 | 40 | 0.000 | 40 |
| E/improved | 0.000 | 40 | 0.000 | 40 |
| E/unchanged | 0.000 | 40 | 0.000 | 40 |
| E/worsened | 0.000 | 40 | 0.000 | 40 |
| E_scope/improved | 0.000 | 40 | 0.000 | 40 |
| E_scope/unchanged | 0.000 | 40 | 0.000 | 40 |
| E_scope/worsened | 0.000 | 40 | 0.000 | 40 |
| V/none | 0.000 | 40 | nan | 0 |

## kimi-k2-0905

Calls 1120, spend $1.5094. Status {'ok': 1120}. Parse {'ok': 1116, 'malformed': 4}. Truncated 4. Served provider {'Novita': 1120}; served model {'moonshotai/kimi-k2-0905': 1120}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.402, +0.402] | no decision (margin not fixed); one-sided 97.5% LB -0.402 | +0.000 to +0.000 | 8 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |
| P2 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |
| P3 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 40 | 0.013 | 40 |
| A0/none | 0.000 | 40 | 0.048 | 39 |
| B/none | 0.000 | 40 | 0.036 | 40 |
| C/none | 0.000 | 40 | 0.032 | 40 |
| C_prime/none | 0.000 | 40 | 0.038 | 40 |
| D1/none | 0.000 | 40 | 0.009 | 40 |
| D2/none | 0.000 | 40 | 0.016 | 40 |
| E/improved | 0.000 | 40 | 0.055 | 40 |
| E/unchanged | 0.000 | 40 | 0.124 | 39 |
| E/worsened | 0.000 | 40 | 0.130 | 40 |
| E_scope/improved | 0.000 | 40 | 0.041 | 40 |
| E_scope/unchanged | 0.000 | 40 | 0.140 | 39 |
| E_scope/worsened | 0.000 | 40 | 0.119 | 40 |
| V/none | 0.000 | 40 | nan | 0 |

## qwen3-235b-a22b-2507

Calls 1120, spend $0.1747. Status {'ok': 1120}. Parse {'ok': 1120}. Truncated 0. Served provider {'DeepInfra': 1120}; served model {'qwen/qwen3-235b-a22b-2507': 1120}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | +0.000 to +0.000 | 8 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.402, +0.402] | no decision (margin not fixed); one-sided 97.5% LB -0.402 | +0.000 to +0.000 | 8 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |
| P2 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |
| P3 | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] | +0.000 [-0.402, +0.402] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 40 | 0.024 | 40 |
| A0/none | 0.000 | 40 | 0.132 | 40 |
| B/none | 0.000 | 40 | 0.079 | 40 |
| C/none | 0.000 | 40 | 0.082 | 40 |
| C_prime/none | 0.000 | 40 | 0.104 | 40 |
| D1/none | 0.000 | 40 | 0.041 | 40 |
| D2/none | 0.000 | 40 | 0.047 | 40 |
| E/improved | 0.000 | 40 | 0.064 | 40 |
| E/unchanged | 0.000 | 40 | 0.431 | 40 |
| E/worsened | 0.000 | 40 | 0.250 | 40 |
| E_scope/improved | 0.000 | 40 | 0.070 | 40 |
| E_scope/unchanged | 0.000 | 40 | 0.487 | 40 |
| E_scope/worsened | 0.000 | 40 | 0.244 | 40 |
| V/none | 0.400 | 40 | nan | 0 |

## deepseek-v3.2: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 39 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| A0/none | 0.500 | 0.500 [0.500, 0.500] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| B/none | 0.750 | 0.745 [0.737, 0.753] | -0.005 [-0.013, +0.003] | 0.005 [-0.003, 0.013] | 8 |
| C/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| C_prime/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D1/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D2/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E/improved | 1.000 | 0.921 [0.884, 0.959] | -0.079 [-0.116, -0.041] | 0.079 [0.041, 0.116] | 8 |
| E/worsened | 0.000 | 0.033 [0.000, 0.083] | +0.033 [-0.018, +0.083] | 0.033 [-0.018, 0.083] | 8 |
| E/unchanged | 0.000 | 0.016 [0.000, 0.055] | +0.016 [-0.022, +0.055] | 0.016 [-0.022, 0.055] | 8 |
| E_scope/improved | 1.000 | 0.956 [0.894, 1.000] | -0.044 [-0.106, +0.018] | 0.044 [-0.018, 0.106] | 8 |
| E_scope/worsened | 0.000 | 0.016 [0.000, 0.055] | +0.016 [-0.022, +0.055] | 0.016 [-0.022, 0.055] | 8 |
| E_scope/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| V/none | – | 0.650 [0.650, 0.650] (degenerate) | excluded from error (no belief gold; ledger S5) | – | 8 |

Belief shift B − A = +0.095 (normative +0.10), case t CI [+0.087, +0.103], 8 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.050 [0.000, 0.168] | 0.950 [0.832, 1.000] | 8 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.100 [0.000, 0.226] | 0.900 [0.774, 1.000] | 8 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.075 [0.000, 0.252] | 0.925 [0.748, 1.000] | 8 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.075 [0.000, 0.162] | 0.925 [0.838, 1.000] | 8 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 1 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: not estimable (no case has trials of both kinds) over 0 of 8 cases; trial table [approve, not] {'unsupported': [0, 0], 'supported_or_not_marked': [0, 479]}.

## gpt-oss-120b: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| A0/none | 0.500 | 0.500 [0.500, 0.500] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| B/none | 0.750 | 0.738 [0.708, 0.767] | -0.012 [-0.042, +0.017] | 0.012 [-0.017, 0.042] | 8 |
| C/none | 0.750 | 0.740 [0.722, 0.758] | -0.010 [-0.028, +0.008] | 0.010 [-0.008, 0.028] | 8 |
| C_prime/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D1/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D2/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E/improved | 1.000 | 1.000 [1.000, 1.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E_scope/improved | 1.000 | 1.000 [1.000, 1.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E_scope/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E_scope/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| V/none | – | 0.650 [0.650, 0.650] (degenerate) | excluded from error (no belief gold; ledger S5) | – | 8 |

Belief shift B − A = +0.087 (normative +0.10), case t CI [+0.058, +0.117], 8 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.350 [0.031, 0.669] | 0.650 [0.331, 0.969] | 8 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.425 [0.181, 0.669] | 0.575 [0.331, 0.819] | 8 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.500 [0.190, 0.810] | 0.500 [0.190, 0.810] | 8 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.725 [0.490, 0.960] | 0.275 [0.040, 0.510] | 8 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: not estimable (no case has trials of both kinds) over 0 of 8 cases; trial table [approve, not] {'unsupported': [0, 0], 'supported_or_not_marked': [0, 480]}.

## kimi-k2-0905: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.643 [0.628, 0.657] | -0.008 [-0.022, +0.007] | 0.013 [0.001, 0.024] | 8 |
| A0/none | 0.500 | 0.545 [0.515, 0.575] | +0.045 [+0.015, +0.075] | 0.048 [0.017, 0.079] | 8 |
| B/none | 0.750 | 0.724 [0.697, 0.751] | -0.026 [-0.053, +0.001] | 0.036 [0.018, 0.055] | 8 |
| C/none | 0.750 | 0.718 [0.701, 0.735] | -0.032 [-0.049, -0.015] | 0.032 [0.015, 0.049] | 8 |
| C_prime/none | 0.750 | 0.717 [0.699, 0.735] | -0.033 [-0.051, -0.015] | 0.038 [0.019, 0.057] | 8 |
| D1/none | 0.650 | 0.649 [0.642, 0.656] | -0.001 [-0.008, +0.006] | 0.009 [0.000, 0.017] | 8 |
| D2/none | 0.650 | 0.659 [0.646, 0.673] | +0.009 [-0.004, +0.023] | 0.016 [0.006, 0.025] | 8 |
| E/improved | 1.000 | 0.945 [0.886, 1.000] | -0.055 [-0.114, +0.004] | 0.055 [-0.004, 0.114] | 8 |
| E/worsened | 0.000 | 0.130 [0.072, 0.188] | +0.130 [+0.072, +0.188] | 0.130 [0.072, 0.188] | 8 |
| E/unchanged | 0.000 | 0.124 [0.080, 0.167] | +0.124 [+0.080, +0.167] | 0.124 [0.080, 0.167] | 8 |
| E_scope/improved | 1.000 | 0.959 [0.920, 0.998] | -0.041 [-0.080, -0.002] | 0.041 [0.002, 0.080] | 8 |
| E_scope/worsened | 0.000 | 0.119 [0.072, 0.165] | +0.119 [+0.072, +0.165] | 0.119 [0.072, 0.165] | 8 |
| E_scope/unchanged | 0.000 | 0.139 [0.068, 0.211] | +0.139 [+0.068, +0.211] | 0.139 [0.068, 0.211] | 8 |
| V/none | – | 0.674 [0.651, 0.698] | excluded from error (no belief gold; ledger S5) | – | 8 |

Belief shift B − A = +0.081 (normative +0.10), case t CI [+0.043, +0.119], 8 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.050 [0.000, 0.168] | 0.950 [0.832, 1.000] | 8 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.275 [0.057, 0.493] | 0.725 [0.507, 0.943] | 8 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.200 [0.000, 0.436] | 0.800 [0.564, 1.000] | 8 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.400 [0.245, 0.555] | 0.600 [0.445, 0.755] | 8 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: not estimable (no case has trials of both kinds) over 0 of 8 cases; trial table [approve, not] {'unsupported': [0, 0], 'supported_or_not_marked': [0, 480]}.

## qwen3-235b-a22b-2507: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.402, +0.402] | 1 (1) | 8 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.402, +0.402] | 1 (not in Holm) | 8 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.400 | [-0.134, +0.759] | 0.13 (not in Holm) | 8 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.400 | [-0.134, +0.759] | 0.13 (not in Holm) | 8 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.100 | [0.000, 0.336] | 8 | 40 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.626 [0.624, 0.627] | -0.024 [-0.026, -0.023] | 0.024 [0.023, 0.026] | 8 |
| A0/none | 0.500 | 0.632 [0.615, 0.649] | +0.132 [+0.115, +0.149] | 0.132 [0.115, 0.149] | 8 |
| B/none | 0.750 | 0.671 [0.625, 0.717] | -0.079 [-0.125, -0.033] | 0.079 [0.033, 0.125] | 8 |
| C/none | 0.750 | 0.667 [0.628, 0.707] | -0.083 [-0.122, -0.043] | 0.083 [0.043, 0.122] | 8 |
| C_prime/none | 0.750 | 0.646 [0.620, 0.673] | -0.104 [-0.130, -0.077] | 0.104 [0.077, 0.130] | 8 |
| D1/none | 0.650 | 0.609 [0.587, 0.632] | -0.041 [-0.063, -0.018] | 0.041 [0.018, 0.063] | 8 |
| D2/none | 0.650 | 0.618 [0.600, 0.637] | -0.032 [-0.050, -0.013] | 0.047 [0.030, 0.063] | 8 |
| E/improved | 1.000 | 0.936 [0.899, 0.972] | -0.064 [-0.101, -0.028] | 0.064 [0.028, 0.101] | 8 |
| E/worsened | 0.000 | 0.250 [0.250, 0.250] (degenerate) | +0.250 [+0.250, +0.250] (degenerate) | 0.250 [0.250, 0.250] (degenerate) | 8 |
| E/unchanged | 0.000 | 0.431 [0.361, 0.502] | +0.431 [+0.361, +0.502] | 0.431 [0.361, 0.502] | 8 |
| E_scope/improved | 1.000 | 0.930 [0.898, 0.962] | -0.070 [-0.102, -0.038] | 0.070 [0.038, 0.102] | 8 |
| E_scope/worsened | 0.000 | 0.244 [0.229, 0.259] | +0.244 [+0.229, +0.259] | 0.244 [0.229, 0.259] | 8 |
| E_scope/unchanged | 0.000 | 0.487 [0.458, 0.517] | +0.487 [+0.458, +0.517] | 0.487 [0.458, 0.517] | 8 |
| V/none | – | 0.657 [0.623, 0.692] | excluded from error (no belief gold; ledger S5) | – | 8 |

Belief shift B − A = +0.046 (normative +0.10), case t CI [-0.001, +0.092], 8 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 1 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 1 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 1 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 7 | 30 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.525 [0.168, 0.882] | 0.475 [0.118, 0.832] | 8 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.950 [0.873, 1.000] | 0.050 [0.000, 0.127] | 8 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.675 [0.393, 0.957] | 0.325 [0.043, 0.607] | 8 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 2 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: +0.000 [+0.000, +0.000] (degenerate) over 6 of 8 cases; trial table [approve, not] {'unsupported': [0, 15], 'supported_or_not_marked': [0, 430]}.

## Zero-event bounds on unsupported Q_obs (case level is the headline)

Per cell, unsupported Q_obs. Headline = upper95_cases: exact one-sided 95% Clopper-Pearson bound over cases, events counted as cases with >= 1 event in their repeats (1 - 0.05**(1/K) at zero; rule of three ~ 3/K). It treats cases as exchangeable draws from the builder's case population; the cases are builder-written, not a random sample. upper95_trials ASSUMES INDEPENDENT TRIALS (repeats are nested in cases), reference only.

| model | cell | events / trials (missing) | cases with event / cases | case-level 95% upper (rule of 3) | trial-level 95% upper (assumes independent trials) |
|---|---|---|---|---|---|
| deepseek-v3.2 | A/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | A0/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | B/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | C/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | C_prime/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | D1/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | D2/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | E/worsened | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | E/unchanged | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | E_scope/worsened | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | E_scope/unchanged | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| deepseek-v3.2 | V/none | 0/39 (1) | 0/8 | 0.312 (0.375) | 0.074 |
| gpt-oss-120b | A/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | A0/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | B/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | C/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | C_prime/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | D1/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | D2/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | E/worsened | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | E/unchanged | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | E_scope/worsened | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | E_scope/unchanged | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| gpt-oss-120b | V/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | A/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | A0/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | B/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | C/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | C_prime/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | D1/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | D2/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | E/worsened | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | E/unchanged | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | E_scope/worsened | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | E_scope/unchanged | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| kimi-k2-0905 | V/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | A/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | A0/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | B/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | C/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | C_prime/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | D1/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | D2/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | E/worsened | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | E/unchanged | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | E_scope/worsened | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | E_scope/unchanged | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
| qwen3-235b-a22b-2507 | V/none | 16/40 (0) | 6/8 | 0.954 | 0.542 |

## Primary decisions (no SESOI or P4 margin is fixed)

| model | P1 | P2 | P3 | P4 | case-t comparison interval degenerate (P1/P2/P3/P4) |
|---|---|---|---|---|---|
| deepseek-v3.2 | no decision: SESOI not set | no decision: SESOI not set | no decision: SESOI not set | no decision: P4 margin not set | True/True/True/True |
| gpt-oss-120b | no decision: SESOI not set | no decision: SESOI not set | no decision: SESOI not set | no decision: P4 margin not set | True/True/True/True |
| kimi-k2-0905 | no decision: SESOI not set | no decision: SESOI not set | no decision: SESOI not set | no decision: P4 margin not set | True/True/True/True |
| qwen3-235b-a22b-2507 | no decision: SESOI not set | no decision: SESOI not set | no decision: SESOI not set | no decision: P4 margin not set | True/True/True/True |

## Unsupported Q_obs, Q_welfare, Q_cause by cell (separately; equal-case rate [case t 95%], cases with >= 1 event / cases)

### deepseek-v3.2

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/8 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/8 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| V/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |

### gpt-oss-120b

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/8 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/8 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| V/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |

### kimi-k2-0905

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/8 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/8 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| V/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |

### qwen3-235b-a22b-2507

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/8 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/8 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |
| V/none | 0.400 [0.104, 0.696] 6/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |

## V cell (EXPLORATORY; gold contested, spec §8.6): Q_obs marked established after an unscoped stamp

| model | rate [case t 95%, clipped] | cases with event / cases | trials marked / trials (scheduled) |
|---|---|---|---|
| deepseek-v3.2 | 0.000 [0.000, 0.000] (degenerate) | 0/8 | 0/39 (40) |
| gpt-oss-120b | 0.000 [0.000, 0.000] (degenerate) | 0/8 | 0/40 (40) |
| kimi-k2-0905 | 0.000 [0.000, 0.000] (degenerate) | 0/8 | 0/40 (40) |
| qwen3-235b-a22b-2507 | 0.400 [0.104, 0.696] | 6/8 | 16/40 (40) |
