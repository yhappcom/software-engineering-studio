# Q006 — Reusable Workflow Output Verdict Boundary

Status: **SOURCE / SYNTHESIS / EXECUTABLE CONTROL COMMITTED — HOSTED VALIDATION OPEN**  
Owner: Quality, Testing & Reliability  
Evidence date: 2026-09-24

## Problem
A successful reusable-workflow call is a transport/execution result, not automatically the semantic acceptance verdict exported by that workflow. Release, security, test, or attestation workflows can therefore false-green if callers check only the called job result while ignoring a verdict-bearing workflow output.

## SOURCE
GitHub Actions documentation checked 2026-09-24 establishes that reusable workflows expose declared `on.workflow_call.outputs` mapped from called-workflow job outputs, and callers consume those outputs through the calling job's `needs.<job>.outputs`. GitHub also documents `needs.<job>.result` separately from `needs.<job>.outputs`, so execution result and exported semantic values are distinct interface fields.

GitHub further documents a matrix-specific reusable-workflow rule: when a reusable workflow with outputs is called through a matrix, the resulting workflow output comes from the last successful completing reusable workflow that actually sets a value. This makes matrix output aggregation a separate later boundary; it is not covered by the non-matrix control in this note.

Primary sources:
- https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
- https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax

## SYNTHESIS
A reusable workflow is an API boundary. A caller that needs semantic acceptance must validate the exported semantic contract, not infer it from `needs.<call>.result == success`.

This extends the already validated same-workflow Q006 expression/output result distinction across a materially different GitHub Actions boundary: `workflow_call`.

## EXECUTABLE CONTROL
Committed fixtures:
- `.github/workflows/q006-reusable-semantic-verdict.yml`
- `.github/workflows/q006-reusable-output-verdict-composition.yml`

Exact caller head: `ac6fee0a185912ecefd642a381c787d265496c51`.

The called reusable workflow intentionally exits successfully while exporting `semantic_verdict=FAIL`. The caller independently requires:
1. called-workflow result is `success`;
2. exported reusable-workflow output is exactly `FAIL`;
3. a semantic predicate requiring `PASS` fails under `continue-on-error`;
4. a final oracle requires that control step's outcome to be `failure`.

This design distinguishes successful workflow transport from semantic acceptance without converting the overall control into an expected-red run.

## VALIDATION
GitHub automatically created hosted run `35964842513` for exact head `ac6fee0a185912ecefd642a381c787d265496c51`. At the time of this record the run is **queued**. No executable PASS is awarded yet.

The run metadata already records the referenced reusable workflow at the same exact head, which binds the caller and called workflow source identity for this attempt. Completion, job steps, and semantic oracle execution remain to be inspected.

## FAILURE MODEL
This control targets:
- caller accepts reusable workflow solely because the called job completed successfully;
- semantic failure crosses `workflow_call` as data but is omitted from the caller acceptance predicate;
- reusable-workflow output mapping is absent/broken and therefore cannot satisfy the exact `FAIL` oracle.

It does not establish:
- matrix reusable-workflow output aggregation correctness;
- secret-redacted/skipped output behavior;
- cancellation/skipped called-workflow behavior;
- cross-repository reusable workflows;
- production release-gate correctness.

## ALTERNATIVE / TRADE-OFF
For binary release gates, the strongest design is often to make the called reusable workflow itself fail when semantic acceptance fails, reducing the chance that every caller must remember a second predicate. Verdict outputs remain useful when callers need diagnostics or multiple states, but then the caller must treat the output as a typed contract rather than informational text.

## RELATED DOMAIN CHECK
- **Foundations:** process/job success versus application semantic completion is the same general boundary already observed in F006; no new Foundations execution prerequisite.
- **Architecture:** reusable-workflow outputs are API contract values; transport success and semantic result have separate meaning.
- **Mobile:** no mobile runtime claim; reusable CI gates can later govern mobile build/test evidence.
- **Data:** not materially relevant to this bounded workflow mechanism.
- **Quality:** owns oracle composition and false-green prevention.
- **Systems:** reusable workflow provenance and release-gate acceptance are supply-chain/delivery concerns; exact source identity is preserved for this control.
- **Design Studio / Web Manager / Marketing Manager:** considered; not materially relevant.
- **Product:** LogMate exact latest observed ref remains `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`; no newer account-required implementation is available, so S007 exact-product transfer remains blocked and no product files were edited.

## HANDOFFS
- **Systems/Delivery:** release/security reusable workflows should fail internally on required semantic failure where practical; otherwise callers must explicitly validate verdict outputs.
- **Architecture:** treat workflow outputs as interface contracts with explicit accepted values, not as logging metadata.
- **Product CI:** when a product begins consuming reusable gates, transfer-test the caller acceptance predicate rather than assuming Studio control behavior proves product correctness.

## OPEN / NEXT
Inspect run `35964842513` after completion. If the called workflow succeeds, the `FAIL` value crosses the reusable boundary, and the final fail-closed oracle succeeds, close this bounded validation. Do not repeat equivalent non-matrix controls afterward; next materially different Q006 candidates are matrix output aggregation, skipped/redacted output behavior, cross-repository reusable workflows, or a natural production-oriented gate.
