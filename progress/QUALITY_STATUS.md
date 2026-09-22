# Quality Specialist Status

Track: Quality, Testing & Reliability  
Prefix: `Q###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-23

## Mission
Build engineering capability to define correctness, design tests with valid oracles, reproduce failures, debug root causes, verify recovery, prevent regressions, and operate software with trustworthy observability.

## Current evidence

### Q001 — Correctness, specification, test oracle and reproducibility
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE.** Canonical: `research/quality/Q001_correctness_specification_oracle_reproducibility.md`.

### Q002 — Test levels, evidence boundaries and trade-offs
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q002_test_levels_evidence_boundaries.md`.

### Q003 — Determinism, nondeterminism, concurrency and flaky-test mechanics
**IN STUDY — two integrated Foundation blocks complete.** Canonical: `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md`. Shared-memory schedule failure plus deterministic 24-order timeout/complete/cancel/retry matrix retained; naive retry violated at-most-one logical effect in 12/24 schedules versus 0/24 with stable operation identity + bounded deduplication.

### Q004 — Property/model-based testing, invariant checking, mutation sensitivity and search strength
**IN STUDY — TWO EXECUTABLE BLOCKS COMPLETE.** Canonical: `research/quality/Q004_property_model_based_testing_invariants.md`, `research/quality/Q004_mutation_sensitivity_search_strength.md`. Bounded generation/shrinking plus exhaustive-vs-generated and deliberate mutation sensitivity evidence retained. Broader runtime/platform transfer remains OPEN.

### Q005 — Debugging, fault isolation and observability foundations
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q005_debugging_fault_isolation_observability.md`. Symptom/correlation/root-cause separation, identical-symptom injected defects, independent invariant and bounded causal intervention retained.

### Q006 — Fault injection, recovery verification and regression governance
**IN STUDY — process-crash recovery transfer + CI verdict-propagation failure→fixture-isolation→repair→hosted-regression chain complete.**  
Canonical: `research/quality/Q006_fault_injection_recovery_regression_governance.md`, `research/quality/Q006_real_crash_recovery_oracle_transfer.md`, `research/quality/Q006_ci_pipeline_exit_status_oracle_integrity.md`.

The retained Python/Linux/SQLite transfer uses actual child-process termination and fresh-process reopen to discriminate structural DB health from semantic recovery/replayability.

The M006 natural false-green exposed a separate regression-governance class: a verdict-bearing command piped through `tee` can preserve failure output while the enclosing pipeline reports success when producer exit status is not propagated. The first hosted Q006 discriminator then exposed its own isolation defect because `pipefail` contaminated the intended control. Repaired exact head `bd763b301752b3adebd36b963c06d064aec94ca8`, run `35792678785`, job `106964648579` completed success on Ubuntu 24.04.5 / GNU Bash 5.2.21. Observed control/treatment statuses were 0 and 23 respectively while both logs preserved `PRIMARY_ORACLE_FAIL`; artifact `10722128536`, digest `sha256:6b8e03ea4f4bd01d10334ddee40065b7fbc6c1acaf4b85cb2719baabfc61f903`.

**VALIDATION:** evidence preservation and verdict propagation are independently testable properties. **VALIDATION:** experimental controls must explicitly isolate inherited shell state when that state is the independent variable.

A repository code-search for `tee` returned incomplete results and even missed the known Q006 workflow; therefore no repository-wide absence claim was made. A complete semantic audit remains OPEN.

## Gate assessment
Quality Stage 1 remains **NOT PASS**. Q001-Q006 have professional Foundation boundaries and Q006 now includes a natural CI false-green, failed first discriminator, root-cause/isolation repair and successful hosted regression. Mobile/backend/storage-power/production release-gate transfer remains materially incomplete. Direct Dart JIT/AOT and Flutter runtime evidence exists in Foundations; older Quality notes saying the SDK/runtime is unavailable are stale and must not be used as the current blocker.

## Dependencies / handoffs
- **Foundations:** F001 direct Dart JIT/AOT and bounded Flutter Chrome/Safari execution exist; F003-F006 continue to supply state-space, concurrency, async and transport mechanisms.
- **Architecture:** contracts/invariants and externally meaningful progress state supply semantic recovery oracles.
- **Mobile:** M006 supplied the natural false-green case; future device/browser harnesses should preserve semantic exit status independently from log capture.
- **Data:** recovery oracles must compare semantic state with durable progress/replayability.
- **Systems:** CI/release gates must preserve verdict propagation and evidence artifacts as separate controls; shell-specific and production release-gate transfer remain required.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical evidence there changes this bounded Quality method.

## CHANGE WATCH / OPEN
- Repository-wide semantic audit for equivalent verdict-bearing pipelines remains OPEN; current code-search result was explicitly incomplete and is not an absence oracle.
- PowerShell/cmd/other CI-shell transfer remains OPEN.
- Q004 broader framework/platform transfer remains OPEN.
- Q006 actual Android/iOS process death, backend/cursor batches, combined network+process faults, filesystem/device/power faults and production release-gate evidence remain OPEN.
- Stronger cross-platform/runtime transfer remains required for Quality Foundation closure.

## Next work
Return to Balance Loop. Do not repeat synthetic Bash `pipefail` variants. Prefer a materially stronger evidence class: a trustworthy complete semantic CI audit, shell/platform transfer, physical/mobile failure boundary, exact-product/release-gate evidence, or another track's stronger Stage-1 gap.
