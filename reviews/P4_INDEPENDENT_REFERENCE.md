# P2 P4: independent conservative statistical reference (review only)

**Source snapshot:** `p2-revision-3` commit `a439c11903a4e4aa23f04964663bf1b93dec3f7a`, 16 Nov 2026. **Audit branch:** `audit/p4-independent-bound-2026-11-16`.

This is an **independent comparator** for the builder's prospective analysis and precision simulation. It is **not** the chosen analysis, a preregistration, evidence of validity, or a reason to size the study from the API budget. It performs **no** model calls.

## Reproduce (Python standard library only)

From the repository root:

```sh
python3 -m unittest discover -s reviews -p 'test_p4_bound_reference.py' -v
```

The test suite checks ceiling behavior, directional sign, missing-data bounds, duplicate-case prevention, model separation, repeat dependence, input validation and the bound formula.

## What it calculates

P4 is a comparison of justified **correct acceptance** on **E_scope improved** versus **E improved**, for the same independently designed case and the same fixed model:

`D_i = correct_acceptance(E_scope improved, i) - correct_acceptance(E improved, i)`.

A `CasePair` represents **one independent case**. Each arm records the number of *scheduled* repeats, repeats with a *scored* 0/1 outcome, and observed correct acceptances. Unknown outputs are never silently dropped, zero-imputed or assumed missing at random.

For an arm, the case-level acceptance rate must lie in

`[accepted / planned, (accepted + planned - scored) / planned]`.

The paired difference is therefore in `[scope_lower - e_upper, scope_upper - e_lower]`. Average those extremes over independent cases to obtain an **identification interval for the observed sample** under unrestricted missing responses.

The one-sided population lower confidence bound is

`L = max(-1, mean_case_difference_lower - sqrt(2 log(1/alpha) / n_cases))`.

This is Hoeffding's inequality for **independent case-level differences in [-1,1]**, even if the two treatment results within a case are strongly correlated. It remains conservative at perfect acceptance: an observed all-zero *difference* does not imply zero uncertainty. Noninferiority is supported by this comparator only if `L > -delta`, with `delta` the independently justified P4 loss margin and `alpha` the one-sided error probability assigned under the primary-family multiplicity policy.

**Do not use this bound for clustered or dependent case families without adjusting the independent sampling unit.** The code rejects duplicate case identifiers and mixing models, but it cannot verify that distinct scenario IDs are scientifically independent. It also does not model variation across case-generating families, selection of cases, uncertain gold labels or time drift in providers.

## Why this is not the recommended final estimator

Hoeffding is intentionally loose. With all paired differences exactly zero, `alpha=.025`, `delta=.05`, and 100 independent cases, the radius is about **0.272**, so the comparator cannot establish noninferiority. At about 3,000 truly independent cases, the radius is about **0.050** and the all-zero-difference example can just reach the threshold. That is **not a P2 sample-size proposal**. The true paired design, covariance, ceiling rates, model heterogeneity, case families, missingness and multiplicity require the builder's dedicated simulation and coverage-tested candidate intervals.

An appropriately validated paired binomial or case-level method may be much sharper than this bound. A discrepancy between the builder's estimate and this conservative comparator is not automatically a bug; investigate whether it reflects justified assumptions or undercoverage.

## Next independent comparison with the builder

Run both the builder's chosen candidate methods and this reference on the **same predeclared simulated scenarios**, including:

- pairs with 100% correct acceptance and varying independent case counts;
- different paired associations (identical outcomes, discordance concentrated in either direction);
- correctly accepted cases mixed with missed justified acceptances;
- missing responses that are independent, condition-dependent, or outcome-dependent;
- multiple repeat calls within a fixed small number of cases;
- case-family dependence and model differences (**the reference is not valid for these unless appropriately regrouped**).

Compare interval coverage, false noninferiority rates when the true effect is at or below `-delta`, power when clinically/practically acceptable, and robustness to nonrandom missingness. Choose and freeze the final method **before** confirmatory outcomes. An independent reviewer should assess both methods; their authors cannot certify their own coverage.

**No model experiments, confirmatory changes or merges are authorized here.**
