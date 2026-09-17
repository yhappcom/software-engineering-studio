# S002 — Threat Modeling, Least Privilege, Secrets & Secure Storage Foundations

Status: **IN STUDY — first integrated executable Foundation block complete**  
Evidence date: 2026-09-18

## Problem and scope
Security controls are weak when chosen as a checklist without naming assets, actors, trust boundaries, authority, failure consequences, and attacker opportunities. This block establishes a reusable Foundation model linking threat modeling to least privilege and secret/storage boundaries. It does not claim a complete product threat model or platform-secure-storage validation.

## SOURCE
- NIST SP 800-154 remains an **Initial Public Draft**; NIST's 2025 planning note says it plans to finalize it. It defines threat modeling as risk assessment that models attack and defense aspects of an entity and emphasizes allocating limited security resources based on risk. Treat it as useful primary draft material, not final normative authority.
- NIST SP 800-53 Rev. 5.1 AC-6 defines least privilege as allowing only authorized access necessary to accomplish assigned tasks, applying the principle to users and processes.
- Android Keystore documentation states that Keystore can keep key material out of the application process and enforce authorized key uses outside the app process; hardware backing is conditional on device/key support and should be verified when relied upon.
- OWASP Secrets Management guidance treats secrets as lifecycle objects requiring creation, rotation, revocation/expiration, scoped access, and protection from logging/exposure. It is guidance, not a platform guarantee.

## SYNTHESIS — security reasoning chain
Use:

`asset/security property → actor/principal → entry point/data flow → trust boundary → authority granted → threat/failure path → control → residual risk → validation`

Threat, vulnerability, risk, control, and observed exploit are distinct claims. Encryption, secure storage, authentication, and least privilege solve different portions of the model.

Least privilege is not merely "few permissions." It requires authority to be scoped by **principal × resource × operation × context/lifetime** closely enough that compromise or misuse has a bounded blast radius while required work remains possible.

## EXECUTABLE VALIDATION — ambient vs scoped authority
Fixture: `research/systems/fixtures/S002_least_privilege_capability_boundary.py`

CLAIM: a component receiving ambient read authority can access unrelated sensitive state; a resource-scoped capability can block that access while preserving the required operation.

PROPERTY/ORACLE:
1. deliberately overprivileged component can read `tax`;
2. capability restricted to `profile` must reject `tax`;
3. the same restricted capability must still read `profile`.

ENVIRONMENT: Python 3.13.5, Linux container, 2026-09-18.

OBSERVATION:
- `ambient_authority=LEAKED:tax-adjustment`
- `scoped_authority=BLOCKED:tax`
- `required_operation=PASS:pilot-profile`

VERDICT: **PASS for the bounded authority model.** The alternative reduces authority without breaking the declared required operation.

FAILURE/ROOT-CAUSE STATUS: the leak is intentionally caused by excessive ambient authority. The fixture isolates authorization scope, not cryptographic confidentiality, OS sandbox escape, malicious native code, or a real plugin/runtime.

EVIDENCE LIMIT: this is a model-level executable comparison. It does not prove Android/iOS/Flutter enforcement, product security, or that capability-style APIs are universally preferable.

## Secrets and secure storage boundary
A secret should be modeled by owner/principal, purpose, permitted operations, storage location, exposure paths, lifetime, rotation/revocation, recovery, logging/telemetry behavior, and compromise response. "Encrypted" is not equivalent to "securely managed."

Android Keystore provides stronger key-material and usage boundaries than storing raw key bytes in ordinary app data when its guarantees apply, but it does not make a compromised app process harmless: official documentation explicitly notes an attacker controlling the process may be able to **use** app keys even when unable to extract key material. Therefore `non-exportable key ≠ unusable-by-compromised-authorized-process`.

## ENGINEERING JUDGMENT
For reusable application design, first minimize the authority a component receives; then protect any secret/key material needed for that authority. Secure storage cannot compensate for an unnecessarily broad authorization surface.

## RELATED DOMAIN CHECK
- Foundations: F002 resource/lifetime and F006 process/network boundaries materially support authority/exposure reasoning.
- Architecture: A002 ownership/dependency boundaries should make authority flow explicit; interfaces can narrow authority.
- Mobile: M003 should transfer-test sandbox/permission/Keystore/Keychain behavior on exact platforms.
- Data: data authority, backup, sync and deletion semantics determine which assets cross boundaries.
- Quality: Q006 fault campaigns should include revoked/expired/overbroad authority and fail-closed oracles.
- Systems: S001 artifact/provenance trust remains separate from runtime authorization and secret use.
- Design Studio: not materially relevant to this bounded mechanism.
- Web Manager: web/PWA credential storage and browser-origin boundaries are a later transfer, not inferred here.
- Marketing Manager: not materially relevant.
- Product source/ref: no product implementation audited in this block; no product security claim made.

## OPEN / VALIDATION / CHANGE WATCH
- OPEN: structured threat-model comparison on a real product subsystem with exact ref and declared version.
- VALIDATION: Android Keystore and Apple Keychain/secure-enclave behavior on real/simulator/device contexts as appropriate; permission revocation, process compromise assumptions, backup/restore, uninstall/reinstall and key invalidation.
- OPEN: secrets in CI/CD, backend/API credentials, Firebase rules/auth and client-public configuration distinctions.
- CHANGE WATCH: Android Keystore/attestation and Apple security APIs/platform policies are version/device sensitive. NIST SP 800-154 is still draft/planned for finalization and must not be cited as final.

## HANDOFFS
- Mobile/M003: transfer `principal × resource × operation × lifetime` into platform sandbox, permission and secure-storage validation; do not equate Keystore presence with full secret-system security.
- Architecture/A002-A003: treat authority width as part of interface/ownership design when security-relevant.
- Quality/Q006: add overprivilege/revocation/expired-secret failure cases with independent authorization oracles.
- Data: classify sensitive assets and authority before backup/sync/export paths are considered safe.
