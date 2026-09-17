# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-18  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial + A005 first executable refactoring/debt boundary block complete |
| Mobile | Stage 1 IN STUDY — M001-M004 first professional/model boundaries complete; direct Flutter/native transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated with persistence/migration/cache/restore/sync evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 executable counterexample/shrinking evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### M004 — Plugin, platform-channel and native integration failure boundaries
Canonical: `research/mobile/M004_plugin_platform_channel_native_integration_boundaries.md`  
Fixture: `research/mobile/fixtures/M004_native_bridge_contract_lifetime.py`

Current Flutter primary documentation establishes platform channels as asynchronous serialized boundaries; `MethodChannel.invokeMethod` distinguishes successful result, `PlatformException` and `MissingPluginException`; payload/result compatibility depends on the codec/runtime contract; and multiple Flutter engines create independent plugin instances/lifetimes. Built-in channel FIFO ordering is not promoted into atomicity, durability or exactly-once semantics.

Python 3.13.5/Linux bounded evidence accepted a valid registered response while rejecting missing registration, schema mismatch and a detached modeled engine instance. A deliberate unsafe adapter converted missing implementation into `None`, showing how an integration-availability failure can be silently collapsed into an application value. This validates the reasoning model only, not Flutter/native behavior.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005 change pressure, ownership/dependency, semantic contracts and refactoring/debt boundaries retained.
- **Mobile:** M001-M004 cover runtime/state, lifecycle/process/background, storage/permission/security properties and first plugin/native integration boundaries; real runtime/platform transfer OPEN.
- **Data:** D001-D006 persistence/migration/cache/restore/sync evidence retained.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 includes executable generated counterexample/shrinking.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Architecture:** plugin method/payload/error/lifecycle behavior is an interface contract, not merely implementation detail.
- **Data:** ambiguous native effects require explicit operation identity/postcondition before retry; channel completion is not durability.
- **Quality:** future real Flutter integration campaign should inject missing plugin, native error, malformed reply, permission denial, engine detach/recreate and ambiguous retry.
- **Systems:** bind plugin validation to exact dependency lock/build/artifact because source package presence does not prove native implementation packaging.
- **Design Studio:** implementation must preserve ambiguous/unavailable states where interaction semantics distinguish them; no canonical design decision changed.
- **Web Manager:** PWA/browser API integration is a distinct transfer target; native plugin evidence does not transfer automatically.
- **Marketing Manager:** not materially relevant to M004.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. `dart` and `flutter` executables remain unavailable in the current environment; Python 3.13.5 is available.

M004 removes another untouched Mobile Stage-1 boundary at first professional/model level. Current strongest independent candidates are:
1. `A006` ADR/evidence-preserving engineering decisions — remaining Architecture professional/governance boundary with broad cross-track reuse;
2. `M005` cross-platform architecture, portability and platform divergence — next Mobile prerequisite, but real transfer evidence may remain runtime-constrained;
3. `Q004` deliberate mutation sensitivity plus exhaustive-vs-generated comparison — deepens test-method evidence;
4. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter platform-channel/plugin registration, background-isolate, federated-plugin and native API behavior are version-sensitive.
- Android storage/permission/backup behavior and Apple Data Protection/Keychain behavior are platform/version sensitive.
- Deployment-platform rollback semantics and app-store/browser delivery policies are service/version sensitive.
- GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive.
- NIST SP 800-154 remains draft/planned for finalization; recheck before treating it as final.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
