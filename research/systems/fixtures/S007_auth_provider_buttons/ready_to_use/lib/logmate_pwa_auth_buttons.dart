// Web/PWA-only implementation.
//
// Import this file only from a Web/PWA composition. It uses Google's official
// Flutter Web renderer rather than a hand-wired Google image button.

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:google_sign_in_web/web_only.dart' as google_web;

import 'auth_surface_spec.dart';

enum LogMatePwaProviderOrder {
  automatic,
  appleFirst,
  googleFirst,
}

class LogMatePwaAuthButtons extends StatelessWidget {
  const LogMatePwaAuthButtons({
    super.key,
    required this.onApple,
    required this.onEmail,
    this.order = LogMatePwaProviderOrder.automatic,
    this.assetRoot = 'assets/auth',
    this.enabled = true,
  });

  final VoidCallback onApple;
  final VoidCallback onEmail;
  final LogMatePwaProviderOrder order;
  final String assetRoot;
  final bool enabled;

  @override
  Widget build(BuildContext context) {
    if (!kIsWeb) {
      throw UnsupportedError(
        'LogMatePwaAuthButtons is Web/PWA-only.',
      );
    }

    final geometry = AuthSurfaceSpec.pwaGeometry(
      viewportWidth: MediaQuery.sizeOf(context).width,
    );
    final brightness = Theme.of(context).brightness;

    final google = SizedBox(
      key: const Key('googleAuthButton'),
      width: geometry.width,
      height: geometry.height,
      child: google_web.renderButton(
        configuration: google_web.GSIButtonConfiguration(
          type: google_web.GSIButtonType.standard,
          theme: brightness == Brightness.dark
              ? google_web.GSIButtonTheme.filledBlack
              : google_web.GSIButtonTheme.outline,
          size: google_web.GSIButtonSize.large,
          text: google_web.GSIButtonText.continueWith,
          shape: google_web.GSIButtonShape.pill,
          logoAlignment: google_web.GSIButtonLogoAlignment.left,
          minimumWidth: geometry.width,
          locale: 'en',
        ),
      ),
    );

    final apple = _PwaRasterButton(
      key: const Key('appleAuthButton'),
      semanticLabel: 'Continue with Apple',
      assetPath: _appleAsset(
        geometry: geometry,
        brightness: brightness,
      ),
      assetRoot: assetRoot,
      width: geometry.width,
      height: geometry.height,
      enabled: enabled,
      onPressed: onApple,
    );

    final email = _PwaEmailButton(
      key: const Key('emailAuthButton'),
      width: geometry.width,
      height: geometry.height,
      enabled: enabled,
      onPressed: onEmail,
    );

    final effectiveOrder = _effectiveOrder();
    final ordered = effectiveOrder == LogMatePwaProviderOrder.appleFirst
        ? <Widget>[apple, google, email]
        : <Widget>[google, apple, email];

    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        for (var i = 0; i < ordered.length; i++) ...[
          ordered[i],
          if (i != ordered.length - 1)
            SizedBox(height: geometry.gap),
        ],
      ],
    );
  }

  LogMatePwaProviderOrder _effectiveOrder() {
    if (order != LogMatePwaProviderOrder.automatic) return order;
    return AuthSurfaceSpec.hostFamily() == LogMateAuthHostFamily.apple
        ? LogMatePwaProviderOrder.appleFirst
        : LogMatePwaProviderOrder.googleFirst;
  }

  String _appleAsset({
    required LogMateAuthButtonGeometry geometry,
    required Brightness brightness,
  }) {
    final size = geometry.width <= 280 ? 'compact' : 'regular';
    final tone = brightness == Brightness.dark ? 'dark' : 'light';
    return 'apple_pwa_${size}_$tone.png';
  }
}

class _PwaRasterButton extends StatelessWidget {
  const _PwaRasterButton({
    super.key,
    required this.semanticLabel,
    required this.assetPath,
    required this.assetRoot,
    required this.width,
    required this.height,
    required this.enabled,
    required this.onPressed,
  });

  final String semanticLabel;
  final String assetPath;
  final String assetRoot;
  final double width;
  final double height;
  final bool enabled;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return Semantics(
      button: true,
      enabled: enabled,
      label: semanticLabel,
      child: SizedBox(
        width: width,
        height: height,
        child: GestureDetector(
          behavior: HitTestBehavior.opaque,
          onTap: enabled ? onPressed : null,
          child: Opacity(
            opacity: enabled ? 1 : 0.55,
            child: Image.asset(
              '$assetRoot/$assetPath',
              width: width,
              height: height,
              fit: BoxFit.fill,
              excludeFromSemantics: true,
            ),
          ),
        ),
      ),
    );
  }
}

class _PwaEmailButton extends StatelessWidget {
  const _PwaEmailButton({
    super.key,
    required this.width,
    required this.height,
    required this.enabled,
    required this.onPressed,
  });

  final double width;
  final double height;
  final bool enabled;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    final dark = Theme.of(context).brightness == Brightness.dark;
    return SizedBox(
      width: width,
      height: height,
      child: OutlinedButton.icon(
        onPressed: enabled ? onPressed : null,
        style: OutlinedButton.styleFrom(
          foregroundColor: dark
              ? const Color(0xFFE3E3E3)
              : const Color(0xFF1F1F1F),
          backgroundColor: dark
              ? const Color(0xFF131314)
              : Colors.white,
          side: BorderSide(
            color: dark
                ? const Color(0xFF8E918F)
                : const Color(0xFF747775),
          ),
          shape: const StadiumBorder(),
          padding: const EdgeInsets.symmetric(horizontal: 12),
          textStyle: const TextStyle(
            fontSize: 14,
            height: 20 / 14,
            fontWeight: FontWeight.w600,
          ),
        ),
        icon: const Icon(Icons.mail_outline, size: 18),
        label: const Text('Continue with Email'),
      ),
    );
  }
}
