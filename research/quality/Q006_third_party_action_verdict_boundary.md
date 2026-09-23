# Q006 — Third-party action verdict boundary

Date: 2026-09-23
Lead: Quality
Status: IN STUDY — executable negative control committed; hosted observation pending

## Problem

The repository-wide selected-token inventory does not detect a distinct CI acceptance boundary: a workflow can delegate a verdict-bearing command to a JavaScript/container action. In that case correctness depends on whether the action propagates the delegated command's failure to the GitHub step verdict.

## Exact Studio target

Repository: `yhappcom/software-engineering-studio`
Prior semantic target: `5bdda29210ce52b863f31088a062eaaddf000b6e`
Executable-control introduction: `9ea9c97838d443c8fa81b04729e0447aee54c175`
Evidence date: 2026-09-23

Representative consumer: `.github/workflows/m002-android-process-death-storage-validation.yml`, which delegates its fail-fast oracle to `reactivecircus/android-emulator-runner@v2`.

## SOURCE — action implementation boundary

Inspection of the upstream `v2` action source showed user scripts executed through `@actions/exec`; execution errors are caught and passed to `core.setFailed`. This supports a fail-closed wrapper model, but the moving major tag is not immutable provenance and source reading is not runtime validation.

## SYNTHESIS

Verdict propagation has at least three layers: producer/oracle exit semantics; action-wrapper semantics; workflow/job acceptance semantics. A lexical audit of workflow shell cannot prove the action-wrapper layer.

## Executable negative control

Commit `9ea9c97838d443c8fa81b04729e0447aee54c175` adds `.github/workflows/q006-third-party-action-nonzero-propagation.yml`.

CLAIM: when the action successfully reaches the delegated script and that script intentionally exits 37, the action step exposes `outcome=failure` rather than normalizing the script to success.

TARGET: `reactivecircus/android-emulator-runner@v2` on an API-35 x86_64 emulator under `ubuntu-latest`.

INPUT: a delegated script that emits `Q006_INTENTIONAL_DELEGATED_FAILURE` then exits 37.

ORACLE: the action step uses `continue-on-error: true` only to preserve the downstream observation. The next ordinary fatal shell step requires `${{ steps.delegated.outcome }}` to equal `failure`; it also records the expected post-continue conclusion (`success`) to distinguish GitHub step outcome from conclusion semantics.

FAILURE MODEL: if the wrapper normalizes the delegated nonzero command to success, the downstream `outcome=failure` assertion fails. Emulator provisioning failure can also yield action outcome failure, so a green downstream assertion alone is not sufficient unless run logs show the intentional marker/script was actually reached.

VALIDATION: immediately after introduction, the Actions query for head `9ea9c978...` returned no run yet. Therefore no runtime PASS is awarded in this block. A later run must inspect both the action log for the intentional marker and the downstream outcome assertion before closing the executable-control gap.

## ENGINEERING JUDGMENT

The fixture improves oracle sensitivity but deliberately does not confuse infrastructure failure with delegated-script failure. The marker/reachability requirement is essential: merely observing action failure would be a false attribution risk.

## VALIDATION / OPEN

- OPEN: hosted run reaching `Q006_INTENTIONAL_DELEGATED_FAILURE` and then satisfying `outcome=failure`.
- OPEN: exact resolved action commit identity for the hosted run and historical M002 runs where verdict propagation is material.
- OPEN: semantic review of other third-party actions and GitHub-expression/action-output acceptance paths.
- No repository-wide semantic correctness PASS is awarded.

## RELATED DOMAIN CHECK

- Foundations: command/process exit semantics are prerequisite; no new Foundations claim.
- Architecture: wrapper boundary is an interface contract between oracle and CI runner.
- Mobile: M002 is the representative consumer; this control does not revalidate Android process-death behavior.
- Data: persistent-file semantics are not revalidated.
- Quality: owner; executable negative-control oracle added.
- Systems: moving action identity/pinning remains a supply-chain/provenance dependency.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this bounded CI-verdict mechanism.
- Product source/ref: not required; this block audits Studio CI only.

## HANDOFFS

### Quality → Systems
- Finding: verdict-bearing third-party actions require both wrapper-failure propagation and immutable/resolved dependency identity for release-grade evidence.
- Evidence: this note and executable control introduced at `9ea9c978...`.
- Impact: moving `@v2` remains CHANGE WATCH even if the runtime negative control later passes.
- Requested action: preserve resolved action identity and compare commit pinning when S004/S005 revisits supply-chain provenance.
- Status: OPEN.
