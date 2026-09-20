# M002 — Android Force-Stop + App-Specific Storage Transfer

Date: 2026-09-20
Status: **IN STUDY — FIRST EXECUTION FAILED; COMMAND-STATE REPAIR PENDING**

## Problem / Balance Loop selection
After M001 closed the bounded synthetic Android-emulator state-transition boundary, the highest-leverage independent Stage-1 gap is Android process death plus storage recovery. It directly crosses Mobile lifecycle/storage, Data durability semantics, Quality recovery oracles, and Systems runtime provenance without repeating the M001 counter fixture.

## SOURCE
Android's current Activity API documentation states that a background activity's process may be killed and later recreated. Android's app-specific storage documentation distinguishes an internal directory for persistent app files from cache storage and states that app-specific files are removed on uninstall. Checked 2026-09-20 from Android Developers primary documentation.

## CLAIM / TEST EVIDENCE CONTRACT
**CLAIM:** in a bounded Android Emulator fixture, a Flutter app can write a sentinel to Android app-specific persistent documents storage, have its process terminated with `adb shell am force-stop`, and after a fresh process launch recover the sentinel from storage rather than from process memory.

**SPEC/PROPERTY:** first launch with absent sentinel must expose `WROTE:persisted-v1`; force-stop must leave no process; relaunch must use a different PID and expose `RECOVERED:persisted-v1` from the previously written file.

**TARGET:** isolated Flutter Android app generated in CI with `path_provider`; debug APK installed on API 35 x86_64 Android Emulator.

**ORACLE:** UIAutomator XML independently observes the visible first-launch and recovered strings. `pidof` brackets force-stop and relaunch, requiring nonempty PID before, empty PID after force-stop, and a different nonempty PID after relaunch. Job success requires the complete sequence and natural step completion.

**ENVIRONMENT / REPRODUCTION DATA:** workflow `.github/workflows/m002-android-process-death-storage-validation.yml`; initial exact head `8f8e7b5bb4b1117e90bc0240abc93a665c36a789`; run `35513638513`, job `106085779672`. Repair commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20` moves the stateful oracle into one Bash process; repair execution is pending at recording time. Workflow records Flutter/Dart identity and Android release/API/ABI when execution reaches the oracle.

**FAILURE MODEL:** toolchain/build, APK install, first process launch/write, UI oracle, force-stop/process disappearance, fresh process identity, persistent-file read, second UI oracle, and job completion are separate phases.

## FAILURE / ISOLATION — run 35513638513
**OBSERVATION:** the run completed `failure`. Checkout, Flutter installation, toolchain recording, isolated fixture creation (including debug APK build), and KVM setup all completed successfully. The sole failing phase was `Execute force-stop and recovery oracle on Android emulator`; the job itself then completed cleanup normally.

**CONTRADICTION:** this is not evidence of a Flutter compile failure, fixture-generation failure, or KVM-setup failure. It also does not yet establish that storage recovery failed because the failing action groups multiple Android/oracle operations.

**CAUSAL HYPOTHESIS:** the initial workflow repeated the command-lifetime mistake already isolated in M001. `reactivecircus/android-emulator-runner` receives a multiline `script`, while the oracle stores `PID_BEFORE` and `PID_AFTER` in shell variables that must survive across later commands. M001 established that these action script lines do not provide the assumed persistent shell state. Therefore the first M002 script contains a known-invalid state-lifetime assumption independent of Android storage semantics.

**FIX UNDER VALIDATION:** commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20` changes only execution plumbing: it writes the complete oracle to `$RUNNER_TEMP/m002_oracle.sh` and gives the emulator runner a single command, `bash "$RUNNER_TEMP/m002_oracle.sh"`. PID variables and `set -euo pipefail` now live in one Bash process. App code, APK target, force-stop sequence, persistence sentinel and UI/PID oracles are unchanged.

**VERDICT:** infrastructure/oracle-command defect isolated strongly enough to justify the minimal repair, but **ROOT CAUSE and Android storage TRANSFER VALIDATION remain pending regression**. Do not claim that the application reached or failed the recovery oracle from job metadata alone.

## ENGINEERING JUDGMENT
`force-stop` is a controlled process-termination boundary, not evidence that Android killed the process specifically for memory pressure. It is useful here because the claim is process-memory loss versus app-specific file recovery. It must not be relabeled as low-memory kill/background-policy validation.

The fixture uses `flush: true` before reporting `WROTE`, but a successful emulator file recovery does not prove physical-device power-loss durability, filesystem flush truthfulness, directory-entry durability, atomic multi-record transactions, SQLite behavior, backup/restore semantics, or production correctness.

## VALIDATION
Repair execution is pending. No PASS or TRANSFER VALIDATION is awarded until a terminal repair run demonstrates APK install, first write/UI oracle, process existence, force-stop disappearance, fresh PID, recovered-file UI oracle and natural completion.

## RELATED DOMAIN CHECK
- Foundations: F001/M001 Android execution boundary checked; this adds persistence + process replacement rather than another in-memory state transition.
- Architecture: persistence state is externally meaningful ownership; no architecture contract changed.
- Mobile: lead track; M002/M003 process-death and storage gaps are directly exercised.
- Data: D001/D005 distinguish memory, persistence, recovery and durability; this fixture proves only bounded file recovery after process termination.
- Quality: independent recovery oracle and process-identity checks are required; green build alone is insufficient. First failure reinforces phase-specific verdict discipline.
- Systems: exact workflow/ref/toolchain/device identity is runtime provenance; action command-shell semantics are part of executable-pipeline provenance.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this bounded lifecycle/storage mechanism; no files edited.
- Product source: no MintTap/LogMate implementation audited; no product claim made.

## HANDOFFS
- Mobile → Data: if successful, treat as Android-emulator process-loss/file-recovery transfer only, not power-loss durability.
- Mobile → Quality: preserve write oracle, process disappearance, fresh PID, recovered-state oracle, and natural completion as distinct evidence phases; do not collapse action failure into application failure.
- Mobile → Systems: retain exact workflow/ref/SDK/API/ABI provenance and action shell/command-boundary behavior; emulator is not physical-device evidence.

## OPEN / CHANGE WATCH
- Terminal regression evidence after repair commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20`.
- Physical Android, low-memory/system-initiated process death, background restrictions and iOS lifecycle.
- SQLite/transactional persistence, permission revocation, storage-full/corruption, physical power loss and production/product transfer.
- Flutter stable, `path_provider`, Android emulator, emulator-runner action and runner behavior are version-sensitive.
