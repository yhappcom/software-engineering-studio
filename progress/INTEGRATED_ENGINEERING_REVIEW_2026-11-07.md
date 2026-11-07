# Software Engineering Studio — Integrated Evidence and LogMate Engine Advisory Review

## 2026-11-07 branch audit addendum — changes the product-priority interpretation

The initial review above used `main@f4bcd2f7...`; newer **unmerged** code/policy exists. GitHub enumeration on 2026-11-07 found 60 branches, 11 open Draft PRs, W013 #38–45 eight PRs. Two separate W013 stacks: product/docs `#42→#43→#44→#45` (`55a1ff894...`, 11 ahead/0 behind main) and staged synthetic writer/recovery probes `#39→#40→#41` (`cc600792...`, 16 ahead/0 behind main). PR43 selectively reuses PR38 export code. Do not treat them as one merged product.

**Policy correction:** owner-approved and documented in unmerged Draft PR42: Automatic + Manual Delta, normal catch-up for supported native/active PWA, manual-only `lastSyncAt` activity, Native manual+conditional automatic Backup, PWA manual external-file backup, and fourth onboarding `Restore from backup file`. This supersedes the October Manual-only interpretation for future advice but does not mean main is synchronized, Production Sync runs, or Restore Activation exists.

**Implementation and evidence correction:** Draft PR43 has actual user-file review, B1 isolated staging, source preservation and disabled Activation; PR44 fixes background stale-completion review; PR45 adds isolated iPhone17 iOS26.1 Simulator Files saved-byte external reread and separate B1 validation. PR43 exact source `4999af73...` produced four observed GitHub completed/success workflow runs 42159090172, 42159093747, 42159097089, 42159100287. PR44 test source `ceb5c0c...` produced checkpoint success 42171249085. PR41 synthetic runner observed raw-handle writer-fence bypass and test-only repair variants, **not product-wide enforcement**. No new Studio tests or physical/installed EFB/runtime/production PASS claimed. W013 latest branch Work count is 7 COMPLETE/2 IN PROGRESS/28 NOT STARTED, main's 7/1/29 older scope remains separate. Account deletion 29/37-store static contradiction still requires independent P0 validation and was not repaired in observed W013 code.

Prioritize approved W013 handoff and exact new validation evidence when product team requests advice; retain S007 account-delete integrity as separate higher-severity release correctness risk. See `research/data/D005_logmate_w013_unmerged_branch_backup_restore_transfer_2026-11-07.md`. Preserve other Studio and product authority boundaries.



**Evidence date:** 2026-11-07 (Asia/Seoul). **Authority:** coordinator synthesis; not an amendment of LogMate product policy.
**Studio input:** `yhappcom/software-engineering-studio → main → 20aa7c582406c221096196c41f0101b37838fc46`, subsequently augmented by `research/systems/S007_logmate_deletion_integrity_exact_ref_audit_2026-11-07.md`.
**Product input:** `yhappcom/logmate → main → f4bcd2f7b7e77039e29653baa1cc93797673885b → declared 1.0.0+1 → 2026-11-07`. Production/deployed ref unknown. Product repository was read-only; no product writes or new tests occurred.
**Cross-repo inputs:** Design Studio `main@3264d490...`; Web Manager `main@2bb27c2e...`; Marketing Manager `main@dcf5fa19...`; their claims retain their own evidence boundaries.

## Executive conclusion

The Studio already has substantial first-principles/executable evidence across six tracks. Continued hourly microtopic proliferation has lower marginal value than **exact-product implementation transfer, negative-path verification, and reusable regression gates**. The old recurring F001 premise that direct Dart JIT/AOT and Flutter execution are unavailable is factually outdated: F001 already has direct Dart JIT/AOT plus Chrome and bounded macOS Safari evidence. Nevertheless **all six Stage 1 gates remain NOT PASS** under the current canonical status, and bounded fixture PASS is never release PASS.

The old Studio `progress/STATUS.md` is September-centered. Current LogMate `MASTER.md`/source/evidence must supersede its old inference that signed-out local-first Welcome still represents product implementation.

