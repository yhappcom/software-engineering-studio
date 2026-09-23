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

## Firebase Auth Emulator validation ladder

Firebase officially supports a Local Emulator Suite Authentication emulator. This creates a stronger intermediate evidence rung between pure fake-adapter tests and real Google/Apple provider/device validation. Use three separate layers: pure product-state tests; Firebase Auth Emulator integration with independent account-state/UID oracles; then real Google/Apple Android/iOS/PWA validation. Emulator account clearing is fixture reset, not product deletion evidence.

## NEW — durable onboarding completion and Previous Total boundary

### EXACT PRODUCT TRANSFER

At the audited LogMate ref, `MASTER.md` already separates durable owner-access/local-entry/initial-setup/baseline metadata from Flight/Simulator record values. It also defines `PreviousTotalBaselineConfiguration` as an optional single durable value, explicitly distinguishes missing baseline from a sparse present baseline, and states that initial logbook setup normally offers Previous Total first, optional source/history import next, then manual entry. Users with no baseline and users with nothing to import remain supported. These are useful persistence primitives, but the current startup/auth spec still routes through account-free local entry and explicit unbound-ledger claim, which is superseded by the newer account-required owner direction.

### SYNTHESIS — do not use baseline presence as onboarding completion

`PreviousTotalBaselineConfiguration != null` cannot be the onboarding-complete predicate. A legitimate user may explicitly have no previous total; conversely a baseline may exist while another required onboarding decision is incomplete. Likewise record count, import history, or Firebase authentication cannot infer completion. Completion needs its own durable state.

Separate at least these facts:

- Firebase identity established for UID;
- local ledger owner initialized for that UID;
- Previous Total step resolved as either `configured(value)` or `explicitlyNone`;
- optional import step resolved as `completed/imported` or `skipped/notNow` according to product UX;
- onboarding completion committed.

An explicit negative decision is data. `No previous total` and `No import now` must survive restart rather than being represented by absence that is indistinguishable from an unfinished step.

### ENGINEERING JUDGMENT — monotonic durable state machine

Prefer a small monotonic setup state rather than a transient page index. A representative semantic progression is:

`ownerReady → previousTotalPending → previousTotalResolved → importDecisionPending → setupComplete`.

The exact UI may combine or reorder optional screens later, so persistence should store semantic milestones/decisions, not widget route names. If import is intentionally allowed after onboarding, `skip/notNow` should complete the initial decision without marking import permanently unavailable.

`setupComplete` must be written only after all mandatory semantic prerequisites are durably committed. Home routing reads the committed state; it must not infer success because the final screen was displayed or because an async save was started.

### Atomicity and idempotency boundary

Fresh-auth processing should be safe under duplicate provider callbacks, PWA redirect replay, app restart, and repeated startup observation:

1. observe authenticated Firebase UID;
2. transactionally initialize-or-read owner binding for that UID;
3. if owner mismatch, fail closed with no onboarding mutation;
4. read durable onboarding milestones;
5. resume the first unresolved semantic step;
6. each step command is idempotent or CAS/version guarded;
7. commit `setupComplete` only after prerequisite writes succeed;
8. route Home only after a fresh read observes matching owner + committed completion.

Previous Total value and the decision that the step is resolved should be committed atomically where practical. Otherwise a crash can create ambiguous states such as baseline written but step still pending, or step marked complete before the baseline is durable. If existing repository primitives cannot make them one transaction, define a deterministic recovery rule and test both interruption orders.

### Failure-first validation contract

Codex/product tests should include at least:

- crash/reconstruction after owner initialization but before Previous Total decision → resume Previous Total;
- `explicitlyNone` survives restart and does not loop back to Previous Total;
- configured baseline + resolved milestone survive restart consistently;
- failure writing baseline never advances the milestone;
- failure writing completion never routes Home;
- duplicate submit does not duplicate baseline/configuration generations or owner initialization;
- import skip survives restart but later import remains available if product policy permits;
- wrong UID cannot read/advance setup state;
- restored matching UID + incomplete setup resumes the first unresolved semantic step;
- restored matching UID + committed setup completion routes Home directly;
- transient network/Auth refresh failure after established owner does not erase local setup completion.

These are source/model requirements, not runtime evidence. Exact repository transaction support and executable tests remain OPEN.

### HANDOFFS — onboarding durability

- **LogMate / Codex:** preserve existing durable initial-setup/baseline primitives where they fit, but remove account-free inference. Add explicit semantic resolution for `no previous total` and optional-import decision; do not use null baseline, zero records, or page index as completion authority.
- **Data:** verify whether baseline write + milestone can share the canonical local transaction/CAS boundary; if not, specify crash recovery ordering.
- **Architecture:** keep Auth, owner binding, setup milestones, baseline data, and import availability separate concepts.
- **Design Studio:** UI may change screen composition without changing semantic persisted milestones; provide explicit No previous total / Skip import actions.
- **Quality:** build restart/interruption and duplicate-submit tests around every durable transition.

## RELATED DOMAIN CHECK

- Foundations: direct Dart/Flutter JIT/AOT and bounded Chrome/Safari runtime evidence already exists; no blocker for this source/model block.
- Architecture: Auth identity, ledger owner, onboarding milestones, baseline data, optional import, Sync and deletion workflow state remain separate ownership dimensions.
- Mobile: native Google/Apple transport, PWA redirect replay and physical/provider lifecycle require separate validation.
- Data: first-owner initialization, setup milestones, baseline resolution and deletion journals require atomic/idempotent semantics.
- Quality: typed mapping, emulator integration, onboarding interruption/restart and deletion orchestration need failure injection and independent state oracles.
- Systems: owns identity/session/provider security and revocation semantics.
- Design Studio: onboarding semantic actions and recovery copy downstream; persisted state must not be widget-route identity.
- Web Manager: popup/redirect/authorized-domain deployment behavior downstream.
- Marketing Manager: no material dependency in this block.
- Product: exact LogMate ref inspected; no product files edited.

## OPEN / VALIDATION / CHANGE WATCH

- OPEN: product-canonical account-required update.
- OPEN: exact repository representation/transaction for semantic onboarding milestones and explicit-negative decisions.
- OPEN: whether initial import needs a durable initial-decision milestone or can be omitted entirely from completion while remaining optional post-setup; product UX must decide without weakening Previous Total durability.
- OPEN: Firebase password policy, one-account-per-email/enumeration-protection, provider enablement/OAuth/SHA/Apple capability/Service-ID/authorized domains.
- OPEN: exact `google_sign_in` version/configuration during implementation.
- OPEN: executable typed-adapter tests and Firebase Auth Emulator integration on exact LogMate code.
- OPEN: exact FlutterFire native exception observations and real provider linking/cancellation/collision behavior.
- OPEN: deletion authority/order, backend/Sync deletion semantics, Apple revocation implementation, secure token/code handling, and local-ledger deletion-vs-lock policy.
- VALIDATION: no Auth/onboarding/provider/deletion runtime PASS claimed; onboarding restart/atomicity contract remains unexecuted.
- CHANGE WATCH: Firebase Auth/FlutterFire/Auth Emulator, `google_sign_in`, Apple account-deletion/revocation/linking policy, browser popup/redirect/persistence behavior, provider console configuration.
