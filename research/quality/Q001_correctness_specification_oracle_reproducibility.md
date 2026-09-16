# Q001 — Correctness, Specification, Test Oracle & Reproducibility

Status: **IN STUDY — FOUNDATION MODEL + EXECUTABLE ORACLE/REPLICATION EVIDENCE**  
Date: 2026-09-16  
Lead: Quality, Testing & Reliability

## Problem

A green test result is often described too loosely as “the code is correct.” That statement collapses several different things:

`intended behavior → specification/property → selected test state/input → observed behavior → oracle → verdict → evidence scope`.

Quality engineering needs a model that says exactly what a passing test establishes, what it does not establish, how a test can be weak or self-confirming, and what must be captured to reproduce a failure.

This is a prerequisite for every other Studio track because executable evidence is only useful if its oracle and reproduction contract are trustworthy.

## SOURCE

Primary sources checked:

1. IEEE Computer Society, **SWEBOK Guide V4.0a**, Software Testing chapter, current official download checked 2026-09-16.  
   - https://www.computer.org/education/bodies-of-knowledge/software-engineering  
   - https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf
2. Python 3.13 `unittest` documentation, official language documentation, checked 2026-09-16.  
   - https://docs.python.org/3.13/library/unittest.html

Relevant SWEBOK points:

- software testing dynamically verifies expected behavior on a finite set of selected cases from a usually much larger execution domain;
- the **oracle** decides whether the observed outcome is correct for a test and can produce pass, fail, or sometimes inconclusive;
- example oracle sources include unambiguous requirements, behavioral models and code annotations;
- fault and failure are distinct: a fault is a cause in the software, while a failure is an undesired externally observed effect; a fault may exist without manifesting on the selected tests;
- successful tests do not justify claiming that bugs are absent because exhaustive testing of realistic software is generally infeasible;
- replication concerns whether different people can perform the same testing activity;
- test reporting should retain when the test ran, who/what performed it, software configuration and other relevant identification evidence.

Python `unittest` provides concrete assertion mechanisms that compare observed behavior with expected conditions; the assertion is the mechanical verdict mechanism, not the source of truth for what the expectation *should* be.

## First-principles model

### 1. Correctness is not an intrinsic property of a test result

A useful Studio model is:

`correct with respect to WHAT contract/property, for WHICH inputs/state, under WHICH environment and assumptions?`

`PASS` without those qualifiers is incomplete.

A test verdict establishes that a selected observation satisfied its oracle. It does **not** by itself establish that:

- the oracle represents the true product requirement;
- all important states or inputs were exercised;
- the implementation contains no latent fault;
- another runtime/platform/build mode behaves the same;
- the result is reproducible;
- the result transfers to production.

### 2. Specification and oracle are related but not identical

A **specification** states the required property or behavior.

An **oracle** is the mechanism used for a concrete test to decide whether observed behavior satisfies the relevant specification/property.

Examples:

- specification: arithmetic total includes every signed ledger entry;
- exact-value oracle: expected total is `5` for `[10, -7, 2]`;
- invariant oracle: negating every entry must negate the total;
- model oracle: compare the SUT result with an independently implemented reference model.

An oracle can be wrong, incomplete, too weak, stale, coupled to the same defect as the SUT, or unable to decide. Therefore “automated assertion exists” is not equivalent to “valid oracle exists.”

### 3. A weak oracle can make a defective implementation look healthy

A test may execute real code and still carry little correctness evidence if its assertion is too weak.

Example:

`result >= 0` on positive-only data cannot detect an implementation that incorrectly discards all negative ledger entries.

The execution is real. The test is green. The defect remains.

### 4. Test selection and oracle strength are independent dimensions

A strong oracle on one trivial case may miss faults because the input space is weak.

Many diverse inputs with a weak oracle may also miss faults.

Quality evidence therefore needs both:

`selection adequacy × oracle adequacy`.

Coverage/activity measures are evidence about what was exercised; they are not automatically evidence that observed behavior was judged against the right requirement.

### 5. Failure observation and fault diagnosis are different jobs

A failing oracle establishes an observed mismatch under the test conditions. It does not automatically identify root cause.

The progression is:

`failure observation → reproduction → narrowing/isolation → causal hypothesis → falsification/check → root cause → fix → regression evidence`.

This distinction prevents test output from being mistaken for debugging proof.

### 6. Reproducibility is an evidence contract

For Studio work, a reproducible test should preserve enough context for another execution to reconstruct the evidence.

Minimum fields when material:

