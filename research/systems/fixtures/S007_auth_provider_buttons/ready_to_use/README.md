# LogMate Ready-to-Use Auth Button Kit

Status: reusable Engineering Studio component. Exact LogMate integration remains a product transfer validation.

## Surface split

The kit deliberately distinguishes three presentation surfaces:

| Surface | Detection / use | Provider visible size |
| --- | --- | --- |
| Native mobile | iOS/Android phone | 48 logical px high; width follows the approved Google aspect ratio |
| Native tablet | iPadOS/Android tablet | 56 logical px high; width follows the approved Google aspect ratio |
| PWA | Flutter Web installed/browser experience | Google GIS-rendered button, 280×40 compact or 360×40 regular; Apple/Email match that footprint |

Native platform widths:
- iOS mobile: 205.09 × 48 (Google iOS ratio 188:44)
- Android mobile: 216 × 48 (Google Android ratio 180:40)
- iPadOS tablet: 239.27 × 56
- Android tablet: 252 × 56

All three visible buttons on a given native surface use the same width and height.

PWA:
- viewport < 400 logical px: 280 × 40
- viewport >= 400 logical px: 360 × 40
- Google GIS renderer supports width configuration up to 400 px.
- Apple uses an official generated button at the same footprint.
- Email uses a LogMate-owned button at the same footprint.

## Order

- iPhone/iPad native: Apple → Google → Email
- Android phone/tablet: Google → Apple → Email
- PWA on Apple-family host: Apple → Google → Email
- Other PWA: Google → Apple → Email

The PWA order can be overridden explicitly.

## Shape / theme

All button footprints use a pill silhouette:
- native Apple system button: corner radius = height / 2
- Google native: official pre-approved Pill PNG
- PWA Google: GIS `shape: pill`
- Email: Flutter StadiumBorder

Apple and Google logos/text are never redrawn. Google Sans is not vendored.

## Product use

Copy this directory into LogMate, or copy the listed files to the product-owned auth UI area.

Native:
- `lib/logmate_native_auth_buttons.dart`
- `lib/auth_surface_spec.dart`
- `lib/apple_system_button.dart`
- `ios/OfficialAppleSignInButtonFactory.swift`
- `assets/`

PWA:
- `lib/logmate_pwa_auth_buttons.dart`
- `lib/auth_surface_spec.dart`
- `assets/`
- direct dependency on `google_sign_in_web` when using the renderer API.

Authentication callbacks are injected. These widgets never decide Firebase UID, owner binding, onboarding completion, provider linking, or account merge.

## Automatic surface resolution

`AuthSurfaceSpec.resolve(context)`:
- Web => PWA
- native shortest side >= 600 logical px => tablet
- otherwise => mobile

Product code may override the surface explicitly for tests or unusual devices.

## Reviewer / release note

The product requires an account because it stores account-bound/personalized user information. Store review credentials are supplied only through App Store Connect / Play Console review metadata. Never commit reviewer passwords to this repository.

## Asset provenance

Run:

```bash
bash tools/prepare_ready_to_use_assets.sh
```

The script:
- copies current provider-approved Google Pill PNGs from the Studio canonical provider asset set;
- generates Apple button PNGs from Apple-owned secure button endpoints at the exact LogMate footprints;
- writes a SHA-256 source manifest.

No font file is fetched or committed.

## Validation

The final kit must pass:
- Flutter static analysis;
- surface geometry/order tests;
- light/dark golden render tests;
- asset aspect-ratio checks;
- PWA composition reference render;
- later exact LogMate native/PWA runtime transfer.

The PWA golden uses a **structural placeholder** for the Google control because the real GIS button is provider-rendered at browser runtime. Production PWA Google sign-in must use Google Identity Services / `google_sign_in_web.renderButton()`, not a hand-wired image button.
