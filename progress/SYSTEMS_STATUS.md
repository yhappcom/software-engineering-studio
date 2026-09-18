# Systems Specialist Status

Track: Systems, Security, Performance & Delivery  
Prefix: `S###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-18

## Current evidence

### S001 — Trust boundaries, artifact identity and build provenance foundations
**IN STUDY — two integrated executable trust-boundary blocks complete.** Canonical: `research/systems/S001_trust_artifact_provenance_foundations.md`. Source/build/artifact/deployment/runtime identity plus integrity/authenticity/authorization/provenance separation established. S005 transfer-tests the authenticity/integrity distinction with a real asymmetric public-key mechanism; public-key lifecycle/authorization, CI trust boundary and mobile signing remain OPEN.

### S002 — Threat modeling, least privilege, secrets and secure storage
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S002_threat_model_least_privilege_secrets_secure_storage.md`. Principal × resource × operation × context/lifetime authority scoping, ambient-authority failure/scoped-capability alternative, secrets lifecycle and Android Keystore guarantee limits established. Real platform/product transfer OPEN.

### S003 — CPU, memory, I/O, network cost models and profiling
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S003_resource_cost_models_profiling_foundations.md`. Wall latency/CPU/allocation/I/O/network observables separated; bounded Python CPU-vs-wait-vs-allocation fixture complete. Variance, profiler alternatives, real I/O/network and Dart/Flutter/device transfer OPEN.

### S004 — Dependency, supply-chain and build-system fundamentals
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S004_dependency_supply_chain_build_system_foundations.md`. Manifest/resolved graph/content/toolchain/build/artifact/provenance identities separated; bounded resolution-drift and same-version integrity failure evidence complete. Direct Dart/pub/build transfer OPEN.

### S005 — CI/CD, signing, versioning, reproducibility and release evidence
**IN STUDY — three integrated executable Foundation blocks; real signature + bounded reproducible-build evidence.** Canonical: `research/systems/S005_ci_signing_versioning_release_evidence.md`, `research/systems/S005_reproducible_build_boundary.md`. Fixtures: `research/systems/fixtures/S005_release_identity_gate.py`, `research/systems/fixtures/S005_real_public_key_signature_boundary.py`, `research/systems/fixtures/S005_reproducible_build_boundary.py`.

The signature block uses actual RSA-2048/OpenSSL verification and deliberate changed-byte/wrong-key negatives. The reproducibility block uses GCC 14.2.0/ld 2.44 to build identical C source in two absolute directories at different wall-clock times. Naive, fixed-time-only, and path-map-only builds differed; `SOURCE_DATE_EPOCH=1700000000` plus per-directory `-ffile-prefix-map=...=/src` produced byte-identical executables with SHA-256 `69c2e47764cc2a982a4a4cc1a535eb06e3a032a6450aee63875ac1fc12395dba`. This is bounded same-host/toolchain reproducibility, not hermeticity or Flutter/mobile build evidence.

### S006 — Rollback, incident evidence, production change safety and release governance
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S006_rollback_incident_change_safety_governance.md`. Rollback is a state-vector transition, not generally the inverse of deployment; bounded schema compatibility failure/restore alternative retained. Real deployment/mobile/incident transfer OPEN.

## Gate assessment
Systems Stage 1 remains **NOT PASS**. S001-S006 all have professional Foundation evidence. S005 now has two materially different real mechanisms: asymmetric signature verification and bounded compiler artifact reproducibility with failure isolation. Direct Dart/mobile/build-pipeline transfer plus real CI/OIDC/attestation, signer authorization/key lifecycle, cross-host/toolchain reproducibility, deployment rollback/recovery and production evidence remain open.

## HANDOFFS
- **Foundations:** release/build/signing remains an external process/artifact/state boundary; direct Dart/Flutter execution remains OPEN.
- **Architecture:** A003/A006 compatibility and evidence-preservation rules apply to release signer/artifact/build-input identity.
- **Mobile:** transfer-test canonical Flutter build twice with exact toolchain/lock/build/post-build provenance; separate unsigned reproducibility from Android/iOS signing/package identity.
- **Data:** migration/recovery evidence should bind to an authorized exact release artifact, not merely a version label or rebuilt source label.
- **Quality:** reproducibility needs its own byte-identity oracle and deliberate input-drift negatives; byte equality is not functional correctness. Signature negatives should include changed artifact and wrong verification-key cases.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes these bounded build/signature mechanisms.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter execution remains unavailable as rechecked 2026-09-18; Python 3.13.5, OpenSSL 3.5.5, GCC 14.2.0 and GNU ld 2.44 are available.
- GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive.
- OpenSSL/provider and compiler/linker reproducibility behavior are version-sensitive; local evidence must not be generalized to platform package signing/builds.
- Real CI/OIDC/workflow permissions, key compromise/revocation, certificate policy, Android/iOS signing, app-store delivery, independent-host/container reproducibility, hermeticity, staged deployment and rollback remain OPEN.

## Next work
Return to Balance Loop. S005's prior named reproducible-build gap is now closed only for a bounded GCC/Linux same-host fixture, so do not repeat local compiler variants. Direct Dart/Flutter/mobile execution remains first-attempt work whenever a trustworthy SDK/device environment becomes available. Otherwise prefer a genuinely stronger evidence rung such as real CI/attestation, independent-environment/canonical-product rebuild, natural exact-ref product transfer, or another track's higher-value real boundary.
