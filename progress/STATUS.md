# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-20  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome transfer; F002-F005 bounded direct execution; F006 semantic PASS + bounded socket-liveness root cause, repaired combined regression pending |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 executable governance + natural product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 direct Flutter framework execution; M006 exact Chromium offline/restart/update-control/cold-start transfer; native/Safari/product runtime OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 product-owned Flutter 3.38.7 baseline + lock transfer; exact-ref source build acquisition remains a dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### F006 — send-side close vs bidirectional teardown causally separated
**VALIDATION / DEBUG:** exact head `d57d5531d9a5d96d21685d31e75bc2aaed051dd4`, run `35489259464`, Dart 3.13.3/linux_x64, Ubuntu 24.04.5. `accepted-close` replicated BODY_DONE followed by timeout/orphan termination; structurally matched `accepted-destroy` reached BODY_DONE and naturally exited. `server-close` and `refused-connect` controls exited; `truncated-eof` retained the close-path failure.

**ROOT CAUSE at this bounded target:** the fixture treated completion of `Socket.close()`'s send-side IOSink contract as complete connected-socket teardown. The receive side could retain process liveness. Explicit bidirectional `destroy()` removed the symptom in the matched accepted-socket case. This is not a universal claim that `Socket.close()` leaks.

**FIX:** commit `5aa89aa5c11c4baf68233a412566e891a855506a` changes the combined semantic fixture to flush its intentionally truncated payload and then destroy the client. **VALIDATION remains OPEN:** semantic PASS and natural process exit must both succeed in the repaired combined fixture before F006 is closed.

Canonical: `research/foundations/F006_process_liveness_phase_isolation.md`.

## Retained cross-track evidence
Architecture, Mobile, Data, Quality and Systems evidence remains unchanged. Balance Loop remains on F006 until the repaired combined regression is terminal or genuinely blocked; this is a foundational resource-lifecycle boundary with direct Quality/Systems leverage.

## HANDOFFS
- Foundations → Quality/Systems: internal semantic PASS/BODY_DONE is insufficient executable-completion evidence; preserve natural process exit/resource lifecycle independently.
- Foundations → Architecture: API completion must be interpreted at its documented contract boundary; send-side completion is not bidirectional teardown.
- Foundations → Mobile/Data: bounded Dart/Linux loopback evidence does not establish browser/mobile networking or durable application completion.
- Other repositories: Design Studio, Web Manager and Marketing Manager considered; no canonical files edited. No MintTap/LogMate behavior is claimed.

## Current Balance Loop
Recover/execute the repaired combined F006 fixture at or after `5aa89aa5...`. Require truncated-EOF rejection, refused-connect observation and natural process exit. If successful, close this bounded F006 professional boundary and move to the next highest-value independent evidence class rather than repeating teardown variants.

## CHANGE WATCH / OPEN
- F006 repaired combined semantic + natural-exit regression remains OPEN.
- F001 native/Safari/PWA/product/release runtime remains OPEN.
- Mobile native/Safari/iPadOS/EFB and canonical LogMate PWA runtime remain OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on authorized source acquisition.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading alone. Preserve `failure → reproduction → isolation → causal hypothesis → falsification/check → root cause → fix → regression`, with exact runtime/ref identity and explicit evidence limits.
