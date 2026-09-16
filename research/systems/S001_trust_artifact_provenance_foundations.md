# S001 — Trust Boundaries, Artifact Identity & Build Provenance Foundations

Status: **IN STUDY — two integrated executable trust-boundary blocks complete**  
Date: 2026-09-16  
Lead: Systems

## Problem
A source commit, build invocation, produced artifact, checksum/provenance document, signer/verifier identity, authorization policy, deployed artifact and runtime observation are related but distinct objects. Security and release reasoning fails when one identity or trust claim is allowed to stand in for another.

## SOURCE
### NIST SP 800-207 — Zero Trust Architecture
NIST states that zero trust grants no implicit trust solely from network location or asset ownership. S001 transfers the general trust-boundary discipline cautiously: identity/location/ownership metadata is evidence input, not authorization or authenticity proof by itself.

Primary: https://csrc.nist.gov/pubs/sp/800/207/final

### NIST FIPS 186-5 — Digital Signature Standard
FIPS 186-5 states that digital signatures are used to detect unauthorized modification and authenticate the identity of the signatory. This supports separating data integrity/origin authentication from a bare digest. It does not imply that a valid signature means the signer is authorized by a particular product policy.

Primary: https://csrc.nist.gov/pubs/fips/186-5/final

### NIST SP 800-218 — Secure Software Development Framework 1.1
SSDF 1.1 remains the final secure-development baseline checked. NIST also lists SSDF 1.2 as a public draft; status must be rechecked before operational adoption.

Primary: https://csrc.nist.gov/pubs/sp/800/218/final

### SLSA v1.2
Current SLSA v1.2 defines provenance as verifiable information about where, when and how an artifact was produced. Its verification model requires more than reading provenance: a consumer evaluates authenticated evidence and policy/trust expectations. SLSA's Verification Summary Attestation model explicitly binds verification to a verifier, artifact subject, resource/purpose and verification result; it warns that compromise of the verifier remains outside that assurance.

Primary: https://slsa.dev/spec/v1.2/provenance  
Primary: https://slsa.dev/spec/v1.2/verification_summary

## SYNTHESIS
A release-evidence chain should keep these questions separate:

`source identity → build inputs/builder → artifact identity → evidence integrity/authenticity → signer/verifier identity → authorization/trust policy → deployment identity → runtime observation`

### Distinctions
- **integrity / byte identity:** did the observed bytes match an expected digest or protected statement?
- **authenticity / origin authentication:** can the consumer verify who authenticated the statement/artifact and that the protected statement was not altered?
- **authorization:** is that authenticated actor permitted by this consumer's policy to make this release/build/verification claim?
- **provenance:** what verifiable production history links the artifact to source/build inputs and builder?
- **deployment/runtime evidence:** what concrete artifact was installed/served and what did it do in a specified environment?

A valid digest does not authenticate the party that supplied the digest. A valid authenticated statement does not by itself authorize its signer for every purpose. Authentic provenance still depends on the trusted builder/verifier/control plane not being compromised.

## VALIDATION A — source ref alone is a weak artifact oracle
Fixture: `research/systems/fixtures/S001_artifact_identity.py`

A deterministic fixture created canonical and post-build-transformed artifacts with the same declared source ref. Both passed a source-ref-only verifier while independent SHA-256 comparison distinguished the byte outputs. This falsifies `same source ref ⇒ same validated artifact`.

Environment: Python 3.13.5; Linux 6.18.44 x86_64; glibc 2.41.

Evidence limit: digest equality is byte-identity evidence only; it is not provenance authenticity, software safety or malicious-builder resistance.

## VALIDATION B — checksum metadata is not self-authenticating
Fixture: `research/systems/fixtures/S001_trust_metadata.py`

### Test Evidence Contract
- **CLAIM:** if an attacker can replace both an artifact and adjacent unsigned checksum metadata, checksum equality can still pass; independently authenticated metadata can detect metadata rewriting, while authorization remains a separate policy decision.
- **SPEC/PROPERTY:** acceptance requires (1) artifact digest equals protected metadata digest, (2) metadata authentication succeeds under verifier-held trust material, and (3) authenticated builder identity is allowed by policy.
- **TARGET:** canonical artifact/metadata versus attacker-rewritten artifact+metadata; separate authentic-but-unapproved builder case.
- **INPUT/STATE:** canonical bytes `app-binary-v1`; tampered bytes `app-binary-v1+evil`; one trusted builder and one unapproved builder.
- **ORACLE:** independent SHA-256, HMAC authentication under verifier-held key, and explicit trusted-builder allow-list.
- **ENVIRONMENT:** Python 3.13.5; Linux 6.18.44 x86_64; glibc 2.41.
- **OBSERVATION:** unsigned checksum metadata rewritten to match the tampered artifact passed the weak checksum comparison. Canonical authenticated metadata passed. Rewritten metadata failed authentication when paired with the original trusted tag. A correctly authenticated statement naming an unapproved builder was detected as authentic but unauthorized.
- **VERDICT:** integrity metadata controlled by the same untrusted party as the artifact is not sufficient authenticity evidence; authenticity and authorization are distinct checks.
- **FAILURE MODEL:** artifact+metadata substitution and authenticated-but-unapproved identity.
- **REPRODUCTION DATA:** deterministic fixture contains all bytes, identities and policy values.
- **EVIDENCE LIMIT:** HMAC is a compact shared-secret demonstration, not public-key code signing, non-repudiation, certificate validation, transparency logging, SLSA conformance, key-compromise resistance, or production CI/CD evidence.

