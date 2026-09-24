# Systems Specialist Status

Track: Systems, Security, Performance & Delivery  
Prefix: `S###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-24

## Current evidence

### S001–S006
Retain prior Foundation evidence and OPEN boundaries: S001 trust/provenance, S002 threat/secrets, S003 cost/profiling, S004 dependency/build, S005 generic attestation/release, S006 rollback/publication durability. Exact-product release provenance, physical/native transfer and hard-power-loss evidence remain OPEN where previously recorded.

### S007 — Authentication identity, session persistence, and account-required onboarding
**IN STUDY — integrated product contract + two hosted failure-first semantic models + provider presentation package VALIDATED at bounded Studio scope; exact-product validation OPEN.** Canonical foundation: `research/systems/S007_auth_identity_session_onboarding_foundations.md`; integrated transfer authority: `research/systems/S007_logmate_auth_onboarding_integrated_product_contract_2026-09-24.md`; onboarding/deletion executable record: `research/systems/S007_onboarding_deletion_failure_first_model_2026-09-24.md`.

Exact product retained: `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`; production identity unknown. Product canonical still encodes account-free first use and remains in CONTRADICTION with newer account-required owner direction. The audited federated-auth operations doc also hard-codes a 15-character minimum, contradicting the newer decision that configured Firebase password policy is authoritative.

**VALIDATION — startup algebra:** fixture `research/systems/fixtures/S007_auth_startup_state_model.py`, exact workflow head `1bc58ec210408a18cb4fd719be85b5b21e727d2e`, run `35909442993`, job `107345269055`, completed successfully with eight fail-closed startup tests.

**NEW VALIDATION — onboarding/deletion semantics:** fixture `research/systems/fixtures/S007_onboarding_deletion_state_model.py`, exact workflow head `967e0e2b087cec80b767d6586b2208c1d07908d1`, run `35938569294`, job `107441122312`, completed success on GitHub-hosted `ubuntu-latest`. Nine tests encode the three explicit setup paths, non-inference of onboarding from data presence, UID mismatch fail-closed behavior, immutable initial setup selection, immediate deletion lock, same-UID reauthentication, identity-absence-not-erasure, local-erasure completion, and restart preservation of deletion lock. This is a bounded Studio reference-model verdict, not LogMate/Firebase/product execution.

Retained auth transfer: account-required startup requires an explicit initialized Auth boundary before Welcome/Home; UID remains identity authority; enumeration-safe email/reset behavior must not depend on account-specific error leakage. Linking adds credentials only to the current UID; collision is recovery, not merge authority; unlink requires a last-effective-recovery-method guard. Remote local-owner access and fresh cloud authority remain separate. Voluntary deletion is a resumable locked saga requiring server data, Firebase identity and device-local data erasure; identity absence alone is not completion. `lastSignInTime` is not product `lastSeenAt`; activity presence is a separate non-blocking server-observed signal.

**PROJECT DECISION — provider buttons:** Apple/Google branding remains provider-owned; Email is LogMate-owned. Reusable package `research/systems/fixtures/S007_auth_provider_buttons/ready_to_use/` separates native mobile, tablet and PWA surfaces. Latest hosted package validation run `35937075501`, job `107436392513`, Flutter 3.47.5 / Dart 3.13.4, reported no analysis issues and 17 tests/reference renders passed. Exact LogMate/provider runtime validation remains OPEN.

## Gate assessment
Systems Stage 1 remains **NOT PASS**. S007 now has two reproducible hosted semantic-model validations plus the provider-presentation package, but exact LogMate Auth initialization, durable onboarding persistence/atomicity, Auth Emulator/backend independent oracles, provider collision/link/unlink, remote invalidation, deletion-saga execution, presence backend, real local wipe, and native/PWA Google/Apple runtime remain absent.

## HANDOFFS
- **LogMate / Codex:** use the integrated contract plus both executable reference models. Reproduce the eight startup cases and nine onboarding/deletion cases in actual Dart/Flutter tests; do not infer onboarding from data presence or deletion completion from signed-out state.
- **Quality:** require exact LogMate tests and Auth Emulator/Admin independent UID/account-state oracles; inject crash/network failures around deletion lock, remote erasure, Firebase delete and local sanitization.
- **Data/Architecture:** preserve separate owner/setup/provider/remote-authority/deletion states and durable deletion milestones; UI route state is not the persistence oracle.
- **Mobile:** transfer the `ready_to_use/` presentation and real provider/restart lifecycles into exact artifacts.
- **Web Manager:** external account-deletion request remains required and must share deletion-coordinator semantics.
- **Design Studio:** recovery/deletion UI must not disclose account/provider existence or claim completion before the saga is terminal; no canonical files edited.

## CHANGE WATCH / OPEN
- LogMate product-canonical account-required update and exact-product startup/Auth/onboarding tests OPEN.
- Actual Firebase password/enumeration/provider configuration, Auth Emulator integration, FlutterFire exception behavior, Google/Apple provider setup and native/PWA lifecycle OPEN.
- Firebase collision/link guidance remains CHANGE WATCH; do not depend on `fetchSignInMethodsForEmail()` under enumeration protection.
- Provider cancellation/redirect/collision/link/unlink/reauth/revocation and account-deletion execution remain OPEN.
- Account deletion coordinator/idempotency, Apple revocation, external web path, actual local wipe and crash-resume execution OPEN.
- Authenticated presence backend/storage/throttle/privacy/retention and cross-surface transfer OPEN.
- Post-positive administrator disable/delete local-ledger policy remains OPEN and distinct from voluntary deletion.
- S004/S005 exact-product release provenance and physical/native release evidence remain OPEN.

## Next work
The semantic contract is now executable at Studio-model scope. The next meaningful rung is **exact LogMate transfer**, not another synthetic state variant: product-canonical account-required implementation, Dart/Flutter regression tests, durable persistence/process-death checks, Firebase Auth Emulator/backend independent oracles, then native/PWA provider transfer. If product implementation is not yet available, resume the Balance Loop rather than manufacturing product evidence.
