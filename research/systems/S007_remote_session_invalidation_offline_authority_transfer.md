# S007 — Remote Session Invalidation vs Offline Ledger Authority Transfer

Status: **SOURCE / SYNTHESIS / PROJECT TRANSFER — exact-product runtime validation OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-24

## Exact product context
`yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`. Production identity remains unknown. `MASTER.md` explicitly retains local-first operation and states that Auth/Sync failure should not block established local use, while the newer owner direction requires Firebase-backed ownership on first use.

## SOURCE
Firebase Authentication persists a signed-in user across application/browser restarts. Flutter Auth listeners emit their initial event after locally stored credentials are restored. Firebase documents that `currentUser == null` can mean either signed out or Auth not yet initialized, so startup must wait for initialized Auth state.

Firebase also documents a less obvious remote-invalidation boundary: disabling or deleting a user through Admin SDK/Console does not itself cause Flutter `authStateChanges`, `idTokenChanges`, or `userChanges` to fire. A forced `currentUser.reload()` is required to retrieve that remote state and can surface `user-disabled` or `user-not-found`.

Firebase ID tokens are short-lived (approximately one hour), while refresh tokens are long-lived and expire when the user is deleted, disabled, or undergoes a major account change; Admin SDK can additionally revoke refresh tokens. Therefore client possession of a previously restored Firebase User is not proof that the account is presently accepted by Firebase.

## SYNTHESIS — two authorities must not be collapsed
LogMate needs separate state dimensions:

1. **local ledger ownership/access authority** — durable binding of a local ledger to a Firebase UID and the product's offline-use policy;
2. **remote Firebase session/cloud authority** — whether Firebase currently accepts that identity/session for online operations.

A restored matching UID establishes continuity with the local owner record, but it does not prove fresh server authorization. Conversely, inability to contact Firebase does not prove revocation. Treating network failure as signed-out/revoked would violate offline-first behavior; treating a positively observed `user-disabled`/`user-not-found` as an ordinary transient network failure would erase a security-relevant server decision.

Minimum remote-authority algebra:
- `unresolved` — Auth initialization not complete;
- `restoredLocally(uid)` — persisted Firebase identity restored; server freshness not established in this observation;
- `serverAccepted(uid)` — an online operation/reload/token refresh has positively established continued Firebase acceptance;
- `temporarilyUnreachable(uid)` — transport failure/outage; not evidence of revocation;
- `serverRejectedDisabled(uid)` / `serverRejectedDeleted(uid)` — authoritative rejection observed;
- `explicitlySignedOut` — local Firebase sign-out action completed.

These states are not interchangeable with ledger-owner state.

## ENGINEERING JUDGMENT / product policy boundary
For an offline-first pilot logbook, immediate remote revocation of already-downloaded local data is technically impossible while a device is disconnected. Product copy/security claims must not promise it. The strongest enforceable rule without a separate local revocation channel is eventual observation when Firebase is contacted again.

The newer product decision already says established ownership remains usable offline. Therefore the safe implementation split is:
- **offline / transient transport failure:** preserve matching-owner local access; mark Sync/cloud unavailable or stale;
- **positive Firebase disabled/deleted observation:** stop cloud/Sync authority immediately and enter an explicit account-recovery/remote-rejected state rather than silently treating the event as generic sign-out;
- **local ledger after positive remote rejection:** OPEN PRODUCT DECISION. Whether local read/write remains available, becomes read-only, or is locked requires an explicit LogMate policy because Firebase cannot retroactively erase offline data and account deletion is already defined separately from local-ledger destruction.

Do not automatically delete local flight records when Firebase reports `user-not-found` or `user-disabled`. Such deletion would be irreversible local data loss and is not implied by Firebase Auth semantics.

## Codex implementation contract
Provider-neutral startup/session code should expose remote-session freshness separately from `AuthSession(uid)`. Do not encode the entire state as `User?` or a boolean `isSignedIn`.

