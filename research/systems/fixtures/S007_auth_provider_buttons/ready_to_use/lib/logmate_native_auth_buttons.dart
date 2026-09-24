import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

import 'apple_system_button.dart';
import 'auth_surface_spec.dart';

class LogMateNativeAuthButtons extends StatelessWidget {
  const LogMateNativeAuthButtons({
    super.key,
    required this.onApple,
    required this.onGoogle,
    required this.onEmail,
    this.surfaceOverride,
    this.assetRoot = 'assets/auth',
    this.enabled = true,
  });

  final VoidCallback onApple;
  final VoidCallback onGoogle;
  final VoidCallback onEmail;
  final LogMateAuthSurface? surfaceOverride;
  final String assetRoot;
  final bool enabled;

  @override
  Widget build(BuildContext context) {
    if (kIsWeb) {
      throw UnsupportedError(
        'Use LogMatePwaAuthButtons on Web/PWA.',
      );
    }

    final surface = AuthSurfaceSpec.resolve(
      context,
      override: surfaceOverride,
    );
    if (surface == LogMateAuthSurface.pwa) {
      throw StateError('Native component received a PWA surface.');
    }

    final platform = defaultTargetPlatform;
    if (platform != TargetPlatform.iOS &&
        platform != TargetPlatform.android) {
      throw UnsupportedError(
        'LogMate native auth buttons support iOS/iPadOS and Android.',
      );
    }

    final geometry = AuthSurfaceSpec.nativeGeometry(
      surface: surface,
      platform: platform,
    );
    final brightness = Theme.of(context).brightness;

    final apple = platform == TargetPlatform.iOS
        ? IgnorePointer(
            ignoring: !enabled,
            child: Opacity(
              opacity: enabled ? 1 : 0.55,
              child: LogMateAppleSystemButton(
                key: const Key('appleAuthButton'),
                onPressed: onApple,
                width: geometry.width,
                height: geometry.height,
              ),
            ),
          )
        : _OfficialRasterButton(
            key: const Key('appleAuthButton'),
            assetPath: _appleAndroidAsset(
              surface: surface,
              brightness: brightness,
            ),
            semanticLabel: 'Continue with Apple',
            width: geometry.width,
            height: geometry.height,
            onPressed: onApple,
            enabled: enabled,
            assetRoot: assetRoot,
          );

    final google = _OfficialRasterButton(
      key: const Key('googleAuthButton'),
      assetPath: _googleAsset(
        platform: platform,
        brightness: brightness,
      ),
      semanticLabel: 'Continue with Google',
      width: geometry.width,
      height: geometry.height,
      onPressed: onGoogle,
      enabled: enabled,
      assetRoot: assetRoot,
    );

    final email = _EmailButton(
      key: const Key('emailAuthButton'),
      width: geometry.width,
      height: geometry.height,
      onPressed: onEmail,
      enabled: enabled,
    );

    final ordered = platform == TargetPlatform.iOS
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

  String _googleAsset({
    required TargetPlatform platform,
    required Brightness brightness,
  }) {
    final tone = brightness == Brightness.dark ? 'dark' : 'light';
    return platform == TargetPlatform.iOS
        ? 'google_ios_$tone.png'
        : 'google_android_$tone.png';
  }

  String _appleAndroidAsset({
    required LogMateAuthSurface surface,
    required Brightness brightness,
  }) {
    final size = surface == LogMateAuthSurface.tablet
        ? 'tablet'
        : 'mobile';
    final tone = brightness == Brightness.dark ? 'dark' : 'light';
    return 'apple_android_${size}_$tone.png';
  }
}

class _OfficialRasterButton extends StatelessWidget {
  const _OfficialRasterButton({
    super.key,
    required this.assetPath,
    required this.semanticLabel,
    required this.width,
    required this.height,
    required this.onPressed,
    required this.enabled,
    required this.assetRoot,
  });

  final String assetPath;
  final String semanticLabel;
  final double width;
  final double height;
  final VoidCallback onPressed;
  final bool enabled;
  final String assetRoot;

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
              fit: BoxFit.contain,
              excludeFromSemantics: true,
              filterQuality: FilterQuality.high,
            ),
          ),
        ),
      ),
    );
  }
}

class _EmailButton extends StatelessWidget {
  const _EmailButton({
    super.key,
    required this.width,
    required this.height,
    required this.onPressed,
    required this.enabled,
  });

  final double width;
  final double height;
  final VoidCallback onPressed;
  final bool enabled;

  @override
  Widget build(BuildContext context) {
    final dark = Theme.of(context).brightness == Brightness.dark;
    final foreground = dark
        ? const Color(0xFFE3E3E3)
        : const Color(0xFF1F1F1F);
    final background = dark
        ? const Color(0xFF131314)
        : const Color(0xFFFFFFFF);
    final border = dark
        ? const Color(0xFF8E918F)
        : const Color(0xFF747775);

    return SizedBox(
      width: width,
      height: height,
      child: OutlinedButton.icon(
        onPressed: enabled ? onPressed : null,
        style: OutlinedButton.styleFrom(
          foregroundColor: foreground,
          backgroundColor: background,
          side: BorderSide(color: border),
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
