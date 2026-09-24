# Q006 — Matrix Reusable Workflow Output Aggregation Boundary

Status: **SOURCE / SYNTHESIS / BOUNDED HOSTED VALIDATION COMPLETE**  
Owner: Quality, Testing & Reliability  
Evidence date: 2026-09-24

## Problem
The previously validated non-matrix reusable-workflow boundary does not establish matrix behavior. GitHub applies a matrix-specific aggregation rule to reusable-workflow outputs, so a caller can receive one scalar output even though multiple successful matrix invocations emitted different semantic verdicts.

## SOURCE
GitHub Actions documentation checked 2026-09-24 states that jobs using a matrix strategy can call a reusable workflow. For a reusable workflow that sets an output and is executed with a matrix, the resulting output is taken from the last successful completing reusable workflow that actually sets a value. GitHub further specifies that an empty string from the last successful completion does not replace the previous successful completion's actual value.

Primary source: https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows

## SYNTHESIS
A matrix reusable-workflow output is an aggregation result, not a collection of every member verdict. Therefore a scalar semantic verdict exported from a matrix is unsafe as an implicit all-members acceptance oracle unless the workflow deliberately implements aggregation semantics that match the required property.

For binary release/security acceptance, each required matrix member should preferably fail when its semantic requirement fails, or a separate aggregation job should explicitly evaluate all required member evidence. Caller transport success alone is insufficient, and the matrix's scalar reusable output does not inherently mean `all(matrix members) passed`.

## EXECUTABLE CONTROL
Committed fixtures:
- `.github/workflows/q006-reusable-matrix-verdict-producer.yml`
- `.github/workflows/q006-reusable-matrix-output-verdict.yml`

Exact control head: `e407b88c47d64170dc6a565d2ed6112758fc55b7`.

The caller invokes two successful reusable-workflow matrix members:
- `PASS`, delayed 1 second;
- `FAIL`, delayed 6 seconds.

Both called workflows succeed as executions. The later successful `FAIL` member sets a nonempty output. The acceptance job independently requires:
1. matrix call result `success`;
2. aggregated `semantic_verdict == FAIL`;
3. transport-only acceptance can therefore still be green;
4. a semantic predicate requiring `PASS` fails under `continue-on-error`;
5. a final oracle requires that semantic-control outcome to be `failure`.

The delay is an experimental ordering aid, not a general scheduling guarantee.

## VALIDATION
Hosted run `35969760559` at exact head `e407b88c47d64170dc6a565d2ed6112758fc55b7` completed **success**. Run metadata binds the referenced reusable workflow to the same exact head.

Jobs:
- `call-matrix (PASS, 1) / producer` — job `107536467918` — success; emit step completed at 07:28:07Z;
- `call-matrix (FAIL, 6) / producer` — job `107536468186` — success; emit step completed at 07:28:13Z;
- `acceptance` — job `107536521104` — success.

The job API independently establishes the intended completion ordering: PASS member completed first, FAIL member completed later. The acceptance job's exact-value aggregation assertion completed successfully, so its observed aggregated reusable-workflow output was `FAIL`. The transport-success assertion also completed successfully. The semantic-control step is intentionally `continue-on-error`; GitHub's job summary reports that step as completed/success at the job-step layer, so its raw command exit is not independently visible through this API response. However, the following independent fail-closed oracle step completed successfully and its predicate requires `steps.semantic_control.outcome == failure`. Thus the control could not reach terminal job success unless the semantic PASS predicate had failed as intended.

**VERDICT — bounded PASS:** with two successful reusable-workflow matrix invocations that export different nonempty semantic verdicts, the caller receives the last successful completing nonempty value under this controlled ordering. Matrix transport success coexists with aggregated semantic `FAIL`; therefore transport success is not an all-members semantic acceptance oracle, and a scalar matrix reusable output is not inherently an `all` reduction.

Evidence boundary: this is a GitHub-hosted Studio control. It does not prove production release-gate correctness, arbitrary scheduling order, or behavior for empty/skipped/redacted outputs.

## FAILURE MODEL
Covers the risk that a release/security/test caller treats a matrix reusable-workflow's transport result or one aggregated scalar output as evidence that every matrix member semantically passed.

Does not establish skipped/empty/redacted output behavior, cancellation, cross-repository reusable workflows, production release gates, or product CI correctness.

## ALTERNATIVES
1. **Preferred for binary gates:** fail each matrix member internally on required semantic failure. GitHub then naturally composes job failure.
2. **Explicit aggregation:** publish per-member durable evidence and have a non-matrix aggregation job evaluate `all(required members)`, preserving identity of each member.
3. **Single scalar output:** acceptable only when its aggregation semantics are intentionally defined and validated; do not assume matrix reusable-workflow output means all-members acceptance.

## RELATED DOMAIN CHECK
- **Foundations:** execution success versus semantic completion remains the underlying distinction; no new prerequisite.
- **Architecture:** matrix outputs are API aggregation semantics and must be part of the interface contract.
- **Mobile:** materially relevant later for Android/iOS/browser build/test matrices, but no runtime claim here.
- **Data:** not materially relevant to this bounded CI mechanism.
- **Quality:** owns oracle composition and false-green prevention.
- **Systems:** release/security matrices should fail closed or use explicit all-member aggregation; provenance remains separately required.
- **Design Studio / Web Manager / Marketing Manager:** considered; not materially relevant.
- **Product:** no product repository was modified. Exact-product transfer must be performed against a recorded product ref when a real matrix gate is adopted.

## HANDOFFS
- **Systems/Delivery:** do not model a matrix reusable-workflow scalar output as an implicit `all` reduction. Prefer member failure or explicit aggregation for release/security gates.
- **Architecture:** document aggregation semantics when workflow outputs cross a matrix boundary.
- **Product CI:** transfer-test real build/test matrices; Studio control is not production evidence.

## OPEN / NEXT
Do not repeat this controlled nonempty-output ordering. Remaining materially different Q006 boundaries include empty/skipped/redacted outputs, cancellation, cross-repository reusable workflows, non-Bash/action-type transfer, remaining natural semantic classification, and production-oriented release gates. S007 exact LogMate transfer remains higher live-product priority as soon as product implementation becomes available.
