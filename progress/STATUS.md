# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-18  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005/A006 first integrated blocks complete |
| Mobile | Stage 1 IN STUDY — M001-M006 all have first professional/model boundaries; direct Flutter/native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated with persistence/migration/cache/restore/sync evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 now has generated shrinking plus mutation/exhaustive-search evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### Q004 — Deliberate mutation sensitivity + exhaustive-vs-generated comparison
Canonical: `research/quality/Q004_mutation_sensitivity_search_strength.md`; fixture: `research/quality/fixtures/Q004_mutation_exhaustive_generated_comparison.py`.

Python 3.13.5/Linux bounded evidence enumerated the complete 3-event sequence space for lengths 1..4: 120 sequences. Against an independent highest-version-wins/delete-semantic oracle, an arrival-order mutant failed 61/120 sequences and an ignore-delete mutant failed 86/120. A deliberately small deterministic generated campaign (seed `20260919`, 3 cases) killed ignore-delete once but missed arrival-order entirely; the retained deterministic `delete_v3 → update_v2` regression killed arrival-order.

This closes Q004's named bounded gaps for deliberate mutation sensitivity and exhaustive-vs-generated comparison. It does **not** establish global test adequacy, mutation-score sufficiency, real synchronization correctness, or Dart/Flutter behavior. Exhaustiveness applies only to the declared 3-event alphabet and length ≤4.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover all planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D001-D006 persistence/migration/cache/restore/sync evidence retained.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 now separates property/oracle strength from search strength with deliberate mutants and bounded enumeration.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Data:** use exact bounded enumeration when a synchronization submodel is genuinely tractable; generated search remains useful for larger spaces, and known failures should become deterministic regressions.
- **Architecture:** machine-checkable contracts/invariants can supply independent properties without exposing implementation representation.
- **Mobile:** transfer only the test-design method; no lifecycle/PWA/platform behavior follows from the Python model.
- **Systems:** mutation/generated CI campaigns require exact artifact/environment/seed/framework identity and resource budgets; mutation score is not a release oracle.
- **Design Studio / Web Manager / Marketing Manager:** considered; no materially relevant canonical evidence changes this bounded Quality method.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5 is available.

Q004's two explicit executable gaps—deliberate mutation sensitivity and exhaustive-vs-generated comparison—are now closed at bounded model level. The strongest independent candidates are:
1. `A005` repeated-change/evolution evidence — closes a stated Architecture gap with high reuse across product maintenance;
2. `A006` executable ADR-corpus governance validation — strengthens evidence-preserving decisions across all tracks;
3. targeted real platform/product transfer when trustworthy Dart/Flutter SDK, browser/EFB or device infrastructure becomes available;
4. direct F001 Dart JIT/AOT + Flutter runtime execution immediately when a trustworthy SDK environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter web build/service-worker/isolate/import and plugin/platform behavior are version-sensitive.
- Browser/PWA install/update/offline/background/storage APIs and iOS/iPadOS behavior are version-sensitive.
- Android storage/permission/backup and Apple Data Protection/Keychain behavior are platform/version sensitive.
- Deployment rollback, app-store/browser delivery, GitHub attestation/Sigstore behavior are service/version sensitive.
- NIST SP 800-154 remains CHANGE WATCH until final status is verified.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
