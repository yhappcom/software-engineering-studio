# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-16  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial Foundation blocks complete |
| Mobile | Stage 1 READY |
| Data | Stage 1 IN STUDY — D001 substantial first block |
| Quality | Stage 1 IN STUDY — Q001 substantial first block |
| Systems | Stage 1 IN STUDY — S001 first integrated artifact-provenance block complete |

No specialist has passed Foundation.

## Meaningful new evidence

### S001 — Trust Boundaries, Artifact Identity & Build Provenance
Canonical: `research/systems/S001_trust_artifact_provenance_foundations.md`

Balance Loop selected Systems over further Architecture expansion because Architecture A001-A003 already have substantial Foundation evidence, Mobile remains direct-toolchain constrained, and artifact/build trust boundaries have cross-track release, Quality, Web/PWA and future Mobile leverage.

New evidence:
- NIST SP 800-207 supports the general rule that trust is not granted implicitly from location or ownership;
- NIST SSDF 1.1 remains the final secure-development baseline checked, while NIST lists SSDF 1.2 as a public draft;
- current SLSA v1.2 provenance separates artifact subject, build definition/parameters, dependencies and trusted builder identity;
- executable fixture `research/systems/fixtures/S001_artifact_identity.py` created canonical and post-build-transformed artifacts with the same declared source ref;
- a source-ref-only verifier accepted both artifacts;
- independent SHA-256 identity distinguished canonical `f8acaec1d75f06db55d7804ce24007d6829ab5cd1a3ab97af1cd89860fa74743` from transformed `fb59fee4330f9c46628166ab7bb00896d5e8bd073b4b6b90bbb22fd7fbfe2aa8`;
- root cause is identity collapse: `same source ref ⇒ same artifact` is an invalid verification shortcut when build/post-build inputs can change output.

Evidence environment: Python 3.13.5, Linux 6.18.44 x86_64/glibc 2.41. This does not prove signed provenance, build reproducibility, malicious-builder resistance, Flutter packaging, or production release integrity.

### Cross-repository transfer
Current `yhappcom/web-manager/STATUS.md` was checked because S001 overlaps its PWA release/operations evidence. Web Manager already records `same source ref ≠ same accepted PWA artifact when build/post-build/origin differs`. S001 independently transfer-validates the artifact-identity mechanism while leaving browser/origin/PWA acceptance under Web Manager/product ownership. No external repository was edited.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **D001:** state/persistence/durability/authority model + SQLite application-process-kill evidence.
- **Q001:** weak-oracle defect + stronger exact/invariant oracle + reproducibility evidence; Test Evidence Contract promoted.
- **A001-A003:** change pressure/information hiding, state ownership/dependency direction, semantic contract/API compatibility with positive/counterexample fixtures and bounded LogMate transfer.

## Cross-track handoffs
- **Mobile:** future device acceptance should capture canonical build target/command, toolchain/dependency lock, post-build transforms, artifact identity, install/deploy target, build mode and exact device/OS.
- **Quality:** source-ref-only target identity is insufficient for release/e2e evidence when multiple artifacts can derive from one ref.
- **Data:** migration/rollback evidence should bind to exact application/schema artifact/version.
- **Web Manager:** existing PWA artifact-provenance guard is supported by reusable executable evidence; runtime acceptance remains open.

## Current Balance Loop
F001 direct Dart/Flutter execution remains OPEN; no replacement evidence is inferred from Python fixtures.

Highest-value next candidates:
1. continue `S001` if the next block can executable-separate integrity, authenticity, authorization and provenance or demonstrate a real trust-boundary failure;
2. open `M001` using authoritative Flutter/Dart/mobile source/model evidence while explicitly preserving runtime/device validation as OPEN;
3. `D002` or `Q002` if persistence/test-boundary risk becomes the stronger live-project prerequisite.

Do not extend Systems merely for rotation. Prefer M001 once source/model work can add professional value without pretending that source reading equals runtime validation.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
