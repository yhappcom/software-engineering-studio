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
- https://firebase.google.com/docs/auth/users
- https://firebase.google.com/docs/auth/limits
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

## NEW — startup initialization authority and enumeration-protection transfer

### SOURCE

Firebase recommends email-enumeration protection and states that projects created on or after 2023-09-15 have it enabled by default. With protection enabled, authentication APIs deliberately reduce account-existence-specific error information; for example `fetchSignInMethodsForEmail()` no longer reveals whether an account exists, and password-reset requests do not expose a missing account. Firebase also documents password policy as project configuration, including 6–30 character minimum configuration and Require/Notify enforcement modes.

### EXACT PRODUCT TRANSFER / CONTRADICTION

At the audited LogMate ref, `FirebaseAuthEngine._auth` initializes Firebase lazily only when an auth action or `readCurrentSession()` requests `_auth`. The comment explicitly says this delay exists so the first frame remains available offline. This was coherent with account-optional startup, but it is no longer sufficient as the routing authority for account-required startup. The new startup contract needs an explicit initialization phase that waits for the initialized Firebase Auth state before deciding Welcome versus restored-session routing. Lazy initialization may still be useful internally, but `null currentUser` observed before the startup boundary is established must never be interpreted as signed out.

The same exact source currently maps `email-already-in-use` to a product-visible `emailAlreadyInUse` outcome and `user-not-found` / `wrong-password` to `invalidCredential`; `signIn()` further renders most non-rate-limit failures as `Incorrect password.`. This error model assumes more account-existence/credential specificity than enumeration-protected Firebase is guaranteed to provide. Product behavior must remain correct when those specific codes collapse to `invalid-credential` or otherwise become less informative. Do not disable enumeration protection merely to preserve identifier-first UX or provider-discovery behavior.

### SYNTHESIS

Startup needs a provider-independent `AuthInitializationState` (or equivalent stream/port) distinct from `AuthSessionSnapshot?`: `uninitialized/initializing → initializedSignedOut | initializedAuthenticated(uid) | initializationFailure`. Welcome/Home routing begins only after the initialized state is authoritative. A recoverable initialization/network failure is not an explicit sign-out and must not unlock/rebind owner data.

Email UX should be enumeration-safe by construction. Login failure copy may say that the credentials could not be verified without asserting whether the email exists. Password reset should use an acceptance-style response that does not disclose account existence; the current `PasswordResetRequestOutcome.accepted` model already points in this direction. Account creation may still receive `email-already-in-use` depending on project/configuration/API behavior, but onboarding correctness must not depend on receiving that specific code.

Provider collision recovery must likewise not depend on `fetchSignInMethodsForEmail()` as an account-discovery oracle. The authenticated UID and explicit credential/link operations remain identity authority; email is presentation/contact data, not owner authority.

### Failure-first Codex contract

Add tests for: startup must not emit Welcome before Auth initialization completes; initialized restored UID routes through owner/setup state; initialization failure does not manufacture explicit sign-out; `invalid-credential` and less-specific enumeration-protected errors produce non-enumerating login copy; password reset missing/existing-account paths are presentation-equivalent where Firebase protection requires it; collision recovery never calls account-discovery APIs as owner authority; password validation does not hard-code 15 characters and has a defined behavior when Firebase policy configuration cannot be read/verified locally.

No runtime PASS is claimed. Exact Firebase project settings for enumeration protection, password policy mode/requirements, one-account-per-email behavior and provider enablement remain operational evidence dependencies.

## Account deletion / revocation transaction boundary

Firebase user deletion requires recent authentication. Apple-linked deletion is a multi-authority operation because provider revocation and Firebase identity deletion can partially succeed. Model deletion as an explicit retryable workflow, retain per-authority evidence until terminal completion, and do not conflate account deletion with local-ledger destruction. Exact ordering remains OPEN pending future Sync/backend and token-handling authority.

## Firebase Auth Emulator validation ladder

Use three evidence layers: pure product-state tests; Firebase Auth Emulator integration with independent account-state/UID oracles; then real Google/Apple Android/iOS/PWA validation. Emulator account clearing is fixture reset, not product deletion evidence.

## Durable onboarding completion and Previous Total boundary

