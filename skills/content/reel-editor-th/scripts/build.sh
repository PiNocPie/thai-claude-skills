#!/usr/bin/env bash
# build.sh — assemble one Thai talking-head reel.
#
#   build.sh <source.mp4> <workdir> [style]
#
# Expects <workdir>/timeline.py to already exist (you author it per clip).
# style: clean (default) | bold | terminal
#
# Steps: HDR->SDR tonemap -> render caption/card overlay -> derive+mix SFX ->
# composite (no color filter, subtle push-in) -> tag bt709 -> covers.
# Outputs land in <workdir>/out/.
set -euo pipefail
SCRIPTS="$(cd "$(dirname "$0")" && pwd)"
SRC="$1"; WORK="$2"; STYLE="${3:-clean}"
mkdir -p "$WORK/out"

# make the engine importable next to the per-clip timeline.py
cp -f "$SCRIPTS"/render_*.py "$SCRIPTS/build_audio.py" "$WORK/"
cd "$WORK"

echo "[1/6] HDR->SDR tonemap (AVFoundation)"
if [ ! -x "$SCRIPTS/tonemap" ]; then
  swiftc -O "$SCRIPTS/tonemap.swift" -o "$SCRIPTS/tonemap" 2>/dev/null || true
fi
if [ -x "$SCRIPTS/tonemap" ]; then
  "$SCRIPTS/tonemap" "$SRC" out/sdr_master.mov && BASE="out/sdr_master.mov"
else
  echo "  (tonemap unavailable; using source directly — check colors!)"; BASE="$SRC"
fi

echo "[2/6] render overlay (captions+cards+CTA) style=$STYLE"
python3 render_overlay_video.py "$STYLE" "out/overlay_${STYLE}.mov"

echo "[3/6] derive + mix SFX"
python3 build_audio.py "$SRC" "out/sfx_mix.m4a"

echo "[4/6] composite (true color, no filter, subtle push-in)"
# trim=start_frame=1 drops the AVFoundation tonemap's washed first frame (base + overlay together)
ffmpeg -y -loglevel error -i "$BASE" -i "out/overlay_${STYLE}.mov" -filter_complex \
"[0:v]scale=1080:1920:flags=bicubic,zoompan=z='min(1.0+on/1600,1.09)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,setsar=1,trim=start_frame=1,setpts=PTS-STARTPTS[base];[1:v]trim=start_frame=1,setpts=PTS-STARTPTS[ov];[base][ov]overlay=0:0[v]" \
-map "[v]" -c:v hevc_videotoolbox -b:v 12M -tag:v hvc1 -colorspace bt709 -color_primaries bt709 -color_trc bt709 -r 30 -movflags +faststart "out/_video_${STYLE}.mp4"

echo "[5/6] mux audio + force bt709 tags"
ffmpeg -y -loglevel error -i "out/_video_${STYLE}.mp4" -i "out/sfx_mix.m4a" \
  -map 0:v -map 1:a -c:v copy -af "atrim=start=0.03334,asetpts=PTS-STARTPTS" -c:a aac -b:a 192k \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 \
  -movflags +faststart "out/reel_${STYLE}.mp4"

echo "[6/6] covers (from true-color frame)"
ffmpeg -y -loglevel error -ss 5 -i "$BASE" -vf "scale=1080:1920" -frames:v 1 -update 1 out/_face.jpg 2>/dev/null
python3 render_cover.py out/_face.jpg || true

echo "DONE -> $WORK/out/reel_${STYLE}.mp4"
ls -la "out/reel_${STYLE}.mp4" out/cover_*.jpg 2>/dev/null || true
