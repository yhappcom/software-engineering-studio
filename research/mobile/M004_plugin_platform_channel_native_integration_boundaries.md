# M004 — Plugin, Platform-Channel & Native Integration Failure Boundaries

Status: **IN STUDY — first integrated Foundation block + bounded executable contract/lifetime evidence**
Evidence date: 2026-09-18

## Problem / scope
Flutter plugins and platform channels cross a runtime, serialization, registration, lifecycle and native-API boundary. A Dart-facing API that looks like an ordinary function call does not erase those boundaries. This block establishes the minimum model needed before treating plugin calls as ordinary local calls.

## SOURCE
Current Flutter primary documentation establishes:

- platform channels asynchronously exchange messages between Flutter and host-platform code;
- `MethodChannel` identity is its channel name; identically named channels interfere;
- the Dart argument/result surface is dynamic but values must be supported by the selected codec;
- `invokeMethod` can complete with a value, `PlatformException`, or `MissingPluginException`; an incompatible generic result can fail at runtime;
- built-in `MethodChannel` guarantees FIFO ordering for method calls on that channel, but that is not a general transaction/durability guarantee;
- plugins can have one instance per Flutter engine; multiple engines therefore imply multiple plugin-instance lifetimes, and engine-specific state should not be assumed global/static;
- federated plugins separate app-facing API, platform interface and platform implementations; endorsed and non-endorsed implementations have different dependency/registration mechanics;
- Flutter documents Pigeon as an alternative for generated type-safe platform-specific interfaces, while raw channels remain dynamically encoded contracts.

Primary sources checked 2026-09-18:
- Flutter, Writing custom platform-specific code / platform channels: https://docs.flutter.dev/platform-integration/platform-channels
- Flutter API, `MethodChannel`: https://api.flutter.dev/flutter/services/MethodChannel-class.html
- Flutter API, `MethodChannel.invokeMethod`: https://api.flutter.dev/flutter/services/MethodChannel/invokeMethod.html
- Flutter, Developing packages & plugins: https://docs.flutter.dev/packages-and-plugins/developing-packages
- Flutter, Plugins in Flutter tests: https://docs.flutter.dev/testing/plugins-in-tests

## SYNTHESIS — integration model
Treat a native integration call as:

`app-facing contract → platform-interface/plugin selection → registration/engine instance → channel name + codec → serialized request → native handler/API → serialized result/error → Dart decoding/type contract → application semantic acceptance`

A successful call therefore establishes only the predicates actually checked across that chain.

Important separations:

1. **API presence ≠ implementation registered.** A Dart package can compile while the running platform lacks a handler for a method.
2. **Message delivery ≠ semantic success.** A decoded reply can still violate the app-facing schema/invariant.
3. **FIFO channel ordering ≠ atomicity, durability or exactly-once effect.** Ordering does not prove native side effects committed, survived process death, or were not repeated by application retry logic.
4. **Plugin package support ≠ every runtime/build has the implementation.** Platform declarations, federated implementation selection, registration and exact build remain relevant.
5. **One plugin class ≠ one process-global lifetime.** Multiple Flutter engines can create independent plugin instances.
6. **Type-safe Dart wrapper ≠ type-safe raw native boundary.** Raw channel payload compatibility still depends on codec/schema agreement unless a stronger generated interface and validation are used.

## FAILURE MODEL
Representative failure classes:
- missing/unregistered platform implementation → `MissingPluginException`;
- native-declared failure → `PlatformException`;
- codec/schema/type disagreement → encode/decode/runtime type failure or semantically invalid result;
- channel-name collision → handlers/messages interfere;
- engine detach/recreation → stale instance/state assumption;
- multiple engines + static/global plugin state → cross-engine interference/resource lifetime bugs;
- platform implementation divergence → same app-facing API, materially different platform behavior;
- native API permission/lifecycle/thread constraint violation → platform-specific failure despite valid Dart call;
- retry after ambiguous native outcome → duplicate effect unless operation semantics make retry safe.

## EXECUTABLE VALIDATION
Fixture: `research/mobile/fixtures/M004_native_bridge_contract_lifetime.py`

Environment: Python 3.13.5 / Linux, 2026-09-18.

### CLAIM
A bridge that distinguishes missing implementation, contract mismatch and per-engine lifetime can reject states that an unsafe “missing means null/default” adapter silently accepts.

