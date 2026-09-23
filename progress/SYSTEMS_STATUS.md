# Systems Specialist Status

Track: Systems, Security, Performance & Delivery  
Prefix: `S###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-24

## Current evidence

### S001–S006
Retain prior Foundation evidence and OPEN boundaries: S001 trust/provenance, S002 threat/secrets, S003 cost/profiling, S004 dependency/build, S005 generic attestation/release, S006 rollback/publication durability. Exact-product release provenance, physical/native transfer and hard-power-loss evidence remain OPEN where previously recorded.

### S007 — Authentication identity, session persistence, and account-required onboarding
**IN STUDY — exact LogMate source transfer + provider/deletion/onboarding/startup/remote-invalidation boundaries + generic executable startup model VALIDATED; exact-product validation OPEN.** Canonical: `research/systems/S007_auth_identity_session_onboarding_foundations.md`; hosted validation record: `research/systems/S007_startup_model_hosted_validation_2026-09-24.md`; provider continuity transfer: `research/systems/S007_provider_link_unlink_identity_continuity_transfer.md`; remote invalidation transfer: `research/systems/S007_remote_session_invalidation_offline_authority_transfer.md`.

Exact product retained: `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`; production identity unknown. Product canonical still encodes account-free first use and remains in CONTRADICTION with newer account-required owner direction. The audited federated-auth operations doc also hard-codes a 15-character minimum, contradicting the newer decision that configured Firebase password policy is authoritative.

VALIDATION: Studio fixture `research/systems/fixtures/S007_auth_startup_state_model.py` at workflow head `1bc58ec210408a18cb4fd719be85b5b21e727d2e` executed on GitHub-hosted Ubuntu 24.04.5 / CPython 3.13.15. Actions run `35909442993`, job `107345269055`, completed successfully; the job log records all eight intended fail-closed startup tests `ok` and `Ran 8 tests ... OK`. This closes only the hosted verdict for the generic deterministic model. It does **not** validate LogMate Dart/Flutter code, Firebase persistence/Auth Emulator, Sembast atomicity, Google/Apple SDKs, Android/iOS, or PWA redirect lifecycle.

Retained auth transfer: account-required startup requires an explicit initialized Auth boundary before Welcome/Home; UID remains identity authority; enumeration-safe email/reset behavior must not depend on account-specific error leakage. Previous Total resolution remains an explicit durable prerequisite rather than nullable-baseline inference or UI sequencing.

Provider-continuity transfer: linking adds a credential to the currently authenticated UID and must not mutate ledger ownership or merge by email. Credential collision is recovery, not merge authority. Unlink requires a capability-based last-effective-recovery-method guard rather than a raw provider count; ambiguous unlink completion requires Firebase state reobservation before retry. Account deletion remains a separate workflow.

New remote-invalidation transfer: Firebase local session restoration and current local ledger ownership must be separated from fresh server acceptance. Firebase documents that Admin-side disable/delete does not itself trigger Flutter Auth streams; `reload()` is required to observe `user-disabled`/`user-not-found`. Network failure is not revocation; positive remote rejection is not generic sign-out. Offline-first operation means immediate remote revocation of already-downloaded local data cannot be promised. Cloud/Sync authority must stop on positively observed rejection, but local ledger read/write policy after such rejection is an OPEN PRODUCT DECISION. Auth rejection must never implicitly delete or rebind ledger data.

## Gate assessment
Systems Stage 1 remains **NOT PASS**. S007 has reproducible hosted executable evidence for the generic startup algebra, but exact LogMate Auth initialization, Auth Emulator, adapter mapping, provider link/unlink continuity, remote disable/delete/revoke observation, onboarding restart/atomicity, and real Firebase/native/PWA provider/revocation validation remain absent.

## HANDOFFS
- **LogMate / Codex:** reproduce the eight validated startup-model invariants in actual Dart/Flutter tests; implement provider link/unlink around same-UID continuity; model remote session freshness separately from local owner access; distinguish unreachable vs disabled/deleted vs explicit sign-out; never merge/delete/rebind ledger data from Auth callbacks.
- **Quality:** next require exact LogMate tests and Auth Emulator/Admin independent UID/account-state oracles, including disable/delete/revoke and network-vs-rejection discrimination.
- **Data/Architecture:** preserve separate owner/setup/baseline/provider/remote-authority states; decide post-positive-rejection local ledger policy explicitly.
- **Mobile:** real native Google/Apple and PWA redirect/link/unlink/reconnect lifecycle remain transfer targets; verify retained-provider recovery and remote rejection observation on Android/iOS/PWA.
- **Design Studio / Web Manager:** auth/recovery copy must remain enumeration-safe and distinguish transient offline state from positive account rejection; no canonical files edited.

## CHANGE WATCH / OPEN
- LogMate product-canonical account-required update and exact-product startup/Auth tests OPEN.
- Exact durable onboarding milestone representation, optional-import completion policy and crash/restart execution OPEN.
- Actual Firebase password/enumeration/provider configuration, `google_sign_in` implementation, Auth Emulator integration and FlutterFire native exception observations OPEN.
- Provider cancellation/redirect/collision/link/unlink/reauth/revocation and account-deletion authority/order OPEN; provider link/unlink semantic boundary is documented but not executable-product validated.
- Post-positive Firebase disabled/deleted local-ledger policy OPEN; exact persistence/recovery semantics for remote rejection OPEN.
- Firebase/FlutterFire/Auth Emulator, Google/Apple SDK/policy and browser redirect/persistence behavior remain CHANGE WATCH.
- S004/S005 exact-product release provenance and physical/native release evidence remain OPEN.

## Next work
Move evidence upward to exact LogMate provider-neutral/startup/link-unlink/remote-rejection tests and Firebase Auth Emulator integration rather than adding equivalent synthetic variants. For remote invalidation, use an independent Admin/Emulator oracle to disable/delete/revoke a known UID and prove the client distinguishes authoritative rejection from transport failure without mutating ledger ownership. Preserve the hosted startup model as a semantic oracle, not a product PASS.
