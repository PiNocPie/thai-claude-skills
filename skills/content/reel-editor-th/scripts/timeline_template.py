# -*- coding: utf-8 -*-
"""timeline.py — the ONLY file you author per clip. Copy this into the workdir,
fill it from the transcript, then run build.sh. Everything else is reusable.

Times are seconds. Canvas is 1080x1920 @ 30fps. Set DUR to the clip length.
Keep copy natural and in the creator's voice. No em dashes (an AI tell)."""

W, H, FPS, DUR = 1080, 1920, 30, 53.0   # <- set DUR to the real clip duration

# ---- CAPTIONS: (start, end, "phrase", [words_to_highlight_green]) -------------
# Chunk into SHORT 2-3 word phrases that track the speech. Split words on spaces;
# the currently-spoken word auto-highlights. Put payload nouns/numbers in the
# emphasis list so they turn green even before they're the active word.
# Time from the reliable segment boundaries of the transcript; distribute within.
CAPTIONS = [
    # (0.0, 1.3, "คำ แรก", ["แรก"]),
    # ...
]

# ---- HOOK (0-~4.5s cold open, big text, captions are suppressed under it) -----
# Two short lines; line 1 white, line 2 green. Sell the payoff/tension. Auto-fits.
HOOK_TEXT = (0.0, 4.6, "บรรทัดแรกฮุค\nบรรทัดสองเขียว")

# ---- PUNCH (the payoff line near the end, yellow) ----------------------------
PUNCH_TEXT = (49.0, 53.0, "ประโยคเด็ดปิดคลิป")

# Optional: time of the big reveal beat -> a chime SFX lands here.
REVEAL_T = None   # e.g. 18.0

# ---- DEMO INSERT CARDS (optional) --------------------------------------------
# (start, end, card_id). card_id must exist in render_cards.py CARDS.
# Cards are topic-specific: edit their CONTENT in render_cards.py to match THIS
# clip, or leave INSERTS = [] to skip cards entirely (captions alone are fine).
# Available card ids: skillmd, arrow, claudechat, excel.
INSERTS = [
    # (18.2, 23.9, "skillmd"),
]

# ---- CTA windows (end of clip) -----------------------------------------------
# Defaults: a small early save sticker, a follow chip, and a link-in-bio line.
# CTA points to the BIO (not "comment X"). Edit the text in
# render_captions.py draw_cta if the offer changes.
CTA = {
    "save_sticker": (3.0, 6.0),
    "follow":       (47.5, 53.0),
    "comment":      (49.5, 53.0),   # this slot draws the bio CTA
    "save_big":     (50.5, 53.0),
}

# ---- Optional manual SFX overrides -------------------------------------------
# Leave unset to auto-derive (whoosh per card, pops on numbers, impact on punch,
# chime on REVEAL_T). Or set: SFX_EVENTS = [(t, "whoosh-short", 0.3), ...]
# SFX_EVENTS = []

GREEN = (11, 222, 133)
INK = (12, 14, 18)
