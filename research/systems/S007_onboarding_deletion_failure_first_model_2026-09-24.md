# S007 — Onboarding + Deletion Failure-First Executable Model

Status: **VALIDATION PENDING — workflow queued; no PASS awarded**  
Owner: Systems / Security / Identity  
Evidence date: 2026-09-24

## Problem
The integrated LogMate Auth/Onboarding contract now has stable project decisions, but exact LogMate implementation remains absent. The highest-value independent next rung is therefore an executable semantic oracle that makes the new three-path onboarding and full-deletion invariants falsifiable before product transfer.

## PROJECT DECISION inputs
Canonical decision input: `S007_logmate_auth_onboarding_integrated_product_contract_2026-09-24.md`.

The model encodes only these approved semantics: Firebase UID is owner authority; fresh authenticated matching owners require explicit setup selection/completion; initial setup is one of new-logbook / Previous Total / Import; data presence does not imply onboarding completion; owner mismatch fails closed; voluntary deletion immediately locks normal access; deletion requires same-UID reauthentication; identity absence is not proof of erasure; local data must be erased before terminal completion; a durable deletion marker prevents post-crash stale-ledger exposure.

## EXECUTABLE TEST
Fixture: `research/systems/fixtures/S007_onboarding_deletion_state_model.py`.

Nine failure-first tests cover:
1. all three setup methods remain onboarding until explicit completion;
2. local/remote data presence cannot infer completion;
3. UID/owner mismatch routes to recovery and rejects setup mutation;
4. the selected initial setup method cannot silently change;
5. deletion confirmation immediately routes away from Home;
6. deletion reauthentication must return the same UID;
7. Firebase/session identity absence after identity deletion remains deletion-locked and is not first use;
8. terminal deletion requires local and remote erasure plus owner removal;
9. reconstructed crash/restart state after identity deletion remains deletion-locked while stale local bytes exist.

Workflow: `.github/workflows/s007-onboarding-deletion-state-model.yml`.

Exact workflow head: `967e0e2b087cec80b767d6586b2208c1d07908d1`.
Run `35938569294` was automatically created from the workflow commit and was **queued** when this note was written. Therefore execution observation and verdict remain OPEN. Do not infer PASS from fixture review or workflow creation.

## Failure model / evidence limit
This reference model can expose semantic collapse such as `signedOut == firstUse`, data-presence-as-onboarding, cross-UID mutation, or identity-delete-as-full-erasure. It cannot validate Firebase persistence, Flutter routing, Sembast atomicity, Apple/Google SDK behavior, backend erasure, actual local wipe, process durability, or LogMate code.

## Product transfer
Exact product remains `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`; production identity unknown and default branch is not assumed production. No LogMate canonical files were edited. The retained product ref still predates the integrated account-required contract.

## RELATED DOMAIN CHECK
- Foundations: direct Dart/Flutter execution exists; not the current blocker.
- Architecture: separate auth/owner/onboarding/deletion axes remain required; the fixture intentionally does not collapse them.
- Mobile: exact native/PWA lifecycle transfer remains OPEN.
- Data: durable deletion marker and local erasure need real persistence/crash validation in product transfer.
- Quality: workflow execution must supply the mechanical verdict; exact-product failure injection remains required.
- Systems: owns this semantic security/state boundary.
- Design Studio: no visual/interaction canonical change required by this bounded model.
- Web Manager: external deletion surface remains a later integration dependency, not exercised here.
- Marketing Manager: not materially relevant.
- Product: exact LogMate ref checked; no product files edited.

## VALIDATION / OPEN
- Await run `35938569294` terminal result and job/environment evidence.
- If green, record exact Python/runner environment and test output; this will be bounded Studio-model validation only.
- Reproduce equivalent invariants in actual LogMate Dart/Flutter tests after product implementation.
- Add persistence/process-death and backend/Auth independent oracles during exact-product transfer.

## HANDOFFS
- LogMate/Codex: use the nine cases as minimum semantic regression tests when implementing the integrated contract.
- Quality: preserve independent assertions for routing, owner identity, erasure state and restart state; do not treat `currentUser == null` as a deletion oracle.
- Data/Architecture: product implementation needs durable semantic milestones, not UI-page inference.
