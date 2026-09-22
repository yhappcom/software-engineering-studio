# Foundations Specialist Status

Track: Computer Science & Programming Foundations
Prefix: `F###`
State: **Stage 1 — IN STUDY / NOT YET PASSED**
Last sync: 2026-09-22

## Active evidence

### F001 — Program Execution Foundations
**IN STUDY — DIRECT DART JIT/AOT + FLUTTER HOST→CHROME + BOUNDED macOS SAFARI RUNTIME TRANSFER VALIDATED.** Run `35423963687` validates Dart JIT/AOT compile+execute; run `35426881450` validates Flutter framework/test binding; exact head `b547c5d564731521eaf49380492fd10b5a980df9`, run `35478966848`, job `105993130270` validates the bounded widget oracle on host and Chrome.

Safari transfer exact head `44c8be44bb53f2b67c08f40a0738f29858018bdd`, run `35727646652`, job `106745123287`, `macos-15`, terminal success; artifact `10694445918`, digest `sha256:f1274228bdbfaf29b6eca507a6e490385dbf3756777ce7e130007ecbb75bdf35`. The committed fail-closed WebDriver oracle loads the release Flutter JavaScript artifact in real macOS Safari and fails unless browser-owned `document.title` reaches the delayed Dart state `M006_ASYNC_READY`. This supplies bounded cross-browser-engine **TRANSFER VALIDATION**. It does not establish iOS/iPadOS/native/PWA offline/product/release behavior.

### F002–F005
Bounded direct Dart/Flutter execution retained: identity/resource lifetime (F002), representation/queue semantics (F003), isolate ownership/sendability (F004), and async ordering/cancellation boundaries (F005). Previously recorded platform/product/GC/performance/backpressure gaps remain OPEN.

### F006 — OS, file, socket and network foundations
**BOUNDED PROFESSIONAL BOUNDARY CLOSED — TRANSPORT SEMANTICS + ROOT CAUSE + FIX + REGRESSION VALIDATED.** Canonical: `research/foundations/F006_direct_dart_socket_transfer.md`, `research/foundations/F006_process_liveness_phase_isolation.md`.

Run `35489259464`, exact head `d57d5531d9a5d96d21685d31e75bc2aaed051dd4`, Dart 3.13.3/linux_x64 on Ubuntu 24.04.5, established the causal discriminator: `accepted-close` replicated BODY_DONE→timeout/orphan termination while structurally matched `accepted-destroy` naturally exited. Server-only/refused-connect controls exited; truncated-eof retained the close-path failure.

**ROOT CAUSE at this bounded target:** the fixture treated send-side `Socket.close()` completion as complete connected-socket teardown. The receive side could retain process liveness; explicit bidirectional `destroy()` removed the symptom in the matched accepted-socket case. This is not a universal claim that `Socket.close()` leaks or is incorrect.

Commit `5aa89aa5c11c4baf68233a412566e891a855506a` repaired the combined fixture. **REGRESSION PASS:** workflow run `35491928998`, job `106028240397`, exact checkout `5aa89aa5...`, Dart 3.13.3 stable/linux_x64, Ubuntu 24.04.5, runner image `20260907.300.1`, completed success. The combined fixture preserved `truncated_eof_rejected=true`, `connect_failure_observed=true`, `bidirectional_teardown=true` and then naturally exited without the prior timeout/orphan termination.

## Gate assessment
Foundation PASS is **not** awarded. F001-F006 each have bounded direct executable evidence, F001 now crosses Chrome→Safari browser engines, and F006 has a complete failure→reproduction→isolation→root cause→fix→regression chain. Native Android/iOS/iPadOS, product/release transfer and other broader Stage-1 scope gaps remain OPEN.

## HANDOFFS
- Quality/Systems: semantic PASS/BODY_DONE is not executable completion; preserve natural process exit/resource lifecycle as an independent oracle. Safari validation is meaningful because its semantic step is fail-closed and bound to exact run/head/artifact identity.
- Architecture: API completion must be interpreted at its documented boundary; send-side completion is not bidirectional teardown.
- Mobile: Safari transfer is bounded macOS browser evidence, not native/iOS/iPadOS/EFB evidence.
- Data: browser execution does not establish persistence/durability semantics.

## CHANGE WATCH / OPEN
- Flutter/Dart/browser behavior is version-sensitive; preserve exact SDK/ref/run identity.
- F006 cross-platform/native/product networking transfer remains OPEN; do not repeat equivalent Linux close-vs-destroy variants.
- F001 native Android/iOS, iOS/iPadOS Safari/EFB, Safari PWA lifecycle, product/release runtime remain OPEN.

## Next work
Return to Balance Loop. Direct Dart JIT/AOT and bounded Flutter Chrome/Safari runtime execution are no longer the historical blocker in older prompts. Prefer a materially different evidence class with higher leverage: native/mobile runtime, Safari PWA lifecycle, exact product PWA/build transfer, physical storage/connectivity boundary, or another track's stronger Stage-1 gap.
