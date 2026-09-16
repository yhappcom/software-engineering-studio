# Software Engineering Studio — Beginner-to-Research/Advisory Roadmap

Status: **ACTIVE CURRICULUM**
Established: 2026-09-16

## Purpose

Build professional software engineering capability from first principles to production and research/advisory judgment. The roadmap is shared by six specialist tracks and is intentionally deeper than framework tutorials.

The Studio progresses through five maturity stages. A later stage can reopen earlier material when a gap is discovered.

---

# Stage 1 — Foundation

Goal: understand what programs, data, execution, state, interfaces, failures, and platforms actually are before optimizing frameworks.

## Foundations track
- computation and program execution model;
- source code → compiler/interpreter/runtime concepts;
- values, variables, control flow, functions, types;
- memory, stack/heap/reference/value concepts;
- data structures and algorithmic complexity;
- processes, threads, scheduling, synchronization;
- asynchronous execution and concurrency fundamentals;
- files, sockets, processes, OS boundaries;
- networking fundamentals from process-to-process communication upward.

## Architecture track
- abstraction and information hiding;
- cohesion, coupling and dependency direction;
- modules, packages, layers and boundaries;
- interfaces/contracts and invariants;
- state ownership and lifecycle;
- decomposition by responsibility/change pressure;
- architecture vs design vs implementation;
- refactoring and technical-debt fundamentals.

## Mobile track
- Dart/Flutter execution model at conceptual level;
- widget/render/state concepts without framework cargo culting;
- Android/iOS application lifecycle;
- app sandbox, files, permissions and process death;
- foreground/background constraints;
- package/plugin/native boundary;
- mobile web/PWA/native conceptual boundaries.

## Data track
- data modeling and invariants;
- serialization and representation;
- local persistence basics;
- database/index/transaction fundamentals;
- schema versioning and migration concepts;
- cache vs source of truth;
- backup/restore fundamentals;
- distributed systems vocabulary: replication, latency, partitions, consistency, conflict.

## Quality track
- correctness and specification;
- test levels and their purposes;
- deterministic vs nondeterministic behavior;
- assertions/invariants/oracles;
- debugging from symptom to cause;
- error classification and recovery;
- observability fundamentals;
- regression and reproducibility.

## Systems track
- trust boundaries and least privilege;
- threat-model fundamentals;
- secure storage/secrets concepts;
- CPU/memory/I/O/network cost models;
- profiling/measurement basics;
- build artifact and dependency concepts;
- versioning, signing, release, rollback fundamentals;
- CI/CD as controlled evidence-producing pipelines.

### Stage 1 gate
A specialist must explain the mechanism from first principles, produce representative executable examples where appropriate, demonstrate at least one failure mode, and identify ownership boundaries with adjacent tracks. Reading summaries alone do not pass.

---

# Stage 2 — Intermediate Professional Practice

Goal: reliably build and diagnose ordinary real applications.

Cross-track themes:
- idiomatic Dart/Flutter and representative second-language comparison where useful;
- API/interface design and versioning;
- state management alternatives and trade-offs;
- dependency injection without pattern worship;
- repository/service/domain boundaries where justified;
- SQLite/local database practice;
- Firestore/Firebase semantics and offline behavior;
- schema migration execution and recovery;
- import/export pipelines and validation;
- network clients, retries, timeout and idempotency;
- unit/integration/widget/e2e test strategy;
- crash/error diagnostics;
- secure local data and platform permission handling;
- performance profiling;
- build/release automation;
- code review and maintainability heuristics;
- accessibility/localization implementation dependencies from Design Studio.

### Stage 2 gate
Evidence must include executable implementation, representative failure/debugging evidence, alternative comparison, and at least one realistic project transfer exercise.

---

# Stage 3 — Advanced / Systems Practice

Goal: reason across component boundaries and under partial failure.

