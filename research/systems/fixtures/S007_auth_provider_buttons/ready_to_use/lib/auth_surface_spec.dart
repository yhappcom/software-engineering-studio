import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';

enum LogMateAuthSurface {
  mobile,
  tablet,
  pwa,
}

enum LogMateAuthHostFamily {
  apple,
  google,
  neutral,
}

@immutable
class LogMateAuthButtonGeometry {
  const LogMateAuthButtonGeometry({
    required this.width,
    required this.height,
    required this.gap,
  });

  final double width;
  final double height;
  final double gap;

  double get radius => height / 2;
}

abstract final class AuthSurfaceSpec {
  static const double _iosRatio = 188 / 44;
  static const double _androidRatio = 180 / 40;

  static LogMateAuthSurface resolve(
    BuildContext context, {
    LogMateAuthSurface? override,
  }) {
    if (override != null) return override;
    if (kIsWeb) return LogMateAuthSurface.pwa;
    return MediaQuery.sizeOf(context).shortestSide >= 600
        ? LogMateAuthSurface.tablet
        : LogMateAuthSurface.mobile;
  }

  static LogMateAuthHostFamily hostFamily() {
    return switch (defaultTargetPlatform) {
      TargetPlatform.iOS || TargetPlatform.macOS =>
        LogMateAuthHostFamily.apple,
      TargetPlatform.android => LogMateAuthHostFamily.google,
      _ => LogMateAuthHostFamily.neutral,
    };
  }

  static LogMateAuthButtonGeometry nativeGeometry({
    required LogMateAuthSurface surface,
    required TargetPlatform platform,
  }) {
    assert(surface != LogMateAuthSurface.pwa);
    final height = switch (surface) {
      LogMateAuthSurface.mobile => 48.0,
      LogMateAuthSurface.tablet => 56.0,
      LogMateAuthSurface.pwa => throw StateError('PWA uses pwaGeometry().'),
    };
    final ratio = switch (platform) {
      TargetPlatform.iOS => _iosRatio,
      TargetPlatform.android => _androidRatio,
      _ => _androidRatio,
    };
    return LogMateAuthButtonGeometry(
      width: height * ratio,
      height: height,
      gap: 12,
    );
  }

  static LogMateAuthButtonGeometry pwaGeometry({
    required double viewportWidth,
  }) {
    final width = viewportWidth < 400 ? 280.0 : 360.0;
    return LogMateAuthButtonGeometry(
      width: width,
      height: 40,
      gap: 12,
    );
  }
}
