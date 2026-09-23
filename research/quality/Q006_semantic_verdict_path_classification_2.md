# Q006 — Semantic verdict-path classification, pass 2

Status: **IN STUDY — ADDITIONAL HIGH-RISK PATHS CLASSIFIED; NO NEW FALSE-GREEN FOUND IN THIS PASS**
Evidence date: 2026-09-23
Lead: Quality; support: Mobile, Systems
Exact Studio ref inspected: `a87f71d5a4cb1632c21426aa6a6bf4b84093c5b9`

## Purpose
Continue the repository-wide semantic CI audit after the complete selected-pattern inventory and the repaired S005 aggregate false-green. This pass intentionally inspects surrounding control flow rather than treating lexical hits as defects.

## Selection rationale
The Balance Loop continues Q006 because its professional boundary is not complete, it has already exposed two natural verdict/oracle defects, and CI evidence integrity affects every specialist. Foundations direct Dart JIT/AOT and bounded Flutter browser execution are already validated, so the historical F001 blocker is stale. Equivalent Safari lifecycle or generic attestation variants would provide less leverage than closing verdict-integrity uncertainty.

## Classification 1 — M003 Keystore `trap` + `exit 0`
Target: `.github/workflows/m003-android-keystore-secure-storage-validation.yml`.

The independent Android oracle deliberately installs an EXIT trap. `finish()` captures `$?`, writes both `phase` and `oracle_rc` to `GITHUB_OUTPUT`, emits diagnostic logcat, and then exits 0. On its own, this would mask the producer failure. The workflow, however, has phase-specific failure steps and an unconditional final gate:

`if: always() && (steps.oracle.outputs.phase != 'complete' || steps.oracle.outputs.oracle_rc != '0')`

That gate exits nonzero. Success is announced only when phase is `complete` and `oracle_rc` is `0`.

**SYNTHESIS:** classify the oracle's `exit 0` as **intentional evidence/status handoff followed by fail-closed downstream propagation**, not a false-green. The decisive property is not the lexical `exit 0`; it is preservation of the original producer status plus a downstream acceptance predicate that rejects every nonzero or incomplete state.

**VALIDATION LIMIT:** this pass is static semantic review. It does not re-award the existing M003 runtime PASS or prove the third-party emulator action's internals.

## Classification 2 — M003 first-launch `tee` and diagnostics
Target: `.github/workflows/m003-first-launch-isolation.yml`.

The generated oracle runs with `set -uo pipefail`. Its verdict-bearing `adb shell am start ... | tee ... || fail am_start` therefore propagates a failing producer through the pipeline. Diagnostic `dumpsys ... | tee ... || true` and `logcat ... | tee ... || true` execute only inside an already-detected UI-observation failure branch immediately before `fail ui_observation_missing`.

**SYNTHESIS:** classify the first path as **protected pipeline/log capture** and the latter two as **diagnostic suppression after failure detection**. The `|| true` diagnostics cannot convert that branch to success because the explicit `fail` follows them.

## Classification 3 — M003 one-time background expiry observation
Target: `.github/workflows/m003-one-time-background-expiry-observation.yml`.

The emulator step is `continue-on-error: true` so semantic evidence can be uploaded even when the Python oracle fails. The Python oracle writes `HARNESS_FAILURE:<phase>` and re-raises on exceptions. Downstream `if: always()` steps preserve the evidence, explicitly fail on `HARNESS_FAILURE`, and finally require both an allowed bounded-observation verdict and `steps.emulator_oracle.outcome == 'success'`.

The allowed verdict `INCONCLUSIVE_WINDOW_EXHAUSTED` is not represented as proof of expiry; it is an explicit bounded-observation outcome. The workflow's final message states that window exhaustion is not converted into platform failure.

**ENGINEERING JUDGMENT:** classify this as **intentional diagnostic continuation + explicit fail-closed harness propagation**, with a separate three-valued semantic result (`observed`, `inconclusive`, `harness failure`). It would become a false-green only if an inconclusive outcome were later cited as evidence that expiry occurred. Existing status claims must therefore remain tied to the exact run that actually observed expiry, not merely to workflow success.

## Classification 4 — M006 Chromium service-worker workflow without selected risk tokens
Target: `.github/workflows/m006-browser-service-worker-validation.yml`.

This file is useful as the required non-pattern sample. Its three Node semantic validators are direct `run:` commands with step timeouts and no `continue-on-error`, `set +e`, `exit 0`, or `tee` masking around them. The cold-start step starts a background HTTP server, installs an EXIT cleanup trap, then directly executes `node validate_cold_start.mjs`. The cleanup trap suppresses only `kill` failure (`|| true`); it does not replace the Node validator's exit status.

**SYNTHESIS:** this sample has a straightforward fail-fast verdict path at workflow level. This does not validate the semantic correctness of each JavaScript oracle; it only shows that their process failures are not visibly converted into workflow success by the inspected wrapper.

## Result
No new genuine false-green was found in these four inspected paths. This is still meaningful audit progress because it separates three valid evidence-preservation patterns from defects and adds a verdict-bearing workflow that does not rely on the selected lexical risk constructs.

The repository-wide semantic-correctness boundary remains **OPEN**. The earlier S005 false-green repair remains the natural defect/regression evidence; this pass does not weaken or replace it.

## RELATED DOMAIN CHECK
- Foundations: shell/process exit status semantics are relevant; no new Foundations PASS.
- Architecture: validator output and downstream acceptance predicate form an evidence contract.
- Mobile: M003/M006 supplied the inspected natural workflows; no new Mobile runtime PASS is awarded.
- Data: not materially relevant to these wrapper paths.
- Quality: owner; semantic classification advanced.
- Systems: evidence preservation versus acceptance remains directly relevant to release/attestation workflows.
- Design Studio: considered; not materially relevant.
- Web Manager: considered; not materially relevant.
- Marketing Manager: considered; not materially relevant.
- Product repositories: not inspected; this pass audits Studio workflows only.

## HANDOFFS
- Mobile: when a fixture intentionally normalizes its own process exit for evidence transport, preserve the original status as explicit output and require an unconditional fail-closed consumer before treating the workflow as evidence.
- Systems: apply the same rule to release/signing/provenance pipelines; diagnostic continuation is not acceptance.

## OPEN / next boundary
1. Continue semantic classification of remaining `continue-on-error`, `set +e`, `exit 0`, `tee`, `trap`, and `|| true` hits that can influence a verdict.
2. Continue sampling verdict-bearing commands that contain none of the selected lexical tokens.
3. Check GitHub-expression conditions and third-party action result propagation where the acceptance predicate depends on outputs/outcomes.
4. Repair and hosted-regress any additional genuine false-green before considering repository semantic-audit closure.
5. Non-Bash shell/platform and production release-gate transfer remain OPEN.
