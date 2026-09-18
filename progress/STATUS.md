# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-18  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 repeated-change executable evidence; A006 decision-lifecycle + bounded executable governance evidence |
| Mobile | Stage 1 IN STUDY — M001-M006 first professional/model boundaries; direct Flutter/native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real application-process crash/restart; D006 real TCP server-death ambiguity plus isolated live-process kernel link interruption |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 generated shrinking + mutation/exhaustive-search evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### D006 — network-device interruption while application processes remain alive
Canonical: `research/data/D006_network_namespace_link_interruption.md`; fixture: `research/data/fixtures/D006_network_namespace_link_interruption.py`.

Python 3.13.5/Linux created a fresh user+network namespace with `unshare -Urn`, enabled its loopback interface, ran real TCP client/server traffic, committed `op-1:+10` to SQLite, then brought `lo` down before the response was received. Both application processes remained alive. The client timed out; after `lo` was restored, retry with stable logical-operation identity + durable dedup returned/finalized 10 with one op record. Under the same link fault without deduplication, retry/final state became 20.

A direct `unshare -n` attempt failed with `Operation not permitted`, while the combined fresh user+network namespace succeeded. Installed `unshare`/`ip` binaries were therefore not treated as privilege evidence; the intended isolation/fault control was executed and observed.

This is stronger than the prior server-death case in failure-mechanism diversity, but remains single-host loopback namespace evidence. It is not veth/two-host, WAN, packet-loss/reorder, mobile radio, Flutter/backend, or production evidence.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D001-D006 persistence/migration/cache/restore/sync evidence retained; D005 includes real process-crash/restart; D006 now has two materially different real ambiguity mechanisms: server death and live-process kernel link-down.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 separates property/oracle strength from search strength.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Quality:** add `commit → link down → timeout → link up → retry → terminal semantic oracle` as a fault schedule distinct from process death.
- **Mobile:** reproduce this ambiguity on the exact Android/iOS/Flutter persistence/sync stack under real lifecycle/connectivity controls.
- **Systems:** fault-injection setup must verify namespace/capability/fault application; operation IDs used for correctness are not automatically replay-security controls.
- **Architecture:** logical operation identity and dedup retention remain protocol/state-ownership contracts.
- **Design Studio / Web Manager / Marketing Manager:** checked; no canonical decision there changes from this bounded transport/data mechanism.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5 is available.

D006 has now crossed two real single-host failure mechanisms: server process death after commit/before ACK, and kernel network-device unavailability while both application processes remain alive. Do not keep adding localhost variants. A further D006 block is justified only if it materially crosses topology/fault semantics, such as verified veth/two-namespace or remote packet-loss/reorder/concurrency. Otherwise prefer D005 storage/I/O fault evidence, exact-ref product transfer, or another track's strongest real evidence gap. Direct F001 Dart/Flutter execution immediately outranks these if a trustworthy SDK appears.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter web build/service-worker/isolate/import and plugin/platform behavior are version-sensitive.
- Browser/PWA install/update/offline/background/storage APIs and iOS/iPadOS behavior are version-sensitive.
- Android storage/permission/backup and Apple Data Protection/Keychain behavior are platform/version sensitive.
- SQLite durability depends on documented OS/filesystem/device assumptions; application-process evidence must not be generalized to power loss.
- Deployment rollback, app-store/browser delivery, GitHub attestation/Sigstore behavior are service/version sensitive.
- NIST SP 800-154 remains CHANGE WATCH until final status is verified.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