Baseline presence, record count, Firebase authentication and widget route are not onboarding-completion authority. Persist explicit semantic decisions. At minimum distinguish owner ready, Previous Total pending/resolved (`configured` or `explicitlyNone`), optional import decision if product requires it, and committed setup completion. Explicit negative decisions are data and must survive restart.

Fresh-auth processing must be safe under duplicate provider callbacks, redirect replay and restart: observe authenticated UID; transactionally initialize-or-read owner binding; fail closed on owner mismatch; read durable setup milestones; resume first unresolved milestone; make each command idempotent/CAS guarded; commit setup completion only after prerequisites; route Home only after a fresh read of matching owner plus committed completion.

Exact repository inspection shows `completeInitialLogbookSetup()` currently writes `completed` without checking a Previous Total resolution prerequisite, while baseline configuration has its own atomic baseline/generation/checkpoint transaction. This is not an old-contract defect; it is the minimal persistence-contract delta exposed by the new product policy. Prefer an explicit durable Previous Total decision plus repository-level prerequisite enforcement over inferring resolution from nullable baseline or relying on UI sequencing. Exact schema/codec/migration implementation remains product work.

Failure-first tests must include crash/reopen after owner initialization, explicit-none persistence, baseline fault rollback, duplicate submit, completion-write failure, wrong UID, restored incomplete/complete setup, and transient Auth/network failure after established ownership.

## RELATED DOMAIN CHECK

- Foundations: direct Dart/Flutter JIT/AOT and bounded Chrome/Safari runtime evidence already exists; no blocker for this source/model block.
- Architecture: Auth initialization, identity, ledger owner, onboarding milestones, baseline data, optional import, Sync and deletion workflow state remain separate ownership dimensions.
- Mobile: native Google/Apple transport, PWA redirect replay and physical/provider lifecycle require separate validation.
- Data: first-owner initialization, setup milestones, baseline resolution and deletion journals require atomic/idempotent semantics.
- Quality: enumeration-safe error mapping, startup initialization, emulator integration, onboarding interruption/restart and deletion orchestration need failure injection and independent state oracles.
- Systems: owns identity/session/provider security, enumeration protection and revocation semantics.
- Design Studio: onboarding semantic actions and recovery copy downstream; persisted state must not be widget-route identity. Login/reset copy must not leak account existence.
- Web Manager: popup/redirect/authorized-domain deployment behavior downstream.
- Marketing Manager: no material dependency in this block.
- Product: exact LogMate ref inspected; no product files edited.

## HANDOFFS

- **LogMate / Codex:** introduce an explicit Auth-initialization boundary before startup routing; preserve UID as authority; make email sign-in/reset enumeration-safe; do not use `fetchSignInMethodsForEmail()` or email equality as owner/provider-discovery authority.
- **Quality:** table-test initialization delay/failure and enumeration-protected error collapse, then repeat with Auth Emulator/project configuration evidence.
- **Design Studio:** authentication error/reset copy must avoid revealing whether an email is registered; no canonical design files edited.
- **Data/Architecture:** retain separate owner/setup/baseline states and enforce Previous Total resolution before durable setup completion.

## OPEN / VALIDATION / CHANGE WATCH

- OPEN: product-canonical account-required update.
- OPEN: exact repository representation/transaction for semantic onboarding milestones and explicit-negative decisions.
- OPEN: whether initial import is a completion milestone or remains optional post-setup.
- OPEN: actual Firebase password policy, enumeration-protection, one-account-per-email, provider enablement/OAuth/SHA/Apple capability/Service-ID/authorized domains.
- OPEN: exact `google_sign_in` version/configuration during implementation.
- OPEN: executable typed-adapter/startup/enumeration tests and Firebase Auth Emulator integration on exact LogMate code.
- OPEN: exact FlutterFire native exception observations and real provider linking/cancellation/collision behavior.
- OPEN: deletion authority/order, backend/Sync deletion semantics, Apple revocation implementation, secure token/code handling, and local-ledger deletion-vs-lock policy.
- VALIDATION: no Auth/onboarding/provider/deletion runtime PASS claimed; startup initialization and onboarding restart/atomicity contracts remain unexecuted.
- CHANGE WATCH: Firebase Auth/FlutterFire/Auth Emulator, email-enumeration protection/password policy, `google_sign_in`, Apple account-deletion/revocation/linking policy, browser popup/redirect/persistence behavior, provider console configuration.
