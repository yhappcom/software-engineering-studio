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
**IN STUDY — two integrated Foundation blocks complete.**

Canonical: `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md`  
Fixtures: `research/quality/fixtures/Q003_concurrency_schedule_flake.py`, `research/quality/fixtures/Q003_async_event_order_matrix.py`

Established:
- one observed schedule cannot establish schedule-independent correctness;
- widened shared read/modify/write reproduced lost updates while Lock comparison satisfied the bounded invariant;
- explicit async event-order enumeration explored all 24 permutations of timeout/original-complete/cancel/retry in the bounded model;
- naive retry violated an at-most-one logical-effect property in 12/24 schedules;
- stable logical operation identity + bounded deduplication violated it in 0/24 schedules;
- exhaustive schedule enumeration is evidence only for the explicitly bounded event alphabet, not a real network/runtime proof.

### Q005 — Debugging, fault isolation and observability foundations
**IN STUDY — first integrated Foundation block complete.**

Canonical: `research/quality/Q005_debugging_fault_isolation_observability.md`  
Fixture: `research/quality/fixtures/Q005_fault_isolation_observability.py`

Established with current OpenTelemetry source semantics plus Python 3.13.5 executable evidence:
- symptom, correlation and root cause are distinct claims;
- two independent injected defects produced the identical final symptom (`11`) in the bounded pipeline;
- final-output-only evidence could not discriminate the causal stage;
- correlated boundary observations plus an independent normalize invariant isolated the first violated contract;
- disabling the injected defect restored the final oracle in the bounded intervention;
- telemetry correlation supports investigation but does not itself establish causation;
- observability should preserve discriminating semantic state/identity where needed, while instrumentation perturbation and privacy/security remain separate concerns.

Evidence limit: deterministic single-process Python model only; no production telemetry, distributed clocks, sampling/drop behavior, crash dump, Flutter DevTools, native symbolication or automated causal-inference claim.

## Initial queue
- `Q001` — substantial Foundation block complete.
- `Q002` — first integrated block complete.
- `Q003` — two integrated blocks complete; harness-vs-SUT flake isolation, larger model/property schedule exploration, runtime transfer OPEN.
- `Q004` — Property-based/model-based testing and invariant checking.
- `Q005` — **IN STUDY / first integrated block complete**; crash/exception isolation, distributed observability, instrumentation perturbation and runtime transfer OPEN.
- `Q006` — Fault injection, recovery verification and regression governance.

## Gate requirement
Quality Stage 1 remains **NOT PASS**. Q005 closes the previously untouched symptom→reproduction→isolation→causal-test Foundation gap at bounded model level, but stronger error/recovery/crash/observability/regression evidence and transfer beyond Python models remain required.

## Dependencies / handoffs
- Foundations: F004/F005 supply scheduling/signaling/timeout/cancellation mechanisms; F001 direct Dart/Flutter execution remains OPEN after environment recheck 2026-09-17.
- Architecture: A003 contracts/invariants are useful independent isolation boundaries; operation terminal-state behavior remains a semantic contract.
- Mobile: lifecycle/process-death/background diagnosis needs exact platform/build/prestate and must distinguish missing callback, failed durable write and failed recovery.
- Data: D006 should record logical operation ID plus delivery/apply/ack/conflict state and first violated invariant when debugging duplicate/reorder failures.
- Systems: runtime observations must bind to artifact/version/environment identity; diagnostic data also requires privacy/security review.
- Design Studio / Web Manager: repository search found no directly applicable current debugging/telemetry evidence.
- Marketing Manager: not materially relevant.

## Next work
Use Balance Loop. Q005 now removes the untouched debugging/fault-isolation Foundation gap with executable ambiguity/isolation evidence. Strong next candidates are `F006` OS/file/socket/network foundations because D006 needs transport/partition mechanisms, or `Q006` fault injection/recovery/regression if reliability evidence outranks networking. Direct Dart/Flutter execution remains first-attempt work whenever a trustworthy SDK environment exists.
