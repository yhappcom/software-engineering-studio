## 2026-11-08 D006 stale-cursor retention floor

New independent local SQLite WAL failure-first evidence (11/11 synthetic controls): a replica cursor behind the server retention floor cannot safely advance to the first surviving page; explicit durable RECOVERY_REQUIRED and separate authenticated recovery are needed. Boolean completeness input is **not** a real proof. Executed script local-only SHA-256 `6032adee8b547c8b224502d17d538976f0a9c0d246bbf85e2e5f883412e5ee85`; hosted/byte-identical replay, forged-proof and concurrent GC remain OPEN. No LogMate write, product defect claim or Stage 1 PASS. Canonical `research/data/D006_retention_floor_stale_cursor_recovery_gate_2026-11-08.md`.

## 2026-11-08 D006 late-commit visibility and cursor linearization

**VERIFIED EXECUTION — independent Python 3.13.5/SQLite 3.46.1 WAL, 10/10:** a pre-reserved seq1 became visible after committed seq2 and cursor2; immutable keyset+high-water silently omitted seq1. Dense committed-prefix refusal and same-SQLite-transaction allocation+event publication bounded alternatives passed. This is a synthetic model, not a LogMate/Firebase defect or production PASS. Local script SHA256 `833c5a85efb0643ee05c3fba01bfaad0debe5e8b438e7c28ca09e644d0db3615`, not hosted-rerun. Canonical `research/data/D006_late_commit_visibility_cursor_counterexample_2026-11-08.md`. Product read-only main `f4bcd2f7...`, 68 branches/19 open Draft PRs incl. PR52/53. **Next handoff:** exact server admission linearization/visibility order and authenticated complete prefix before cursor advance. D006 Stage1 NOT PASS.

## 2026-11-08 D006 mutable pagination / retention failure-first

**VERIFIED EXECUTION (independent SQLite synthetic, 7/7):** OFFSET pagination lost seq3 after retention deletion and duplicated seq20 after an intervening insertion; an empty OFFSET page falsely implied completeness. Bounded keyset+high-water avoided positional shifts but did not prove already-GC'd history or late-commit visibility. Local executed script SHA256 `84ef180b65b5ea6006ec8b11990340d36e02678792908c389c0aacfc57b51b7d`; functionally equivalent clean fixture committed, **not independently hosted-rerun**. Canonical `research/data/D006_mutable_pagination_retention_failure_first_2026-11-08.md`. Exact LogMate source unchanged, no product CI/writes, D006 Stage1 NOT PASS. Product handoff: define server sequence/commit visibility, snapshot bound, retention floor and stale-cursor recovery.

## 2026-11-08 D006 sparse global-sequence completeness oracle

**VERIFIED EXECUTION (independent model only):** Python3.13.5 file-backed SQLite WAL synthetic 12/12 checks. Owner A global seq1,3 cannot safely advance past missing seq2 without authenticated, complete, owner-bound skip evidence; dense owner-local streams instead require contiguous sequence. Negative cases: unproven/unauthenticated/wrong-owner/incomplete skip, cross-owner event, post-insert/pre-cursor crash+reopen, replay. Local script SHA256 `d1a11263856029f58fcf07699efead80eef2fc344e62bcc471a2ae8b2848faad`; not yet hosted or Studio-committed. The synthetic `authenticated` flag is an assumption, **not a cryptographic proof**. Canonical `research/data/D006_sparse_global_sequence_authenticated_skip_oracle_2026-11-08.md`. Product owner-local vs sparse-global sequence and actual completeness oracle remain OPEN; LogMate read only, no product CI; D006 Stage1 NOT PASS.

## 2026-11-08 D006 contiguous cursor / historical replay negative evidence

Independent Python3.13.5 SQLite WAL synthetic canary 9/9: seq1→3 gap refused, later seq2→3 replay recovered; wrong Owner/Generation rejected; post-record/pre-cursor crash rolled back after reopen; unsafe high-watermark jump skipped records. A synthetic model flaw that checked only the current cursor allowed forged older seq1 after cursor4; corrected to verify all historical seq identities and reran 9/9. Canonical `research/data/D006_contiguous_cursor_owner_generation_failure_first_2026-11-08.md`. Local script SHA256 `224c274360ca379cb66e00c80c6585630701cdcaf8d6e4f87ebc25ebc0995097` not yet published as a fixture. Sparse global server sequence/filtered events need authenticated skip proof; D006 product Dart/Sembast/Firebase and Stage1 PASS remain OPEN. LogMate read only, 66 branches/17 Draft PRs; no product CI.

