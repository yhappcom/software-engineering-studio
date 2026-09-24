# S007 — LogMate Authentication & Onboarding Integrated Product Contract

Status: **PROJECT DECISION — PRODUCT CONTRACT FROZEN FOR IMPLEMENTATION; EXACT LOGMATE RUNTIME VALIDATION OPEN**  
Owner: Systems / Security / Identity  
Evidence date: 2026-09-24

## Purpose

This document consolidates the currently approved LogMate authentication, onboarding, account lifecycle, provider-button, session, ownership, recent-activity, and deletion decisions into one implementation-facing contract.

Until the LogMate product repository is explicitly updated to a newer product-canonical contract, this document is the Engineering Studio's authoritative transfer document for the owner's newer decisions.

Exact product evidence retained for comparison:

`yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`

The audited LogMate ref still contains older account-free startup and hard-coded password-policy semantics. Those older semantics are superseded by the decisions below. Production identity is not assumed from `main`.

---

## 1. Account requirement

### PROJECT DECISION

LogMate requires an account for first use.

Supported V1 authentication methods:

- Apple
- Google
- Email + Password

Account-free local-only first use is not part of the product.

The product rationale for requiring an account is that LogMate stores account-bound/personalized user information and establishes durable owner identity. Authentication is therefore part of ownership and personalization, not merely analytics/telemetry gating.

Store reviewers will receive a dedicated working test account when credentials are required for review.

### Security boundary

Reviewer credentials:

- must be supplied only through App Store Connect / Google Play review metadata or equivalent secure review channels;
- must never be committed to Engineering Studio, LogMate, CI configuration, screenshots, fixtures, or documentation.

---

## 2. Identity authority

Firebase UID is the authoritative LogMate owner identity.

The following are **not** owner authority:

- email address;
- Google email;
- Apple email;
- Apple private-relay email;
- display name;
- provider label.

Matching email addresses must never auto-merge two Firebase UIDs or two ledgers.

A provider credential can be linked to a Firebase UID, but provider membership is authentication reachability, not ledger ownership.

---

## 3. Startup and persisted session behavior

A single `loggedIn` boolean is insufficient. Startup must distinguish at least:

- Auth initialization state;
- Firebase session state;
- local owner/access state;
- onboarding state;
- remote authority/freshness state;
- deletion-lock state.

### Required routing

#### Auth unresolved / initializing

Do not flash Welcome or Home.

Show a startup gate/loading state until local Firebase Auth initialization has resolved enough to classify the session.

#### Initialized, signed out

Show Welcome / authentication entry.

#### Authenticated, matching owner, onboarding complete

Go directly to Home.

Do not show Welcome or onboarding again.

#### Authenticated, matching owner, onboarding incomplete

Resume onboarding from durable semantic state.

#### Authenticated UID differs from existing local owner

Fail closed into identity mismatch/recovery.

Do not expose or mutate the existing ledger.

#### Deletion pending / deletion locked

Do not expose Home or logbook data.

Resume deletion workflow.

### Persisted session rule

If the user did not explicitly Sign out, a temporary network failure, token-refresh failure, Firebase outage, or offline startup is not automatically equivalent to signed-out.

Once ownership has been established, offline-first local use remains available subject to the separate remote-authority state.

---

## 4. Provider-button presentation contract

The complete reusable implementation is stored at:

`research/systems/fixtures/S007_auth_provider_buttons/ready_to_use/`

Shared visible copy:

- **Sign in with Apple**
- **Sign in with Google**
- **Sign in with Email**

Apple and Google marks, typography, provider-owned spacing, and provider-rendered behavior must not be redrawn or distorted.

Email is LogMate-owned UI and is visually matched to the provider controls.

### Surface separation

| Surface | Geometry | Provider order |
| --- | --- | --- |
| iPhone native | iOS ≈ 205.09 × 48 logical px | Apple → Google → Email |
| Android phone | 216 × 48 logical px | Google → Apple → Email |
| iPadOS native | ≈ 239.27 × 56 logical px | Apple → Google → Email |
| Android tablet | 252 × 56 logical px | Google → Apple → Email |
| PWA compact, viewport < 400 px | 280 × 40 logical px | Apple-family host: Apple first; otherwise Google first |
| PWA regular, viewport ≥ 400 px | 360 × 40 logical px | Apple-family host: Apple first; otherwise Google first |

