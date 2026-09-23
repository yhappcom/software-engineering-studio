# M006 — Safari service-worker lifecycle run-4 closure

Status: **BOUNDED TRANSFER VALIDATION — PASS**  
Evidence date: 2026-09-23

## Scope
This note closes only the macOS Safari/SafariDriver fixture claim that remained OPEN after the false-green and two navigation-lifetime oracle defects documented in `M006_safari_service_worker_lifecycle_transfer.md`.

## VALIDATION
Exact repository/ref: `yhappcom/software-engineering-studio → main → 54bbd5283920aa3d82057cc2da8a14b0db4bacbf`. Workflow run `35810765603` completed success. Run-bound artifact `10729767594`, digest `sha256:34bc15dbb8cb15776571ded24d38de1d38b3be87228c644844de59551740f67f`, was directly downloaded and inspected.

The non-empty semantic oracle records verdict `SAFARI_SW_REGISTER_UPDATE_RESTART_PASS` and the following ordered observations:
- initial V1 controller acquisition: `false → true` across navigation;
- independent V1 semantic query: `false → true`, ending at `M006_SW_READY_V1`;
- explicit update/controller replacement: `controller-changed-to-new-worker false → true`, ending at `M006_SW_CONTROLLER_CHANGED`;
- V2 control confirmed at `M006_SW_READY_V2`;
- after quitting and recreating Safari WebDriver, restart controller persistence: `false → true` across navigation;
- independent restarted-document V2 query: `true` at `M006_SW_READY_V2`.

The artifact also records `ENABLE_RC=0`; server evidence contains page and `/sw.js` requests spanning registration, update and restart.

## TRANSFER VALIDATION
**PASS, bounded to this fixture/environment.** The exercised macOS Safari environment supports the fixture's V1 registration/control, explicit V1→V2 update with controller replacement, and V2 registration/control recovery across a fresh Safari WebDriver session when lifecycle-valid browser-owned controller state is used across navigation and application-owned version state is queried only in the surviving controlled document.

This restores the combined Safari service-worker lifecycle transfer that had been withdrawn after the historical false-green. It does not rehabilitate the invalid historical run; run `35741047017` remains INVALID evidence.

## FAILURE / ROOT-CAUSE CHAIN RETAINED
1. Historical green was invalid because a verdict-bearing producer was piped through `tee` without fail-closed propagation and produced a zero-byte semantic artifact.
2. Fail-closed execution exposed an initial-document oracle that expected application-owned title state from an invocation destroyed by reload.
3. Repair exposed the same lifetime error at the recreated-session restart boundary.
4. Exact head `54bbd528...` separates browser-owned controller state across each navigation from independent application-owned V1/V2 queries in surviving documents.
5. Run `35810765603` supplies the regression evidence above.

## ENGINEERING JUDGMENT
Navigation-aware validation is a repeated boundary discipline, not a one-time harness property. At every reload/recreation boundary, the oracle must be owned by state whose lifetime spans that boundary. Workflow success, subprocess exit propagation, semantic artifact presence, and lifecycle validity are independent evidence controls.

## EVIDENCE LIMIT
No claim is made for ordinary Safari user-profile relaunch, installed PWA, offline cold start across a fresh SafariDriver session, Flutter-generated service-worker semantics, LogMate's product-owned post-build PWA artifact, iOS/iPadOS/EFB, physical devices, cache eviction, production release identity, or production behavior. The separately observed fresh-WebDriver origin-down cold-start contradiction remains OPEN and is not resolved by this lifecycle PASS.

## RELATED DOMAIN CHECK
- Foundations: direct Dart JIT/AOT and bounded Flutter Chrome/Safari runtime evidence already exists; not a blocker.
- Architecture: registration, controller ownership, update/controller replacement and session persistence remain distinct lifecycle contracts.
- Mobile: owner; bounded combined Safari SW lifecycle transfer now PASS.
- Data: no application-data durability/cache correctness claim.
- Quality: Q006 verdict-propagation lesson transferred naturally; property owner/lifetime must match each navigation boundary.
- Systems: exact head/run/artifact/digest and semantic payload are retained separately from workflow metadata.
- Design Studio: not materially relevant to this runtime validation.
- Web Manager: PWA/browser overlap considered; no external canonical file edited.
- Marketing Manager: not materially relevant.
- Product: retained prior identity only: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence 2026-09-20`; default branch is not assumed production and this run did not execute that product.

## OPEN / CHANGE WATCH
- OPEN: ordinary Safari profile/relaunch and installed-PWA persistence.
- OPEN: fresh-SafariDriver origin-down cold start lower-level mechanism.
- OPEN: exact LogMate `make build-pwa` artifact/runtime, pending a trustworthy authorized source/build environment.
- OPEN: iOS/iPadOS/EFB and physical-device transfer.
- CHANGE WATCH: Safari/WebKit service-worker behavior and hosted macOS runner image.

## HANDOFFS
- Quality: retain the full false-green → fail-closed red → two lifecycle-oracle root causes → repaired regression chain as a reusable validation case.
- Systems: a green CI run is admissible only when verdict propagation, non-empty semantic evidence and the semantic oracle itself are independently valid.
- Web Manager / LogMate: bounded generic Safari lifecycle evidence may now be consumed as feasibility evidence, but not as product PWA/runtime or installed-PWA evidence.
