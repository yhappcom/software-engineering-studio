# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-20  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome transfer; F002-F005 bounded direct execution; F006 bounded semantic/root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 executable governance + natural product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 host/Chrome + bounded Android Emulator transfer VALIDATED; M002 controlled Android force-stop + app-specific persistent-file recovery VALIDATED; M006 Chromium offline/restart/update/cold-start transfer |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 product-owned Flutter 3.38.7 baseline + lock + build-path transfer; hosted exact-ref source acquisition isolated as credential-context dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### M002 — bounded Android process-loss + persistent-file recovery TRANSFER VALIDATION PASS
Initial run `35513638513` failed in the combined emulator/oracle action. The failure was isolated to a CI command-state lifetime assumption, not to Android storage semantics. Repair commit `659c6e266dbcc4fe20e5b1b842ba73c2ab564f20` moved the unchanged stateful oracle into one Bash process.

Regression run `35516637659`, job `106093583857`, exact head `659c6e2...`, completed success. The fail-fast oracle requires first-launch `WROTE:persisted-v1`, an initial PID, no process after controlled `am force-stop`, a different fresh PID after relaunch, `RECOVERED:persisted-v1` from app-specific documents storage, and natural job completion. This closes the named Android-emulator force-stop/file-recovery professional boundary. It does not establish system low-memory kill, physical power-loss durability, iOS, product runtime or production behavior.

Canonical: `research/mobile/M002_android_force_stop_storage_transfer.md`.

## Retained evidence
M001 bounded Android-emulator state-transition transfer remains validated. F006 bounded regression chain remains closed. S004 source acquisition remains a credential-context dependency. Architecture, Data and Quality retained evidence is unchanged.

## HANDOFFS
- Mobile → Data: controlled process-memory loss + file recovery is validated on Android Emulator; physical power-loss durability, transactional atomicity and backup semantics remain distinct.
- Mobile → Quality: write, process disappearance, fresh PID, recovered-state oracle and natural completion remain separate evidence phases; command-shell lifetime is itself an oracle dependency.
- Mobile → Systems: preserve exact workflow/ref/API/ABI-class provenance; controlled force-stop is not system low-memory kill evidence.
- Other repositories: no Design Studio, Web Manager, Marketing Manager or product canonical files edited.

## Current Balance Loop
M002's bounded force-stop/file-recovery boundary is terminal; do not repeat equivalent sentinel variants. Re-rank the next independent block across tracks. Prefer system-initiated lifecycle/background behavior, permissions/storage-full, physical Android/iOS/Safari execution, canonical product artifact/runtime when authorization exists, physical storage/connectivity, natural ADR/release evidence, or another materially stronger Stage-1 gap.

## CHANGE WATCH / OPEN
- Physical Android/iOS, Safari/iPadOS/EFB and canonical product runtime remain OPEN.
- System-initiated Android/iOS process death/background, storage-full/permissions/secure storage and broader plugin-native behavior remain OPEN.
- Physical power-loss/storage durability remains OPEN; M002 file recovery must not be promoted to that claim.
- F006 cross-platform/native/product networking transfer remains OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading alone. Preserve `failure → reproduction → isolation → causal hypothesis → falsification/check → root cause → fix → regression`, with exact runtime/ref identity and explicit evidence limits.
