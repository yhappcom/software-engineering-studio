# S007 × W013 — Android independent Repository PID transfer and remaining adoption authority

**Evidence date:** 2026-11-08 Asia/Seoul. **Lead:** Systems S007; related Mobile/Data/Quality. **Classification:** SOURCE / PRODUCT-REPORTED VALIDATION / SYNTHESIS / ENGINEERING JUDGMENT / OPEN / DEPENDENCY / TRANSFER VALIDATION / CHANGE WATCH. No Studio-run product test or CI dispatch.

## Evidence identity and audit scope

- Studio predecessor: `yhappcom/software-engineering-studio → main@ba81e69848d6cb36cf9f3161c61c8d46f6eea158 → 2026-11-08`.
- Product default baseline: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → pubspec 1.0.0+1 → 2026-11-08`; **not** production identity.
- New product verification branch: `yhappcom/logmate → verify/w013-android-runtime-20261108 → reported exact final executable Source ce81418fe5c962b06e5cd42264ec3d2165794d3d → pubspec 1.0.0+1 → 2026-11-08`. Its remote branch HEAD SHA was **not independently resolved** this run; do not equate executable SHA with HEAD. Canonical [product evidence](https://github.com/yhappcom/logmate/blob/verify/w013-android-runtime-20261108/docs/evidence/w013-android-runtime-2026-11-08.md). Source is unmerged and is a verification branch, not a product adoption PR.
- Its stated base: PR49 `feat/w013-mobile-ownership-20261108@dd221883edcb01bc879be8fe0f1f1a33d353e477`, stacked on PR48 and PR47. Existing policy/docs and synthetic verification stacks remain distinct. Enumeration returned 65 branches and 15 open PRs (#49 through prior open items), not a new merge.
- Evidence is **read-only product-authored report**; machine JSON/log bytes and physical artifacts were not independently downloaded or executed by Studio. The report states final source/driver artifact and preservation audits; its source-bound PASS is not Studio replication or release acceptance.

## New failure/negative oracle and bounded positive result

The PR49 Android runtime gap is materially narrowed: the product team reports an **isolated Android 16 / API36 ARM64 emulator**, synthetic app `app.minttap.logmate.acceptance.w013ownership`, private fixture DB and three **real independent OS Repository PIDs** A=8104, B=8207, C=8321 (same app UID 10213). The old production AVD was not booted; a separately authorized temporary AVD was created and stopped after tests. Original PR49 APK first exposed a test-driver assumption that Android `Directory.systemTemp` resolved to `code_cache`, not `cache`; a second driver regex omitted underscore. Both initial failures and repairs are retained. These are harness defects, not demonstrated backend corruption.

Reported ordered oracle:
1. A owns the DB. B's attempted Open is rejected **before Sembast factory (0 calls)**; raw DB hash unchanged.
2. A commits the frozen Flight operation; retired-but-open ownership continues blocking B.
3. Actual A Close permits B to Open and seal epoch2.
4. A's stale facade rejects reuse of its original operation without new Operation ID or DB hash mutation.
5. Fresh independent C PID rejects Open while B owns DB; after B Close, C Opens and independently observes `sealed=true, epoch2, Record1/History1/Pending1` with expected namespace.

This is stronger than PR49's C↔Dart kernel FD interoperability because **both B and C are actual Dart/Sembast Repository actors**. It addresses the PR47 cached stale-writer overwrite counterexample **only for cooperating opt-in Android synthetic ownership**. The raw/Legacy uncooperative writer still can ignore advisory locking. Test probe `IsolatedWriterAuthority` protocol0 is not a production Guard/Generation.

At exact reported executable source `ce81418...`: product report lists format/analyze, focused 825 PASS/1 SKIP, full Flutter 1360 PASS/1 SKIP, Chrome 48 PASS, Web/Android/iOS builds, Android runtime seven process-interruption groups, independent Android Repository PIDs, and existing bounded iOS Simulator regression PASS. Counts overlap and are not additive. Artifact hash and machine reports are linked from the product evidence. **No new Studio execution, CI dispatch, physical Android, physical iOS, OS restart/power-loss or independent iOS Repository PID test.** Source-only report cannot independently prove artifact hashes or execution provenance without reading linked machine evidence.

## Gates, alternatives and outstanding authority

- **TRANSFER VALIDATION:** Android API36 ARM64 synthetic cooperating independent Repository A/B/C **bounded product-reported PASS**. This supersedes the prior `Android runtime NOT RUN` only for this new verification source; PR49's historical evidence remains correct for its own run.
- **OPEN:** independent iOS Repository A/B/C PID, physical devices, durable production namespace and app upgrade/downgrade data-fork handling, OS interruption/power loss, real release artifact. No production enrollment, Restore Activation remains HOLD, W013 overall Supported Writer OPEN/BLOCKED.
- **S007 OPEN:** 29 explicit terminal drops versus 37 persisted definitions, phase-edge admission and deletion-intent lock, full file-backed all-store wipe, old handle after deletion and owner A→B reopen. Android writer ownership cannot establish deletion erasure or Firebase UID authority.
- **PROJECT DECISION (unchanged):** owner-approved Automatic + Manual Delta Sync, conditional native automatic Backup and fourth Restore onboarding option remain approved-but-unmerged/not activated. D006 receipt/cursor/idempotency/convergence is OPEN.
- **ENGINEERING JUDGMENT / alternatives:** in-place advisory lock cannot force old binary; separate namespace isolates only cooperating new clients but creates migration and fork-reconciliation risks. Keep existing legacy data, IDs, Pending and History; no automatic move/merge/relabel or new production namespace without product approval.

## RELATED DOMAIN CHECK

Foundations: file locks, process vs Isolate, FD lifetime; F001 Dart/Flutter bounded execution exists. Architecture: admission before factory and actual Close; test-only Services must not become production authority. Mobile: emulator API36/ARM64 transfer, isolated Android Service processes; iOS independent Repository and physical devices OPEN. Data: immutable Flight Operation/History/Pending continuity and 37-store deletion; D006 authenticated Sync not inferred. Quality: independent third-process persisted-state oracle, negative rejection, source-bound artifacts, preserved failed drivers. Systems: old binaries, owner UID, deletion and release provenance. Design Studio: no new UI semantics. Web Manager: managed EFB PWA unaffected. Marketing Manager: no new production Sync/Restore claims. Product: read-only; no product Work or configuration touched.

## HANDOFFS

- **LogMate/Codex (approval required):** run the iOS independent Repository PID A/B/C oracle, then review stable namespace, existing `logmate_ledger.db`, Pending/History continuity, legacy downgrade forks and migration before any default enrollment. Preserve synthetic-only environment.
- **Systems × Data × Quality:** separately authorize and execute S007 file-backed 37-store owner A deletion→B reopen, invalid phase transitions, stale raw/cooperating writer, interrupted/dual driver and independent raw-store inspection; never use customer DB.
- **Mobile/Quality:** reproduce Android API36 with fresh independent evidence and eventually physical/OEM/OS-restart; compare final source SHA, APK hash, logs and artifacts. A green build or existing iOS simulator gate is not physical/release acceptance.

**CHANGE WATCH:** [Android Service process declaration](https://developer.android.com/guide/topics/manifest/service-element), [Android emulator invocation/data](https://developer.android.com/studio/run/emulator-commandline), [FlutterEngine embedding](https://api.flutter.dev/javadoc/io/flutter/embedding/engine/FlutterEngine.html). Pin SDK/ABI and artifact when transferring.
