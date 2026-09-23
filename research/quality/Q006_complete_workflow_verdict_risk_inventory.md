# Q006 — Complete workflow verdict-risk inventory

Status: **IN STUDY — executable complete-inventory harness added; semantic review pending**
Evidence date: 2026-09-23
Lead: Quality; support: Systems

## Problem
Earlier repository code search for `tee` was incomplete and even missed a known workflow. It therefore could not support an absence claim about verdict-masking constructs. The repository currently contains many evidence-producing workflows, so a complete checkout-local inventory has higher reliability leverage than another synthetic `pipefail` variant.

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

## Why this is stronger than the prior search
The target is the checked-out repository tree at one exact ref, not an external search index. The manifest binds both the workflow count and every workflow byte digest, so later semantic review can state exactly what corpus it covered.

## VALIDATION
Hosted execution for exact head `d573b47f05a1d5f65daea94d4133dcc221973d2a` is **OPEN** at this note revision. No inventory completeness PASS or semantic audit PASS is awarded until a run is observed and its run-bound artifact is inspected.

After execution, every hit must be classified semantically. Examples:
- benign log capture protected by `set -o pipefail`;
- deliberate diagnostic suppression (`|| true`) outside a verdict path;
- intentional producer-status capture with explicit downstream fail-closed propagation;
- genuine false-green risk requiring repair.

The audit must also sample verdict-bearing commands without these lexical constructs; this scanner is a risk inventory, not a general shell/workflow verifier.

## FAILURE MODEL / LIMITS
The fixture can expose incomplete external search and provide a complete lexical corpus for the selected patterns. It cannot prove that shell state is inherited as expected, that GitHub expression conditions are correct, that third-party actions propagate their internal verdicts, or that semantic oracles themselves are valid.

## RELATED DOMAIN CHECK
- Foundations: process exit status and shell pipeline semantics are relevant; no new Foundations claim.
- Architecture: CI evidence contracts are interfaces between validators and release/governance consumers.
- Mobile: M006 supplied the natural false-green transfer that motivates this audit.
- Data: no data-specific claim.
- Quality: owner; complete inventory and semantic classification.
- Systems: CI/CD evidence and release-gate consumers materially depend on trustworthy verdict propagation.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this repository-internal CI corpus.
- Product source: no product behavior audited; this block targets `yhappcom/software-engineering-studio` only.

## HANDOFFS
- Systems: use the resulting classified corpus to decide which CI/release patterns are safe to reuse; do not treat inventory completion as release-gate correctness.
- Mobile: retain navigation-aware semantic-oracle review separately from shell verdict propagation.

## OPEN
1. Observe hosted run for exact head and inspect run-bound artifact.
2. Classify every inventory hit against surrounding shell/workflow semantics.
3. Repair any genuine false-green path and obtain regression evidence.
4. Only then decide whether the repository-wide selected-pattern audit boundary can close.