Themes:
- concurrency, races, deadlocks, cancellation and backpressure;
- event-driven and asynchronous architectures;
- transaction boundaries and distributed consistency;
- offline-first architecture;
- multi-device synchronization;
- conflict detection/resolution and merge semantics;
- idempotency and exactly/at-least/at-most-once distinctions;
- local-first/distributed data ownership;
- resilient networking and partial connectivity;
- background execution constraints across mobile platforms;
- performance architecture and resource budgets;
- security architecture and attack-surface reduction;
- privacy engineering and data minimization;
- observability across async/distributed flows;
- fault injection and chaos-style bounded validation;
- large-codebase modularity and evolutionary architecture;
- migration/replatforming under compatibility constraints.

### Stage 3 gate
A PASS requires system-level failure analysis, cross-track review, executable fault/edge validation where feasible, explicit recovery semantics, and transfer testing across at least two materially different contexts or architectures.

---

# Stage 4 — Production & Authorship

Goal: produce reliable reusable engineering systems rather than only understand them.

Themes:
- production-quality libraries/components/tools;
- automated validation harnesses;
- reproducible build/release pipelines;
- architecture decision records and revision history;
- migration/rollback tooling;
- telemetry and operational diagnostics;
- incident analysis and postmortems;
- performance/security/reliability release gates;
- platform/version compatibility matrices;
- dependency and supply-chain governance;
- reusable project bootstrap and engineering playbooks;
- evidence-preserving code review/release governance.

### Stage 4 gate
Work must survive independent execution/review, preserve failure→revision evidence, include operational constraints and rollback/recovery, and be demonstrably reusable beyond a single happy-path demo.

---

# Stage 5 — Research & Advisory

Goal: independently investigate ambiguous engineering problems and advise across products under uncertainty.

Themes:
- primary-source and standards analysis;
- independent reproduction of platform/runtime behavior;
- comparative architecture research;
- performance/security/reliability experiments;
- contradictory evidence reconciliation;
- technology adoption and migration decisions;
- build-vs-buy and dependency-risk analysis;
- total cost of ownership and maintenance economics;
- long-horizon technical-debt strategy;
- cross-product platform strategy;
- engineering governance and capability design;
- publication-quality technical argument with explicit boundary conditions.

### Stage 5 gate
The specialist must formulate the problem, select defensible methods, generate or reproduce evidence, critique alternatives, state uncertainty and transfer limits, and improve a real strategic or technical decision without relying on authority-by-confidence.

---

# Initial priority program

The Studio starts broad enough to avoid premature specialization, but current yhappcom products create legitimate early priorities.

1. **Execution & programming foundations** — shared prerequisite.
2. **State, persistence and correctness** — critical for both MintTap and LogMate.
3. **Flutter/mobile runtime** — current product platform priority.
4. **Architecture and testability** — prevents framework-driven accumulation.
5. **Offline-first, backup/restore, import/export** — especially relevant to LogMate.
6. **Networking and synchronization** — including device-to-device and server-mediated models without assuming one solution.
7. **Security/privacy and data integrity**.
8. **Performance and resource behavior**.
9. **Build/release/CI/CD and production operations**.
10. **Advanced distributed/local-first systems and cross-product platform strategy**.

Live project needs may reorder these, but a prerequisite cannot be skipped when it materially affects correctness or reliability.

# Cross-cutting collaboration

- `yhappcom/design-studio` supplies reusable design/interaction/content evidence; Engineering validates executable behavior and returns implementation constraints.
- `yhappcom/web-manager` supplies website/product-web requirements and operational context; Engineering supplies reusable runtime/architecture/security/performance evidence.
- `yhappcom/marketing-manager` supplies measurement/activation/ad/experiment intent; Engineering validates instrumentation and runtime impact.
- product repositories supply actual implementation truth.

# Study method

For substantial topics, prefer:

`history/problem → first-principles mechanism → model → primary docs/spec → implementation → failure → executable validation → debugging → alternatives → cross-track review → project transfer → competency gate`.

The curriculum is not measured by file count. It is measured by the ability to explain, implement, break, debug, compare, validate, recover, and advise.
