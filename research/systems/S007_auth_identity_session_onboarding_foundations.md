# S007 — Authentication Session, Account-Required Startup, and Onboarding Foundations

Status: **IN STUDY — SOURCE/SYNTHESIS + EXACT-PRODUCT TRANSFER; EXECUTABLE VALIDATION OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-24

## Problem and scope

LogMate is moving from account-optional local-first entry to account-required first use while preserving offline-first daily operation after ownership is established. Firebase identity/session, local-ledger ownership/access, onboarding completion, provider reachability, and Sync eligibility remain separate state dimensions.

## Product evidence inspected

`yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`.

Default branch is **not** assumed production. At this exact ref the product still exposes `Start a new logbook`, `LocalEntryState`, `startLocalUse()`, local-only `Connect account`, and explicit unbound-ledger claim. This **CONTRADICTS** the newer owner direction; product canonical source has not yet been updated.

## Authoritative sources retained

### SOURCE — Firebase session and password policy

Firebase Flutter Auth persists authentication state across native app restarts and web reloads; native persistence is built in while web persistence is configurable. `authStateChanges()` emits its initial event after locally stored credentials, if any, are restored. Startup therefore needs an explicit Auth-initializing state; a transient pre-initialization null must not be treated as signed out.

Firebase Authentication password policy is console-configured. LogMate should not maintain an independent hard-coded 15-character minimum that can disagree with the backend.

Sources:
- https://firebase.google.com/docs/auth/flutter/start
- https://firebase.google.com/docs/auth/web/auth-state-persistence
- https://firebase.google.com/docs/auth/android/password-auth

### SOURCE — provider linking and collision

Firebase's Flutter account-linking contract identifies a person by the same Firebase UID after another provider credential is linked to the currently authenticated user. A credential already belonging to another Firebase user is not authority to merge LogMate ledgers.

Sources:
- https://firebase.google.com/docs/auth/flutter/account-linking
- https://firebase.google.com/docs/auth/flutter/errors

**CHANGE WATCH:** reproduce linking with the exact FlutterFire/plugin/project configuration before release; documentation alone is not PASS.

### SOURCE — Flutter federated provider mechanics

Current Firebase Flutter federated-auth guidance distinguishes Google from Apple:

- Google on native iOS/Android requires the official `google_sign_in` plugin to trigger Google authentication, then creates a `GoogleAuthProvider` credential for Firebase `signInWithCredential`.
- Google on Web uses Firebase popup/redirect provider flows.
- Apple can use FlutterFire `AppleAuthProvider`; current guidance uses `signInWithPopup` on Web and `signInWithProvider` on non-Web platforms. A manual Apple-platform nonce/ID-token credential path also exists when needed.
- FlutterFire exposes provider-specific linking and reauthentication variants; Web popup/redirect and native provider operations have different lifecycle boundaries.

Sources:
- https://firebase.google.com/docs/auth/flutter/federated-auth
- https://firebase.google.com/docs/auth/web/apple
- https://firebase.google.com/docs/auth/android/apple

Apple private-relay email and first-authorization-only profile fields remain attributes, not LogMate owner identity.

## TRANSFER VALIDATION — exact LogMate dependency/platform audit

Exact ref dependency evidence:

- Dart SDK constraint: `^3.10.7`.
- `firebase_auth: ^6.7.0`, lockfile exact `6.7.0`.
- `firebase_core: ^4.15.0`, lockfile exact `4.15.0`.
- lockfile exact `firebase_auth_web 6.3.0` and `_flutterfire_internals 1.3.77`.
- **No direct `google_sign_in` dependency exists in `pubspec.yaml`.** Therefore the current exact source cannot implement Firebase's documented native Google flow without an explicit dependency/configuration change.
- No `sign_in_with_apple` package is required by the simplest current FlutterFire Apple provider path; `AppleAuthProvider` is supplied by `firebase_auth`. A manual Apple credential/nonce path would be a separate implementation choice and may add dependencies.
- `firebase_options.dart` contains generated Web, Android, and iOS Firebase app options for project `logmate-pilot-logbook`; macOS/Windows/Linux are explicitly unsupported by that generated configuration.
- Web has an `authDomain`; Android and iOS Firebase app IDs are present. This proves generated app registration data exists, **not** that Google/Apple providers, OAuth clients, SHA fingerprints, authorized domains, Apple Service ID, Return URL, relay, or capabilities are correctly configured.
- `ios/Runner/Info.plist` at the exact ref contains ordinary app metadata/orientation keys but no provider-specific configuration observed in that file.
- `ios/Runner/Runner.entitlements` was not present at the inspected path. This is evidence that the expected conventional entitlement file is absent at that ref, not proof that the Xcode project has no Sign in with Apple capability through every possible configuration representation.

### Exact AuthEngine transfer

