import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:logmate_auth_button_kit/auth_surface_spec.dart';

enum _PreviewPlatform { ios, android, pwa }

class _ReadyPreview extends StatelessWidget {
  const _ReadyPreview({
    required this.platform,
    required this.surface,
    required this.brightness,
    this.pwaWidth,
  });

  final _PreviewPlatform platform;
  final LogMateAuthSurface surface;
  final Brightness brightness;
  final double? pwaWidth;

  @override
  Widget build(BuildContext context) {
    final dark = brightness == Brightness.dark;
    final geometry = platform == _PreviewPlatform.pwa
        ? AuthSurfaceSpec.pwaGeometry(viewportWidth: pwaWidth ?? 390)
        : AuthSurfaceSpec.nativeGeometry(
            surface: surface,
            platform: platform == _PreviewPlatform.ios
                ? TargetPlatform.iOS
                : TargetPlatform.android,
          );

    final apple = _assetButton(
      asset: _appleAsset(geometry),
      width: geometry.width,
      height: geometry.height,
    );
    final google = platform == _PreviewPlatform.pwa
        ? _gisReference(geometry)
        : _assetButton(
            asset: dark
                ? (platform == _PreviewPlatform.ios
                    ? 'assets/google_ios_dark.png'
                    : 'assets/google_android_dark.png')
                : (platform == _PreviewPlatform.ios
                    ? 'assets/google_ios_light.png'
                    : 'assets/google_android_light.png'),
            width: geometry.width,
            height: geometry.height,
          );
    final email = _email(geometry);

    final appleFirst = platform == _PreviewPlatform.ios;
    final children = appleFirst
        ? <Widget>[apple, google, email]
        : <Widget>[google, apple, email];

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        brightness: brightness,
        useMaterial3: true,
      ),
      home: Scaffold(
        backgroundColor: dark
            ? const Color(0xFF101214)
            : const Color(0xFFF7F8FA),
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              for (var i = 0; i < children.length; i++) ...[
                children[i],
                if (i != children.length - 1)
                  SizedBox(height: geometry.gap),
              ],
              const SizedBox(height: 24),
              Text(
                _caption(geometry),
                style: TextStyle(
                  fontSize: 12,
                  color: dark ? Colors.white60 : Colors.black54,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  String _appleAsset(LogMateAuthButtonGeometry g) {
    final tone = brightness == Brightness.dark ? 'dark' : 'light';
    if (platform == _PreviewPlatform.ios) {
      final size = surface == LogMateAuthSurface.tablet
          ? 'tablet'
          : 'mobile';
      return 'assets/apple_ios_${size}_ref_$tone.png';
    }
    if (platform == _PreviewPlatform.android) {
      final size = surface == LogMateAuthSurface.tablet
          ? 'tablet'
          : 'mobile';
      return 'assets/apple_android_${size}_$tone.png';
    }
    final size = g.width <= 280 ? 'compact' : 'regular';
    return 'assets/apple_pwa_${size}_$tone.png';
  }

  String _caption(LogMateAuthButtonGeometry g) {
    final kind = switch (platform) {
      _PreviewPlatform.ios => surface == LogMateAuthSurface.tablet
          ? 'iPadOS tablet'
          : 'iOS mobile',
      _PreviewPlatform.android => surface == LogMateAuthSurface.tablet
          ? 'Android tablet'
          : 'Android mobile',
      _PreviewPlatform.pwa => 'PWA reference',
    };
    return '$kind · ${g.width.toStringAsFixed(1)}×${g.height.toStringAsFixed(0)}';
  }

  Widget _assetButton({
    required String asset,
    required double width,
    required double height,
  }) {
    return SizedBox(
      width: width,
      height: height,
      child: Image.asset(
        asset,
        width: width,
        height: height,
        fit: BoxFit.contain,
      ),
    );
  }

  Widget _gisReference(LogMateAuthButtonGeometry g) {
    final dark = brightness == Brightness.dark;
    return Container(
      width: g.width,
      height: g.height,
      alignment: Alignment.center,
      decoration: ShapeDecoration(
        color: dark ? const Color(0xFF131314) : Colors.white,
        shape: StadiumBorder(
          side: BorderSide(
            color: dark
                ? const Color(0xFF8E918F)
                : const Color(0xFF747775),
          ),
        ),
      ),
      child: Text(
        'Google GIS renderButton()',
        style: TextStyle(
          fontSize: 12,
          fontWeight: FontWeight.w600,
          color: dark
              ? const Color(0xFFE3E3E3)
              : const Color(0xFF1F1F1F),
        ),
      ),
    );
  }

  Widget _email(LogMateAuthButtonGeometry g) {
    final dark = brightness == Brightness.dark;
    return SizedBox(
      width: g.width,
      height: g.height,
      child: OutlinedButton.icon(
        onPressed: () {},
        style: OutlinedButton.styleFrom(
          backgroundColor: dark
              ? const Color(0xFF131314)
              : Colors.white,
          foregroundColor: dark
              ? const Color(0xFFE3E3E3)
              : const Color(0xFF1F1F1F),
          side: BorderSide(
            color: dark
                ? const Color(0xFF8E918F)
                : const Color(0xFF747775),
          ),
          shape: const StadiumBorder(),
        ),
        icon: const Icon(Icons.mail_outline, size: 18),
        label: const Text('Sign in with Email'),
      ),
    );
  }
}

Future<void> _golden(
  WidgetTester tester, {
  required _PreviewPlatform platform,
  required LogMateAuthSurface surface,
  required Brightness brightness,
  required String file,
  double? pwaWidth,
}) async {
  await tester.binding.setSurfaceSize(
    platform == _PreviewPlatform.pwa
        ? Size(pwaWidth ?? 390, 844)
        : surface == LogMateAuthSurface.tablet
            ? const Size(1024, 768)
            : const Size(430, 932),
  );
  addTearDown(() => tester.binding.setSurfaceSize(null));

  await tester.pumpWidget(
    _ReadyPreview(
      platform: platform,
      surface: surface,
      brightness: brightness,
      pwaWidth: pwaWidth,
    ),
  );
  await tester.pumpAndSettle();

  await expectLater(
    find.byType(MaterialApp),
    matchesGoldenFile(file),
  );
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  for (final brightness in Brightness.values) {
    final suffix = brightness == Brightness.light ? 'light' : 'dark';

    testWidgets('mobile iOS $suffix', (tester) async {
      await _golden(
        tester,
        platform: _PreviewPlatform.ios,
        surface: LogMateAuthSurface.mobile,
        brightness: brightness,
        file: 'goldens/mobile_ios_$suffix.png',
      );
    });

    testWidgets('mobile Android $suffix', (tester) async {
      await _golden(
        tester,
        platform: _PreviewPlatform.android,
        surface: LogMateAuthSurface.mobile,
        brightness: brightness,
        file: 'goldens/mobile_android_$suffix.png',
      );
    });

    testWidgets('tablet iPadOS $suffix', (tester) async {
      await _golden(
        tester,
        platform: _PreviewPlatform.ios,
        surface: LogMateAuthSurface.tablet,
        brightness: brightness,
        file: 'goldens/tablet_ipados_$suffix.png',
      );
    });

    testWidgets('tablet Android $suffix', (tester) async {
      await _golden(
        tester,
        platform: _PreviewPlatform.android,
        surface: LogMateAuthSurface.tablet,
        brightness: brightness,
        file: 'goldens/tablet_android_$suffix.png',
      );
    });

    testWidgets('PWA compact structural reference $suffix', (tester) async {
      await _golden(
        tester,
        platform: _PreviewPlatform.pwa,
        surface: LogMateAuthSurface.pwa,
        brightness: brightness,
        file: 'goldens/pwa_compact_$suffix.png',
        pwaWidth: 360,
      );
    });

    testWidgets('PWA regular structural reference $suffix', (tester) async {
      await _golden(
        tester,
        platform: _PreviewPlatform.pwa,
        surface: LogMateAuthSurface.pwa,
        brightness: brightness,
        file: 'goldens/pwa_regular_$suffix.png',
        pwaWidth: 900,
      );
    });
  }
}
