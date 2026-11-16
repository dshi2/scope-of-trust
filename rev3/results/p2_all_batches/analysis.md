# P2 pilot analysis

**DIAGNOSTIC PILOT on development cases (one author, one template family). Interval method provisional; P4 margin unapproved; not confirmatory evidence.**

## deepseek-v3.2

Calls 5040, spend $4.5967. Status {'ok': 5040}. Parse {'ok': 5039, 'malformed': 1}. Truncated 0. Served provider {'AtlasCloud': 5040}; served model {'deepseek/deepseek-v3.2': 5040}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.120, +0.120] | no decision (margin not fixed); one-sided 97.5% LB -0.120 | +0.000 to +0.000 | 36 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |
| P2 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |
| P3 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 180 | 0.000 | 180 |
| A0/none | 0.000 | 180 | 0.000 | 180 |
| B/none | 0.000 | 180 | 0.001 | 180 |
| C/none | 0.000 | 180 | 0.000 | 180 |
| C_prime/none | 0.000 | 180 | 0.000 | 180 |
| D1/none | 0.000 | 180 | 0.000 | 180 |
| D2/none | 0.000 | 180 | 0.000 | 180 |
| E/improved | 0.000 | 180 | 0.051 | 180 |
| E/unchanged | 0.000 | 180 | 0.014 | 180 |
| E/worsened | 0.000 | 180 | 0.018 | 180 |
| E_scope/improved | 0.000 | 180 | 0.039 | 180 |
| E_scope/unchanged | 0.000 | 180 | 0.000 | 180 |
| E_scope/worsened | 0.000 | 180 | 0.007 | 180 |
| V/none | 0.000 | 179 | nan | 0 |

## gpt-oss-120b

Calls 5040, spend $0.6923. Status {'ok': 5040}. Parse {'ok': 5040}. Truncated 0. Served provider {'DeepInfra': 5040}; served model {'openai/gpt-oss-120b': 5040}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.120, +0.120] | no decision (margin not fixed); one-sided 97.5% LB -0.120 | +0.000 to +0.000 | 36 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |
| P2 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |
| P3 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 180 | 0.000 | 180 |
| A0/none | 0.000 | 180 | 0.001 | 180 |
| B/none | 0.000 | 180 | 0.004 | 180 |
| C/none | 0.000 | 180 | 0.003 | 180 |
| C_prime/none | 0.000 | 180 | 0.002 | 180 |
| D1/none | 0.000 | 180 | 0.000 | 180 |
| D2/none | 0.000 | 180 | 0.000 | 180 |
| E/improved | 0.000 | 180 | 0.000 | 180 |
| E/unchanged | 0.000 | 180 | 0.000 | 180 |
| E/worsened | 0.000 | 180 | 0.000 | 180 |
| E_scope/improved | 0.000 | 180 | 0.000 | 180 |
| E_scope/unchanged | 0.000 | 180 | 0.000 | 180 |
| E_scope/worsened | 0.000 | 180 | 0.000 | 180 |
| V/none | 0.000 | 180 | nan | 0 |

## kimi-k2-0905

Calls 5040, spend $8.9538. Status {'ok': 5040}. Parse {'ok': 4999, 'malformed': 38, 'invalid': 3}. Truncated 38. Served provider {'Novita': 5040}; served model {'moonshotai/kimi-k2-0905': 5040}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | -0.011 to +0.000 | 36 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.120, +0.120] | no decision (margin not fixed); one-sided 97.5% LB -0.120 | +0.000 to +0.000 | 36 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |
| P2 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |
| P3 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 36 | 179 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | D1/none | 0.994 | [0.983, 1.000] | 36 | 180 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 178 | 0.015 | 180 |
| A0/none | 0.000 | 180 | 0.050 | 173 |
| B/none | 0.000 | 180 | 0.021 | 180 |
| C/none | 0.000 | 180 | 0.030 | 180 |
| C_prime/none | 0.000 | 180 | 0.024 | 180 |
| D1/none | 0.000 | 180 | 0.011 | 180 |
| D2/none | 0.000 | 180 | 0.012 | 178 |
| E/improved | 0.000 | 180 | 0.044 | 178 |
| E/unchanged | 0.000 | 180 | 0.143 | 176 |
| E/worsened | 0.000 | 179 | 0.097 | 179 |
| E_scope/improved | 0.000 | 180 | 0.079 | 180 |
| E_scope/unchanged | 0.000 | 180 | 0.182 | 177 |
| E_scope/worsened | 0.000 | 180 | 0.145 | 176 |
| V/none | 0.017 | 179 | nan | 0 |

