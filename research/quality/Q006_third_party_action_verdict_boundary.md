# Q006 — Third-party action verdict boundary

Date: 2026-09-23
Lead: Quality
Status: IN STUDY — bounded semantic classification, no new runtime PASS

## Problem

The repository-wide selected-token inventory does not detect a distinct CI acceptance boundary: a workflow can delegate a verdict-bearing command to a JavaScript/container action. In that case the workflow YAML may contain no `continue-on-error`, `set +e`, `|| true`, `tee`, `trap`, or `exit 0`; correctness depends on whether the action propagates the delegated command's failure to the GitHub step verdict.

## Exact Studio target

Repository: `yhappcom/software-engineering-studio`
Ref inspected: `5bdda29210ce52b863f31088a062eaaddf000b6e`
Evidence date: 2026-09-23

Representative workflow: `.github/workflows/m002-android-process-death-storage-validation.yml`.

The final emulator step delegates `bash "$RUNNER_TEMP/m002_oracle.sh"` to `reactivecircus/android-emulator-runner@v2`. The oracle itself is fail-fast (`set -euo pipefail`) and checks write observation, process disappearance after force-stop, changed PID after restart, recovered persistent value, and emits a final PASS marker only after those assertions.

## SOURCE — action implementation boundary

The action source at the referenced `v2` ref executes each parsed user script through `@actions/exec` using `sh -c`. Its custom-script block catches execution errors and calls `core.setFailed(...)`; its outer error path also calls `core.setFailed(...)`. Therefore, at the inspected upstream source ref, a delegated nonzero script is intended to mark the action failed rather than normalize the command to success.

This is stronger than assuming a third-party action propagates exit status merely because historical workflow runs were red/green. It is still not immutable provenance: the Studio workflow references the moving major tag `@v2`, not a full commit SHA.

## SYNTHESIS

Verdict propagation has at least three layers:

1. producer/oracle command exit semantics;
2. action wrapper semantics (`exec`/catch/`setFailed` or equivalent);
3. workflow/job acceptance semantics (`continue-on-error`, expressions, downstream aggregate predicates).

A lexical audit of workflow shell cannot prove layer 2. Third-party actions that execute verdict-bearing scripts are therefore a separate semantic-audit class.

## ENGINEERING JUDGMENT

For the inspected M002 wrapper boundary, the current upstream `v2` implementation is consistent with fail-closed propagation of the delegated oracle's nonzero exit. This classification is not a new M002 runtime PASS and does not prove every historical `@v2` resolution had identical semantics.

The mutable major tag creates a Systems/supply-chain dependency: future `v2` movement could alter wrapper behavior without changing Studio workflow source. Pinning to a reviewed commit is a stronger provenance control, but changing repository-wide dependency policy is outside this Quality block.

## VALIDATION / OPEN

- OPEN: executable negative-control fixture that deliberately returns nonzero through the exact third-party action and confirms the GitHub step/job fails at the current resolved action revision.
- OPEN: exact resolved commit identity for each historical `@v2` run where verdict propagation is material.
- OPEN: semantic review of other third-party actions that participate in acceptance, including artifact preservation and attestation actions.
- No repository-wide semantic correctness PASS is awarded.

## RELATED DOMAIN CHECK

- Foundations: command/process exit semantics are prerequisite; no new Foundations claim.
- Architecture: wrapper boundary is an interface contract between oracle and CI runner.
- Mobile: M002 is the representative consumer; no new Android behavior inferred.
- Data: M002 persistent-file semantics are not revalidated here.
- Quality: owns oracle/verdict propagation classification.
- Systems: action identity/pinning and supply-chain provenance materially affect stability of the verdict contract.
- Design Studio: not materially relevant.
- Web Manager: not materially relevant.
- Marketing Manager: not materially relevant.
- Product source/ref: not required; this block audits Studio CI, not a product implementation.

## HANDOFFS

### Quality → Systems
- Finding: verdict-bearing third-party actions form a semantic layer not covered by shell-token inventory; M002 currently depends on `reactivecircus/android-emulator-runner@v2` wrapper behavior.
- Evidence: this note; Studio ref `5bdda29210ce52b863f31088a062eaaddf000b6e`; upstream action source inspected 2026-09-23.
- Impact: mutable major-tag identity is a CHANGE WATCH / supply-chain provenance issue.
- Requested action: when S004/S005 revisits action provenance, compare moving major tags against commit-pinned alternatives and preserve resolved action identity for release-grade evidence.
- Status: OPEN.