PWA ordering may be explicitly overridden when product/platform evidence requires it.

### Provider implementation

#### Apple — iOS/iPadOS

Use native `ASAuthorizationAppleIDButton` with sign-in type.

The Studio bridge is included in the ready-to-use package.

#### Apple — Android / PWA

Use Apple-generated official button assets at the selected exact footprint.

#### Google — native mobile/tablet

Use provider-approved Pill PNGs without aspect-ratio distortion.

#### Google — PWA

Use Google Identity Services via `google_sign_in_web.renderButton()`.

Do not replace the live PWA Google control with a hand-wired raster image.

#### Email

Use the LogMate Flutter control from the ready-to-use package, matched to each surface's visible footprint.

### Validation evidence

Latest bounded Studio package validation:

- workflow: `S007 Ready Auth Button Kit`
- run: `35937075501`
- job: `107436392513`
- Flutter: 3.47.5 stable
- Dart: 3.13.4
- `flutter analyze`: no issues
- tests/reference renders: **17 passed**

This validates the reusable Studio package and presentation contract, not exact LogMate/native/provider runtime integration.

---

## 5. Email account creation and verification

Creating a Firebase Email/Password account is not equivalent to verifying ownership of the email address.

### Required flow

`Email + Password → Firebase account creation → verification email → user verifies → app reload/reobserves verification state → onboarding`

Email users do not enter normal onboarding/Home until email verification is complete.

Restart behavior:

- if a Firebase session exists and `emailVerified == false`, return to verification-pending state;
- do not attempt to create another account;
- after verification, reload/reobserve the user state before continuing.

Password rules must follow the actual configured Firebase Password Policy.

Do not hard-code the older 15-character requirement unless the Firebase policy is explicitly configured to that value.

Enumeration-safe UX must not expose account existence through provider discovery or identifier-first branching.

---

## 6. Onboarding entry point

Authentication completion and onboarding completion are separate states.

After valid authentication and owner establishment, a fresh user must choose one of three setup methods.

### Choice A — Start a new logbook

Meaning:

- no previous historical records are imported;
- no Previous Total baseline is entered;
- the user begins a new LogMate ledger from the start.

This is **not** the old account-free Welcome action.

It exists only after successful account authentication/ownership establishment.

### Choice B — Enter Previous Total

Meaning:

- historical individual flight rows are not imported;
- the user establishes prior cumulative values as a baseline;
- LogMate starts recording new flights from that baseline.

### Choice C — Import existing logbook

Meaning:

- the user imports supported prior electronic/file-based logbook data;
- the import workflow handles source mapping, duplicates, batch identity, and recovery/undo according to the import contract.

The three choices are mutually exclusive **as the initial onboarding setup path**, but their related capabilities may be used later.

---

## 7. Durable onboarding state

Onboarding completion must not be inferred from:

- current route/page number;
- Firebase signed-in state;
- baseline null/non-null alone;
- record count;
- whether an import exists;
- whether a screen was previously visited.

Persist semantic state instead.

Recommended conceptual fields:

- `ownerReady`
- `setupMethod = newLogbook | previousTotal | import`
- `setupInProgress`
- `setupCompleted`
- `onboardingComplete`

The exact schema may differ, but the semantic invariants must remain.

### Completion rule

`onboardingComplete` becomes true only after the selected setup method has reached its accepted terminal state.

The repository/service layer should enforce this invariant rather than trusting UI order alone.

Crash/restart must deterministically resume the selected method or return the user to a valid setup-recovery state.

---

## 8. Post-onboarding modification

The onboarding choice records how the user initially started LogMate. It is **not** a permanent application mode.

### Previous Total

May be edited later.

Any affected totals/aggregates/checkpoints must be recomputed or invalidated according to the calculation contract.

Where practical, preserve modification history or sufficient provenance for diagnostics.

### Import

May be run again after onboarding.

Examples:

