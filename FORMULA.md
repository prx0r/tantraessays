# EXACT FORMULA — locked

For any essay source set (e.g. Essay 1 = Karma 93.9m + Markji 36.8m = 130.7m original):

- A = 10-20 min. All gold, nothing else. Verbatim Mark cores + minimal bridges to play standalone. Must make sense alone. Highest signal only.
- B = 20-40 min. Contains ALL of A, plus depth/explanation. Adds silver argument, origins, bridges. A plays inside B unchanged.
- C = rest to near-complete. Contains ALL of A and ALL of B, plus texture (anecdotes, Q&A, asides, alternate opens). Closest to full lecture without chant/tech/filler.

Rules:
1. A ⊂ B ⊂ C. Always. Never rewrite A inside B, never rewrite B inside C. Append only.
2. Quotes verbatim from txt, timestamps from srt. Mantra Sanskrit via PDF only, never whisper transliteration.
3. C excludes: chant runs, mic-checks, room noise, fan/water breaks. Those stay in source, never in essay.
4. Every clip block retains: AUDIO path, TRANSCRIPT path, TIMESTAMP, EXCAVATION file. No clip without source.
5. Grades are essay-local: A=gold must-use, B=silver should-include, C=mention worth-keeping. Global pyramid across corpus: A small (25), B larger (55), C largest (66).

Essay 1 calibration: 130.7m original → A ~15m full-section play (~1m verbatim + bridges), B ~30m, C ~45m. Adjust windows, not quotes, to hit runtimes.

Essay 1 calibration (locked 2026-10-24): 130.7m original (Karma 93.9 + Markji 36.8) → A 7 clips ~15m windows (~3m verbatim), B +3 clips ~27m, C +3 clips ~42m. A⊂B⊂C append-only verified.

33-sermon alignment (2026-10-24): budgets A 10-20 / B 20-40 / C rest (their 20-40 aim 30 adapted to essay brevity). Keep-rank: cold open / spine / unlock / close. Always-cut: chant/tech/mic/fan/Q&A tails/bio/recap/2nd telling. Seam: block after cut reads standalone, pause-snapped, never mid-sentence. Timebase: srt-native = audio (no YT/DS map needed). Cutplan.json per essay: target/kept/timebase/seam/grades. Speakers: Mark archive / Human cold-open+bridges ~2-3 min / Plain key-only (trika_key.json). Verbatim: audio windows are truth, md quotes are pointers with ... allowed only if render expands to sentence boundaries. Render (port analayo when needed): concat keeps, loudnorm -16 LUFS, afade 0.15s, bell -20dB, cough micro-cuts ±0.3s, pause breath 1.5s / water 2.5s.