## qwen3-235b-a22b-2507

Calls 5040, spend $0.8090. Status {'ok': 5040}. Parse {'ok': 5039, 'invalid': 1}. Truncated 0. Served provider {'DeepInfra': 5040}; served model {'qwen/qwen3-235b-a22b-2507': 5040}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | +0.000 to +0.000 | 36 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.120, +0.120] | no decision (margin not fixed); one-sided 97.5% LB -0.120 | +0.000 to +0.000 | 36 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |
| P2 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |
| P3 | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] | +0.000 [-0.120, +0.120] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 179 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 36 | 180 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 180 | 0.031 | 180 |
| A0/none | 0.000 | 180 | 0.132 | 180 |
| B/none | 0.000 | 180 | 0.069 | 180 |
| C/none | 0.000 | 180 | 0.086 | 180 |
| C_prime/none | 0.000 | 179 | 0.084 | 180 |
| D1/none | 0.000 | 180 | 0.030 | 180 |
| D2/none | 0.000 | 180 | 0.040 | 180 |
| E/improved | 0.000 | 180 | 0.081 | 180 |
| E/unchanged | 0.000 | 180 | 0.419 | 180 |
| E/worsened | 0.000 | 180 | 0.246 | 180 |
| E_scope/improved | 0.000 | 180 | 0.089 | 180 |
| E_scope/unchanged | 0.000 | 180 | 0.462 | 180 |
| E_scope/worsened | 0.000 | 180 | 0.249 | 180 |
| V/none | 0.533 | 180 | nan | 0 |

## deepseek-v3.2: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 179 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| A0/none | 0.500 | 0.500 [0.500, 0.500] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| B/none | 0.750 | 0.749 [0.747, 0.750] | -0.001 [-0.003, +0.000] | 0.001 [-0.000, 0.003] | 36 |
| C/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| C_prime/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| D1/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| D2/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| E/improved | 1.000 | 0.949 [0.933, 0.966] | -0.051 [-0.067, -0.034] | 0.051 [0.034, 0.067] | 36 |
| E/worsened | 0.000 | 0.018 [0.003, 0.033] | +0.018 [+0.003, +0.033] | 0.018 [0.003, 0.033] | 36 |
| E/unchanged | 0.000 | 0.014 [0.000, 0.028] | +0.014 [+0.000, +0.028] | 0.014 [0.000, 0.028] | 36 |
| E_scope/improved | 1.000 | 0.961 [0.942, 0.980] | -0.039 [-0.058, -0.020] | 0.039 [0.020, 0.058] | 36 |
| E_scope/worsened | 0.000 | 0.007 [0.000, 0.017] | +0.007 [-0.003, +0.017] | 0.007 [-0.003, 0.017] | 36 |
| E_scope/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| V/none | – | 0.651 [0.649, 0.652] | excluded from error (no belief gold; ledger S5) | – | 36 |

Belief shift B − A = +0.099 (normative +0.10), case t CI [+0.097, +0.100], 36 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.061 [0.013, 0.109] | 0.939 [0.891, 0.987] | 36 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.117 [0.070, 0.163] | 0.883 [0.837, 0.930] | 36 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.083 [0.031, 0.135] | 0.917 [0.865, 0.969] | 36 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.122 [0.079, 0.166] | 0.878 [0.834, 0.921] | 36 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 1 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: not estimable (no case has trials of both kinds) over 0 of 36 cases; trial table [approve, not] {'unsupported': [0, 0], 'supported_or_not_marked': [0, 2159]}.

