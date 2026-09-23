# S007 — Authentication Session, Account-Required Startup, and Onboarding Foundations

Status: **IN STUDY — SOURCE/SYNTHESIS + EXACT-PRODUCT TRANSFER; EXECUTABLE VALIDATION OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-24

## Problem and product identity

LogMate is moving from account-optional local-first entry to account-required first use while preserving offline-first daily operation after ownership is established. Firebase identity/session, local-ledger ownership/access, onboarding completion, provider reachability, and Sync eligibility remain separate state dimensions.

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
- https://firebase.google.com/docs/auth/web/apple

## PROJECT DECISION

Owner direction, 2026-09-23: remove normal `Start a new logbook`; first use requires Firebase-backed Apple, Google, or email; restored authenticated users route by onboarding state; established ownership remains offline-first; pre-launch/no released users means no production account-free compatibility obligation; configured Firebase password policy is authoritative. Product canonical update remains OPEN.

## SYNTHESIS — provider-neutral command and outcome algebra

The shared abstraction is a product state transition, not a shared provider transport. Keep commands distinct:

- `authenticate(provider)`
- `reauthenticate(provider)`
- `link(provider)`
- `unlink(provider)`

A minimum typed outcome vocabulary should distinguish:

| Product outcome | Representative lower-level evidence | Durable mutation rule |
| --- | --- | --- |
| `authenticated(uid)` | Firebase `UserCredential` established | owner/onboarding transition may begin only after UID is known |
| `cancelled` | provider/user closes or cancels UI; Web popup closed | no owner/onboarding mutation |
| `credentialCollision` | `account-exists-with-different-credential`, `credential-already-in-use` | no merge/rebind; recovery flow only |
| `providerAlreadyLinked` | provider already attached to current user | idempotent/no owner mutation; UI may report already connected |
| `providerUnavailableOrMisconfigured` | `operation-not-allowed`, unsupported environment, missing provider configuration | no durable mutation; operational remediation |
| `networkOrOutcomeUnknown` | network failure, redirect/process interruption before authoritative result | no optimistic completion; recover from Firebase state on restart/return |
| `rateLimited` | `too-many-requests`, quota/rate limiting | no durable mutation; retry/backoff UX |
| `requiresRecentLogin` | sensitive operation lacks recent proof | preserve state; invoke explicit reauthentication |
| `accountDisabled` | disabled Firebase user | deny cloud-sensitive operation; do not reinterpret as ordinary cancel |
| `invalidCredential` | expired/invalid/malformed credential where distinguishable | no durable mutation |
| `failure` | unclassified lower-level exception | fail closed; preserve diagnostic cause internally |

### SOURCE — Firebase error surface

Firebase Flutter error guidance establishes `FirebaseAuthException.code` as the stable programmatic discriminator rather than message parsing. It explicitly documents `too-many-requests` and `operation-not-allowed`, and the account-exists-with-different-credential recovery shape. Current Firebase JS Auth reference additionally exposes browser lifecycle codes such as `popup-blocked`, `popup-closed-by-user`, `network-request-failed`, `provider-already-linked`, `no-such-provider`, and `operation-not-supported-in-this-environment`. These are evidence for Web adapter classification, not proof that every code is emitted identically by FlutterFire on every platform.

**ENGINEERING JUDGMENT:** product enums must be intentionally coarser than SDK exception taxonomies. They should encode whether mutation/retry/recovery is safe, while retaining raw provider/Firebase code as diagnostic metadata. Do not create one enum member for every current SDK code; that couples product state to volatile SDK internals.

### Important ambiguity boundary

`networkOrOutcomeUnknown` must not be treated as `cancelled` or `signedOut`. A provider/backend operation may have succeeded remotely while the client lost the response. Recovery should re-observe authoritative Firebase Auth state before retrying owner initialization, linking, unlinking, or deletion. This is especially important for Web redirect/reload and process interruption.

### Collision recovery

Firebase documentation describes account-exists-with-different-credential as: authenticate with the existing provider first, then link the pending credential. For LogMate this is safe only if the authenticated Firebase UID is the expected LogMate owner. Equal email is discovery/recovery context, never ledger ownership authority.

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

Fresh-owner initialization and provider callback/redirect recovery must be idempotent. Explicit sign-out remains distinct from passive network/provider failure.

## VALIDATION design — adapter tests before provider UI

