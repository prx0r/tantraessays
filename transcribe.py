import os, sys
from faster_whisper import WhisperModel
model = WhisperModel("small.en", device="cpu", compute_type="int8", num_workers=6)
os.makedirs(os.path.expanduser("~/dyczkowski/transcripts"), exist_ok=True)
import glob
files = sorted(glob.glob(os.path.expanduser("~/dyczkowski/audio/*.mp3")) + glob.glob(os.path.expanduser("~/dyczkowski/audio/*.m4a")))
for f in files:
    base = os.path.splitext(os.path.basename(f))[0]
    out = os.path.expanduser(f"~/dyczkowski/transcripts/{base}.txt")
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        print("skip (done)", base, flush=True); continue
    print("transcribing", base, flush=True)
    segs, info = model.transcribe(f, language="en", beam_size=5, vad_filter=True)
    with open(out, "w") as o:
        for s in segs:
            o.write(s.text.strip() + "\n")
    print("wrote", out, flush=True)
