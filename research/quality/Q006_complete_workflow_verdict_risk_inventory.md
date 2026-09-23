# Q006 — Complete workflow verdict-risk inventory

Status: **IN STUDY — COMPLETE LEXICAL INVENTORY VALIDATED; SEMANTIC CLASSIFICATION OPEN**
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

**SYNTHESIS:** the hit count is deliberately not a defect count. Direct inspection already shows materially different semantics: ordinary version/log capture under `set -euo pipefail`; diagnostic `|| true`; explicit producer-status capture; fail-closed downstream checks; and negative tests where nonzero is the expected behavior. Therefore a blanket rewrite would destroy valid evidence patterns.

**TRANSFER VALIDATION:** the known repaired M006 Safari offline and service-worker workflows appear in the complete corpus with `set +e` setup capture and `tee` oracle paths. Their current oracle steps explicitly enable `pipefail` or capture/validate producer status, demonstrating why lexical presence alone cannot decide safety.

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

## RELATED DOMAIN CHECK
- Foundations: process exit status and shell pipeline semantics are relevant; no new Foundations claim.
- Architecture: CI evidence contracts are interfaces between validators and release/governance consumers.
- Mobile: M006 supplied the natural false-green transfer and current navigation-aware oracle examples.
- Data: no data-specific claim.
- Quality: owner; complete inventory now validated, semantic classification remains open.
- Systems: CI/CD evidence and release-gate consumers materially depend on trustworthy verdict propagation.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this repository-internal CI corpus.
- Product source: no product behavior audited; this block targets `yhappcom/software-engineering-studio` only.

## HANDOFFS
- Systems: use the classified corpus to decide which CI/release patterns are safe to reuse; do not treat inventory completion as release-gate correctness.
- Mobile: retain navigation-aware semantic-oracle review separately from shell verdict propagation.

## OPEN
1. Semantically classify every verdict-relevant hit against its enclosing step/job behavior.
2. Sample verdict-bearing commands that do not match the selected lexical patterns.
3. Repair any genuine false-green path and obtain exact-head regression evidence.
4. Only then decide whether the repository-wide semantic CI audit boundary can close.
