# S005 — CI/CD, Signing, Versioning, Reproducibility & Release Evidence

Status: **IN STUDY — two integrated executable Foundation blocks; real public-key signature boundary added**  
Evidence date: 2026-09-18

## Problem / scope
A green CI run, a version label, a signature, and a deployed artifact are different claims. Release acceptance needs an evidence chain that binds the intended source and build process to the exact bytes accepted for deployment.

## SOURCE

### GitHub artifact attestations
Current GitHub documentation states that artifact attestations create cryptographically signed claims about build provenance and can include repository, environment, commit SHA, triggering event and workflow linkage. GitHub explicitly warns that an attestation is not a guarantee that an artifact is secure; verification and policy evaluation are required.

Primary sources:
- https://docs.github.com/en/actions/concepts/security/artifact-attestations
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations

### SLSA
SLSA 1.2 treats provenance as verifiable information describing where, when and how an artifact was produced; stronger build levels strengthen provenance authenticity and build-platform integrity. Provenance does not establish application correctness.

Primary source:
- https://slsa.dev/spec/v1.2/build-provenance

### Semantic Versioning
SemVer 2.0.0 requires a declared public API for semantic-version claims and states that released version contents must not be modified. Build metadata does not affect version precedence. Versioning therefore communicates an API/change contract; it is not artifact identity or proof of byte equality.

Primary source:
- https://semver.org/spec/v2.0.0.html

### OpenSSL signature verification
Current OpenSSL `dgst` documentation states that `-sign` signs using a private key and `-verify` verifies the signature using the corresponding public key; verification returns success or failure for the supplied signature and input file. The documentation also explicitly limits `dgst` verification: it verifies the RSA/DSA/ECDSA signature itself and does not provide the surrounding signer-identification/certificate semantics of formats such as X.509, CMS or S/MIME.

Primary source:
- https://docs.openssl.org/3.0/man1/openssl-dgst/

## SYNTHESIS — release evidence chain
Use separate identities and verdicts:

`intended source/ref → resolved dependencies/toolchain → CI workflow/run → build output bytes/digest → signing/attestation subject → verification policy → release/version record → deployment target → runtime acceptance`

Invalid shortcuts:
- `CI green => releasable`;
- `version label matches => artifact bytes match`;
- `signature verifies => source/ref is intended`;
- `attestation exists => artifact is secure/correct`;
- `same source => reproducible bytes`;
- `deployed successfully => intended artifact was deployed`.

Signing authenticates a statement/object under a trust/key policy. It does not decide whether the signed object is the object the release intended. Version labels identify release semantics only under their declared versioning contract. Reproducibility is a separate property requiring controlled inputs and repeated build comparison.

## VALIDATION A — bounded release identity gate
Canonical fixture: `research/systems/fixtures/S005_release_identity_gate.py`

### Test Evidence Contract
- **CLAIM:** release acceptance that checks only a build number or payload presence can accept the wrong source or changed bytes; binding source identity, build identity and artifact digest rejects those bounded substitutions.
- **SPEC/PROPERTY:** accepted artifact must simultaneously match expected source, expected build identity and expected digest.
- **TARGET:** deterministic Python release-gate model, not GitHub Actions, Flutter signing or an app-store pipeline.
- **INPUT/STATE:** intended `source=abc123`, `build=42`, known payload digest; variants preserve build number while substituting either source identity or payload bytes.
- **ORACLE:** direct equality of independently supplied expected source/build plus SHA-256 digest of artifact bytes.
- **ENVIRONMENT:** Python 3.13.5, Linux 6.18.44 x86_64, 2026-09-18.
- **OBSERVATION:** intended artifact accepted; stale-source artifact rejected; same-source/build but changed bytes rejected.
- **VERDICT:** PASS for the bounded identity property.
- **FAILURE MODEL:** stale/wrong-source release and post-build/rebuild byte substitution under a reused build label.
- **REPRODUCTION:** run canonical fixture with Python 3.13.5.
- **EVIDENCE LIMIT:** no real signature, key custody, GitHub Actions runner, OIDC, attestation verification, app signing, reproducible build, deployment or store evidence.

