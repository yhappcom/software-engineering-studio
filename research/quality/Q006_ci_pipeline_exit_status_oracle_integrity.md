# Q006 — CI pipeline exit-status oracle integrity

Status: **IN STUDY — executable regression pending**
Date: 2026-09-23
Lead: Quality; support: Systems

## Problem

The M006 Safari offline cold-start investigation exposed a real validation defect: a semantic oracle was piped through `tee`, but the shell pipeline did not propagate the producer's non-zero exit status. A green CI step could therefore coexist with a failed primary oracle. This note promotes the mechanism into reusable Quality knowledge rather than treating it as Safari-specific.

## SOURCE / mechanism

In a shell pipeline, the pipeline's status is not automatically evidence that every component succeeded. The validation contract must preserve the primary oracle's verdict through any logging/presentation stage. For Bash-based GitHub Actions steps that intentionally pipe an oracle through `tee`, `pipefail` is one valid mechanism; an explicit capture/check of the producer status is another. The engineering requirement is verdict propagation, not a preference for one shell idiom.

## FAILURE CASE and executable discriminator

Fixture: `research/quality/fixtures/Q006_ci_pipeline_exit_propagation.sh`.

The synthetic primary oracle prints `PRIMARY_ORACLE_FAIL` and exits 23. Two structurally matched cases are exercised:

1. pipeline without `pipefail`: producer output is preserved by `tee`, but the observed pipeline status is expected to be 0 because the final `tee` succeeds;
2. pipeline with Bash `pipefail`: the same producer/output path is expected to return 23.

The fixture independently asserts both exit statuses and that both logs contain the same failure payload. This separates **log preservation** from **verdict propagation**.

Workflow: `.github/workflows/q006-ci-pipeline-exit-propagation.yml`.
Exact target head: `14f0d8e3e707695e5cb79e969f4163578536b494`.
Run: `35792552545`.
At note creation the run is still in progress, so no PASS is awarded.

## SYNTHESIS

A CI log/artifact can truthfully contain the primary oracle's failure output while the enclosing step is falsely green. Therefore evidence preservation and verdict propagation are independent properties and both must be validated. A later grep for a positive sentinel can strengthen the contract but cannot replace propagation of unexpected producer failures unless the sentinel itself is complete for the claim.

## ENGINEERING JUDGMENT

For executable validation pipelines, prefer a fail-closed pattern that combines:

- primary process exit propagation (`pipefail` or explicit producer-status check);
- non-empty evidence assertion when an artifact is required;
- explicit semantic verdict assertion where a bounded PASS sentinel exists;
- `if: always()` evidence upload for failure diagnosis.

Do not infer that every workflow lacking an explicit `set -o pipefail` is defective: GitHub Actions shell invocation and script boundaries must be inspected, and pipelines that do not carry a primary verdict have different semantics.

## VALIDATION / OPEN

- **VALIDATION:** hosted Ubuntu execution of the exact fixture is pending at run `35792552545`.
- **OPEN:** repository-wide workflow audit for equivalent verdict-bearing pipelines should follow only after the mechanism regression succeeds; avoid regex-only accusations without inspecting command semantics.
- **OPEN:** transfer to PowerShell/cmd/other CI shells requires shell-specific validation rather than assuming Bash behavior.

## RELATED DOMAIN CHECK

- Foundations: shell process exit status and pipeline composition are the underlying execution mechanism; direct Dart/Flutter availability is no longer a blocker.
- Architecture: not materially relevant to the bounded shell mechanism, except that validation is an external evidence boundary.
- Mobile: M006 supplied the natural failure that motivated this reusable study; no new mobile-runtime claim is made.
- Data: not materially relevant.
- Quality: owns oracle integrity, false-green prevention, failure evidence, and regression governance.
- Systems: CI/CD owns shell/runtime/environment identity and release-gate propagation; handoff required.
- Design Studio / Web Manager / Marketing Manager: considered; no evidence there changes this mechanism.
- Product repositories: no product behavior audited in this block.

## HANDOFFS

- Systems: when CI/release evidence uses pipelines for verdict-bearing commands, audit exit-status propagation and evidence preservation as separate controls. Canonical note: this file; exact Studio head/run above. Do not generalize to non-Bash shells without transfer validation.
- Mobile: M006's prior false-green is now a reusable Quality regression class; future browser/device harnesses should preserve primary semantic exit status independently from log capture.
