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
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### S001 — integrity, authenticity, authorization and provenance separation
Canonical: `research/systems/S001_trust_artifact_provenance_foundations.md`  
New fixture: `research/systems/fixtures/S001_trust_metadata.py`

The second S001 block deliberately replaced both an artifact and its adjacent unsigned checksum metadata. The weak verifier still accepted the tampered artifact because the attacker controlled both target and expected digest. When metadata authentication was independently anchored in verifier-held trust material, rewriting the metadata while reusing the trusted authentication tag failed. A separate case then produced valid authenticated metadata for an unapproved builder and correctly classified it as authentic but unauthorized.

Bounded result:
- byte-integrity metadata is not self-authenticating when the same untrusted path controls artifact and oracle metadata;
- authenticity and authorization are separate decisions;
- provenance/authenticated evidence still depends on a trusted builder/verifier/control plane.

Primary-source reinforcement: NIST FIPS 186-5 defines digital signatures as mechanisms for detecting unauthorized modification and authenticating signatory identity; SLSA v1.2 verification models trusted verifier identity, artifact subject and policy/purpose separately.

Evidence environment: Python 3.13.5 / Linux 6.18.44 x86_64 / glibc 2.41. HMAC is only a bounded shared-secret demonstration and is not claimed as public-key code signing, non-repudiation, SLSA conformance or production release evidence.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked this run: neither executable is available.
- **D001:** state/persistence/durability/authority model + SQLite application-process-kill evidence.
- **Q001:** weak-oracle defect + stronger exact/invariant oracle + reproducibility evidence; Test Evidence Contract promoted.
- **A001-A003:** change pressure/information hiding, state ownership/dependency direction, semantic contract/API compatibility with positive/counterexample fixtures and bounded product transfer.
- **S001 block 1:** same source ref can identify byte-distinct artifacts after build/post-build divergence.

## Cross-track handoffs
- **Quality:** release/e2e expected-digest/provenance metadata needs an independent trust basis; target and oracle must not silently share the same attacker-controlled source.
- **Mobile:** future Android/iOS signing work must distinguish package digest, signer identity, authorization/trust, distribution identity and installed runtime evidence.
- **Data:** migration/rollback acceptance should bind to authorized application/schema release identity.
- **Web Manager:** existing PWA same-source artifact guard is strengthened by the unsigned-checksum substitution counterexample; no external repository was edited.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated.

S001's immediate trust distinction is now materially stronger. Highest-value next candidates are:
1. `M001` — highest untouched MintTap/LogMate leverage; use authoritative Flutter/Dart/platform source/model evidence while keeping runtime/device claims OPEN unless trustworthy execution becomes available;
2. `S002` — threat modeling/least privilege if a concrete executable privilege-boundary failure can be produced;
3. `Q002` — test-level boundaries, because upcoming Mobile/Data work needs explicit unit/integration/system evidence allocation.

Do not continue cryptographic mechanism detail merely for continuity; return to Balance Loop.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.