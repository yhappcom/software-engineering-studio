# Q006 — CI pipeline exit-status oracle integrity

Status: **BOUNDED EXECUTABLE REGRESSION COMPLETE**
Date: 2026-09-23
Lead: Quality; support: Systems

## Problem

The M006 Safari offline cold-start investigation exposed a real validation defect: a semantic oracle was piped through `tee`, but the shell pipeline did not propagate the producer's non-zero exit status. A green CI step could therefore coexist with a failed primary oracle. This note promotes the mechanism into reusable Quality knowledge rather than treating it as Safari-specific.

## SOURCE / mechanism

In a shell pipeline, the pipeline's status is not automatically evidence that every component succeeded. The validation contract must preserve the primary oracle's verdict through any logging/presentation stage. For Bash-based GitHub Actions steps that intentionally pipe an oracle through `tee`, `pipefail` is one valid mechanism; an explicit capture/check of the producer status is another. The engineering requirement is verdict propagation, not a preference for one shell idiom.

## FAILURE CASE and executable discriminator

Fixture: `research/quality/fixtures/Q006_ci_pipeline_exit_propagation.sh`.

The synthetic primary oracle prints `PRIMARY_ORACLE_FAIL` and exits 23. Two structurally matched cases are exercised:

1. pipeline with `pipefail` explicitly disabled: producer output is preserved by `tee`, while the observed pipeline status is 0 because the final `tee` succeeds;
2. pipeline with Bash `pipefail` enabled: the same producer/output path returns 23.

The fixture independently asserts both exit statuses and that both logs contain the same failure payload. This separates **log preservation** from **verdict propagation**.

The first hosted attempt at exact head `14f0d8e3e707695e5cb79e969f4163578536b494`, run `35792552545`, exposed a fixture-isolation defect: inherited `pipefail` contaminated the intended no-`pipefail` control. That failure is retained rather than discarded.

Repair exact head: `bd763b301752b3adebd36b963c06d064aec94ca8`.
Hosted regression run: `35792678785`, job `106964648579`, terminal **success** on GitHub-hosted `ubuntu-24.04`; recorded GNU Bash 5.2.21 and Ubuntu 24.04.5. The semantic step observed:

- `without_pipefail_rc=0`
- `with_pipefail_rc=23`
- both payloads equal `PRIMARY_ORACLE_FAIL`
- final sentinel `Q006_CI_PIPELINE_EXIT_PROPAGATION_PASS`

Run-bound artifact: `10722128536`, digest `sha256:6b8e03ea4f4bd01d10334ddee40065b7fbc6c1acaf4b85cb2719baabfc61f903`.

**VALIDATION:** under this exact Bash/GitHub Actions environment, log preservation through `tee` is independent of propagation of the producer's non-zero verdict, and explicit `pipefail` changes the pipeline status from 0 to the producer failure 23 while preserving identical failure output.

## SYNTHESIS

A CI log/artifact can truthfully contain the primary oracle's failure output while the enclosing step is falsely green. Therefore evidence preservation and verdict propagation are independent properties and both must be validated. A later grep for a positive sentinel can strengthen the contract but cannot replace propagation of unexpected producer failures unless the sentinel itself is complete for the claim.

The regression also demonstrates a second Quality rule: a failure experiment must isolate the intended independent variable. A fixture that accidentally inherits the treatment into its control can produce a misleading failure even when the underlying mechanism is understood correctly.

## ENGINEERING JUDGMENT

For executable validation pipelines, prefer a fail-closed pattern that combines:

- primary process exit propagation (`pipefail` or explicit producer-status check);
- non-empty evidence assertion when an artifact is required;
- explicit semantic verdict assertion where a bounded PASS sentinel exists;
- `if: always()` evidence upload for failure diagnosis.

Do not infer that every workflow lacking an explicit `set -o pipefail` is defective: GitHub Actions shell invocation and script boundaries must be inspected, and pipelines that do not carry a primary verdict have different semantics.

## Repository audit boundary

A follow-up code-search attempt for `tee` in `.github/workflows` returned no indexed matches while reporting incomplete results. That search result is not sufficient evidence that no equivalent pipelines exist. The known Q006 workflow itself contains `tee`, demonstrating why an incomplete search index cannot be used as a repository-wide absence oracle.

**OPEN:** perform a semantic workflow audit only when a trustworthy complete retrieval/search mechanism is available; inspect whether a pipeline actually carries a verdict before classifying it. Do not convert an incomplete code-search result into PASS.

## VALIDATION / OPEN

- **VALIDATION COMPLETE:** hosted Ubuntu/Bash execution of the repaired exact fixture at run `35792678785`.
- **OPEN:** repository-wide semantic audit for equivalent verdict-bearing pipelines remains incomplete because current code-search evidence was explicitly incomplete.
- **OPEN:** transfer to PowerShell/cmd/other CI shells requires shell-specific validation rather than assuming Bash behavior.
- **OPEN:** production/release-gate transfer remains absent.

## RELATED DOMAIN CHECK

- Foundations: shell process exit status and pipeline composition are the underlying execution mechanism; direct Dart/Flutter availability is no longer a blocker.
- Architecture: not materially relevant to the bounded shell mechanism, except that validation is an external evidence boundary.
- Mobile: M006 supplied the natural failure that motivated this reusable study; no new mobile-runtime claim is made.
- Data: not materially relevant.
- Quality: owns oracle integrity, false-green prevention, failure evidence, regression governance, and experimental isolation.
- Systems: CI/CD owns shell/runtime/environment identity and release-gate propagation; handoff required.
- Design Studio / Web Manager / Marketing Manager: considered; no evidence there changes this mechanism.
- Product repositories: no product behavior audited in this block.

## HANDOFFS

- Systems: when CI/release evidence uses pipelines for verdict-bearing commands, audit exit-status propagation and evidence preservation as separate controls. Canonical note: this file; repaired exact head/run/job/artifact above. Do not generalize to non-Bash shells without transfer validation.
- Mobile: M006's prior false-green is now a reusable Quality regression class; future browser/device harnesses should preserve primary semantic exit status independently from log capture.
- Quality: retain the failed first hosted attempt as experimental-isolation evidence; do not erase failed fixture design from the regression chain.
