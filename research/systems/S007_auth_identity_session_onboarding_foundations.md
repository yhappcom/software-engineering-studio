# S007 — Authentication Session, Account-Required Startup, and Onboarding Foundations

Status: **IN STUDY — SOURCE/SYNTHESIS + EXACT-PRODUCT TRANSFER; EXECUTABLE VALIDATION OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-23

## Problem and scope

LogMate is moving from an account-optional local-first entry model to an account-required first-use model while preserving offline-first daily operation after ownership is established.

This study separates four concerns that must not be collapsed:

1. Firebase authentication identity/session;
2. local ledger ownership and local access;
3. first logbook-data onboarding (PreviousTotalBaseline, optional import, completion state);
4. server Sync eligibility and convergence.

The immediate live-project question is not visual styling. It is the startup/auth state machine that Codex must implement before Welcome/Onboarding UI is visually locked.

## Product evidence inspected

yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-23.

Default branch is **not** assumed production.

Relevant inspected product files include:

- MASTER.md
- docs/specs/startup-and-auth-entry-spec.md
- docs/specs/ui-contract.md
- docs/operations/federated-auth-providers.md
- codex/prompt.md
- lib/main.dart
- lib/auth/auth_engine.dart
- lib/application/logbook/local_ledger_auth_access_service.dart
- lib/application/logbook/local_ledger_access_coordinator.dart
- lib/repository/logbook/logbook_repository.dart
- lib/repository/logbook/sembast_logbook_repository.dart
- pubspec.yaml, firebase.json

### Current product-source observation

At e79f97c..., product source still treats account-free local use as first-class:

- Welcome retains Start a new logbook;
- LocalEntryState.notStarted / started / legacyUndetermined participates in startup;
- startLocalUse() is a supported command;
- unbound local-only Home can later expose Connect account;
- verified unbound auth uses explicit Connect this logbook claim.

Therefore the repository currently **contradicts the newly stated owner direction** below. Do not silently describe the source as already account-required.

## Authoritative sources

### SOURCE — Firebase Auth state restoration

Firebase Flutter documentation states that Auth state is persisted across app restarts/page reloads. On Android/iOS persistence is built in and not configurable; on web persistence is stored client-side and can be explicitly configured. Firebase recommends observing Auth state via authStateChanges()/related streams so the first event reflects restored credentials after initialization.

Sources:
- https://firebase.google.com/docs/auth/flutter/start
- https://firebase.google.com/docs/auth/flutter/manage-users
- https://firebase.google.com/docs/auth/users
- https://firebase.google.com/docs/auth/web/auth-state-persistence

### SOURCE — Federated auth

Firebase Flutter supports Google/Apple federated auth. Native and web paths differ; provider enablement and platform configuration are prerequisites. Provider authentication yields a Firebase user identity; provider linking is a separate operation.

Sources:
- https://firebase.google.com/docs/auth/flutter/federated-auth
- https://firebase.google.com/docs/auth/flutter/account-linking

### SOURCE — Password policy

Firebase Authentication supports console-configured password policy. Minimum password length is configurable from 6 to 30 characters, default 6; maximum can be configured up to 4096. Product UI and Firebase enforcement must agree.

Source:
- https://firebase.google.com/docs/auth/android/password-auth

### SOURCE — Apple login-service requirement

Apple App Review Guideline 4.8 requires an equivalent privacy-preserving login option when qualifying third-party/social login is used to establish or authenticate the primary account, subject to its stated exceptions.

Source:
- https://developer.apple.com/app-store/review/guidelines/

## Newly confirmed project direction

### PROJECT DECISION — account-required first use

Owner direction, 2026-09-23:

