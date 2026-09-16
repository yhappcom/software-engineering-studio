# Quality Specialist Status

Track: Quality, Testing & Reliability  
Prefix: `Q###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-16

## Mission
Build engineering capability to define correctness, design tests with valid oracles, reproduce failures, debug root causes, verify recovery, prevent regressions, and operate software with trustworthy observability.

## Current evidence

### Q001 — Correctness, specification, test oracle and reproducibility
**SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed.**

Canonical: `research/quality/Q001_correctness_specification_oracle_reproducibility.md`
Fixture: `research/quality/fixtures/Q001_oracle_reproducibility.py`

Established independent specification/oracle discipline, deliberate weak-oracle defect evidence, invariant/exact oracles, seeded reproducibility, and the Studio-wide Test Evidence Contract V1 in `methods/VALIDATION_STANDARD.md`.

### Q002 — Test levels, evidence boundaries and trade-offs
**IN STUDY — first integrated Foundation block complete.**

Canonical: `research/quality/Q002_test_levels_evidence_boundaries.md`
Fixture: `research/quality/fixtures/Q002_test_level_boundary.py`

New evidence:
- SWEBOK v4 and ISTQB CTFL v4.0.1 distinguish test levels by target/objective/interactions/environment rather than prestige;
- test level is modeled as an evidence boundary: target + real/substituted collaborators + crossed runtime/platform boundaries + environment + oracle + observable failure classes;
- executable Python fixture: isolated Service test with fake repository PASS, concrete control PASS, deliberate real-collaborator write-drop integration FAIL;
- root cause: the fake substituted away the mechanism containing the defect;
- therefore component/unit PASS does not establish integration correctness;
- broader tests are not automatically superior: breadth can increase relevant mechanism coverage while worsening localization/nondeterminism, and cannot repair an invalid oracle.

Evidence limit: no Dart/Flutter/database/network/device/system E2E execution was claimed.

## Initial queue
- `Q001` — substantial Foundation block complete.
- `Q002` — **IN STUDY** — first integrated test-level boundary block complete; broader system-level counterexample/transfer still open.
- `Q003` — Determinism, nondeterminism, concurrency and flaky-test mechanics.
- `Q004` — Property-based/model-based testing and invariant checking.
- `Q005` — Debugging, fault isolation, observability and crash analysis.
- `Q006` — Fault injection, recovery verification and regression governance.

## Gate requirement
Foundation PASS requires tests that can fail for the right reason, reproduced defect/failure paths, root-cause reasoning, explicit test-level/evidence boundaries, and foundational debugging/recovery/regression understanding. Quality Stage 1 is **not PASS**.

## Dependencies / handoffs
- Foundations: attach runtime/build/process context; F001 Dart/Flutter execution remains OPEN.
- Architecture: A003 contracts can supply test properties, but fake-provider tests do not prove every provider implementation.
- Mobile: lifecycle/process-death/background claims require exact platform/device/build/prestate and tests that cross those mechanisms.
- Data: storage/transaction/durability claims require real persistence mechanisms where relevant; fake repositories cannot establish them.
- Systems: artifact/release/security checks require claim-specific environment and artifact identity.
- Design Studio: interaction semantics can become acceptance specifications when materially relevant.
- Web Manager: browser/PWA tests need browser/network/cache/origin/artifact context.
- Marketing Manager: instrumentation correctness requires semantic event/version oracles, not SDK presence.

## Next work
Use Balance Loop. Q002 should continue only if a trustworthy broader-system counterexample or product transfer is available; otherwise D002 now has high leverage because Q002 supplies the evidence-boundary discipline needed to test real serialization/database/index/transaction mechanisms.