# Engineering Validation Standard

## Principle

Engineering knowledge is not production-grade because it is plausible, documented, popular, or demonstrated once. Evidence must match the claim.

## Evidence ladder

Use the strongest feasible rung:

1. `SOURCE` — specification, official docs, standards, primary implementation docs.
2. `MODEL` — first-principles explanation with explicit assumptions.
3. `WORKED EXAMPLE` — bounded example showing expected mechanism.
4. `EXECUTABLE TEST` — reproducible code/test with recorded environment.
5. `FAILURE CASE` — representative breakage, invalid input, race, interruption, process death, partial failure, or boundary condition.
6. `DEBUG/ROOT CAUSE` — evidence connecting symptom to mechanism.
7. `ALTERNATIVE` — materially different implementation or architecture comparison.
8. `TRANSFER VALIDATION` — same conclusion tested in another platform/product/context.
9. `PRODUCTION EVIDENCE` — observed real-project/runtime evidence with exact ref/version/release context.

## Validation record

When executable validation is material, record:

- question/hypothesis;
- environment/toolchain/versions;
- exact code or fixture location;
- setup and inputs;
- expected result;
- observed result;
- failure variants;
- interpretation;
- limitations;
- reproducibility notes.

## Common invalid shortcuts

Do not equate:

- code coverage with correctness;
- one benchmark run with performance truth;
- one platform with cross-platform behavior;
- simulator/emulator with physical-device evidence when the distinction matters;
- successful write with durability;
- no observed crash with reliability;
- retry with idempotency;
- encryption presence with secure system design;
- default branch with production;
- type safety with runtime correctness;
- unit tests with system integration correctness;
- a framework abstraction with an OS/platform guarantee.

## Failure-first expectation

For topics involving persistence, sync, concurrency, migrations, security, release, or recovery, validation should deliberately include failure paths before PASS.

Examples:
- process killed between operations;
- network drop/timeout/reorder;
- duplicate request/event;
- stale or conflicting state;
- storage full/corrupt/invalid input;
- schema mismatch/migration interruption;
- permission revoked;
- dependency/build/release failure;
- clock/timezone/version mismatch when relevant.

## Gate discipline

A specialist status must state why evidence is sufficient for PASS and what remains OPEN. Missing human, device, production, security-review, or field evidence must remain explicit rather than simulated.
