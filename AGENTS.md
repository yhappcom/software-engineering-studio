# Software Engineering Studio Instructions

## Purpose

Software Engineering Studio is the canonical reusable engineering knowledge system for yhappcom. Chat history is temporary context; GitHub is long-term memory.

The Studio exists to improve real software decisions across products. It is not a product implementation repository, snippets archive, framework cookbook, or collection of fashionable patterns.

The long-term standard is professional engineering judgment: first-principles understanding, source literacy, executable verification, failure analysis, architecture reasoning, maintainability, production evidence, cross-domain collaboration, and explicit uncertainty.

## Product truth boundary

Product repositories are the source of truth for what a product actually implements. Never infer production behavior from Studio notes.

When inspecting a product repository, record at minimum:

`repository → exact ref/tag/branch/commit → declared product/app version when available → evidence date`.

Never assume the default branch is the current production implementation without evidence.

Project-specific implementation decisions remain in the product repository or project-specific case records. Promote a finding into Studio knowledge only when its mechanism, evidence strength, scope, and transfer limits are explicit.

## Specialist architecture

The Studio begins with six peer specialist tracks.

1. **Computer Science & Programming Foundations**
   - canonical research: `research/foundations/`
   - status: `progress/FOUNDATIONS_STATUS.md`
   - prefix: `F###`
   - owns computation/program execution models, data structures, algorithms, complexity, types, memory, processes/threads, concurrency foundations, OS/network fundamentals, and language-independent programming principles.

2. **Software Architecture & Design**
   - canonical research: `research/architecture/`
   - status: `progress/ARCHITECTURE_STATUS.md`
   - prefix: `A###`
   - owns decomposition, boundaries, abstraction, coupling/cohesion, dependency direction, modularity, interfaces/APIs, state ownership, architectural patterns, ADRs, refactoring, technical debt, and maintainability structure.

3. **Mobile & Cross-Platform Engineering**
   - canonical research: `research/mobile/`
   - status: `progress/MOBILE_STATUS.md`
   - prefix: `M###`
   - owns Flutter/Dart application engineering, Android/iOS lifecycle and platform constraints, native integration, permissions, app sandbox/storage behavior, background execution, packaging, and mobile/web/PWA boundary knowledge.

4. **Data, Persistence & Distributed Systems**
   - canonical research: `research/data/`
   - status: `progress/DATA_STATUS.md`
   - prefix: `D###`
   - owns data modeling, local persistence, schema evolution, migrations, transactions, caching, offline-first systems, synchronization, replication, conflict handling, backup/restore, import/export, distributed-system semantics, and data integrity.

5. **Quality, Testing & Reliability**
   - canonical research: `research/quality/`
   - status: `progress/QUALITY_STATUS.md`
   - prefix: `Q###`
   - owns testing strategy, unit/integration/system/e2e/property-based testing, deterministic verification, test doubles, debugging, fault injection, error/recovery behavior, crash analysis, regression prevention, observability, reliability methods, and release validation evidence.

6. **Systems, Security, Performance & Delivery**
   - canonical research: `research/systems/`
   - status: `progress/SYSTEMS_STATUS.md`
   - prefix: `S###`
   - owns security boundaries, secure storage, authentication/authorization engineering, secrets and supply chain, privacy engineering support, profiling, CPU/memory/I/O/network performance, startup/runtime efficiency, build systems, CI/CD, signing/versioning, release/rollback, and production delivery mechanics.

These are canonical ownership boundaries, not intellectual silos. Any specialist may study adjacent material when needed to understand or verify its own problem, but reusable canonical conclusions belong with the owning track.

AI-assisted engineering, Codex/agentic development, developer tooling, accessibility implementation, localization implementation, analytics instrumentation, and platform policy are initially cross-cutting concerns. They may become dedicated tracks later only when evidence shows a stable independent body of work.

## Shared maturity model

All tracks progress through five maturity stages:

1. **Foundation** — concepts, mechanisms, vocabulary, first-principles models.
2. **Intermediate Professional Practice** — ordinary implementation, comparison, debugging, trade-offs, failure modes.
3. **Advanced / Systems Practice** — interactions across runtime, architecture, data, concurrency, reliability, security, performance, and operations.
4. **Production & Authorship** — reproducible implementations, tests, tooling, release evidence, documented failures/revisions, reusable methods.
5. **Research & Advisory** — independent investigation, conflicting evidence synthesis, cross-context transfer, uncertainty management, and senior engineering advice.

Later work may expose a foundational gap; `REVISIT` is expected and is not failure.

## Evidence ladder

Reading alone never equals PASS.

Prefer the strongest valid evidence available. A typical engineering evidence ladder is:

`SOURCE → EXPLANATION/MODEL → WORKED EXAMPLE → EXECUTABLE TEST → FAILURE CASE → DEBUGGING/ROOT CAUSE → ALTERNATIVE IMPLEMENTATION → CROSS-PLATFORM/CONTEXT TRANSFER → LIVE PROJECT/PRODUCTION EVIDENCE`.

Not every question requires every rung, but a gate must state what evidence is sufficient and what remains unverified.

Distinguish:

- `SOURCE` — authoritative source explicitly establishes a fact;
- `SYNTHESIS` — transferable engineering conclusion inferred from evidence;
- `ENGINEERING JUDGMENT` — professional interpretation under stated assumptions;
- `PROJECT DECISION` — choice for a specific product/context;
- `OPEN` — unresolved question;
- `DEPENDENCY` — information/work needed from another track/team;
- `VALIDATION` — executable or real-world evidence still required;
- `CHANGE WATCH` — platform/toolchain/policy/version behavior requiring recheck;
- `REPLICATION` — deliberate independent reproduction;
- `CONTRADICTION` — conflicting evidence or failed assumption;
- `TRANSFER VALIDATION` — test that a finding survives a different language/platform/product/context.

## Start-of-work protocol

Before every substantial learning, design, audit, implementation experiment, or project-advisory block:

1. read `AGENTS.md`;
2. read `LEARNING_ROADMAP.md`;
3. read `progress/STATUS.md`;
4. read all six specialist status files;
5. inspect relevant Studio research;
6. inspect related `yhappcom/design-studio`, `yhappcom/web-manager`, and `yhappcom/marketing-manager` evidence when materially relevant;
7. inspect the relevant product repository/ref when the question depends on actual product behavior;
8. identify known facts, assumptions, unknowns, dependencies, and validation needs;
9. decide whether existing evidence should be reused, replicated, challenged, extended, or transfer-tested;
10. choose the smallest coherent work block that materially improves engineering capability or a live project decision.

## RELATED DOMAIN CHECK

Every substantial research note should record, when relevant:

- Foundations evidence checked;
- Architecture evidence checked;
- Mobile evidence checked;
- Data evidence checked;
- Quality evidence checked;
- Systems/Security/Performance/Delivery evidence checked;
- Design Studio evidence checked;
- Web Manager evidence checked;
- Marketing Manager evidence checked;
- product source/ref checked;
- reusable findings, contradictions, dependencies, transfer risks, and planned handoffs.

`Not materially relevant` is acceptable only after considering whether that domain could change the conclusion.

## Cross-repository collaboration boundaries

### Design Studio ↔ Engineering Studio

Design Studio owns reusable visual, interaction, typography, color, layout, web-design, and content-design expertise. Engineering Studio owns executable implementation mechanics, architecture, correctness, platform behavior, performance/security/reliability evidence, and feasibility constraints.

Engineering must not silently redefine a design state/semantic contract merely because an implementation is easier. When implementation evidence limits or contradicts a design assumption, preserve the evidence and hand it back.

### Web Manager ↔ Engineering Studio

Web Manager owns company website strategy, information/content architecture, website operations, discovery/SEO, and web-management decisions. Engineering owns reusable implementation/runtime/security/performance/build knowledge and executable technical evidence.

