# Quality Specialist Status

Track: Quality, Testing & Reliability  
Prefix: `Q###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-24

## Mission
Build engineering capability to define correctness, design tests with valid oracles, reproduce failures, debug root causes, verify recovery, prevent regressions, and operate software with trustworthy observability.

## Current evidence

### Q001 — Correctness, specification, test oracle and reproducibility
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Canonical: `research/quality/Q001_correctness_specification_oracle_reproducibility.md`.

### Q002 — Test levels, evidence boundaries and trade-offs
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q002_test_levels_evidence_boundaries.md`.

### Q003 — Determinism, nondeterminism, concurrency and flaky-test mechanics
**IN STUDY — two integrated Foundation blocks complete.** Canonical: `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md`.

### Q004 — Property/model-based testing, invariant checking, mutation sensitivity and search strength
**IN STUDY — TWO EXECUTABLE BLOCKS COMPLETE.** Canonical: `research/quality/Q004_property_model_based_testing_invariants.md`, `research/quality/Q004_mutation_sensitivity_search_strength.md`.

### Q005 — Debugging, fault isolation and observability foundations
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q005_debugging_fault_isolation_observability.md`.

### Q006 — Fault injection, recovery verification and regression governance
**IN STUDY — repository semantic CI audit; delegated nonzero causality, immutable pinned-action regression, same-workflow expression/job-output composition, reusable-workflow output transfer, and matrix reusable-output aggregation VALIDATED at bounded hosted targets.**  
Canonical includes `research/quality/Q006_complete_workflow_verdict_risk_inventory.md`, `research/quality/Q006_third_party_action_verdict_boundary.md`, `research/quality/Q006_expression_output_verdict_composition.md`, `research/quality/Q006_reusable_workflow_output_verdict_boundary.md`, and `research/quality/Q006_matrix_reusable_workflow_output_aggregation.md`.

Retained evidence includes the hosted Bash verdict discriminator, the exact-head 29-workflow/131-hit selected-pattern inventory, the repaired S005 natural false-green aggregate-verdict defect, causal third-party action control, immutable action pin regression, same-workflow semantic output composition, and non-matrix reusable-workflow output transfer.

**VALIDATION — matrix reusable output aggregation:** exact head `e407b88c47d64170dc6a565d2ed6112758fc55b7`, run `35969760559`, completed success. `PASS` member job `107536467918` succeeded and emitted first; `FAIL` member job `107536468186` succeeded and emitted later. Acceptance job `107536521104` succeeded only after asserting matrix transport `success`, exact aggregated output `FAIL`, and an independent fail-closed oracle requiring the semantic-PASS control's outcome to be `failure`. This directly validates GitHub's documented last-successful-nonempty matrix reusable-workflow output rule under controlled completion ordering. It also demonstrates that a scalar matrix output is not inherently an `all(matrix members)` reduction.

## Gate assessment
Quality Stage 1 remains **NOT PASS**. Q006 now covers shell/process propagation, causal third-party wrapper propagation, same-workflow semantic output composition, non-matrix reusable-workflow semantic output transfer, and controlled matrix reusable-output aggregation. Historical resolved action identity, remaining natural semantic classification, empty/skipped/redacted/cancelled output paths, non-Bash/action-type transfer and production release-gate evidence remain incomplete.

## Dependencies / handoffs
- **Foundations:** direct Dart JIT/AOT and bounded Flutter Chrome/Safari execution exist; historical SDK blocker is stale.
- **Architecture:** exported CI verdicts and matrix aggregation are interface semantics distinct from transport success; a scalar matrix output is not automatically an all-members contract.
- **Mobile:** build/test matrices for Android/iOS/browser should transfer-test member identity and aggregation rather than infer product coverage from one scalar output.
- **Data:** recovery oracles must compare semantic state with durable progress/replayability.
- **Systems:** binary release/security reusable workflows should preferably fail internally per required matrix member or use an explicit all-member aggregation gate; scalar matrix output plus transport success is insufficient.
- **Design Studio / Web Manager / Marketing Manager:** considered; not materially relevant to this bounded CI-verdict mechanism.

## CHANGE WATCH / OPEN
- Exact resolved action identity for historical causal and M002 runs remains OPEN; do not infer it from current tag state.
- Remaining selected-pattern semantic classification and natural verdict-bearing non-pattern paths remain OPEN.
- Empty/skipped/redacted reusable outputs, cancellation, cross-repository reusable workflows, PowerShell/cmd/other action-type transfer and production release-gate evidence remain OPEN.

## Next work
Return to Balance Loop. S007 exact-product transfer remains higher live LogMate leverage when implementation becomes available. If it is still unavailable, do not repeat equivalent nonempty matrix controls; prefer skipped/empty output behavior, a natural repository defect, cross-repository transfer, non-Bash action type, or a production-oriented release gate.
