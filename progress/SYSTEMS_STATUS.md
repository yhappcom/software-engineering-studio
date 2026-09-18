# Systems Specialist Status

Track: Systems, Security, Performance & Delivery  
Prefix: `S###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-18

## Current evidence

### S001 — Trust boundaries, artifact identity and build provenance foundations
**IN STUDY — two integrated executable trust-boundary blocks complete.** Canonical: `research/systems/S001_trust_artifact_provenance_foundations.md`. Source/build/artifact/deployment/runtime identity plus integrity/authenticity/authorization/provenance separation established. S005 now transfer-tests the authenticity/integrity distinction with a real asymmetric public-key mechanism; public-key lifecycle/authorization, CI trust boundary and mobile signing remain OPEN.

### S002 — Threat modeling, least privilege, secrets and secure storage
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S002_threat_model_least_privilege_secrets_secure_storage.md`. Principal × resource × operation × context/lifetime authority scoping, ambient-authority failure/scoped-capability alternative, secrets lifecycle and Android Keystore guarantee limits established. Real platform/product transfer OPEN.

### S003 — CPU, memory, I/O, network cost models and profiling
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S003_resource_cost_models_profiling_foundations.md`. Wall latency/CPU/allocation/I/O/network observables separated; bounded Python CPU-vs-wait-vs-allocation fixture complete. Variance, profiler alternatives, real I/O/network and Dart/Flutter/device transfer OPEN.

### S004 — Dependency, supply-chain and build-system fundamentals
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S004_dependency_supply_chain_build_system_foundations.md`. Manifest/resolved graph/content/toolchain/build/artifact/provenance identities separated; bounded resolution-drift and same-version integrity failure evidence complete. Direct Dart/pub/build transfer OPEN.

### S005 — CI/CD, signing, versioning, reproducibility and release evidence
**IN STUDY — two integrated executable Foundation blocks; real public-key signature boundary added.** Canonical: `research/systems/S005_ci_signing_versioning_release_evidence.md`. Fixtures: `research/systems/fixtures/S005_release_identity_gate.py`, `research/systems/fixtures/S005_real_public_key_signature_boundary.py`.

The original model separates CI verdict/version/source/artifact digest/signature-attestation/verification/deployment identities and rejects stale-source/changed-byte substitutions. New OpenSSL 3.5.5/Linux evidence uses actual RSA-2048 private/public key operations: the original artifact verifies, changed bytes fail under the original signature, and the original signature fails under an unrelated public key. This closes the prior "no real signature" gap only for a bounded asymmetric signature mechanism. It does not establish signer authorization, key custody/revocation, certificate chains, CI/OIDC, GitHub attestations, Android/iOS signing, store delivery or provenance.

### S006 — Rollback, incident evidence, production change safety and release governance
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S006_rollback_incident_change_safety_governance.md`. Rollback is a state-vector transition, not generally the inverse of deployment; bounded schema compatibility failure/restore alternative retained. Real deployment/mobile/incident transfer OPEN.

## Gate assessment
Systems Stage 1 remains **NOT PASS**. S001-S006 all have professional Foundation evidence and S005 now includes a real asymmetric signature mechanism with deliberate negative cases. Direct Dart/mobile/build-pipeline transfer plus real CI/OIDC/attestation, signer authorization/key lifecycle, reproducibility, deployment rollback/recovery and production evidence remain open.

## HANDOFFS
- **Foundations:** release/build/signing remains an external process/artifact/state boundary; direct Dart/Flutter execution remains OPEN.
- **Architecture:** A003/A006 compatibility and evidence-preservation rules apply to release signer/artifact identity.
- **Mobile:** transfer-test canonical Flutter build/sign/install/update and package signer identity before claiming mobile-signing equivalence.
- **Data:** migration/recovery evidence should bind to an authorized exact release artifact, not merely a version label.
- **Quality:** signature negative tests should include changed artifact and wrong verification-key cases; signature success is not a release-authorization oracle.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes this bounded cryptographic mechanism.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter execution remains unavailable as rechecked 2026-09-18; Python 3.13.5 and OpenSSL 3.5.5 are available.
- GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive.
- OpenSSL/provider behavior is version-sensitive; this evidence must not be generalized to platform package signing.
- Real CI/OIDC/workflow permissions, key compromise/revocation, certificate policy, Android/iOS signing, app-store delivery, reproducible-build comparison, staged deployment and rollback remain OPEN.

## Next work
Return to Balance Loop. S005's real-signature mechanism materially raises the evidence rung, so do not repeat equivalent local cryptographic variants. Direct Dart/Flutter/mobile execution remains first-attempt work whenever a trustworthy SDK/device environment becomes available. Otherwise prefer a genuinely stronger release boundary such as real CI/attestation/reproducible-build evidence when accessible, or another track's higher-value real transfer gap.
