# RENDER CHECKLIST — ported from analayo, verified on real audio 2026-10-24

Proof run: Essay 2, four clips from `ESSAY_A.md` exact spans, concatenated →
`render_proof.mp3` (196.9s, 4.7MB, loudnormed -16 LUFS). Commands that produced it:

```
ffmpeg -y -ss <start> -to <end> -i audio/<file>.mp3 -c copy /tmp/render/clip_N.mp3   # one per beat
# afades at clip edges, then concat + loudnorm:
ffmpeg -y -f concat -safe 0 -i list.txt \
  -af "afade=t=in:st=0:d=0.15,afade=t=out:st=<end-dur>:d=0.15,loudnorm=I=-16:TP=-1.5:LRA=11" \
  -ar 44100 -b:a 192k render.mp3
```

Per essay (copy Essay 2's flow):
1. Read ESSAY_A.md footline "Full-section edit (exact spans…)" — every timestamp is HH:MM:SS,mmm, pause-snapped at render.
2. Cut one ffmpeg clip per AUDIO span, `-c copy` (no re-encode on cut).
3. Concatenate in file order; apply in/out afades (0.15s) between beats; loudnorm I=-16 TP=-1.5 LRA=11.
4. Verify duration matches summed spans (±0.3s), listen for seam mid-sentence (seam rule: block after cut reads standalone).
5. Do not render B/C until A proof passes. Human intros (~40s cold open + bridges) and the plain-voice TTS layer (trika_key.json, key-only, first hearing per essay) sit *around* the concat — recorded later, not in this proof.

Caveats learned:
- Multi-quote beats may span non-contiguous srt blocks (e.g. E09 beat 1) — each quote gets its own AUDIO line and clip.
- srt ends sometimes trail 2-8s of room tone; trim to sentence end before concat.
- Chant recitation runs stay excluded (PDFs for Sanskrit only).
