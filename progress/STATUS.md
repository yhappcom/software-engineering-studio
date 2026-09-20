# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-20  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome transfer; F002-F005 bounded direct execution; F006 bounded semantic/root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 executable governance + natural product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 host/Chrome + bounded Android Emulator transfer VALIDATED; M002 Android force-stop + app-specific storage recovery execution pending; M006 Chromium offline/restart/update/cold-start transfer |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 product-owned Flutter 3.38.7 baseline + lock + build-path transfer; hosted exact-ref source acquisition isolated as credential-context dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### M002 — Android force-stop + persistent-file recovery transfer started
Balance Loop selected Android process loss + storage recovery as the next materially stronger evidence class after M001's synthetic in-memory Android transfer. Android primary documentation distinguishes process recreation from app-specific persistent-file storage; the new fixture tests those boundaries together without claiming low-memory kill or physical durability.

Exact initial workflow head `8f8e7b5bb4b1117e90bc0240abc93a665c36a789`, run `35513638513` was queued at recording time. The oracle requires: first launch visibly reports `WROTE:persisted-v1`; process exists; `adb shell am force-stop` leaves no process; relaunch has a different PID; the fresh process visibly reports `RECOVERED:persisted-v1`; job completes naturally. No PASS/TRANSFER VALIDATION is awarded while execution is pending.

Canonical: `research/mobile/M002_android_force_stop_storage_transfer.md`.

## Retained evidence
M001 bounded Android-emulator state-transition transfer remains validated. F006 bounded regression chain remains closed. S004 source acquisition remains a credential-context dependency. Architecture, Data and Quality retained evidence is unchanged.

## HANDOFFS
- Mobile → Data: distinguish process-memory loss + file recovery from physical power-loss durability, transactional atomicity and backup semantics.
- Mobile → Quality: treat write, process disappearance, fresh PID, recovered-state oracle and natural completion as separate evidence phases.
- Mobile → Systems: preserve exact workflow/ref/toolchain/API/ABI provenance; controlled force-stop is not system low-memory kill evidence.
- Other repositories: no Design Studio, Web Manager, Marketing Manager or product canonical files edited.

## Current Balance Loop
Continue M002 until terminal evidence is recovered. If it fails, isolate build/install/first-launch/write/force-stop/PID/relaunch/recovery/job phase and repair only the isolated defect. Do not switch topics while this professional boundary is cheaply closable.

## CHANGE WATCH / OPEN
- M002 run `35513638513` terminal evidence is OPEN.
- Physical Android/iOS, Safari/iPadOS/EFB and canonical product runtime remain OPEN.
- System-initiated Android/iOS process death/background, storage-full/permissions and broader plugin-native behavior remain OPEN.
- F006 cross-platform/native/product networking transfer remains OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading alone. Preserve `failure → reproduction → isolation → causal hypothesis → falsification/check → root cause → fix → regression`, with exact runtime/ref identity and explicit evidence limits.
