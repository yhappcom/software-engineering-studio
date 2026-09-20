# M002 — Android Force-Stop + App-Specific Storage Transfer

Date: 2026-09-20
Status: **BOUNDED TRANSFER VALIDATED — FORCE-STOP + FRESH-PROCESS FILE RECOVERY**

## Problem / Balance Loop selection
After M001 closed the bounded synthetic Android-emulator state-transition boundary, the highest-leverage independent Stage-1 gap was Android process loss plus storage recovery. It crosses Mobile lifecycle/storage, Data persistence semantics, Quality recovery oracles, and Systems runtime provenance without repeating the M001 counter fixture.

## SOURCE
Android's current Activity documentation states that a background activity's process may be killed and later recreated. Android app-specific storage documentation distinguishes persistent app files from cache and states that app-specific files are removed on uninstall. Checked 2026-09-20 from Android Developers primary documentation.

## CLAIM / TEST EVIDENCE CONTRACT
**CLAIM:** in this bounded Android Emulator fixture, a Flutter app can write a sentinel to Android app-specific documents storage, lose its process through controlled `adb shell am force-stop`, and after a fresh process launch recover the sentinel from storage rather than process memory.

**SPEC/PROPERTY:** first launch with absent sentinel exposes `WROTE:persisted-v1`; force-stop leaves no process; relaunch has a different PID and exposes `RECOVERED:persisted-v1`.

**TARGET:** isolated Flutter Android app generated in CI with `path_provider`; debug APK installed on API 35 x86_64 Android Emulator.

**ORACLE:** UIAutomator XML independently observes the visible first-launch and recovered strings. `pidof` brackets force-stop and relaunch, requiring nonempty PID before, empty PID after force-stop, and a different nonempty PID after relaunch. The Bash oracle uses `set -euo pipefail`, so the action cannot complete successfully if any required grep/test fails.

**ENVIRONMENT / REPRODUCTION DATA:** workflow `.github/workflows/m002-android-process-death-storage-validation.yml`; repaired exact head `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20`; run `35516637659`; job `106093583857`; GitHub-hosted `ubuntu-latest`; API 35 x86_64 Android Emulator. The workflow records Flutter/Dart identity and Android release/API/ABI during execution; the terminal job evidence establishes successful execution of every named step but the connector-visible job metadata does not expose the captured version-log values, so those values are not fabricated here.

**FAILURE MODEL:** toolchain/build, APK install, first process launch/write, UI oracle, force-stop/process disappearance, fresh process identity, persistent-file read, second UI oracle, and job completion are distinct evidence phases.

## FAILURE → ISOLATION → REPAIR → REGRESSION
### Initial run `35513638513`
The initial exact head `8f8e7b5bb4b1117e90bc0240abc93a665c36a789` failed only in the combined emulator/oracle action after checkout, Flutter installation, toolchain recording, fixture creation/debug APK build and KVM setup succeeded.

**CAUSAL HYPOTHESIS:** the workflow repeated the command-lifetime mistake previously isolated in M001: PID shell variables were expected to survive across multiline action commands.

### Minimal repair
Commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20` changed execution plumbing only. It writes the complete stateful oracle to `$RUNNER_TEMP/m002_oracle.sh` and invokes it as one Bash process. App code, APK target, force-stop sequence, sentinel and UI/PID oracles remained unchanged.

### REGRESSION / ROOT CAUSE
Run `35516637659`, job `106093583857`, exact head `659c6e2...`, completed **success**. Every job step succeeded, including `Create isolated persistence fixture`, `Create stateful Android oracle script`, KVM setup, and `Execute force-stop and recovery oracle on Android emulator`; the job then completed naturally. Because the unchanged oracle is fail-fast and explicitly requires first-launch `WROTE`, nonempty pre-stop PID, empty post-stop PID, different nonempty relaunch PID, and recovered `RECOVERED` UI state, successful completion establishes the complete bounded oracle chain.

**ROOT CAUSE at the failed CI target:** the first workflow encoded stateful shell variables across command boundaries that did not preserve the assumed shell lifetime. Moving the unchanged oracle into one Bash process removed that infrastructure defect and the regression passed.

**TRANSFER VALIDATION — PASS, bounded:** the Studio now has Android-emulator evidence that app-specific persistent file state survives controlled process termination and is recovered by a fresh Flutter process under this fixture. This is materially stronger than M001's in-memory Android state transition.

## ENGINEERING JUDGMENT / EVIDENCE LIMIT
`force-stop` is a controlled process-termination boundary, not evidence that Android killed the process for memory pressure. The fixture uses `flush: true`, but successful emulator recovery does not prove physical-device power-loss durability, truthful filesystem flush, directory-entry durability, atomic multi-record transactions, SQLite semantics, backup/restore correctness, storage-full/corruption recovery, or production behavior.

It also does not establish iOS lifecycle behavior, system-initiated Android low-memory kill behavior, background-execution policy, release-mode behavior, or MintTap/LogMate behavior.

## RELATED DOMAIN CHECK
- Foundations: F001/M001 Android execution boundary checked; M002 adds persistence + process replacement.
- Architecture: persistence state is externally meaningful ownership; no architecture contract changed.
- Mobile: lead track; M002/M003 process-loss and storage boundary directly exercised.
- Data: D001/D005 distinguish memory, persistence, recovery and durability; this proves only bounded file recovery after controlled process termination.
- Quality: independent UI + PID recovery oracles and natural completion are retained; first failure and repaired regression preserve root-cause discipline.
- Systems: exact workflow/ref/API/ABI class and action shell boundary are execution provenance; emulator remains distinct from physical-device evidence.
- Design Studio / Web Manager / Marketing Manager: considered; not materially relevant to this bounded lifecycle/storage mechanism; no files edited.
- Product source: no MintTap/LogMate implementation audited; no product claim made.

## HANDOFFS
- Mobile → Data: Android-emulator process-loss/file-recovery transfer is now validated; physical power-loss and transactional durability remain separate.
- Mobile → Quality: retain write, process disappearance, fresh PID, recovered-state and natural completion as independent recovery evidence; CI command lifetime itself can invalidate an oracle.
- Mobile → Systems: shell/action execution semantics are part of pipeline provenance; preserve exact workflow/ref and do not equate emulator with physical-device evidence.

## OPEN / CHANGE WATCH
- Physical Android, system-initiated low-memory/process death, background restrictions and iOS lifecycle.
- SQLite/transactional persistence, permission revocation, storage-full/corruption, physical power loss and product/production transfer.
- Exact captured Flutter/Dart/Android version values should be retained from logs/artifacts when a connector-accessible evidence path exists; do not infer them from current stable labels.
- Flutter stable, `path_provider`, Android emulator, emulator-runner action and runner behavior are version-sensitive.
