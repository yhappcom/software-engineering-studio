#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIT="$(cd "$HERE/.." && pwd)"
SRC="$KIT/assets"
DST="$HERE/assets"

mkdir -p "$DST"
rm -f "$DST"/*.png

cp "$SRC/apple/center_continue_black_375x56@3x.png"   "$DST/apple_light.png"
cp "$SRC/apple/center_continue_white_outline_375x56@3x.png"   "$DST/apple_dark.png"

cp "$SRC/google/iOS/PNG @3x/Neutral/Theme=Light, Show text=Yes, Shape=Pill, Platform=iOS@3x.png"   "$DST/google_ios_light.png"
cp "$SRC/google/iOS/PNG @3x/Dark/Theme=Dark, Show text=Yes, Shape=Pill, Platform=iOS@3x.png"   "$DST/google_ios_dark.png"

cp "$SRC/google/Android + Web/PNG @3x/Light/Theme=Light, Show text=Yes, Shape=Pill, Platform=Android+Web@3x.png"   "$DST/google_android_light.png"
cp "$SRC/google/Android + Web/PNG @3x/Dark/Theme=Dark, Show text=Yes, Shape=Pill, Platform=Android+Web@3x.png"   "$DST/google_android_dark.png"

printf 'Prepared render assets:\n'
find "$DST" -maxdepth 1 -type f -name '*.png' -print | sort
