# Quality Specialist Status

Track: Quality, Testing & Reliability  
Prefix: `Q###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-17

## Mission
Build engineering capability to define correctness, design tests with valid oracles, reproduce failures, debug root causes, verify recovery, prevent regressions, and operate software with trustworthy observability.

## Current evidence

### Q001 — Correctness, specification, test oracle and reproducibility
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed.**

Canonical: `research/quality/Q001_correctness_specification_oracle_reproducibility.md`
Fixture: `research/quality/fixtures/Q001_oracle_reproducibility.py`

Established independent specification/oracle discipline, deliberate weak-oracle defect evidence, seeded reproducibility, and the Studio-wide Test Evidence Contract V1 in `methods/VALIDATION_STANDARD.md`.

### Q002 — Test levels, evidence boundaries and trade-offs
**IN STUDY — first integrated Foundation block complete.**

Canonical: `research/quality/Q002_test_levels_evidence_boundaries.md`
Fixture: `research/quality/fixtures/Q002_test_level_boundary.py`

Established that test level is an evidence boundary defined by target, real/substituted collaborators, crossed runtime/platform boundaries, environment, oracle and observable failure classes. An isolated fake-repository test passed while the concrete collaborator with a deliberate write-drop defect failed; broader tests are not automatically superior and cannot repair an invalid oracle.

### Q003 — Determinism, nondeterminism, concurrency and flaky-test mechanics
**IN STUDY — first integrated Foundation block complete.**

Canonical: `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md`  
Fixture: `research/quality/fixtures/Q003_concurrency_schedule_flake.py`

Established with current Python/pytest sources plus Python 3.13.5/Linux executable evidence:
- deterministic specification, deterministic behavior, reproducible setup, reproduced failure and flaky verdict are distinct claims;
- a deliberately widened two-thread read/yield/write race violated an exact 2,000-increment invariant in 20/20 observed runs, producing 1,000;
- the bounded Lock comparison produced 2,000 in five runs;
- root cause is lost update across a non-indivisible logical read-modify-write; the injected yield exposes the schedule but is not the causal defect;
- a green run under one schedule cannot establish schedule-independent correctness;
- reruns can gather evidence but must not silently convert intermittent FAIL into correctness evidence;
- D006 sync validation should exercise explicit event-order matrices rather than one happy ordering.

Evidence limit: deliberately widened CPython thread fixture only; no probability estimate, Dart isolate/event-loop, Flutter runtime, real network/backend, or production claim.

## Initial queue
- `Q001` — substantial Foundation block complete.
- `Q002` — first integrated test-level boundary block complete; broader system transfer still open.
- `Q003` — **IN STUDY / first integrated block complete**; schedule exploration, harness-vs-SUT flake isolation, cancellation/deadlock and Dart/runtime transfer OPEN.
- `Q004` — Property-based/model-based testing and invariant checking.
- `Q005` — Debugging, fault isolation, observability and crash analysis.
- `Q006` — Fault injection, recovery verification and regression governance.

## Gate requirement
Foundation PASS requires tests that can fail for the right reason, reproduced defect/failure paths, root-cause reasoning, explicit test-level/evidence boundaries, and foundational debugging/recovery/regression understanding. Quality Stage 1 is **not PASS**.

## Dependencies / handoffs
- Foundations: F004/F005 should deepen scheduling/async semantics; F001 direct Dart/Flutter execution remains OPEN after environment recheck 2026-09-17.
- Architecture: synchronization must follow ownership/invariant contracts rather than patch undefined ownership.
- Mobile: lifecycle/process-death/background claims require exact platform/device/build/prestate and controllable ordering where feasible.
- Data: D006 reorder/duplicate/conflict tests should preserve explicit event traces and exercise order matrices.
- Systems: artifact/runtime/environment identity is part of reproducibility.
- Design Studio: interaction semantics can become acceptance specifications when materially relevant.
- Web Manager: browser/PWA ordering requires separate browser/service-worker transfer evidence.
- Marketing Manager: instrumentation correctness requires semantic event/version oracles, not SDK presence.

## Next work
Use Balance Loop. Q003 exposes a Foundations prerequisite: deeper scheduling, synchronization and async/event-loop mechanics in `F004/F005` now have high cross-track leverage. Continue Q003 directly only if a coherent schedule-exploration/harness-isolation block can be validated without pretending Dart/Flutter or network evidence.