## Six-track evidence summary (no new PASS awarded)

| Track | Strong existing evidence | Material open boundary |
| --- | --- | --- |
| Foundations F001–F006 | direct Dart JIT/AOT, Flutter Chrome/Safari, direct identity, structures, isolate, async and OS socket root-cause/fix/regression | native/product/release transfer; physical runtime and cross-context |
| Architecture A001–A007 | information hiding/change pressure, dependency direction/ownership, contracts/API evolution, refactoring evolution, ADR governance and Light/Dark role ownership transfer | actual modern product code refactor, authoritative screen semantics, natural ADR supersession and real-native visual/state acceptance |
| Mobile M001–M006 | emulator lifecycle, foreground/background/permissions, bounded Keystore, Chromium PWA and Safari worker lifecycle | actual iOS/iPadOS/physical/OEM/EFB/installed-PWA/eviction/long-offline acceptance |
| Data D001–D006 | Sembast/SQLite storage, schema migration, WAL/recovery/failure injection, direct Dart candidate-publication, Sync idempotency and transport models | populated product storage/backup/delete, hard-power-loss/directory durability, live server replication/convergence |
| Quality Q001–Q006 | oracle/independence, property/mutation testing, fault isolation; CI delegated/action/output/reusable/matrix/skipped failure controls and natural Mobile immutable-action transfer | present product release gate, non-Bash/cancelled/redacted controls and exact product failure/recovery oracles |
| Systems S001–S007 | trust/security/cost/build provenance/attestation/rollback and Auth/onboarding/deletion semantic models | real Firebase/backend/platform independent validation, deletion completeness, current-product release provenance |

## Latest product change: what is already present versus not closed

The exact LogMate source `main@f4bcd2f7...` has account-required `SessionGate`/Firebase Auth/provider seams; UID-owned local repository; minute-typed canonical ledger; revision/CAS, immutable outbox, timeline/page/checkpoint publication; typed Custom Flight fields; Add/Edit/Draft/View; B1 whole-ledger format; and F1 local Sync state/replica identity (capability-v17).

**W-003 / O18 local Home scope:** user-approved LIMITED COMPLETE and PR37 merged. Actual closure evidence retains 7 COMPLETE / 1 IN PROGRESS (W-031) / 0 READY / 29 NOT STARTED out of 37; existing exact-source focused 637 and full 1,184 pass / 1 skip, with a separate exact-source PWA upload/download/verifier roundtrip PASS. Visual Mobile Dark End remains unresolved. Existing tests/renders are historical per their SHAs; no new `main@f4bcd2f7` CI run was conducted for this review. File DB close/reopen is **not** OS process death or independent Files recovery.

**Major accepted-but-not-built capabilities:** 2026-10-17 Local-First **Manual Delta Sync** is a CONFIRMED product contract, but its production server/receipt/cursor/apply/convergence vertical slice is NOT IMPLEMENTED. Production Import/roster parser+review+batch/undo, personal Search, remaining full Core surfaces, physical Android/iOS and EFB installed PWA/release acceptance remain separate OPEN requirements. PWA is the only V1 Web-family product target; desktop web is out of scope. The roadmap is a proposal until approved Work IDs are assigned.

**Cross-domain product boundaries:** Figma is final visual authority; Flutter host-render tests are functional evidence, not final visual approval. Design Studio owns role/color/layout/content semantics. Web Manager reports PWA RELEASE HOLD and preserves unexecuted 37-store/deletion/managed-EFB test requirements; Marketing Manager holds LogMate public Import/Store/PWA claims and does not activate ads until real manual Sync/consent/deployment gates are satisfied.

## High-value CONTRADICTION: deletion terminal authority