### ORACLE
Independent predicates require:
- registered `read` method;
- response schema version 1 with explicit `value`;
- detached engine instance must fail while a separate attached instance remains usable.

### OBSERVATION
The fixture passed success, missing-registration, contract-mismatch and independent engine-lifetime assertions. The deliberately unsafe adapter converted missing registration to `None`, demonstrating how an availability failure can be silently collapsed into an application value.

### VERDICT
**VALIDATION — PASS for the bounded reasoning model only.**

### EVIDENCE LIMIT
This is not Flutter/Dart/native execution evidence. It does not reproduce Flutter codecs, plugin registration, Android/iOS threads, platform permissions, Pigeon, real multi-engine embedding or native API behavior. Direct Flutter transfer remains OPEN because `dart` and `flutter` executables are unavailable in the current environment as rechecked 2026-09-18.

## ENGINEERING JUDGMENT
At an application boundary, normalize plugin outcomes into explicit domain states only when the product contract justifies that normalization. In particular, do not convert `MissingPluginException`, permission denial, unavailable capability, malformed reply and native operation failure into the same benign `null` unless they are genuinely semantically equivalent.

For correctness-sensitive effects, define operation identity and postcondition separately from transport/channel success. A Future completing successfully is not by itself evidence of durable application state.

Prefer a platform interface or generated interface when it materially reduces contract drift/test cost, but do not treat code generation as proof that platform semantics are equivalent.

## ALTERNATIVES
- Raw `MethodChannel`: low ceremony, flexible, but schema/type agreement is runtime-sensitive.
- Pigeon/generated interface: stronger generated cross-language contract; still requires platform implementation, lifecycle, semantic and native failure validation.
- Federated plugin interface: separates platform implementations and enables platform-specific evolution/testing; dependency/endorsement/registration must still be verified.
- Pure Dart implementation: avoids native channel boundary when the required capability is genuinely portable; cannot replace OS APIs that require native/browser platform authority.

## RELATED DOMAIN CHECK
- **Foundations:** F001/F005/F006 checked. Async completion and process/message boundaries do not imply semantic commit or durability. Direct Dart execution remains OPEN.
- **Architecture:** A003 checked conceptually. Plugin method names, payload schemas, errors and lifecycle expectations are interface contracts; platform divergence must not silently weaken them.
- **Mobile:** M001-M003 checked. Engine/process lifecycle, permissions and secure-storage properties remain separate from the channel mechanism.
- **Data:** D006 relevant when retrying ambiguous native effects; retry is not idempotency.
- **Quality:** Q001/Q002/Q006 relevant. Mocked plugin tests prove the mocked boundary, not native integration; real integration needs failure injection and semantic oracles.
- **Systems:** S001/S004/S005 relevant. Exact dependency/build/artifact determines which native implementation is actually packaged.
- **Design Studio:** checked global status 2026-09-18. Interaction semantics must not be collapsed because native integration exposes ambiguous/unavailable states; no Design canonical decision changed.
- **Web Manager:** checked status 2026-09-18. PWA/browser APIs are a different platform boundary; native plugin conclusions are not automatically transferred.
- **Marketing Manager:** checked status 2026-09-18; not materially relevant to this mechanism block.
- **Product source/ref:** no product audit performed; no MintTap/LogMate implementation claim is made.

## OPEN / VALIDATION / CHANGE WATCH
- **OPEN:** direct Dart/Flutter `MethodChannel` success/error/missing-plugin execution.
- **OPEN:** Pigeon vs raw-channel executable comparison.
- **OPEN:** Android/iOS plugin registration, permission, lifecycle and thread failure execution.
- **OPEN:** multiple Flutter-engine plugin-instance transfer validation.
- **OPEN:** exact product plugin inventory and integration contracts when a live product question requires audit.
- **CHANGE WATCH:** Flutter plugin registration, platform-channel/background-isolate behavior, federated-plugin tooling and platform APIs are version-sensitive.

## HANDOFFS
- **Architecture:** model plugin/native schemas, errors and lifecycle assumptions as explicit contracts rather than implementation details.
- **Quality:** future Flutter integration campaign should distinguish success, native error, missing plugin, malformed/type-mismatched reply, permission denial, engine detach/recreate and ambiguous retry outcome.
- **Systems:** bind plugin validation to exact dependency lock/build/artifact; source-level package presence does not prove native implementation packaging.
- **Data:** correctness-sensitive native writes require explicit effect identity/postcondition; channel completion is not durability evidence.
