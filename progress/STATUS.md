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
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 now includes real application-process crash/restart SQLite evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 generated shrinking + mutation/exhaustive-search evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — real application-process crash/restart transaction boundary
Canonical: `research/data/D005_process_crash_transaction_boundary.md`; fixture: `research/data/fixtures/D005_process_crash_transaction_boundary.py`.

Python 3.13.5/Linux used the Python SQLite runtime in WAL mode with `synchronous=FULL`. Separate child processes executed the same transaction shape and then terminated abruptly via `os._exit`, bypassing orderly connection close. A child killed with an active uncommitted transaction exited 24; a fresh process observed only the baseline row with `integrity_check=ok`. A second child committed first and immediately exited 23; a fresh process observed both baseline and committed rows with `integrity_check=ok`.

This advances the evidence ladder from modeled/pre-publication failure injection to a real OS **application-process termination/restart** boundary. It does not establish OS-crash, power-loss, filesystem/device durability, WAL/checkpoint restore safety, mobile behavior or Flutter plugin behavior. Those remain OPEN.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D001-D006 persistence/migration/cache/restore/sync evidence retained; D005 now includes real process-crash/restart evidence.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 separates property/oracle strength from search strength.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Quality:** reuse out-of-process crash injection + fresh-process semantic acceptance; do not relabel application crash as power-loss evidence.
- **Mobile:** reproduce pre/post-commit process-death behavior on the exact Android/iOS/Flutter persistence stack.
- **Systems:** stronger durability claims require fault injection below the application-process boundary plus explicit filesystem/device assumptions.
- **Architecture:** commit state and application semantic acceptance remain distinct contracts.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes from this bounded persistence mechanism.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5 is available. The standalone `sqlite3` CLI is also absent, but Python's SQLite runtime supports the D005 fixture.

The prior strongest queue called for real crash/restart/durable/network evidence. D005 now closes the **application-process crash/restart** portion with actual out-of-process execution. Do not deepen it by merely generating more synthetic process-crash cases. Next candidates should seek a genuinely stronger available boundary: storage/I/O fault or real network interruption/restart evidence; exact-ref product transfer where it resolves a real decision; direct F001 Dart/Flutter execution immediately if a trustworthy SDK appears; or real mobile/browser/EFB transfer when infrastructure becomes available.

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
