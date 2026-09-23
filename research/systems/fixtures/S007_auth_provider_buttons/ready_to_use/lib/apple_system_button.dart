import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class LogMateAppleSystemButton extends StatelessWidget {
  const LogMateAppleSystemButton({
    super.key,
    required this.onPressed,
    required this.width,
    required this.height,
  });

  final VoidCallback onPressed;
  final double width;
  final double height;

  @override
  Widget build(BuildContext context) {
    if (kIsWeb || defaultTargetPlatform != TargetPlatform.iOS) {
      throw UnsupportedError(
        'LogMateAppleSystemButton is only for native iOS/iPadOS.',
      );
    }

    return SizedBox(
      width: width,
      height: height,
      child: UiKitView(
        viewType: 'logmate/apple-sign-in-button',
        creationParams: <String, Object?>{
          'style': Theme.of(context).brightness == Brightness.dark
              ? 'white'
              : 'black',
          'type': 'continue',
          'cornerRadius': height / 2,
        },
        creationParamsCodec: const StandardMessageCodec(),
        onPlatformViewCreated: (int viewId) {
          final channel = MethodChannel(
            'logmate/apple-sign-in-button/$viewId',
          );
          channel.setMethodCallHandler((MethodCall call) async {
            if (call.method == 'pressed') onPressed();
          });
        },
      ),
    );
  }
}
