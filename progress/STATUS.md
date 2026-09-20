# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-21

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome transfer; F006 bounded root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 governance + product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 Android Emulator VALIDATED; M002 force-stop/file recovery + HOME background/resume VALIDATED; M003 runtime permission grant/revoke VALIDATED; M006 Chromium lifecycle transfer |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 exact product baseline/lock/build-path transfer; hosted source acquisition remains credential-context dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### M002 — Android ordinary background/resume transfer validated
Exact Studio head `a278de3f2a9015195262b30662b1c240601f336e`, workflow run `35529237932`, job `106126775150` completed **success**. The job successfully completed the fail-fast `Execute Android background lifecycle oracle` step and natural job completion.

The pinned Flutter `3.47.5` fixture targets Android Emulator API 35 x86_64 and requires: initial live PID → HOME → same PID in background → foreground with same PID → Flutter visible lifecycle history containing `paused` and `resumed` → independent native Activity log containing `onPause`, `onStop`, and at least two `onResume` observations → natural completion. **TRANSFER VALIDATION PASS is awarded only for this bounded controlled HOME/background/resume path.**

**SOURCE/SYNTHESIS retained:** Android treats non-visible/cached processes as killable under pressure; Flutter documents that lifecycle notifications may be skipped on abrupt termination. Therefore successful callback delivery here does not make lifecycle callbacks guaranteed finalization/durability hooks or establish Android process-retention guarantees.

Canonical: `research/mobile/M002_android_background_lifecycle_transfer.md`.

## Retained evidence
M001/M002 force-stop/M003 remain validated; F006 regression chain remains closed; S004 source acquisition remains a credential-context dependency. Architecture, Data and Quality retained evidence is unchanged.

## HANDOFFS
- Mobile → Architecture/Data: controlled ordinary lifecycle delivery is now executable evidence, but durable truth still must not depend on `paused`/`onStop` or any assumed final callback.
- Mobile → Quality: Flutter state history, native callback log, PID continuity and natural completion are distinct evidence surfaces; system-initiated process loss remains a separate failure class.
- Mobile → Systems: background process survival/priority is platform-controlled; same-PID survival in this controlled HOME test is not a retention guarantee.
- Design Studio/Web Manager/Marketing Manager: considered; no external canonical files edited.

## Current Balance Loop
M002's controlled HOME/background/resume professional boundary is terminal-success and closed at its stated scope. Do not repeat equivalent HOME/force-stop variants. Re-rank the remaining gaps and prefer a materially different high-leverage class: physical Android/iOS/Safari, system-initiated process pressure, secure storage, user-driven permission behavior, canonical product runtime, physical storage/connectivity, or another track's stronger Stage-1 gap.

## CHANGE WATCH / OPEN
- Physical Android/iOS, Safari/iPadOS/EFB and canonical product runtime remain OPEN.
- System-initiated process death/background pressure, storage-full, user-driven/one-time/auto-reset permissions, secure storage and broader plugin-native behavior remain OPEN.
- Physical power-loss/storage durability remains OPEN; M002 force-stop must not be promoted to that claim.
- F006 cross-platform/native/product networking transfer remains OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading alone. Preserve exact claim/oracle/environment boundaries and never infer unexecuted evidence.