Observed digests:
- canonical SHA-256 `5127bc22f7e4f1e964a8233b0a81ce0747203170a9cd985285c05fcbac5a33e2`
- tampered SHA-256 `4e1a1990306c31209b449a799fa65cee3412ad27ed6ed8e1bf7c51bd980ba895`

### FAILURE / ROOT CAUSE
The weak verifier asks only whether artifact bytes agree with attacker-controlled metadata. The attacker can preserve that internal consistency by replacing both. The missing property is an independent trust anchor for the metadata. The second case demonstrates a different error: even authentic evidence can name an identity that policy does not authorize.

## CONTRADICTIONS
Shortcuts falsified:

`same source ref = same validated artifact`

`artifact hash matches adjacent checksum = artifact provenance is authentic`

`authenticated signer/builder = signer/builder is authorized for this purpose`

## ENGINEERING JUDGMENT
Trust is a relation among evidence, identity, policy and a threat model. Cryptography can protect evidence, but it cannot decide business/release authorization or eliminate compromise of the trusted signer/builder/verifier. Higher-risk pipelines should minimize and protect the trusted computing base and bind acceptance to explicit identities, purposes and artifacts.

## CROSS-REPOSITORY TRANSFER
### Web Manager
Current `yhappcom/web-manager/STATUS.md`, checked 2026-09-16, records `same source ref ≠ same accepted PWA artifact when build/post-build/origin differs`. Validation A independently transfer-validates that mechanism. Validation B adds a reusable warning for future web release evidence: a checksum published or mutable in the same untrusted path as the artifact is not an independent authenticity anchor. Browser/origin/service-worker acceptance remains Web Manager/product-owned.

No Web Manager canonical file was edited.

### Design Studio / Marketing Manager
Not materially relevant to this bounded trust mechanism. No files edited.

### Product repositories
No MintTap or LogMate implementation claim was required. No production ref is inferred.

## RELATED DOMAIN CHECK
- **Foundations:** F001 source/runtime/process distinctions retained; direct Dart/Flutter execution remains OPEN after environment recheck on 2026-09-16.
- **Architecture:** A001-A003 semantic contracts do not establish build/artifact authenticity.
- **Mobile:** future package/signing/store transfer remains OPEN.
- **Data:** migration/rollback evidence should bind to authorized application/schema artifact identity.
- **Quality:** Q001 Test Evidence Contract used; expected digest/metadata must have an independent basis proportionate to risk.
- **Systems:** owning track.
- **Web Manager:** current release-provenance guard checked; no external write.

## HANDOFFS
- **TO Quality:** release/e2e validation should record where expected artifact identity/provenance came from and whether the same actor/path can rewrite both target and oracle metadata.
- **TO Mobile:** future Android/iOS signing work must separate package digest, signer identity, certificate/key trust, store/distribution authorization and installed artifact/runtime evidence.
- **TO Data:** rollback/migration allow-lists should identify authorized release/schema versions, not only checksum equality.
- **TO Web Manager:** preserve independent trust for release metadata when moving from source-ref provenance to production artifact acceptance.

## OPEN / VALIDATION
- public-key signing/certificate/key-rotation and compromise/revocation evidence;
- least-privilege failure beyond release metadata;
- CI/CD control-plane versus user-build-step trust boundary;
- dependency/toolchain identity and reproducibility versus provenance;
- Android/iOS/Flutter package signing/store delivery transfer;
- resource measurement/profiling remains separate S003 work.

## CHANGE WATCH
- SLSA current version checked as v1.2 on 2026-09-16.
- NIST FIPS 186-5 is final; NIST notes a future correction/revision is planned, so operational cryptographic policy should recheck current errata/revision.
- NIST SSDF 1.1 remains final while 1.2 is listed as public draft; recheck before policy adoption.

## Current conclusion
Systems Foundation now distinguishes identity, integrity, authenticity, authorization and provenance. **A checksum can identify bytes without authenticating its source; authenticated evidence can establish origin without granting authorization; provenance can describe production history without making a compromised trusted builder safe.** Release validation therefore needs a concrete artifact plus an independent, policy-appropriate trust path—not merely matching metadata.