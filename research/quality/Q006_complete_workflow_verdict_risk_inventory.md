# Q006 — Complete workflow verdict-risk inventory

Status: **IN STUDY — COMPLETE LEXICAL INVENTORY VALIDATED; SEMANTIC AUDIT FOUND AND REPAIRED ONE GENUINE FALSE-GREEN PATH; HOSTED REGRESSION PENDING**
Evidence date: 2026-09-23
Lead: Quality; support: Systems

## Problem
Earlier repository code search for `tee` was incomplete and even missed a known workflow. It therefore could not support an absence claim about verdict-masking constructs. The repository contains many evidence-producing workflows, so a checkout-local complete inventory has higher reliability leverage than another synthetic `pipefail` variant.

## CLAIM / SPEC
**CLAIM:** a checkout-local traversal can enumerate every YAML workflow file present at an exact Studio ref and record every occurrence of selected verdict-risk constructs without relying on GitHub code-search indexing.

This is an inventory claim, not a correctness claim. A hit is not automatically defective, and absence of a selected lexical construct does not prove semantic correctness.

**SPEC/PROPERTY:** `methods/VALIDATION_STANDARD.md` requires trustworthy oracles and forbids equating workflow green with correctness. Q006 already validated that evidence preservation and producer verdict propagation are independent properties.

## Executable harness
- `research/quality/fixtures/Q006_workflow_verdict_risk_inventory.py`
- `.github/workflows/q006-workflow-verdict-risk-inventory.yml`
- introduction commits: `b9421c5c9d305924a095a64bafad53f06e2f5423`, `d573b47f05a1d5f65daea94d4133dcc221973d2a`

The fixture traverses both `*.yml` and `*.yaml` under `.github/workflows`, records the SHA-256 of every workflow, and inventories these constructs with exact file/line/text: pipeline `tee`, `continue-on-error: true`, `|| true`, `set +e`, `trap`, `exit 0`, and `if: always()`.

The hosted wrapper uses `set -euo pipefail`, requires a non-empty JSON inventory and an explicit completion marker, and preserves JSON/log artifacts even on failure.

## VALIDATION — exact hosted corpus
Exact head `d573b47f05a1d5f65daea94d4133dcc221973d2a`, run `35837301494`, completed **success**. Run-bound artifact `10739703444`, size 6,997 bytes, digest `sha256:5e47724ef150ff334548a21479a0c72afe296cbf6379354b424a03ecbf37c103`, was downloaded and directly inspected.

The manifest records **29 workflow files** and **131 selected risk hits**:
- `pipeline_tee`: 75
- `always`: 25
- `continue-on-error`: 12
- `set_plus_e`: 7
- `or_true`: 5
- `trap`: 4
- `exit_zero`: 3

**VALIDATION:** the exact-head lexical inventory boundary is PASS. This replaces the prior incomplete external code-search inventory for these selected constructs.

**SYNTHESIS:** the hit count is deliberately not a defect count. Direct inspection shows materially different semantics: ordinary version/log capture under fail-fast shell state; diagnostic `|| true`; explicit producer-status capture; fail-closed downstream checks; and negative tests where nonzero is the expected behavior. Therefore a blanket rewrite would destroy valid evidence patterns.

**TRANSFER VALIDATION:** the known repaired M006 Safari offline and service-worker workflows appear in the complete corpus with `set +e` setup capture and `tee` oracle paths. Their current oracle steps explicitly enable `pipefail` or capture/validate producer status, demonstrating why lexical presence alone cannot decide safety.

## Semantic audit finding — S005 verification boundary
The semantic review found a genuine verdict-propagation defect in `.github/workflows/s005-attestation-verification-boundary.yml`.

The workflow deliberately marked four attestation checks `continue-on-error: true`. Its final verdict step recorded all four outcomes, but asserted only the two negative controls (`wrong repository` and `wrong subject`). It did **not** assert that the positive attestation API query or exact-repository verification succeeded. Therefore the job could be green when the positive evidence path failed, provided the negative controls still returned their expected rejection outcomes.

**CONTRADICTION:** this violates the workflow's verification claim and the Studio Validation Standard. Recording an outcome is not equivalent to propagating that outcome into the job verdict.

**ROOT CAUSE at this exact workflow boundary:** positive checks were converted into non-fatal step outcomes with `continue-on-error`, but the downstream aggregate oracle omitted `QUERY=success` and `EXACT=success` from its acceptance predicate. The negative-control outcomes were propagated; the positive-control outcomes were not.

**REPAIR:** commit `6216003dc4d42c1ea2156500bcc1df1d404c045d` changes the aggregate step to fail closed on all four required outcomes and enables `set -euo pipefail` there. The repair preserves diagnostic execution of all checks while making positive-query and exact-verification failures job-fatal at the aggregate verdict boundary.

**VALIDATION:** hosted regression run `35843352058` is queued at exact repaired head `6216003dc4d42c1ea2156500bcc1df1d404c045d`. No regression PASS is awarded until its terminal result is inspected. Given the separately observed historical-attestation HTTP 404, a red result may be the correct fail-closed behavior rather than a regression defect; terminal evidence must distinguish these cases.

## Semantic-review boundary
Every hit that can affect a verdict must be classified against surrounding shell/workflow semantics. Required classes:
1. protected pipeline/log capture (`pipefail` or equivalent producer-status propagation);
2. deliberate diagnostic suppression outside the verdict path;
3. expected-failure/negative control with an independent downstream oracle;
4. intentional status capture followed by fail-closed propagation;
5. genuine false-green risk requiring repair.

The audit must also sample verdict-bearing commands without these lexical constructs. This scanner is a complete selected-pattern inventory, not a general shell/workflow verifier.

## FAILURE MODEL / LIMITS
The fixture proves corpus enumeration for the selected patterns at the exact ref. It cannot prove inherited shell state, GitHub-expression correctness, third-party-action internal verdict propagation, semantic-oracle validity, or absence of false-green paths expressed without these tokens.

The S005 repair establishes a static semantic defect and code correction; until hosted execution completes it does not establish the repaired workflow's runtime behavior.

## RELATED DOMAIN CHECK
- Foundations: process exit status and shell pipeline semantics are relevant; no new Foundations claim.
- Architecture: CI evidence contracts are interfaces between validators and release/governance consumers.
- Mobile: M006 supplied the natural false-green transfer and current navigation-aware oracle examples.
- Data: no data-specific claim.
- Quality: owner; complete inventory validated and semantic audit has now found one genuine false-green path.
- Systems: S005 is the natural release-evidence transfer; positive and negative attestation controls must both participate in the final verdict.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this repository-internal CI corpus.
- Product source: no product behavior audited; this block targets `yhappcom/software-engineering-studio` only.

## HANDOFFS
- Systems: treat the repaired S005 aggregate oracle as the reusable pattern: diagnostic continuation is acceptable only when every required positive/negative outcome is explicitly folded into a fail-closed final verdict.
- Mobile: retain navigation-aware semantic-oracle review separately from shell/workflow verdict propagation.

## OPEN
1. Inspect run `35843352058`; classify a red result against the known historical-attestation 404 rather than treating green as the only desired outcome.
2. Continue semantic classification of remaining verdict-relevant hits.
3. Sample verdict-bearing commands that do not match the selected lexical patterns.
4. Repair any additional genuine false-green path and obtain exact-head regression evidence.
5. Only then decide whether the repository-wide semantic CI audit boundary can close.
