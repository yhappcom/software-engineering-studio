# S007 — Authentication Session, Account-Required Startup, and Onboarding Foundations

Status: **IN STUDY — SOURCE/SYNTHESIS + EXACT-PRODUCT TRANSFER; EXECUTABLE VALIDATION OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-24

## Problem and product identity

LogMate is moving from account-optional local-first entry to account-required first use while preserving offline-first daily operation after ownership is established. Firebase identity/session, local-ledger ownership/access, onboarding completion, provider reachability, Sync eligibility, and account-deletion completion remain separate state dimensions.

Exact product evidence: `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`. Default branch is not assumed production. This ref still exposes account-free entry and therefore CONTRADICTS the newer owner direction.

## Retained SOURCE / TRANSFER VALIDATION

Firebase Flutter Auth persists sessions and emits initial auth state after locally stored credentials are restored; startup therefore needs an Auth-initializing state. Password policy is Firebase-configured rather than a LogMate hard-coded 15-character rule. Provider linking preserves the Firebase UID of the currently authenticated user; equal email or a credential belonging to another UID is not ledger-merge authority.

Current Flutter federated-auth guidance requires official `google_sign_in` for native Android/iOS Google, while Web uses Firebase popup/redirect. Apple can use FlutterFire `AppleAuthProvider`, with Web/native lifecycle/configuration differences. Exact LogMate dependency inspection found `firebase_auth 6.7.0`, `firebase_core 4.15.0`, `firebase_auth_web 6.3.0`, generated Web/Android/iOS Firebase options, and no direct `google_sign_in`. Generated app options do not prove provider-console/OAuth/SHA/Apple-capability readiness. Existing `AuthEngine` is email-centric but already maps Firebase errors into product failure codes.

Primary sources retained/checked 2026-09-24:
- https://firebase.google.com/docs/auth/flutter/start
- https://firebase.google.com/docs/auth/web/auth-state-persistence
- https://firebase.google.com/docs/auth/android/password-auth
- https://firebase.google.com/docs/auth/flutter/account-linking
- https://firebase.google.com/docs/auth/flutter/errors
- https://firebase.google.com/docs/auth/flutter/federated-auth
- https://firebase.google.com/docs/auth/flutter/manage-users
- https://firebase.google.com/docs/auth/android/apple
- https://firebase.google.com/docs/emulator-suite/connect_auth
- https://firebase.google.com/docs/reference/rest/auth
- https://developer.apple.com/support/offering-account-deletion-in-your-app
- https://developer.apple.com/documentation/accountorganizationaldatasharing/revoke-tokens

## PROJECT DECISION

Owner direction, 2026-09-23: remove normal `Start a new logbook`; first use requires Firebase-backed Apple, Google, or email; restored authenticated users route by onboarding state; established ownership remains offline-first; pre-launch/no released users means no production account-free compatibility obligation; configured Firebase password policy is authoritative. Product canonical update remains OPEN.

## SYNTHESIS — provider-neutral command and outcome algebra

The shared abstraction is a product state transition, not a shared provider transport. Keep commands distinct: `authenticate(provider)`, `reauthenticate(provider)`, `link(provider)`, and `unlink(provider)`.

Minimum typed outcomes: `authenticated(uid)`, `cancelled`, `credentialCollision`, `providerAlreadyLinked`, `providerUnavailableOrMisconfigured`, `networkOrOutcomeUnknown`, `rateLimited`, `requiresRecentLogin`, `accountDisabled`, `invalidCredential`, and fail-closed `failure`. Raw provider/Firebase codes are diagnostic metadata rather than product-state authority.

Firebase Flutter guidance establishes `FirebaseAuthException.code` as the programmatic discriminator rather than message parsing. Web additionally exposes browser lifecycle errors such as popup blocked/closed and network failure; those Web codes are not claimed as native Flutter observations.

`networkOrOutcomeUnknown` must not become `cancelled` or `signedOut`: redirect/process/network interruption can lose the response after a remote transition. Re-observe Firebase state before retrying durable owner/link/unlink/delete transitions.

## Startup/ownership matrix retained

| State | Route |
| --- | --- |
| Auth unresolved | startup/loading; no Welcome/Home decision |
| initialized + signed out | Welcome |
| authenticated UID + no owned ledger | idempotent UID-owner initialization → onboarding |
| matching UID + onboarding incomplete | resume onboarding |
| matching UID + onboarding complete | Home |
| different UID + bound ledger | mismatch/recovery; no data exposure/rebind |
| explicit sign-out + bound ledger | Welcome; DB retained and locked |
| established matching owner + transient transport failure | local access retained where durable contract permits; Sync degraded |