- remove Start a new logbook from the normal product path;
- V1 account methods: Apple, Google, email/password;
- no account-free first-use mode;
- once a user has authenticated and has not explicitly signed out, normal app launches should bypass Welcome and proceed according to onboarding completion;
- after established owner access, local/offline daily use remains available during ordinary network/Firebase unavailability;
- the app is pre-launch and has no existing users, so preservation of a legacy account-free production user population is not required;
- password rules should follow the configured Firebase policy rather than a product-hard-coded 15-character minimum.

This decision is not yet canonical LogMate repository truth until the product repository is updated.

## SYNTHESIS — state ownership model

### Authentication state is not the same as product onboarding state

Firebase Auth answers: **which Firebase user identity is currently restored/authenticated?**

The product must separately answer:

- which UID owns this local ledger?
- is local access durably unlocked or explicitly signed-out/locked?
- has first logbook-data setup completed?
- is Sync currently eligible/available?

A valid implementation must not infer any of these from a matching email string or from record count.

### Account-required does not imply network-required

For a pilot logbook, requiring a Firebase-backed identity on first setup can coexist with offline-first usage.

Once ownership is established, an ordinary network outage or transient Firebase/token-refresh failure should not be rewritten as an explicit user sign-out. Local operation may continue under the existing durable owner-access contract; Sync becomes unavailable/deferred.

### Restored Firebase session should bypass Welcome

Do not read currentUser prematurely during Firebase initialization and treat temporary null as signed out. Use the initialized Auth-state observation boundary. A restored authenticated user should then be routed by product state, not back through Welcome.

## Proposed account-required startup matrix

| Auth observation / local state | Expected product route |
| --- | --- |
| Auth initialized, no user | Welcome: Apple / Google / email |
| Authenticated UID, no local owner ledger yet | create/initialize ledger owned by that UID, then first-data onboarding |
| Authenticated matching UID + setup not complete | resume first-data onboarding |
| Authenticated matching UID + setup complete | Home |
| Authenticated different UID + existing bound local ledger | mismatch/recovery; never rebind or expose ledger |
| Explicitly signed out + bound local ledger | Welcome/sign-in required; preserve local DB but keep access locked |
| Established matching owner + transient network/Firebase service failure | local product access remains available if existing durable access contract allows it; Sync paused/degraded |
| Provider flow cancelled | return to origin with no durable owner/setup mutation |

This is a **SYNTHESIS/implementation target**, not executable validation evidence.

## Architecture impact on the existing LogMate model

### SUPERSEDE from normal product path

The new account-required direction makes these concepts unnecessary as ordinary first-use UX:

- Welcome Start a new logbook;
- account-free unbound Home access;
- startLocalUse() as a normal application command;
- local-only Home Connect account;
- local-only → authenticated Connect this logbook as the default new-user route;
- LocalEntryState as normal startup access authority.

Because the app has no released users, there is no production-user compatibility requirement to retain the old account-free onboarding.

### Do not delete security boundaries merely because the UX is simpler

Retain or replace with equivalent protections:

- Firebase UID remains the owner identity authority, not email;
- different UID cannot read/rebind/unlock an existing ledger;
- explicit sign-out locks local access while preserving local DB;
- passive network/Auth-service failure is not explicit sign-out;
- account deletion remains distinct from sign-out/local removal;
- Sync eligibility remains separate from local access.

### OPEN — internal schema cleanup strategy

“No released users” removes the external production-user migration requirement; it does **not** automatically prove that current capability/versioned repository code can delete LocalEntryState without controlled schema/test updates.

Codex must inspect current capability-v7 migration and fixture assumptions before removing stores/code. Development/test databases may be reset if product policy allows, but this must be explicit rather than accidental.

## Password policy refinement

### PROJECT DECISION

Do not hard-code a 15-character LogMate rule.

Use the Firebase Authentication password-policy configuration as the enforcement source of truth and keep UI validation aligned with that configuration.

### VALIDATION required

Before release, record the actual Firebase project policy and test:

- allowed minimum/maximum lengths;
- signup rejection at policy boundary;
- password change/recovery behavior;
- UI/server consistency;
- paste/password-manager/autofill behavior.

