# Q006 — Skipped-job output boundary

Date: 2026-09-24
Status: **IN STUDY — HOSTED VALIDATION QUEUED**

## Problem / scope

Q006 already established that transport/job success and semantic outputs are separate verdict channels, including reusable and matrix workflows. This block targets a materially different failure class: a prerequisite job that is intentionally skipped before its output-producing step runs.

## SOURCE

GitHub Actions documents that `needs.<job_id>.result` can be `success`, `failure`, `cancelled`, or `skipped`, while `needs.<job_id>.outputs.<name>` is a separate string-valued channel. GitHub also documents that a job skipped by an `if` condition is marked skipped and can report success as a required check, and that downstream jobs normally skip after a skipped dependency unless an explicit condition such as `always()` permits continuation. Job outputs are evaluated at job completion; outputs that are not produced cannot be treated as affirmative semantic evidence.

Primary sources checked 2026-09-24:
- GitHub Docs, Contexts reference (`needs` context).
- GitHub Docs, Using jobs in a workflow (dependency skip propagation / `always()`).
- GitHub Docs, Using conditions to control job execution (skipped-job check behavior).
- GitHub Docs, Workflow syntax (`jobs.<job_id>.outputs`).

## SYNTHESIS

A downstream acceptance gate must not interpret an absent verdict from a skipped producer as semantic PASS. Transport/check presentation, dependency result, and semantic verdict are distinct channels. For a required semantic gate, `PASS` should be positively established; missing/empty output, skipped producer, failure, or cancellation must remain non-PASS unless the product/release contract explicitly defines another safe state.

## Failure model

Dangerous consumer pattern: accept whenever `semantic_verdict != FAIL`. If the producer is skipped and emits no verdict, an empty/missing value satisfies that negative predicate and can create a false acceptance.

Safer predicate: require the producer state and semantic verdict expected by the contract, e.g. producer result `success` **and** verdict exactly `PASS`. A skipped producer is not semantic evidence.

## Executable control

Fixture: `.github/workflows/q006-skipped-job-output-boundary.yml`
Exact head: `cc42697d60daf94e6c801bf68ccbbf61c28e3f03`
Hosted run: `35987588099`
Environment: GitHub-hosted `ubuntu-latest` requested by workflow.

The `producer` job is deliberately skipped with `if: ${{ false }}` before its output step can execute. The `acceptance` job uses `if: ${{ always() }}` and checks three independent properties:

1. producer result is exactly `skipped`;
2. semantic output is empty;
3. an intentionally unsafe `!= FAIL` consumer reaches the false-acceptance discriminator and fails, after which the final oracle requires that failure and refuses to call the missing verdict `PASS`.

## VALIDATION

**OPEN.** At record time run `35987588099` is queued. No PASS is awarded. The intended observations above remain hypotheses until the hosted run completes and job/step evidence is inspected.

## ENGINEERING JUDGMENT

This boundary has high reuse value for optional build/test/deploy jobs, path-filtered jobs, feature/platform matrices, and release workflows. It is especially important where branch protection can display a skipped job as a successful required check while no semantic validation actually ran.

## RELATED DOMAIN CHECK

- Foundations: execution/non-execution distinction applies; no new Foundations canonical conclusion required.
- Architecture: result and semantic output are separate interface fields; missing output must not be conflated with a valid domain state.
- Mobile: platform-specific build/test jobs can be skipped by conditions; release coverage must preserve member identity.
- Data: not materially changed by this bounded CI mechanism.
- Quality: owning track; extends Q006 with a distinct skipped-execution failure class.
- Systems/Delivery: release/security gates must fail closed when a required producer did not execute.
- Design Studio: not materially relevant.
- Web Manager: not materially relevant to this bounded mechanism.
- Marketing Manager: not materially relevant.
- Product source: LogMate exact implementation was rechecked; `yhappcom/logmate → main → 7551e1ca9e07df0b99e88aa03c8a56be03d8b2d3 → declared 1.0.0+1 → evidence 2026-09-24`; production identity unknown. No newer S007 implementation exists, so product transfer was not fabricated.

## HANDOFFS

- Systems/Delivery: treat required skipped producers as non-evidence; do not approve release/security semantics from check presentation alone.
- Mobile: when Android/iOS/Web jobs are conditional, acceptance must distinguish intentionally optional members from required members that failed to execute.
- Architecture: model absent verdict explicitly rather than encoding it as implicit PASS.

## OPEN / CHANGE WATCH

- Inspect hosted run `35987588099` after completion; preserve exact job/step observations before upgrading this block.
- Cancellation remains a distinct Q006 failure class.
- Secret-redacted outputs are distinct from skipped outputs and require separate evidence.
- Cross-repository reusable workflows and production release-gate transfer remain OPEN.
