"""Transcribe ~/dyczkowski/audio via Cloudflare Workers AI whisper-large-v3-turbo.

Chunks each file into 90s 16kHz mono pieces, transcribes in parallel,
stitches segments with absolute offsets. Writes .txt + .srt per file.
~$0.0005/min (~$0.40 for the whole 13h library).
"""
import base64
import concurrent.futures as cf
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request
import urllib.error

ACCT = "954612afb5a97bb15dddcdc70176813d"
MODEL = "@cf/openai/whisper-large-v3-turbo"
AUDIO_DIR = os.path.expanduser("~/dyczkowski/audio")
OUT_DIR = os.path.expanduser("~/dyczkowski/transcripts")
CHUNK = 90
WORKERS = 5
PROMPT = ("Kashmir Shaivism lecture by Mark Dyczkowski. Sanskrit terms: Shiva, "
          "Shakti, Trika, Abhinavagupta, Spanda, Spanda Samdoha, Vijnana Bhairava, "
          "Shiva Sutras, Tantraloka, Tantrasara, Kundalini, Yogini, Kubjika, "
          "Anuttara, Bhairava, Krama, Kula, Kaula, Pratyabhijna, mantra, sutra.")


def load_env():
    env = {}
    for line in open("/home/ubuntu/figgsite/.env"):
        line = line.strip()
        if line and "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k] = v
    return env


KEY = load_env()["CF_API_TOKEN"]
URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/ai/run/{MODEL}"


def run_one(b64, attempt=0):
    payload = json.dumps({"audio": b64, "task": "transcribe",
                          "language": "en", "vad_filter": True,
                          "initial_prompt": PROMPT}).encode()
    req = urllib.request.Request(URL, data=payload,
                                 headers={"Authorization": "Bearer " + KEY,
                                          "Content-Type": "application/json"},
                                 method="POST")
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            d = json.load(r)
        res = d.get("result") or {}
        if isinstance(res, dict) and ("text" in res or "segments" in res):
            # Empty text (e.g. silence after VAD) is valid — return as-is.
            res.setdefault("text", "")
            res.setdefault("segments", [])
            return res
        raise RuntimeError(str(d)[:200])
    except Exception as e:
        if attempt < 3:
            time.sleep(5 * (attempt + 1))
            return run_one(b64, attempt + 1)
        raise


def chunks_of(path, tmpd):
    dur = float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1", path]).decode().split("=")[1])
    out, t, i = [], 0.0, 0
    while t < dur:
        seg = os.path.join(tmpd, f"c{i:04d}.mp3")
        subprocess.check_call(
            ["ffmpeg", "-y", "-v", "error", "-ss", str(t), "-t", str(CHUNK),
             "-i", path, "-ac", "1", "-ar", "16000", "-b:a", "48k", seg])
        out.append((seg, t))
        t += CHUNK
        i += 1
    return out


def srt_ts(s):
    h, m = int(s // 3600), int((s % 3600) // 60)
    return f"{h:02d}:{m:02d}:{int(s % 60):02d},{int((s % 1) * 1000):03d}"


def do_file(path):
    base = os.path.splitext(os.path.basename(path))[0]
    txt, srt = os.path.join(OUT_DIR, base + ".txt"), os.path.join(OUT_DIR, base + ".srt")
    if os.path.exists(txt) and os.path.getsize(txt) > 1000:
        print("skip (done)", base, flush=True)
        return
    os.makedirs(OUT_DIR, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmpd:
        segs = chunks_of(path, tmpd)
        print(f"{base}: {len(segs)} chunks", flush=True)
        b64s = []
        for seg, off in segs:
            with open(seg, "rb") as f:
                b64s.append(base64.b64encode(f.read()).decode())
        results = [None] * len(segs)
        with cf.ThreadPoolExecutor(max_workers=WORKERS) as ex:
            futs = {ex.submit(run_one, b): i for i, b in enumerate(b64s)}
            for fut in cf.as_completed(futs):
                results[futs[fut]] = fut.result()
                print(f"{base}: chunk {sum(r is not None for r in results)}/{len(segs)}",
                      flush=True)
    lines, subs, n = [], [], 1
    for (_, off), res in zip(segs, results):
        for s in res.get("segments", []) or [{"start": 0, "end": 0,
                                              "text": res.get("text", "")}]:
            t = (s.get("text") or "").strip()
            if not t:
                continue
            lines.append(t)
            subs.append(f"{n}\n{srt_ts(off + s.get('start', 0))} --> "
                        f"{srt_ts(off + s.get('end', 0))}\n{t}\n")
            n += 1
    open(txt, "w").write("\n".join(lines) + "\n")
    open(srt, "w").write("\n".join(subs))
    print(f"wrote {txt} ({len(lines)} segs)", flush=True)


if __name__ == "__main__":
    import glob
    files = sorted(glob.glob(os.path.join(AUDIO_DIR, "*.mp3")) +
                   glob.glob(os.path.join(AUDIO_DIR, "*.m4a")))
    only = sys.argv[1:]
    if only:
        files = [f for f in files if os.path.splitext(os.path.basename(f))[0] in only]
    for f in files:
        do_file(f)
    print("ALL DONE")
