# Mobile Specialist Status

Track: Mobile & Cross-Platform Engineering
Prefix: `M###`
State: **Stage 1 — READY / NOT YET PASSED**
Last sync: 2026-09-16

## Mission
Build deep Flutter/Dart and mobile-platform engineering capability while preserving the distinction between framework behavior, Android/iOS platform behavior, and cross-platform abstractions.

## Initial queue
- `M001` — Dart/Flutter runtime model, widget/render/state pipeline, app lifecycle and platform boundary.
- `M002` — Android/iOS process lifecycle, termination, background execution and resume semantics.
- `M003` — App sandbox, files, permissions, secure storage and platform APIs.
- `M004` — Plugins/platform channels/native integration and failure boundaries.
- `M005` — Cross-platform architecture, portability and platform divergence.
- `M006` — Native app vs PWA/web boundary and mobile deployment constraints.

## Gate requirement
Foundation PASS requires official platform/framework evidence, executable validation on representative environments where feasible, failure/resume/process-death cases, and explicit Android/iOS differences rather than assuming Flutter erases them.

## Dependencies / handoffs
- Foundations supplies runtime/concurrency models.
- Architecture supplies state/dependency structure.
- Data supplies persistence/offline behavior.
- Quality supplies lifecycle/failure test strategy.
- Systems supplies security/performance/build/release constraints.
- Design Studio supplies interaction/accessibility/content requirements for implementation transfer.

## Current product relevance
MintTap and LogMate make this an early high-priority track, but product-specific claims require exact repository refs and versions.

## Next work
`M001` after the first execution-model foundation, or jointly where executable Flutter evidence improves F001.
