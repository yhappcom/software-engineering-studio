# M006 — Safari offline cold-start failure isolation

Status: **IN STUDY — SAME-SESSION OFFLINE PASS / FRESH-WEBDRIVER OFFLINE FAIL ISOLATED**  
Evidence date: 2026-09-23

## Scope
Continuation of `M006_safari_offline_cold_start_transfer.md`. This note preserves the trustworthy semantic failure chain and narrows the causal boundary. It does not award a general Safari offline cold-start PASS or product TRANSFER VALIDATION.

## VALIDATION — diagnostic run 3
Exact head `65add7b1eb2259ed0090fb4d1a79e39ac2f4d851`; workflow run `35767549760`; terminal **failure**. Run-bound artifact `10712587587`, digest `sha256:66645847351e3edf45096cf13314061cb48a20241885f94311e83d7da2261d9d`, was downloaded and inspected.

Environment: macOS 15.7.9 build 24G830; Safari/safaridriver 26.6.1; WebDriver enablement `ENABLE_RC=0`. Online app execution succeeded, but the title-based post-registration control oracle timed out. Exact source showed the intentional reload replaced the document and reset its title, so `M006_CONTROLLED` could no longer be produced. **ROOT CAUSE:** oracle lifetime did not survive the lifecycle transition. Commit `b4176f9b4a3adf675bc4dd11a05f52a0a1d86e5d` repaired the check to poll browser-owned `navigator.serviceWorker.controller`.

## VALIDATION — run 4 reaches the real origin-down boundary
Exact repaired head `b4176f9b4a3adf675bc4dd11a05f52a0a1d86e5d`; workflow run `35774016112`; job `106902502799`; runner image `macos-15-arm64` `20260907.0337.1`; macOS 15.7.9 build 24G830; Safari/safaridriver 26.6.1; Selenium 4.49.0. Terminal **failure**. Artifact `10714614946`, digest `sha256:60a4a089c72d7a4917f6216f99fc20533a3ce4f7fa68ddef48cf28c999ae8723`.

Failure-path evidence established online execution/control, `cache-precondition=true`, `origin-down=true`, then repeated Safari `Failed to open page` after quitting Safari WebDriver and creating a fresh session. This **CONTRADICTED** the fixture's fresh-WebDriver cold-start expectation but did not isolate Safari offline fetch from automation-session persistence.

## VALIDATION — run 5 causal discriminator
Exact head `91c5374bc7f09c6103c7f216bd7bf1146b78f40d`; workflow run `35780706023`; terminal **failure**. Run-bound artifact `10718495328`, digest `sha256:ec95755ab0c98a8b9e8f6ead62bc3d190c3edeedd6e4b0a0f78b6e7d2113c563`, was downloaded and inspected directly.

Environment artifact: macOS 15.7.9 build 24G830; Safari/safaridriver 26.6.1; WebDriver enablement `ENABLE_RC=0`.

The semantic observation sequence was:

- online app reached `M006_APP_READY`;
- `navigator.serviceWorker.controller` transitioned false → true;
- `cache-precondition=true`;
- independent probe established `origin-down=true`;
- **same Safari WebDriver session, origin still down:** navigation reached `M006_APP_READY` and `offline-same-session-controller=true`;
- after quitting/recreating Safari WebDriver, the same unavailable-origin navigation first had an empty title and then repeatedly returned `Failed to open page` for the full timeout;
- exact failure: `AssertionError('timeout offline-fresh-webdriver-app: wanted M006_APP_READY')`.

### Verdict
**VALIDATION:** Safari 26.6.1 in this exact hosted macOS environment can serve and execute the cached app shell with a controlling Service Worker after the origin server is terminated **within the surviving WebDriver browsing session**. This is bounded executable evidence for origin-down offline fetch/cache behavior; it is not ordinary Safari relaunch, installed PWA, iOS/iPadOS/EFB or product evidence.

**CONTRADICTION:** the fresh-WebDriver-session cold-start expectation remains false in two consecutive exact-head runs after cache/control preconditions were established.

**ROOT-CAUSE STATUS:** the discriminator isolates the observed difference to the WebDriver/session-recreation boundary or state coupled to it. It does **not** prove which WebKit/SafariDriver implementation mechanism discards, partitions, or fails to expose the prior Service Worker/Cache state, and it does not establish that an ordinary user Safari relaunch behaves the same way. Therefore the lower-level implementation root cause remains OPEN.

## SOURCE / model
WebKit's Service Worker implementation model makes browsing-session/storage partition identity a material variable. The executable discriminator now independently demonstrates that session survival changes the observed result in this hosted SafariDriver context. Source/model and executable evidence agree that `webdriver.Safari()` recreation must not be treated as a neutral synonym for ordinary browser restart.

## SYNTHESIS
A "browser restart" is not a valid test abstraction unless the automation mechanism preserves the storage/profile/session identity implied by the product scenario. Service Worker registration, CacheStorage, browser process lifetime, WebDriver session lifetime, browser profile lifetime, and installed/Home-Screen PWA lifetime are distinct boundaries.

For recovery/offline tests, the oracle should separately establish: cached prerequisite state → actual origin unavailability → same-identity offline execution → any intended restart/relaunch identity transition. A red restart step must not erase a preceding positive offline-fetch result.

## RELATED DOMAIN CHECK
- Foundations: navigation/document replacement and process/session ownership checked; no native-runtime claim.
- Architecture: offline boot is externally observable; browser/session identity is part of the validation boundary rather than an invisible harness detail.
- Mobile: owner; same-session macOS Safari origin-down offline behavior is now positively validated, while fresh-WebDriver cold start remains contradictory.
- Data: cached app-shell presence was positively established before origin termination; application-data durability is not claimed.
- Quality: run 5 is a causal discriminator with independent cache/origin-down/session observations; lower-level implementation ROOT CAUSE remains OPEN.
- Systems: exact head/run/artifact/environment identity retained; WebDriver-session recreation is an explicit environment/provenance variable.
- Design Studio: not materially relevant.
- Web Manager: PWA/browser overlap considered; no canonical edit required.
- Marketing Manager: not materially relevant.
- Product context retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`; production identity unknown, default branch not assumed production, no product execution claimed.

## HANDOFFS
- Quality: recovery/restart tests must prove the harness preserves or intentionally changes the identity/state boundary named by the claim; preserve positive pre-restart evidence separately from a later restart failure.
- Systems: product PWA transfer must bind browser/profile/storage identity as well as source→build→artifact→origin; WebDriver session recreation is not release/runtime provenance.
- Mobile: do not repeat equivalent same-session/fresh-session variants. A stronger next rung requires an ordinary Safari profile/relaunch mechanism, installed PWA/iOS/iPadOS/EFB, physical device/network, or exact product artifact.

## OPEN / CHANGE WATCH
- OPEN: ordinary Safari relaunch/profile persistence semantics versus SafariDriver session recreation in a trustworthy environment.
- OPEN: lower-level SafariDriver/WebKit mechanism responsible for the fresh-session state boundary.
- OPEN: LogMate `make build-pwa`, iOS/iPadOS/EFB, physical network/storage and production transfer.
- CHANGE WATCH: Safari/WebKit Service Worker behavior and hosted macOS runner image.
