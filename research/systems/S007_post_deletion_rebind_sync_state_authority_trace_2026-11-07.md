# S007 — Post-deletion UID rebind and Sync-state carryover: exact-source authority trace

**Date:** 2026-11-07 Asia/Seoul. **Lead:** Systems (S007), with Data D006 and Architecture A002. **Evidence class:** SOURCE / STATIC TRACE / CONTRADICTION / ENGINEERING JUDGMENT / VALIDATION OPEN. **No product code modified; no Dart/Sembast executable test performed.**

## Scope and identity

- Product: `yhappcom/logmate → verify/w013-target-file-resume-20261107@472e3fa90c4e5f8c346aadc19d42f9e6ddd7ef24 → pubspec.yaml 1.0.0+1 → 2026-11-07`. Production/deployed ref **unknown**. Product source `lib/repository/logbook/sembast_logbook_repository.dart` blob `f2b8b0eb681f5d960532dac5c87b29cf85a459b8` is unchanged from main `f4bcd2f7...` and earlier W013 Draft. Coordinator `lib/application/account_deletion_coordinator.dart` blob `8e844e888b39d3b5e1648aeb84be26e6582ed60f`.
- Studio source read at current main `cf0961c072fa8a476f5280c4c21a7b595d424554` (before this addition).
- Branch/PR inventory observed: **61 branches, 12 open PRs**, latest #46 Draft `472e3fa...`; #46 is evidence-only and does not alter the repository implementation in scope.

## NEW SOURCE-level trace beyond the earlier 29/37 count

**Claim under test:** After a successful terminal deletion of UID A, a subsequent fresh UID B must not inherit A's Sync operation identity, cursor, receipts, head/hold evidence or replica-derived authority merely because the owner field has been replaced. Whether retaining a per-installation Replica ID is safe must be a separately justified design decision; retention itself is not a proven privacy incident.

1. **Terminal wipe drops exactly 29 named stores.** `wipeLocalUserDataAndCompleteDeletion` at source lines 1099–1156 drops `_schemaStore` through `_flightEntrySaveReceiptStore`, then calls `_initializeFreshDatabase(transaction)` and writes deletion phase `completed`. It **does not drop** `_localReplicaStore`, `_syncStateStore`, `_syncBindingStore`, `_syncReceiptStore`, `_syncAppliedIdentityStore`, `_syncCursorStore`, `_syncHeadStore`, `_syncHoldStore`.
2. **Fresh initialization is not a Sync-store reset.** `_initializeFreshDatabase` (5026–5043) calls `_writeReadyMigration` → `_publishCapabilityV7` (5115–5145) with unbound owner. `_writeOwnerAccess` (3662–3679) changes only the `ownerUid` field of any pre-existing `_syncStateStore` row, preserving other fields. Thus the existing Sync row is not erased by this path. The source shows separate explicit Sync-store drops at 561–567 for **backup staging format upgrade**, proving such a reset operation exists but is not invoked by terminal deletion.
3. **Potential B rebind retains Sync row contents.** `createOwnedLedger(B)` (1702–1726) and `bindOwner(B)` (1728–1750) accept an unbound owner, write `LocalOwnerAccess.bound(B)`, and call `_writeOwnerAccess`, which replaces only `_syncStateStore.ownerUid` with B. No Sync store clearing occurs in these methods. Therefore, **if** the post-wipe database is successfully reopened and UID B is allowed to bind, preexisting non-owner fields of the same Sync-state record and separate seven Sync stores are not removed by these code paths.
4. **Replica identity persistence is explicit:** `_ensureLocalReplicaIdentity` (3240+) preserves an existing replica; `_readLocalReplicaIdentity` (3225–3242) validates it. The correct deletion policy for an installation-level replica identity requires explicit owner/operation isolation analysis; its survival is not automatically an exploit. However, retaining A's Sync operation evidence under B's newly written ownerUid is a distinct risk from merely retaining a random replica identifier.
5. **Phase admission remains too permissive as a public repository boundary:** `advanceAccountDeletion` (1068–1097) rejects backward moves but accepts equal/forward jumps rather than exact adjacent transitions; `requestAccountDeletion` (1036–1066) persists deletion phase `localLocked` without atomically updating `BoundLocalOwnerAccess.lock`. Normal coordinator (lines 47–90) sequences external operations; no evidence that it naturally skips steps or a remote actor can call the repository API.
6. **Fresh staging is stricter than post-deletion fresh state:** `_requireEmptyLbkDestination` (6460–6480) requires exactly five Sync-state fields, unbound owner, matching destination Replica ID, and no extra metadata. A post-deletion state that retains A's Sync metadata would not satisfy that fresh-staging predicate. This is a **static design inconsistency**, not proof that ordinary B onboarding invokes the staging predicate.

