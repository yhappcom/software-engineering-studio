# M006 — Safari offline cold-start failure isolation

Status: **IN STUDY — ORIGIN-DOWN FAILURE REACHED / SESSION-PERSISTENCE DISCRIMINATOR PENDING**  
Evidence date: 2026-09-23

## Scope
Continuation of `M006_safari_offline_cold_start_transfer.md`. This note preserves the trustworthy semantic failure chain and narrows the next causal discriminator. It does not award Safari offline PASS or TRANSFER VALIDATION.

## VALIDATION — diagnostic run 3
Exact head `65add7b1eb2259ed0090fb4d1a79e39ac2f4d851`; workflow run `35767549760`; terminal **failure**. Run-bound artifact `10712587587`, digest `sha256:66645847351e3edf45096cf13314061cb48a20241885f94311e83d7da2261d9d`, was downloaded and inspected.

Environment: macOS 15.7.9 build 24G830; Safari/safaridriver 26.6.1; WebDriver enablement `ENABLE_RC=0`. Online app execution succeeded, but the title-based post-registration control oracle timed out. Exact source showed the intentional reload replaced the document and reset its title, so `M006_CONTROLLED` could no longer be produced. **ROOT CAUSE:** oracle lifetime did not survive the lifecycle transition. Commit `b4176f9b4a3adf675bc4dd11a05f52a0a1d86e5d` repaired the check to poll browser-owned `navigator.serviceWorker.controller`.

## VALIDATION — run 4 reaches the real origin-down boundary
Exact repaired head `b4176f9b4a3adf675bc4dd11a05f52a0a1d86e5d`; workflow run `35774016112`; job `106902502799`; runner image `macos-15-arm64` `20260907.0337.1`; macOS 15.7.9 build 24G830; Safari/safaridriver 26.6.1; Selenium 4.49.0. Terminal **failure**. Artifact `10714614946`, digest `sha256:60a4a089c72d7a4917f6216f99fc20533a3ce4f7fa68ddef48cf28c999ae8723`.

Failure-path job logs establish the following sequence:

- `online-app` reached `M006_APP_READY`;
- `online-controlled` changed from false to true;
- `cache-precondition=true` for cached shell + `/app.js`;
- `origin-down=true` after server termination and independent HTTP probe;
- after quitting Safari WebDriver and creating a fresh `webdriver.Safari()` session, navigation to the same origin repeatedly produced Safari's `Failed to open page` title for the full timeout;
- failure: `AssertionError('timeout offline-cold-start-app: wanted M006_APP_READY')`.

This is the first trustworthy run that reaches the intended origin-down boundary. It **CONTRADICTS** the fixture's fresh-WebDriver cold-start expectation at this exact environment, but it does not yet prove a general Safari offline limitation or a WebKit defect.

## SOURCE / causal hypothesis
WebKit's primary Service Worker implementation description states that service workers and Cache API data are partitioned by origin and browsing session, and that service-worker/cache information is persistent within the relevant partition. Safari 26.6 release notes also show Service Worker implementation remains actively changing. These sources make WebDriver browsing-session recreation a material variable rather than a neutral way to model an ordinary browser restart.

**ENGINEERING JUDGMENT:** run 4 has two live hypotheses that must be discriminated before ROOT CAUSE: (1) Safari cannot serve this cached navigation after origin loss even while the original browsing session survives; or (2) same-session offline fetch works, while quitting/recreating WebDriver changes or discards the storage/Service Worker partition used by this automation environment. The current evidence cannot choose between them.

## Diagnostic discriminator
Commit `91c5374bc7f09c6103c7f216bd7bf1146b78f40d` changes only the validation sequence. After online control/cache preconditions it terminates the origin and first attempts the cached navigation **in the same Safari WebDriver session**, requiring `M006_APP_READY` plus a non-null controller. Only after that does it quit/recreate WebDriver and repeat the unavailable-origin navigation.

Interpretation contract:
- same-session offline fails → the failure is earlier than WebDriver-session persistence; investigate fetch/navigation/cache semantics without blaming recreation;
- same-session offline passes and fresh-WebDriver fails → bounded causal evidence isolates the difference to session recreation/persistence context; do not call this a generic Safari offline failure;
- both pass → run 4 was non-reproducing/transient and requires replication before any transfer verdict.

No PASS is awarded from this code change. Exact-head workflow evidence is required.

## SYNTHESIS
A "browser restart" is not a valid test abstraction unless the automation mechanism preserves the same storage/browsing-session identity that the product scenario assumes. Service Worker registration, CacheStorage, browser process lifetime, WebDriver session lifetime, and installed/Home-Screen PWA lifetime are distinct boundaries and must not be conflated.

## RELATED DOMAIN CHECK
- Foundations: navigation/document replacement and process/session ownership checked; no native-runtime claim.
- Architecture: offline boot remains externally observable; validation now separates browser-session ownership from fetch behavior.
- Mobile: owner; macOS Safari origin-down fresh-WebDriver behavior is red, but general offline capability remains unresolved.
- Data: cached app-shell presence was positively established before origin termination; application-data durability is not claimed.
- Quality: failure-path diagnostics and causal discriminator follow failure→isolation discipline; no ROOT CAUSE is awarded for run 4 yet.
- Systems: exact head/run/job/artifact/environment identity retained; WebDriver-session recreation is now an explicit environment variable.
- Design Studio: not materially relevant.
- Web Manager: PWA/browser overlap considered; no canonical edit required.
- Marketing Manager: not materially relevant.
- Product context retained: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`; production identity unknown, default branch not assumed production, no product execution claimed.

## HANDOFFS
- Quality: restart/recovery tests must verify that the test harness preserves the identity/state boundary implied by the claim; process/session recreation is not automatically product-equivalent.
- Systems: product PWA transfer must bind browser/profile/storage identity as well as source→build→artifact→origin.
- Mobile: use the same-session/fresh-session discriminator before changing Service Worker logic.

## OPEN / CHANGE WATCH
- OPEN: exact-head execution verdict for commit `91c5374bc7f09c6103c7f216bd7bf1146b78f40d`.
- OPEN: whether same-session Safari origin-down navigation succeeds with the proven cache/controller precondition.
- OPEN: semantics of SafariDriver session recreation versus ordinary Safari relaunch/profile persistence in this hosted environment.
- OPEN: LogMate `make build-pwa`, iOS/iPadOS/EFB, physical network/storage and production transfer.
- CHANGE WATCH: Safari/WebKit Service Worker behavior and hosted macOS runner image.
