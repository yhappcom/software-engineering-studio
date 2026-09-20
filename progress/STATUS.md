# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-20  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome transfer validated; F002-F005 bounded direct Dart/Flutter execution; F006 transport semantic oracles PASS but post-oracle process/resource liveness fails; root cause OPEN |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 executable governance + natural product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 direct Flutter framework execution; M006 exact Chromium offline + restart + update/control + offline cold-start transfer; native/Safari-iPadOS/EFB/product runtime OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 product-owned Flutter 3.38.7 baseline + lock transfer validated; exact-ref source build blocked at cross-private-repository runner acquisition |

No specialist has passed Foundation.

## Meaningful new evidence

### F006 — transport semantics separated from process liveness
**VALIDATION:** decoded historical logs for exact head `835104ea9dac410b4f0a4d17f748882710f5921c`, run `35437455712`, job `105882433731` show Dart 3.13.3 emitted `F006_DART_SOCKET_PASS truncated_eof_rejected=true connect_failure_observed=true` roughly 0.25 seconds after the fixture step began. The process then remained alive until the independent one-minute step timeout; runner cleanup explicitly terminated the orphan Dart process.

**SYNTHESIS:** the bounded truncated-frame EOF and released-port connection-failure oracles passed. The failing dimension is natural process/resource-lifecycle completion after those oracles. A target PASS marker and a successful executable run are distinct verdicts.

**DEBUG:** prior client close-order hypothesis remains falsified. Exact alternative head `3904ca9806d8e48bb90b5f6019acbdffc60feffb` changes listener ownership to one-shot `server.first`, adds phase markers and bounded cleanup while preserving the semantic oracles. Run `35484021836`, job `106006913686` is pending; no resource-retention root cause is claimed yet.

Canonical: `research/foundations/F006_process_liveness_phase_isolation.md`.

## Retained evidence
- F001-F005: bounded direct Dart/Flutter execution appropriate to current claims; F001 includes host→Chrome test-runtime transfer.
- F006: direct Dart transport semantic oracles now positively observed; natural process exit/resource lifecycle failed in the historical fixture; causal resource remains OPEN.
- Architecture: A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, evolution and evidence-preserving decisions; A006 includes natural exact-ref product decision-state transfer.
- Mobile: M001 direct framework execution; M006 exact Chromium same-session offline, restart persistence, update/client-control lifecycle and offline cold-start evidence.
- Data: D005 rollback/storage/WAL/checkpoint/live backup/interruption evidence; D006 transport faults + exact-ref inbound progress transfer.
- Quality: Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- Systems: S004 exact Flutter 3.38.7 project baseline + dependency-lock integrity transfer; product-owned `make build-pwa` path recovered but source build blocked before checkout. S005 hosted attestation evidence plus verifier contradiction; S006 directory-sync publication failure evidence.

## Cross-track handoffs
- **Foundations → Quality/Systems:** F006 demonstrates semantic-oracle PASS can coexist with executable-process-liveness FAIL; keep target assertions, cleanup/liveness and outer harness deadlines as separate evidence dimensions.
- **Foundations → Mobile/Data:** F006 transport semantic evidence is bounded `dart:io` loopback evidence only; it does not establish browser/mobile networking or application durable completion.
- **Foundations → Mobile:** F001 Chrome success is browser test-runtime evidence only; M006 remains the stronger PWA lifecycle evidence and native/Safari platform execution remains separate.
- **Architecture → Product/Data/Mobile/Systems:** preserve decision status separately from implementation/evidence status; presentation implementation must not silently close persistence/Sync/platform/release questions.
- **Mobile → Quality:** PWA acceptance should separately test warm offline, restart persistence, update/controller transition and offline-before-navigation cold start; an uncached negative oracle detects false offline passes.
- **Mobile → Systems:** exact Chromium identity for current M006 evidence is `140.0.7339.16`, Playwright build `v1187`; future product acceptance must additionally bind LogMate build/post-build artifact, origin and active worker/controller identity.
- **Mobile → Data:** CacheStorage/service-worker shell persistence is not authoritative-record persistence, durability, backup/recovery or eviction evidence.
- **Systems / LogMate:** exact source build still needs authorized cross-private-repository execution access; no LogMate files were edited.
- **Design Studio / Web Manager / Marketing Manager:** RELATED DOMAIN CHECK performed where material; no canonical decisions changed and no files edited there.

## Current Balance Loop
Finish the current F006 professional boundary before changing topic: recover run `35484021836`; if natural exit succeeds, require a minimal A/B reproduction before naming listener lifecycle as root cause; if it still hangs, use phase markers to isolate the retained resource. Do not repeat blind close-order permutations. Resume S004 immediately when authorized exact-ref source acquisition is available. Otherwise prefer materially stronger evidence classes: Safari/iPadOS/EFB or Android/iOS execution, canonical LogMate PWA runtime, storage-eviction or physical/real-connectivity transfer, natural ADR/release lifecycle evidence.

## CHANGE WATCH
- Flutter/Dart/browser/service-worker behavior is version-sensitive; exact SDK/ref/engine/browser identity matters.
- F006 direct Dart bounded transport semantic oracles are positive at run `35437455712`, but natural process exit failed and resource-retention root cause remains OPEN; alternative run `35484021836` is pending.
- F001 host→Chrome test-runtime transfer is validated at run `35478966848`; native/Safari/PWA/product/release runtime remains OPEN.
- Product-owned LogMate project baseline is exact Flutter 3.38.7; operational release toolchain/production identity remains unknown.
- Canonical LogMate source build/artifact identity remains OPEN and depends on authorized execution-time source acquisition.
- Current M006 Chromium identity is exact `140.0.7339.16` / Playwright build `v1187`; future browser versions require revalidation rather than silent transfer.
- Safari/iPadOS/EFB and Android/iOS storage/background/backup behavior is platform/version sensitive.
- A006 natural ADR lifecycle corpus and long-horizon supersession evidence remain OPEN.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
