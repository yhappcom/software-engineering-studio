#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIT="$(cd "$HERE/.." && pwd)"
CANONICAL="$KIT/assets"
OUT="$HERE/assets"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$OUT"
rm -f "$OUT"/*.png "$OUT"/SOURCE_MANIFEST.txt

# Google: preserve provider-approved artwork and aspect ratio.
cp "$CANONICAL/google/iOS/PNG @3x/Light/Theme=Light, Show text=Yes, Shape=Pill, Platform=iOS@3x.png"   "$OUT/google_ios_light.png"
cp "$CANONICAL/google/iOS/PNG @3x/Dark/Theme=Dark, Show text=Yes, Shape=Pill, Platform=iOS@3x.png"   "$OUT/google_ios_dark.png"
cp "$CANONICAL/google/Android + Web/PNG @3x/Light/Theme=Light, Show text=Yes, Shape=Pill, Platform=Android+Web@3x.png"   "$OUT/google_android_light.png"
cp "$CANONICAL/google/Android + Web/PNG @3x/Dark/Theme=Dark, Show text=Yes, Shape=Pill, Platform=Android+Web@3x.png"   "$OUT/google_android_dark.png"

APPLE="https://appleid.cdn-apple.com/appleid/button"

fetch_apple() {
  local output="$1"
  local width="$2"
  local height="$3"
  local color="$4"
  local border="$5"
  local radius="$6"

  curl --fail --get --silent --show-error "$APPLE"     --data-urlencode "width=$width"     --data-urlencode "height=$height"     --data-urlencode "color=$color"     --data-urlencode "border=$border"     --data-urlencode "type=sign-in"     --data-urlencode "border_radius=$radius"     --data-urlencode "scale=3"     --data-urlencode "locale=en_US"     -o "$OUT/$output"
}

# iOS/iPad images are references for hosted render validation only.
# Production iOS/iPadOS uses ASAuthorizationAppleIDButton.
fetch_apple apple_ios_mobile_ref_light.png 205 48 black false 24
fetch_apple apple_ios_mobile_ref_dark.png 205 48 white true 24
fetch_apple apple_ios_tablet_ref_light.png 239 56 black false 28
fetch_apple apple_ios_tablet_ref_dark.png 239 56 white true 28

# Android production-ready bundled Apple buttons.
fetch_apple apple_android_mobile_light.png 216 48 black false 24
fetch_apple apple_android_mobile_dark.png 216 48 white true 24
fetch_apple apple_android_tablet_light.png 252 56 black false 28
fetch_apple apple_android_tablet_dark.png 252 56 white true 28

# PWA Apple buttons match the configured Google GIS width.
fetch_apple apple_pwa_compact_light.png 280 40 black false 20
fetch_apple apple_pwa_compact_dark.png 280 40 white true 20
fetch_apple apple_pwa_regular_light.png 360 40 black false 20
fetch_apple apple_pwa_regular_dark.png 360 40 white true 20

{
  echo "Manifest: deterministic; generation timestamp intentionally omitted"
  echo "Apple source: $APPLE"
  echo "Google source: canonical Studio provider asset set generated from https://developers.google.com/static/identity/images/signin-assets.zip"
  echo
  echo "SHA-256:"
  find "$OUT" -type f -name '*.png' -print0 | sort -z | xargs -0 sha256sum
} > "$OUT/SOURCE_MANIFEST.txt"

echo "Ready-to-use auth assets prepared under: $OUT"