## Provider/account implications retained for later S007 blocks

- Google + Apple + email are the V1 methods.
- Linking is an authenticated-account operation, not signed-out auto-merge.
- Same email text is not owner authority.
- A credential already linked to another Firebase UID is a typed collision.
- Unlink must not strand the account without a usable login method.
- Provider cancellation must be no-mutation.
- Google/Apple availability must be validated across iOS, Android and PWA surfaces used by the same account.
- Account deletion/revocation requires a separate fail/retry model.

## Failure-first validation plan

Before any Auth/onboarding PASS, add executable evidence for at least:

1. restored session → setup complete → Home without Welcome;
2. restored session → setup incomplete → onboarding resume;
3. signed out → no Home exposure;
4. explicit sign-out → local lock persists across restart;
5. transient offline/network failure does not manufacture sign-out;
6. different Firebase UID cannot rebind/read existing owner ledger;
7. provider cancel → zero durable mutation;
8. first successful auth creates/assigns a new owner ledger exactly once;
9. duplicate callback/retry cannot create two ledgers or two owner transitions;
10. web reload/PWA restart and native app restart preserve the intended Auth/startup state.

Native, web/PWA, emulator and physical-device evidence are not interchangeable.

## RELATED DOMAIN CHECK

- **Foundations:** direct Dart/Flutter runtime evidence exists; no current blocker.
- **Architecture:** state ownership must separate Auth identity, local owner access, onboarding completion and Sync.
- **Mobile:** Android/iOS session restoration and PWA/browser persistence require cross-platform execution evidence.
- **Data:** removal of local-entry metadata affects capability-v7 schema/migration contracts; exact storage cleanup requires Data review.
- **Quality:** startup matrix requires failure-first state-transition and restart tests.
- **Systems:** canonical owner; authentication, identity, session persistence, provider configuration and trust boundaries.
- **Design Studio:** owns Welcome/provider/onboarding visual hierarchy and accessibility after state/action contract is fixed.
- **Web Manager:** PWA/auth-return-domain implications may require later handoff; no canonical file edited.
- **Marketing Manager:** not materially relevant to the technical state model.
- **Product:** exact LogMate ref inspected as above; product repo not edited in this study.

## HANDOFFS

### TO: LogMate / Codex

Update product canonical contracts before implementing provider UI:

1. record the account-required startup decision and supersede account-free local-use wording;
2. remove Start a new logbook from Welcome;
3. redefine fresh successful authentication as new owned-ledger initialization, not claim of a pre-existing account-free ledger;
4. preserve mismatch/sign-out/offline/security semantics;
5. route restored session + setup complete directly to Home;
6. route restored session + incomplete setup to onboarding resume;
7. inspect and deliberately retire or repurpose LocalEntryState/startLocalUse and related tests/schema; no silent deletion;
8. align password UI with actual Firebase password policy instead of fixed 15 characters;
9. implement provider-neutral contract before Apple/Google visual completion.

### TO: Architecture/Data/Quality/Mobile

- Architecture: review state-machine simplification and dependency direction.
- Data: determine clean capability-v7 retirement path for obsolete local-entry metadata.
- Quality: build the failure-first startup/auth oracle matrix.
- Mobile: execute cross-platform auth restoration/provider flows on Android/iOS/PWA.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN:** exact product-repository update that supersedes AUTH-E1/E2/E4/E5 account-free portions.
- **OPEN:** exact Firebase production password-policy configuration.
- **OPEN:** Google/Apple Firebase/provider-console enablement and per-platform OAuth/capability settings.
- **OPEN:** account deletion/revocation executable design.
- **VALIDATION:** no runtime claim in this note is promoted to product PASS.
- **CHANGE WATCH:** Firebase Auth behavior/docs, Apple App Review policy, provider SDK/plugin versions and browser persistence behavior.
