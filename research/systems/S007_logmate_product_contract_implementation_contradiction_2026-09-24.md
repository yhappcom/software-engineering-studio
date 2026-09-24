# S007 — LogMate product-contract / implementation contradiction

Date: 2026-09-24
Owning track: Systems
Status: IN STUDY — exact-product transfer blocker identified

## Product evidence identity

- repository: `yhappcom/logmate`
- branch/ref inspected: `main`
- exact commit: `7551e1ca9e07df0b99e88aa03c8a56be03d8b2d3`
- declared version: `1.0.0+1`
- evidence date: 2026-09-24
- production identity: NOT ESTABLISHED; do not equate `main` with production.

## SOURCE

At the exact ref above, `docs/product/logmate-welcome-onboarding-implementation-spec.md` is the current product decision for the signed-out Welcome surface. It removes `Start a new logbook` and specifies exactly three authentication choices: `Continue with Apple`, `Continue with Google`, and `Continue with Email`.

At the same exact ref, `lib/main.dart` still composes `OpeningScreen` with a `startNewLogbookButton` whose visible label is `Start a new logbook`, plus a separate `openingSignInButton` labelled `Sign in`. The session gate also still exposes `startLocalUse` and the unbound-local-ledger opening path.

## CONTRADICTION

The product contract and executable product source disagree at the same repository commit. Documentation transfer is therefore ahead of implementation transfer. The Welcome contract must not be reported as implemented merely because the canonical product document changed.

## SYNTHESIS

S007 now has a concrete exact-product transfer target rather than only a waiting dependency. The next implementation boundary is not provider styling first; it is removal/replacement of the account-free opening path so the runtime surface and startup state machine conform to the product contract. Provider-compliant Apple/Google/Email controls, auth persistence, deletion semantics, and native/PWA lifecycle remain downstream validation boundaries.

## VALIDATION

This run performed source-level exact-ref comparison only. No Dart/Flutter runtime execution was available through the connected environment in this run, so no runtime PASS is awarded. Existing Studio executable semantic models remain reference oracles, not evidence that LogMate satisfies them.

## OPEN

1. Update LogMate implementation so signed-out Welcome exposes only the three product-approved authentication choices.
2. Verify the old local-use/start-new-logbook path is unreachable or deliberately migrated according to the product decision.
3. Run Flutter widget/integration tests against the exact implementation ref, including constrained height/landscape, text scaling, focus/state, cancellation, restart, and fail-closed startup.
4. Transfer the Studio S007 startup/onboarding/deletion invariants into Dart/Flutter and Firebase/native/PWA evidence.
5. Establish release/production identity separately before making production claims.

## RELATED DOMAIN CHECK

- Design: Welcome geometry and provider-brand constraints remain relevant, but do not override product authentication semantics.
- Quality: release-gate evidence must preserve exact product ref and distinguish source/document agreement from executable validation.
- Architecture/Data: removing account-free entry changes startup/access-state assumptions and may require migration handling for existing local ledgers.

## HANDOFFS

- LogMate implementation owner: reconcile `lib/main.dart` / session-gate behavior with the current product Welcome contract.
- Mobile/Quality: once an implementation ref exists, perform widget/runtime and failure-path transfer validation rather than another synthetic model cycle.

## Gate consequence

Systems Stage 1 remains NOT PASS. This finding strengthens the reason: current exact-product source contradicts its own current Welcome product contract, and runtime transfer validation has not yet occurred.