## 2026-11-08 D006 independent SQLite failure-first evidence

A new **Studio-owned independent execution** (local Python3.13.5 SQLite WAL, 6/6 synthetic controls) discriminated safe atomic local record+applied-cursor commit from **cursor-first silent data loss** under interruption, and verified same-OpID/digest ACK-loss retry versus digest collision. This is a generic prerequisite, not product Sync PASS; exact LogMate W013 #51 remains unmerged and S007 deletion OPEN. Canonical `research/data/D006_sqlite_receipt_cursor_atomicity_failure_first_2026-11-08.md`; no private LogMate code/tests or CI invoked. Data Stage 1 NOT PASS.

## 2026-11-08 PR51 iOS same-PID observation / adoption approval still pending

New unmerged Draft PR51 `62d7295da6b447ba45dd3f0196c81ec449f2cdf9` atop PR50 reports a **bounded iOS Simulator same-PID ordinary double launch** (PID76822, factory0, 172 installed artifact files matched), not a two-Repository lock/Seal test. It proposes, but does **not** approve or implement, fresh-only Native application-private namespace integration with release enrollment OFF, legacy-only untouched and both-path/downgrade HOLD; old binary cross-path fork remains a limitation. Exact executable is older `ce81418fe5c962b06e5cd42264ec3d2165794d3d`; PR51 is evidence/proposal, not new runtime. iOS independent Repository PID and physical gates, S007 deletion and W013 Activation remain OPEN. Systems canonical: `research/systems/S007_w013_pr51_ios_pid_observation_and_fresh_only_adoption_review_2026-11-08.md`. No Studio-run product tests or new Stage 1 PASS.

## 2026-11-08 PR49 bounded iOS Simulator ownership transfer

New unmerged LogMate Draft PR49 `dd221883edcb01bc879be8fe0f1f1a33d353e477` stacked on #48, frozen executable `ee5b03629ce804ae31f97a2baa7f89d61fa795a4`, reports 9 actual iOS26.1 Simulator Session cases, 8 controlled recovery groups/15 app PIDs, independent C↔Dart kernel directory contention with 0 Sembast factory calls on rejected open, full Flutter 1360 PASS/1 SKIP and Chrome 48 PASS. Android ARM64 ABI/build only; no Android runtime. **Two independent mobile Repository PIDs with Seal/Epoch/History NOT RUN**, no production/default Legacy enrollment or physical iOS; Supported Writer OPEN/BLOCKED, Restore Activation HOLD, S007 37-store A→B OPEN. No Studio-run tests. See `research/systems/S007_w013_pr49_ios_simulator_ownership_and_repository_pid_gap_2026-11-08.md`.

## 2026-11-08 PR48 bounded Host ownership correction, S007 still OPEN

New LogMate Draft PR48 `afbdbf037b637bb924ffc9bea173e87385dd398f` stacked on PR47 (63 branches/14 open PRs) reports a materially new **synthetic macOS Host pre-open kernel ownership PASS** at frozen execution SHA `eff2f0f501c2f909d01dc5eee737235d82c94ea3`: 9 independent-process groups/41 child PIDs, 16 Native units, 1357 Flutter PASS/1 SKIP and 48 Chrome PASS. B is denied before DB factory while A owns; lock persists through actual Close, third process sees sealed epoch2. The original PR47 stale raw-writer FAIL remains a valid bypass counterexample. **No iOS/Android backend, production/default Legacy enrollment, old-client isolation or S007 37-store deletion/A→B execution**; W013 Supported Writer Acceptance OPEN, Activation HOLD, S007 OPEN. No Studio-run tests or CI. See `research/systems/S007_w013_pr48_preopen_native_ownership_host_gate_transfer_2026-11-08.md`.

## 2026-11-07 PR47 Native cross-process writer safety failure

New unmerged LogMate Draft PR47 `e035d70...` stacked on PR46 (62 branches, 13 open Draft PRs) reports a **real synthetic file-backed two-process Native FAIL** at exact execution source `5230831...`: a cached old writer committed after a separate process sealed epoch2; fresh third-process read showed epoch1/unsealed and one committed record. The bounded facade and 1341 Flutter PASS at `dc7c596...` do not close this independent-process gate. This changes the S007 test priority: an old-writer-after-deletion-intent case must use independently opened Native processes and independent raw-store inspection, not just same-process revocation. This is **not** an executed S007 deletion/A→B leak. Canonical `research/systems/S007_w013_native_independent_process_stale_writer_counterexample_2026-11-07.md`; W013 Activation HOLD and S007 37-store deletion OPEN. No new Studio test or product modification.

