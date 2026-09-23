import 'dart:ui' as ui;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:s007_auth_button_render_harness/auth_button_preview.dart';

Future<ui.Size> _assetNaturalSize(String path) async {
  final data = await rootBundle.load(path);
  final codec = await ui.instantiateImageCodec(data.buffer.asUint8List());
  final frame = await codec.getNextFrame();
  return ui.Size(
    frame.image.width.toDouble(),
    frame.image.height.toDouble(),
  );
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  Future<void> render(
    WidgetTester tester, {
    required PreviewPlatform platform,
    required Brightness brightness,
    required String golden,
  }) async {
    await tester.binding.setSurfaceSize(const Size(430, 932));
    addTearDown(() => tester.binding.setSurfaceSize(null));

    await tester.pumpWidget(
      AuthButtonPreview(platform: platform, brightness: brightness),
    );
    await tester.pumpAndSettle();

    for (final key in const ['appleButton', 'googleButton', 'emailButton']) {
      final size = tester.getSize(find.byKey(Key(key)));
      expect(size.width, AuthButtonPreview.buttonWidth);
      expect(size.height, AuthButtonPreview.buttonHeight);
    }

    final apple = tester.getTopLeft(find.byKey(const Key('appleButton')));
    final google = tester.getTopLeft(find.byKey(const Key('googleButton')));
    final email = tester.getTopLeft(find.byKey(const Key('emailButton')));

    if (platform == PreviewPlatform.ios) {
      expect(apple.dy, lessThan(google.dy));
      expect(google.dy, lessThan(email.dy));
      expect(
        google.dy - (apple.dy + AuthButtonPreview.buttonHeight),
        AuthButtonPreview.gap,
      );
      expect(
        email.dy - (google.dy + AuthButtonPreview.buttonHeight),
        AuthButtonPreview.gap,
      );
    } else {
      expect(google.dy, lessThan(apple.dy));
      expect(apple.dy, lessThan(email.dy));
      expect(
        apple.dy - (google.dy + AuthButtonPreview.buttonHeight),
        AuthButtonPreview.gap,
      );
      expect(
        email.dy - (apple.dy + AuthButtonPreview.buttonHeight),
        AuthButtonPreview.gap,
      );
    }

    expect(
      find.bySemanticsLabel('Continue with Apple'),
      findsOneWidget,
    );
    expect(
      find.bySemanticsLabel('Continue with Google'),
      findsOneWidget,
    );
    expect(find.text('Continue with Email'), findsOneWidget);

    await expectLater(
      find.byType(MaterialApp),
      matchesGoldenFile(golden),
    );
  }

  testWidgets('iOS light geometry + golden', (tester) async {
    await render(
      tester,
      platform: PreviewPlatform.ios,
      brightness: Brightness.light,
      golden: 'goldens/ios_light.png',
    );
  });

  testWidgets('iOS dark geometry + golden', (tester) async {
    await render(
      tester,
      platform: PreviewPlatform.ios,
      brightness: Brightness.dark,
      golden: 'goldens/ios_dark.png',
    );
  });

  testWidgets('Android light geometry + golden', (tester) async {
    await render(
      tester,
      platform: PreviewPlatform.android,
      brightness: Brightness.light,
      golden: 'goldens/android_light.png',
    );
  });

  testWidgets('Android dark geometry + golden', (tester) async {
    await render(
      tester,
      platform: PreviewPlatform.android,
      brightness: Brightness.dark,
      golden: 'goldens/android_dark.png',
    );
  });

  test('selected provider assets decode and preserve positive dimensions', () async {
    const paths = <String>[
      'assets/apple_light.png',
      'assets/apple_dark.png',
      'assets/google_ios_light.png',
      'assets/google_ios_dark.png',
      'assets/google_android_light.png',
      'assets/google_android_dark.png',
    ];

    for (final path in paths) {
      final size = await _assetNaturalSize(path);
      expect(size.width, greaterThan(0));
      expect(size.height, greaterThan(0));
      // Print dimensions into hosted evidence logs.
      // ignore: avoid_print
      print('ASSET_SIZE $path ${size.width.toInt()}x${size.height.toInt()}');
    }
  });
}
