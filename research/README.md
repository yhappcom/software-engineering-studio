# Research Index

Canonical reusable research is organized by specialist ownership: `research/foundations/` (`F###`), `research/architecture/` (`A###`), `research/mobile/` (`M###`), `research/data/` (`D###`), `research/quality/` (`Q###`), and `research/systems/` (`S###`).

## Current studies

### Foundations
- `F001` — `research/foundations/F001_program_execution_foundations.md` — **IN STUDY**; direct Dart JIT/AOT process/I/O transfer and first Flutter framework/test-binding execution are successful on hosted Linux; native/browser/product transfer remains OPEN.
- `F004` — base concurrency/synchronization study plus `research/foundations/F004_direct_dart_isolate_transfer.md`; direct Dart 3.13.3 hosted execution now validates isolate-owned mutable state through message requests and rejection of an explicitly unsendable `ReceivePort`; external-resource/native/browser/product transfer remains OPEN.
- `F005` — `research/foundations/F005_async_event_loop_futures_cancellation.md` — direct Dart 3.13.3 transfer validates the documented microtask→zero-delay-event relation, waiter-timeout ≠ source-cancellation, and API-specific StreamSubscription cancellation at bounded hosted-Linux scope.
- `F002`, `F003`, `F006` — initial integrated executable/model Foundation blocks complete; direct Dart/runtime transfer remains selectively OPEN; see `progress/FOUNDATIONS_STATUS.md`.

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
- `S004` — base dependency/supply-chain/build-system study plus `research/systems/S004_logmate_lockfile_toolchain_transfer.md`: exact-ref LogMate transfer confirms committed package versions/content hashes while exact Flutter SDK/engine identity remains unbound in inspected repository evidence; canonical product Dart/pub/build execution OPEN.
- `S005` — release-identity model + real OpenSSL asymmetric signature verification + bounded GCC/ld reproducibility + exact-ref LogMate build-identity transfer + real GitHub Actions attestation generation + one successful hosted retrieval/verification/negative identity run. Offline export and stronger authorization remain OPEN because later hosted baseline verification contradicted the earlier success and command-level root cause evidence is absent.
- `S006` — rollback/change-safety foundation plus directory-sync publication failure evidence; hard-power-loss and platform transfer remain OPEN.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS. Do not create files merely to count activity; prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record `repository → exact ref/tag/branch/commit → declared version if available → evidence date`. A product observation is not automatically reusable Studio truth; state mechanism and transfer limits.
