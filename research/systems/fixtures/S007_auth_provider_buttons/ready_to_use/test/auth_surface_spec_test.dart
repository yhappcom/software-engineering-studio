import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:logmate_auth_button_kit/auth_surface_spec.dart';

void main() {
  group('surface geometry', () {
    test('iOS mobile preserves Google iOS aspect ratio at 48 high', () {
      const ratio = 188 / 44;
      final g = AuthSurfaceSpec.nativeGeometry(
        surface: LogMateAuthSurface.mobile,
        platform: TargetPlatform.iOS,
      );
      expect(g.height, 48);
      expect(g.width, closeTo(48 * ratio, 0.0001));
      expect(g.radius, 24);
      expect(g.gap, 12);
    });

    test('Android mobile is 216x48', () {
      final g = AuthSurfaceSpec.nativeGeometry(
        surface: LogMateAuthSurface.mobile,
        platform: TargetPlatform.android,
      );
      expect(g.width, 216);
      expect(g.height, 48);
    });

    test('iPad tablet preserves iOS ratio at 56 high', () {
      final g = AuthSurfaceSpec.nativeGeometry(
        surface: LogMateAuthSurface.tablet,
        platform: TargetPlatform.iOS,
      );
      expect(g.width, closeTo(56 * 188 / 44, 0.0001));
      expect(g.height, 56);
    });

    test('Android tablet is 252x56', () {
      final g = AuthSurfaceSpec.nativeGeometry(
        surface: LogMateAuthSurface.tablet,
        platform: TargetPlatform.android,
      );
      expect(g.width, 252);
      expect(g.height, 56);
    });

    test('PWA compact and regular footprints', () {
      final compact = AuthSurfaceSpec.pwaGeometry(viewportWidth: 360);
      final regular = AuthSurfaceSpec.pwaGeometry(viewportWidth: 361);
      expect(compact.width, 280);
      expect(compact.height, 40);
      expect(regular.width, 360);
      expect(regular.height, 40);
    });
  });
}
