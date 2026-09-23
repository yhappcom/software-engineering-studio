# S007 — Auth Provider Button Render Validation — 2026-09-24

Status: **HOSTED FLUTTER GEOMETRY/RENDER VALIDATION CLOSED; RAW PRE-APPROVED PNG FULL-WIDTH COMPOSITION REJECTED; EXACT LOGMATE/NATIVE PROVIDER VALIDATION OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-24

## Product decisions carried into this validation
- LogMate account is mandatory.
- The product stores account-bound/personalized user information; authentication is therefore part of product ownership/personalization, not merely telemetry gating.
- App Store / Play review will be given a dedicated working reviewer account when review requires credentials.
- Reviewer credentials are operational secrets and must be supplied through the store review channels; do **not** commit passwords or reusable credentials to Engineering Studio or LogMate source control.
- V1 providers: Apple, Google, Email.
- Intended ordering: iOS/iPadOS Apple → Google → Email; Android Google → Apple → Email. Web/PWA remains platform/product-specific and requires separate runtime validation.

## Target
Reusable Studio fixture:
`research/systems/fixtures/S007_auth_provider_buttons/render_harness/`

Provider assets:
`research/systems/fixtures/S007_auth_provider_buttons/assets/`

Rendered evidence commit:
`c0719bd93c2fb5304fb76537faeca2d7dd9ac9f9`

Successful GitHub Actions run:
- workflow: `S007 Auth Button Render`
- run: `35934806084`
- job: `107429333111`
- trigger head: `42551ada243b6f0450c2d72975f65b7d023978a9`
- environment: GitHub-hosted Linux
- Flutter: 3.47.5 stable
- Dart: 3.13.4

## Failure-first record
Initial run `35934647522`, job `107428844926`, failed before rendering because the harness guessed a nonexistent Google iOS asset path (`Neutral/Theme=Light`). The provider ZIP actually stores a separate `Light/Theme=Light` path.

This failure was isolated to asset selection/provenance rather than Flutter rendering. Commit `42551ada243b6f0450c2d72975f65b7d023978a9` corrected the path and the same workflow then completed successfully.

## Automated checks
Hosted run `35934806084` reports:
- `flutter analyze`: **No issues found**
- 4 widget/golden tests:
  - iOS light
  - iOS dark
  - Android light
  - Android dark
- 1 provider-asset decode/dimension test
- total: **5 tests passed**

Geometry oracle:
- layout slot width: 375 logical px
- layout slot height: 56 logical px
- vertical gap: 12 logical px
- iOS order: Apple < Google < Email
- Android order: Google < Apple < Email
- semantic labels for Apple/Google and visible Email copy present.

## Observed official asset dimensions
The hosted decoder recorded:
- Apple light: 1125×168 px = 375×56 at 3x; aspect ratio ≈ 6.696
- Apple dark: 1125×168 px; aspect ratio ≈ 6.696
- Google iOS light/dark: 564×132 px = 188×44 at 3x; aspect ratio ≈ 4.273
- Google Android light/dark: 540×120 px = 180×40 at 3x; aspect ratio = 4.5

## Render verdict
The slot-level geometry is valid, but **raw provider PNGs cannot produce equal visible 375×56 buttons while preserving their official aspect ratios**.

With `BoxFit.contain`:
- Apple fills the 375×56 slot exactly.
- Google iOS, constrained by 56 px height, occupies only about 239 px of visible width.
- Google Android, constrained by 56 px height, occupies only about 252 px of visible width.
- Stretching Google to 375×56 would distort the approved asset and violates the no-distortion branding constraint.

The committed golden renders therefore demonstrate a real distinction between **equal layout slots** and **equal visible button geometry**.

## Primary-source recheck after render
Google's current Sign in with Google Branding Guidelines, last updated 2026-07-07, explicitly states:
- Google Identity Services rendering is recommended.
- Pre-approved image assets are permitted.
- A developer may create a custom Sign in with Google button when needed to match app design, provided the specified size/text/color/font/padding/logo rules are followed.
- The Google button should be approximately the same size and visual weight as other third-party sign-in options.
- Custom button font is Google Sans Medium 14/20; standard-color G and prescribed platform padding must be retained.
- Button scaling is allowed for device/screen size, but the Google logo aspect ratio must not be distorted.

Web GIS `renderButton` supports a configured standard button width up to 400 px and is preferred for Web/PWA.

## Engineering conclusion
**REJECT as final:** “Use the downloaded Apple and Google standard PNGs unchanged inside identical 375×56 full-width slots.”

That implementation passes slot geometry but fails the intended visible-uniformity goal.

Next implementation candidates:
1. **Provider-rendered / provider-compliant full-width path**
   - Apple: system/generated official button.
   - Google Web: GIS/Flutter Web renderer with configured width.
   - Google native: provider-compliant custom button following Google's published logo/font/padding/color contract when the fixed pre-approved raster does not satisfy product width.
   - Email: LogMate-owned button matched to the final visible footprint.
2. **Natural-size official raster path**
   - iOS: approximately 188×44 for all three.
   - Android: approximately 180×40 for all three.
   - preserves raw asset dimensions but is materially narrower than the desired full-width mobile composition.

Engineering preference for LogMate is candidate 1, but final visual acceptance belongs with Design Studio/product review after a compliant render is produced.

## Evidence limit
This validation proves the Studio Flutter harness, exact selected official PNG dimensions, order/slot invariants, and the raw-raster visual mismatch. It does not prove:
- actual LogMate UI integration;
- native iOS `ASAuthorizationAppleIDButton`;
- native Google authentication;
- Google custom-button branding approval;
- Google Web GIS runtime rendering;
- Apple/Google account authentication;
- App Store / Play review acceptance;
- physical-device rendering/accessibility.

## RELATED DOMAIN CHECK
- Architecture: rendering is a provider adapter; UID/session authority unchanged.
- Mobile: native system/provider controls remain separate transfer targets.
- Data: not materially changed.
- Quality: failure-first run retained; hosted geometry/golden oracle closed for this fixture.
- Systems: owns provider integration and compliance constraints.
- Design Studio: visible geometry mismatch requires a design/engineering handoff before LogMate final composition.
- Web Manager: GIS Web renderer remains relevant for PWA.
- Product: LogMate source not modified.

## HANDOFFS
- **Design Studio:** do not treat equal 375×56 slots as equal visible buttons. Review a second compliant render using Google provider-rendered/custom-compliant geometry.
- **LogMate / Codex:** do not copy the current raw-raster 375×56 composition as final UI. Preserve the validated order/semantics but replace Google native presentation with a compliant geometry strategy.
- **Quality/Mobile:** next validation must exercise the selected compliant implementation on native iOS/Android and PWA.

## CHANGE WATCH / OPEN
- Google branding, GIS renderer, Google Sans/padding requirements and Flutter plugin APIs remain CHANGE WATCH.
- Apple system/generated button APIs remain CHANGE WATCH.
- Exact LogMate integration and store-review credentials remain operational OPEN items until release preparation.