At current exact LogMate source, deletion-phase progression uses forward enum index rather than adjacent legal edge; normal coordinator is sequential, but repository admission is weaker. Terminal wipe drops 29 stores while the Sync-aware 37-store model includes local replica and seven Sync stores omitted from the explicit wipe list. `requestAccountDeletion` records a deletion phase but does not atomically change `LocalOwnerAccess.lock`; whether already-open stale writers can mutate after intent requires direct execution. Three current in-memory coordinator tests do not prove full 37-store sanitizer parity. This is **SOURCE / CONTRADICTION, runtime VALIDATION OPEN**, not a witnessed privacy incident. See canonical focused audit in `research/systems/S007_logmate_deletion_integrity_exact_ref_audit_2026-11-07.md`.

## Ranked next learning/application blocks

1. **P0 — S007 × Data × Quality: file-backed deletion authority/completeness**. Verify 37-store synthetic owner-A canaries, all legal/illegal phase transitions, old writer after intent, duplicate driver and interruption, terminal wipe/reopen and owner-B normal startup. Compare existing manual list with registry-driven erase and independently enumerate stores; no real customer DB. Product changes need an explicitly authorized LogMate Work. High risk, reusable state/erasure correctness; most important closed-bounded next block.
2. **P1 — D006 × Systems × Quality: production Manual Sync trust/receipt/idempotency vertical-slice design + executable failure oracle**, only against approved exact product contract. Preserve local-first commit, stable Operation/Replica identity, authenticated server receipt, zero-delta sync, UNKNOWN/retry, 2-device convergence, server cursor and Firestore no-direct-client-write policy. Do not relabel F1 local persistence as live Sync.
3. **P1 — D005 × Mobile × Web Manager: B1 backup/export/Files/PWA custody, process death and independent reopen**. Distinguish candidate completion, publication, durable filesystem sync, external file ownership, file transfer and installed EFB retention. Reuse existing W-012 native restore evidence before testing new platform/failure class.
4. **P1/P2 — Architecture × Quality × Mobile: actual Core Logbook transaction/UI transfer and exact artifact gates**. Reuse W-003 verified Home/read models and Codex Work IDs; validate Custom→Add/Edit→View official totals→Home→restart/Draft across supported platforms, with neutral reference oracles and Figma approval kept separate.
5. **P2 — release/marketing dependencies**. Source-ref→toolchain→PWA artifact ZIP and served origin→browser/device→logbook local safety; Apple/Google provider, remote deletion, web request path, real Auth/Store claims and deferred ads. Keep LogMate ads optional/native only under existing owner constraints; no PWA ad runtime.

## Cadence and queue governance

Recommended **one integrated substantive learning block per hourly trigger, not six microtasks**. Each run: read current Studio protocols/six statuses/index/recent commits; inspect exact current LogMate ref and only materially relevant Design/Web/Marketing evidence; score risk, prerequisite, product leverage, evidence gap, cross-track leverage, reuse and urgency. Prefer a genuinely new executable failure/transfer/production oracle. An unchanged upstream SHA with no new evidence should not produce duplicate notes or false PASS; instead advance an independent prerequisite or record a dependency. Run-source and result provenance must remain reproducible; work must not mutate other repositories.

**No new validation in this synthesis.** Stage 1 all NOT PASS; production-release status unverified. Previous evidence is referenced, not rerun. Re-audit current LogMate refs before applying advice; no autonomous product implementation is authorized.

## RELATED DOMAIN CHECK / HANDOFFS

Foundations: reuse actual Dart runtime, no stale SDK blocker. Architecture: shared state-machine ownership and transaction boundaries. Mobile: native/installed PWA lifecycle and old client sessions. Data: 37-store Sync deletion and backup/receipt. Quality: independent canary and negative oracles. Systems: Auth revocation and server erasure, release provenance. Design: final Figma state authority. Web: managed EFB and served PWA. Marketing: no unverified claim or ad activation. LogMate: source truth read only.

**HANDOFF to LogMate owner/Codex (advice, not execution order):** first consider an explicitly approved deletion-integrity Work, then Manual Sync and independent backup/PWA acceptance; keep existing W-003 closure and F1 tests as bounded regressions, and assign no new Work without owner approval.

**OPEN:** actual 37-store test, old-writer/dual-driver path, secure remote deletion, physical/managed EFB, standalone production Sync, import, release and stage-gate evidence. No broad PASS inferred.