Required behaviors:
1. initial listener event after credential restoration may route only after Auth initialization and UID-owner comparison;
2. a network failure during optional freshness/reload cannot mutate owner binding or manufacture signed-out state;
3. `user-disabled` and `user-not-found` from a positive Firebase operation become typed remote-rejection outcomes;
4. token refresh/reload success for the same UID may advance remote freshness but never create/rebind the ledger owner;
5. any observed UID change is owner mismatch/recovery, not account replacement;
6. explicit sign-out remains distinct from server rejection and retains the local ledger under lock per existing direction;
7. remote rejection never triggers local record deletion as an Auth side effect.

## Failure-first validation matrix
- restored matching UID while fully offline → established local-access policy preserved; cloud state degraded, no owner mutation;
- restored matching UID + `reload()` network failure → not signed out, not revoked;
- restored matching UID + `reload()` `user-disabled` → typed disabled state, cloud/Sync denied;
- restored matching UID + `reload()` `user-not-found` → typed deleted state, cloud/Sync denied;
- token refresh failure caused by network vs invalid/revoked credentials → distinct outcomes;
- remote deletion while app remains open → verify listeners alone do not falsely claim immediate detection; force reload path observes rejection;
- remote disable while device is offline, then reconnect → eventual rejection observation without ledger deletion/rebind;
- explicit sign-out while offline → Firebase sign-out/local lock behavior remains distinct from server rejection;
- stale restored UID A followed by authenticated UID B → no access to/rebind of A ledger;
- restart after previously observed server rejection → policy state must not accidentally route Home solely because a stale local owner exists.

## OPEN / VALIDATION
- OPEN PROJECT DECISION: local ledger read/write policy after a **positively observed** Firebase disabled/deleted account.
- OPEN: whether LogMate needs durable persistence of the last remote-rejection observation or can derive it safely at startup without weakening offline-first behavior.
- VALIDATION: exact LogMate Dart/Flutter tests; Firebase Auth Emulator/Admin-side disable/delete/revoke experiment; Android/iOS/PWA restart/reconnect transfer.
- VALIDATION: determine exact FlutterFire exception surfaces for reload/token refresh at the implementation version used by LogMate.
- CHANGE WATCH: Firebase Auth listener/reload/session behavior and FlutterFire mapping.

## RELATED DOMAIN CHECK
- Foundations: no new runtime prerequisite.
- Architecture: local ownership and remote authorization are distinct authorities/state machines.
- Mobile: background/reconnect/restart detection timing differs by native/PWA lifecycle and needs transfer tests.
- Data: remote Auth rejection must never implicitly destroy ledger data; any lock/read-only persistence policy needs explicit schema/transaction ownership.
- Quality: requires network-vs-revocation fault discrimination and independent Emulator/Admin oracle.
- Systems: owns session invalidation/security semantics.
- Design Studio: recovery/disabled/deleted copy must distinguish offline outage from account rejection; no files edited.
- Web Manager: PWA reconnect/session behavior is a downstream transfer target; no files edited.
- Marketing Manager: not materially relevant.
- Product: exact LogMate ref inspected; no product files edited.

## HANDOFFS
- **LogMate / Codex:** add a remote-session-freshness/rejection dimension instead of reducing startup to `User?`; implement typed `network/unreachable`, `disabled`, `deleted`, `explicitSignOut`, and UID-mismatch outcomes. Do not delete/rebind ledger data from Auth callbacks.
- **Quality:** build Auth Emulator/Admin-side tests that disable/delete/revoke a known UID and independently verify the client observation path; prove network failure cannot masquerade as revocation.
- **Architecture/Data:** decide and document the post-positive-rejection local-ledger policy separately from cloud authority and account-deletion workflow.
- **Design/Mobile:** design recovery states only after that product policy is fixed; validate reconnect/background/PWA behavior separately.
