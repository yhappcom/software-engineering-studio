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
**IN STUDY — TWO EXECUTABLE BLOCKS COMPLETE.**  
Canonical: `research/quality/Q004_property_model_based_testing_invariants.md`, `research/quality/Q004_mutation_sensitivity_search_strength.md`  
Fixtures: `research/quality/fixtures/Q004_model_property_sequence_shrinking.py`, `research/quality/fixtures/Q004_mutation_exhaustive_generated_comparison.py`

First block: seed `20260917` generated and reduced the stale-update-after-delete counterexample to deterministic `delete_v3 → update_v2`, 1-minimal under single-command deletion.

Second block, Python 3.13.5/Linux 2026-09-18: exact enumeration of the 3-event alphabet for lengths 1..4 covered all 120 bounded sequences. An arrival-order mutant disagreed with the independent version-aware oracle on 61/120 sequences; an ignore-delete mutant on 86/120. A deliberately small generated campaign (seed `20260919`, 3 cases) killed ignore-delete once but missed arrival-order entirely, while the retained deterministic regression killed arrival-order. This isolates search/input strength from property/oracle strength and demonstrates why generated sampling is not bounded exhaustiveness.

Evidence limit: mutation killing and exhaustive-to-bound are not global correctness, mutation-score sufficiency, real sync behavior, or Dart/Flutter evidence. Direct runtime/platform transfer remains OPEN.

### Q005 — Debugging, fault isolation and observability foundations
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q005_debugging_fault_isolation_observability.md`. Symptom/correlation/root-cause separation, identical-symptom injected defects, independent invariant and bounded causal intervention retained.

### Q006 — Fault injection, recovery verification and regression governance
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q006_fault_injection_recovery_regression_governance.md`. Three-point fault campaign, semantic recovery oracle and deliberate idempotency-regression mutant retained.

## Gate assessment
Quality Stage 1 remains **NOT PASS**. Q001-Q006 all have professional Foundation boundaries. Q004's previously explicit mutation-sensitivity and exhaustive-vs-generated gaps are now closed at bounded Python-model level, but real crash/restart/durable/network/mobile evidence and Dart/Flutter/runtime transfer remain materially incomplete. Reading, mutation score, or bounded enumeration cannot close the track.

## Dependencies / handoffs
- **Foundations:** F003 explains state-space growth; F004/F005/F006 supply concurrency/async/transport failure mechanisms; F001 direct Dart/Flutter execution remains OPEN.
- **Architecture:** A003 contracts/invariants are independent property/recovery-oracle candidates.
- **Mobile:** exact process/lifecycle/PWA fault controls and durable-state oracles are required before transferring the method.
- **Data:** D006 supplied the stale-update/delete class; exact enumeration is preferred when a synchronization submodel is genuinely tractable, with generated search for larger spaces and deterministic regressions for known failures.
- **Systems:** CI mutation/generated campaigns must bind artifact/environment/seed/framework and resource budget; mutation score alone is not a release oracle.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical evidence there changes this bounded Quality method.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter execution remains unavailable after environment recheck 2026-09-18; Python 3.13.5 is available.
- Q004 real Dart/Flutter framework transfer, equivalent-mutant/operator design and real persistence/network/process-death transfer remain OPEN.
- Stronger real recovery/crash/runtime/platform transfer remains required for Quality Foundation closure.

## Next work
Return to Balance Loop. Q004's two named executable evidence gaps are now closed at bounded model level, so do not deepen it merely for continuity. Strong independent candidates are `A005` repeated-change/evolution evidence, `A006` executable ADR-governance validation, or targeted real platform/product transfer when trustworthy runtime/device infrastructure becomes available. Direct Dart/Flutter execution remains first-attempt work whenever a trustworthy SDK environment becomes available.
