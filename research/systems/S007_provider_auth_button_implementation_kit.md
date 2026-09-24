# S007 — Provider Auth Button Implementation Kit

Status: **PROJECT DECISION + SOURCE/SYNTHESIS; REUSABLE KIT PREPARED; EXACT-PRODUCT RUNTIME VALIDATION OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-24

## Scope
Prepare a reusable, copy-ready authentication-button kit for LogMate and future Flutter products while preserving Apple and Google provider branding authority.

Exact product evidence: `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`. Default branch is not assumed production. The audited ref still lacks `google_sign_in` and still contains the older account-free opening path.

## PROJECT DECISION
- Account is mandatory for LogMate first use.
- Account-required product rationale includes storage of account-bound/personalized user information; authentication is part of user ownership/personalization, not merely telemetry gating.
- Store review will receive a dedicated working reviewer account when credentials are required. Reviewer passwords/credentials must be supplied through store review metadata and must never be committed to source control.
- V1 providers are Apple, Google, and Email.
- Apple and Google use provider-approved/system/provider-rendered button treatment rather than a LogMate-redrawn logo/button.
- Email uses LogMate-owned UI.
- Apple, Google, and Email must have comparable prominence, width, tap target, and placement.
- Provider branding remains provider-owned; LogMate styling is applied around the controls rather than by redrawing the provider marks.

## SOURCE
Apple HIG states that system-provided Sign in with Apple buttons guarantee Apple-approved appearance, proportions, localization, and accessibility. Apple also permits custom buttons under strict rules and provides official assets / secure button-image endpoints. `ASAuthorizationAppleIDButton` is the native iOS/macOS control.

Google Sign in with Google branding guidance recommends Google Identity Services rendered buttons or pre-approved downloadable button assets. The button must be at least as prominent as other third-party sign-in options. Current Flutter `google_sign_in` guidance requires the SDK-rendered web button via `google_sign_in_web.renderButton()`; native platforms can use user-initiated UI with `authenticate()`.

Firebase Flutter federated-auth guidance currently identifies the official `google_sign_in` plugin for native Google authentication and `AppleAuthProvider` for Apple. Provider button rendering and provider credential/session handling remain separate concerns.

Primary sources rechecked 2026-09-24:
- Apple HIG — Sign in with Apple
- Apple `ASAuthorizationAppleIDButton`
- Apple Sign in with Apple REST button endpoints / web button guidance
- Google Sign in with Google Branding Guidelines
- Google Identity Services web `renderButton`
- Flutter `google_sign_in` 7.2.x guidance
- Firebase Flutter federated identity guidance

## Reusable implementation kit
Canonical fixture:
`research/systems/fixtures/S007_auth_provider_buttons/`

The kit intentionally does **not** redraw either provider logo and does not vendor fonts. It contains:
1. an asset acquisition script that pulls only provider-approved image resources from provider-owned endpoints;
2. Flutter wrappers for provider-approved image buttons and the LogMate Email button;
3. a native iOS `ASAuthorizationAppleIDButton` platform-view bridge;
4. a Web Google renderer example using the official Flutter Google web renderer;
5. dependency/configuration fragments and integration instructions.

The asset acquisition script is the canonical way to refresh binary provider assets. This avoids treating stale copied artwork as Studio-owned branding truth.

## Platform matrix
| Surface | Apple | Google | Email |
| --- | --- | --- | --- |
| iOS/iPadOS | Prefer native `ASAuthorizationAppleIDButton`; official generated PNG is fallback/reference | Google pre-approved native image button + official `google_sign_in` authentication | LogMate Flutter button |
| Android | Apple official generated button image + Firebase/Apple provider flow | Google pre-approved image button + official `google_sign_in` / current Google identity flow | LogMate Flutter button |
| PWA/Web | Apple official web/REST-generated button presentation; provider auth via supported web flow | `google_sign_in_web.renderButton()` / GIS renderer | LogMate Flutter/web button |

## Engineering constraints
- Do not recolor, crop, stretch, recreate, or substitute either provider logo.
- Do not ship the Google SVG variants without the required Google font handling; the kit fetches PNG resources by default.
- LogMate's selected shared copy is `Sign in with Apple / Google / Email`; Apple system/REST button type is therefore `signIn` / `sign-in`, and Google uses its official `Sign in with Google` presentation.
- Provider button tap must delegate into provider-neutral Auth commands; UI assets never become identity authority.
- Loading/disabled state must not modify provider artwork in a way that violates branding. Prefer an external progress indicator or disable pointer input while preserving the image.
- Provider-specific errors must map to typed Auth outcomes rather than leak raw SDK strings.
- Button visibility/prominence must remain comparable across Apple/Google/Email.

## VALIDATION
Hosted Flutter render validation is recorded in `research/systems/S007_auth_button_render_validation_2026-09-24.md`. Run `35934806084`, job `107429333111`, on Flutter 3.47.5 / Dart 3.13.4 passed analysis and all 5 render/geometry/decode tests and committed four light/dark iOS/Android goldens at `c0719bd93c2fb5304fb76537faeca2d7dd9ac9f9`.

