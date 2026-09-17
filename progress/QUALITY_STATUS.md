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

### Q004 — Property/model-based testing and invariant checking
**IN STUDY — SOURCE/MODEL + EXECUTABLE FIXTURE PREPARED; EXECUTION OPEN.**

Canonical: `research/quality/Q004_property_model_based_testing_invariants.md`  
Fixture: `research/quality/fixtures/Q004_model_property_sequence_shrinking.py`

Established from QuickCheck/model-based-testing literature and current Hypothesis stateful-testing documentation:
- property/invariant, generator/model transition system, search strategy and counterexample reduction are separate concerns;
- stateful generated tests can compare a SUT against an independent reference model and check invariants across action sequences;
- shrinking/reduction preserves a failure while simplifying its reproducer but does not prove root cause or global minimality;
- passing generated samples is counterexample-search evidence, not proof;
- bounded exhaustive enumeration remains preferable when the complete relevant state/event space is genuinely tractable.

A stdlib-only fixture was added to generate versioned update/delete delivery sequences, compare a naive arrival-order replica against a version-aware model, and greedily reduce the first violation to a 1-minimal sequence under single-command deletion. **Execution is OPEN:** available execution tools failed with infrastructure `GatewaySelectionError`, so no runtime output/verdict/environment is claimed. Creating executable code is not validation evidence.

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
- `Q003` — two integrated blocks complete; harness-vs-SUT flake isolation, larger runtime schedule exploration and runtime transfer OPEN.
- `Q004` — **IN STUDY / source-model block + prepared fixture; execution/mutation evidence OPEN**.
- `Q005` — first integrated block complete; crash/exception isolation, distributed observability, instrumentation perturbation and runtime transfer OPEN.
- `Q006` — first integrated block complete; real crash/restart/durable/network fault campaigns, combined faults, resource cleanup and release-gate transfer OPEN.

## Gate requirement
Quality Stage 1 remains **NOT PASS**. Q001-Q006 now all have at least a professional Foundation boundary, but Q004 lacks execution evidence and stronger real recovery/crash/runtime/platform transfer remains open. Reading or an unexecuted fixture cannot close the gate.

## Dependencies / handoffs
- Foundations: F003 complexity explains state-space growth; F004/F005/F006 provide concurrency/async/transport failure mechanisms; F001 direct Dart/Flutter execution remains OPEN.
- Architecture: A003 contracts/invariants are independent property/recovery-oracle candidates; terminal-state/recovery behavior remains semantic contract material.
- Mobile: M002 should inject exact process/lifecycle failure points and judge durable/recovered state rather than callback arrival alone; generated state-machine testing waits for real platform controls.
- Data: D006 supplies the current stale-update/delete transfer case; future delete/recreate/tombstone-GC semantics should define Data-owned invariants before Q004 generates histories.
- Systems: generated/release campaigns must bind exact artifact/build/environment, framework/seed and resource budget; security fault injection remains separate.
- Design Studio / Web Manager / Marketing Manager: considered; no current canonical evidence materially changes this bounded Quality method.

## Next work
First attempt to execute and mutation-check the prepared Q004 fixture when a trustworthy execution environment is available. If execution remains infrastructure-blocked, do not deepen source-only Q004 merely for continuity; use Balance Loop to advance an independent high-value gap such as Architecture Foundation closure or S002/S003. Direct Dart/Flutter execution remains first-attempt work whenever a trustworthy SDK environment becomes available.
