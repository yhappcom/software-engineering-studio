# S007 — Ordinary DB reopen versus B1 backup owner-validation gap after terminal deletion

**2026-11-07 KST. Lead Systems S007; Data D005/D006 and Quality Q001/Q006 support.**
**Evidence:** SOURCE / STATIC CONTROL-FLOW TRACE / CONTRADICTION / ENGINEERING JUDGMENT / VALIDATION OPEN. No Dart/Sembast product or Studio fixture execution; no incident or production claim.

## Source and branch authority

- Product: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b` and newest open Draft PR #46 `verify/w013-target-file-resume-20261107@472e3fa90c4e5f8c346aadc19d42f9e6ddd7ef24 → pubspec 1.0.0+1 → 2026-11-07`; production identity unknown. Repository implementation `lib/repository/logbook/sembast_logbook_repository.dart` blob `f2b8b0eb681f5d960532dac5c87b29cf85a459b8`, unchanged between those refs.
- Fresh GitHub branch/PR census: **61 branches, 12 open Draft PRs**, #46 latest, no new change since prior S007 trace. #46 evidence-only. PR #42–46 product evidence stack and PR #39–41 writer-fence probe stack are distinct. No claim of merge.
- Existing Studio source: `research/systems/S007_post_deletion_rebind_sync_state_authority_trace_2026-11-07.md` identified 29/37 terminal drops, `_writeOwnerAccess` owner-field relabel and possible UID A→B carryover. This block advances **the missing validation gate** rather than restating that count.

## New exact-source discriminator: live open validates less than backup import

**Ordinary local DB open:** repository lines 5010–5015 call `_readLocalReplicaIdentity` and `_validateSyncState`. `_validateSyncState` (5238–5260) checks **only** the single `_syncStateStore` record's `schemaVersion`, `originReplicaId`, `streamBindingStatus`, `remoteBaselineStatus`, `ownerUid` consistency with `_ownerAccessStore`, and origin Replica ID equality with `_localReplicaStore`. It does **not enumerate or check ownership of rows** in `_syncBindingStore`, `_syncReceiptStore`, `_syncAppliedIdentityStore`, `_syncCursorStore`, `_syncHeadStore`, `_syncHoldStore`. Thus **ordinary-open Sync validation alone cannot establish that retained auxiliary rows belong to the currently bound UID**. This is a direct inspection of the invoked validation function, not proof of the entire startup flow accepting a post-deletion DB.

**Terminal deletion:** `wipeLocalUserDataAndCompleteDeletion` (1099–1157) drops 29 stores, not Replica and seven Sync stores, then `_initializeFreshDatabase` (5026–5043) → `_publishCapabilityV7` (5115–5175) → `_writeOwnerAccess` (3662–3679). This writes unbound `ownerUid=null` into an existing Sync State record without clearing its other fields. `_ensureSyncState` (5177–5186) **returns immediately if the state row already exists**, so it cannot restore initial `streamBindingStatus='unbound'` and `remoteBaselineStatus='unverified'` for a retained row. Subsequent `createOwnedLedger(B)`/`bindOwner(B)` (1702–1750) call the same owner-only write, and neither resets Sync auxiliary stores. Therefore the live-open validator checks owner/replica agreement **after those fields are rewritten** but does not independently verify historical ownership of retained Sync evidence. Whether the full A→B open succeeds is **OPEN**, because other validators and state transitions must be exercised with valid file-backed fixtures.

**B1 backup validation is materially stricter:** `_validateLbkSyncEvidence` (6271–6335) inspects Sync State plus every Sync store and calls `_validateLbkSyncOwnerReferences(value,ownerUid)` on each row, including a direct `_syncBindingStore.ownerUid` match and operation/revision relationship checks. It is **not called by `_validateSyncState`**. Consequently a B1 export/import or staging acceptance can reject some stale A-owner evidence that the narrower ordinary-open Sync validator does not itself detect. Exact backup failure behavior after A→B still needs a real test; it must not be claimed as proven.

**Security invariant:** UID reassignment must not be treated as historical Sync evidence reassignment. A valid `ownerUid` on the Sync State header does not prove that receipts/cursors/bindings/holds are valid for that UID, nor that the server will accept them. The approved Automatic + Manual Delta policy in unmerged PR42 increases the importance of enforcing this boundary before any production server Sync, but the server engine is still NOT IMPLEMENTED.

## Independent test plan (next product-authorized execution)

Use an isolated, synthetic, file-backed **exact-product** Sembast v17 database and its real production codec, not hand-built malformed rows. Create valid A ledger and Sync operational evidence through supported APIs/fixtures; capture independent raw StoreRef keys, counts and cryptographic digests for all 37 stores. Control group: fresh empty ledger B and A→A reopen; negative group: a valid A receipt/binding/cursor/hold surviving terminal wipe and owner B bind. Check `_validateSyncState` in isolation, **full repository open**, B1 export/import candidate, and later authenticated server Sync independently; these have different acceptance authorities. Inject a row with explicit `ownerUid=A` versus a legacy row with no UID, and a row whose operation ID collides with B's, to distinguish fail-closed checks and false positive assumptions. Include interrupted deletion/restart, stale A writer, wrong UID, phase jumps, dual drivers, new B operation and receipt/cursor authority. After each, assert raw persisted canary absence or an explicit approved safe-retention exception, not only public API output. A separate server/UID oracle is needed before release PASS.

**Possible remediation alternatives, NOT APPROVED:**
1. Centralized registry-driven terminal erase of all 37 stores, then a new replica/Sync identity as appropriate; independently assess any per-installation Replica retention contract.
2. Targeted Sync-state and seven-store reset plus owner-scoped invariants, with a versioned compatibility strategy and old-writer fences. A mere `ownerUid` rewrite or adding a UI lock is insufficient.
3. Always validate all auxiliary rows on ordinary open, but this alone does not meet erasure/privacy requirements: refusing to open stale A rows is not equivalent to deleting them.

## Evidence boundaries and comparison

- **SOURCE:** exact named functions and line ranges above, `_validateSyncState` narrower than `_validateLbkSyncEvidence`.
- **SYNTHESIS:** the deletion+rebind path can preserve metadata fields and auxiliary records; ordinary-open header validation does not independently authorize them.
- **ENGINEERING JUDGMENT:** account erasure requires explicit ownership-scoped store sanitation and fail-closed state transitions, independent of B1 validation.
- **OPEN:** real A→B file-backed run, whether other open checks reject, data read/transmission, Firebase server state, exploitability, actual release ref and remediation approval.
- **VALIDATION:** none newly executed. No Stage-1 gate or production PASS.

## RELATED DOMAIN CHECK

Foundations: transactional ordering and aliasing of persistent identities; Architecture: single authoritative owner and bounded state transitions; Mobile: restart and old-tab/device behavior separate from file test; Data D005/D006: independent B1 owner oracle vs local F1 receipt/cursor semantics; Quality: use independent StoreRef enumeration and explicit negative controls; Systems: privacy/UID trust and post-deletion local erasure. Design/Web/Marketing: no new product-facing decision; existing PWA cross-tab deletion remains a transfer candidate, not evidence.

## HANDOFFS

**FROM:** Engineering Studio Systems S007. **TO:** LogMate/Codex product owner (advisory, no writes). **Decision/problem:** reconcile terminal wipe and ordinary-open/backup owner validation before Production Sync and Restore Activation. **Canonical source:** exact PR46 SHA and blob above; Studio S007 prior trace. **Requested action:** owner-authorized isolated exact-product file-backed A→B test with 37-store independent census and both local-open and B1 validation outcomes; then decide authoritative wipe/owner-scoped Sync policy and negative-path regression. **Status:** OPEN / product execution requires separate approval.

**TO:** Data D006: ensure no future automatic Sync consumes inherited cursor/receipt on mere owner-field equality. **TO:** Quality: distinguish 'open accepted', 'backup rejected', 'A metadata physically erased' and 'remote authority accepted' as four separate oracles. **CHANGE WATCH:** if LogMate repository blob or product policy changes, re-audit exact refs; do not repeat static trace on unchanged source.