Shared areas such as web architecture, performance, security, deployment, analytics, and PWA/browser behavior require explicit ownership of the decision being made rather than duplicate canonical truth.

### Marketing Manager ↔ Engineering Studio

Marketing owns audience, value proposition, acquisition/activation/retention/monetization intent, experiment interpretation, and marketing measurement decisions. Engineering owns instrumentation feasibility, event implementation, ad SDK/runtime behavior, performance/reliability impact, privacy/security mechanics, and code-level observability.

Engineering must not optimize ad impressions, analytics volume, or experiment instrumentation in isolation from product/marketing guardrails.

### Product repositories ↔ Engineering Studio

Product repositories own implementation truth. Engineering Studio may audit, test, compare, or advise but does not rewrite product truth inside Studio notes.

Reusable engineering findings discovered in product work are recorded here with the exact source ref and transfer limits.

## Handoffs

After substantial work, add `## HANDOFFS` when another track/repository can materially use the result.

A handoff should state:

- what changed or was learned;
- canonical Studio file/section;
- source/product ref and evidence date when applicable;
- whether the result confirms, limits, contradicts, or transfer-tests prior evidence;
- scope limits and remaining validation;
- concrete action or question for the receiving team.

Do not edit another repository's canonical files unless explicitly authorized for that task.

## Concurrency and writing boundaries

Ordinary specialist writes are constrained to reduce collisions:

- Foundations → `research/foundations/`, `progress/FOUNDATIONS_STATUS.md`
- Architecture → `research/architecture/`, `progress/ARCHITECTURE_STATUS.md`
- Mobile → `research/mobile/`, `progress/MOBILE_STATUS.md`
- Data → `research/data/`, `progress/DATA_STATUS.md`
- Quality → `research/quality/`, `progress/QUALITY_STATUS.md`
- Systems → `research/systems/`, `progress/SYSTEMS_STATUS.md`

Coordinator/governance owns:

- `AGENTS.md`
- `LEARNING_ROADMAP.md`
- `progress/STATUS.md`
- `research/README.md`
- `methods/`
- `coordination/`

Specialists do not move, delete, rename, or renumber existing canonical research during ordinary learning.

## Balance principle

Do not allocate study time evenly merely for symmetry. Select work according to:

1. foundational gaps that block later correctness;
2. live MintTap/LogMate/future-project dependencies;
3. evidence maturity and missing executable validation;
4. cross-track bottlenecks;
5. high-risk unknowns in correctness, data loss, security, reliability, or release behavior;
6. reusable value across products.

A balance loop may intentionally keep one track quiet while another closes a prerequisite.

## Depth and cadence rule

Learn more deeply than you report. Avoid one-file-per-term microlearning.

Preferred sequence for a major engineering topic:

`history/problem → first-principles mechanism → abstraction/model → authoritative specification/docs → representative implementation → failure modes → executable verification → debugging/root cause → alternatives/trade-offs → cross-domain effects → project transfer → integrated competency`.

Persist at coherent professional-topic boundaries.

## Project mode

Live project needs take priority over nonessential curriculum expansion, but urgency does not justify guessing or skipping a prerequisite that materially affects safety, correctness, data integrity, security, or reliability.

Expected project output normally includes:

- verified product/ref context;
- problem diagnosis;
- constraints and assumptions;
- viable alternatives;
- engineering recommendation and trade-offs;
- architecture/data/mobile/quality/security/performance implications as relevant;
- executable validation plan;
- rollback/recovery considerations when relevant;
- cross-team dependencies and handoffs;
- explicit unknowns.

## Persistence and continuity

After every substantial integrated work block:

1. save reusable evidence in the correct canonical area;
2. update the owning specialist status;
3. update OPEN/VALIDATION/CHANGE WATCH items;
4. record dependencies and handoffs;
5. update `progress/STATUS.md` when the global queue or maturity picture materially changes;
6. commit before moving to a materially different block when practical.

Research volume, commit count, or code volume is not the success metric. The measure is whether the Studio can explain, implement, break, debug, compare, validate, transfer, and defend engineering decisions in real products.
