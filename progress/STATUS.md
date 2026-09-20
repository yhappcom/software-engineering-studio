# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-21

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome transfer; F006 bounded root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 governance + product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 Android Emulator VALIDATED; M002 force-stop/file recovery VALIDATED + background/resume transfer PENDING; M003 runtime permission grant/revoke VALIDATED; M006 Chromium lifecycle transfer |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 exact product baseline/lock/build-path transfer; hosted source acquisition remains credential-context dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### M002 — Android ordinary background/resume transfer started
Balance Loop selected ordinary Android foreground→HOME/background→foreground lifecycle as the next materially different evidence class. This is not another force-stop/storage variant: it tests callback/state propagation while the process remains alive and separates Flutter lifecycle observation from native Activity callbacks.

Initial exact Studio head `a278de3f2a9015195262b30662b1c240601f336e`, workflow run `35529237932` is in progress. The fixture pins Flutter `3.47.5`, targets API-35 x86_64 emulator, and requires same PID across HOME/background/resume, Flutter UI history containing paused/resumed, native `onPause`/`onStop` and a second `onResume`, then natural completion. **No PASS/TRANSFER VALIDATION yet.** Canonical: `research/mobile/M002_android_background_lifecycle_transfer.md`.

**SOURCE/SYNTHESIS:** Android treats non-visible/cached processes as killable under pressure; Flutter documents that lifecycle notifications may be skipped on abrupt termination. Therefore lifecycle callbacks are coordination signals, not guaranteed finalization/durability hooks.

## Retained evidence
M001/M002 force-stop/M003 remain validated; F006 regression chain remains closed; S004 source acquisition remains a credential-context dependency. Architecture, Data and Quality retained evidence is unchanged.

## HANDOFFS
- Mobile → Architecture/Data: do not make durable truth depend on `paused`/`onStop` or any assumed final callback.
- Mobile → Quality: distinguish Flutter state history, native callback log, PID continuity and natural completion as separate evidence surfaces.
- Mobile → Systems: background process survival/priority is platform-controlled; same-PID survival in a controlled HOME test is not a retention guarantee.
- Design Studio/Web Manager/Marketing Manager: considered; no external canonical files edited.

## Current Balance Loop
Continue M002 run `35529237932` to terminal evidence. Do not switch topics while this professional boundary is unresolved. A success closes only controlled HOME background/resume on the named emulator; a failure must be isolated by build/emulator/PID/native-callback/Flutter-state/oracle phase before semantic changes.

## CHANGE WATCH / OPEN
- M002 run `35529237932` terminal verdict is OPEN.
- Physical Android/iOS, Safari/iPadOS/EFB and canonical product runtime remain OPEN.
- System-initiated process death/background pressure, storage-full, user-driven/one-time/auto-reset permissions, secure storage and broader plugin-native behavior remain OPEN.
- Physical power-loss/storage durability remains OPEN; M002 force-stop must not be promoted to that claim.
- F006 cross-platform/native/product networking transfer remains OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading alone. Preserve exact claim/oracle/environment boundaries and never infer unexecuted evidence.
