# S007 — Account Deletion, Reauthentication, Provider Revocation, and Data-Erasure Saga

Status: **SOURCE / SYNTHESIS / ENGINEERING JUDGMENT / PROJECT TRANSFER — runtime validation OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-24

## Problem
Account deletion is not equivalent to `FirebaseAuth.currentUser.delete()`. For an account-creating cross-platform app using email, Google, and Apple, deletion crosses at least identity-provider authorization, Firebase Authentication identity, product-owned remote data, device-local data, and store-policy obligations. These steps cannot generally be committed as one transaction. The engineering problem is therefore a recoverable deletion saga with explicit irreversible boundaries, not a single Auth call.

## SOURCE
- Firebase Flutter user management documents that account deletion is security-sensitive and can fail with `requires-recent-login`; the user must reauthenticate with a fresh credential before retrying.
- Firebase Apple documentation says Apple token revocation is required for deletion support. Firebase does not retain the Apple user token for later revocation; the user must sign in again and the fresh Apple authorization/access material must be used to revoke before deleting the Firebase account.
- Apple account-deletion guidance requires apps supporting account creation to let users initiate deletion in-app. Apps using Sign in with Apple should revoke Apple user tokens. Apple's TN3194 further separates token revocation from deletion of developer-held account data and describes credential-revocation notifications.
- Google Play's current User Data policy requires account-creating apps to provide both an in-app deletion path and an external web resource where users can request account and associated-data deletion. Freezing/deactivation is not deletion; retained data for legitimate reasons must be disclosed.

Primary sources checked 2026-09-24:
- Firebase Flutter Manage Users: https://firebase.google.com/docs/auth/flutter/manage-users
- Firebase Flutter Federated Auth: https://firebase.google.com/docs/auth/flutter/federated-auth
- Firebase Apple Android/Web/iOS guidance: https://firebase.google.com/docs/auth/android/apple ; https://firebase.google.com/docs/auth/web/apple ; https://firebase.google.com/docs/auth/ios/apple
- Apple account deletion: https://developer.apple.com/support/offering-account-deletion-in-your-app
- Apple TN3194: https://developer.apple.com/documentation/technotes/tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple
- Google Play account deletion requirements: https://support.google.com/googleplay/android-developer/answer/13327111

## SYNTHESIS — deletion is a saga
A robust provider-neutral contract needs distinct phases:

`requested → identityConfirmed → providerRevocationPrepared → providerRevoked/NotApplicable → remoteDataDeletionCommitted → firebaseIdentityDeleted → localSanitizationCommitted → completed`

The exact product may choose a different ordering, but each irreversible side effect must be observable and recoverable. A boolean `deleting=true` is insufficient because retry behavior differs before and after each side effect.

### Critical ordering constraint for Apple
For an Apple-linked account, deleting the Firebase identity first can destroy the easiest in-app path to obtain the fresh Apple authorization material needed for token revocation. Therefore the client flow must obtain fresh Apple authorization/reauthentication and successfully perform the required Apple revocation before treating Firebase identity deletion as complete.

This does **not** mean every product-data delete must happen client-side before Auth deletion. Product-owned remote deletion should use an authenticated/deletion-authorized coordinator whose retry semantics survive client loss. Otherwise a network/process failure after Firebase identity deletion can leave orphaned server data that the now-deleted user can no longer authenticate to remove.

### Provider-neutral vs provider-specific work
Provider-neutral deletion owns: intent confirmation, UID continuity, recent-auth requirement, remote-data deletion request/state, Firebase identity deletion, local-data disposition, restart/resume, and final completion.

Provider adapters own only provider-specific proof/revocation mechanics. Apple requires a revocation step. Do not invent a symmetric Google revocation requirement merely to make the interface visually uniform; if Google disconnect/revocation is later required by product or provider policy, add it from current primary evidence.

## ENGINEERING JUDGMENT — recommended transaction boundary
For a local-first app, prefer a server-authoritative deletion request/coordinator for remote account data, keyed to the Firebase UID and an idempotency key. The client may drive the UX, but should not be the sole durable owner of a multi-system erasure workflow.

Recommended invariant set:
1. reauthentication must return the same Firebase UID; a different UID aborts deletion and never rebinds the ledger;
2. Apple revocation success/known-already-revoked is recorded before Firebase identity deletion is accepted as complete;
3. remote deletion request is idempotent and resumable across process death/network loss;
4. Firebase identity deletion is not used as the oracle that product data was deleted;
5. local data erasure is an explicit required durable step; voluntary deletion retains no user-accessible local archive;
6. after any ambiguous network result, reobserve authoritative state before retrying a non-idempotent provider operation;
7. completion means all required product/provider/policy obligations reached their terminal accepted states, not merely `currentUser == null`.