- repository/file and exact commit/ref;
- tool/runtime/compiler/framework version;
- OS/platform/device/build mode;
- test target and test objective;
- specification/property/oracle;
- exact inputs or deterministic generation method;
- random seed when randomness is controlled;
- pre-test state/fixture/data/schema;
- configuration/feature flags/environment variables;
- relevant external dependency versions/endpoints/mocks;
- time/locale/timezone/network assumptions when relevant;
- observed output/failure signature;
- expected outcome;
- cleanup/recovery procedure when the test mutates durable state.

A deterministic seed does not make the software deterministic in general. It only controls the random source represented by that seed. Threads, clocks, networks, process scheduling, storage and external systems may still introduce nondeterminism.

## EXECUTABLE VALIDATION — weak oracle vs specification-derived oracle

Fixture:

`research/quality/fixtures/Q001_oracle_reproducibility.py`

Environment:

- Python 3.13.5
- Linux execution environment
- deterministic generated input seed: `20260916`
- generated cases: `100`

Bounded specification:

> `ledger_total(entries)` returns the arithmetic sum of every signed integer entry.

Implementations:

1. `ledger_total_correct` — sums every entry.
2. `ledger_total_mutant` — deliberate fault: ignores every negative entry.

Oracles:

1. **weak oracle** — only checks that a positive-only example returns a nonnegative value;
2. **exact oracle** — compares known examples with exact arithmetic results;
3. **signed-symmetry oracle** — checks a property derived from arithmetic sum: negating every input must negate the result;
4. **generated exact oracle** — generates 100 deterministic input lists, records their SHA-256 case-set hash, and compares each candidate result with an independent `sum(entries)` reference derived directly from the bounded specification.

Observed output:

```text
python=3.13.5
spec=ledger_total(entries) returns the arithmetic sum of every signed integer entry.
{"exact_failure_count": 0, "first_generated_failure": null, "generated_case_hash": "81efdf1e5bd528f37007ee1759cf43cb3be44b470768e357c51c799d6b9a4857", "generated_failure_count": 0, "generated_seed": 20260916, "implementation": "correct", "symmetry_oracle_pass": true, "weak_oracle_pass": true}
{"exact_failure_count": 2, "first_generated_failure": {"entries": [-10, -14, 3, 12, -5, 17], "expected": 3, "index": 1, "observed": 32}, "generated_case_hash": "81efdf1e5bd528f37007ee1759cf43cb3be44b470768e357c51c799d6b9a4857", "generated_failure_count": 75, "generated_seed": 20260916, "implementation": "mutant", "symmetry_oracle_pass": false, "weak_oracle_pass": true}
```

The fixture was executed twice without modification. The complete stdout, generated case-set hash and failure counts were identical on both runs.

### What this establishes

- a real deliberate fault can pass a real executable test when the oracle is too weak;
- the same faulty implementation is detected by exact expected values and a specification-derived invariant;
- recording seed plus deterministic generation logic makes this bounded random input set reproducible in this environment;
- an input-set hash is useful evidence that repeated runs exercised the same generated cases;
- a passing test verdict must be interpreted in terms of its oracle and selected cases.

### What this does NOT establish

- that generated testing with 100 cases proves the correct implementation globally correct;
- that Python `sum` would be an independent enough production oracle for every real arithmetic/calculation engine;
- Flutter/Dart testing behavior;
- concurrent, time-dependent, networked or distributed reproducibility;
- correctness of MintTap or LogMate;
- adequate test coverage for financial, aviation or safety-related domain rules.

## Failure and anti-pattern analysis

### Anti-pattern: assertion without a requirement

`assert output != null` may be executable but says little if the requirement concerns exact semantic correctness.

### Anti-pattern: implementation-derived expected value

If the expected result is generated by calling the same production algorithm or copy-pasting the same faulty logic, the test may reproduce the defect in both SUT and oracle.

Prefer oracle independence proportional to risk: explicit examples, independently derived formulae, reference models, invariants, cross-implementation comparison, authoritative domain tables, or human/domain review where automation cannot decide.

### Anti-pattern: green suite as global proof

A green suite is bounded evidence. It supports confidence only to the extent that the test selection, oracle, environment, and failure model match the claim being made.

### Anti-pattern: unreproducible failure treated as noise

A failure that cannot yet be reproduced is not automatically invalid. Preserve available context first. Nondeterministic/concurrent failures require a different reproduction strategy rather than immediate dismissal.

### Anti-pattern: fixing symptom without proving root cause

Changing code until a test turns green may remove the observed failure while leaving the actual causal defect or another failure path intact. Root-cause evidence and regression design are separate obligations.

## SYNTHESIS — Studio Test Evidence Contract V1

For substantial executable evidence, record:

`CLAIM → SPEC/PROPERTY → TARGET → INPUT/STATE → ORACLE → ENVIRONMENT → OBSERVATION → VERDICT → FAILURE MODEL → REPRODUCTION DATA → EVIDENCE LIMIT`

