# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-16  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial Foundation blocks complete |
| Mobile | Stage 1 IN STUDY — M001 first integrated Foundation block complete |
| Data | Stage 1 IN STUDY — D001 substantial first block |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### Q002 — Test levels as evidence boundaries
Canonical: `research/quality/Q002_test_levels_evidence_boundaries.md`  
Fixture: `research/quality/fixtures/Q002_test_level_boundary.py`

SWEBOK v4 and ISTQB CTFL v4.0.1 were used to ground component/unit, integration, system and acceptance distinctions in test object, objective, interactions and environment rather than a simple confidence hierarchy.

Executable bounded evidence (Python 3.13.5/Linux): the same Service semantic path passed an isolated component test using a fake repository and a concrete control, while a deliberate concrete collaborator that silently dropped writes failed the integration oracle. Root cause: the isolated fake removed the mechanism containing the defect.

Validated bounded conclusion: **component/unit PASS does not establish integration correctness**. Conversely, broader tests are not automatically stronger for every claim; breadth does not repair an invalid oracle and can worsen localization/nondeterminism. Test selection should match the mechanism and failure class relevant to the claim.

Evidence limit: no Dart/Flutter/database/network/device/system-E2E execution claimed.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked: neither executable is available.
- **D001:** state/persistence/durability/authority model + SQLite application-process-kill evidence.
- **Q001:** weak-oracle defect + stronger exact/invariant oracle + reproducibility; Test Evidence Contract promoted.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Cross-track handoffs
- **Mobile:** lifecycle/process-death claims require tests that actually cross platform/process mechanisms; widget/component tests cannot establish OS behavior.
- **Data:** D002 persistence/serialization/index/transaction claims should use real storage integration where those semantics are the target rather than fake repositories.
- **Systems:** release/signing/artifact/deployment claims require exact artifact/environment evidence.
- **Architecture:** contract tests can validate semantic boundaries, but substituted providers do not prove every concrete provider.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated.

Current highest-value candidates:
1. `D002` — serialization/files/database/index/transaction fundamentals, now strongly enabled by Q002's evidence-boundary discipline and directly relevant to future LogMate local ledger plus MintTap data integrity;
2. continue `Q002` only if a trustworthy broader-system counterexample or exact product test transfer is available;
3. `M002` — Android/iOS process lifecycle/termination/background semantics when trustworthy platform-level validation can be obtained.

Selection follows evidence opportunity and live-project risk, not rotation.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.