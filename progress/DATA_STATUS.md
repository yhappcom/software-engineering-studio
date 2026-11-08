## 2026-11-08 D006 restored-metadata ABA and signed-witness replay

**VERIFIED EXECUTION (independent synthetic SQLite WAL, 9/9):** after a second connection replaced event contents but reused owner/generation/version/floor/high, the old HMAC still verified; binding a signed incarnation rejected the old witness at incarnation102, but restoring incarnation101 re-enabled the old token against third-generation event contents. Signed metadata is not a current-page/freshness proof and an incarnation stored solely in a restorable snapshot is not rollback-resistant. Canonical `research/data/D006_restore_metadata_aba_witness_rollback_negative_2026-11-08.md`; public synthetic fixture `research/data/fixtures/D006_metadata_aba_restore_canary.py`. Executed local SHA-256 `018d4f8f40308714b4ba45b98cd50153109784174650613682a752ec53739c1d`; committed transcription byte equality and hosted replay OPEN. Product read-only main `f4bcd2f7...`, 1.0.0+1, 69 branches/20 Draft PRs; no Firebase/LogMate PASS, no product writes or CI. **Next gate:** separate non-restorable stream authority plus page-content binding and rollback/restart negatives; D006 Stage 1 NOT PASS.

## 2026-11-08 D006 actual SQLite WAL GC/page race and late-admission

**VERIFIED EXECUTION (independent Python 3.13.5 / SQLite 3.46.1 WAL, 9/9):** two concurrent file-backed connections proved a pinned reader snapshot retains old metadata+events while another connection commits GC; a fresh read sees the new floor; stale witness/split-view is rejected, uncommitted GC rollback survives reopen. **Distinct counterexample:** after GC, late insertion of lower seq2 is invisible to `seq>4` catch-up; server admission linearization is a separate required contract. Executed local script SHA256 `8fde5b2fb8be3ef5427728dfe6c6d14babeb53fb52807fab5bc6a90448572174`; cleaned equivalent committed fixture `research/data/fixtures/D006_gc_snapshot_two_connection_canary.py`, **not byte-identical/host-rerun**. Canonical `research/data/D006_gc_snapshot_two_connection_race_and_late_admission_2026-11-08.md`. Product read-only 69 branches/20 Draft PRs, main `f4bcd2f7...` version `1.0.0+1`. Firebase/product/Stage 1 PASS remain OPEN.

## 2026-11-08 D006 snapshot-bound retention witness negative oracle

**VERIFIED EXECUTION, bounded Node.js v22.16.0 deterministic synthetic classifier: 10/10.** Forged Boolean/modified MAC/foreign owner-generation/cursor and stale witness after simulated GC version advance rejected; authenticated stale cursor enters RECOVERY_REQUIRED. Public synthetic fixture committed; local executed script SHA256 `f1bb90a4635c1e1e8689b8033988cb922bddb7b2faf223a112238fbdf07a68cb`. HMAC key intentionally public/synthetic; this does **not** prove page completeness, freshness against a forged current view, real concurrent GC, Firebase, LogMate or Stage 1 PASS. Canonical `research/data/D006_snapshot_bound_retention_witness_negative_oracle_2026-11-08.md`.

## 2026-11-08 D006 retention-floor stale-cursor recovery negative

**VERIFIED EXECUTION, bounded synthetic model only:** Python 3.13.5 / file-backed SQLite WAL / two connections / independent reopen; **11/11** expected controls matched. Replica cursor1 behind retained floor3 must enter durable RECOVERY_REQUIRED without advancing; wrong owner/generation, absent completeness flag, excessive high-water, gaps and foreign-event context rejected; valid contiguous [3,4] from proven cursor2 persists. Exact executed script SHA-256 `6032adee8b547c8b224502d17d538976f0a9c0d246bbf85e2e5f883412e5ee85`; script local-only, not hosted/committed. Boolean completeness is **not** authenticated and forged-true/racing GC remain OPEN. Canonical `research/data/D006_retention_floor_stale_cursor_recovery_gate_2026-11-08.md`. No LogMate product claim or Stage 1 PASS.

