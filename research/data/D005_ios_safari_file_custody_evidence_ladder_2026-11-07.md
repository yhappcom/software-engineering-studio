# D005 — iOS Native File Review versus iPadOS Safari Download Custody: Evidence-Ladder Transfer

**Date:** 2026-11-07 (KST). **Lead:** Data, Persistence & Distributed Systems (D005). **Support:** Mobile M006, Quality Q006, Systems S007, Architecture A003. **State:** SOURCE / SYNTHESIS / ENGINEERING JUDGMENT / OPEN. No new app, device, test, CI, or Studio fixture was executed in this Studio cycle.

## Question and high-information-gain delta

The 2026-11-06 W013 review left native iOS OS Picker→in-app B1 validation and Safari actual download/save handoff OPEN. On 2026-11-07 a new **Draft PR #46** advanced the first boundary but sharpened the second. This is a change in actual evidence level, not a change in product contract or release status.

- Product: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b`; unmerged Draft chain `#42→#43→#44→#45→#46`; PR #45 base `docs/w013-target-platform-validation-20261106@55a1ff894fcaa9e66765fcfe690c576dda61df98`; **PR #46 head** `verify/w013-target-file-resume-20261107@472e3fa90c4e5f8c346aadc19d42f9e6ddd7ef24`; declared `pubspec.yaml 1.0.0+1`; evidence 2026-11-07. PR #46 is **one commit ahead of PR #45, zero behind**, with evidence and W013 checklist changes only. All PRs are Draft/Open/unmerged, not production.
- **Installed iOS app** is separately pinned to PR #44 `f484e0824c809fb7e8267bfb90bf8391bc534cb7`, with 254 installed bundle hashes checked. **Web and APK build** source `4d333dd275c04332de6a0892cd3653d88184647c`. Product/test/plugin/permission/platform trees unchanged; no new full test/CI/build PASS from PR #46. Do not attribute the installed app to the PR #46 commit.
- Canonical actual-run evidence: `docs/evidence/w013-target-platform-resume-2026-11-07.md`, `observations.json`, `iphone-after-review-export-files.json`, `ipad-downloaded-bytes-final.json`, and screenshots under `docs/evidence/w013-target-platform-resume-2026-11-07/` at the exact PR #46 SHA.

## SOURCE / bounded iPhone validation: stronger than previous CLI-only claim

Actual iPhone17 / iOS26.1 Simulator, isolated memory-backed synthetic Owner and one Flight, no Firebase or active persistent product DB:

1. Previous Files-saved LBK remained present **13276 bytes**, SHA-256 `dddc173859b013e0d379b02c90af49d5d9cac97048cdfe6fa810e8455145a2f8`.
2. Native file selection via human-assisted OS Picker succeeded after automation input failed; app independently displayed **File read Completed → Decode Completed → Full B1 Passed → Temporary staging reopen Passed** and compatible format2. The candidate remained private/locked and was disposed. This is **in-app path execution**, distinct from PR #45's CLI validation of saved bytes.
3. Cancel outcome, retry, review acknowledgement, and **disabled Activate** were observed. Acknowledgement was screen-only, not durable consent.
4. A new actual local Files save **after Review** produced independently reread provider bytes **13276 bytes**, SHA-256 `6b704b7429742e1b8cd5f135f8319370b87f11c6299d6ab638e9fdd7e73e3df8`, matching the live memory-source pre-flow B1 snapshot hash. The old LBK remained. This is a **before/after serialized-source invariant**, not a persistent database or crash/power-loss durability oracle.
5. The old selected file and new saved post-review file have different hashes because the harness cold launch uses new synthetic operation identities. Do **not** demand old-file hash = new-file hash or misinterpret the difference as corruption. The correct invariant is **current pre-flow snapshot = current post-flow snapshot** and independent old-file integrity.

**Classification:** Native Simulator OS Save + readback and in-app OS Open/B1/staging/review **TRANSFER VALIDATION** at a pinned synthetic artifact. No Activation, real UID, Generation, user database, physical iPhone or release PASS.

## SOURCE / Safari iPadOS: bytes complete is not accessible custody

Same iPadOS26.1 Simulator Safari tab at loopback `http://127.0.0.1:18763/`, memory-only file Harness with no owned worker. Human initiated downloads. Safari live accessibility tree reported 13KB item `complete=true, progress=1.0`; independently inspected two internal `Library/Safari/Downloads/<UUID>/` artifacts, **13276 bytes** each, SHA-256 `c736accba3092b70fa48c76300609e0ff8fc763193568edbb58e41761874c921`, equal to current synthetic B1 source. But Files **On My iPad** was observed empty. No user-accessible Files destination, app repick, Web B1/staging/Review or installed-PWA/offline acceptance. The plugin's pinned Web adapter triggers a Blob/anchor download and returns null; `lib/presentation/backup_file_picker_access.dart` correctly returns **downloadRequested** on Web. Internal Safari downloads are not a durable user-designated backup destination oracle. Root cause of missing Files visibility remains **UNRESOLVED**, not proven Simulator, Safari, plugin, or app defect.

**Critical distinction:** `B0=bytes generated`; `B1=browser reports download complete`; `B2=internal browser artifact bytes match`; `B3=user can locate and retain an accessible file in Files/provider`; `B4=user can repick file into app and B1-validate it`; `B5=isolated candidate reopen and source preservation`; `B6=separate authorized Activation/Owner/Generation/writer fence`; `B7=persistent product/device/release acceptance`. Safari currently establishes **B0–B2 only**. iPhone synthetic Native establishes **B0–B5** with limited OS and memory-source scope. Do not collapse these rungs into `Saved` or `Restore works`.

