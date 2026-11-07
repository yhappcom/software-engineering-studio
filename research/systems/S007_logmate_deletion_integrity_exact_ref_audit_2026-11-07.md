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

## 2026-11-07 exact unmerged W-013 branch recheck — SOURCE / CHANGE WATCH

New product ref inspected read-only: `yhappcom/logmate → docs/w013-target-platform-validation-20261106 → 55a1ff894fcaa9e66765fcfe690c576dda61df98 → pubspec 1.0.0+1 → 2026-11-07`; `main@f4bcd2f7b7e77039e29653baa1cc93797673885b` remains the comparison baseline, and deployed/production identity remains unknown. This W-013 branch is stacked on Draft PR #42→#43→#44→#45 and has **not** been merged into main. Independent recovery writer probes PR #40→#41 are a separate Draft chain; their test-only adapter must not be represented as installed product fencing.

**New exact-ref identity observation:** `lib/repository/logbook/sembast_logbook_repository.dart` has the **same Git blob SHA `f2b8b0eb681f5d960532dac5c87b29cf85a459b8`** at both main and PR #45 HEAD. The actual `requestAccountDeletion`, `advanceAccountDeletion` and `wipeLocalUserDataAndCompleteDeletion` functions were re-read on both refs. Therefore the previously recorded 29-drop/37-store and nonadjacent phase-admission static contradictions **also apply to this latest W-013 product branch**; W-013 file-review work did not itself repair them. The identical blob is stronger than assuming all new PR code is merged, but is **not** a runtime or user-data erasure test.

**Cross-boundary relevance:** PR #43 adds backup-file selection, isolated temporary B1 staging, review and owner/session/deletion checks; PR #44 corrects background review expiry; PR #45 adds target-platform simulator evidence. All retain disabled Production Activation. This creates an additional review dependency: a future activation or recovery path must not reuse an already-open repository writer after deletion intent, nor interpret a successful file review as authorization to bind a deleted owner. Current W-013 tests do not establish the S007 all-store terminal-wipe, stale-writer or cross-account reopen oracles. The separate PR #41 synthetic writer-probe demonstrates that bypass by an uncooperative/raw handle is a real *probe boundary*, not a product-wide repair.

**Validation boundary:** exact-source code/blob comparison and PR/evidence reading only. No LogMate tests, CI dispatch, user DB, file mutation, production authentication or deployed PWA execution. Studio Stage 1 remains NOT PASS. Prior proposed exact-product canary tests still require a separately authorized LogMate/Codex Work; no automatic Work creation or product-policy change follows.

**RELATED DOMAIN CHECK:** Foundations—direct Dart execution exists but was not needed for this source-identity recheck. Architecture—repository transaction/facade and deletion admission authority. Mobile—old tab/process and actual Files custody still open. Data—B1 37-store registry, W-013 candidate staging and F1 local state. Quality—independent all-store canaries and negative transitions required. Systems—terminal erasure and stale-owner access. Design Studio—not materially needed for the unchanged code-identity claim; future review/lock semantics remain design-owned. Web Manager—managed EFB/PWA lifecycle is a transfer candidate. Marketing Manager—do not claim completed deletion/privacy or Restore readiness. Product—main and PR #45 both read-only.

**HANDOFFS:** To LogMate/Codex (approval required): before integrating W-013 activation, run file-backed populated 37-store deletion tests, old-handle after intent, phase-edge negatives, interrupted/dual-driver and owner-A→B reopen against an exact approved product ref, with independent store enumeration and no user DB. To Data D005/D006: preserve candidate/active ledger isolation and Generation/Owner proof. To Quality Q006: require per-source execution/negative reports; do not convert PR #45 simulator Save or PR #41 test-only fencing into deletion PASS.
