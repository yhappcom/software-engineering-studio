# Research Index

Canonical reusable research is organized by specialist ownership: `research/foundations/` (`F###`), `research/architecture/` (`A###`), `research/mobile/` (`M###`), `research/data/` (`D###`), `research/quality/` (`Q###`), and `research/systems/` (`S###`).

## Current studies

### Foundations
- `F001` — `research/foundations/F001_program_execution_foundations.md` — **IN STUDY**; direct Dart JIT/AOT process/I/O transfer and first Flutter framework/test-binding execution are successful on hosted Linux; native/browser/product transfer remains OPEN.
- `F002` — base `research/foundations/F002_values_references_memory_lifetime.md` plus `research/foundations/F002_direct_dart_identity_resource_lifetime_transfer.md`; run `35455279567`, job `105929339080` validates direct Dart 3.13.3 identity/mutable-alias, `final`-binding versus object mutability, shallow nested aliasing, bounded explicit-copy isolation and explicit `dart:io` file-handle close. GC/finalizer timing, JIT/AOT equivalence and platform/product transfer remain OPEN.
- `F003` — initial integrated executable/model Foundation block complete; direct Dart structures/complexity, space cost and broader runtime/product transfer remain OPEN.
- `F004` — base concurrency/synchronization study plus `research/foundations/F004_direct_dart_isolate_transfer.md`; direct Dart 3.13.3 hosted execution validates isolate-owned mutable state through message requests and rejection of an explicitly unsendable `ReceivePort`; external-resource/native/browser/product transfer remains OPEN.
- `F005` — `research/foundations/F005_async_event_loop_futures_cancellation.md` — direct Dart 3.13.3 transfer validates the documented microtask→zero-delay-event relation, waiter-timeout ≠ source-cancellation, and API-specific StreamSubscription cancellation at bounded hosted-Linux scope.
- `F006` — base OS/socket/network study plus `research/foundations/F006_direct_dart_socket_transfer.md`; direct Dart loopback validation reproduces a fixture hang and falsifies the first close-order root-cause hypothesis. Run `35437455712` validates independent CI containment by terminating the fixture as a bounded failure; socket correctness and exact internal blocking phase remain OPEN.

### Architecture
- `A001`–`A003` — substantial Foundation blocks complete.
- `A005` — base study + repeated-change executable evidence + natural exact-ref LogMate evolution transfer; direct Flutter runtime and long-horizon product evolution OPEN.
- `A006` — evidence-preserving decisions + governance fixture; natural ADR-corpus validation OPEN.

### Mobile
- `M001`–`M006` — all planned Foundation boundaries have first professional/model evidence; M001 has first direct Flutter framework execution; native/browser/EFB transfer remains OPEN.

### Data
- `D001`–`D004` — Foundation studies initiated with executable/professional evidence.
- `D005` — recovery/process crash/storage faults/short-write/torn-image model + real WAL crash/checkpoint/main-file-copy + active-reader checkpoint progress + live Online Backup concurrency + interrupted candidate/publication evidence. Systems S006 separately validates directory-sync failure after rename visibility; physical power loss and mobile durability remain OPEN.
- `D006` — base sync + real TCP ambiguous retry + isolated kernel link interruption + LogMate inbound cursor atomicity transfer; actual LogMate persistence/Sync remains OPEN.

### Quality
- `Q001`–`Q005` — professional Foundation boundaries initiated; Q004 includes generated shrinking plus mutation/exhaustive-search evidence.
- `Q006` — model fault campaign plus real child-process crash/restart + SQLite persistent-state oracle discrimination; Dart/Flutter/mobile/backend/production transfer OPEN.

### Systems
- `S001`–`S003` — planned Foundation boundaries initiated with executable/professional evidence.
- `S004` — base dependency/supply-chain/build-system study + `research/systems/S004_logmate_lockfile_toolchain_transfer.md` + `research/systems/S004_logmate_lock_enforcement_execution.md`. Exact product-owned Flutter 3.38.7 project baseline and dependency-lock integrity transfer are validated; exact-ref `make build-pwa` path is recovered. Baseline source build/artifact identity remain OPEN because the Studio runner cannot currently acquire the separate private LogMate repository at execution time; prior build attempts fail before product source executes.
- `S005` — release-identity model + real OpenSSL asymmetric signature verification + bounded GCC/ld reproducibility + exact-ref LogMate build-identity transfer + real GitHub Actions attestation generation + one successful hosted retrieval/verification/negative identity run. Offline export and stronger authorization remain OPEN because later hosted baseline verification contradicted the earlier success and command-level root cause evidence is absent.
- `S006` — rollback/change-safety foundation plus directory-sync publication failure evidence; hard-power-loss and platform transfer OPEN.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS. Do not create files merely to count activity; prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record `repository → exact ref/tag/branch/commit → declared version if available → evidence date`. A product observation is not automatically reusable Studio truth; state mechanism and transfer limits.
