# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-18  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 refactoring/debt + A006 evidence-preserving decision lifecycle first integrated blocks complete |
| Mobile | Stage 1 IN STUDY — M001-M006 all have first professional/model boundaries; direct Flutter/native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated with persistence/migration/cache/restore/sync evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 executable counterexample/shrinking evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### M006 — Native app vs PWA/web boundary and deployment constraints
Canonical: `research/mobile/M006_native_pwa_web_deployment_constraints.md`; fixture: `research/mobile/fixtures/M006_native_pwa_acceptance_matrix.py`.

Current WebKit/MDN evidence separates Home Screen installation, offline capability, service-worker event execution, storage policy, update/client-control state and continuous background execution. Service workers may be terminated/restarted; their global state is not persistent. Background Sync remains limited availability rather than a portable baseline. iOS/iPadOS 26 changed Home Screen behavior so sites added there open as web apps by default unless the user disables `Open as Web App`; this does not make service workers/offline/background guarantees automatic.

Python 3.13.5/Linux bounded acceptance evidence showed an installability-only gate falsely accepting a modeled PWA after the contract was strengthened to require guaranteed continuous background execution; the capability-aware oracle rejected it. PASS is only for the acceptance model, not browser/platform behavior.

Exact-ref transfer: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-18`. Product truth treats native and tablet/EFB PWA as first-class targets but explicitly does not guarantee immediate Sync while backgrounded/terminated without separate validation; canonical ledger/persistence/backup/server Sync are not yet implemented. Default branch is not assumed to equal production and no PWA acceptance claim is made.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 now cover every planned Foundation boundary at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D001-D006 persistence/migration/cache/restore/sync evidence retained.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 includes executable generated counterexample/shrinking.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Architecture:** PWA/native adapters and delivery mechanisms need semantic acceptance criteria; installability/API shape is not portability evidence.
- **Data:** PWA authoritative persistence, eviction/recovery and queued sync guarantees require exact-platform transfer validation.
- **Quality:** PWA acceptance should inject offline, service-worker update/control, storage, termination and retry failures and verify explicit unsupported/degraded outcomes.
- **Systems:** bind PWA acceptance to exact source/build/post-build/artifact/deployment origin/browser/OS/service-worker client-control identity.
- **Design Studio:** no materially relevant PWA/mobile-web search result found this run; Engineering must return unsupported/degraded sync states rather than silently redefine interaction semantics.
- **Web Manager:** no materially relevant LogMate/PWA search result found this run; browser/PWA operational decisions remain Web-owned where applicable.
- **Marketing Manager:** no materially relevant PWA search result found this run.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. Environment recheck 2026-09-18 found no `dart` or `flutter` executable; Python 3.13.5 is available.

M006 removes the final untouched Mobile Stage-1 boundary at first professional/model level. All six tracks now have initial evidence across their planned Foundation areas, but none passes because transfer/production evidence remains materially incomplete. Current strongest independent candidates are:
1. `Q004` deliberate mutation sensitivity plus exhaustive-vs-generated comparison — executable, closes a stated Quality evidence gap and strengthens state-space search methods reused by Data/async/reliability;
2. `A005` repeated-change/evolution evidence — strengthens architecture closure with reusable change-pressure evidence;
3. targeted real platform/product transfer when a trustworthy Dart/Flutter SDK, browser/EFB or device environment becomes available;
4. direct F001 Dart JIT/AOT + Flutter runtime execution immediately when a trustworthy SDK environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter web build/service-worker/isolate/import behavior and plugin/platform behavior are version-sensitive.
- Browser/PWA install/update/offline/background/storage APIs and iOS/iPadOS Home Screen behavior are platform/version sensitive.
- Android storage/permission/backup behavior and Apple Data Protection/Keychain behavior are platform/version sensitive.
- Deployment-platform rollback semantics and app-store/browser delivery policies are service/version sensitive.
- GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive.
- ADR process guidance checked 2026-09-18; operational guidance can evolve.
- NIST SP 800-154 remains draft/planned for finalization; recheck before treating it as final.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
