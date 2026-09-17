# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-18  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 refactoring/debt + A006 evidence-preserving decision lifecycle first integrated blocks complete |
| Mobile | Stage 1 IN STUDY — M001-M005 first professional/model boundaries complete; direct Flutter/native/web transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated with persistence/migration/cache/restore/sync evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 executable counterexample/shrinking evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### M005 — Cross-platform architecture, portability and platform divergence
Canonical: `research/mobile/M005_cross_platform_portability_divergence.md`; fixture: `research/mobile/fixtures/M005_capability_contract_matrix.py`.

Current Flutter/Dart/browser guidance establishes that shared Flutter/Dart source does not erase platform differences: Flutter web lacks `dart:io` filesystem access, has different platform-detection/import mechanisms, and does not currently provide Dart isolate concurrency in the same way as native; web platform integration generally uses JS interoperability rather than native platform channels. Studio synthesis therefore models portability as `semantic contract → capability vector → platform mechanism → failure/fallback → acceptance oracle` rather than code-reuse percentage or matching API names.

Python 3.13.5/Linux bounded execution rejected an unsafe native-filesystem assumption for the web model, allowed a download fallback where the higher-level export contract permitted it, and kept required background retry explicitly unsupported when the modeled platform lacked the guarantee. PASS is only for this capability model, not Flutter/browser behavior.

Exact-ref transfer: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-18`. At that ref, product truth explicitly excludes guaranteed automatic PWA P2P without common LAN and immediate transfer while backgrounded/terminated, and the current canonical Makefile exposes a distinct `build-pwa` pipeline. Default branch is not assumed to equal production; no PWA/EFB acceptance claim is made.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt and evidence-preserving decision lifecycle.
- **Mobile:** M001-M005 now cover runtime/state, lifecycle/process/background, storage/permission/security, plugin/native boundaries and portability/divergence; real runtime/platform transfer OPEN.
- **Data:** D001-D006 persistence/migration/cache/restore/sync evidence retained.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 includes executable generated counterexample/shrinking.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Architecture:** platform adapters/conditional imports need semantic acceptance criteria; shared API shape is not portability evidence.
- **Data:** offline/persistence/sync/durability guarantees require per-platform transfer validation.
- **Quality:** cross-platform contract suites should test explicit unsupported/degraded outcomes and platform-specific failures.
- **Systems:** PWA/native validation must bind exact source/build/post-build/artifact/deployment/runtime identity.
- **Design Studio:** no materially relevant PWA/mobile-web search result found this run; Engineering must still return unsupported/degraded implementation states rather than silently redefine interaction semantics.
- **Web Manager:** no materially relevant LogMate/PWA search result found this run; browser/PWA operational decisions remain Web-owned where applicable.
- **Marketing Manager:** no materially relevant PWA search result found this run.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5 is available.

M005 removes the previously untouched Mobile portability/divergence boundary at first professional/model level. Current strongest independent candidates are:
1. `M006` native app vs PWA/web boundary and deployment constraints — high direct LogMate/EFB leverage and now the remaining untouched Mobile Foundation block, but requires current browser/platform evidence plus a coherent acceptance/failure boundary rather than a source-only summary;
2. `Q004` deliberate mutation sensitivity plus exhaustive-vs-generated comparison — executable and strengthens search-method evidence without Dart/Flutter;
3. `A005` repeated-change/evolution evidence — strengthens architecture closure if a reusable change-pressure experiment can be constructed;
4. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter web isolate/Wasm/import behavior, plugin registration and native/web integration are version-sensitive.
- Browser/PWA install/update/offline/background APIs and iOS/iPadOS PWA behavior are platform/version sensitive.
- Android storage/permission/backup behavior and Apple Data Protection/Keychain behavior are platform/version sensitive.
- Deployment-platform rollback semantics and app-store/browser delivery policies are service/version sensitive.
- GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive.
- ADR process guidance checked 2026-09-18; operational guidance can evolve.
- NIST SP 800-154 remains draft/planned for finalization; recheck before treating it as final.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