A test report missing the oracle or claim boundary cannot support a strong engineering conclusion even when execution is fully automated.

### Evidence-strength questions

Before citing a test as proof, ask:

1. What exact claim is this test intended to support?
2. Where does the expected behavior come from?
3. Can the oracle disagree with the implementation if the implementation is wrong?
4. Which states/inputs/failures are absent?
5. What environment/build/runtime assumptions matter?
6. Can another run reconstruct the same relevant conditions?
7. Does the test expose a failure, or also establish root cause?
8. What conclusion would be invalid to infer from this pass?

## RELATED DOMAIN CHECK

### Foundations
F001 established that runtime/build/process context matters. Q001 therefore requires environment/build/runtime identity on runtime-sensitive tests rather than treating all executions as equivalent.

### Data
D001 is a concrete example of claim-scoped evidence. Its SIGKILL fixture supports application-process-crash transaction behavior under one SQLite configuration; Q001 confirms why it must not be generalized to power-loss, WAL, Android/iOS or distributed synchronization.

### Architecture
Architecture contracts and invariants are valuable oracle sources. A boundary is easier to maintain when its externally observable contract can be tested without reproducing its implementation internally.

### Mobile
Lifecycle/process-death/background tests require explicit platform/build/device state in the reproduction contract. Desktop or Linux evidence cannot silently become Android/iOS evidence.

### Systems
Performance/security/release gates need specialized oracles: threshold/contract/policy/state-transition evidence, not merely “command exited 0.” Build identity and configuration are part of reproducibility.

### Design Studio
Interaction and Content semantics can act as upstream product specifications for observable states. Engineering tests should verify the real state contract rather than invent implementation-friendly semantics.

### Web Manager
Browser/network/performance evidence needs browser/runtime/version/route/network/cache context before transfer.

### Marketing Manager
Analytics/ad instrumentation tests require event-definition/version and semantic correctness, not only proof that an SDK emitted some event.

## PROJECT TRANSFER

### LogMate
Product source previously checked at:

`yhappcom/logmate → main commit b551ce434ad72b1895033e0f3617c73b026d40ea → evidence date 2026-09-16`.

Q001 does **not** validate LogMate code. It supplies a future test discipline for the planned local ledger/import/backup/sync pipeline:

- each flight-domain calculation requires an independent expected-value or invariant source;
- local durable commit tests must define the failure boundary they claim to survive;
- import tests need exact fixture provenance and duplicate/review oracle rules;
- synchronization tests need explicit state/conflict/reconciliation oracles;
- “same result across native and PWA” requires the same canonical input/specification plus platform-specific execution evidence.

### MintTap
No MintTap repository was audited in Q001. Transfer is methodological only: financial calculations and analytics/ad instrumentation should not treat green execution or event presence as semantic correctness without independently defined expected behavior.

## OPEN / VALIDATION

1. `Q002`: distinguish unit/integration/system/e2e boundaries by the failure/contract each can observe.
2. `Q003`: directly reproduce nondeterministic/flaky behavior and separate determinism from reproducibility.
3. `Q004`: add property-based/model-based testing and mutation analysis beyond this bounded hand-written mutant.
4. Apply the Test Evidence Contract to an actual Dart/Flutter test environment when available.
5. Apply the contract to a real product calculation or persistence boundary using an exact product ref and independent product/domain specification.
6. Define risk-based oracle independence requirements for financial and aviation-domain calculations before declaring production-grade validation.

## HANDOFFS

- **Quality → all tracks:** use `CLAIM → SPEC/PROPERTY → TARGET → INPUT/STATE → ORACLE → ENVIRONMENT → OBSERVATION → VERDICT → FAILURE MODEL → REPRODUCTION DATA → EVIDENCE LIMIT` for substantial executable evidence.
- **Quality → Data:** continue preserving exact SQLite mode/synchronous/failure boundary; add oracle source and reproduction fields to future migration/backup/sync fixtures.
- **Quality → Mobile:** mobile lifecycle tests must record platform/device/build/lifecycle prestate and distinguish process death from ordinary route/widget disposal.
- **Quality → Architecture:** make contracts/invariants independently observable so tests do not need to clone internal implementation.
- **Quality → Systems:** release/performance/security checks require claim-specific oracles and configuration identity.

## Current judgment

`Q001` has Foundation-level source/model evidence plus an executable deliberately faulty implementation demonstrating a weak-oracle false sense of safety and deterministic reproduction of stronger-oracle failures.

It is **not a Quality Stage 1 PASS**. The track still requires test-level trade-offs, nondeterminism/flakiness, debugging/root-cause evidence, observability, and fault/recovery/regression work across Q002–Q006.
