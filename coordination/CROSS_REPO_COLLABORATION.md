# Cross-Repository Collaboration Contract

## Purpose

Prevent duplicated or contradictory canonical truth while allowing active cross-team validation among:

- `yhappcom/software-engineering-studio`
- `yhappcom/design-studio`
- `yhappcom/web-manager`
- `yhappcom/marketing-manager`
- product repositories such as MintTap and LogMate.

## Canonical ownership rule

A repository owns the reusable truth of its discipline; product repositories own actual implementation truth.

Cross-team work should **reference, test, constrain, or hand back** evidence rather than silently copying and diverging it.

## Engineering ↔ Design Studio

### Design Studio owns
- visual and interaction design expertise;
- typography, color, layout/spatial systems;
- interaction/state/recovery design semantics;
- web design expertise;
- content design/UX writing semantics.

### Engineering Studio owns
- executable implementation mechanics;
- code/data/runtime architecture;
- platform constraints and integration behavior;
- correctness, testing and reliability;
- security/performance/build/release evidence.

### Shared workflow
1. retrieve the design contract and exact relevant study/status;
2. identify implementation assumptions;
3. implement or validate without redefining semantics for convenience;
4. return measured constraints, contradictions, or transfer failures;
5. keep reusable design conclusions in Design Studio and reusable engineering conclusions here.

## Engineering ↔ Web Manager

### Web Manager owns
- company/product website strategy;
- information/content architecture and visitor journeys;
- SEO/discovery and site-level governance;
- website operational decisions and requirements.

### Engineering Studio owns
- reusable browser/runtime/network implementation knowledge;
- code architecture and integration mechanics;
- web security/performance/build/deployment technical evidence;
- executable validation methods.

For overlap such as PWA, hosting, analytics, browser behavior, performance, security, or release operations, state **which decision** is being made and which repository owns that decision. Link rather than duplicate canonical material.

## Engineering ↔ Marketing Manager

### Marketing owns
- audience/market/value proposition;
- acquisition, activation, retention and monetization intent;
- experiment/business interpretation;
- marketing measurement definitions and guardrails.

### Engineering owns
- analytics/ad SDK implementation;
- event emission semantics at code/runtime level;
- instrumentation feasibility and data-flow constraints;
- performance/reliability/privacy/security consequences;
- technical validation of experiment implementation.

Marketing metrics do not override product correctness or user safety. Engineering metrics do not redefine business success.

## Engineering ↔ Product repositories

Product repositories are authoritative for actual product behavior.

Before claiming a product implements or lacks a behavior, capture:

`repo → exact ref/tag/branch/commit → declared version → evidence date`.

If the production ref is unknown, say so. Never equate default branch with production without evidence.

Project-specific code changes belong in product repositories. Studio research may contain bounded experimental code or fixtures only when their purpose is reusable learning/validation.

## Handoff record

A meaningful cross-repo handoff should contain:

- **FROM / TO**
- **decision/problem**
- **canonical source**
- **product/ref/version** if applicable
- **finding**
- **evidence level**
- **impact on receiver**
- **scope/limitations**
- **requested action or validation**
- **status**: OPEN / ACKNOWLEDGED / VALIDATED / SUPERSEDED

## Conflict protocol

When repositories appear to disagree:

1. do not overwrite either conclusion;
2. verify dates, versions, definitions, scope, platform and product ref;
3. distinguish semantic/design requirement from implementation observation;
4. reproduce the disputed behavior where feasible;
5. record `CONTRADICTION` explicitly;
6. identify the canonical owner of the disputed claim;
7. hand evidence back to that owner for resolution.

## Change-watch protocol

Platform SDK behavior, OS restrictions, Flutter/Dart behavior, browser behavior, app-store requirements, Firebase/Google Mobile Ads APIs, security recommendations, and similar volatile facts must include version/date context and `CHANGE WATCH` when operational advice depends on them.

## No silent dependency

If engineering work depends materially on a design, marketing, web, legal/policy, or product decision that is unknown, record it as a `DEPENDENCY`. Do not invent the missing decision to keep implementation moving.