## Failure-first matrix
- stale session → Firebase `requires-recent-login` → provider-specific reauth → same UID → resume;
- reauth returns different UID → abort/recovery, no ledger mutation;
- Apple reauth succeeds, revocation fails → Firebase account must not be declared deleted; retry/recovery remains possible;
- Apple revocation succeeds, Firebase delete fails → resume from post-revocation state without requiring duplicate destructive assumptions;
- remote-data deletion request accepted, client crashes before Firebase delete → restart reads durable deletion state and resumes;
- Firebase delete succeeds, client dies before local sanitization → startup must not misclassify this as ordinary signed-out first use and expose stale ledger to another UID;
- network timeout during remote deletion → query request/idempotency status before resubmission;
- local wipe fails/storage error → deletion is not silently declared fully complete if product policy requires local erasure;
- duplicate delete tap/callback → one logical deletion request, no duplicate destructive workflow;
- web deletion request from an uninstalled-device user → external path can authenticate/verify request without requiring app reinstall, satisfying the Google Play surface requirement.

## OPEN / DEPENDENCY / VALIDATION
- **PROJECT DECISION — CLOSED:** voluntary account deletion immediately revokes normal local access and requires deletion of all device-local LogMate user data. No user-accessible retained local archive is part of the deleted-account state. A durable deletion-pending/locked state must survive restart until required server, identity, provider-revocation, and local-erasure steps are complete.
- **DEPENDENCY — Web Manager/product web:** Google Play requires an external deletion-request resource. Engineering should provide identity-verification and deletion-status requirements; Web Manager owns the public web surface/operations.
- **DEPENDENCY — backend architecture:** if LogMate has no server-side deletion coordinator yet, account deletion cannot honestly claim atomic erasure across remote product data merely from a client Firebase delete.
- **VALIDATION:** exact FlutterFire version behavior for `requires-recent-login`, Apple authorization-code/access-token revocation, process-death resume, duplicate request, and post-Firebase-delete startup.
- **VALIDATION:** real Apple sandbox/native and PWA deletion/revocation transfer; Firebase Auth Emulator can cover Firebase identity state but cannot substitute for Apple token revocation.
- **CHANGE WATCH:** Apple/Firebase revocation APIs and App Store/Google Play account-deletion policy.

## RELATED DOMAIN CHECK
- Foundations: no missing execution prerequisite; F001 direct Dart/Flutter evidence exists.
- Architecture: deletion is a multi-owner saga; irreversible side effects require explicit state ownership and idempotent/resumable contracts.
- Mobile: native Apple reauth/revocation and browser redirect lifecycles require separate transfer tests.
- Data: remote-data erasure and local-ledger disposition are independent of Firebase identity deletion; crash-safe durable deletion state is required.
- Quality: failure injection must target every boundary between revocation, remote erasure, Auth deletion, and local sanitization.
- Systems: owns Auth/revocation/security semantics and policy-sensitive delivery boundary.
- Design Studio: destructive confirmation/recovery semantics are relevant, but no directly matching canonical evidence was found in the checked search; no files edited.
- Web Manager: no directly matching account-deletion canonical evidence was found in the checked search; external deletion resource is now a concrete handoff.
- Marketing Manager: not materially relevant.
- Product repositories: no product files edited in this block; exact LogMate product evidence remains the S007 retained ref in Systems status, and default branch is not assumed production.

## HANDOFFS
- **LogMate/Codex:** model deletion as a resumable state machine, not `user.delete()`; enforce same-UID reauth; for Apple obtain fresh authorization and revoke before Firebase identity deletion; preserve deletion state across restart; immediately lock normal local access after confirmation; delete all device-local LogMate user data before completion; never use `currentUser == null` as proof of data erasure.
- **Data/Architecture:** define durable deletion-request/idempotency schema and local-ledger disposition; separate product-data deletion acceptance from Auth identity deletion.
- **Quality:** build crash/network/duplicate/ambiguous-result tests at every saga boundary; Auth Emulator validates Firebase state only, not Apple revocation.
- **Web Manager:** provide an external LogMate account-deletion request surface that does not require reinstalling the app; align its identity-verification/status semantics with the product deletion coordinator.
- **Design Studio:** once local-data disposition is decided, design confirmation/recovery states that distinguish request accepted, provider reauth required, partial failure, and completed deletion without false completion language.
