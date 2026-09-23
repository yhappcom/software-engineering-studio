import 'package:flutter/material.dart';

/// Displays a provider-approved image asset without redrawing or restyling it.
///
/// Authentication is deliberately injected through [onPressed]. This widget
/// has no authority over Firebase UID, provider linking, owner binding, or
/// onboarding state.
class OfficialProviderImageButton extends StatelessWidget {
  const OfficialProviderImageButton({
    super.key,
    required this.assetPath,
    required this.semanticLabel,
    required this.onPressed,
    this.height = 56,
    this.maxWidth = 375,
    this.enabled = true,
  });

  final String assetPath;
  final String semanticLabel;
  final VoidCallback onPressed;
  final double height;
  final double maxWidth;
  final bool enabled;

  @override
  Widget build(BuildContext context) {
    return Semantics(
      button: true,
      enabled: enabled,
      label: semanticLabel,
      child: ConstrainedBox(
        constraints: BoxConstraints(maxWidth: maxWidth, minHeight: height),
        child: SizedBox(
          width: double.infinity,
          height: height,
          child: IgnorePointer(
            ignoring: !enabled,
            child: GestureDetector(
              behavior: HitTestBehavior.opaque,
              onTap: enabled ? onPressed : null,
              child: Opacity(
                opacity: enabled ? 1 : 0.55,
                child: Image.asset(
                  assetPath,
                  fit: BoxFit.contain,
                  alignment: Alignment.center,
                  excludeFromSemantics: true,
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

/// LogMate-owned Email auth button.
///
/// Keep its overall prominence comparable to Apple/Google, while provider
/// artwork remains provider-owned.
class LogMateEmailAuthButton extends StatelessWidget {
  const LogMateEmailAuthButton({
    super.key,
    required this.onPressed,
    this.enabled = true,
    this.label = 'Continue with Email',
  });

  final VoidCallback onPressed;
  final bool enabled;
  final String label;

  @override
  Widget build(BuildContext context) {
    return ConstrainedBox(
      constraints: const BoxConstraints(maxWidth: 375),
      child: SizedBox(
        width: double.infinity,
        height: 56,
        child: OutlinedButton(
          onPressed: enabled ? onPressed : null,
          child: Text(label),
        ),
      ),
    );
  }
}
