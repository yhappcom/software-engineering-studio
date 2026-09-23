# S007 — Authentication Session, Account-Required Startup, and Onboarding Foundations

Status: **IN STUDY — SOURCE/SYNTHESIS + EXACT-PRODUCT TRANSFER + GENERIC EXECUTABLE STARTUP MODEL VALIDATED; EXACT-PRODUCT VALIDATION OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-24

## Problem and product identity
LogMate is moving from account-optional local-first entry to account-required first use while preserving offline-first daily operation after ownership is established. Firebase identity/session, local-ledger ownership/access, onboarding completion, provider reachability, Sync eligibility, and account-deletion completion remain separate state dimensions.

Exact product evidence retained: `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`. Default branch is not assumed production. This ref still exposes account-free entry and therefore CONTRADICTS the newer owner direction.

## Retained SOURCE / TRANSFER VALIDATION
Firebase Flutter Auth persists sessions and emits initial auth state after locally stored credentials are restored; startup therefore needs an Auth-initializing state. Password policy is Firebase-configured rather than a LogMate hard-coded 15-character rule. Provider linking preserves the Firebase UID of the currently authenticated user; equal email or a credential belonging to another UID is not ledger-merge authority.

Current Flutter federated-auth guidance requires official `google_sign_in` for native Android/iOS Google, while Web uses Firebase popup/redirect. Apple can use FlutterFire `AppleAuthProvider`, with Web/native lifecycle/configuration differences. Exact LogMate dependency inspection found `firebase_auth 6.7.0`, `firebase_core 4.15.0`, `firebase_auth_web 6.3.0`, generated Web/Android/iOS Firebase options, and no direct `google_sign_in`. Generated app options do not prove provider-console/OAuth/SHA/Apple-capability readiness. Existing `AuthEngine` is email-centric but already maps Firebase errors into product failure codes.

Primary sources retained/checked 2026-09-24: Firebase Flutter Auth start/account-linking/errors/federated-auth/manage-users/Auth Emulator/users/limits/password-auth and Apple account-deletion/token-revocation documentation.

## PROJECT DECISION
Owner direction, 2026-09-23: remove normal `Start a new logbook`; first use requires Firebase-backed Apple, Google, or email; restored authenticated users route by onboarding state; established ownership remains offline-first; pre-launch/no released users means no production account-free compatibility obligation; configured Firebase password policy is authoritative. Product canonical update remains OPEN.

## SYNTHESIS — provider-neutral command and outcome algebra
The shared abstraction is a product state transition, not a shared provider transport. Keep commands distinct: `authenticate(provider)`, `reauthenticate(provider)`, `link(provider)`, and `unlink(provider)`.

Minimum typed outcomes: `authenticated(uid)`, `cancelled`, `credentialCollision`, `providerAlreadyLinked`, `providerUnavailableOrMisconfigured`, `networkOrOutcomeUnknown`, `rateLimited`, `requiresRecentLogin`, `accountDisabled`, `invalidCredential`, and fail-closed `failure`. Raw provider/Firebase codes are diagnostic metadata rather than product-state authority. `networkOrOutcomeUnknown` must not become `cancelled` or `signedOut`; re-observe Firebase state before retrying durable transitions.

## Startup/ownership matrix
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

## Startup initialization authority and enumeration-protection transfer
Firebase recommends email-enumeration protection; newer projects enable it by default. Product behavior must remain correct when account-specific errors collapse to less-specific errors. Do not disable enumeration protection to preserve identifier-first UX or provider discovery. At the audited LogMate ref, Firebase initialization is lazy and was designed for account-optional first-frame behavior; new account-required routing instead needs an explicit initialization boundary. `null currentUser` before that boundary is not signed-out authority.

Startup therefore needs a provider-independent initialization state distinct from a nullable session snapshot: `uninitialized/initializing → initializedSignedOut | initializedAuthenticated(uid) | initializationFailure`. Login/reset presentation must be enumeration-safe, and provider collision recovery must not use email or `fetchSignInMethodsForEmail()` as owner authority.

## VALIDATION — generic executable fail-closed startup model
Canonical hosted validation record: `research/systems/S007_startup_model_hosted_validation_2026-09-24.md`.

Fixture `research/systems/fixtures/S007_auth_startup_state_model.py` and workflow `.github/workflows/s007-auth-startup-state-model.yml` executed at exact workflow head `1bc58ec210408a18cb4fd719be85b5b21e727d2e`. GitHub Actions run `35909442993`, job `107345269055`, on GitHub-hosted Ubuntu 24.04.5 / CPython 3.13.15 completed successfully. The job log records all eight intended fail-closed startup tests as `ok` and `Ran 8 tests ... OK`.

