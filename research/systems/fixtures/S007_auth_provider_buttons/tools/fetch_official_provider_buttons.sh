#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ASSETS="$ROOT/assets"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$ASSETS/google" "$ASSETS/apple"
rm -rf "$ASSETS/google"/* "$ASSETS/apple"/*

GOOGLE_URL="https://developers.google.com/static/identity/images/signin-assets.zip"
GOOGLE_ZIP="$TMP/signin-assets.zip"

echo "Fetching Google pre-approved Sign in with Google assets..."
curl --fail --location --silent --show-error "$GOOGLE_URL" -o "$GOOGLE_ZIP"
unzip -q "$GOOGLE_ZIP" -d "$TMP/google"

# Keep only PNG resources. Do not vendor Google Sans or other fonts.
while IFS= read -r -d '' file; do
  rel="${file#"$TMP/google/"}"
  mkdir -p "$ASSETS/google/$(dirname "$rel")"
  cp "$file" "$ASSETS/google/$rel"
done < <(find "$TMP/google" -type f -iname '*.png' -print0)

echo "Generating Apple-approved Sign in with Apple PNGs..."
APPLE_CENTER="https://appleid.cdn-apple.com/appleid/button"
APPLE_LEFT="https://appleid.cdn-apple.com/appleid/button/left"
APPLE_LOGO="https://appleid.cdn-apple.com/appleid/button/logo"

fetch_apple_button() {
  local endpoint="$1"
  local output="$2"
  local color="$3"
  local border="$4"
  local type="$5"

  curl --fail --get --silent --show-error "$endpoint"     --data-urlencode "height=56"     --data-urlencode "width=375"     --data-urlencode "color=$color"     --data-urlencode "border=$border"     --data-urlencode "type=$type"     --data-urlencode "border_radius=12"     --data-urlencode "scale=3"     --data-urlencode "locale=en_US"     -o "$ASSETS/apple/$output"
}

for mode in center left; do
  if [[ "$mode" == "center" ]]; then endpoint="$APPLE_CENTER"; else endpoint="$APPLE_LEFT"; fi
  for type in sign-in continue; do
    fetch_apple_button "$endpoint" "${mode}_${type}_black_375x56@3x.png" black false "$type"
    fetch_apple_button "$endpoint" "${mode}_${type}_white_375x56@3x.png" white false "$type"
    fetch_apple_button "$endpoint" "${mode}_${type}_white_outline_375x56@3x.png" white true "$type"
  done
done

for color in black white; do
  curl --fail --get --silent --show-error "$APPLE_LOGO"     --data-urlencode "size=56"     --data-urlencode "color=$color"     --data-urlencode "border=false"     --data-urlencode "border_radius=12"     --data-urlencode "scale=3"     -o "$ASSETS/apple/logo_${color}_56@3x.png"
done

{
  echo "Generated: $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
  echo "Google source: $GOOGLE_URL"
  echo "Apple center source: $APPLE_CENTER"
  echo "Apple left source: $APPLE_LEFT"
  echo "Apple logo source: $APPLE_LOGO"
  echo
  echo "SHA-256:"
  find "$ASSETS" -type f ! -name SOURCE_MANIFEST.txt -print0     | sort -z     | xargs -0 sha256sum
} > "$ASSETS/SOURCE_MANIFEST.txt"

echo "Provider assets prepared under: $ASSETS"
