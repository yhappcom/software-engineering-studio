# LogMate integration steps

1. Copy `ready_to_use/assets/*.png` to LogMate `assets/auth/`.
2. Copy shared/native Dart files into the product auth UI package.
3. For iOS/iPadOS, copy `OfficialAppleSignInButtonFactory.swift` and register the platform view id `logmate/apple-sign-in-button` from `AppDelegate.swift`.
4. Use `LogMateNativeAuthButtons` on Android/iOS. It auto-resolves phone vs tablet at 600 logical px shortest-side unless overridden.
5. Use `LogMatePwaAuthButtons` on Flutter Web/PWA. Do not replace its Google GIS-rendered control with an image click handler.
6. Wire Apple/Google/Email callbacks to the provider-neutral Auth command boundary. Button press is not authentication success.
7. Keep reviewer credentials out of Git and provide them only in the store review portals.

Example native usage:

```dart
LogMateNativeAuthButtons(
  onApple: () => auth.authenticate(AuthProvider.apple),
  onGoogle: () => auth.authenticate(AuthProvider.google),
  onEmail: openEmailFlow,
)
```

Example PWA usage:

```dart
LogMatePwaAuthButtons(
  onApple: () => auth.authenticate(AuthProvider.apple),
  onEmail: openEmailFlow,
)
```

Google PWA button presses are handled by the Google Identity Services renderer / plugin flow.

## AppDelegate registration

```swift
if let registrar = self.registrar(forPlugin: "LogMateOfficialAppleButton") {
  registrar.register(
    OfficialAppleSignInButtonFactory(messenger: registrar.messenger()),
    withId: "logmate/apple-sign-in-button"
  )
}
```

## Surface acceptance

- phone: verify 48-high native footprint on at least one iPhone and one Android phone;
- tablet: verify 56-high footprint on iPad and Android tablet;
- PWA: verify compact 280×40 and regular 360×40 GIS render in Chrome/Safari-compatible supported flows;
- verify light/dark, VoiceOver/TalkBack/browser accessibility, cancellation, duplicate tap, and loading/error states.