The existing `AuthEngine` is email-centric: `createAccount`, email/password `signIn`, password reset, email verification, session read and sign-out. `AuthFailureCode` already establishes the valuable precedent that presentation/application logic should not match raw English Firebase messages, but it does **not** yet represent provider cancellation, credential collision/provider-already-linked, popup/redirect interruption, or provider configuration failure precisely enough for Apple/Google lifecycle decisions.

`FirebaseAuthEngine` lazily initializes Firebase only when an Auth action/session read occurs. This supports offline first-frame availability, but startup routing must still distinguish `Auth initialization unresolved` from `initialized signed out`; simply reading `currentUser` at an arbitrary pre-initialization moment is not the desired startup oracle.

**TRANSFER VALIDATION:** provider-neutral expansion should evolve this existing boundary rather than put Firebase/provider exception switches into Welcome. Native Google needs an added dependency and platform configuration; Apple can initially remain within `firebase_auth` provider APIs if exact runtime/configuration validation supports that route.

## PROJECT DECISION — current LogMate direction

Owner direction, 2026-09-23:

- remove `Start a new logbook` from normal product entry;
- first use requires Firebase-backed Apple, Google, or email authentication;
- authenticated users who have not explicitly signed out bypass Welcome and route by onboarding state;
- established owner access remains local/offline-first during ordinary network/Firebase unavailability;
- LogMate is pre-launch with no released users, so no production account-free user population requires compatibility;
- password rules follow configured Firebase policy, not a product-fixed 15-character minimum.

This remains a project decision pending canonical LogMate repository update.

## SYNTHESIS — provider-neutral identity and command boundary

`Firebase UID` is the cloud account/owner identity key. Provider email, Apple relay email, display name, and provider subject metadata are attributes/credentials, not ledger-owner keys.

Recommended product-level operations remain distinct:

- `authenticate(provider)` → authenticated UID or typed cancellation/collision/configuration/transport/rate-limit/failure outcome;
- `reauthenticate(provider)` → fresh proof for sensitive operations and must resolve to the current owner UID;
- `link(provider)` → credential-to-current-user operation, assert UID before == UID after;
- `unlink(provider)` → Settings-only, ensure at least one usable method remains and verify post-operation reachability.

Provider adapters may differ by Android/iOS/Web/PWA. Native Google's `google_sign_in → GoogleAuthProvider credential → Firebase` chain is materially different from Web Firebase popup/redirect. Apple provider transport differs again. The shared abstraction is the product outcome/state transition, not the transport implementation.

### Fresh first authentication

On a fresh local store, successful Firebase authentication should initialize exactly one ledger ownership binding for that UID and then enter first-data onboarding. It should not ask the ordinary fresh user to claim a nonexistent account-free ledger.

### Existing bound ledger

If a local ledger is bound to UID A and Firebase restores/authenticates UID B, fail closed into mismatch/recovery. Never auto-rebind because emails match.

### Web/PWA redirect transaction boundary

A redirect may destroy the current Flutter page/process context. Redirect initiation and completion are separate phases. Never mark authentication, owner initialization or onboarding complete before the returned Firebase identity is established. After return, run the same idempotent ownership/onboarding transition used by native success.

## Proposed startup matrix

| Auth/local state | Route |
| --- | --- |
| Auth not initialized | startup/loading; no Welcome/Home decision yet |
| Auth initialized, no user | Welcome: Apple / Google / email |
| Authenticated UID, no owned ledger | idempotently initialize UID-owned ledger → onboarding |
| Matching UID + onboarding incomplete | resume onboarding |
| Matching UID + onboarding complete | Home |
| Different UID + bound ledger | mismatch/recovery; no ledger exposure/rebind |
| Explicitly signed out + bound ledger | Welcome; DB preserved but access locked |
| Matching established owner + transient network/Firebase outage | local access continues where durable access contract allows; Sync degraded |
| Provider cancel | origin screen; no durable owner/setup mutation |
| Credential belongs to another Firebase UID | typed collision/recovery; no automatic ledger merge |
| Web redirect initiated but no authenticated result recovered yet | pending/recoverable Auth transaction; no owner/setup completion |

This is **SYNTHESIS**, not executable validation.

## Architecture/data impact

The account-required model supersedes as ordinary UX: `Start a new logbook`, account-free Home, `startLocalUse()`, local-only `Connect account`, ordinary fresh-user `Connect this logbook`, and `LocalEntryState` as normal startup authority. No released users removes external migration compatibility, but does not prove capability-v7 stores/migrations/tests can be deleted without deliberate schema work.

Security boundaries retained: UID ownership, different-owner denial, explicit-sign-out durable lock, passive network failure ≠ sign-out, deletion ≠ sign-out, and Sync eligibility ≠ local access.

## Failure-first validation plan

Before PASS, execute at least:

