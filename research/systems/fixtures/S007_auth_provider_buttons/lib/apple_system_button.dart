import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

/// Native iOS/iPadOS bridge for Apple's system-provided
/// ASAuthorizationAppleIDButton.
///
/// Register OfficialAppleSignInButtonFactory.swift with the platform-view id
/// 'logmate/apple-sign-in-button'.
class AppleSystemSignInButton extends StatelessWidget {
  const AppleSystemSignInButton({
    super.key,
    required this.onPressed,
    this.height = 56,
  });

  final VoidCallback onPressed;
  final double height;

  @override
  Widget build(BuildContext context) {
    if (kIsWeb || defaultTargetPlatform != TargetPlatform.iOS) {
      throw UnsupportedError(
        'AppleSystemSignInButton is for native iOS/iPadOS only.',
      );
    }

    return ConstrainedBox(
      constraints: const BoxConstraints(maxWidth: 375),
      child: SizedBox(
        width: double.infinity,
        height: height,
        child: UiKitView(
          viewType: 'logmate/apple-sign-in-button',
          creationParams: <String, Object?>{
            'style': Theme.of(context).brightness == Brightness.dark
                ? 'white'
                : 'black',
            'type': 'continue',
            'cornerRadius': 12.0,
          },
          creationParamsCodec: const StandardMessageCodec(),
          onPlatformViewCreated: (int viewId) {
            final channel = MethodChannel(
              'logmate/apple-sign-in-button/$viewId',
            );
            channel.setMethodCallHandler((MethodCall call) async {
              if (call.method == 'pressed') {
                onPressed();
              }
            });
          },
        ),
      ),
    );
  }
}