## gpt-oss-120b: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| A0/none | 0.500 | 0.501 [0.499, 0.503] | +0.001 [-0.001, +0.003] | 0.001 [-0.001, 0.003] | 36 |
| B/none | 0.750 | 0.746 [0.739, 0.752] | -0.004 [-0.011, +0.002] | 0.004 [-0.002, 0.011] | 36 |
| C/none | 0.750 | 0.747 [0.744, 0.751] | -0.003 [-0.006, +0.001] | 0.003 [-0.001, 0.006] | 36 |
| C_prime/none | 0.750 | 0.748 [0.745, 0.752] | -0.002 [-0.005, +0.002] | 0.002 [-0.002, 0.005] | 36 |
| D1/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| D2/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| E/improved | 1.000 | 1.000 [1.000, 1.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| E/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| E/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| E_scope/improved | 1.000 | 1.000 [1.000, 1.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| E_scope/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| E_scope/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| V/none | – | 0.650 [0.650, 0.650] (degenerate) | excluded from error (no belief gold; ledger S5) | – | 36 |

Belief shift B − A = +0.096 (normative +0.10), case t CI [+0.089, +0.102], 36 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.211 [0.113, 0.309] | 0.789 [0.691, 0.887] | 36 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.472 [0.346, 0.599] | 0.528 [0.401, 0.654] | 36 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.322 [0.216, 0.429] | 0.678 [0.571, 0.784] | 36 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.639 [0.522, 0.755] | 0.361 [0.245, 0.478] | 36 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: not estimable (no case has trials of both kinds) over 0 of 36 cases; trial table [approve, not] {'unsupported': [0, 0], 'supported_or_not_marked': [0, 2160]}.

## kimi-k2-0905: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.017 | [-0.105, +0.146] | 0.9 (not in Holm) | 36 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.017 | [-0.105, +0.146] | 0.9 (not in Holm) | 36 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 178 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 36 | 179 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| V/none | 0.006 | [0.000, 0.017] | 36 | 179 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.640 [0.635, 0.645] | -0.010 [-0.015, -0.005] | 0.015 [0.010, 0.019] | 36 |
| A0/none | 0.500 | 0.548 [0.537, 0.560] | +0.048 [+0.037, +0.060] | 0.050 [0.040, 0.061] | 36 |
| B/none | 0.750 | 0.731 [0.725, 0.737] | -0.019 [-0.025, -0.013] | 0.021 [0.015, 0.027] | 36 |
| C/none | 0.750 | 0.720 [0.713, 0.728] | -0.030 [-0.037, -0.022] | 0.030 [0.023, 0.038] | 36 |
| C_prime/none | 0.750 | 0.730 [0.723, 0.738] | -0.020 [-0.027, -0.012] | 0.024 [0.017, 0.031] | 36 |
| D1/none | 0.650 | 0.644 [0.640, 0.648] | -0.006 [-0.010, -0.002] | 0.011 [0.007, 0.015] | 36 |
| D2/none | 0.650 | 0.650 [0.646, 0.655] | +0.000 [-0.004, +0.005] | 0.011 [0.008, 0.015] | 36 |
| E/improved | 1.000 | 0.956 [0.940, 0.972] | -0.044 [-0.060, -0.028] | 0.044 [0.028, 0.060] | 36 |
| E/worsened | 0.000 | 0.097 [0.076, 0.119] | +0.097 [+0.076, +0.119] | 0.097 [0.076, 0.119] | 36 |
| E/unchanged | 0.000 | 0.142 [0.117, 0.167] | +0.142 [+0.117, +0.167] | 0.142 [0.117, 0.167] | 36 |
| E_scope/improved | 1.000 | 0.921 [0.896, 0.945] | -0.079 [-0.104, -0.055] | 0.079 [0.055, 0.104] | 36 |
| E_scope/worsened | 0.000 | 0.145 [0.122, 0.167] | +0.145 [+0.122, +0.167] | 0.145 [0.122, 0.167] | 36 |
| E_scope/unchanged | 0.000 | 0.182 [0.145, 0.219] | +0.182 [+0.145, +0.219] | 0.182 [0.145, 0.219] | 36 |
| V/none | – | 0.659 [0.651, 0.668] | excluded from error (no belief gold; ledger S5) | – | 36 |

Belief shift B − A = +0.091 (normative +0.10), case t CI [+0.082, +0.101], 36 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 1 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.067 [0.027, 0.106] | 0.933 [0.894, 0.973] | 36 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.344 [0.249, 0.440] | 0.656 [0.560, 0.751] | 36 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.144 [0.075, 0.214] | 0.856 [0.786, 0.925] | 36 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.383 [0.297, 0.470] | 0.617 [0.530, 0.703] | 36 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 1 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: +0.000 [+0.000, +0.000] (degenerate) over 3 of 36 cases; trial table [approve, not] {'unsupported': [0, 3], 'supported_or_not_marked': [0, 2152]}.

## qwen3-235b-a22b-2507: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.120, +0.120] | 1 (1) | 36 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.120, +0.120] | 1 (not in Holm) | 36 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.533 | [+0.361, +0.697] | 2e-05 (not in Holm) | 36 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.533 | [+0.361, +0.697] | 2e-05 (not in Holm) | 36 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.050 | [0.000, 0.105] | 36 | 180 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 179 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 36 | 180 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.625 [0.620, 0.631] | -0.025 [-0.030, -0.019] | 0.031 [0.027, 0.035] | 36 |
| A0/none | 0.500 | 0.632 [0.619, 0.645] | +0.132 [+0.119, +0.145] | 0.132 [0.119, 0.145] | 36 |
| B/none | 0.750 | 0.681 [0.664, 0.698] | -0.069 [-0.086, -0.052] | 0.069 [0.052, 0.086] | 36 |
| C/none | 0.750 | 0.665 [0.651, 0.679] | -0.085 [-0.099, -0.071] | 0.086 [0.072, 0.101] | 36 |
| C_prime/none | 0.750 | 0.666 [0.654, 0.679] | -0.084 [-0.096, -0.071] | 0.084 [0.072, 0.097] | 36 |
| D1/none | 0.650 | 0.623 [0.617, 0.628] | -0.027 [-0.033, -0.022] | 0.030 [0.025, 0.034] | 36 |
| D2/none | 0.650 | 0.636 [0.626, 0.645] | -0.014 [-0.024, -0.005] | 0.040 [0.033, 0.047] | 36 |
| E/improved | 1.000 | 0.919 [0.900, 0.939] | -0.081 [-0.100, -0.061] | 0.081 [0.061, 0.100] | 36 |
| E/worsened | 0.000 | 0.246 [0.240, 0.253] | +0.246 [+0.240, +0.253] | 0.246 [0.240, 0.253] | 36 |
| E/unchanged | 0.000 | 0.419 [0.393, 0.445] | +0.419 [+0.393, +0.445] | 0.419 [0.393, 0.445] | 36 |
| E_scope/improved | 1.000 | 0.911 [0.890, 0.931] | -0.089 [-0.110, -0.069] | 0.089 [0.069, 0.110] | 36 |
| E_scope/worsened | 0.000 | 0.249 [0.238, 0.261] | +0.249 [+0.238, +0.261] | 0.249 [0.238, 0.261] | 36 |
| E_scope/unchanged | 0.000 | 0.462 [0.441, 0.482] | +0.462 [+0.441, +0.482] | 0.462 [0.441, 0.482] | 36 |
| V/none | – | 0.644 [0.633, 0.654] | excluded from error (no belief gold; ledger S5) | – | 36 |

Belief shift B − A = +0.056 (normative +0.10), case t CI [+0.038, +0.074], 36 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 3 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 1 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 1 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 3 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 28 | 128 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 1 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.511 [0.385, 0.637] | 0.489 [0.363, 0.615] | 36 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.956 [0.923, 0.988] | 0.044 [0.012, 0.077] | 36 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.733 [0.636, 0.830] | 0.267 [0.170, 0.364] | 36 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.978 [0.951, 1.000] | 0.022 [0.000, 0.049] | 36 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 36 | 11 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: +0.000 [+0.000, +0.000] (degenerate) over 32 of 36 cases; trial table [approve, not] {'unsupported': [0, 88], 'supported_or_not_marked': [0, 1925]}.

## Zero-event bounds on unsupported Q_obs (case level is the headline)

Per cell, unsupported Q_obs. Headline = upper95_cases: exact one-sided 95% Clopper-Pearson bound over cases, events counted as cases with >= 1 event in their repeats (1 - 0.05**(1/K) at zero; rule of three ~ 3/K). It treats cases as exchangeable draws from the builder's case population; the cases are builder-written, not a random sample. upper95_trials ASSUMES INDEPENDENT TRIALS (repeats are nested in cases), reference only.

| model | cell | events / trials (missing) | cases with event / cases | case-level 95% upper (rule of 3) | trial-level 95% upper (assumes independent trials) |
|---|---|---|---|---|---|
| deepseek-v3.2 | A/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | A0/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | B/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | C/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | C_prime/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | D1/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | D2/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | E/worsened | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | E/unchanged | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | E_scope/worsened | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | E_scope/unchanged | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| deepseek-v3.2 | V/none | 0/179 (1) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | A/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | A0/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | B/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | C/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | C_prime/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | D1/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | D2/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | E/worsened | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | E/unchanged | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | E_scope/worsened | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | E_scope/unchanged | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| gpt-oss-120b | V/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | A/none | 0/178 (2) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | A0/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | B/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | C/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | C_prime/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | D1/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | D2/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | E/worsened | 0/179 (1) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | E/unchanged | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | E_scope/worsened | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | E_scope/unchanged | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| kimi-k2-0905 | V/none | 3/179 (1) | 3/36 | 0.202 | 0.043 |
| qwen3-235b-a22b-2507 | A/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | A0/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | B/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | C/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | C_prime/none | 0/179 (1) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | D1/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | D2/none | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | E/worsened | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | E/unchanged | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | E_scope/worsened | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | E_scope/unchanged | 0/180 (0) | 0/36 | 0.080 (0.083) | 0.017 |
| qwen3-235b-a22b-2507 | V/none | 96/180 (0) | 32/36 | 0.961 | 0.597 |

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
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/36 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/36 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| V/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |

### gpt-oss-120b

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/36 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/36 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| V/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |

### kimi-k2-0905

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/36 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/36 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| V/none | 0.017 [0.000, 0.036] 3/36 | 0.006 [0.000, 0.017] 1/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |

### qwen3-235b-a22b-2507

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/36 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/36 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |
| V/none | 0.533 [0.418, 0.649] 32/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 | 0.000 [0.000, 0.000] (degenerate) 0/36 |

## V cell (EXPLORATORY; gold contested, spec §8.6): Q_obs marked established after an unscoped stamp

| model | rate [case t 95%, clipped] | cases with event / cases | trials marked / trials (scheduled) |
|---|---|---|---|
| deepseek-v3.2 | 0.000 [0.000, 0.000] (degenerate) | 0/36 | 0/179 (180) |
| gpt-oss-120b | 0.000 [0.000, 0.000] (degenerate) | 0/36 | 0/180 (180) |
| kimi-k2-0905 | 0.017 [0.000, 0.036] | 3/36 | 3/179 (180) |
| qwen3-235b-a22b-2507 | 0.533 [0.418, 0.649] | 32/36 | 96/180 (180) |