## 2026-11-07 iPad Simulator Provider custody / source-oracle transfer

LogMate PR46 `aa4faeb4...` adds actual iPadOS26.1 Simulator Safari-tab Files Provider selection/B1/reopen, screen Review, Home/return expiry, eventual explicit Cancel and retry; independent original cache↔renamed Provider 13276-byte SHA and matching post-flow internal download show **synthetic memory-source serialized snapshot equality**. The new download's user-visible Files publication, persistent product ledger, installed PWA, owner/Generation and Activation remain OPEN; `.lbk` extension root cause is confounded. No Studio test or broader PASS. Canonical `research/data/D005_ipad_simulator_provider_custody_and_snapshot_oracle_2026-11-07.md`; S007 37-store deletion remains P0.

## 2026-11-07 W013 external-file integrity and File UX scope correction

Latest LogMate Draft PR46 `9da013466705e18cb23d27f5011fb2cc15bc3393` adds a **product-executed** host validation of a physical-iPad user-transferred synthetic LBK (13,276 bytes; independent SHA match to user-reported Expected SHA; full B1/37-store, temporary candidate reopen, exit 0) and user-reported actual Files Provider Cancel/Retry plus Review expiry. This **closes the specifically executed synthetic File UX round** but not W013 or production Restore. Native Simulator cancel/retry-open has bounded observed PASS; iPad Simulator selection remains unverified. Executable source is older `bd310585...`; latest PR HEAD is documentation, not a new tested build. Installed/offline managed EFB PWA, browser persistence, authenticated owner, Activation and S007 37-store deletion remain OPEN. Canonical Studio D005 note: `research/data/D005_w013_external_file_integrity_and_scoped_ux_closure_2026-11-07.md`. No new Studio runtime test or six-track gate change.

## 2026-11-07 physical iPad Safari B1 and Review evidence transfer

New LogMate Draft PR46 documentation head `0073619667944f760366e37cc3b38774cb44611d` (61 branches/12 open PRs; `1.0.0+1`) records physical iPad9/iPadOS18.6.2 Safari normal-tab **user-reported** synthetic B1/staging success, later re-selection B1, Review acknowledgement and disabled Activation. Frozen tested Web source is older `bd31058569e54f838a667c57865554aed1b3547e`; PR46 documentation-only HEAD is not an executed build. Earlier Safari external download/Files custody uncertainty remains OPEN; selecting an already saved synthetic file is not independent browser-export custody. Provider Cancel, installed/offline PWA, real Owner/Generation, Activation and S007 37-store A→B tests remain OPEN; no Studio tests, no product edits, no Stage-1 PASS. New D005 transfer: `research/data/D005_physical_ipad_safari_picker_review_evidence_transfer_2026-11-07.md`.

# Software Engineering Studio Global Status

## 2026-11-07 S007 live-open versus backup owner oracle disparity
No new LogMate PR/branch since #46 (61 branches/12 open Draft PRs); exact `sembast_logbook_repository.dart` blob remains `f2b8b0e...`. Fresh static comparison shows `_validateSyncState` on ordinary DB open checks only Sync State header, owner and Replica, whereas B1 `_validateLbkSyncEvidence` inspects seven Sync stores' owner references. Retained Sync State prevents `_ensureSyncState` from resetting binding/baseline status after terminal deletion. A→B file-backed full open, B1 rejection and remote data exposure are NOT EXECUTED/NOT PROVEN. S007 new distinct acceptance oracle documented in `research/systems/S007_live_open_vs_backup_owner_oracle_gap_2026-11-07.md`; Stage-1 gates unchanged.


## 2026-11-07 S007 new cross-owner Sync authority trace
Current LogMate inventory unchanged at 61 branches/12 open PRs, latest Draft #46 `472e3fa...`. At exact repository blob `f2b8b0e...`, deletion's 29-store wipe is followed by initialization that changes only `_syncStateStore.ownerUid`; subsequent new-UID bind likewise relabels owner without clearing prior Sync operational rows. The distinct risk is **retained A Sync metadata under B's owner field**, not merely a retained random Replica ID. This is a static proof obligation, **not an executed A→B flow or proven exploit**. See `research/systems/S007_post_deletion_rebind_sync_state_authority_trace_2026-11-07.md`; file-backed 37-store A-delete→B, phase-edge and stale-writer validation remains OPEN. All Stage-1 gates unchanged.


## 2026-11-07 new Draft PR46 evidence transfer