- add older historical periods;
- fill missing periods;
- import another supported source;
- correct earlier data through batch undo/reimport.

Required capabilities include duplicate detection and import batch identity/recovery.

### Start a new logbook

After data exists, this is not a simple toggle.

Treat it as a separate destructive reset/new-ledger operation with explicit confirmation and data-loss semantics.

Do not overwrite an existing ledger merely by changing `setupMethod`.

---

## 9. Fresh owner / local ledger initialization

A normal newly authenticated user should receive an idempotently initialized owner-bound local ledger for the authenticated Firebase UID.

Conceptually:

`createOwnedLedger(firebaseUid)`

must be safe to repeat after:

- callback duplication;
- app restart;
- process interruption;
- ambiguous completion.

Ordinary fresh users must not see legacy flows such as:

- `Connect this logbook`
- `Connect account`
- unbound-ledger claim UI

unless a future explicit recovery/migration feature requires them.

Because LogMate is pre-launch with no production account-free user base, backward compatibility with the old local-only first-use model is not a product requirement.

---

## 10. Offline-first access

After ownership is established, LogMate remains offline-first.

Temporary failures must not automatically revoke valid local access:

- no network;
- Firebase service unavailable;
- temporary token-refresh failure;
- transient backend failure.

Local owner/access and remote cloud authority are separate state axes.

Positive authoritative remote rejection — for example a confirmed disabled/deleted account — must stop cloud/sync authority.

The exact local-ledger policy after administrator-side disable/delete remains a separate OPEN product policy and must not be confused with voluntary user account deletion.

---

## 11. Recent usage / last active

Firebase Auth `lastSignInTime` is not sufficient to represent actual LogMate usage because a persisted session can enter Home without an interactive sign-in.

Maintain a separate server-associated activity field, conceptually:

- `createdAt`
- `lastActiveAt`
- optional `lastSignInAt`
- `accountStatus`

### lastActiveAt semantics

Record meaningful authenticated app activation after:

- Firebase/session restoration succeeds enough to identify UID;
- UID matches the accepted local owner;
- startup authorization gate accepts local access;
- Home/meaningful foreground use is entered.

Do not update merely because of:

- token refresh;
- background callbacks;
- passive SDK events.

### Timestamp / offline behavior

Prefer server-authoritative time for the canonical server field.

Activity reporting must:

- never block Home;
- be throttled/coalesced;
- tolerate offline use;
- retry/synchronize later;
- treat the newest pending observation as replacing older pending observations where appropriate.

Activity metadata is user-associated data and must be included in account-deletion server erasure.

Privacy disclosures and store data declarations must match the final implementation.

---

## 12. Provider linking

Linking adds another login credential to the currently authenticated Firebase UID.

Successful linking must preserve the same Firebase UID.

Linking must never:

- rebind the ledger;
- infer sameness by email;
- merge another Firebase UID;
- copy/migrate another ledger automatically.

Credential collision with another Firebase UID is a typed recovery state, not merge authority.

---

## 13. Provider unlinking

Unlink is allowed only when at least one **effective usable recovery method** remains.

Do not rely only on raw provider count.

The effective set should consider:

- provider actually linked to the Firebase UID;
- method supported by LogMate V1;
- method operationally enabled/configured;
- method usable on required product surfaces.

If removing the provider would leave no effective login/recovery method, block unlink before the Firebase mutation.

After unlink:

- reobserve Firebase state;
- verify UID continuity;
- verify the provider is absent;
- verify at least one recovery method remains.

If the network result is ambiguous, reobserve before retrying.

Unlink is not account deletion.

---

## 14. Voluntary account deletion

### PROJECT DECISION

Once the user confirms account deletion:

- normal local LogMate access is immediately locked;
- all LogMate server-side user data must be deleted;
- the Firebase identity must be deleted;
- all device-local LogMate user data must be deleted;
- no retained user-accessible local archive remains.

Deletion is a resumable multi-system saga, not a single `currentUser.delete()` call.

### Conceptual sequence

`requested → local access locked → same-UID recent reauthentication → provider-specific revocation if required → server/product data erasure → Firebase identity deletion → device-local wipe → completed`

