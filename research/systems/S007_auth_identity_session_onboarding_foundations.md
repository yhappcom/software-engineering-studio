# S007 — Authentication Session, Account-Required Startup, and Onboarding Foundations

Status: **IN STUDY — SOURCE/SYNTHESIS + EXACT-PRODUCT TRANSFER; EXECUTABLE VALIDATION OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-23

## Problem and scope

LogMate is moving from an account-optional local-first entry model to an account-required first-use model while preserving offline-first daily operation after ownership is established. The model separates Firebase identity/session, local-ledger ownership/access, onboarding completion, and Sync eligibility.

## Product evidence inspected

`yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-23`.

Default branch is **not** assumed production. At this exact ref the product still exposes `Start a new logbook`, `LocalEntryState`, `startLocalUse()`, local-only `Connect account`, and explicit unbound-ledger claim. This **CONTRADICTS** the newer owner direction; product canonical source has not yet been updated.

## Authoritative sources

### SOURCE — Firebase session and password policy

Firebase Flutter Auth persists authentication state across native app restarts and web reloads; native persistence is built in while web persistence is configurable. Startup must observe initialized Auth state rather than treating a transient pre-initialization null as signed out.

Firebase Authentication password policy is console-configured. LogMate should not maintain an independent hard-coded 15-character minimum that can disagree with the backend.

Sources:
- https://firebase.google.com/docs/auth/flutter/start
- https://firebase.google.com/docs/auth/flutter/manage-users
- https://firebase.google.com/docs/auth/web/auth-state-persistence
- https://firebase.google.com/docs/auth/android/password-auth

### SOURCE — provider linking and collision

Firebase's Flutter account-linking contract identifies a person by the same Firebase UID after a second provider credential is linked to the currently authenticated user. `linkWithCredential()` has distinct failure classes including `provider-already-linked`, `invalid-credential`, and `credential-already-in-use`. Therefore a provider credential that already belongs to another Firebase user is not authority to merge LogMate ledgers.

Firebase's Flutter error documentation also exposes `account-exists-with-different-credential` under the one-account-per-email setting. Its documented recovery flow first authenticates the existing account and then links the pending credential. This is materially different from treating equal email text as owner authority.

Sources:
- https://firebase.google.com/docs/auth/flutter/account-linking
- https://firebase.google.com/docs/auth/flutter/errors

**CHANGE WATCH:** Firebase's account-linking documentation currently carries a known-issue warning for some projects/platform pages. Before relying on linking for release, reproduce the exact FlutterFire/plugin/project configuration rather than promoting documentation examples directly to PASS.

### SOURCE — unlink is identity-destructive, not cosmetic

Firebase documents that unlinking a provider removes that sign-in method. Platform documentation warns that signing in again with an unlinked provider can create a new separate Firebase user rather than restoring the former link. Therefore LogMate must not expose unlink as a harmless preference toggle.

Source:
- https://firebase.google.com/docs/auth/flutter/account-linking
- https://firebase.google.com/docs/auth/android/account-linking

### SOURCE — Apple cross-platform and privacy boundaries

Apple states Sign in with Apple can be offered across Apple and non-Apple platforms. Apple's authentication documentation uses a nonce to bind an authorization response to a client session. Firebase's Apple flows likewise require secure nonce handling in manual flows. Apple private-relay identities require applicable anonymized-data rules; relay email must not be treated as LogMate ownership authority.

Sources:
- https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple/
- https://developer.apple.com/documentation/signinwithapple/authenticating-users-with-sign-in-with-apple
- https://firebase.google.com/docs/auth/android/apple
- https://firebase.google.com/docs/auth/web/apple

## PROJECT DECISION — current LogMate direction

Owner direction, 2026-09-23:

- remove `Start a new logbook` from normal product entry;
- first use requires Firebase-backed Apple, Google, or email authentication;
- authenticated users who have not explicitly signed out bypass Welcome and route by onboarding state;
- established owner access remains local/offline-first during ordinary network/Firebase unavailability;
- LogMate is pre-launch with no released users, so no production account-free user population requires compatibility;
- password rules follow configured Firebase policy, not a product-fixed 15-character minimum.

This remains a project decision pending canonical LogMate repository update.

## SYNTHESIS — provider-neutral identity state machine

### Stable authority

`Firebase UID` is the cloud account/owner identity key. Provider email, Apple relay email, display name, and provider subject metadata are attributes/credentials, not ledger-owner keys.

### Fresh first authentication

On a fresh local store, successful Firebase authentication should initialize exactly one ledger ownership binding for that UID and then enter first-data onboarding. It should not ask the ordinary fresh user to "claim" a nonexistent account-free ledger.

### Existing bound ledger

If a local ledger is already bound to UID A and Firebase restores/authenticates UID B, fail closed into mismatch/recovery. Never auto-rebind because emails match.

### Linking

