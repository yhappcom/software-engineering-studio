# Research Index

Canonical reusable research is organized by specialist ownership: `research/foundations/` (`F###`), `research/architecture/` (`A###`), `research/mobile/` (`M###`), `research/data/` (`D###`), `research/quality/` (`Q###`), and `research/systems/` (`S###`).

## Current studies

### Foundations
- `F001` — direct Dart JIT/AOT, Flutter framework/test-binding execution, and `research/foundations/F001_flutter_chrome_runtime_transfer.md`: same bounded Flutter widget oracle validated on host and Chrome target at exact workflow head `b547c5d...`, run `35478966848`; native/Safari/PWA/product/release transfer remains OPEN.
- `F002` — direct Dart identity/alias/final-binding/explicit-close transfer validated; GC/finalizer/platform/product transfer OPEN.
- `F003` — direct Dart List front-removal versus `ListQueue.removeFirst()` semantic/representation transfer validated; timing is diagnostic only; broader algorithms/product performance OPEN.
- `F004` — direct Dart isolate-owned mutable state/message transfer validated; external-resource/platform/product transfer OPEN.
- `F005` — direct Dart async ordering, waiter-timeout/source-cancellation and subscription-cancellation boundaries validated.
- `F006` — loopback fixture hang reproduced, first root-cause hypothesis falsified and outer CI containment validated; socket verdict/root cause OPEN.

### Architecture
- `A001`–`A003` — substantial Foundation blocks complete.
- `A005` — repeated-change executable evidence + natural exact-ref LogMate evolution transfer; runtime/long-horizon transfer OPEN.
- `A006` — evidence-preserving decisions + executable governance fixture + `research/architecture/A006_logmate_natural_decision_state_transfer.md`. Natural LogMate history validates separate decision vs implementation/evidence states without relabeling the product master as an ADR corpus; natural ADR lifecycle and long-horizon supersession remain OPEN.

### Mobile
- `M001`–`M005` — planned Foundation boundaries have professional/model evidence; M001 has first direct Flutter framework execution.
- `M006` — `research/mobile/M006_real_browser_service_worker_transfer.md` contains four exact-Chromium evidence classes: same-session controlled-cache offline, browser-restart/persistent-profile persistence, service-worker update/waiting/activation/client-controller transition, and second-process offline-before-navigation cold start. Run `35473544016` establishes exact Chromium `140.0.7339.16` / Playwright build `v1187`. Storage eviction/physical network loss, Safari/iPadOS/EFB, Flutter/LogMate artifact and production transfer remain OPEN.

### Data
- `D001`–`D004` — Foundation studies initiated with executable/professional evidence.
- `D005` — recovery/process crash/storage faults/WAL/checkpoint/live Online Backup/interrupted candidate-publication evidence; physical power loss/mobile durability OPEN.
- `D006` — sync + real TCP ambiguous retry + isolated link interruption + LogMate inbound cursor atomicity transfer; actual LogMate persistence/Sync OPEN.

### Quality
- `Q001`–`Q005` — professional Foundation boundaries initiated; Q004 includes generated shrinking plus mutation/exhaustive-search evidence.
- `Q006` — real child-process crash/restart + SQLite persistent-state oracle discrimination; mobile/backend/production transfer OPEN.

### Systems
- `S001`–`S003` — planned Foundation boundaries initiated with executable/professional evidence.
- `S004` — exact product-owned Flutter 3.38.7 project baseline and dependency-lock integrity transfer validated; exact-ref `make build-pwa` path recovered. Baseline source build/artifact identity OPEN because Studio runner cannot acquire separate private LogMate repository at execution time.
- `S005` — release identity + hosted attestation evidence; later verifier contradiction retained; stronger/offline verification OPEN.
- `S006` — rollback/change-safety + directory-sync publication failure evidence; hard-power-loss/platform transfer OPEN.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS. Do not create files merely to count activity; prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record `repository → exact ref/tag/branch/commit → declared version if available → evidence date`. A product observation is not automatically reusable Studio truth; state mechanism and transfer limits.