## 2026-11-08 D006 late-commit visibility and cursor linearization

**VERIFIED EXECUTION — independent Python 3.13.5/SQLite 3.46.1 WAL, 10/10:** a pre-reserved seq1 became visible after committed seq2 and cursor2; immutable keyset+high-water silently omitted seq1. Dense committed-prefix refusal and same-SQLite-transaction allocation+event publication bounded alternatives passed. This is a synthetic model, not a LogMate/Firebase defect or production PASS. Local script SHA256 `833c5a85efb0643ee05c3fba01bfaad0debe5e8b438e7c28ca09e644d0db3615`, not hosted-rerun. Canonical `research/data/D006_late_commit_visibility_cursor_counterexample_2026-11-08.md`. Product read-only main `f4bcd2f7...`, 68 branches/19 open Draft PRs incl. PR52/53. **Next handoff:** exact server admission linearization/visibility order and authenticated complete prefix before cursor advance. D006 Stage1 NOT PASS.

## 2026-11-08 D006 mutable pagination / retention failure-first

**VERIFIED EXECUTION (independent SQLite synthetic, 7/7):** OFFSET pagination lost seq3 after retention deletion and duplicated seq20 after an intervening insertion; an empty OFFSET page falsely implied completeness. Bounded keyset+high-water avoided positional shifts but did not prove already-GC'd history or late-commit visibility. Local executed script SHA256 `84ef180b65b5ea6006ec8b11990340d36e02678792908c389c0aacfc57b51b7d`; functionally equivalent clean fixture committed, **not independently hosted-rerun**. Canonical `research/data/D006_mutable_pagination_retention_failure_first_2026-11-08.md`. Exact LogMate source unchanged, no product CI/writes, D006 Stage1 NOT PASS. Product handoff: define server sequence/commit visibility, snapshot bound, retention floor and stale-cursor recovery.

## 2026-11-08 D006 sparse global-sequence completeness oracle

**VERIFIED EXECUTION (independent model only):** Python3.13.5 file-backed SQLite WAL synthetic 12/12 checks. Owner A global seq1,3 cannot safely advance past missing seq2 without authenticated, complete, owner-bound skip evidence; dense owner-local streams instead require contiguous sequence. Negative cases: unproven/unauthenticated/wrong-owner/incomplete skip, cross-owner event, post-insert/pre-cursor crash+reopen, replay. Local script SHA256 `d1a11263856029f58fcf07699efead80eef2fc344e62bcc471a2ae8b2848faad`; not yet hosted or Studio-committed. The synthetic `authenticated` flag is an assumption, **not a cryptographic proof**. Canonical `research/data/D006_sparse_global_sequence_authenticated_skip_oracle_2026-11-08.md`. Product owner-local vs sparse-global sequence and actual completeness oracle remain OPEN; LogMate read only, no product CI; D006 Stage1 NOT PASS.

## 2026-11-08 D006 contiguous sequence and context negatives

**INDEPENDENT EXECUTABLE EVIDENCE:** Python3.13.5 file-backed SQLite WAL synthetic 9/9 after failure-first refinement. Sequence gap 1→3 is rejected until 2 arrives; owner/generation mismatch is fenced; crash before cursor commit rolls back; unsafe high-watermark advance loses records; forged historical replay (seq1 when cursor4) was initially accepted by a flawed synthetic checker, then fixed and regression verified. Canonical `research/data/D006_contiguous_cursor_owner_generation_failure_first_2026-11-08.md`. Local experiment SHA256 `224c274360ca379cb66e00c80c6585630701cdcaf8d6e4f87ebc25ebc0995097`, **not yet committed script/host rerun**. Sparse global sequences may need authenticated skip proofs; no product PASS. D006 Stage 1 NOT PASS.

## 2026-11-08 D006 independent file-backed receipt/cursor negative oracle

