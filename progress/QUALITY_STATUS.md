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
**IN STUDY — repository semantic CI audit; delegated nonzero causality, immutable pinned-action regression, same-workflow expression/job-output composition, reusable/matrix output transfer, and skipped-producer output boundary VALIDATED at bounded hosted targets.**

Canonical includes `research/quality/Q006_complete_workflow_verdict_risk_inventory.md`, `Q006_third_party_action_verdict_boundary.md`, `Q006_expression_output_verdict_composition.md`, `Q006_reusable_workflow_output_verdict_boundary.md`, `Q006_matrix_reusable_workflow_output_aggregation.md`, and `Q006_skipped_job_output_boundary.md`.

Retained evidence includes the hosted Bash verdict discriminator, exact-head selected-pattern inventory, repaired S005 natural false-green, causal third-party action control with immutable pin, same-workflow semantic output composition, reusable-workflow transfer, and controlled matrix aggregation.

**VALIDATION — skipped producer / absent semantic output:** exact head `cc42697d60daf94e6c801bf68ccbbf61c28e3f03`, run `35987588099`, completed success. Producer job `107593783363` was `skipped` with no executed steps. Acceptance job `107593782370` succeeded only after asserting producer result `skipped`, empty semantic output, raw failure of an intentionally unsafe `verdict != FAIL` discriminator, and explicit refusal to treat the absent verdict as `PASS`. This validates at the bounded hosted target that non-execution/empty output is not affirmative semantic evidence and that negative-only acceptance can false-accept missing verdicts.

## Gate assessment
Quality Stage 1 remains **NOT PASS**. Q006 now covers shell/process propagation, causal third-party wrapper propagation, same-workflow semantic output composition, non-matrix reusable-workflow transfer, controlled matrix aggregation, and skipped-producer/empty-output behavior. Historical resolved action identity, remaining natural semantic classification, secret-redacted/cancelled paths, non-Bash/action-type transfer and production release-gate evidence remain incomplete.

## Dependencies / handoffs
- **Foundations:** direct Dart JIT/AOT and bounded Flutter Chrome/Safari execution exist; historical SDK blocker is stale.
- **Architecture:** result and semantic output are separate interface semantics; absent output must not become implicit PASS.
- **Mobile:** conditional Android/iOS/browser jobs require explicit required-member identity and fail-closed treatment of skipped required members.
- **Data:** recovery oracles must compare semantic state with durable progress/replayability.
- **Systems:** release/security gates should require positive semantic PASS from required producers; skipped/empty is non-evidence unless explicitly optional by contract.
- **Design Studio / Web Manager / Marketing Manager:** considered; not materially relevant to this bounded CI-verdict mechanism.

## CHANGE WATCH / OPEN
- Exact resolved action identity for historical causal and M002 runs remains OPEN; do not infer it from current tag state.
- Remaining selected-pattern semantic classification and natural verdict-bearing non-pattern paths remain OPEN.
- Secret-redacted outputs, cancellation, cross-repository reusable workflows, PowerShell/cmd/other action-type transfer and production release-gate evidence remain OPEN.

## Next work
Return to Balance Loop. S007 exact-product transfer remains higher live LogMate leverage when implementation becomes available. If still unavailable, do not repeat equivalent skipped/empty controls; prefer cancellation, secret-redaction, a natural repository defect, cross-repository/non-Bash transfer, or a production-oriented release gate.
