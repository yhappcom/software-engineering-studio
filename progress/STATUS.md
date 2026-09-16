# Software Engineering Studio Global Status

Operating state: **ACTIVE — INITIALIZED / FOUNDATION ENTRY**
Governance sync: 2026-09-16
Canonical curriculum: `LEARNING_ROADMAP.md`

## Mission

Build reusable software-engineering capability that improves real yhappcom product decisions through first-principles understanding, executable verification, failure analysis, and cross-repository collaboration.

GitHub is canonical memory; chat is temporary context.

## Specialist map

| Specialist | Canonical research | Status | Prefix | Current state |
| --- | --- | --- | --- | --- |
| Computer Science & Programming Foundations | `research/foundations/` | `progress/FOUNDATIONS_STATUS.md` | `F###` | Stage 1 READY |
| Software Architecture & Design | `research/architecture/` | `progress/ARCHITECTURE_STATUS.md` | `A###` | Stage 1 READY |
| Mobile & Cross-Platform Engineering | `research/mobile/` | `progress/MOBILE_STATUS.md` | `M###` | Stage 1 READY |
| Data, Persistence & Distributed Systems | `research/data/` | `progress/DATA_STATUS.md` | `D###` | Stage 1 READY |
| Quality, Testing & Reliability | `research/quality/` | `progress/QUALITY_STATUS.md` | `Q###` | Stage 1 READY |
| Systems, Security, Performance & Delivery | `research/systems/` | `progress/SYSTEMS_STATUS.md` | `S###` | Stage 1 READY |

No specialist has passed Foundation yet. Repository initialization is governance evidence, not domain competency evidence.

## Initial integrated learning queue

The first cycle is intentionally cross-specialist rather than six isolated streams.

1. **F001 — Program execution from source to running process/runtime** — lead: Foundations; supporting checks: Mobile, Systems, Quality.
2. **D001 — State, persistence, durability and source-of-truth fundamentals** — lead: Data; supporting checks: Architecture, Quality, Mobile.
3. **M001 — Flutter/Dart runtime and mobile application lifecycle foundations** — lead: Mobile; supporting checks: Foundations, Systems.
4. **A001 — Boundaries, state ownership, coupling/cohesion and change pressure** — lead: Architecture; supporting checks: Data, Quality, Mobile.
5. **Q001 — Correctness, specification, test oracle and reproducibility foundations** — lead: Quality; supporting checks: all tracks.
6. **S001 — Trust/resource/build boundaries: security, performance and delivery foundations** — lead: Systems; supporting checks: Foundations, Mobile, Quality.

The balance loop may reorder these when a prerequisite or live project dependency is stronger.

## Current product-relevance map

### MintTap
Potential future transfer areas include Flutter architecture, Firebase/Firestore behavior, analytics/ad instrumentation, calculation correctness, persistence/data integrity, release/version auditing, performance, privacy/security, and regression validation. Actual conclusions require an exact product repository ref/version.

### LogMate
Potential future transfer areas include offline-first persistence, import pipelines, backup/restore, multi-device synchronization, platform constraints, data integrity, conflict handling, Flutter/mobile lifecycle, and testability. Do not assume a synchronization mechanism until platform/runtime evidence is validated.

## Cross-repository operating state

- `yhappcom/design-studio` — collaboration boundary defined; Design owns reusable design semantics, Engineering owns executable mechanics/constraints.
- `yhappcom/web-manager` — collaboration boundary defined; Web Manager owns site strategy/operations decisions, Engineering owns reusable implementation/runtime evidence.
- `yhappcom/marketing-manager` — collaboration boundary defined; Marketing owns growth/measurement intent, Engineering owns instrumentation/runtime feasibility and impact.
- Product repositories — implementation source of truth; exact ref/version required for audits.

Canonical coordination details: `coordination/CROSS_REPO_COLLABORATION.md`.

## Evidence rule

No PASS from reading alone. Expected progression where applicable:

`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.

## Hourly learning behavior

The recurring learning loop should:

1. read current governance/status and recent commits;
2. compare all six tracks by prerequisite gap, live-project value, and missing executable evidence;
3. select one coherent high-value block rather than six microtasks;
4. involve adjacent tracks through RELATED DOMAIN CHECK;
5. use authoritative/current sources when needed;
6. execute validation where reading cannot establish the material claim;
7. persist reusable evidence and update owning status/global status when materially changed;
8. report only meaningful new findings and repository updates.

## Current next action

Begin **F001 — Program Execution Foundations** unless a stronger live-project dependency appears before the first scheduled run.