For Apple-linked accounts, obtain the fresh authorization material needed for required Apple revocation before treating identity deletion as complete.

### Durable deletion state

Use a durable deletion state such as:

- `deletionPending`
- `deletionInProgress`
- `retryableIncomplete`
- `completed`

A restart during incomplete deletion must never fall through to ordinary signed-out first use and expose stale local data.

### Required failure cases

Test at least:

- remote erasure succeeds, local wipe fails;
- Firebase identity deletion succeeds, app dies before local wipe;
- offline during deletion;
- duplicate deletion request/callback;
- Apple revoke succeeds, later step fails;
- reauthentication returns a different UID;
- ambiguous network result at a destructive boundary.

Completion means every required terminal deletion obligation has been satisfied; `currentUser == null` is not sufficient proof.

---

## 15. External deletion surface

Google Play requires an external account-deletion request resource for account-creating apps.

This creates a Web Manager/product-web handoff.

The external resource must align with the same identity verification, deletion intent, and deletion coordinator semantics as the in-app flow.

Do not create a separate deletion meaning that can diverge from the product saga.

---

## 16. Store review operational contract

Before submission:

- create a dedicated reviewer/test account;
- verify it can reach required app functionality;
- ensure the backend and any required services are available for review;
- provide clear review notes/instructions;
- avoid OTP/2FA/recovery dependencies that make the supplied reviewer account unusable unless the review instructions explicitly support them.

Reviewer credentials remain operational secrets.

---

## 17. Required implementation state model

The implementation should keep these concerns distinct rather than collapsing them into one enum/boolean:

### Auth/session
- uninitialized
- initializing
- signedOut
- authenticated(uid)
- initializationFailure

### Owner/access
- freshNoOwner
- matchingOwnerUnlocked
- ownerMismatch
- deletionLocked

### Onboarding
- noSetupSelected
- selectedNewLogbook
- selectedPreviousTotal
- selectedImport
- setupInProgress
- complete

### Remote authority
- locallyRestored
- serverAccepted
- temporarilyUnreachable
- serverRejectedDisabled
- serverRejectedDeleted
- explicitlySignedOut

The exact type names may differ, but the axes must not be conflated.

---

## 18. Exact LogMate repository contradictions to remove

At the retained audited ref, LogMate still contains older semantics including:

- account-free `Start a new logbook`;
- unbound local ledger;
- `startLocalUse()`;
- `LocalEntryState`;
- `Connect account` / `Connect this logbook` paths;
- hard-coded 15-character password policy text.

These are superseded by this contract and must be removed, repurposed, or isolated during the authorized LogMate implementation change.

Do not blindly delete data-model capability or tests without first verifying whether they still serve a different valid recovery/import/storage role.

---

## 19. Ready-to-use assets and code

Reusable provider-presentation implementation:

`research/systems/fixtures/S007_auth_provider_buttons/ready_to_use/`

Important files include:

- `lib/auth_surface_spec.dart`
- `lib/logmate_native_auth_buttons.dart`
- `lib/logmate_pwa_auth_buttons.dart`
- `lib/apple_system_button.dart`
- `ios/OfficialAppleSignInButtonFactory.swift`
- `assets/`
- `INTEGRATION.md`
- `pubspec.fragment.yaml`
- tests and golden/reference renders

The button kit owns presentation only.

It does not own:

- Firebase UID;
- account creation state;
- owner binding;
- onboarding completion;
- provider merge/link authority;
- account deletion state.

---

## 20. Validation status

### Bounded validation already closed

- generic fail-closed startup model: hosted executable validation, 8 tests passed;
- provider button official asset acquisition/provenance;
- initial raw-raster geometry test, which correctly rejected the 375×56 full-width assumption;
- ready-to-use mobile/tablet/PWA presentation package;
- latest package static analysis + 17 tests/reference renders.

### Exact product validation still OPEN

Before production release, validate on the exact LogMate artifact:

