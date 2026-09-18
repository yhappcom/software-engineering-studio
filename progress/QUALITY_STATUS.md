# Quality Specialist Status

Track: Quality, Testing & Reliability  
Prefix: `Q###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-18

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
**IN STUDY — TWO EXECUTABLE BLOCKS COMPLETE.** Canonical: `research/quality/Q004_property_model_based_testing_invariants.md`, `research/quality/Q004_mutation_sensitivity_search_strength.md`. Bounded generation/shrinking plus exhaustive-vs-generated and deliberate mutation sensitivity evidence retained. Direct runtime/platform transfer remains OPEN.

### Q005 — Debugging, fault isolation and observability foundations
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q005_debugging_fault_isolation_observability.md`. Symptom/correlation/root-cause separation, identical-symptom injected defects, independent invariant and bounded causal intervention retained.

### Q006 — Fault injection, recovery verification and regression governance
**IN STUDY — model block + real process-crash recovery-oracle transfer complete.**  
Canonical: `research/quality/Q006_fault_injection_recovery_regression_governance.md`, `research/quality/Q006_real_crash_recovery_oracle_transfer.md`.  
Fixtures: `research/quality/fixtures/Q006_fault_injection_recovery_regression.py`, `research/quality/fixtures/Q006_real_crash_recovery_oracle.py`.

The new Python 3.13.5/Linux/SQLite transfer uses actual child-process termination and fresh-process reopen. Unsafe cursor-first publication reopened with entity `(100,1)`, cursor `1`, no modeled replay, and `integrity_check=ok`: the structural oracle passed while the independent semantic recovery oracle failed. A single transaction terminated before COMMIT reopened at entity `(100,1)`, cursor `0`, preserving replayability; both structural and semantic oracles passed. This closes Q006's named real process kill/restart + durable-storage recovery gap at this bounded platform/context, not at Dart/Flutter/mobile/backend/production level.

## Gate assessment
Quality Stage 1 remains **NOT PASS**. Q001-Q006 all have professional Foundation boundaries. Q004 has bounded mutation/search-strength evidence and Q006 now has real process crash/restart + persistent-storage oracle discrimination. Direct Dart/Flutter/mobile/runtime transfer, real backend/network combinations, lower-layer storage/power faults and production release-gate evidence remain materially incomplete.

## Dependencies / handoffs
- **Foundations:** F003/F004/F005/F006 supply state-space, concurrency, async and transport mechanisms; F001 direct Dart/Flutter remains OPEN.
- **Architecture:** contracts/invariants and externally meaningful progress state supply semantic recovery oracles.
- **Mobile:** reproduce structural-vs-semantic recovery discrimination on the exact Flutter persistence stack under process death.
- **Data:** D006 supplied the cursor/effect invariant and stronger crash boundary; recovery oracles must compare semantic state with durable progress/replayability.
- **Systems:** release recovery gates must bind artifact/environment identity and must not substitute DB health/process liveness for semantic recovery.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical evidence there changes this bounded Quality method.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter execution remains unavailable after environment recheck 2026-09-18; Python 3.13.5 is available.
- Q004 real Dart/Flutter framework transfer and real persistence/network/process-death transfer beyond the bounded models remain OPEN.
- Q006 actual Android/iOS process death, backend/cursor batches, combined network+process faults, filesystem/device/power faults and production release-gate evidence remain OPEN.
- Stronger cross-platform/runtime transfer remains required for Quality Foundation closure.

## Next work
Return to Balance Loop. Q006's named real process kill/restart + durable-storage recovery gap is now closed at bounded Python/Linux/SQLite level. Do not repeat equivalent local crash variants. Direct Dart/Flutter execution remains first-attempt work whenever a trustworthy SDK appears; otherwise select another track's strongest real transfer/evidence gap or a materially different Q006 failure mechanism such as combined transport+restart only when the infrastructure genuinely changes the failure class.