Observed output:
```text
good= True
stale_source= False
rebuilt_bytes= False
PASS: release acceptance binds source, build identity and artifact bytes
```

## VALIDATION B — real public-key signature / exact-byte boundary
Canonical fixture: `research/systems/fixtures/S005_real_public_key_signature_boundary.py`

### Test Evidence Contract
- **CLAIM:** a real public-key signature verifier can distinguish the signed artifact bytes from changed bytes and can distinguish the corresponding verification key from an unrelated key; this does not by itself establish release authorization or provenance.
- **SPEC/PROPERTY:** OpenSSL SHA-256 signature verification must succeed for the original artifact under the signer's public key and fail after artifact-byte substitution or public-key substitution.
- **TARGET:** actual OpenSSL CLI signature generation/verification, using ephemeral RSA-2048 key pairs and one bounded artifact.
- **INPUT/STATE:** artifact bytes `artifact-v1\nsource=abc123\nbuild=42\n`; tampered variant appends `TAMPER\n`; a second independently generated RSA key pair supplies the wrong-key case.
- **ORACLE:** OpenSSL `dgst -sha256 -verify` exit/result plus independent SHA-256 comparison for byte substitution. The expected verification relation comes from OpenSSL's documented sign/verify semantics, not duplicated release-gate logic.
- **ENVIRONMENT:** OpenSSL 3.5.5 27 Jan 2026, Python 3.13.5, Linux x86_64 execution environment; evidence date 2026-09-18.
- **OBSERVATION:** original artifact/signature/public-key verification returned `Verified OK`; changed bytes returned verification failure; unrelated public key returned verification failure. Original SHA-256 was `8c827ea914a8256cec448cd7b3af2d86403abd73f620966ea2a6cf04eb88523c`; tampered SHA-256 was `34aa7c80e35a8c252228944b1f5488819edc5d4e3a90e970d004c09d3f229a67`.
- **VERDICT:** PASS for this bounded cryptographic binding property.
- **FAILURE MODEL:** post-sign artifact-byte substitution and verifier-key substitution.
- **REPRODUCTION:** canonical fixture generates fresh ephemeral keys each run; the artifact/tampered bytes and verification predicates are deterministic, while signature/key bytes are intentionally not asserted as reproducible.
- **EVIDENCE LIMIT:** not CI signing, GitHub attestation, certificate-chain validation, key custody/HSM, authorization, revocation, timestamping, transparency log, provenance, Android/iOS package signing, store delivery, or production evidence.

### FAILURE / ROOT CAUSE
The changed-byte case fails because verification covers a digest of the supplied message under the signature scheme; changing the message changes the verification relation. The unrelated-key case demonstrates a separate trust input: a cryptographically valid signature is meaningful only relative to the verification key selected by the verifier. The experiment does **not** prove that the selected key belongs to an authorized release signer. That policy/trust-anchor step remains separate.

### CONTRADICTION
The prior S005 evidence limit said there was no real signature evidence. That statement is now superseded for this bounded OpenSSL context. It remains true for CI, mobile/package signing, certificate/key lifecycle and production release systems.

## DEBUG / ROOT CAUSE — identity gate
The two model mutants exploit identity collapse. In one, the build number is retained while the source changes; in the other, source/build labels are retained while bytes change. A release gate that treats any one label as the whole artifact identity cannot distinguish these states. The bounded alternative keeps the identities independent and requires all declared predicates.