- Dart/Flutter implementation tests;
- Firebase Auth Emulator;
- actual Firebase Password Policy;
- email-enumeration protection behavior;
- Google provider configuration;
- Apple provider configuration;
- iOS/iPadOS native Apple system button compile/runtime;
- Android Google authentication;
- iOS Google authentication;
- iOS Apple authentication;
- PWA Google GIS runtime;
- PWA Apple callback/redirect;
- provider collision/link/unlink;
- same-UID reauthentication;
- onboarding crash/restart durability;
- Previous Total transaction/invariant;
- import onboarding failure/recovery;
- account-deletion saga and local wipe;
- Apple token revocation;
- remote disable/delete observation;
- recent-activity backend write/throttle/offline retry;
- accessibility on VoiceOver/TalkBack/browser;
- final App Store / Google Play review.

No Studio validation should be promoted to an exact LogMate production PASS without these product-transfer checks.

---

## 21. Implementation handoff order

Recommended authorized LogMate implementation sequence:

1. update LogMate product docs to supersede account-free startup;
2. introduce explicit Auth initialization/session startup state;
3. replace ordinary unbound/local-entry first-use flow with account-required owner initialization;
4. implement provider-neutral Auth outcomes;
5. integrate Email account creation + verification;
6. integrate Google native/PWA;
7. integrate Apple native/PWA;
8. copy/adapt the `ready_to_use/` provider-button package;
9. implement idempotent owner-bound ledger initialization;
10. implement the 3-choice onboarding state machine;
11. enforce durable onboarding completion in repository/service layer;
12. implement post-onboarding Previous Total edit and repeat Import;
13. implement `lastActiveAt` backend contract;
14. implement provider link/unlink/recovery;
15. implement durable deletion saga + external web deletion handoff;
16. run exact-product unit/widget/integration/Auth Emulator tests;
17. run native Android/iOS/iPadOS and PWA transfer validation;
18. perform store-review readiness checks.

---

## RELATED DOMAIN CHECK

- **Foundations:** no new prerequisite; runtime/toolchain foundations exist.
- **Architecture:** Auth/session, owner, onboarding, remote authority and deletion remain separate state ownership domains.
- **Mobile:** exact iOS/Android/iPadOS provider runtime and lifecycle transfer remains required.
- **Data:** owner binding, baseline, import, presence metadata and deletion erasure require durable transaction/recovery semantics.
- **Quality:** exact LogMate tests, Auth Emulator, failure injection, device/browser transfer and independent state oracles are required.
- **Systems:** owns identity, provider, security, deletion, policy-sensitive delivery contract.
- **Design Studio:** provider branding/geometry is a hard external constraint; surrounding onboarding composition can be designed independently.
- **Web Manager:** external deletion request and PWA auth/authorized-origin readiness are concrete handoffs.
- **Marketing Manager:** not materially relevant to implementation.
- **Product:** LogMate repository remains unchanged by this documentation task.

---

## HANDOFFS

### LogMate / Codex

Treat this document as the integrated implementation contract. Do not reconstruct product policy from the older account-free LogMate files where they conflict with this contract.

### Design Studio

Use the ready-to-use provider controls as fixed external-branding constraints. Design the surrounding authentication/onboarding composition, not the provider marks.

### Web Manager

Implement the external deletion-request surface and coordinate PWA auth domains/callback infrastructure.

### Quality / Mobile / Data / Architecture

Use the validation and failure matrices above as the product-transfer gate.

---

## Final product contract summary

LogMate is **account-required + offline-first**.

A user authenticates with Apple, Google, or verified Email. Firebase UID is owner authority. A fresh authenticated user chooses exactly one initial setup path:

1. Start a new logbook
2. Enter Previous Total
3. Import existing logbook

After onboarding, Previous Total remains editable and Import can be run again. The initial choice is history, not a permanent mode.

Returning authenticated users with completed onboarding go directly to Home. Actual app use is tracked separately from Firebase sign-in time through a non-blocking `lastActiveAt` contract.

Apple/Google/Email presentation is already prepared as a reusable mobile/tablet/PWA package in Engineering Studio.

Voluntary account deletion immediately locks local access and must delete server data, Firebase identity, and device-local LogMate data through a resumable deletion saga.

Exact LogMate integration and production/runtime validation remain the next gate.
