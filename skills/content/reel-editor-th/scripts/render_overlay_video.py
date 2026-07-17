# -*- coding: utf-8 -*-
"""Render the full-length RGBA overlay to a ProRes4444 .mov (alpha) by piping
raw frames to ffmpeg. Composites captions/hook/cta (render_captions) + demo
cards (render_cards, if available)."""
import sys, os, subprocess
import timeline as T
from render_captions import build_frame
try:
    import render_cards
    HAS_CARDS = True
except Exception as e:
    print("cards module not loaded:", e); HAS_CARDS = False

def main(style, out_path, with_cards=True):
    n = int(round(T.DUR * T.FPS))
    ff = subprocess.Popen([
        "ffmpeg","-y","-loglevel","error",
        "-f","rawvideo","-pix_fmt","rgba","-s",f"{T.W}x{T.H}","-r",str(T.FPS),"-i","-",
        "-c:v","prores_ks","-profile:v","4444","-pix_fmt","yuva444p10le",
        out_path
    ], stdin=subprocess.PIPE)
    for i in range(n):
        t = i / T.FPS
        img = build_frame(t, style)
        if with_cards and HAS_CARDS:
            render_cards.draw(img, t, style)
        ff.stdin.write(img.tobytes())
        if i % 150 == 0:
            print(f"  {style}: {i}/{n} frames")
    ff.stdin.close()
    rc = ff.wait()
    print(f"done {style} -> {out_path} rc={rc}")
    return rc

if __name__ == "__main__":
    style = sys.argv[1] if len(sys.argv)>1 else "bold"
    out = sys.argv[2] if len(sys.argv)>2 else f"assets/overlay_{style}.mov"
    wc = not (len(sys.argv)>3 and sys.argv[3]=="nocards")
    sys.exit(main(style, out, wc))
