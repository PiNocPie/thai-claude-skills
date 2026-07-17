# Authoring guide — writing `timeline.py` and tuning a reel

This is the detail behind SKILL.md step 2-3. Read it when authoring the per-clip file.

## Contents
1. Caption chunking (the core craft)
2. Hook, punch, CTA
3. Demo cards — customizing content
4. The viral beat structure (53s reference)
5. Tuning knobs and gotchas

---

## 1. Caption chunking

Captions are the backbone. Rules that make them read as viral, not as a transcript:

- **Short phrases: 2-3 words on screen**, occasionally 1 for a punch. Never a full sentence.
- **Track the speech** — the words on screen should be roughly what the speaker is saying at that
  moment, chunked. You can lightly condense for readability; keep the meaning and timing.
- **Time from the transcript's segment boundaries** (those are reliable). Within a segment,
  split the span across your chunks proportional to length. The renderer auto-highlights the
  currently-spoken word, so per-word timing inside a chunk is derived automatically.
- **Emphasis list = green.** Put the payload words there (product name, numbers, the verb
  that carries the hook). The active word is already green; emphasis makes a word green even
  when it is not the active one. Do not green everything.

Format: `(start, end, "phrase text", [emphasis_words])`

Example (real):
```
(13.0, 14.35, "ทุกวัน ก็ทำแบบนี้", []),
(14.35, 15.65, "1 2 3 4", ["1","2","3","4"]),   # number-only -> auto SFX pops
(18.0, 19.5, "ด้วย Claude Skill.md", ["Claude","Skill.md"]),
```

Number-only captions like `"1 2 3 4"` automatically get pop SFX — nice for counting beats.

## 2. Hook, punch, CTA

- `HOOK_TEXT = (0.0, 4.6, "line1\nline2")` — cold open. Line 1 white, line 2 green.
  Captions are suppressed under the hook so it owns the first beat. Make it provocative and
  concrete; land the promise fast. It auto-fits to width, but keep each line short.
- `PUNCH_TEXT = (start, end, "one line")` — the payoff near the end, yellow. This is the
  shareable line; give it room (slow beat) and it gets an impact SFX.
- `CTA` windows are usually fine as-is. The bio offer text ("ของฟรีทั้งหมด ที่ไบโอ")
  and the follow chip copy live in `render_captions.py > draw_cta` — edit there if the
  offer changes. Keep it centered and above the bottom ~15% (IG UI zone).

## 3. Demo cards — customizing content

Cards are optional cutaway panels that slide over the upper frame while the speaker keeps talking —
they fix the "it feels like something's missing / choppy" problem and let you SHOW a prompt
or result instead of just saying it. Four cards exist in `render_cards.py`:

- `skillmd` — a macOS editor window typing out a `SKILL.md` file line by line.
- `arrow` — a simple "say X -> do Y -> then Z" analogy with labeled chips.
- `claudechat` — a Claude Code chat: a user prompt bubble + a streaming ✓ checklist. This
  is how you show "the prompt you told viewers to type".
- `excel` — a spreadsheet whose rows fill in with green checks + a counter.

To use: add `(start, end, "card_id")` to `INSERTS` in `timeline.py`, timed to when the speaker talks
about that thing. **The text inside each card is topic-specific** — open `render_cards.py`
and edit the content lists in the matching `card_*` function (the `SKILL.md` lines, the chat
prompt + checklist, the Excel rows) to match THIS clip. If nothing fits, leave `INSERTS = []`
— captions alone are a complete reel.

Cards render dark (coder aesthetic) across all styles; that reads as "developer" and stays
legible. They slide in from the right and out at the end automatically.

Timing tips: give a card ~5-9s so its typing/reveal completes. Cards may overlap the face —
that is fine, it is a cutaway. Sequence rather than stack (don't show two full-panel cards at
once); a small card (like `arrow`, which sits higher) can coexist with the talking head.

## 4. Viral beat structure (53s reference)

A structure that worked. Scale to the real clip length.

- 0.0-4.5  HOOK — cold open, big text by 1s, provocative promise.
- 4.5-13   PROBLEM/STAKES — fastest caption cadence (survive the early drop-off).
- 13-19    REVEAL — name the method; green-highlight the key term. Set `REVEAL_T` here for
  a chime.
- 19-42    BUILD — the how; this is where demo cards live. Keep visual change every 3-5s.
- 42-48    PAYOFF — the money line; slow down a touch, let it breathe.
- 48-53    CTA + LOOP — follow + bio, and try to make the last frame flow back into the
  first so the replay is seamless.

Guiding rule: no 3-second stretch where nothing changes (cut, caption change, card, or SFX).

## 5. Tuning knobs and gotchas

- **Colors look wrong (green skin, grey/odd shirt)** → the HDR tonemap didn't run. Confirm
  `scripts/tonemap` built and `out/sdr_master.mov` exists and is bt709. Never grade to
  "fix" this; it's a decode problem, not a look problem.
- **Tofu boxes (▯)** → PIL has no emoji/symbol fallback with Sukhumvit. Never render emoji
  or glyphs like ⚡ 📌 ▌ → as text; draw them as shapes (see how `render_cover.py` draws
  the arrow/cursor, and `render_cards.py` draws checkmarks).
- **Thai looks doubled or misaligned** → use font advance (`getlength`) and a common
  baseline from `getmetrics()`, not per-glyph bbox. The renderers already do this.
- **Caption covers the face during hook/punch** → the hook suppresses captions 0-HOOK_END
  by design; if the running captions sit too high/low, adjust `STYLES[style]["y"]`.
- **Overlapping renders corrupt files** → run builds sequentially. Two ffmpeg processes
  writing the same output (or the hardware hevc encoder used twice at once) can produce a
  truncated/`moov not found` file. Don't launch parallel builds of the same clip.
- **Desktop writes** → macOS TCC may block *overwriting* an existing Desktop file from
  cp/ffmpeg (creating new files/folders is fine; the Write tool can overwrite Desktop text).
  Deliver into a fresh folder with fresh filenames.
- **Render time** → the overlay render is ~1590 PIL frames (~1 min for 53s). The tonemap is
  ~10s. Total a few minutes per style. Fine unattended; just keep it sequential.
