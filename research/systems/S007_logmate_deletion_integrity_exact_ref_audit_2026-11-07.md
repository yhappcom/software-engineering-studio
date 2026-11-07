# S007 — LogMate Account-Deletion and Local-Store Integrity: Exact-Ref Transfer Audit

Status: **SOURCE / CONTRADICTION / ENGINEERING JUDGMENT / VALIDATION OPEN**. No product tests executed in this audit; no product repository edits.
Evidence date: **2026-11-07 (Asia/Seoul)**.
Canonical Studio read: `yhappcom/software-engineering-studio → main → 20aa7c582406c221096196c41f0101b37838fc46`.
Product read: **`yhappcom/logmate → main → f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec.yaml 1.0.0+1 → 2026-11-07`**. Production/deployed ref unknown; `main` is not asserted to be production.
Cross-reference: Web Manager `STATUS.md` (2026-11-07) and `research/529_stage8_pwa_owner_deletion_backup_mdm_custody_20261030.md`, prior Studio `S007_account_deletion_reauthentication_revocation_saga.md`, LogMate `MASTER.md` §0 / §13 and `docs/evidence/w003-o18-closure-2026-10-31.md`.

## Scope and observed product change

The Studio's September S007 global/status records describe an old Welcome/documentation-only implementation baseline and are stale for the product. Current LogMate source has `lib/app/session_gate.dart`, `lib/application/account_deletion_coordinator.dart`, account-required Auth/provider surfaces, local owner access, Sync v17 local persistence, and a W-003 local Home implementation merged by PR #37. The current `MASTER.md` confirms local-first, Firebase UID owner authority, Manual Delta Sync approved but **production server Sync not implemented**, and separate release/physical-device gates.

## SOURCE / CONTRADICTION: deletion step admission versus declared saga

At `lib/repository/logbook/sembast_logbook_repository.dart`, `requestAccountDeletion` records `localLocked` but does not update `BoundLocalOwnerAccess.lock` in the same transaction. `advanceAccountDeletion` rejects `none`, `completed`, and backwards indexes, but does **not** enforce an exact adjacent predecessor/successor transition. Thus the repository's public transition API alone does not structurally require every intervening irreversible side effect. The normal `AccountDeletionCoordinator.resume()` *does* call reauth → revoke → remote erase → identity delete → local wipe sequentially, so this is an **admission/encapsulation gap**, not proof that the normal flow skips steps or that a remote attacker can exploit it.

The coordinator reads phase then awaits external ports without an observed single-flight, lease, expected-predecessor CAS or independent server-authority oracle in that file. Two concurrent clients/drivers may therefore be a **race/failure hypothesis**, not a proven duplicated side effect or exploit. A concurrent exact-product test is needed.

## SOURCE / CONTRADICTION: local wipe versus persisted Sync store set

The current backup registry in the same repository defines **37** persisted stores, including `_localReplicaStore` and seven Sync stores. In `wipeLocalUserDataAndCompleteDeletion`, the explicit drop loop includes **29** stores and omits the local replica store and seven Sync stores. After the loop, `_initializeFreshDatabase` is invoked. In `_writeOwnerAccess`, clearing/replacing the local owner changes `_syncStateStore.ownerUid` but does not clear the other Sync-state fields or all other Sync stores. This is a **static deletion-completeness contradiction** with the product contract requiring terminal local user-data erasure, especially when pre-deletion Sync stores are populated.

This audit does **not** claim residual data is readable to a user, that a second UID successfully binds via normal startup, that the deployed app shares this code, or that a production data incident occurred. It identifies the stronger missing oracle: terminal `completed` and unbound owner are insufficient to prove full persisted-store sanitization.

Current `test/application/account_deletion_coordinator_test.dart` includes three in-memory tests: ordered success, remote failure/resume and wrong-UID rejection. These do not populate all 37 stores, inject cross-process death, execute two drivers, or verify A-delete→B startup after file close/reopen. Their presence is not an execution result for this audit.

## Engineering judgment and alternatives

**Priority P0 for release correctness, NOT permission to edit LogMate:** before adding more synthetic S007 models, perform an isolated exact-head **Dart/Sembast populated-store file-backed failure-first audit**. Generate known canaries for all existing store classes and verify before/after identity by independent enumeration. Exercise deletion request, old-writer mutation attempt, each phase-edge negative case, duplicate-driver/interrupted external calls, terminal wipe, reopen, and same-device different-UID startup. For remote/provider obligations, a local fake is only a model: require Auth Emulator/backend-independent oracle and a durable remote erasure/idempotency ledger before claiming release PASS.

Compare (A) a single authoritative registry-driven and centrally validated erase transaction against (B) expanding a manually maintained drop list, with explicit treatment of local replica identity, backup Files artifacts, retained audit/tombstone rules, and recovery semantics. Do not silently declare external Files backups erased; distinguish app-controlled local stores from user-exported independent copies and public disclosure obligations.

**Phase invariant:** after deletion is requested, every write path, including already-open handles/other tabs and stale callbacks, must be denied at the persistence authority; a UI-only Home block is insufficient. Coordinate with Data D005/D006, Mobile M002/M006, Quality Q004/Q006 and Security S007 before implementation.

## RELATED DOMAIN CHECK

- **Foundations:** direct Dart JIT/AOT and Flutter execution have already been validated by F001; old prompt blocker is superseded, not a reason to simulate tests.
- **Architecture:** one authoritative deletion phase/state machine and ownership of guard enforcement vs UI surface; no boolean-only or UI-only state authority.
- **Mobile:** Android/iOS lifecycle, Web IndexedDB/old tab, managed EFB and physical-device boundaries are separate transfer gates.
- **Data:** D005 publication/backup acceptance, D006 replica/outbox/cursor identity and complete 37-store durability; terminal wipe must not rely on old 29-store shape.
- **Quality:** independent canary count/oracle, failed transitions, interruption, process death, dual writers and exact artifact capture.
- **Systems:** recent reauth, Apple revocation and server erasure are separate irreversible boundaries; Firebase official reauth and federated-auth documentation rechecked 2026-11-07.
- **Design Studio:** deletion/recovery UI states must faithfully reflect locked/partial/retry outcomes; visual approval is not a local-data erase oracle.
- **Web Manager:** the 2026-10-30 PWA 529 report is a **DIRECTLY APPLICABLE static-source issue** at the inspected current deletion functions; its proposed Web/physical tests remain **TRANSFER CANDIDATES** and unexecuted.
- **Marketing Manager:** do not promote release/deletion/privacy claims until the product and release gate accept exact evidence.
- **LogMate:** exact current `main` audited read-only; `MASTER.md` remains product authority.

## VALIDATION / OPEN / HANDOFFS

**VALIDATION OPEN:** no new executable test/run/device/product artifact was generated. No PASS or deployment assertion. Next accepted evidence must be exact-code checkout, toolchain and store-registry identity, fixture input, semantic oracle, raw observed results, negative failures, persistence restart and independent remote oracle. Reassess after any product ref moves.

**HANDOFF — Engineering Studio → LogMate/Codex (advisory only):** request owner-approved Work scope for the bounded deletion-integrity regression; preserve existing product source and user ledger. Acceptance requires no stale A-owned canaries, fail-closed writes after intent, legal transitions only, idempotent/crash-resumable provider/server work, terminal local erasure, explicit independent Files-custody boundary, and normal B startup behavior as selected by product policy. Do not edit LogMate from Studio.

**CHANGE WATCH:** Flutter/Firebase provider behavior, Apple revocation requirements, Google Play external deletion path, managed iPad PWA and storage policies must be rechecked against current primary docs before release decisions.
