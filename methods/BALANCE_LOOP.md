# Software Engineering Studio Balance Loop

## Purpose

Choose the highest-value next learning block without creating six independent shallow streams.

## Required inputs on every run

Read:

1. `AGENTS.md`
2. `LEARNING_ROADMAP.md`
3. `progress/STATUS.md`
4. all six specialist status files
5. recent relevant Studio research and commits
6. relevant Design Studio / Web Manager / Marketing Manager status or research when the candidate topic crosses those boundaries
7. relevant product repository/ref when a live product dependency is involved.

## Selection criteria

Compare candidate work by:

1. **Prerequisite severity** — does a missing basic mechanism make later work unreliable?
2. **Product leverage** — does MintTap, LogMate, or another live project need it now?
3. **Evidence gap** — is knowledge based only on reading when executable/failure evidence is needed?
4. **Risk** — could misunderstanding cause data loss, financial/correctness defects, security/privacy failure, unrecoverable migration, release failure, or major performance/reliability harm?
5. **Cross-track leverage** — will the work unblock multiple specialists?
6. **Reuse value** — is the result transferable across products?
7. **Change urgency** — is a platform/toolchain fact volatile enough to require current verification?

Do not use equal-time rotation as the default.

## Work-block shape

A normal hourly run selects **one coherent primary block**, with one lead specialist and only the supporting specialists materially needed.

Example:

`D006 synchronization semantics`
- lead: Data
- support: Foundations for concurrency/network semantics
- Mobile for lifecycle/connectivity constraints
- Quality for fault/conflict validation
- Systems for security/resource implications

## Depth rule

Do not split one concept into many microfiles merely because the schedule is hourly. An hourly run may continue the same study if its professional boundary is not yet complete.

A run should leave one of these states:

- meaningful integrated research persisted;
- executable validation added;
- contradiction/failure resolved or sharpened;
- project transfer performed;
- gate evidence advanced;
- or an explicit finding that no trustworthy progress is possible without a dependency.

## Reporting rule

Report only meaningful new findings, validation results, changed status/gates, cross-repo handoffs, and next target. Do not report routine file reads or repeat previously established facts.

## Persistence rule

Before changing to a materially different topic:

- update the owning specialist status;
- update global `progress/STATUS.md` if maturity/queue changed;
- index canonical research when needed;
- preserve OPEN/VALIDATION/CHANGE WATCH and handoffs;
- commit evidence.
