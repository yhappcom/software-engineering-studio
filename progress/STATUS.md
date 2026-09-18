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
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real application-process crash/restart; D006 real TCP ACK-loss/restart retry evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 generated shrinking + mutation/exhaustive-search evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### D006 — real TCP ambiguous ACK loss across server restart
Canonical: `research/data/D006_real_tcp_ambiguous_retry_restart.md`; fixture: `research/data/fixtures/D006_real_tcp_ambiguous_retry_restart.py`.

Python 3.13.5/Linux used actual IPv4 loopback TCP, separate server OS processes and SQLite persistent state. Server 1 received logical `op-1:+10`, committed it, then terminated via `os._exit(33)` before sending application ACK bytes. The client observed EOF. A fresh server process reopened the DB and received the retry. With stable operation identity + a durable dedup/result record in the mutation transaction, retry returned 10 and terminal state remained 10 with one operation record. Under the same failure schedule without deduplication, retry applied the mutation again and terminal state became 20.

This advances D006 from a modeled ambiguous-response failure to real socket communication + real application-process restart + persistent dedup state. It does not establish WAN loss, multi-host partition, mobile radio behavior, Firestore/Flutter behavior, hostile replay safety or exactly-once semantics.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D001-D006 persistence/migration/cache/restore/sync evidence retained; D005 includes real process-crash/restart; D006 now includes real TCP/process-restart ambiguous retry evidence.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 separates property/oracle strength from search strength.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Quality:** reuse commit → kill-before-ACK → restart → retry and judge terminal semantic state; reconnect success alone is not a recovery oracle.
- **Mobile:** reproduce this ambiguity on the exact Android/iOS/Flutter persistence/sync stack under lifecycle/network interruption.
- **Systems:** operation IDs used for correctness are not automatically replay-security controls; threat-model authorization/replay separately.
- **Architecture:** logical operation identity and dedup retention are protocol/state-ownership contracts.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes from this bounded transport/data mechanism.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5 is available. `tc`, `ip`, and `unshare` executables exist, but their presence alone is not treated as proof that privileged network-namespace fault injection is trustworthy/available.

D005 already established application-process crash/restart persistence. D006 now establishes a stronger cross-boundary failure: actual TCP response loss caused by server death after commit, followed by server restart and retry against durable state. Do not deepen by repeating localhost cases. Next work should attempt a genuinely stronger controllable network interruption/namespace boundary only if privileges and isolation can be verified, or a storage/I/O fault below application process; otherwise use exact-ref product transfer or another track's strongest real evidence gap. Direct F001 Dart/Flutter execution immediately outranks these if a trustworthy SDK appears.

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
