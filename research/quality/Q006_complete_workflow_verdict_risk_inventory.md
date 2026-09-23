# Q006 — Complete workflow verdict-risk inventory

Status: **IN STUDY — COMPLETE LEXICAL INVENTORY VALIDATED; SEMANTIC AUDIT HAS ONE REPAIRED NATURAL FALSE-GREEN CLASS AND ADDITIONAL SAFE CLASSIFICATIONS**
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
- `continue_on_error`: 12
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

**VALIDATION — hosted fail-closed regression:** exact repaired head `6216003dc4d42c1ea2156500bcc1df1d404c045d`, run `35843352058`, job `107123462773`, completed **failure**. All four diagnostic check steps were allowed to complete; the final `Record verification boundary and propagate verdict` step alone failed. The job-level red result demonstrates that a required positive failure is no longer silently tolerated by the aggregate oracle. This is the intended fail-closed behavior, not evidence that the repair is defective.

## Additional semantic classifications — exact main `2e67e8b08aaafdebc825d250ad28b5e60d1c61e2`
The next audit pass inspected further high-risk constructs against surrounding workflow semantics rather than counting tokens.

### `s005-attestation-authorization-policy.yml` — deliberate diagnostic suppression, not a job-verdict claim
The baseline repository verification is an ordinary fatal step. Three subsequent signer/source-ref/source-digest predicate-isolation steps use `continue-on-error: true`, but their names and structure make them observational discriminator probes rather than acceptance predicates. Three explicit wrong-policy controls are ordinary fatal shell steps and invert the verifier correctly (`if gh ...; then exit 1; fi`).

**ENGINEERING JUDGMENT:** classify the three predicate-isolation `continue-on-error` hits as **deliberate diagnostic suppression outside the final verdict path**. They must not be cited as PASS evidence for those individual predicates. No repair is justified unless the workflow's declared claim is strengthened to require those isolated predicates to succeed.

### `s005-offline-attestation-verification.yml` — explicit status capture + fail-closed propagation
The positive network-isolated verifier deliberately runs under `set +e`, stores stdout/stderr and `rc`, then exits with that exact `rc`; the step is `continue-on-error` only so evidence and negative controls can be preserved. A final `if: steps.offline_positive.outcome != 'success'` step exits 98. The two negative controls capture their verifier status and require nonzero with `test "$rc" -ne 0`.

**VALIDATION by code-path semantics, not execution re-award:** classify these selected-pattern hits as **intentional status capture followed by fail-closed propagation**. The existing hosted run `35826855911` remains the bounded execution evidence for the generic offline-attestation claim; this audit does not manufacture new execution evidence.

### `m006-flutter-safari-runtime-validation.yml` — protected pipelines and intentional setup status capture
Toolchain/log `tee` pipelines execute under `set -euxo pipefail`. SafariDriver/venv/pip setup intentionally omits `-e`, captures each producer status, and explicitly exits nonzero for every failed required setup phase. The semantic Safari oracle itself executes under `set -euxo pipefail`; its Python process raises nonzero on oracle timeout while `tee` preserves output.

**TRANSFER VALIDATION:** classify these paths as **protected pipeline/log capture** plus **intentional status capture followed by fail-closed propagation**. This is consistent with the already retained exact Safari runtime evidence; no new Mobile PASS is awarded here.

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

The S005 hosted regression proves fail-closed aggregate propagation under the observed failing positive condition. It does not establish why the historical attestation is unavailable or prove all other workflow paths semantically correct.

Static semantic classification can show that a construct is wired into a fail-closed path, but it does not replace execution evidence where a runtime claim requires it.

## RELATED DOMAIN CHECK
- Foundations: process exit status and shell pipeline semantics are relevant; no new Foundations claim.
- Architecture: CI evidence contracts are interfaces between validators and release/governance consumers.
- Mobile: M006 supplied natural false-green transfer and protected-pipeline/status-capture examples.
- Data: no data-specific claim.
- Quality: owner; complete inventory validated; semantic audit has a repaired hosted-regressed natural false-green and additional safe classifications.
- Systems: S005 supplies both the false-green transfer and valid diagnostic/status-capture contrasts.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this repository-internal CI corpus.
- Product source: no product behavior audited; this block targets `yhappcom/software-engineering-studio` only.

## HANDOFFS
- Systems: diagnostic continuation is acceptable only when every result required by the declared claim is folded into a fail-closed verdict; observational discriminator probes must not be promoted to PASS evidence.
- Mobile: retain navigation-aware semantic-oracle review separately from shell/workflow verdict propagation; current Safari runtime workflow demonstrates protected `tee` and explicit setup-status capture.

## OPEN
1. Continue semantic classification of remaining verdict-relevant hits, especially other `continue-on-error`, `set +e`, and `exit 0` paths.
2. Sample verdict-bearing commands that do not match the selected lexical patterns.
3. Repair any additional genuine false-green path and obtain exact-head regression evidence.
4. Only then decide whether the repository-wide semantic CI audit boundary can close.