1. restored session + setup complete → Home without Welcome;
2. restored session + setup incomplete → onboarding resume;
3. signed out → no Home exposure;
4. explicit sign-out → lock persists across restart;
5. transient offline/network failure does not manufacture sign-out;
6. UID B cannot rebind/read UID A ledger;
7. provider cancel → zero durable mutation;
8. duplicate auth callback/retry initializes owner/setup once;
9. link provider → UID unchanged;
10. credential used by another UID → no merge/owner mutation;
11. unlink last usable provider → blocked;
12. PWA redirect/popup interruption → no premature onboarding mutation;
13. native restart and web/PWA reload preserve routing;
14. native Google cancellation/failure is translated at adapter boundary without local mutation;
15. native Google success produces Firebase UID before any owner initialization;
16. Apple provider cancellation/failure produces no local mutation;
17. Apple first/later authorization and relay-email differences do not affect UID-based owner initialization;
18. reauthentication resolving to another UID blocks the sensitive operation.

Native, Web/PWA, emulator, and physical-device evidence are not interchangeable.

## Codex implementation consequence from exact dependency audit

Do not begin by writing one generic provider method and assuming dependencies already exist.

1. Canonically supersede account-free startup first.
2. Extend the product-level Auth boundary with typed provider operations/outcomes.
3. Add `google_sign_in` deliberately for native Google; rerun/verify FlutterFire and Android/iOS Google configuration rather than relying on transitive packages.
4. Prefer the current FlutterFire `AppleAuthProvider` provider path initially unless an identified requirement forces the manual nonce/plugin path; validate iOS capability and Android/Web Apple configuration separately.
5. Preserve Web popup/redirect as a distinct lifecycle implementation behind the shared semantic boundary.
6. Add adapter-level tests that prove raw provider/Firebase exceptions map to no-mutation/collision/configuration/ambiguous outcomes correctly.
7. Do not call provider support complete from `firebase_options.dart` presence or successful compilation; provider-console/capability/OAuth runtime validation remains mandatory.

## Alternatives considered

- **Auto-merge by equal email:** rejected.
- **Sign into provider B then merge UID B into UID A:** rejected for V1.
- **Never allow provider linking:** simpler initially but harms account reachability; keep Settings-only after executable validation.
- **One identical provider implementation for native and Web/PWA:** rejected; semantics can be shared, transport cannot.
- **Add a third-party Apple plugin immediately:** not justified by current evidence. FlutterFire already exposes Apple provider APIs; add another dependency only for a demonstrated requirement such as a chosen manual credential path.

## RELATED DOMAIN CHECK

- **Foundations:** direct Dart/Flutter runtime evidence exists; not the blocker.
- **Architecture:** Auth identity, ledger owner, onboarding state, and Sync eligibility remain separate ownership.
- **Mobile:** native Google dependency and native/Web provider lifecycle need separate transfer validation.
- **Data:** capability-v7 cleanup and idempotent first-owner initialization require schema/transaction review.
- **Quality:** provider exception mapping, cancel/restart/duplicate/redirect/collision oracles required.
- **Systems:** canonical owner for identity/session/provider security semantics.
- **Design Studio:** provider visual hierarchy/recovery copy downstream.
- **Web Manager:** PWA redirect/authorized-domain behavior later handoff.
- **Marketing Manager:** not materially relevant.
- **Product:** exact LogMate ref and dependencies inspected; no product files edited.

## HANDOFFS

### LogMate / Codex

The exact product does not currently include native Google's required `google_sign_in` dependency. Treat adding/configuring it as an explicit implementation slice. Apple can start from FlutterFire's `AppleAuthProvider` path, but provider enablement, iOS capability and Android/Web Apple configuration remain unverified. Expand `AuthEngine` at the semantic boundary rather than placing provider-specific exception logic in Welcome. Do not infer provider readiness from generated Firebase app options.

### Architecture / Data / Quality / Mobile

Architecture: review command/state ownership. Data: define atomic first-owner initialization and capability-v7 cleanup. Quality: implement adapter exception/outcome and lifecycle failure tests. Mobile: validate native Google and Apple separately from PWA.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN:** LogMate canonical update superseding account-free AUTH portions.
- **OPEN:** exact Firebase password policy, one-account-per-email and enumeration-protection configuration.
- **OPEN:** Google/Apple provider console/capability/OAuth/SHA/Service-ID/authorized-domain configuration.
- **OPEN:** exact `google_sign_in` version and configuration selected during implementation; it is absent at the audited product ref.
- **OPEN:** whether a manual Apple nonce/plugin path is required; current evidence does not justify it by default.
- **OPEN:** executable provider-linking behavior under the final FlutterFire/project configuration.
- **OPEN:** deployed PWA popup/redirect/reload/cancel recovery.
- **OPEN:** account deletion/revocation failure/retry design.
- **VALIDATION:** no runtime Auth/onboarding/provider PASS is claimed.
- **CHANGE WATCH:** Firebase Auth/FlutterFire, `google_sign_in`, Apple policy, browser popup/redirect/persistence behavior, provider console configuration.
