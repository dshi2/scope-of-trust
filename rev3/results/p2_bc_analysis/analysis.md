# P2 pilot analysis

**DIAGNOSTIC PILOT on development cases (one author, one template family). Interval method provisional; P4 margin unapproved; not confirmatory evidence.**

## deepseek-v3.2

Calls 1120, spend $1.0139. Status {'ok': 1120}. Parse {'ok': 1120}. Truncated 0. Served provider {'AtlasCloud': 1120}; served model {'deepseek/deepseek-v3.2': 1120}.

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
| B/none | 0.000 | 40 | 0.000 | 40 |
| C/none | 0.000 | 40 | 0.000 | 40 |
| C_prime/none | 0.000 | 40 | 0.000 | 40 |
| D1/none | 0.000 | 40 | 0.000 | 40 |
| D2/none | 0.000 | 40 | 0.000 | 40 |
| E/improved | 0.000 | 40 | 0.052 | 40 |
| E/unchanged | 0.000 | 40 | 0.033 | 40 |
| E/worsened | 0.000 | 40 | 0.000 | 40 |
| E_scope/improved | 0.000 | 40 | 0.052 | 40 |
| E_scope/unchanged | 0.000 | 40 | 0.000 | 40 |
| E_scope/worsened | 0.000 | 40 | 0.000 | 40 |
| V/none | 0.000 | 40 | nan | 0 |

## gpt-oss-120b

Calls 1120, spend $0.1574. Status {'ok': 1120}. Parse {'ok': 1120}. Truncated 0. Served provider {'DeepInfra': 1120}; served model {'openai/gpt-oss-120b': 1120}.

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
| B/none | 0.000 | 40 | 0.007 | 40 |
| C/none | 0.000 | 40 | 0.002 | 40 |
| C_prime/none | 0.000 | 40 | 0.007 | 40 |
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

Calls 1120, spend $1.6204. Status {'ok': 1120}. Parse {'ok': 1116, 'malformed': 4}. Truncated 4. Served provider {'Novita': 1120}; served model {'moonshotai/kimi-k2-0905': 1120}.

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
| V3_manipulation_check | D1/none | 0.975 | [0.916, 1.000] | 8 | 40 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 8 | 40 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 40 | 0.015 | 40 |
| A0/none | 0.000 | 40 | 0.069 | 38 |
| B/none | 0.000 | 40 | 0.016 | 40 |
| C/none | 0.000 | 40 | 0.019 | 40 |
| C_prime/none | 0.000 | 40 | 0.020 | 40 |
| D1/none | 0.000 | 40 | 0.011 | 40 |
| D2/none | 0.000 | 40 | 0.009 | 40 |
| E/improved | 0.000 | 40 | 0.042 | 40 |
| E/unchanged | 0.000 | 40 | 0.146 | 40 |
| E/worsened | 0.000 | 40 | 0.087 | 40 |
| E_scope/improved | 0.000 | 40 | 0.116 | 40 |
| E_scope/unchanged | 0.000 | 40 | 0.174 | 40 |
| E_scope/worsened | 0.000 | 40 | 0.155 | 40 |
| V/none | 0.000 | 39 | nan | 0 |

## qwen3-235b-a22b-2507

Calls 1120, spend $0.1765. Status {'ok': 1120}. Parse {'ok': 1120}. Truncated 0. Served provider {'DeepInfra': 1120}; served model {'qwen/qwen3-235b-a22b-2507': 1120}.

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
| A/none | 0.000 | 40 | 0.034 | 40 |
| A0/none | 0.000 | 40 | 0.134 | 40 |
| B/none | 0.000 | 40 | 0.075 | 40 |
| C/none | 0.000 | 40 | 0.100 | 40 |
| C_prime/none | 0.000 | 40 | 0.086 | 40 |
| D1/none | 0.000 | 40 | 0.026 | 40 |
| D2/none | 0.000 | 40 | 0.029 | 40 |
| E/improved | 0.000 | 40 | 0.089 | 40 |
| E/unchanged | 0.000 | 40 | 0.425 | 40 |
| E/worsened | 0.000 | 40 | 0.237 | 40 |
| E_scope/improved | 0.000 | 40 | 0.131 | 40 |
| E_scope/unchanged | 0.000 | 40 | 0.481 | 40 |
| E_scope/worsened | 0.000 | 40 | 0.254 | 40 |
| V/none | 0.725 | 40 | nan | 0 |

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
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 40 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| A0/none | 0.500 | 0.500 [0.500, 0.500] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| B/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| C/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| C_prime/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D1/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D2/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E/improved | 1.000 | 0.948 [0.920, 0.975] | -0.052 [-0.080, -0.025] | 0.052 [0.025, 0.080] | 8 |
| E/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E/unchanged | 0.000 | 0.033 [0.000, 0.083] | +0.033 [-0.018, +0.083] | 0.033 [-0.018, 0.083] | 8 |
| E_scope/improved | 1.000 | 0.948 [0.906, 0.989] | -0.052 [-0.094, -0.011] | 0.052 [0.011, 0.094] | 8 |
| E_scope/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E_scope/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| V/none | – | 0.650 [0.650, 0.650] (degenerate) | excluded from error (no belief gold; ledger S5) | – | 8 |

