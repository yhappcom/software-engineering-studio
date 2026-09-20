# Research Index

Canonical reusable research is organized by specialist ownership: `research/foundations/` (`F###`), `research/architecture/` (`A###`), `research/mobile/` (`M###`), `research/data/` (`D###`), `research/quality/` (`Q###`), and `research/systems/` (`S###`).

## Current studies

### Foundations
- `F001` — direct Dart JIT/AOT, Flutter framework/test-binding execution, and host→Chrome bounded widget-oracle transfer validated; native/Safari/PWA/product/release transfer OPEN.
- `F002` — direct Dart identity/alias/final-binding/explicit-close transfer validated; GC/finalizer/platform/product transfer OPEN.
- `F003` — direct Dart queue representation/semantic transfer validated; broader algorithms/product performance OPEN.
- `F004` — direct Dart isolate ownership/message transfer validated; external-resource/platform/product transfer OPEN.
- `F005` — direct Dart async ordering, timeout/source-cancellation and subscription-cancellation boundaries validated.
- `F006` — `research/foundations/F006_process_liveness_phase_isolation.md`: semantic socket oracles PASS. Run `35486660067` isolates natural-exit failure to accepted connected-socket cases: server-only close and refused-connect exit; accepted-close and truncated-eof reach BODY_DONE then hang. Official `Socket.close()` send-side vs `destroy()` bidirectional semantics motivate a close-vs-destroy causal test at workflow head `d57d5531d9a5d96d21685d31e75bc2aaed051dd4`; terminal evidence/root cause pending.

### Architecture
- `A001`–`A003` — substantial Foundation blocks complete.
- `A005` — repeated-change executable evidence + natural exact-ref LogMate evolution transfer; runtime/long-horizon transfer OPEN.
- `A006` — evidence-preserving decisions + executable governance + natural LogMate decision-state transfer; natural ADR lifecycle OPEN.

### Mobile
- `M001`–`M005` — planned Foundation boundaries have professional/model evidence; M001 has direct Flutter framework execution.
- `M006` — exact Chromium same-session offline, restart persistence, update/controller transition and offline-before-navigation cold-start evidence; storage eviction/physical network loss, Safari/iPadOS/EFB, Flutter/LogMate artifact and production transfer OPEN.

### Data
- `D001`–`D004` — Foundation studies with executable/professional evidence.
- `D005` — recovery/process crash/storage faults/WAL/checkpoint/live Online Backup/interrupted candidate-publication evidence; physical power/mobile durability OPEN.
- `D006` — sync + real TCP ambiguous retry + isolated link interruption + LogMate inbound cursor atomicity transfer; actual LogMate persistence/Sync OPEN.

### Quality
- `Q001`–`Q005` — professional Foundation boundaries; Q004 includes mutation/exhaustive-search evidence.
- `Q006` — real child-process crash/restart + SQLite persistent-state oracle discrimination; mobile/backend/production transfer OPEN.

### Systems
- `S001`–`S003` — Foundation boundaries with executable/professional evidence.
- `S004` — exact product-owned Flutter 3.38.7 baseline and dependency-lock transfer; product `make build-pwa` path recovered; canonical source build/artifact identity remains dependent on source acquisition.
- `S005` — release identity + hosted attestation evidence; verifier contradiction retained.
- `S006` — rollback/change-safety + directory-sync publication failure evidence; hard-power-loss/platform transfer OPEN.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS. Do not create files merely to count activity; prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record `repository → exact ref/tag/branch/commit → declared version if available → evidence date`. A product observation is not automatically reusable Studio truth; state mechanism and transfer limits.
