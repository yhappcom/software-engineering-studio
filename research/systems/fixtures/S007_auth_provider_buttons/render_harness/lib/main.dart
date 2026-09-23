import 'package:flutter/material.dart';
import 'auth_button_preview.dart';

void main() {
  runApp(
    const AuthButtonPreview(
      platform: PreviewPlatform.ios,
      brightness: Brightness.light,
    ),
  );
}
