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

## Run provenance, materiality and visibility

Scheduled executions must keep **five independent evidence gates**: enabled schedule; actual run/status; correctly bound latest result (same run ID and attempt time); independently verified new execution/source/commit evidence; user notification or delivery acknowledgement when available. A Git commit is **not** mandatory proof of a successful no-delta run, and an enabled schedule is **not** evidence of actual execution. A published chat result does not prove a user saw a notification. Do not infer delivery from an unknown delivery status or claim continuous hourly liveness from a single latest run. See `research/quality/Q005_scheduled_research_run_evidence_and_nonpublication_2026-11-08.md`.

If product refs and previously studied OPEN risks have not changed, do **not** end a substantive study cycle with repeated inventory alone. After a bounded fresh-state check, advance a genuinely independent prerequisite using executable tests/negative controls when safe; otherwise perform a nonduplicative official-source/alternative/root-cause investigation or state the precise blocking dependency. Preserve real evidence and avoid fabricated PASS or filler commits. For public Studio, **never copy private product source, user ledger, credentials or private test artifacts** into public Actions or research files. Do not silently trigger private product CI. The hourly cadence can continue even if one cycle legitimately has no publishable delta.

