# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-20  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome transfer; F002-F005 bounded direct execution; F006 semantic oracles PASS, accepted-socket liveness failure isolated, close-vs-destroy causal test pending |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 executable governance + natural product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 direct Flutter framework execution; M006 exact Chromium offline/restart/update-control/cold-start transfer; native/Safari/product runtime OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 product-owned Flutter 3.38.7 baseline + lock transfer; exact-ref source build acquisition remains a dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### F006 — accepted connected Socket is the minimal failing family
**VALIDATION:** exact head `75ba5067f8b173cc2ce8e7fdf7a7effb2e9dcefe`, run `35486660067` completed its four matrix jobs. `server-close` and `refused-connect` naturally exited. `accepted-close` and `truncated-eof` each reached `F006_AB_BODY_DONE` and then remained alive until the independent one-minute timeout; runner cleanup terminated the orphan Dart process.

**SYNTHESIS:** the common failure boundary is now creation of an accepted connected `Socket`; server bind/close alone and a refused connection alone do not reproduce the liveness failure.

**SOURCE / ENGINEERING JUDGMENT:** official Dart API documents `Socket.close()` as closing the IOSink/send side and `Socket.destroy()` as destroying both directions. This makes receive-side lifecycle retention a defensible causal hypothesis, not yet root cause.

**DEBUG:** fixture commit `18447ee486b24eade05a5e3478957bf5c804958c` adds structurally matched `accepted-destroy`; workflow head `d57d5531d9a5d96d21685d31e75bc2aaed051dd4` compares close vs destroy under the same environment. Terminal run evidence is pending. Root cause requires replicated close failure plus destroy natural exit before promotion.

Canonical: `research/foundations/F006_process_liveness_phase_isolation.md`.

## Retained cross-track evidence
Architecture, Mobile, Data, Quality and Systems evidence remains unchanged from the previous global status. The current Balance Loop intentionally stays on F006 because it is an unresolved foundational process/resource boundary with direct Quality/Systems leverage; stronger native/product evidence in other tracks remains blocked by platform/source dependencies.

## HANDOFFS
- Foundations → Quality/Systems: internal semantic PASS and BODY_DONE are insufficient executable-completion oracles; preserve natural process exit independently.
- Foundations → Architecture: send-side completion and bidirectional resource lifecycle are distinct contracts.
- Foundations → Mobile/Data: bounded Dart/Linux loopback evidence does not establish browser/mobile networking or durable application completion.
- Other repositories: Design Studio, Web Manager and Marketing Manager considered; no canonical files edited. No MintTap/LogMate behavior is claimed by this block.

## Current Balance Loop
Recover the close-vs-destroy workflow first. If `accepted-close` fails again and `accepted-destroy` exits, repair the combined semantic fixture with explicit bidirectional teardown and require semantic PASS + natural exit regression. If the discriminator does not separate outcomes, falsify/refine the hypothesis rather than changing topic or repeating blind cleanup permutations.

## CHANGE WATCH / OPEN
- F006 exact retained-resource root cause and combined natural-exit regression remain OPEN.
- F001 native/Safari/PWA/product/release runtime remains OPEN.
- Mobile native/Safari/iPadOS/EFB and canonical LogMate PWA runtime remain OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on authorized source acquisition.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading alone. Preserve `failure → reproduction → isolation → causal hypothesis → falsification/check → root cause → fix → regression`, with exact runtime/ref identity and explicit evidence limits.