## Account deletion / revocation transaction boundary

### SOURCE

Firebase Flutter `User.delete()` requires recent authentication; stale credentials fail with `requires-recent-login`, after which the user should explicitly reauthenticate rather than sign out/in as an implementation shortcut. Apple requires App Store apps that support account creation to allow deletion initiation inside the app, and apps using Sign in with Apple should revoke Apple authorization tokens. Apple's revoke endpoint is idempotent at the protocol result level: HTTP 200 also covers a token that was already invalidated.

Exact LogMate operations evidence already says provider token revocation/account deletion is NOT IMPLEMENTED / NOT VERIFIED and blocks release on executable deletion/revocation evidence. It also says authorization code/token material needed by the approved revocation design must be preserved. This is a valid product operational requirement, but the exact secure storage/backend mechanism is not yet decided.

### SYNTHESIS

Account deletion is a distributed multi-system operation, not a single `FirebaseUser.delete()` UI call. Potential authorities include future LogMate server-side user/sync data, Apple provider authorization when linked, Firebase Authentication identity, and local owner-bound ledger/device data. These transitions can partially succeed. A client must not show `Account deleted` merely because one call succeeded, and must not destroy the only local recovery evidence before remote completion is known.

### ENGINEERING JUDGMENT — ordering and state model

Do not encode deletion as one optimistic boolean. Model at least `idle → reauthenticationRequired/authorized → deletionInProgress → completed | retryableIncomplete | outcomeUnknown | terminalFailure` with per-authority completion evidence retained until the operation reaches its defined terminal state.

The safest exact ordering depends on future Sync/backend authority and Apple-token handling, so no universal sequence is declared PASS here. Firebase-first removes the principal Firebase identity early but may remove convenient authorization/context for later cleanup. Remote/provider cleanup first preserves Firebase identity for retry but can leave a live Firebase account after provider/server cleanup. Introduce an orchestration boundary and explicit partial-state journal before irreversible calls.

Local ledger deletion is separate from account deletion. If product policy later chooses local destruction, perform it only at the explicitly defined terminal point and after any required export/warning. If policy retains an inaccessible archive, preserve owner binding and lock it; never silently rebind it to a future UID.

### Failure-first validation contract

Before release, executable tests should cover stale-session recent-login failure, wrong-UID reauthentication, partial Apple/Firebase success, response loss, retry, duplicate Delete, crash/restart, local-ledger protection, and a completion oracle that requires every authority selected by product policy.

Fake/provider-port tests can validate orchestration and false-success prevention. They cannot prove real Apple token revocation, Firebase console configuration, provider credentials, backend deletion, or physical-device behavior.

## NEW — Firebase Auth Emulator validation ladder

### SOURCE

Firebase officially supports a Local Emulator Suite Authentication emulator for prototyping/testing. The Auth emulator exposes REST endpoints to clear project accounts, inspect/patch emulator configuration, and retrieve out-of-band codes. Firebase's REST Auth API also documents deterministic email/password sign-up/sign-in responses including the returned Firebase `localId`/UID. Emulator transport is HTTP/local and explicitly not production security evidence.

### SYNTHESIS

This creates a stronger intermediate evidence rung between pure fake-adapter tests and real Google/Apple provider/device validation. It can validate real Firebase Auth client/backend semantics for email/password and account state without touching production credentials. It cannot validate Google/Apple OAuth consent, native SDK cancellation, Apple nonce/capability, Google SHA/OAuth configuration, browser popup/redirect lifecycle, provider revocation, or production persistence/security.

Use three separate layers rather than treating one test class as Auth PASS:

1. **Pure product-state tests:** fake provider/auth ports; exhaustively validate typed outcome mapping, no durable mutation on failure, startup routing, duplicate callback and owner-initializer idempotency.
2. **Firebase Auth Emulator integration:** real Firebase Auth SDK against emulator; validate email create/sign-in/sign-out/reauth/delete where supported, UID stability, initialized auth observation, same-UID owner gate, restart/reconstruction behavior that the harness can genuinely reproduce, and backend account existence/deletion via independent emulator REST oracle.
3. **Real provider/platform validation:** actual Google/Apple on Android/iOS/PWA plus project console configuration, cancellation, collision/link/unlink, redirect/popup, Apple revocation and physical/browser lifecycle.

### VALIDATION DESIGN

For emulator integration, do not let the app under test be its own oracle. Pair SDK observations with the emulator REST state where possible. Representative evidence contract:

