import 'package:flutter/material.dart';

enum PreviewPlatform { ios, android }

class AuthButtonPreview extends StatelessWidget {
  const AuthButtonPreview({
    super.key,
    required this.platform,
    required this.brightness,
  });

  final PreviewPlatform platform;
  final Brightness brightness;

  static const double buttonWidth = 375;
  static const double buttonHeight = 56;
  static const double gap = 12;

  String get _appleAsset => brightness == Brightness.dark
      ? 'assets/apple_dark.png'
      : 'assets/apple_light.png';

  String get _googleAsset {
    if (platform == PreviewPlatform.ios) {
      return brightness == Brightness.dark
          ? 'assets/google_ios_dark.png'
          : 'assets/google_ios_light.png';
    }
    return brightness == Brightness.dark
        ? 'assets/google_android_dark.png'
        : 'assets/google_android_light.png';
  }

  @override
  Widget build(BuildContext context) {
    final isDark = brightness == Brightness.dark;
    final background = isDark ? const Color(0xFF101214) : const Color(0xFFF7F8FA);
    final foreground = isDark ? Colors.white : const Color(0xFF17191C);
    final border = isDark ? const Color(0xFF9AA0A6) : const Color(0xFF74777C);

    final apple = _ProviderImageSlot(
      key: const Key('appleButton'),
      semanticLabel: 'Continue with Apple',
      assetPath: _appleAsset,
    );
    final google = _ProviderImageSlot(
      key: const Key('googleButton'),
      semanticLabel: 'Continue with Google',
      assetPath: _googleAsset,
    );
    final email = SizedBox(
      key: const Key('emailButton'),
      width: buttonWidth,
      height: buttonHeight,
      child: OutlinedButton(
        style: OutlinedButton.styleFrom(
          foregroundColor: foreground,
          backgroundColor: isDark ? const Color(0xFF101214) : Colors.white,
          side: BorderSide(color: border),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
          textStyle: const TextStyle(
            fontSize: 16,
            fontWeight: FontWeight.w600,
            height: 1,
          ),
        ),
        onPressed: () {},
        child: const Text('Continue with Email'),
      ),
    );

    final ordered = platform == PreviewPlatform.ios
        ? <Widget>[apple, google, email]
        : <Widget>[google, apple, email];

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        brightness: brightness,
        useMaterial3: true,
      ),
      home: Scaffold(
        backgroundColor: background,
        body: SafeArea(
          child: Center(
            child: SizedBox(
              width: 430,
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 27.5),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text(
                      'LogMate',
                      style: TextStyle(
                        color: foreground,
                        fontSize: 34,
                        fontWeight: FontWeight.w800,
                        letterSpacing: -1,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      'Sign in to continue',
                      style: TextStyle(
                        color: foreground.withValues(alpha: 0.70),
                        fontSize: 16,
                      ),
                    ),
                    const SizedBox(height: 40),
                    for (var i = 0; i < ordered.length; i++) ...[
                      ordered[i],
                      if (i != ordered.length - 1)
                        const SizedBox(height: gap),
                    ],
                    const SizedBox(height: 20),
                    Text(
                      platform == PreviewPlatform.ios
                          ? 'iOS / iPadOS order'
                          : 'Android order',
                      style: TextStyle(
                        color: foreground.withValues(alpha: 0.55),
                        fontSize: 12,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class _ProviderImageSlot extends StatelessWidget {
  const _ProviderImageSlot({
    super.key,
    required this.semanticLabel,
    required this.assetPath,
  });

  final String semanticLabel;
  final String assetPath;

  @override
  Widget build(BuildContext context) {
    return Semantics(
      button: true,
      label: semanticLabel,
      child: SizedBox(
        width: AuthButtonPreview.buttonWidth,
        height: AuthButtonPreview.buttonHeight,
        child: Image.asset(
          assetPath,
          fit: BoxFit.contain,
          filterQuality: FilterQuality.high,
          excludeFromSemantics: true,
        ),
      ),
    );
  }
}
