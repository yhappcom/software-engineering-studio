# Q006 — Matrix Reusable Workflow Output Aggregation Boundary

Status: **SOURCE / SYNTHESIS / EXECUTABLE CONTROL COMMITTED — HOSTED VALIDATION OPEN**  
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

Current control head after caller creation: `e407b88c47d64170dc6a565d2ed6112758fc55b7`.

The caller invokes two successful reusable-workflow matrix members:
- `PASS`, delayed 1 second;
- `FAIL`, delayed 6 seconds.

Both called workflows are intended to succeed as executions. The later successful `FAIL` member sets a nonempty output. The acceptance job independently requires:
1. matrix call result `success`;
2. aggregated `semantic_verdict == FAIL`;
3. transport-only acceptance can therefore still be green;
4. a semantic predicate requiring `PASS` fails under `continue-on-error`;
5. a final oracle requires that semantic-control outcome to be `failure`.

The delay is an experimental ordering aid, not proof that GitHub scheduling will always produce the intended completion order. The exact hosted observation must be inspected before any PASS.

## VALIDATION
**OPEN.** At the time this note was created, no hosted run existed yet for exact head `e407b88c47d64170dc6a565d2ed6112758fc55b7`. Do not infer execution from committed YAML or from the official documented rule.

Required closure evidence:
- exact run/head identity;
- both matrix called jobs successful;
- observable member outputs/order sufficient to support the aggregation claim;
- acceptance log shows `MATRIX_RESULT=success`;
- acceptance log shows `AGGREGATED_VERDICT=FAIL`;
- semantic control outcome is `failure`;
- terminal marker `Q006_MATRIX_REUSABLE_OUTPUT_FAIL_CLOSED_PASS`.

If observed ordering differs, revise the fixture rather than reinterpret the oracle.

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
Wait for and inspect the hosted control. If it validates, close only this matrix aggregation boundary and move to a materially different class such as skipped/empty outputs, cross-repository transfer, non-Bash action types, or a natural production-oriented gate. If the hosted result contradicts the expected ordering/aggregation, preserve the contradiction and debug the harness or platform semantics before proceeding.
