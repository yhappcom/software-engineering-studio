# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-18  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial + A005 first executable refactoring/debt boundary block complete |
| Mobile | Stage 1 IN STUDY — M001 runtime/lifecycle + M002 process/background + M003 sandbox/storage/permission/security-property first blocks complete |
| Data | Stage 1 IN STUDY — D001-D006 initiated with persistence/migration/cache/restore/sync evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 executable counterexample/shrinking evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### M003 — App sandbox, files, permissions, secure storage and platform APIs
Canonical: `research/mobile/M003_sandbox_files_permissions_secure_storage_platform_apis.md`  
Fixture: `research/mobile/fixtures/M003_storage_property_vector.py`

Current Android/Apple primary documentation plus bounded model evidence establish that mobile storage must be reasoned about as independent properties rather than a single “private/secure/persistent” label. Relevant axes include namespace/access authority, purgeability, uninstall behavior, backup/migration, lock-state availability, protection, sharing/export and recovery role.

Android app-specific internal persistent files and cache are both app-private, but cache can be removed earlier and app-specific files are removed on uninstall. Android also provides app-private/system-mediated file access paths that do not require broad storage permissions. Apple Data Protection and Keychain accessibility classes expose different availability and migration contracts; device-only accessibility can intentionally conflict with migration/recovery requirements.

Python 3.13.5/Linux bounded fixture passed independent role predicates that reject purgeable cache as the only non-reconstructible authoritative record, reject app-private internal files when uninstall survival is required, and reject ordinary private files when credential protection is required. This validates the reasoning model only; it is not Android/iOS/Flutter execution evidence.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005 change pressure, ownership/dependency, semantic contracts and refactoring/debt boundaries retained.
- **Mobile:** M001-M003 now cover runtime/state, lifecycle/process/background and first storage/permission/security-property boundaries; real runtime/platform transfer OPEN.
- **Data:** D001-D006 persistence/migration/cache/restore/sync evidence retained.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 includes executable generated counterexample/shrinking.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Architecture:** storage API/location is subordinate to explicit state ownership and recovery contracts.
- **Data:** app-private does not establish durability, uninstall survival, backup or restore acceptance; specify those independently.
- **Quality:** real-platform validation should inject cache eviction, permission denial/revocation, lock/reboot, uninstall/reinstall and restore boundaries with semantic oracles.
- **Systems:** S002 remains canonical for threat modeling/least privilege/secrets; M003 applies those principles at mobile platform APIs.
- **Design Studio:** recovery/export UX may constrain storage semantics; no canonical design decision changed here.
- **Web Manager:** PWA/browser storage is not covered by native M003 and remains M006/web overlap.
- **Marketing Manager:** not materially relevant to this block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. `dart` and `flutter` executables remain unavailable in the current environment; Python 3.13.5 is available.

M003 removes another major untouched Mobile Stage-1 boundary at first professional/model level. Current strongest independent candidates are:
1. `M004` plugin/platform-channel/native integration and failure boundaries — high mobile prerequisite and future Flutter leverage, but real runtime execution may remain constrained;
2. `A006` ADR/evidence-preserving decisions — closes a remaining Architecture professional boundary with broad governance/release leverage;
3. `Q004` deliberate mutation sensitivity plus exhaustive-vs-generated comparison — deepens test-method evidence;
4. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Android storage/permission/backup behavior and Apple Data Protection/Keychain behavior are platform/version sensitive.
- Flutter/plugin mappings to native storage/security APIs require exact-version transfer validation.
- Deployment-platform rollback semantics and app-store/browser delivery policies are service/version sensitive.
- GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive.
- NIST SP 800-154 remains draft/planned for finalization; recheck before treating it as final.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
