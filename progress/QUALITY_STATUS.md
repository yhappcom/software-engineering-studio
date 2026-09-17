# Quality Specialist Status

Track: Quality, Testing & Reliability  
Prefix: `Q###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-17

## Mission
Build engineering capability to define correctness, design tests with valid oracles, reproduce failures, debug root causes, verify recovery, prevent regressions, and operate software with trustworthy observability.

## Current evidence

### Q001 — Correctness, specification, test oracle and reproducibility
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed.** Canonical: `research/quality/Q001_correctness_specification_oracle_reproducibility.md`.

### Q002 — Test levels, evidence boundaries and trade-offs
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q002_test_levels_evidence_boundaries.md`.

### Q003 — Determinism, nondeterminism, concurrency and flaky-test mechanics
**IN STUDY — two integrated Foundation blocks complete.** Canonical: `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md`.

Established shared-memory schedule failure plus a deterministic 24-order timeout/complete/cancel/retry matrix. Naive retry violated an at-most-one logical-effect property in 12/24 schedules while stable logical-operation identity + bounded deduplication violated it in 0/24. Exhaustiveness is only for the bounded event alphabet.

### Q005 — Debugging, fault isolation and observability foundations
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/quality/Q005_debugging_fault_isolation_observability.md`.

Established symptom/correlation/root-cause separation with identical-symptom injected defects, correlated boundary observations, an independent invariant and a bounded causal intervention. Production/distributed/crash/runtime transfer remains OPEN.

### Q006 — Fault injection, recovery verification and regression governance
**IN STUDY — first integrated Foundation block complete.**

Canonical: `research/quality/Q006_fault_injection_recovery_regression_governance.md`  
Fixture: `research/quality/fixtures/Q006_fault_injection_recovery_regression.py`

Established with Python 3.13.5/Linux deterministic model evidence:
- fault observation and recovery correctness are distinct claims;
- a campaign injected `before_apply`, `after_apply_before_ack`, and `after_ack` failures and judged recovery by independent terminal-state semantics;
- stable logical-operation identity preserved the exactly-one bounded effect in 3/3 injected points after replay;
- a deliberate regression mutant that recorded but did not enforce operation identity produced balance 120 at both post-apply fault points, while the before-apply point still passed;
- therefore successful retry is not itself a recovery oracle;
- killing the deliberate mutant demonstrates sensitivity to this specific duplicated-effect regression, not mutation-testing completeness.

Evidence limit: deterministic single-process model only; no Dart/Flutter, real process death, durable storage, network/backend, combined faults, mobile or production release-gate claim.

## Initial queue
- `Q001` — substantial Foundation block complete.
- `Q002` — first integrated block complete.
- `Q003` — two integrated blocks complete; harness-vs-SUT flake isolation, larger model/property schedule exploration, runtime transfer OPEN.
- `Q004` — Property-based/model-based testing and invariant checking.
- `Q005` — first integrated block complete; crash/exception isolation, distributed observability, instrumentation perturbation and runtime transfer OPEN.
- `Q006` — **IN STUDY / first integrated block complete**; real crash/restart/durable/network fault campaigns, combined faults, resource cleanup and release-gate transfer OPEN.

## Gate requirement
Quality Stage 1 remains **NOT PASS**. Q001-Q006 now cover correctness/oracles, test-level boundaries, nondeterministic schedule reasoning, debugging/root-cause separation, and a first fault-injection/recovery/regression campaign. Property/model-based testing (Q004), stronger real recovery/crash evidence, and runtime/platform transfer remain open.

## Dependencies / handoffs
- Foundations: F004/F005/F006 provide concurrency/async/transport failure mechanisms; F001 direct Dart/Flutter execution remains OPEN after environment recheck 2026-09-17.
- Architecture: A003 contracts/invariants are independent recovery-oracle candidates; terminal-state/recovery behavior remains semantic contract material.
- Mobile: M002 should inject exact process/lifecycle failure points and judge durable/recovered state rather than callback arrival alone.
- Data: D005/D006 should reuse the Q006 campaign shape while retaining Data-owned restore/sync semantics and operation identity.
- Systems: release-gate recovery evidence must bind to exact artifact/build/environment; security fault injection remains separate.
- Design Studio / Web Manager / Marketing Manager: no current canonical evidence materially changes this bounded Quality method.

## Next work
Use Balance Loop. Q006 removes the untouched fault-injection/recovery/regression Foundation gap at bounded executable level. Strong next candidates are `M002` Android/iOS process lifecycle/background execution because Q006 now supplies a recovery-test method, or untouched `F002/F003` if their prerequisite leverage outranks platform work. `Q004` becomes increasingly valuable once a richer state machine exists. Direct Dart/Flutter execution remains first-attempt work whenever a trustworthy SDK environment becomes available.