LogMate remote inventory now **61 branches / 12 open Draft PRs** (2026-11-07), new #46 `verify/w013-target-file-resume-20261107@472e3fa90c4e5f8c346aadc19d42f9e6ddd7ef24` stacked one commit on #45. **New positive evidence:** iPhone17 Simulator actual human-assisted OS file selection into app, full B1 and isolated staging/review, post-review Files saved-byte readback and current synthetic memory-source snapshot equality. **New unresolved boundary:** iPadOS Safari download-complete and internal SHA-matched bytes but Files user-visible destination empty, so external custody/repick/installed PWA not PASS. No product code or CI change in #46; W013 Activation still HOLD. S007 deletion 29/37-store static contradiction persists (same repository blob). Studio D005 analysis `research/data/D005_ios_safari_file_custody_evidence_ladder_2026-11-07.md`; no new Studio-run tests. Earlier 60/11 count below is historical as of prior audit.


## 2026-11-07 unmerged branch reconciliation — after earlier main-only audit

Fresh LogMate branch enumeration: **60 remote branches, 11 open Draft PRs**, including eight W013 PR #38–45. Current `main@f4bcd2f7...` is not representative of all ongoing engineering. Latest W013 product Draft `docs/w013-target-platform-validation-20261106@55a1ff894...` is **11 commits ahead** of main; independent W013 writer-fence probe `verify/w013-writer-fence-lease-20261105@cc600792...` is **16 ahead**. Owner-approved but unmerged Draft PR42 changes future policy to **Automatic + Manual bidirectional Delta Sync**, native conditional automatic Backup and fourth onboarding `Restore from backup file`; production Sync/Activation/automatic Backup remain unimplemented. Latest W013 branch source provides bounded isolated B1 staging/review, actual Chrome tests, iPhone Simulator Files save and independent B1 readback. PR43 exact-source CI four completed/success runs verified, but final submission heads and physical/release remain unvalidated. W013 remains IN PROGRESS, product branch Work count 7 COMPLETE/2 IN PROGRESS/28 NOT STARTED, compared with earlier main 7/1/29. Historic S007 deletion-integrity static risk remains OPEN; no broader PASS. Canonical new D005 audit `research/data/D005_logmate_w013_unmerged_branch_backup_restore_transfer_2026-11-07.md`. Review current branches/PRs, not only main, before next source audit.



## 2026-11-07 coordinator synthesis — latest product transfer priority
Current audited canonical Studio read `main@20aa7c582406c221096196c41f0101b37838fc46`; LogMate read-only `main@f4bcd2f7b7e77039e29653baa1cc93797673885b`, `pubspec 1.0.0+1`, production identity unknown. Product development advanced far beyond the 2026-09-24 snapshot below: Auth/runtime and local Sync v17 present; W-003 O18 local Home scope merged, 7 COMPLETE / 1 IN PROGRESS / 29 NOT STARTED. Manual Delta Sync product contract is approved, **production Sync/Import/Search/release acceptance OPEN**. F001 direct JIT/AOT and bounded Flutter runtime are already validated, so stale prompts must not reopen that blocker. Highest-leverage new **SOURCE-level CONTRADICTION** is S007 terminal deletion completeness/phase authority at current code: 29-drop wipe vs 37-store persisted registry, with old-writer, phase and cross-account file-backed probes **VALIDATION OPEN**; no actual product test run/incident and no Stage 1 PASS. Prior sections retain original historical evidence, not current product implementation claims. See `progress/INTEGRATED_ENGINEERING_REVIEW_2026-11-07.md` and `research/systems/S007_logmate_deletion_integrity_exact_ref_audit_2026-11-07.md`. Balance Loop next: one integrated Systems×Data×Quality deletion-integrity evidence block, then exact-product Manual Sync and backup/PWA custody, not six small studies. LogMate and peer repositories were not modified.


Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-24

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome + bounded macOS Safari runtime transfer; F006 bounded root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 governance + product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 Android Emulator; M002 process/file + HOME lifecycle; M003 permission/FGS + bounded Keystore replication; M006 Chromium PWA + macOS Safari runtime + bounded Safari SW registration/update/restart transfer + same-session origin-down offline |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q006 selected-pattern inventory + false-green repairs + hosted verdict-composition/reusable/matrix transfer evidence |
| Systems | Stage 1 IN STUDY — S004 product build provenance; S005 generic offline attestation; S007 account-required Auth/onboarding semantic models + latest LogMate Welcome product delta; exact-product runtime OPEN |

No specialist has passed Foundation.

