// Web-only reference. Import this file only from a Web-specific implementation.
//
// Add direct dependency on google_sign_in_web when using this API:
//   import 'package:google_sign_in_web/web_only.dart' as web;

import 'package:flutter/widgets.dart';
import 'package:google_sign_in_web/web_only.dart' as web;

/// Google-rendered Sign in with Google button for Flutter Web/PWA.
///
/// Google requires the Web user-initiated sign-in flow to use the SDK-rendered
/// button rather than an application-provided replacement.
Widget buildOfficialGoogleWebButton({
  double minimumWidth = 342,
}) {
  return web.renderButton(
    configuration: web.GSIButtonConfiguration(
      type: web.GSIButtonType.standard,
      theme: web.GSIButtonTheme.outline,
      size: web.GSIButtonSize.large,
      text: web.GSIButtonText.continueWith,
      shape: web.GSIButtonShape.rectangular,
      logoAlignment: web.GSIButtonLogoAlignment.left,
      minimumWidth: minimumWidth,
      locale: 'en',
    ),
  );
}
