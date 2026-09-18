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
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real application-process crash/restart + bounded SQLite `SQLITE_FULL`; D006 real TCP server-death ambiguity + isolated live-process kernel link interruption |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 generated shrinking + mutation/exhaustive-search evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — bounded SQLite capacity failure (`SQLITE_FULL`)
Canonical: `research/data/D005_bounded_sqlite_full_transaction_boundary.md`; fixture: `research/data/fixtures/D005_sqlite_full_transaction_boundary.py`.

Python 3.13.5 / SQLite 3.46.1 / Linux used SQLite's documented `PRAGMA max_page_count` database-growth limit to force a transaction-level capacity failure. With a committed baseline `(1,100)`, page count 2 and max page count 4, a 5000-byte insert raised SQLite code 13 `SQLITE_FULL`. After rollback, the independent semantic aggregate remained `(1,100)` and `PRAGMA integrity_check=ok`.

This advances D005's failure evidence but is deliberately narrower than actual disk exhaustion. A constrained tmpfs mount was attempted and denied by the environment, so OS/filesystem `ENOSPC`, short-write/fsync failure, WAL/checkpoint capacity failure, power/device failure and mobile storage pressure remain OPEN rather than simulated.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D001-D006 persistence/migration/cache/restore/sync evidence retained; D005 includes real process-crash/restart plus bounded capacity failure; D006 has server death and live-process kernel link-down ambiguity mechanisms.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 separates property/oracle strength from search strength.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Quality:** storage-fault campaigns must distinguish deterministic SQLite growth limits from OS/filesystem/device faults and use terminal semantic/integrity oracles.
- **Mobile:** reproduce storage capacity/quota and process/network interruption on the exact Android/iOS/Flutter persistence stack.
- **Systems:** future lower-layer storage fault injection must prove which I/O boundary failed; application exception text alone is insufficient.
- **Architecture:** transaction/recovery publication boundaries remain externally relevant state contracts.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes from this bounded data/storage mechanism.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5 is available.

D005 now has a documented SQLite capacity-boundary failure in addition to real application-process crash/restart. Do not repeat `max_page_count` variants. A stronger storage block is justified only if the environment can prove a materially lower-layer fault such as constrained filesystem/device ENOSPC, short write/fsync failure, or VFS-level fault injection. D006 likewise should not add more single-host variants without a topology/fault-semantic change. Otherwise prefer exact-ref product transfer or another track's strongest real evidence gap. Direct F001 Dart/Flutter execution immediately outranks these if a trustworthy SDK appears.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter web build/service-worker/isolate/import and plugin/platform behavior are version-sensitive.
- Browser/PWA install/update/offline/background/storage APIs and iOS/iPadOS behavior are version-sensitive.
- Android storage/permission/backup and Apple Data Protection/Keychain behavior are platform/version sensitive.
- SQLite durability depends on documented OS/filesystem/device assumptions; bounded `SQLITE_FULL` and application-process evidence must not be generalized to power loss or lower-layer ENOSPC.
- Deployment rollback, app-store/browser delivery, GitHub attestation/Sigstore behavior are service/version sensitive.
- NIST SP 800-154 remains CHANGE WATCH until final status is verified.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