`CLAIM`: a successful first Firebase authentication establishes one UID and repeated startup/auth observation does not create a second identity or second owner initialization.

`SPEC/PROPERTY`: Firebase UID is identity authority; owner initializer is idempotent per UID.

`TARGET`: exact FlutterFire/Firebase Auth adapter + owner initialization boundary.

`ORACLE`: SDK result UID plus independent emulator account state and durable local owner state/count.

`FAILURE MODEL`: duplicate callback, sign-out/re-sign-in, wrong UID, stale local owner, process/test reconstruction, deletion/recreation ambiguity.

`EVIDENCE LIMIT`: emulator PASS is not Google/Apple/provider-console/native/PWA/production PASS.

The emulator's account-clear endpoint is useful for deterministic fixture reset, but clearing accounts must never be confused with product account deletion semantics. Emulator configuration can expose `allowDuplicateEmails`; therefore the test harness must record its exact configuration rather than assume production one-account-per-email behavior.

### ENGINEERING JUDGMENT — Codex test order

Codex should make the provider-neutral/product-state suite pass first, then add Auth Emulator integration for email/UID/owner/session semantics, and only then spend effort on provider-specific E2E. This isolates product-state defects from OAuth/platform defects and provides a reproducible failure-first base before console/device work.

## Account linking/unlinking consequence

Linking is credential-to-current-UID, not account merge. Assert UID before == UID after. A credential attached to another UID enters collision recovery. Unlink must ensure another usable login method remains and sensitive account changes may require recent authentication. Apple additionally requires explicit consent before linking Apple credentials to other data/accounts; this is a product/UX handoff and release-policy CHANGE WATCH.

## RELATED DOMAIN CHECK

- Foundations: direct Dart/Flutter JIT/AOT and bounded Chrome/Safari runtime evidence already exists; the historical F001 blocker is stale.
- Architecture: Auth identity, ledger owner, onboarding, Sync and deletion workflow state remain separate ownership dimensions.
- Mobile: native Google/Apple transport, revocation and physical/provider lifecycle require separate validation.
- Data: first-owner initialization and deletion journals must be atomic/idempotent; emulator account reset is not a persistence oracle for local ledger durability.
- Quality: typed mapping, emulator integration and deletion orchestration need failure injection, independent state oracles, restart and duplicate-callback controls.
- Systems: owns identity/session/provider security and revocation semantics.
- Design Studio: recovery/collision/reauth/deletion confirmation and partial-failure copy downstream.
- Web Manager: popup/redirect/authorized-domain deployment behavior downstream.
- Marketing Manager: no material dependency in this block.
- Product: exact LogMate ref inspected; no product files edited.

## HANDOFFS

### LogMate / Codex

Evolve existing `AuthEngine` behind provider-neutral typed results. Build the validation ladder explicitly: pure state tests → Firebase Auth Emulator email/UID/owner integration → real Google/Apple Android/iOS/PWA validation. Record emulator configuration and use independent emulator REST/account-state oracles where possible. For deletion, add an explicit orchestrator/state record before irreversible calls. Do not choose local-ledger destruction semantics implicitly.

### Quality / Data / Mobile

Quality: fake-provider failure matrix plus emulator-backed UID/account-state integration and deletion partial-success/crash/retry controls. Data: idempotent first-owner initializer and durable deletion-step journal if deletion spans restart. Mobile: real native provider/revocation behavior later; Web/PWA popup/redirect separately.

## OPEN / VALIDATION / CHANGE WATCH

- OPEN: product-canonical account-required update.
- OPEN: Firebase password policy, one-account-per-email/enumeration-protection, provider enablement/OAuth/SHA/Apple capability/Service-ID/authorized domains.
- OPEN: exact `google_sign_in` version/configuration during implementation.
- OPEN: executable typed-adapter tests and Firebase Auth Emulator integration on exact LogMate code.
- OPEN: exact FlutterFire native exception observations and real provider linking/cancellation/collision behavior.
- OPEN: deletion authority/order, backend/Sync deletion semantics, Apple revocation implementation, secure token/code handling, and local-ledger deletion-vs-lock policy.
- VALIDATION: no Auth/onboarding/provider/deletion runtime PASS claimed; emulator evidence, when produced, must remain bounded to emulator-supported semantics.
- CHANGE WATCH: Firebase Auth/FlutterFire/Auth Emulator, `google_sign_in`, Apple account-deletion/revocation/linking policy, browser popup/redirect/persistence behavior, provider console configuration.
