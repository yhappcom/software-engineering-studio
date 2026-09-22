# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-23

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome + bounded macOS Safari runtime transfer; F006 bounded root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 governance + product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 Android Emulator; M002 process/file + HOME lifecycle; M003 permission/FGS causal transfers + bounded Keystore replication; M006 Chromium PWA lifecycle + macOS Safari runtime/SW lifecycle + bounded same-session origin-down offline transfer |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 exact product baseline/lock/build-path transfer; hosted source acquisition remains credential-context dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### M006 — Safari origin-down offline discriminator
Exact head `91c5374bc7f09c6103c7f216bd7bf1146b78f40d`, workflow run `35780706023`, terminal failure. Run-bound artifact `10718495328`, digest `sha256:ec95755ab0c98a8b9e8f6ead62bc3d190c3edeedd6e4b0a0f78b6e7d2113c563`, was downloaded and inspected. Environment artifact records macOS 15.7.9 build 24G830 and Safari/safaridriver 26.6.1.

Online execution/control passed, CacheStorage precondition was true, and an independent probe established `origin-down=true`. With the same surviving Safari WebDriver session, navigation to the unavailable origin reached `M006_APP_READY` and retained a non-null Service Worker controller. After quitting/recreating Safari WebDriver, the same navigation repeatedly returned `Failed to open page` until timeout.

**VALIDATION:** bounded same-session macOS Safari origin-down offline fetch/cache/app-shell execution. **CONTRADICTION:** fresh-WebDriver cold-start expectation. The lower-level SafariDriver/WebKit implementation ROOT CAUSE remains OPEN; WebDriver session recreation is not equated with ordinary Safari relaunch/profile or installed PWA restart.

## Retained evidence
M001, both bounded M002 transfers, M003 permission/FGS/Keystore evidence, M006 Chromium PWA lifecycle/Safari generic runtime/Safari SW lifecycle, F006 regression closure, Data/Quality executable boundaries and S004 authorization dependency remain unchanged.

## Current Balance Loop
The Safari same-session/fresh-WebDriver discriminator has reached its useful bounded boundary. Do not repeat equivalent session-recreation variants. Re-rank toward materially stronger evidence classes: ordinary browser/profile relaunch only if a trustworthy mechanism exists, physical/native Android/iOS/iPadOS/EFB, exact-product authorized PWA build/runtime, physical storage/connectivity/publication durability, natural release/ADR evidence, or another stronger Stage-1 prerequisite gap.

F001 direct Dart/Flutter is not the historical blocker stated in older prompts: direct Dart JIT/AOT, Flutter framework/test binding, host→Chrome and bounded macOS Safari runtime evidence exist. Native Android/iOS/iPadOS, product and release transfer remain OPEN.

## CHANGE WATCH / OPEN
- M003 transfers remain bounded to exact API-35 emulator fixtures; independent physical Android/OEM/other API REPLICATION remains OPEN.
- M006 same-session macOS Safari origin-down offline behavior is bounded to the Studio fixture; ordinary Safari relaunch/profile persistence, installed PWA and iOS/iPadOS/EFB remain OPEN.
- Physical Android/iOS and canonical product runtime remain OPEN.
- System-initiated process pressure and physical power-loss/storage durability remain OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading alone. Preserve exact claim/oracle/environment boundaries and never infer unexecuted evidence.
