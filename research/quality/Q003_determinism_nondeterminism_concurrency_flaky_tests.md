# Q003 — Determinism, Nondeterminism, Concurrency & Flaky-Test Mechanics

Status: **IN STUDY — first integrated Foundation block complete**  
Date: 2026-09-17  
Lead: Quality, Testing & Reliability

## Problem
A repeated green result is not automatically evidence that behavior is deterministic. Concurrent software admits multiple schedules; a test can accidentally exercise only one, while a timing-based attempt to expose a race can itself be flaky. Q003 establishes a claim-scoped model for schedule-dependent failures and reproducibility.

## SOURCE
Checked 2026-09-17:
- Python 3.13 `threading` docs: threads share a process; Lock is a synchronization primitive; when multiple waiters contend, which proceeds is not defined. Barrier can coordinate fixed parties. https://docs.python.org/3.13/library/threading.html
- pytest current flaky-test guidance: higher-level/shared-state/order-sensitive tests can be flaky; parallel execution can expose ordering/global-state assumptions; reruns mitigate symptoms but are dangerous as permanent concealment. https://docs.pytest.org/en/stable/explanation/flaky.html

## SYNTHESIS
Keep these distinct:
- deterministic specification: permitted outcome is unique for the relevant state/input;
- deterministic implementation under a model: all permitted schedules/events produce the required observable result;
- reproducible test setup: another run can reconstruct relevant conditions;
- reproduced failure: the failure occurred again;
- flaky test: nominally identical test executions can yield different verdicts because uncontrolled relevant state/order/timing/environment changes.

A fixed random seed controls only represented randomness. It does not control thread scheduling, clocks, network order, storage completion, external services, or hidden shared state.

## EXECUTABLE VALIDATION
Fixture: `research/quality/fixtures/Q003_concurrency_schedule_flake.py`

Environment observed before persistence:
- Python 3.13.5
- Linux 6.18.44 x86_64
- glibc 2.41

### CLAIM
A passing execution under one schedule does not establish schedule-independent correctness; an unsynchronized shared read-modify-write can violate the bounded counter invariant.

### SPEC/PROPERTY
Two workers each perform 1,000 logical increments. Accepted final value: exactly 2,000.

### TARGET / FAILURE MODEL
Unsafe variant deliberately splits read and write and calls `time.sleep(0)` between them to widen an interleaving window. Two threads begin through a Barrier. Comparison variant protects the increment with one Lock.

### OBSERVATION
Pre-persistence execution produced 20/20 unsafe results of `1000` rather than `2000`; five locked comparison runs produced `2000`.

### ROOT CAUSE
The unsafe operation is not one indivisible logical update: both workers can read the same old value before either publishes the increment, so one logical increment overwrites the other. The yield is test instrumentation that makes the schedule easier to reproduce; it is not the production cause.

### ALTERNATIVE
The lock comparison establishes the bounded invariant for this fixture by serializing the critical update. This does not establish that mutex serialization is the correct architecture for distributed, async, isolate, database, or message-driven systems.

### REPLICATION
The fixture persists exact iteration/run counts and uses no random seed. Re-execution should record environment and complete output. A future run that fails to expose the unsafe race is not evidence that the unsafe algorithm became correct; it shows the test schedule did not manifest the fault under that run.

### EVIDENCE LIMIT
This is deliberately widened CPython thread evidence. It is not a scheduler probability estimate, Dart isolate/thread evidence, Flutter runtime evidence, real network reorder evidence, or production evidence. The GIL does not make multi-step application invariants automatically atomic.

## ENGINEERING JUDGMENT — flaky-test response
A rerun can help collect evidence but must not silently redefine FAIL as PASS. Preserve the first failure signature and relevant schedule/state; then reduce uncontrolled variables, create explicit synchronization/fault injection where possible, and add a regression oracle tied to the underlying invariant. `sleep()`-only tests are weak because elapsed time is an indirect scheduler assumption; use explicit barriers/events/hooks when the mechanism can be exposed.

## D006 TRANSFER
D006 established duplicate delivery, lost acknowledgement and concurrent-writer conflict semantics in a deterministic model. Q003 adds the validation rule: distributed/sync tests must enumerate or deliberately generate relevant event orders instead of relying on one happy schedule. `delivery A then B` passing cannot establish `B then A`, duplicate, delayed ACK, concurrent delete/update, or reconnect order correctness.

## RELATED DOMAIN CHECK
- Foundations: F004/F005 remain prerequisites for deeper process/thread/async scheduling models; F001 direct Dart/Flutter execution remains OPEN.
- Architecture: synchronization strategy must follow state ownership/invariant boundaries; adding a lock is not a substitute for defining ownership.
- Mobile: lifecycle/connectivity/process-death ordering needs exact platform/runtime validation later.
- Data: D006 directly motivates order/duplicate/conflict schedule coverage.
- Systems: runtime/build/environment identity belongs in flaky/reproduction evidence.
- Design Studio: not materially relevant to this first mechanism block except future user-visible conflict/recovery semantics.
- Web Manager: not materially relevant to this first thread mechanism block; browser/service-worker ordering belongs to later transfer validation.
- Marketing Manager: not materially relevant.
- Product source: no new product behavior claim required; retained LogMate exact-ref transfer remains methodological only.

## OPEN / VALIDATION
- enumerate event-order testing/model-based schedule exploration rather than timing-only manifestation;
- distinguish test flakiness caused by the SUT from flakiness caused by test harness/shared global state;
- cancellation/timeouts/deadlock/livelock/starvation;
- Dart event loop/isolate and Flutter runtime execution when trustworthy toolchain exists;
- real network/backend duplicate/reorder/concurrent-writer transfer for D006.

## HANDOFFS
- **Quality → Data:** D006 follow-up should test explicit order matrices and preserve first-failure event trace; do not use retries as correctness proof.
- **Quality → Foundations:** F004/F005 should supply deeper scheduling/happens-before/async mechanics before Q003 claims broader concurrency competence.
- **Quality → Mobile:** eventual lifecycle/sync tests should replace arbitrary sleeps with controllable hooks where feasible and record platform/build/prestate.

## Current judgment
First integrated Q003 block has SOURCE + executable failure + root-cause isolation + synchronized alternative + D006 transfer. Q003 and Quality Stage 1 remain **NOT PASS**; deeper schedule exploration, harness-vs-SUT flake isolation, debugging/observability and recovery/regression work remain open.
