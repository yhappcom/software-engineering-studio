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

Account deletion is a distributed multi-system operation, not a single `FirebaseUser.delete()` UI call. Potential authorities include:

1. LogMate server-side user/sync data when Sync exists;
2. Apple provider authorization when linked;
3. Firebase Authentication user identity;
4. local owner-bound ledger/device data.

These transitions can partially succeed. Therefore a client must not show `Account deleted` merely because one call succeeded, and must not destroy the only local recovery evidence before remote completion is known.

### ENGINEERING JUDGMENT — ordering and state model

Do not encode deletion as one optimistic boolean. Model at least `idle → reauthenticationRequired/authorized → deletionInProgress → completed | retryableIncomplete | outcomeUnknown | terminalFailure` with per-authority completion evidence retained until the operation reaches its defined terminal state.

The safest exact ordering depends on future Sync/backend authority and Apple-token handling, so no universal sequence is declared PASS here. Two alternatives have materially different failure modes:

- **Firebase-first:** removes the principal Firebase identity early, but later Apple/server cleanup may lose convenient authenticated authorization/context.
- **remote/provider cleanup first:** preserves Firebase identity for authenticated cleanup/retry, but a later Firebase deletion failure leaves an account whose provider/server side may already be partially revoked/deleted.

Therefore Codex should first introduce an orchestration boundary and explicit partial-state journal rather than hard-code an irreversible ordering before backend/Sync semantics are known.

Local ledger deletion is also a separate product choice from account deletion. If product policy says account deletion deletes local logbook data, perform it only at the explicitly defined terminal point and after any required export/warning. If policy instead retains an inaccessible local archive, preserve owner binding and lock it; never silently rebind it to a future UID.

### Apple-specific consequence

Apple revocation is not equivalent to Firebase user deletion. When Apple is linked, deletion orchestration needs an Apple revocation step using valid provider authorization material or an approved server-side mechanism. The current LogMate document says to preserve authorization code/token material, but long-lived sensitive token storage itself creates a security boundary. Prefer a design that minimizes client-side long-lived provider secrets/tokens; exact mechanism remains OPEN until implementation architecture is selected.

### Failure-first validation contract

Before release, executable tests should cover at least:

1. stale session → `requiresRecentLogin` → no deletion mutation before successful same-owner reauthentication;
2. reauthentication returns a different UID → fail closed, no deletion;
3. Apple revocation succeeds, Firebase deletion fails → durable `retryableIncomplete`, never false success;
4. Firebase deletion succeeds but final response is lost → `outcomeUnknown`; recover by re-observing auth/backend state rather than blindly recreating/rebinding;
5. network failure before any remote acceptance → retry without duplicating completed steps;
6. retry after an already-completed Apple revocation treats idempotent provider result correctly;
7. duplicate Delete taps/callbacks produce one logical deletion workflow;
8. local ledger remains protected throughout partial remote failure;
9. terminal completion cannot be emitted until every authority required by product policy is complete or explicitly reconciled;
10. crash/restart during each boundary resumes from durable step evidence rather than restarting irreversible steps blindly.

Fake/provider-port tests can validate orchestration and false-success prevention. They cannot prove real Apple token revocation, Firebase console configuration, provider credentials, backend deletion, or physical-device behavior.

## Account linking/unlinking consequence

Linking is credential-to-current-UID, not account merge. Assert UID before == UID after. A credential attached to another UID enters collision recovery. Unlink must ensure another usable login method remains and sensitive account changes may require recent authentication. Apple additionally requires explicit consent before linking Apple credentials to other data/accounts; this is a product/UX handoff and release-policy CHANGE WATCH.

## RELATED DOMAIN CHECK

- Foundations: Dart/Flutter runtime evidence exists; not the current blocker.
- Architecture: Auth identity, ledger owner, onboarding, Sync and deletion workflow state remain separate ownership dimensions.
- Mobile: native Google/Apple transport, revocation and physical/provider lifecycle require separate validation.
- Data: first-owner initialization and deletion journals must be atomic/idempotent; local destruction policy requires explicit product decision.
- Quality: typed mapping and deletion orchestration need failure injection, restart, duplicate-callback and false-success oracles.
- Systems: owns identity/session/provider security and revocation semantics.
- Design Studio: recovery/collision/reauth/deletion confirmation and partial-failure copy downstream.
- Web Manager: popup/redirect/authorized-domain deployment behavior downstream.
- Marketing Manager: no material dependency in this block.
- Product: exact LogMate ref inspected; no product files edited.

## HANDOFFS

### LogMate / Codex

Evolve existing `AuthEngine` behind provider-neutral typed results. For deletion, add an explicit orchestrator/state record before implementing irreversible calls. Require recent same-owner reauthentication, distinguish Apple revocation from Firebase deletion, preserve retry/unknown outcomes, and never report success from one sub-step. Do not choose local-ledger destruction semantics implicitly.

### Quality / Data / Mobile

Quality: fake-provider failure matrix plus deletion partial-success/crash/retry controls. Data: idempotent first-owner initializer and durable deletion-step journal if deletion spans restart. Mobile: real native provider/revocation behavior later; Web/PWA popup/redirect separately.

## OPEN / VALIDATION / CHANGE WATCH

- OPEN: product-canonical account-required update.
- OPEN: Firebase password policy, one-account-per-email/enumeration-protection, provider enablement/OAuth/SHA/Apple capability/Service-ID/authorized domains.
- OPEN: exact `google_sign_in` version/configuration during implementation.
- OPEN: executable typed-adapter tests and exact FlutterFire native exception observations.
- OPEN: provider linking under final project configuration; Firebase docs retain a known linking issue warning in some projects.
- OPEN: deletion authority/order, backend/Sync deletion semantics, Apple revocation implementation, secure token/code handling, and local-ledger deletion-vs-lock policy.
- VALIDATION: no Auth/onboarding/provider/deletion runtime PASS claimed.
- CHANGE WATCH: Firebase Auth/FlutterFire, `google_sign_in`, Apple account-deletion/revocation/linking policy, browser popup/redirect/persistence behavior, provider console configuration.
