# Foundations Specialist Status

Track: Computer Science & Programming Foundations
Prefix: `F###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-20

## Active evidence

### F001 — Program Execution Foundations
**IN STUDY — DIRECT DART JIT/AOT + FLUTTER HOST→CHROME RUNTIME TRANSFER VALIDATED.** Run `35423963687` validates Dart JIT/AOT compile+execute; run `35426881450` validates Flutter framework/test binding; exact head `b547c5d564731521eaf49380492fd10b5a980df9`, run `35478966848`, job `105993130270` validates the same bounded widget oracle on host and Chrome. Native/Safari/PWA/product/release transfer remains OPEN.

### F002–F005
Bounded direct Dart/Flutter execution retained: identity/resource lifetime (F002), representation/queue semantics (F003), isolate ownership/sendability (F004), and async ordering/cancellation boundaries (F005). Previously recorded platform/product/GC/performance/backpressure gaps remain OPEN.

### F006 — OS, file, socket and network foundations
**IN STUDY — TRANSPORT SEMANTICS PASS; BOUNDED PROCESS-LIVENESS ROOT CAUSE ESTABLISHED; COMBINED REGRESSION PENDING.** Canonical: `research/foundations/F006_direct_dart_socket_transfer.md`, `research/foundations/F006_process_liveness_phase_isolation.md`.

Run `35489259464`, exact head `d57d5531d9a5d96d21685d31e75bc2aaed051dd4`, Dart 3.13.3/linux_x64 on Ubuntu 24.04.5, provides the causal discriminator: `accepted-close` replicated BODY_DONE→timeout/orphan termination while structurally matched `accepted-destroy` reached BODY_DONE and naturally exited. `server-close` and `refused-connect` controls also exited; `truncated-eof` retained the close-path failure.

**ROOT CAUSE at this bounded target:** the fixture treated send-side `Socket.close()` completion as complete connected-socket teardown. The receive side could retain process liveness; explicit bidirectional `destroy()` removed the symptom in the matched accepted-socket case. This is not a universal claim that `Socket.close()` leaks or is incorrect.

Commit `5aa89aa5c11c4baf68233a412566e891a855506a` repairs the combined semantic fixture to flush its truncated payload and then explicitly destroy the client. Hosted combined semantic + natural-exit regression remains pending; do not close F006 before terminal evidence.

## Gate assessment
Foundation PASS is **not** awarded. F001-F005 retain bounded direct execution. F006 now has semantic transport evidence plus bounded debug/root-cause evidence, but repaired combined regression and broader native/product transfer remain OPEN.

## HANDOFFS
- Quality/Systems: semantic PASS/BODY_DONE is not executable completion; preserve natural process exit/resource lifecycle as an independent oracle.
- Architecture: API completion must be interpreted at its documented boundary; send-side completion is not bidirectional teardown.
- Mobile/Data: Dart/Linux loopback evidence does not establish browser/mobile networking or durable application completion.

## CHANGE WATCH / OPEN
- Flutter/Dart/browser behavior is version-sensitive; preserve exact SDK/ref/run identity.
- F006 repaired combined semantic + natural-exit regression remains OPEN.
- F001 native Android/iOS, Safari/iPadOS/EFB, PWA/product/release runtime remains OPEN.

## Next work
Recover/execute the combined F006 fixture at or after `5aa89aa5...`; require truncated-EOF rejection + refused-connect semantic PASS + natural process exit. If successful, close this bounded F006 professional boundary and return to Balance Loop rather than repeating socket teardown variants.
