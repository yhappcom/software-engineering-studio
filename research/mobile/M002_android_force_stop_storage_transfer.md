# M002 — Android Force-Stop + App-Specific Storage Transfer

Date: 2026-09-20
Status: **IN STUDY — EXECUTION PENDING**

## Problem / Balance Loop selection
After M001 closed the bounded synthetic Android-emulator state-transition boundary, the highest-leverage independent Stage-1 gap is Android process death plus storage recovery. It directly crosses Mobile lifecycle/storage, Data durability semantics, Quality recovery oracles, and Systems runtime provenance without repeating the M001 counter fixture.

## SOURCE
Android's current Activity API documentation states that a background activity's process may be killed and later recreated. Android's app-specific storage documentation distinguishes an internal directory for persistent app files from cache storage and states that app-specific files are removed on uninstall. Checked 2026-09-20 from Android Developers primary documentation.

## CLAIM / TEST EVIDENCE CONTRACT
**CLAIM:** in a bounded Android Emulator fixture, a Flutter app can write a sentinel to Android app-specific persistent documents storage, have its process terminated with `adb shell am force-stop`, and after a fresh process launch recover the sentinel from storage rather than from process memory.

**SPEC/PROPERTY:** first launch with absent sentinel must expose `WROTE:persisted-v1`; force-stop must leave no process; relaunch must use a different PID and expose `RECOVERED:persisted-v1` from the previously written file.

**TARGET:** isolated Flutter Android app generated in CI with `path_provider`; debug APK installed on API 35 x86_64 Android Emulator.

**ORACLE:** UIAutomator XML independently observes the visible first-launch and recovered strings. `pidof` brackets force-stop and relaunch, requiring nonempty PID before, empty PID after force-stop, and a different nonempty PID after relaunch. Job success requires the complete sequence and natural step completion.

**ENVIRONMENT / REPRODUCTION DATA:** workflow `.github/workflows/m002-android-process-death-storage-validation.yml`; initial exact head `8f8e7b5bb4b1117e90bc0240abc93a665c36a789`; initial run `35513638513` queued at recording time. Workflow records Flutter/Dart identity and Android release/API/ABI.

**FAILURE MODEL:** toolchain/build, APK install, first process launch/write, UI oracle, force-stop/process disappearance, fresh process identity, persistent-file read, second UI oracle, and job completion are separate phases.

## ENGINEERING JUDGMENT
`force-stop` is a controlled process-termination boundary, not evidence that Android killed the process specifically for memory pressure. It is useful here because the claim is process-memory loss versus app-specific file recovery. It must not be relabeled as low-memory kill/background-policy validation.

The fixture uses `flush: true` before reporting `WROTE`, but a successful emulator file recovery does not prove physical-device power-loss durability, filesystem flush truthfulness, directory-entry durability, atomic multi-record transactions, SQLite behavior, backup/restore semantics, or production correctness.

## VALIDATION
Execution is pending. No PASS, TRANSFER VALIDATION, or runtime verdict is awarded until the workflow reaches terminal evidence and the phase-specific observations are checked.

## RELATED DOMAIN CHECK
- Foundations: F001/M001 Android execution boundary checked; this adds persistence + process replacement rather than another in-memory state transition.
- Architecture: persistence state is externally meaningful ownership; no architecture contract changed.
- Mobile: lead track; M002/M003 process-death and storage gaps are directly exercised.
- Data: D001/D005 distinguish memory, persistence, recovery and durability; this fixture proves only bounded file recovery after process termination.
- Quality: independent recovery oracle and process-identity checks are required; green build alone is insufficient.
- Systems: exact workflow/ref/toolchain/device identity is runtime provenance.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this bounded lifecycle/storage mechanism; no files edited.
- Product source: no MintTap/LogMate implementation audited; no product claim made.

## HANDOFFS
- Mobile → Data: if successful, treat as Android-emulator process-loss/file-recovery transfer only, not power-loss durability.
- Mobile → Quality: preserve write oracle, process disappearance, fresh PID, recovered-state oracle, and natural completion as distinct evidence phases.
- Mobile → Systems: retain exact workflow/ref/SDK/API/ABI provenance; emulator is not physical-device evidence.

## OPEN / CHANGE WATCH
- Terminal execution of run `35513638513`.
- Physical Android, low-memory/system-initiated process death, background restrictions and iOS lifecycle.
- SQLite/transactional persistence, permission revocation, storage-full/corruption, physical power loss and production/product transfer.
- Flutter stable, `path_provider`, Android emulator and runner behavior are version-sensitive.
