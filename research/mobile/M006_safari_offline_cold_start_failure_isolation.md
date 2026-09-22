# M006 — Safari offline cold-start failure isolation

Status: **IN STUDY — HARNESS ROOT CAUSE ISOLATED / REGRESSION PENDING**  
Evidence date: 2026-09-23

## Scope
Continuation of `M006_safari_offline_cold_start_transfer.md`. This note preserves the first trustworthy semantic failure from diagnostic run 3 and the resulting oracle repair. It does not award Safari offline PASS or TRANSFER VALIDATION.

## VALIDATION — diagnostic run 3
Exact head `65add7b1eb2259ed0090fb4d1a79e39ac2f4d851`; workflow run `35767549760`; terminal **failure**. Run-bound artifact `10712587587`, digest `sha256:66645847351e3edf45096cf13314061cb48a20241885f94311e83d7da2261d9d`, was downloaded and inspected.

Environment evidence: macOS 15.7.9 build 24G830; Safari/safaridriver 26.6.1; WebDriver enablement `ENABLE_RC=0`.

The failure-path evidence is now non-empty and identifies the first failure precisely:

- `online-app` reached `M006_APP_READY`;
- `registerSW()` was invoked;
- the following `online-controlled` poll observed `M006_APP_READY` repeatedly for the full timeout;
- failure: `AssertionError('timeout online-controlled: wanted M006_CONTROLLED')`.

No cache-precondition, origin-down, fresh-session offline navigation, or offline-controller stage was reached. Therefore run 3 says nothing about Safari offline cold-start capability.

## ROOT CAUSE — validation harness, not Safari semantics
Exact fixture source shows `registerSW()` waits for registration/readiness and, when the current document has no controller, calls `location.reload()` and returns. The reloaded document executes `app.js` again, which unconditionally sets `document.title='M006_APP_READY'`; it does not automatically call `registerSW()` again or set `M006_CONTROLLED` merely because a controller now exists.

The validator nevertheless used `document.title == 'M006_CONTROLLED'` as the post-registration controller oracle. After the intentional reload, that title can never be produced by the reloaded page unless `registerSW()` is invoked again. The observed stable `M006_APP_READY` sequence is therefore explained by the fixture/oracle mismatch without requiring a Safari Service Worker failure hypothesis.

This is a bounded **ROOT CAUSE** for run 3: the online-control oracle asserted an application-title transition whose producer disappeared across the deliberate navigation. It is not evidence that Safari failed to install, activate, claim, cache, or control the reloaded document.

## Repair
Commit `b4176f9b4a3adf675bc4dd11a05f52a0a1d86e5d` replaces the title-based online-control check with a direct browser-owned semantic oracle: poll `Boolean(navigator.serviceWorker.controller)` after `registerSW()`/reload. The observations retain both controller state and title for diagnosis. Cache precondition, origin termination, independent failed HTTP probe, fresh Safari session, offline app execution, and offline-controller assertions are unchanged.

Regression workflow run `35774016112` targets exact head `b4176f9b4a3adf675bc4dd11a05f52a0a1d86e5d`; it was queued at the post-commit check. **No PASS/TRANSFER VALIDATION is awarded until that run completes and its run-bound evidence is inspected.**

## SYNTHESIS
For browser lifecycle tests, an application-owned presentation signal is a valid oracle only while the code responsible for producing that signal survives the lifecycle transition being tested. Across reload/navigation, controller ownership should be asserted from the browser API (`navigator.serviceWorker.controller`) or another independently surviving semantic source, not from a title/state mutation that is reset by the new document.

## RELATED DOMAIN CHECK
- Foundations: navigation replaces the document execution context; prior application-owned state is not a durable runtime oracle.
- Architecture: externally observable offline boot remains unchanged; this repair changes only validation semantics.
- Mobile: owner; offline cold-start behavior remains OPEN.
- Data: cache correctness was not reached in run 3.
- Quality: failure-path diagnostics successfully converted an undifferentiated red into a bounded harness root cause; oracle lifetime must match lifecycle lifetime.
- Systems: exact run/head/artifact/environment identity preserved; no product provenance claim.
- Design Studio: not materially relevant to this runtime oracle defect.
- Web Manager: PWA overlap considered; no canonical edit required.
- Marketing Manager: not materially relevant.
- Product context retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`; production identity unknown and no product execution is claimed.

## HANDOFFS
- Quality: add oracle-lifetime/lifecycle alignment to reusable browser validation guidance; presentation state reset by navigation must not stand in for browser-owned lifecycle state.
- Systems: preserve the repaired exact-head regression and artifact identity before any product transfer.
- Mobile: if regression reaches later stages, isolate the next first failure before changing service-worker behavior.

## OPEN / CHANGE WATCH
- OPEN: run `35774016112` regression verdict and artifact observations.
- OPEN: Safari origin-down cached cold-start semantics.
- OPEN: LogMate `make build-pwa`, iOS/iPadOS/EFB, physical network/storage and production transfer.
- CHANGE WATCH: Safari/WebKit Service Worker behavior and hosted macOS runner image.
