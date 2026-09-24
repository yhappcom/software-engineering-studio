# S007 — LogMate Welcome Product Delta

Status: **TRANSFER VALIDATION / CONTRADICTION SHARPENED — PRODUCT PRESENTATION AUTHORITY ADVANCED; RUNTIME OPEN**  
Owner: Systems / Security / Identity  
Evidence date: 2026-09-24

## Why this note exists

The prior integrated S007 transfer contract was written against LogMate ref `e79f97cb7edd8823860daf14770a589f28a63ffc`. LogMate has since advanced. Product repositories are implementation/product truth; Studio notes must not silently override a newer explicit product decision.

Latest audited product evidence:

`yhappcom/logmate → main → 7551e1ca9e07df0b99e88aa03c8a56be03d8b2d3 → declared 1.0.0+1 → evidence date 2026-09-24`

Production identity remains unknown; `main` is not assumed production.

## SOURCE — new product-canonical Welcome decision

At exact ref `7551e1ca...`, `docs/specs/welcome-mobile-light-visual-spec.md` is `IMPLEMENTATION HANDOFF / CROSS-DOMAIN REVIEWED` and explicitly states that its owner-approved Welcome decisions supersede older Welcome-specific visual assumptions where they conflict.

The product now explicitly requires the signed-out Welcome composition to show:

- `LOGMATE`
- `Pilot Logbook`
- `Continue with Apple`
- `Continue with Google`
- `Continue with Email`

and explicitly excludes `Start a new logbook` from this Welcome composition.

It also records Roboto as an owner-selected product decision for this implementation, requires a coherent three-choice component family, requires provider/platform branding constraints to override LogMate styling where mandatory, preserves official marks/aspect ratio/clear space, requires reflow/reachability at constrained geometry and 200% text, and requires real Flutter render evidence before visual promotion.

The same exact product ref declares `1.0.0+1`, Dart `^3.10.7`, `firebase_auth ^6.7.0`, and `firebase_core ^4.15.0` in `pubspec.yaml`.

## CONTRADICTION — Studio presentation transfer is now partially stale

The earlier integrated Studio contract section 4 freezes shared visible copy as:

- `Sign in with Apple`
- `Sign in with Google`
- `Sign in with Email`

The newer product decision freezes:

- `Continue with Apple`
- `Continue with Google`
- `Continue with Email`

For LogMate product implementation, the newer product wording is authoritative. The Studio `Sign in with ...` wording remains reusable package/reference-fixture evidence, not current LogMate product copy.

The prior Studio package also encodes surface-specific provider-owned controls/geometry. The new product spec asks the three choices to read as one coherent LogMate family, but explicitly says provider/platform branding requirements override LogMate styling where mandatory. Therefore this is **not yet evidence that native Apple/Google controls may be restyled into arbitrary identical shells**. The implementation must satisfy both product visual coherence and provider/platform constraints. If the real provider control cannot satisfy a requested shared-shell property, preserve provider compliance and return the constraint to product/design rather than redrawing the provider control.

## SYNTHESIS — what advanced and what did not

The earlier S007 statement that the exact LogMate product still showed the old unauthenticated `Start a new logbook` Welcome is no longer fully current. The latest Welcome visual contract explicitly removes that action from Welcome and establishes Apple/Google/Email as the only three visible entry choices.

However, this is a **documentation/product-contract transfer**, not implementation/runtime validation. The product spec itself says older local-first assumptions still exist elsewhere and must be synchronized during implementation. No claim is made here that `MASTER.md`, startup routing, Auth engine, durable onboarding state, tests, Firebase provider configuration, or native/PWA provider execution have already been updated.

Therefore:

- account-required Welcome direction: **product documentation now confirms it at the Welcome surface**;
- exact three visible Welcome choices: **product documentation confirms**;
- current visible copy: **`Continue with ...`**;
- old `Start a new logbook` on signed-out Welcome: **superseded by latest Welcome spec**;
- full product-canonical auth/startup synchronization: **OPEN**;
- exact Flutter implementation/runtime: **OPEN**;
- provider operational configuration and native/PWA execution: **OPEN**;
- three-path authenticated onboarding, owner UID, deletion saga, presence and provider continuity transfer: **OPEN unless separately synchronized in product canonical files/code**.

## VALIDATION boundary

No PASS is awarded from this document read. The product spec itself requires real Flutter evidence including ordinary portrait, constrained height/landscape, 200% text, resolved fonts, focus/state evidence, action mapping tests, and provider-compliant marks. Those remain transfer-validation targets.

The Studio ready-to-use provider package remains useful as implementation evidence, but its copy must not be copied blindly into LogMate after this product decision. Exact-product tests must assert the product copy and behavior at the audited implementation ref.

## RELATED DOMAIN CHECK

- **Foundations:** direct Dart/Flutter execution already exists; not the blocker.
- **Architecture:** product decision authority and implementation/evidence state remain separate; do not infer implementation from the handoff document.
- **Mobile:** real Flutter/native/PWA rendering and provider lifecycle remain required.
- **Data:** not materially changed by this visual contract; durable onboarding/owner/deletion state remains separately OPEN.
- **Quality:** exact-product tests must discriminate documentation agreement from runtime behavior and preserve constrained-layout/provider failure cases.
- **Systems:** identity/auth authority remains S007; provider compliance and operational setup remain OPEN.
- **Design Studio:** the product spec explicitly records a cross-domain-reviewed visual contract; Studio does not overwrite Design Studio canonical files.
- **Web Manager:** PWA/provider and external deletion surfaces remain future transfer dependencies; no change made here.
- **Marketing Manager:** not materially relevant to this auth-entry implementation boundary.
- **Product source/ref checked:** `yhappcom/logmate → main → 7551e1ca9e07df0b99e88aa03c8a56be03d8b2d3 → 1.0.0+1 → 2026-09-24`.

## HANDOFFS

### LogMate / Codex
Use `docs/specs/welcome-mobile-light-visual-spec.md` at `7551e1ca...` as the newer LogMate Welcome presentation authority. Do not restore `Start a new logbook` to signed-out Welcome. Use `Continue with Apple / Google / Email` unless a still-newer product decision supersedes it. Preserve provider/platform compliance even when seeking common visual geometry. Synchronize the remaining auth/startup canonical files and tests rather than treating this visual handoff alone as full S007 implementation.

### Quality / Mobile / Systems
The next high-value evidence rung is exact-product implementation transfer: inspect the implementation ref after code lands, run Dart/Flutter tests, stress constrained geometry/200% text, verify each visible choice maps to the correct provider-neutral auth action, and then validate real Apple/Google native/PWA behavior. Do not award runtime PASS from the handoff document.

## OPEN / CHANGE WATCH

- Whether current LogMate code has implemented this handoff remains OPEN.
- Full account-required startup/auth canonical synchronization remains OPEN.
- Product copy/provider requirements can change; always inspect the latest exact product ref before implementation transfer.
- Apple/Google provider presentation/runtime requirements are externally governed and remain CHANGE WATCH.