Source reading is insufficient for PASS. The next executable boundary can nevertheless validate product semantics without automating Google/Apple UI for every failure.

Build provider adapters behind injectable ports/fakes and execute table-driven tests asserting:

1. success returns exact UID before any owner mutation is permitted;
2. cancel/popup-close maps to `cancelled` and mutation count remains zero;
3. collision codes map to `credentialCollision`, preserve pending recovery metadata where safe, and never invoke owner rebind/merge;
4. operation-not-allowed/configuration errors map to `providerUnavailableOrMisconfigured`;
5. network failure maps to `networkOrOutcomeUnknown`, not sign-out/cancel;
6. too-many-requests maps to `rateLimited`;
7. recent-login-required maps to `requiresRecentLogin` for unlink/delete/sensitive operations;
8. provider-already-linked is distinguishable from another-user credential collision;
9. unknown SDK code fails closed while retaining code for diagnostics;
10. duplicate success callbacks or redirect recovery invoke idempotent first-owner initialization once;
11. reauthentication success must assert returned/current UID equals the ledger owner before sensitive mutation;
12. Web popup-blocked/closed and redirect-return-without-result do not complete onboarding.

Then add Firebase Emulator/runtime tests for email/session/startup where supported, and real provider/platform tests for Google/Apple lifecycle/configuration. Emulator adapter tests cannot prove provider console, OAuth, browser popup, Apple capability, or physical-device behavior.

**OPEN:** exact current FlutterFire exception emission must be captured during implementation; do not fabricate codes from Web docs as native Flutter evidence.

## Account linking/unlinking consequence

Linking is credential-to-current-UID, not account merge. Assert UID before == UID after. A credential attached to another UID enters collision recovery. Unlink must ensure another usable login method remains and sensitive account changes may require recent authentication. Apple additionally requires explicit consent before linking Apple credentials to other data/accounts; this is a product/UX handoff and release-policy CHANGE WATCH.

## RELATED DOMAIN CHECK

- Foundations: Dart/Flutter runtime evidence exists; not the current blocker.
- Architecture: Auth identity, ledger owner, onboarding, and Sync remain separate state ownership.
- Mobile: native Google/Apple transport and physical/provider lifecycle require separate validation.
- Data: first-owner initialization must be atomic/idempotent; account-free capability cleanup needs deliberate schema review.
- Quality: typed mapping needs executable mutation/no-mutation oracles and unknown-code negative control.
- Systems: owns identity/session/provider security semantics.
- Design Studio: recovery/collision/reauth copy and consent presentation downstream.
- Web Manager: popup/redirect/authorized-domain deployment behavior downstream.
- Marketing Manager: no material dependency in this block.
- Product: exact LogMate ref inspected previously; no product files edited.

## HANDOFFS

### LogMate / Codex

Evolve the existing `AuthEngine` instead of branching on raw Firebase/provider messages in Welcome. Add a provider-neutral typed result plus diagnostic metadata, then implement native Google, Apple, Web adapters behind it. Treat `networkOrOutcomeUnknown` as recoverable ambiguity: re-observe Firebase state before durable retry. Add table-driven adapter tests before UI polish. Do not auto-merge equal-email accounts or mutate ledger ownership on collision.

### Quality / Data / Mobile

Quality: build fake-provider exception matrix and mutation-count oracle. Data: expose idempotent first-owner initializer whose precondition is an established UID. Mobile: capture real native provider cancellation/configuration behavior later; Web/PWA separately capture popup/redirect interruption/reload.

## OPEN / VALIDATION / CHANGE WATCH

- OPEN: product-canonical account-required update.
- OPEN: Firebase password policy, one-account-per-email/enumeration-protection, provider enablement/OAuth/SHA/Apple capability/Service-ID/authorized domains.
- OPEN: exact `google_sign_in` version/configuration during implementation.
- OPEN: executable typed-adapter tests and exact FlutterFire native exception observations.
- OPEN: provider linking under final project configuration; Firebase docs retain a known linking issue warning in some projects.
- OPEN: deployed PWA popup/redirect recovery and account deletion/revocation transaction semantics.
- VALIDATION: no Auth/onboarding/provider runtime PASS claimed.
- CHANGE WATCH: Firebase Auth/FlutterFire, `google_sign_in`, Apple linking/consent policy, browser popup/redirect/persistence behavior, provider console configuration.