## Falsifiable next validation matrix (not executed here)

| Boundary | Independent oracle | Failure-first/negative controls | Stop condition |
| --- | --- | --- | --- |
| iPad Safari Files custody | Human finds the downloaded LBK in user-accessible Files location; record exact destination/provider, size/hash, app-independent reopening after Safari/tab close | cancel/share interruption; download-list complete but Files absent; stale Downloads entry; offline local Files vs cloud-only provider | Internal browser cache alone never passes B3 |
| Safari repick/isolated staging | OS Files selection returns actual file bytes to app; exact B1 digest/Owner/registry/format validation and separate IndexedDB candidate close/reopen | wrong UID, truncated/modified LBK, no provider permission, cancelled picker, session change mid-await | No active ledger replacement; B4/B5 independent from B3 |
| Native source preservation | Persistent file-backed synthetic ledger with pre/post snapshots, close/reopen, killed process between read/review/export; new independent user-owned Files backup readback | changed source while dialog pending; deletion lock; old file retained after new save failure | Memory-only snapshot equality cannot pass persistent-source gate |
| Installed EFB PWA | Controlled worker, origin/cache identity, persistent IndexedDB/Owner, Home Screen/managed Web Clip entry, offline cold reopen, saved external file repick | browser-tab vs installed context, worker update, origin unavailable, provider permission revoked | Safari tab/loopback/no-worker evidence never upgrades installed EFB gate |
| Android Native | Dedicated verified synthetic-only AVD/package, actual SAF save/read/reselect/B1/reopen and negative provider cases | existing base AVD contains production package; must not boot/overwrite/reset without isolation | APK compile/package identity is not Android file acceptance |
| Production Activation | independent authenticated Owner/Generation/coverage oracle, complete writer fence (including old/raw handle), idempotent receipt, crash-safe old/new namespace, post-activation Flight reopen | bypassing writer, concurrent sessions, interrupted commit, stale Generation, wrong owner, downgrade/old binary | Remains HOLD/NOT AUTHORIZED, irrespective of B0–B5 |

## Engineering judgment: acceptance architecture and alternatives

- **Option A: keep browser download-request semantics** until B3/B4 is actually measured on supported iPad Safari/managed EFB. This is the current safe classification and avoids falsely promising file custody.
- **Option B: user-directed share/export to a Files provider** may improve B3 discoverability, but requires explicit product approval and supported iPadOS API/MDM validation. A new plugin, Files copy, private cache transfer, or simulator filesystem injection cannot be called a repair without reproducing the cause and validating user-visible custody.
- **Option C: automatic cloud/server backup** is **not** the approved PWA V1 policy and cannot be silently substituted for missing B3. Native conditional automatic backup remains a separate future implementation.

A file hash proves identity of observed bytes at the observation time, not user custody, durability across app removal, ownership, credential authority, or recovery activation. The independent oracles should use distinct names/status types (`DownloadRequested`, `BrowserInternalComplete`, `ProviderSavedReadback`, `CandidateValidated`, `ActivationAccepted`) rather than a single `success` boolean.

## RELATED DOMAIN CHECK

- **Foundations F005/F006:** asynchronous OS picker and browser download completion are different state machines; no implication from a returned future to provider custody.
- **Architecture A003/A006:** strengthen contracts with evidence-specific outcomes; do not make current file adapter promise stronger than its API.
- **Mobile M002/M006:** iOS Simulator vs physical, Safari tab vs installed PWA, process death and MDM storage restrictions are independent axes.
- **Data D005/D006:** isolated B1 candidate does not establish sync Generation/Owner/remote coverage or durable backup file retention.
- **Quality Q004/Q006:** hash/source invariant is valid only for matching same-run pre/post snapshots; require fault injection and negative file/UID/provider cases.
- **Systems S007:** account deletion, owner reauth and complete 37-store terminal erasure remain separate P0. Exact `sembast_logbook_repository.dart` blob `f2b8b0eb681f5d960532dac5c87b29cf85a459b8` remains unchanged on PR #46; do not upgrade S007.
- **Design Studio:** distinguish `Download requested` and `File saved` copy and disabled Activation; UI review is not durable consent.
- **Web Manager:** managed EFB/browser worker/storage/origin and Files user journey need their own evidence; no edits.
- **Marketing:** no user-facing promise of completed PWA backup, production Restore or release support.
- **LogMate:** product ref read-only; Work37 remains 7 COMPLETE/2 IN PROGRESS/28 NOT STARTED in PR #46; W013 IN PROGRESS, Activation HOLD.

## HANDOFFS / OPEN / CHANGE WATCH

**TO LogMate/Codex (advisory only):** retain #46's actual iPhone Picker→B1→Review validation as bounded evidence. Next independent high-value run should prioritize user-visible iPad Safari Files custody B3, then app repick B4/B5, with a known synthetic-only device and human-assisted provider comparison. Do not modify PR #46 or install an unapproved adapter to manufacture PASS. For Android isolate the synthetic AVD before any app install. Keep S007 terminal deletion file-backed 37-store canary regression as distinct P0 release gate.

**OPEN:** actual iPad user Files destination, provider retention, Web B1/IndexedDB, installed/offline EFB, physical iOS/Android, persistent source invariance, Activation and old writer fencing. **CHANGE WATCH:** iOS/iPadOS Safari download locations, Files provider UX, plugin version, EFB MDM/Web Clip and OS updates require exact release-time verification; no official platform guarantee is inferred solely from a simulator.

**Studio execution:** GitHub exact-source reads/compare only. No Studio-run Dart/Flutter/device/CI tests, no new product issue, PR, Work or configuration. Stage 1 remains NOT PASS.
