# S007 × W013 — Native independent-process stale-writer counterexample and deletion-authority transfer

**Evidence date:** 2026-11-07 (Asia/Seoul). **Status:** PRODUCT-EXECUTED NEGATIVE / SOURCE / SYNTHESIS / VALIDATION OPEN. This is a Studio read-only analysis of product-owned execution evidence, **not** a new Studio-executed Dart test or an observed customer incident.

## Exact identities and branch topology

- Canonical Studio before this study: `yhappcom/software-engineering-studio → main@37b0b62991b0c747ffb1eca727ad56a46a7752cf → 2026-11-07`.
- Product baseline: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec 1.0.0+1 → 2026-11-07`; deployed/production SHA unknown.
- Product new Draft: `yhappcom/logmate → feat/w013-supported-writer-20261107@e035d70dc8c51941a135c2f174659f280e3766d1 → pubspec 1.0.0+1 → 2026-11-07`; PR #47 based on PR #46 `aa4faeb4...`, which is stacked on #45→#44→#43→#42. Independent verification #39→#40→#41 remains a separate chain; none is presumed merged. Current enumeration: **62 remote branches, 13 open Draft PRs**.
- **Do not conflate test sources:** final Flutter regressions/builds at `dc7c5962fdcf1c55c30403eb1eda11429db6f815`; independent Native-process and Chrome-tab executions at `523083120ef8e14027dd3d6906ee21aa25e64dfe`; later documentation HEAD `e035d70...` is not itself a tested artifact.
- Primary evidence: `docs/evidence/w013-supported-writer-2026-11-07.md`, `docs/evidence/w013-supported-writer-2026-11-07/native-process-results-final.json`, and `docs/evidence/w013-supported-writer-2026-11-07/source-dc7c596/*meta.json` at PR47. Product `MASTER.md` and `docs/specs/backup-file-flow-spec.md` retain Activation HOLD and only scoped first writer-unit authorization.

## Distinct new evidence — process-local transaction check is not a cross-process fence

The first authorized W013 supported-writer unit introduces an owned repository facade, revocable session lifetime, and 31 protected transaction roots (28 existing mutations, initialization/migration, dispatch and recovery). The test-only `w013_test_only_writer_v0` guard is **not** a production protocol and is not installed by normal legacy open.

The independent Native IO test used distinct host processes against a synthetic file-backed Sembast ledger. Process A opened/cached the ledger. Process B sealed it at epoch 2. A then committed a stale write with exit 0. A third fresh-process inspection observed `records=1`, `pending=1`, and `guard.epoch=1, sealed=false`. Thus a check inside an apparently atomic transaction did not enforce an external seal across independently cached processes; the stale commit also overwrote the guard's observed sealed state. **This is an executed, bounded counterexample**, not merely static speculation.

The same product evidence separately reports controlled own-child SIGKILL before Commit → fresh-process ABSENT → exact retry once; after Commit → COMMITTED → retry without duplicate. Chrome same-origin separate tabs observed stale Seal rejection and one-winner CAS. Those positive outcomes **do not negate the independent Native-process failure** or establish cross-platform transfer.

Final-source reported checks: focused **806 PASS/1 SKIP**, full **1341 PASS/1 SKIP**, Chrome **48 PASS**, format/analyze and Web/Android-debug/iOS-simulator-debug builds successful. These are source-bound and product-executed; builds are not real-device acceptance, and the independent-process FAIL remains mandatory.

## S007 deletion and W013 Restore relationship

The earlier S007 static concern remains: terminal account deletion explicitly drops 29 stores versus a 37-store persisted inventory; ordinary DB owner checks and B1 owner checks have different coverage; A→B file-backed deletion/reopen remains unexecuted. The new W013 counterexample is **not** an execution of the S007 deletion coordinator and does not prove an A→B leak. It does falsify the *general assumption* that a process-local Sembast transaction check is sufficient to enforce an independently issued seal against an already-open Native writer.

Therefore S007's old-writer-after-deletion-intent oracle must explicitly include **independent processes with pre-opened DB handles**. In-process revocation, green unit tests, and even same-origin Chrome-tab results cannot replace that oracle. For W013, no durable guard, production lease/lock, cross-process owner election, legacy adoption, selector, generation or Activation should be declared accepted from the current evidence.

## Independent validation design and acceptance oracles

1. **Fresh isolated file-backed synthetic ledger:** seed all 37 persisted store classes with distinct A-owned canaries and inspect by independent raw-store enumeration, not only the app's own registry.
2. **Two independently launched Native processes:** A opens and retains a DB handle; B records deletion intent/seal and completes authorized terminal wipe; release A to attempt a previously prepared mutation. Fresh third process must observe no stale write, no restored old guard/owner, and zero residual A canaries. Test A commit before and after B, as separate schedules.
3. **Crash/interrupt boundaries:** SIGKILL at intent, guard/seal, per-store cleanup, and post-terminal phases; restart must be fail-closed and idempotent, with explicit legal phase-edge checks. Process SIGKILL is not OS power-loss proof.
4. **Owner B reopen:** independently verify no A Sync binding/receipt/cursor/head/hold rows; compare ordinary open, B1 validation and raw-store scan; no assumption that a changed `ownerUid` means scrubbed metadata.
5. **Separate platform transfer:** macOS-host file IO is a negative mechanism demonstration; actual iOS/Android process lifecycle, managed EFB/PWA and old binary compatibility require their own target-specific gates.
6. **No implicit solution selection:** evaluate pre-open OS-backed single-owner lifetime and crash/quiescence, generation-isolated storage, or other approved durable protocols as alternatives. Cross-process exclusion must be measured; a process-local `epoch` or lease in a cached Sembast DB is insufficient by the observed counterexample. No production protocol approval is implied.

**Oracle:** safety requires independent post-restart observation of no unauthorized stale commit, no resurrection of sealed/erased state, and no cross-owner residue. A test that only asserts that a method threw, a facade was revoked, or a CI job was green is insufficient.

## RELATED DOMAIN CHECK

- **Foundations:** file caches/process address spaces and transaction visibility; bounded Dart runtime is available, no old JIT/AOT blocker.
- **Architecture:** session ownership, raw adapter bypass, storage-opener authority and legacy compatibility.
- **Mobile:** iOS/Android Native process lifetimes versus Safari/IndexedDB tabs; simulator/build evidence does not establish managed-EFB or production acceptance.
- **Data:** Sembast file-backed durability, B1 37-store inventory, backup restore staging and Sync metadata ownership.
- **Quality:** adversarial two-process schedule, independent third-process oracle, failure injection, source-bound provenance and false-PASS prevention.
- **Systems:** account deletion/revocation and multi-process owner fences; S007 remains P0.
- **Design/Web/Marketing:** no visual change; Web EFB retention and public safety/Sync/Restore claims remain HOLD without product release evidence.

## HANDOFFS / OPEN

**Product/Codex Work approval required** for actual LogMate 37-store deletion execution, any source modification, native OS locking protocol, or new production persistent Guard/Outcome. Studio must not dispatch LogMate CI or touch real user DB. Existing PR47 is Draft and blocked on Native independent-process safety. Continue the reusable independent-process fault model in Studio-owned fixtures when runtime and source permissions allow; until executed, this note is a bounded transfer and an explicit new negative result from the product's own evidence.

**Gate:** W013 supported-writer unit **PARTIALLY VERIFIED / mandatory Native Gate FAIL**; W013 Activation **HOLD**; S007 deletion safety **OPEN**, with stronger required old-writer process oracle. No Stage-1 specialist PASS or release PASS.