The render also falsified one earlier implementation assumption: equal 375×56 layout slots do **not** make the raw pre-approved Google and Apple PNGs visibly equal. Apple 3x assets are 1125×168 (375×56 logical), Google iOS 3x assets are 564×132 (188×44), and Google Android 3x assets are 540×120 (180×40). Preserving aspect ratio leaves the Google visible button substantially narrower. The raw-raster 375×56 composition is therefore rejected as the final LogMate presentation.

### Ready-to-use LogMate package

A directly reusable package is now stored at `research/systems/fixtures/S007_auth_provider_buttons/ready_to_use/`.

It explicitly separates:
- **native mobile** — 48 logical-px height; iOS ≈205.09×48, Android 216×48;
- **native tablet** — 56 logical-px height; iPadOS ≈239.27×56, Android 252×56;
- **PWA** — 280×40 below 400 logical-px viewport width, otherwise 360×40.

Ordering:
- iPhone/iPad: Apple → Google → Email;
- Android phone/tablet: Google → Apple → Email;
- PWA Apple-family host: Apple → Google → Email; other PWA: Google → Apple → Email, with explicit override support.

Rendering:
- iOS/iPadOS Apple uses `ASAuthorizationAppleIDButton`;
- Android Apple uses exact-size Apple REST-generated official assets;
- native Google uses provider-approved Pill PNGs without aspect-ratio distortion;
- PWA Google uses `google_sign_in_web.renderButton()`;
- Email is LogMate-owned Flutter UI matched to the selected footprint.
- shared product copy is `Sign in with Apple / Google / Email`.

Latest bounded package validation: workflow run `35937075501`, job `107436392513`, Flutter 3.47.5 / Dart 3.13.4. `flutter analyze` reported no issues and **17 tests passed**. Current deterministic generated assets/renders were already materialized in repository state, so the final run reported no generated diff. The generated asset/render line is retained through commits `9c5eb99fb0196c5a6f008a6844b6af3467f24667` and deterministic-manifest commit `5eb345f5bba33ec70a6b76a5e0948c9174851840`.

**Bounded asset-acquisition validation:** workflow-triggered refresh commit `70fd04dbc6a0ee222cac1f711ee9eb1effb60d18` successfully materialized 111 tracked files: one SHA-256/source manifest plus 110 provider-approved PNG assets (14 Apple, 96 Google). Apple assets were generated from Apple-owned secure button endpoints; Google assets came from Google's current pre-approved Sign in with Google ZIP. The local fetch script also passed `bash -n` syntax validation before the hosted refresh.

The Studio package now has hosted Flutter analysis/geometry/reference-render evidence. It still does not establish exact LogMate integration, iOS Swift/Xcode compilation or physical-device rendering, Firebase provider configuration, real Google/Apple authentication, live browser GIS/OAuth execution, App Store review, or Play review.

Required transfer validation after LogMate integration:
1. `flutter pub get` / static analysis on the exact LogMate ref;
2. widget semantics and hit-target tests;
3. iOS simulator/device system Apple button rendering;
4. Android/iOS Google button + authentication;
5. Web Google SDK-rendered button;
6. Web Apple button + auth callback;
7. light/dark provider-button prominence inspection;
8. screen-reader labeling;
9. provider cancellation / duplicate tap / network-outcome-unknown behavior.

## RELATED DOMAIN CHECK
- Foundations: no new prerequisite.
- Architecture: provider button rendering remains a UI adapter; provider-neutral Auth command boundary retained.
- Mobile: iOS native button bridge and native provider flows need exact-platform transfer.
- Data: no ownership mutation may happen at button-render level.
- Quality: exact-product widget/native/web tests required.
- Systems: owns provider auth/security/integration contract.
- Design Studio: provider branding is a hard external constraint; LogMate composition may style spacing/background but not redefine provider marks. No Design Studio files edited.
- Web Manager: PWA provider rendering/authorized-origin configuration remains a downstream dependency. No Web Manager files edited.
- Marketing Manager: not materially relevant.
- Product: LogMate exact ref checked; no product files edited.

## HANDOFFS
- **LogMate / Codex:** copy/adapt the kit, run the official asset fetcher, add the official Google dependencies, register the Apple native platform view where selected, and connect presses to provider-neutral Auth commands. Do not redraw provider logos.
- **Design Studio:** treat provider button artwork/brand rules as immutable external constraints; design only the surrounding composition and comparable prominence.
- **Quality/Mobile:** validate native/Web rendering and provider flows on exact LogMate artifacts before release.

## CHANGE WATCH / OPEN
- Google branding assets, Flutter `google_sign_in`/web renderer APIs, Apple HIG/button endpoints, Flutter platform-view APIs, and store/provider verification requirements are CHANGE WATCH.
- Exact LogMate dependency compatibility and provider configuration remain OPEN.
- No product/runtime PASS is awarded from this reusable kit.
