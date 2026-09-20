# Foundations Specialist Status

Track: Computer Science & Programming Foundations
Prefix: `F###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-20

## Active evidence

### F001 — Program Execution Foundations
**IN STUDY — DIRECT DART JIT/AOT + FLUTTER HOST→CHROME RUNTIME TRANSFER VALIDATED.** Run `35423963687` validates Dart JIT/AOT compile+execute; run `35426881450` validates Flutter framework/test binding; exact head `b547c5d564731521eaf49380492fd10b5a980df9`, run `35478966848`, job `105993130270` validates the same bounded widget oracle on host and Chrome. Native/Safari/PWA/product/release transfer remains OPEN.

### F002–F005
Bounded direct Dart/Flutter execution retained: identity/resource lifetime (F002), representation/queue semantics (F003), isolate ownership/sendability (F004), and async ordering/cancellation boundaries (F005). Their previously recorded platform/product/GC/performance/backpressure gaps remain OPEN.

### F006 — OS, file, socket and network foundations
**IN STUDY — TRANSPORT SEMANTICS PASS; ACCEPTED SOCKET LIVENESS FAILURE ISOLATED; CLOSE-vs-DESTROY CAUSAL TEST PENDING.** Canonical: `research/foundations/F006_direct_dart_socket_transfer.md`, `research/foundations/F006_process_liveness_phase_isolation.md`.

Run `35486660067`, exact head `75ba5067f8b173cc2ce8e7fdf7a7effb2e9dcefe`, completed the four-way isolation: `server-close` and `refused-connect` naturally exited; `accepted-close` and `truncated-eof` each emitted their BODY_DONE marker and then timed out, with runner cleanup terminating the orphan Dart process. The common boundary is creation of an accepted connected `Socket`, not server bind/close or refused connect alone.

Official Dart API distinguishes `Socket.close()` as closing the IOSink/send side from `Socket.destroy()` as destroying both directions. This supports a new causal hypothesis that send-side close leaves receive-side lifecycle capable of retaining process liveness. It is not yet ROOT CAUSE.

Fixture commit `18447ee486b24eade05a5e3478957bf5c804958c` adds an `accepted-destroy` control; workflow head `d57d5531d9a5d96d21685d31e75bc2aaed051dd4` compares close vs bidirectional destroy under the same matrix. Terminal execution evidence is pending.

## Gate assessment
Foundation PASS is **not** awarded. F001-F005 retain bounded direct execution. F006 has positive semantic transport evidence and now a materially narrower process-liveness failure family, but exact cause and successful combined regression remain OPEN. Native/product transfer and previously recorded F003/F004/F005 gaps remain material.

## HANDOFFS
- Quality/Systems: F006 proves semantic-oracle PASS and application BODY_DONE do not imply executable completion. Keep natural process exit as an independent oracle and preserve falsified alternatives.
- Mobile/Data: F006 is Dart/Linux loopback evidence only; do not transfer it to browser/mobile networking or durable application completion.
- Architecture: send-side completion and bidirectional resource lifecycle are distinct contracts.

## CHANGE WATCH / OPEN
- Flutter/Dart/browser behavior is version-sensitive; preserve exact SDK/ref/run identity.
- F006 exact root cause remains OPEN. Root-cause criterion for the current hypothesis is same-environment replication of `accepted-close` failure plus natural exit of structurally matched `accepted-destroy`.
- F006 combined semantic fixture still needs a successful natural-exit regression after cause is established.
- F001 native Android/iOS, Safari/iPadOS/EFB, PWA/product/release runtime remains OPEN.

## Next work
Recover the run triggered by workflow head `d57d5531d9a5d96d21685d31e75bc2aaed051dd4`. If close fails and destroy exits, repair the combined fixture with explicit bidirectional teardown and run regression; if not, falsify/refine the directionality hypothesis. Do not switch topics before this professional boundary is resolved or genuinely blocked.
