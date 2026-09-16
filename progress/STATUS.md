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
| Quality | Stage 1 IN STUDY — Q001 substantial first block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### M001 — Flutter runtime/UI/lifecycle/platform boundary
Canonical: `research/mobile/M001_flutter_runtime_widget_lifecycle_platform_boundary.md`  
Fixture: `research/mobile/fixtures/M001_lifecycle_notification_gap.py`

Current official Flutter/Dart/Android/iOS sources establish distinct app/framework/engine/embedder/OS layers, distinct Widget/Element/State/RenderObject roles, non-1:1 Flutter/platform lifecycle naming, and the explicit Flutter warning that applications must not rely on receiving every lifecycle notification.

A bounded executable model then compared two persistence policies. Saving only on modeled `paused` preserved an edit during orderly backgrounding but lost it when abrupt termination skipped that callback. Committing at the semantic mutation boundary preserved the modeled value in both sequences.

Evidence boundary: Python 3.13.5 / Linux 6.18.44 x86_64 / glibc 2.41. This is a model-level failure demonstration, **not** Flutter/Android/iOS runtime, filesystem durability, power-loss, database or device evidence.

### LogMate transfer scope
`yhappcom/logmate → main commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → 2026-09-16`.

The exact pubspec confirms Flutter and Dart SDK `^3.10.7`, establishing stack relevance only. No lifecycle/persistence defect is inferred.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked this run: neither executable is available.
- **D001:** state/persistence/durability/authority model + SQLite application-process-kill evidence.
- **Q001:** weak-oracle defect + stronger exact/invariant oracle + reproducibility evidence; Test Evidence Contract promoted.
- **A001-A003:** change pressure/information hiding, state ownership/dependency direction, semantic contract/API compatibility with positive/counterexample fixtures and bounded product transfer.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation with two executable trust-boundary blocks.

## Cross-track handoffs
- **Data:** durable commit/recovery must not rely solely on lifecycle notification arrival; distinguish UI state from durable domain state.
- **Quality:** lifecycle validation needs skipped-callback/process-death cases and exact platform/device/build prestate, not orderly transitions only.
- **Architecture:** Widget/State ownership is not automatically domain/data ownership.
- **Systems:** framework-normalized lifecycle state is not an OS/platform guarantee; runtime evidence needs exact artifact/build/platform identity.
- **LogMate advisory:** future local-ledger persistence should not use `paused`/`detached` as the sole commit boundary for user-entered flight data.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated. Mobile is no longer untouched, but its strongest runtime/device claims remain open.

Current highest-value candidates:
1. `Q002` — test-level boundaries and trade-offs, because upcoming M002 process-death, D002 persistence and Systems release validation need explicit placement of unit/integration/system evidence;
2. `D002` — files/serialization/database/index/transaction fundamentals, high direct leverage for LogMate local ledger and MintTap data integrity;
3. `M002` — Android/iOS process lifecycle/termination/background semantics if a trustworthy platform-level failure/transfer method is available without pretending device execution.

Selection should follow evidence opportunity and live-project risk, not rotation.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
