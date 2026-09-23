# S007 Auth Provider Button Kit

Purpose: copy-ready provider button resources for LogMate and future Flutter apps.

This kit keeps Apple/Google artwork provider-owned. Do not redraw logos.

## 1. Fetch official assets

Run:

```bash
bash tools/fetch_official_provider_buttons.sh
```

Output:

```text
assets/google/...
assets/apple/...
assets/SOURCE_MANIFEST.txt
```

Google: the script downloads the current pre-approved Sign in with Google asset ZIP from Google and keeps PNG resources only.

Apple: the script generates current button PNGs from Apple's secure Sign in with Apple button endpoints. It generates:
- center and left aligned;
- sign-in and continue;
- black;
- white;
- white with border;
- logo-only black/white.

No font files are fetched or committed by the script.

## 2. Recommended LogMate mapping

### iOS/iPadOS
- Apple: use `AppleSystemSignInButton` + `OfficialAppleSignInButtonFactory.swift`.
- Google: use a Google pre-approved PNG button and trigger the official `google_sign_in` flow.
- Email: use `LogMateEmailAuthButton`.

### Android
- Apple: use an Apple official generated PNG and trigger the Firebase Apple provider flow.
- Google: use a Google pre-approved PNG button and trigger the official Google flow.
- Email: use `LogMateEmailAuthButton`.

### Web/PWA
- Google: prefer `google_sign_in_web.renderButton()`; see `lib/google_web_render_button_example.dart`.
- Apple: use Apple-approved generated/web button presentation and the supported Firebase/Apple web flow.
- Email: use the LogMate button.

## 3. Common layout

Use comparable prominence:
- same containing width;
- target visual height around 48–56 logical px where provider rules allow;
- minimum tap target at least 44 logical px;
- same vertical rhythm;
- none hidden behind “More” while another provider is primary.

Recommended product copy:
- Apple: **Continue with Apple**
- Google: **Continue with Google**
- Email: **Continue with Email**

“Continue” is appropriate when the same control handles both initial account creation and returning sign-in.

## 4. Flutter integration

Copy:
- `lib/provider_image_button.dart`
- `lib/apple_system_button.dart` when using the iOS system control
- `ios/OfficialAppleSignInButtonFactory.swift`
- `lib/google_web_render_button_example.dart` for PWA/Web

Copy/fetch provider assets into the product's asset folder and add them to the product `pubspec.yaml`.

The kit does not own authentication state. Button presses must call LogMate's provider-neutral Auth commands.

## 5. Dependencies

See `pubspec.fragment.yaml`.

At the 2026-09-24 evidence point:
- Firebase Flutter guidance uses the official `google_sign_in` plugin for native Google sign-in.
- current `google_sign_in` is 7.2.x;
- Web provider rendering is exposed by `google_sign_in_web`.

Treat versions as CHANGE WATCH; resolve against the exact LogMate Flutter/Dart toolchain before integration.

## 6. Apple iOS registration

Register the platform view in `AppDelegate.swift` after Flutter setup:

```swift
if let registrar = self.registrar(forPlugin: "LogMateOfficialAppleButton") {
  registrar.register(
    OfficialAppleSignInButtonFactory(messenger: registrar.messenger()),
    withId: "logmate/apple-sign-in-button"
  )
}
```

The Dart widget creates a per-view method channel. On a native button press it calls the provided Dart callback. Authentication remains in Flutter/Firebase code.

## 7. Assets are not identity logic

Never:
- infer provider from asset state;
- bind ledger ownership from email text;
- merge accounts because Google/Apple email matches;
- treat button press as authentication success.

Only the provider-neutral Auth result and Firebase UID can advance ownership/session state.

## 8. Validation still required

This kit is reusable implementation material, not LogMate runtime PASS. Validate exact LogMate iOS/Android/PWA rendering, provider configuration, callbacks, semantics, failure handling, and store/provider verification before release.
