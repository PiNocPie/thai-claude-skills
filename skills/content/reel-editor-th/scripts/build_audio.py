# -*- coding: utf-8 -*-
"""Build the SFX-mixed audio track for a reel.

SFX are derived automatically from timeline.py so you almost never hand-place
them: a whoosh on every demo-card slide-in, pops on number captions, a chime on
the reveal beat, an impact on the punchline. Override by defining SFX_EVENTS in
timeline.py (list of (time_seconds, sfx_name, gain)).

Usage: python3 build_audio.py <source_or_sdr.mp4> <out.m4a> [sfx_dir]
The source's own audio is the voiceover bed; SFX are layered on top (they do not
duck the voice — they sit under it at low gain).
"""
import sys, os, subprocess
import timeline as T

DEFAULT_SFX = os.path.expanduser("~/.claude/skills/hyperframes-media/assets/sfx")

def derive_events():
    if hasattr(T, "SFX_EVENTS") and T.SFX_EVENTS:
        return list(T.SFX_EVENTS)
    ev = []
    # whoosh on each demo card slide-in
    for st, en, cid in getattr(T, "INSERTS", []):
        ev.append((round(st + 0.05, 2), "whoosh-short", 0.30))
    # chime on the reveal beat if defined, else on the first insert
    reveal = getattr(T, "REVEAL_T", None)
    if reveal is not None:
        ev.append((round(reveal, 2), "chime", 0.42))
    # pops on number-only captions (e.g. "1 2 3 4")
    for st, en, text, emph in T.CAPTIONS:
        toks = text.split()
        if toks and all(t.strip().isdigit() for t in toks):
            span = (en - st) / max(1, len(toks))
            for i in range(len(toks)):
                ev.append((round(st + i * span, 2), "pop", 0.32))
    # impact on the punchline
    if getattr(T, "PUNCH_TEXT", None):
        ev.append((round(T.PUNCH_TEXT[0] + 0.05, 2), "impact-bass-1", 0.46))
    return ev

def main(src, out, sfx_dir=DEFAULT_SFX):
    events = [(t, f, g) for (t, f, g) in derive_events()
              if os.path.exists(f"{sfx_dir}/{f}.mp3")]
    if not events:
        # no sfx available -> just copy source audio
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",src,
                        "-vn","-c:a","aac","-b:a","192k",out], check=True)
        print("no sfx; copied source audio"); return
    inputs = ["-i", src]
    for _, f, _ in events:
        inputs += ["-i", f"{sfx_dir}/{f}.mp3"]
    labels = ["[0:a]aformat=sample_rates=48000:channel_layouts=stereo[a0]"]
    mix = ["[a0]"]
    for i, (t, f, g) in enumerate(events):
        ms = int(t * 1000)
        labels.append(f"[{i+1}:a]aformat=sample_rates=48000:channel_layouts=stereo,"
                      f"volume={g},adelay={ms}|{ms}[s{i}]")
        mix.append(f"[s{i}]")
    fc = ";".join(labels) + ";" + "".join(mix) + \
         f"amix=inputs={len(events)+1}:normalize=0:duration=first,alimiter=limit=0.95[aout]"
    cmd = ["ffmpeg","-y","-loglevel","error"] + inputs + \
          ["-filter_complex", fc, "-map","[aout]","-c:a","aac","-b:a","192k", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(f"sfx events={len(events)} rc={r.returncode}", r.stderr[-200:] if r.returncode else "ok")

if __name__ == "__main__":
    src = sys.argv[1]; out = sys.argv[2]
    sfx = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_SFX
    main(src, out, sfx)