**INDEPENDENT EXECUTABLE MODEL — 6/6 bounded SQLite controls PASS** in local Python 3.13.5: lost-ACK retry preserves one server event, duplicate receipt identity, digest-collision rejection, record+cursor rollback under injected failure, reopen/replay convergence and **cursor-first silent-loss counterexample**. Three synthetic WAL SQLite DBs plus unsafe control, no private product source. Canonical `research/data/D006_sqlite_receipt_cursor_atomicity_failure_first_2026-11-08.md`. This proves a generic transaction-order mechanism only; no Dart/Sembast, Firebase, cross-process or release PASS. Product W013 #51 unchanged and unmerged; D006 Stage 1 NOT PASS.

## 2026-11-07 iPad Simulator actual Provider re-selection / bounded source invariance

Draft PR46 `aa4faeb4feba23655be79e2d11dc7c6393fec0f7` (61 branches/12 open PRs, declared 1.0.0+1; frozen executable `bd310585...`) adds actual iPadOS26.1 Simulator Safari-tab CUA selection, B1+isolated staging, screen-only Review, Home/resume expiry, explicit eventual Files cancellation and successful retry. Renamed Provider synthetic LBK and one original Safari download share 13276 bytes/SHA256 `826df401...`; new post-flow Safari internal download matches same hash and six prior synthetic files unchanged. This proves only **bounded synthetic memory-source B1 snapshot equality**, not persistent product DB invariance, new-download Files publication, installed/offline PWA, owner/Generation or Activation. Filename and Provider location changed together, so extension root cause is unproven. No Studio-run tests. `research/data/D005_ipad_simulator_provider_custody_and_snapshot_oracle_2026-11-07.md`; W013 IN PROGRESS, S007 OPEN, Stage 1 NOT PASS.

## 2026-11-07 W013 external saved-file integrity and scoped File UX closure

New Draft PR46 `9da013466705e18cb23d27f5011fb2cc15bc3393` (61 branches/12 open PRs, declared 1.0.0+1) records host-side independent measurement of a user-transferred **synthetic 13,276-byte LBK**, SHA-256 `5aa9cb8a06142612258eb45ed0f2fb0b26d1f7c83a320d4d332d797cf68648a5` matching the **user-reported** Safari Expected SHA, and product-side Dart CLI full B1/37-store + isolated candidate reopen **exit 0** at frozen executable `bd310585...`. Separately, physical iPad Safari actual Files Cancel/Retry and Review expiry are **USER-REPORTED PASS**; native Simulator Cancel/retry-open observed, iPad Simulator file select still inaccessible. This advances earlier external-file byte **NOT VERIFIED** and Provider Cancel **NOT RUN** classifications to scoped evidence, **not** installed/offline PWA, controlled browser persistence, real Owner, active Activation, release or S007 PASS. See `research/data/D005_w013_external_file_integrity_and_scoped_ux_closure_2026-11-07.md`. No new Studio tests or product changes.

## 2026-11-07 physical iPad Safari B1/review transfer — new user-reported evidence

LogMate Draft PR #46 latest documentation head `0073619667944f760366e37cc3b38774cb44611d` (61 branches/12 open PRs; 1.0.0+1, 2026-11-07) records a **physical iPad9 / iPadOS18.6.2 Safari normal-tab** synthetic file flow: user-reported B1 and temporary staging PASS in one trial; later menu dismissal, re-selection B1, screen-only Review acknowledgement and disabled Activation reported PASS. Frozen tested executable source is **`bd31058569e54f838a667c57865554aed1b3547e`**, not latest documentation HEAD. No new Studio-run device tests or product CI; independent external saved-file bytes/hash, explicit Files Provider Cancel, installed/offline PWA, durable product ledger, real Owner/Generation and Activation remain NOT VERIFIED/NOT RUN. Earlier Safari download-custody gap is **not closed** by selecting an already saved file. New canonical bounded transfer: `research/data/D005_physical_ipad_safari_picker_review_evidence_transfer_2026-11-07.md`. D005 bounded file-UX evidence advanced; Stage 1 NOT PASS.

