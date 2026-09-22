# Quality Specialist Status

Track: Quality, Testing & Reliability  
Prefix: `Q###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-23

## Mission
Build engineering capability to define correctness, design tests with valid oracles, reproduce failures, debug root causes, verify recovery, prevent regressions, and operate software with trustworthy observability.

## Current evidence

### Q001 — Correctness, specification, test oracle and reproducibility
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed.** Canonical: `research/quality/Q001_correctness_specification_oracle_reproducibility.md`.

### Q002 — Test levels, evidence boundaries and trade-offs
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q002_test_levels_evidence_boundaries.md`.

### Q003 — Determinism, nondeterminism, concurrency and flaky-test mechanics
**IN STUDY — two integrated Foundation blocks complete.** Canonical: `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md`. Shared-memory schedule failure plus deterministic 24-order timeout/complete/cancel/retry matrix retained; naive retry violated at-most-one logical effect in 12/24 schedules versus 0/24 with stable operation identity + bounded deduplication.

### Q004 — Property/model-based testing, invariant checking, mutation sensitivity and search strength
**IN STUDY — TWO EXECUTABLE BLOCKS COMPLETE.** Canonical: `research/quality/Q004_property_model_based_testing_invariants.md`, `research/quality/Q004_mutation_sensitivity_search_strength.md`. Bounded generation/shrinking plus exhaustive-vs-generated and deliberate mutation sensitivity evidence retained. Broader runtime/platform transfer remains OPEN.

### Q005 — Debugging, fault isolation and observability foundations
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q005_debugging_fault_isolation_observability.md`. Symptom/correlation/root-cause separation, identical-symptom injected defects, independent invariant and bounded causal intervention retained.

### Q006 — Fault injection, recovery verification and regression governance
**IN STUDY — process-crash recovery transfer complete; CI verdict-propagation regression added and hosted execution pending.**  
Canonical: `research/quality/Q006_fault_injection_recovery_regression_governance.md`, `research/quality/Q006_real_crash_recovery_oracle_transfer.md`, `research/quality/Q006_ci_pipeline_exit_status_oracle_integrity.md`.

The retained Python/Linux/SQLite transfer uses actual child-process termination and fresh-process reopen to discriminate structural DB health from semantic recovery/replayability.

A natural M006 failure exposed a separate regression-governance class: a verdict-bearing command piped through `tee` can preserve failure output while the enclosing pipeline reports success when producer exit status is not propagated. Fixture `research/quality/fixtures/Q006_ci_pipeline_exit_propagation.sh` holds output constant and compares no-`pipefail` versus Bash `pipefail`; workflow `.github/workflows/q006-ci-pipeline-exit-propagation.yml`, exact target head `14f0d8e3e707695e5cb79e969f4163578536b494`, run `35792552545`. Run is still in progress, so **no executable PASS yet**.

## Gate assessment
Quality Stage 1 remains **NOT PASS**. Q001-Q006 have professional Foundation boundaries, but mobile/backend/storage-power/production release-gate transfer remains materially incomplete. Direct Dart JIT/AOT and Flutter runtime evidence now exists in Foundations; older Quality notes saying the SDK/runtime is unavailable are stale and must not be used as the current blocker.

## Dependencies / handoffs
- **Foundations:** F001 direct Dart JIT/AOT and bounded Flutter Chrome/Safari execution now exist; F003-F006 continue to supply state-space, concurrency, async and transport mechanisms.
- **Architecture:** contracts/invariants and externally meaningful progress state supply semantic recovery oracles.
- **Mobile:** M006 supplied the natural false-green case; future device/browser harnesses should preserve semantic exit status independently from log capture.
- **Data:** recovery oracles must compare semantic state with durable progress/replayability.
- **Systems:** CI/release gates must preserve verdict propagation and evidence artifacts as separate controls; shell-specific transfer remains required.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical evidence there changes this bounded Quality method.

## CHANGE WATCH / OPEN
- Q006 CI pipeline exit-propagation hosted run `35792552545` is pending; do not award PASS before terminal evidence.
- Repository-wide audit for equivalent verdict-bearing pipelines should inspect semantics rather than flag every pipeline mechanically.
- Q004 broader framework/platform transfer remains OPEN.
- Q006 actual Android/iOS process death, backend/cursor batches, combined network+process faults, filesystem/device/power faults and production release-gate evidence remain OPEN.
- Stronger cross-platform/runtime transfer remains required for Quality Foundation closure.

## Next work
First close the pending Q006 hosted regression and, if it succeeds, audit only verdict-bearing CI pipelines for the same false-green class. Then return to Balance Loop for a materially stronger evidence class rather than repeating synthetic shell variants.