Provider linking is allowed only while an existing Firebase user is authenticated and after the new provider credential has been obtained for **linking**, not after signing into a second Firebase account and attempting to merge data. Successful linking preserves the Firebase UID. `credential-already-in-use` / `account-exists-with-different-credential` are typed recovery states, not merge authorization.

### Unlinking

Before unlink, compute whether at least one independently usable sign-in method will remain. Require recent authentication where Firebase/security policy requires it and explicit user intent. Treat provider revocation as a separate provider-specific operation where required. A successful unlink changes future account reachability and therefore needs failure/retry handling and tests.

### Cancellation and ambiguity

Provider cancellation is a no-mutation outcome. Network interruption or browser redirect loss can be ambiguous; do not persist owner/setup transitions until Firebase identity success is established and local ownership initialization is committed idempotently.

## Proposed startup matrix

| Auth/local state | Route |
| --- | --- |
| Auth initialized, no user | Welcome: Apple / Google / email |
| Authenticated UID, no owned ledger | idempotently initialize UID-owned ledger → onboarding |
| Matching UID + onboarding incomplete | resume onboarding |
| Matching UID + onboarding complete | Home |
| Different UID + bound ledger | mismatch/recovery; no ledger exposure/rebind |
| Explicitly signed out + bound ledger | Welcome; DB preserved but access locked |
| Matching established owner + transient network/Firebase outage | local access continues where durable access contract allows; Sync degraded |
| Provider cancel | origin screen; no durable owner/setup mutation |
| Credential belongs to another Firebase UID | typed collision/recovery; no automatic ledger merge |

This is **SYNTHESIS**, not executable validation.

## Architecture/data impact

The new account-required model supersedes as ordinary UX: `Start a new logbook`, account-free Home, `startLocalUse()`, local-only `Connect account`, ordinary fresh-user `Connect this logbook`, and `LocalEntryState` as normal startup authority. No released users removes external migration compatibility, but does not prove capability-v7 stores/migrations/tests can be deleted without deliberate schema work.

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
9. link provider to authenticated UID → UID unchanged;
10. credential already used by another UID → no merge/owner mutation;
11. unlink last usable provider → blocked;
12. unlink non-last provider → remaining provider still authenticates same UID;
13. PWA redirect/popup interruption → no premature onboarding mutation;
14. native restart and web/PWA reload preserve intended routing.

Native, web/PWA, emulator, and physical-device evidence are not interchangeable.

## Alternatives considered

- **Auto-merge by equal email:** rejected as owner authority; conflicts with UID-based ownership and provider collision semantics.
- **Sign into provider B then merge UID B into UID A:** rejected for V1; Firebase linking is credential-to-current-user, not a general ledger/user merge primitive.
- **Never allow provider linking:** simpler and safer initially, but reduces recovery/reachability. Keep linking as a Settings capability only after executable validation.
- **Allow unlink freely:** rejected; can strand identity or create a later separate Firebase user.

## RELATED DOMAIN CHECK

- **Foundations:** direct Dart/Flutter runtime evidence exists; not the blocker.
- **Architecture:** Auth identity, ledger owner, onboarding state, and Sync eligibility require separate ownership.
- **Mobile:** native vs web provider flows and session restoration require separate transfer validation.
- **Data:** capability-v7 cleanup and idempotent first-owner initialization need schema/transaction review.
- **Quality:** collision/cancel/restart/duplicate-callback failure oracles required.
- **Systems:** canonical owner for identity/session/provider security semantics.
- **Design Studio:** provider visual hierarchy and recovery copy are downstream of these states.
- **Web Manager:** PWA redirect/authorized-domain behavior is a later handoff.
- **Marketing Manager:** not materially relevant.
- **Product:** exact LogMate ref recorded above; no product files edited.

## HANDOFFS

### LogMate / Codex

Before provider UI polish: canonically supersede account-free startup; implement a provider-neutral result model; bind fresh ownership idempotently to Firebase UID; preserve mismatch/sign-out/offline boundaries; treat provider collision as recovery rather than merge; prevent last-provider unlink; and add restart/cancel/collision tests.

### Architecture / Data / Quality / Mobile

Architecture: review the four-state ownership split. Data: define capability-v7 retirement and atomic first-owner initialization. Quality: implement failure-first state-transition oracles. Mobile: transfer-test Google/Apple/session restoration separately on Android/iOS/PWA.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN:** LogMate canonical update superseding AUTH-E1/E2/E4/E5 account-free portions.
- **OPEN:** exact Firebase password policy and one-account-per-email/enumeration-protection configuration.
- **OPEN:** exact Google/Apple provider console/capability/OAuth configuration.
- **OPEN:** executable provider-linking behavior under current FlutterFire/project configuration, including documented known issue.
- **OPEN:** account deletion/revocation failure/retry design.
- **VALIDATION:** no runtime Auth/onboarding PASS is claimed.
- **CHANGE WATCH:** Firebase Auth/FlutterFire provider behavior, Apple policy, browser popup/redirect/persistence behavior.