## Meaningful new evidence
### S007 — LogMate product authority advanced beyond the prior transfer baseline
Latest audited product evidence is `yhappcom/logmate → main → 7551e1ca9e07df0b99e88aa03c8a56be03d8b2d3 → declared 1.0.0+1 → evidence date 2026-09-24`; production identity remains unknown. The cross-domain-reviewed Welcome implementation handoff now explicitly removes `Start a new logbook` from signed-out Welcome and fixes Apple/Google/Email as the three visible choices. Product copy is `Continue with Apple / Google / Email`, superseding the older Studio fixture copy `Sign in with ...` for LogMate implementation. This is product-documentation transfer, not runtime validation. Full auth/startup canonical synchronization, Flutter implementation, Firebase provider operation and native/PWA execution remain OPEN.

Canonical delta: `research/systems/S007_logmate_welcome_product_delta_2026-09-24.md`.

### Q006 — retained CI verdict-boundary evidence
Repository semantic CI work retains the exact-head selected-pattern inventory, repaired natural false-green, causal third-party action control with immutable pin, same-workflow semantic-output composition, reusable-workflow transfer and controlled matrix reusable-output aggregation. These bounded controls do not constitute production release-gate PASS; remaining natural classification, empty/skipped/redacted/cancelled paths, non-Bash/action-type transfer and production gate evidence remain OPEN.

### M006 / Q006 — retained Safari lifecycle transfer
Exact repaired head `54bbd5283920aa3d82057cc2da8a14b0db4bacbf`, run `35810765603`, retains bounded Safari registration/control/update/restart TRANSFER VALIDATION after the historical zero-byte false-green and two navigation-lifetime oracle defects. Fresh-WebDriver origin-down cold start remains a separate CONTRADICTION.

### S005 — retained generic offline attestation boundary
Generic fresh-attestation offline verification remains bounded PASS at exact repaired head `c1ca5a8ae09717fc794b7e064358938e346b56cb`, run `35826855911`. This does not resolve the older historical-subject availability contradiction and does not constitute exact-product release provenance.

## Current Balance Loop
S007 remains highest live LogMate leverage because product authority changed materially. The semantic Studio model is already deep enough; do not manufacture more synthetic Auth variants. Re-audit exact LogMate implementation after code lands and transfer the existing startup/onboarding/deletion/provider contracts into Dart/Flutter/Firebase/native/PWA evidence. Until implementation exists, Q006 or another materially independent Stage-1 gap may advance under the Balance Loop.

Do not regress to the stale F001 prompt blocker; direct Dart JIT/AOT and bounded Flutter Chrome/Safari runtime evidence already exist.

## CHANGE WATCH / OPEN
- S007 full LogMate auth/startup canonical synchronization and exact-product runtime/tests remain OPEN despite the newer Welcome handoff.
- S007 current product copy is `Continue with ...`; provider/platform presentation constraints remain CHANGE WATCH and override incompatible restyling.
- Firebase password-policy configuration and Google/Apple provider operational setup/cross-surface validation are OPEN.
- Q006 repository-wide semantic audit remains OPEN; selected-pattern inventory and bounded controls do not prove global semantic correctness.
- Q006 non-Bash/action-type and production release-gate transfer remain OPEN.
- M006 ordinary Safari relaunch/profile, installed PWA and fresh-SafariDriver origin-down cold-start mechanism remain OPEN.
- M003 physical Android/OEM/other API REPLICATION remains OPEN.
- Physical Android/iOS and canonical product runtime remain OPEN.
- System-initiated process pressure and physical power-loss/storage durability remain OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- S005 historical attestation availability cause remains OPEN; exact-product/release provenance remains OPEN.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading or workflow-green alone. Preserve exact claim/oracle/environment boundaries, subprocess verdict propagation, lifecycle-valid semantic oracles at every navigation boundary, and run-bound semantic evidence; never infer unexecuted evidence.

## 2026-11-08 — Android W013 independent Repository PID evidence

Unmerged LogMate `verify/w013-android-runtime-20261108` (reported executable `ce81418fe5c962b06e5cd42264ec3d2165794d3d`, declared `1.0.0+1`; branch HEAD not independently resolved) advances PR49's Android runtime gap: product reports API36 ARM64 synthetic emulator actual Repository A/B/C OS PIDs, pre-factory contention refusal, epoch2 Seal, stale facade rejection, fresh third-process persisted-state read. Product-reported bounded PASS, not Studio-run replication, CI or release. iOS independent Repository, physical, namespace/legacy fork and S007 all-store deletion remain OPEN; Supported Writer OPEN/BLOCKED and Restore HOLD. Systems canonical: `research/systems/S007_w013_android_independent_repository_pid_transfer_2026-11-08.md`. No Stage 1 PASS or product write.