### Bounded inference

From the cited code it is justified to say: **the terminal deletion method does not explicitly erase eight stores; owner rebind does not clear retained Sync fields or records.** It is **not** justified to claim: a file-backed A→B sequence has been executed, UID B can read A's records, the Sync engine will transmit A's operations under B, a released app has this defect, or remote deletion failed. The Sync server implementation is still OPEN; whether `_validateSyncState` rejects the resulting state after reopen must be checked in an executable or full-code path test.

## Failure-first test specification (Studio-owned harness permitted; exact-product execution requires separate product Work)

- **Fixture:** disposable file-backed Sembast v17 database; populate A's 37 registry stores with valid typed entries and independent canary keys/digests (do not inject malformed rows that make the initial fixture invalid). Preserve pre-deletion complete store census, including Sync receipts/bindings/cursors/heads/holds and Replica ID.
- **Oracle 1:** request deletion; attempt stale same-owner write and unlock; verify persistence-authority fail-closed. Include wrong UID/request ID and every forbidden phase edge, especially equal and non-adjacent jumps.
- **Oracle 2:** drive legal phase sequence with controlled fake external ports, inject failures at each boundary, resume and restart, ensure exactly-once effects where required and no phase advanced before side effect.
- **Oracle 3:** terminal wipe, close/reopen, independent raw StoreRef enumeration of all 37 names, verify no A-associated Sync canary remains (or document explicit safe-retention policy), and distinguish new mandatory baseline rows from retained historical rows.
- **Oracle 4:** create/bind UID B on same file; check all 37 store values and Sync operational metadata, ensure A's operation/cursor/receipt/hold never becomes B's authority, and check B's initial Sync readiness/validation. Exercise duplicate/concurrent deletion driver and old open Repository handle.
- **Oracle 5:** compare current 29-name manual loop with a registry-driven wipe and a targeted eight-store wipe; preserve per-installation identity only with a proven cross-UID authority separation. An independent second UID / server-side authenticated Sync test is required before product/release PASS.

**No executable result claimed.** This is an exact-source proof obligation and a stronger test specification. A generic Python/Dart mock without real Sembast is not a substitute for the requested file-backed exact-source test.

## RELATED DOMAIN CHECK

- **Foundations:** transaction ordering and stale handle concurrency; Dart runtime availability already confirmed in F001, not a blocker assertion.
- **Architecture:** authoritative owner and phase state machine; no UID rebind that simply relabels operational metadata.
- **Mobile:** local DB persistence across app restart and managed EFB/browser storage differs; local file test alone does not prove all surfaces.
- **Data:** D006 cursor/receipt/Operation ID/Replica scope; W013 Restore staging's stricter Sync-state reset must not be silently conflated with deletion.
- **Quality:** independent store census and negative phase transitions; explicit false-positive controls for mandatory regenerated rows.
- **Systems:** terminal deletion privacy/erasure semantics, server-side UID authority, and external user-managed .lbk files are separate obligations.
- **Design/Web/Marketing:** no change to user-facing copy, PWA storage policy or product claims from this static trace.

## HANDOFFS / OPEN

**To LogMate/Codex:** prioritize a product-authorized isolated file-backed 37-store A-delete→B exact-head regression with independent canary enumeration and negative phase-edge tests. Inspect `_validateSyncState`, owner lock and session guards, all raw DB write entrypoints; do not infer current source is production. Compare an authoritative registry-driven erase and strict phase CAS with manual-list repair. Do not implement or merge without product Work approval.

**To Studio next cycle:** if safe independent Dart/Sembast execution becomes available, build the minimal real file-backed canary and record environment/oracle/logs; otherwise advance an independent gap, not another static rephrasing. S007 remains **OPEN / high release correctness risk**; no PASS or exploit established.