# Data Specialist Status

## 2026-11-07 PR46 actual iPhone review / Safari custody boundary

New Draft `yhappcom/logmate → verify/w013-target-file-resume-20261107@472e3fa90c4e5f8c346aadc19d42f9e6ddd7ef24` (#46, one commit ahead of #45; declared 1.0.0+1, 2026-11-07) contains evidence-only iPhone17 iOS26.1 **actual OS picker→in-app file read/full B1/isolated staging/review** with Activation disabled, plus independent Files post-review save/readback preserving the current memory-source B1 hash. iPadOS Safari has download-complete/internal byte/hash evidence but Files On My iPad empty; **user-accessible file custody and repick remain NOT VERIFIED**, cause unknown. Source-level evidence is not Studio-run device validation or product/release PASS. Canonical new analysis: `research/data/D005_ios_safari_file_custody_evidence_ladder_2026-11-07.md`; Safari B0–B2 only, iPhone synthetic B0–B5. S007 29/37 deletion issue persists, identical product repository blob on PR46. Stage 1 NOT PASS.


## 2026-11-07 unmerged W-013 product transfer — SOURCE / bounded TRANSFER VALIDATION / OPEN

Product identity: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b` and separate Draft W013 product head `docs/w013-target-platform-validation-20261106@55a1ff894fcaa9e66765fcfe690c576dda61df98`; declared `1.0.0+1`; evidence date 2026-11-07; production ref unknown. Main is older than unmerged November 4–6 W013 development. W013 PR #38–45 include actual Export File UX, full B1 validation in isolated candidate/staging, review, background-state fix and recorded iPhone 17 iOS 26.1 Simulator Files-save + independent byte/SHA readback (13276 bytes). PR43 exact-source GitHub workflows 42159090172/93747/97089/100287 succeeded. PR41 retains a tested **uncooperative direct Repository writer bypass** in a synthetic restoration-fence candidate, not repaired production code. Activation, iOS in-app Open, Android device, physical iOS/iPad, installed/offline PWA, legacy writer fence and Firebase Owner/Generation remain OPEN. A separate owner-approved **Automatic + Manual Delta Sync**, native conditional automatic Backup and fourth onboarding `Restore from backup file` policy is recorded in Draft PR42 but not merged into main or implemented. Exact full audit: `research/data/D005_logmate_w013_unmerged_branch_backup_restore_transfer_2026-11-07.md`. **No new direct test in Studio; Stage 1 NOT PASS.**



Track: Data, Persistence & Distributed Systems  
Prefix: `D###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-25

## Mission
Build rigorous knowledge of data representation, integrity, persistence, transactions, schema evolution, migrations, caching, offline-first systems, replication, synchronization, conflict handling, backup/restore, and distributed-system semantics.

## Current evidence

### D001 — State, persistence, durability, source of truth and invariants
**IN STUDY — substantial first block complete.** Canonical: `research/data/D001_state_persistence_durability_source_of_truth.md`.

### D002 — Representation, files, databases, indexes and transaction fundamentals
**IN STUDY — two integrated executable Foundation blocks complete.** Canonical: `research/data/D002_representation_files_database_indexes_transactions.md`.

### D003 — Schema evolution, migration, rollback and compatibility
**IN STUDY — two integrated executable Foundation blocks complete.** Canonical: `research/data/D003_schema_evolution_migration_rollback_compatibility.md`.

### D004 — Cache semantics and offline-first data ownership
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/data/D004_cache_offline_first_data_ownership.md`.

### D005 — Backup, restore, recovery acceptance and crash/storage boundaries
**IN STUDY — prior SQLite recovery/WAL/backup evidence plus direct Dart candidate/publication TRANSFER VALIDATION.** Canonical includes the base recovery studies, `research/data/D005_online_backup_interruption_publication.md`, and `research/data/D005_dart_candidate_publication_transfer_2026-09-25.md`.

Prior Linux/Python/SQLite evidence distinguishes uncommitted rollback from committed persistence, forces bounded storage faults, models short writes/torn images, demonstrates WAL/main-file/checkpoint boundaries, active-reader checkpoint effects, live Online Backup concurrency, and interruption before backup completion/publication.

**TRANSFER VALIDATION — direct Dart process/file boundary:** exact workflow head `9c52779c0e69f10557e8e36da97db55aa24325f2`, hosted run `36020700051`, job `107704539236`, GitHub-hosted `ubuntu-24.04`, Dart 3.13.4, completed success. A child produced and flushed a semantically complete private replacement candidate, then was SIGKILLed before publication. The fail-closed parent oracle required nonzero child exit and proved the previously accepted generation=1/10-row artifact remained byte-identical and semantically intact; only a later explicit rename published the independently validated generation=2/200-row candidate. This transfers the candidate→validation→publication separation into direct Dart execution. It does not prove crash-durable rename, directory fsync, mobile filesystem behavior or hard-power-loss durability.

### D006 — Replication, synchronization, consistency, idempotency and conflicts
**IN STUDY — five integrated blocks; exact-ref LogMate protocol transfer added.** Canonical: `research/data/D006_replication_sync_consistency_idempotency_conflicts.md`, `D006_real_tcp_ambiguous_retry_restart.md`, `D006_network_namespace_link_interruption.md`, `D006_logmate_inbound_cursor_atomicity_transfer.md`.

## Product transfer retained
Latest product audit relevant to current Balance Loop: `yhappcom/logmate → main → 7551e1ca9e07df0b99e88aa03c8a56be03d8b2d3 → declared version 1.0.0+1 → evidence date 2026-09-25`; production identity remains unknown and default branch is not assumed production. D005 does not claim LogMate currently implements SQLite backup or the Dart publication fixture protocol.

## Gate assessment
Data Stage 1 remains **NOT PASS**. D001-D006 cover planned Foundation mechanisms with executable evidence, and D005 now has direct Dart process/file transfer in addition to SQLite/Python recovery evidence. Physical filesystem/device/power behavior, truthful-vs-lying fsync, crash-durable publication/directory fsync, sustained writer starvation/resource thresholds, Android/iOS transfer and exact product persistence/backup behavior remain incomplete.

## Dependencies / handoffs
- **Foundations:** direct Dart JIT/AOT and bounded Flutter browser runtime evidence exist; the historical direct-Dart-unavailable blocker is stale.
- **Architecture:** backup/export candidate, validated and published states are ownership and semantic-contract boundaries.
- **Mobile:** reproduce the Dart candidate-before-publication process-death oracle on exact Android/iOS/Flutter persistence/export stacks.
- **Quality:** require nonzero injected-failure evidence plus independent old/new semantic state oracles; workflow green alone is insufficient.
- **Systems:** validate publication durability separately: file/directory synchronization, replacement primitive, temporary destination lifecycle and hard-power-loss boundary.
- **LogMate:** define backup consistency point, completion/validation/publication semantics before implementation and transfer-test on an exact product ref/build.

## CHANGE WATCH / OPEN
- D005 physical storage/power behavior, lying-successful fsync, directory fsync, crash-durable publication, sustained writer starvation/resource thresholds and Android/iOS transfer remain OPEN.
- D006 remote/packet faults, concurrent retry, dedup retention/GC, external side effects, tombstone GC and real multi-writer/backend evidence remain OPEN.
- Exact LogMate persistence/backup/export transfer remains OPEN.
- No Data Foundation PASS yet.

## Next work
Return to Balance Loop. Do not repeat equivalent Linux candidate-before-publication process-kill variants. Prefer a materially stronger evidence class: physical/mobile filesystem transfer, hard-power-loss/publication durability, exact product persistence/backup runtime, or another track's stronger Stage-1 gap.