Belief shift B − A = +0.100 (normative +0.10), case t CI [+0.100, +0.100] (degenerate), 8 cases.

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
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.025 [0.000, 0.084] | 0.975 [0.916, 1.000] | 8 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.200 [0.074, 0.326] | 0.800 [0.674, 0.926] | 8 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.100 [0.000, 0.226] | 0.900 [0.774, 1.000] | 8 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.075 [0.000, 0.162] | 0.925 [0.838, 1.000] | 8 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: not estimable (no case has trials of both kinds) over 0 of 8 cases; trial table [approve, not] {'unsupported': [0, 0], 'supported_or_not_marked': [0, 480]}.

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
| B/none | 0.750 | 0.743 [0.725, 0.760] | -0.007 [-0.025, +0.010] | 0.007 [-0.010, 0.025] | 8 |
| C/none | 0.750 | 0.748 [0.742, 0.753] | -0.002 [-0.008, +0.003] | 0.002 [-0.003, 0.008] | 8 |
| C_prime/none | 0.750 | 0.743 [0.725, 0.760] | -0.007 [-0.025, +0.010] | 0.007 [-0.010, 0.025] | 8 |
| D1/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| D2/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E/improved | 1.000 | 1.000 [1.000, 1.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E_scope/improved | 1.000 | 1.000 [1.000, 1.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E_scope/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| E_scope/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 |
| V/none | – | 0.650 [0.650, 0.650] (degenerate) | excluded from error (no belief gold; ledger S5) | – | 8 |

Belief shift B − A = +0.092 (normative +0.10), case t CI [+0.075, +0.110], 8 cases.

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
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.175 [0.000, 0.383] | 0.825 [0.617, 1.000] | 8 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.400 [0.010, 0.790] | 0.600 [0.210, 0.990] | 8 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.250 [0.000, 0.556] | 0.750 [0.444, 1.000] | 8 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.650 [0.307, 0.993] | 0.350 [0.007, 0.693] | 8 | 0 |
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
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 8 | 39 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.645 [0.638, 0.652] | -0.005 [-0.012, +0.002] | 0.015 [0.004, 0.026] | 8 |
| A0/none | 0.500 | 0.563 [0.525, 0.602] | +0.063 [+0.025, +0.102] | 0.071 [0.045, 0.097] | 8 |
| B/none | 0.750 | 0.734 [0.724, 0.745] | -0.016 [-0.026, -0.005] | 0.016 [0.005, 0.026] | 8 |
| C/none | 0.750 | 0.731 [0.715, 0.746] | -0.019 [-0.035, -0.004] | 0.019 [0.004, 0.035] | 8 |
| C_prime/none | 0.750 | 0.730 [0.715, 0.745] | -0.020 [-0.035, -0.005] | 0.020 [0.005, 0.035] | 8 |
| D1/none | 0.650 | 0.644 [0.638, 0.651] | -0.006 [-0.012, +0.001] | 0.011 [0.003, 0.019] | 8 |
| D2/none | 0.650 | 0.651 [0.642, 0.659] | +0.001 [-0.008, +0.009] | 0.009 [0.001, 0.018] | 8 |
| E/improved | 1.000 | 0.958 [0.930, 0.987] | -0.042 [-0.070, -0.013] | 0.042 [0.013, 0.070] | 8 |
| E/worsened | 0.000 | 0.087 [0.042, 0.132] | +0.087 [+0.042, +0.132] | 0.087 [0.042, 0.132] | 8 |
| E/unchanged | 0.000 | 0.146 [0.068, 0.225] | +0.146 [+0.068, +0.225] | 0.146 [0.068, 0.225] | 8 |
| E_scope/improved | 1.000 | 0.884 [0.835, 0.934] | -0.116 [-0.165, -0.066] | 0.116 [0.066, 0.165] | 8 |
| E_scope/worsened | 0.000 | 0.155 [0.077, 0.233] | +0.155 [+0.077, +0.233] | 0.155 [0.077, 0.233] | 8 |
| E_scope/unchanged | 0.000 | 0.174 [0.075, 0.272] | +0.174 [+0.075, +0.272] | 0.174 [0.075, 0.272] | 8 |
| V/none | – | 0.668 [0.646, 0.690] | excluded from error (no belief gold; ledger S5) | – | 8 |

Belief shift B − A = +0.089 (normative +0.10), case t CI [+0.077, +0.102], 8 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 1 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.050 [0.000, 0.127] | 0.950 [0.873, 1.000] | 8 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.275 [0.122, 0.428] | 0.725 [0.572, 0.878] | 8 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.175 [0.000, 0.363] | 0.825 [0.637, 1.000] | 8 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.525 [0.258, 0.792] | 0.475 [0.208, 0.742] | 8 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 1 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: not estimable (no case has trials of both kinds) over 0 of 8 cases; trial table [approve, not] {'unsupported': [0, 0], 'supported_or_not_marked': [0, 478]}.

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
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.725 | [+0.085, +0.945] | 0.028 (not in Holm) | 8 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.725 | [+0.085, +0.945] | 0.028 (not in Holm) | 8 |

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
| A/none | 0.650 | 0.616 [0.604, 0.629] | -0.034 [-0.046, -0.021] | 0.034 [0.021, 0.046] | 8 |
| A0/none | 0.500 | 0.634 [0.621, 0.648] | +0.134 [+0.121, +0.148] | 0.134 [0.121, 0.148] | 8 |
| B/none | 0.750 | 0.675 [0.628, 0.722] | -0.075 [-0.122, -0.028] | 0.075 [0.028, 0.122] | 8 |
| C/none | 0.750 | 0.650 [0.620, 0.680] | -0.100 [-0.130, -0.070] | 0.100 [0.070, 0.130] | 8 |
| C_prime/none | 0.750 | 0.664 [0.628, 0.700] | -0.086 [-0.122, -0.050] | 0.086 [0.050, 0.122] | 8 |
| D1/none | 0.650 | 0.624 [0.623, 0.626] | -0.026 [-0.027, -0.024] | 0.026 [0.024, 0.027] | 8 |
| D2/none | 0.650 | 0.631 [0.622, 0.641] | -0.019 [-0.028, -0.009] | 0.029 [0.023, 0.035] | 8 |
| E/improved | 1.000 | 0.911 [0.863, 0.959] | -0.089 [-0.137, -0.041] | 0.089 [0.041, 0.137] | 8 |
| E/worsened | 0.000 | 0.237 [0.218, 0.257] | +0.237 [+0.218, +0.257] | 0.237 [0.218, 0.257] | 8 |
| E/unchanged | 0.000 | 0.425 [0.362, 0.488] | +0.425 [+0.362, +0.488] | 0.425 [0.362, 0.488] | 8 |
| E_scope/improved | 1.000 | 0.869 [0.822, 0.915] | -0.131 [-0.178, -0.085] | 0.131 [0.085, 0.178] | 8 |
| E_scope/worsened | 0.000 | 0.254 [0.245, 0.263] | +0.254 [+0.245, +0.263] | 0.254 [0.245, 0.263] | 8 |
| E_scope/unchanged | 0.000 | 0.481 [0.460, 0.503] | +0.481 [+0.460, +0.503] | 0.481 [0.460, 0.503] | 8 |
| V/none | – | 0.626 [0.610, 0.643] | excluded from error (no belief gold; ledger S5) | – | 8 |

Belief shift B − A = +0.059 (normative +0.10), case t CI [+0.009, +0.108], 8 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 2 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 1 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 6 | 26 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.525 [0.180, 0.870] | 0.475 [0.130, 0.820] | 8 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.950 [0.832, 1.000] | 0.050 [0.000, 0.168] | 8 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.625 [0.381, 0.869] | 0.375 [0.131, 0.619] | 8 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.975 [0.916, 1.000] | 0.025 [0.000, 0.084] | 8 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 6 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: +0.000 [+0.000, +0.000] (degenerate) over 8 of 8 cases; trial table [approve, not] {'unsupported': [0, 23], 'supported_or_not_marked': [0, 422]}.

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
| deepseek-v3.2 | V/none | 0/40 (0) | 0/8 | 0.312 (0.375) | 0.072 |
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
| kimi-k2-0905 | V/none | 0/39 (1) | 0/8 | 0.312 (0.375) | 0.074 |
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
| qwen3-235b-a22b-2507 | V/none | 29/40 (0) | 8/8 | 1.000 | 0.837 |

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
| V/none | 0.725 [0.443, 1.000] 8/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 | 0.000 [0.000, 0.000] (degenerate) 0/8 |

## V cell (EXPLORATORY; gold contested, spec §8.6): Q_obs marked established after an unscoped stamp

| model | rate [case t 95%, clipped] | cases with event / cases | trials marked / trials (scheduled) |
|---|---|---|---|
| deepseek-v3.2 | 0.000 [0.000, 0.000] (degenerate) | 0/8 | 0/40 (40) |
| gpt-oss-120b | 0.000 [0.000, 0.000] (degenerate) | 0/8 | 0/40 (40) |
| kimi-k2-0905 | 0.000 [0.000, 0.000] (degenerate) | 0/8 | 0/39 (40) |
| qwen3-235b-a22b-2507 | 0.725 [0.443, 1.000] | 8/8 | 29/40 (40) |