The validated bounded claims are: unresolved/failed initialization never routes to Welcome/Home; duplicate authenticated observations initialize an owner at most once; a mismatching UID cannot rebind an owner; explicit sign-out retains owner binding while locking routing; matching complete/incomplete owners route Home/onboarding respectively; reauthentication after explicit sign-out can restore Home.

**EVIDENCE LIMIT:** this is a Python Studio semantic model, not LogMate runtime evidence. It does not execute LogMate Dart/Flutter, Firebase session persistence, Sembast transactions, Firebase Auth Emulator, Google/Apple SDKs, Android/iOS lifecycle, or PWA redirect behavior. No product/provider PASS follows from this result.

## Account deletion / revocation transaction boundary
Firebase user deletion requires recent authentication. Apple-linked deletion is a multi-authority operation because provider revocation and Firebase identity deletion can partially succeed. Model deletion as an explicit retryable workflow, retain per-authority evidence until terminal completion, and do not conflate account deletion with local-ledger destruction. Exact ordering remains OPEN pending future Sync/backend and token-handling authority.

## Firebase Auth Emulator validation ladder
Use three evidence layers: pure product-state tests; Firebase Auth Emulator integration with independent account-state/UID oracles; then real Google/Apple Android/iOS/PWA validation. Emulator account clearing is fixture reset, not product deletion evidence.

## Durable onboarding completion and Previous Total boundary
Baseline presence, record count, Firebase authentication and widget route are not onboarding-completion authority. Persist explicit semantic decisions. At minimum distinguish owner ready, Previous Total pending/resolved (`configured` or `explicitlyNone`), optional import decision if product requires it, and committed setup completion. Explicit negative decisions are data and must survive restart.

Fresh-auth processing must be safe under duplicate provider callbacks, redirect replay and restart. Exact repository inspection shows `completeInitialLogbookSetup()` currently writes `completed` without checking a Previous Total resolution prerequisite, while baseline configuration has its own atomic baseline/generation/checkpoint transaction. This is not an old-contract defect; it is the minimal persistence-contract delta exposed by the new policy. Prefer explicit durable Previous Total decision plus repository-level prerequisite enforcement over nullable-baseline inference or UI sequencing.

## RELATED DOMAIN CHECK
- Foundations: direct Dart/Flutter JIT/AOT and bounded Chrome/Safari runtime evidence exists; no historical F001 blocker.
- Architecture: initialization, identity, ledger owner, onboarding milestones, baseline, Sync and deletion remain separate state/ownership dimensions.
- Mobile: native Google/Apple and PWA redirect replay require separate validation.
- Data: owner initialization and setup milestones require atomic/idempotent semantics.
- Quality: generic startup model now has hosted executable evidence; exact-product failure injection remains required.
- Systems: owns identity/session/provider security and this validation boundary.
- Design Studio: auth/recovery copy downstream; persisted state must not be widget-route identity. No canonical files edited.
- Web Manager: popup/redirect/authorized-domain behavior downstream. No canonical files edited.
- Marketing Manager: not materially relevant.
- Product: exact LogMate ref retained; no product files edited.

## HANDOFFS
- **LogMate / Codex:** reproduce the eight validated model invariants in actual Dart/Flutter tests: no Welcome before initialized Auth; exactly-once owner initialization under duplicate observations; wrong UID no mutation; explicit sign-out retains owner but locks access; matching completed owner restores Home; incomplete owner resumes onboarding.
- **Quality:** preserve run `35909442993`, job `107345269055`, and exact head as bounded generic evidence; next require exact LogMate tests and Auth Emulator independent UID/account-state oracles.
- **Data/Architecture:** preserve explicit owner/setup/baseline state and enforce Previous Total resolution before durable setup completion.

## OPEN / VALIDATION / CHANGE WATCH
- OPEN: exact LogMate implementation execution and product-canonical account-required update.
- OPEN: exact semantic-onboarding persistence representation and optional-import completion policy.
- OPEN: actual Firebase password policy/enumeration/provider configuration and `google_sign_in` implementation version/configuration.
- OPEN: exact FlutterFire exception observations, Auth Emulator integration, real linking/cancellation/collision/revocation and PWA redirect behavior.
- OPEN: deletion authority/order, backend/Sync deletion, secure token/code handling and local-ledger deletion-vs-lock policy.
- VALIDATION: generic startup model hosted verdict CLOSED; no LogMate/Auth/provider runtime PASS claimed.
- CHANGE WATCH: Firebase Auth/FlutterFire/Auth Emulator, password/enumeration settings, Google/Apple SDK/policy, browser popup/redirect/persistence and provider console configuration.