## ALTERNATIVES / trade-offs
- **Green CI only:** useful test evidence, but not release/artifact identity.
- **Version/build label only:** human/product release identity; insufficient for byte identity.
- **Digest only:** strong byte identity for a known artifact; does not explain source/build provenance or authorization.
- **Bare public-key signature:** binds message bytes to possession/use of a corresponding private key under the verifier-selected public key; key identity, authorization, custody, revocation and provenance remain separate.
- **Certificate/CMS/package-signing systems:** can add signer identity/chain/policy semantics but introduce certificate, trust-store, expiry/revocation and platform-policy dependencies.
- **Attestation + verification policy:** binds richer provenance claims and permits policy enforcement; still requires correctness/security tests and trustworthy workflow/platform assumptions.
- **Reproducible build comparison:** can strengthen source/input→byte confidence; requires controlled toolchain/environment and is not demonstrated here.

## ENGINEERING JUDGMENT
A release pipeline should produce evidence, not merely execute commands. The acceptance record should make it possible to answer which source/ref, resolved inputs/toolchain, workflow/run and exact artifact were approved, how authenticity/provenance were verified, what tests applied to that artifact, and what deployment target received it. A release version should not substitute for these identities. Bare signature verification is a useful mechanism rung, but production authorization requires a separately justified trust/key policy.

## RELATED DOMAIN CHECK
- **Foundations:** F001 execution/artifact boundaries and F006 external process boundaries support pipeline reasoning; direct Dart/Flutter execution remains unavailable after environment recheck on 2026-09-18.
- **Architecture:** A003 compatibility contracts determine what a version change means; A005 observer sets include release-visible behavior; A006 requires evidence identity/status to remain explicit.
- **Mobile:** Android/iOS signing, package identity, store delivery and Flutter build transfer remain OPEN.
- **Data:** migration/recovery evidence must bind the exact release artifact and schema behavior.
- **Quality:** green tests are evidence for their declared oracle/target, not authorization to release a different artifact; negative signature cases strengthen oracle sensitivity only for the stated cryptographic property.
- **Systems:** S001 provenance/trust and S004 dependency/build identity are direct prerequisites. S001's HMAC-only authenticity demonstration is now transfer-tested with an actual asymmetric public-key mechanism, but authorization remains independently OPEN.
- **Design Studio / Web Manager / Marketing Manager:** considered; this bounded signing mechanism does not alter their canonical decisions, so no external canonical file was edited.
- **Product source/ref:** no product audit required; no MintTap/LogMate production claim is made.

## HANDOFFS
### TO Quality
Bind release-test evidence to the exact artifact/digest or proven-equivalent build path. Negative verification should include changed artifact and wrong trust-key cases where signature identity matters.

### TO Mobile
When a trustworthy Flutter/mobile environment is available, transfer-test source/ref→canonical build→platform package signing→artifact digest→installed package signer/package identity. Do not treat this OpenSSL fixture as Android/iOS signing evidence.

### TO Systems S001/S006
S001 may reuse this asymmetric-key transfer as evidence that authenticity and authorization remain separate under a real signature mechanism. S006 rollback/release governance should preserve the accepted artifact and signer/trust-policy identity rather than rebuild an old source label by default.

## OPEN / VALIDATION / CHANGE WATCH
- **OPEN / VALIDATION:** direct GitHub Actions attestation generation/verification, OIDC/workflow permission boundaries, key compromise/revocation, certificate-chain policy, mobile signing, store delivery, reproducible-build comparison and deployment rollback.
- **OPEN:** distinguish build reproducibility from hermeticity and deterministic outputs with executable multi-build evidence.
- **CHANGE WATCH:** GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive; recheck before operational adoption.
- **CHANGE WATCH:** OpenSSL command/provider behavior is version-sensitive; this fixture records 3.5.5 and must not be generalized to platform package-signing semantics.
- **CHANGE WATCH:** product/mobile versioning schemes may not be SemVer; do not impose SemVer unless the product declares that contract.

## Gate effect
S005 now has SOURCE → MODEL → EXECUTABLE FAILURE/ALTERNATIVE plus a **real asymmetric public-key signing/verification mechanism** with changed-byte and wrong-key negative cases. Systems Stage 1 remains **NOT PASS** because real CI/OIDC/attestation, key lifecycle/authorization, mobile signing, reproducibility, deployment and production evidence remain open.
