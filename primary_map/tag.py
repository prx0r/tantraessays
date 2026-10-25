#!/usr/bin/env python3
"""Apply primary_map TSVs to atoms. Idempotent. Run from repo root.

- unit_tags.tsv  -> appends [text:<id>:<kind>] to `### uid — ...` headers (all grades)
- segments.tsv   -> appends [text:<id>:<kind>] to coverage `- L...` entry lines (A/B/C)
Asserts: every uid tagged exactly once; every coverage entry line lands in a segment.
"""
import re, sys, os, glob, collections

TAG_RE = re.compile(r' ?\[text:[^\]]+\]')
HDR_RE = re.compile(r'^(### [a-z0-9-]+(?:_[a-z0-9]+)? — .*)$')  # unit headers (uid may contain _)
ENTRY_RE = re.compile(r'^- L(\d+)(?:-\d+)?\b')

def load_tsv(path):
    rows = []
    with open(path) as f:
        head = f.readline()
        for line in f:
            line = line.rstrip('\n')
            if not line: continue
            rows.append(line.split('\t'))
    return rows

def main():
    units = load_tsv('primary_map/unit_tags.tsv')
    segs  = load_tsv('primary_map/segments.tsv')

    stats = collections.Counter()
    # --- units ---
    by_uid = {r[0]: r for r in units}
    assert len(by_uid) == len(units), 'duplicate uid in unit_tags.tsv'
    seen = set()
    for path in sorted(glob.glob('excavations/*.md')):
        base = os.path.basename(path)
        if base in ('CATALOGUE.md', 'ESSAY_SPINE.md', 'EXTRACT_10H.md', '_SCHEMA.md'):
            continue
        out, changed = [], False
        for line in open(path):
            m = HDR_RE.match(line.rstrip('\n'))
            if m:
                uid = line.split('—')[0].strip().replace('### ', '').strip()
                if uid in by_uid:
                    _, f, text, kind, *_ = by_uid[uid]
                    assert f == base, f'{uid}: file mismatch {f} vs {base}'
                    bare = TAG_RE.sub('', line.rstrip('\n')).rstrip()
                    newline = f'{bare} [text:{text}:{kind}]'
                    if newline != line.rstrip('\n'):
                        changed = True
                    seen.add(uid)
                    out.append(newline + '\n')
                    continue
            out.append(line)
        if changed:
            open(path, 'w').write(''.join(out))
        stats[base] = sum(1 for l in out if l.startswith('### ') and '[text:' in l)
    missing = set(by_uid) - seen
    if missing:
        print('MISSING unit headers:', sorted(missing)); sys.exit(1)

    # --- coverage segments ---
    seg_by_file = collections.defaultdict(list)
    for r in segs:
        f, a, b, text, kind = r[0], int(r[1]), int(r[2]), r[3], r[4]
        seg_by_file[f].append((a, b, text, kind))
    untagged = []
    for path in sorted(glob.glob('excavations/coverage/*.md')):
        base = os.path.basename(path)
        seglist = sorted(seg_by_file.get(base, []))
        if not seglist:
            print(f'NO SEGMENTS for {base}'); sys.exit(1)
        out, changed = [], False
        section = None
        for line in open(path):
            s = line.rstrip('\n')
            if s.startswith('## '):
                section = s[3]
            m = ENTRY_RE.match(s)
            if m and section in ('A', 'B', 'C'):
                ln = int(m.group(1))
                hit = next(((a, b, t, k) for a, b, t, k in seglist if a <= ln <= b), None)
                if hit is None:
                    untagged.append((base, ln)); out.append(line); continue
                a, b, t, k = hit
                bare = TAG_RE.sub('', s)
                if bare.endswith(':'):
                    new = bare[:-1] + f' [text:{t}:{k}]:'
                else:
                    new = bare + f' [text:{t}:{k}]'
                if new != s: changed = True
                out.append(new + '\n')
            else:
                out.append(line)
        if changed:
            open(path, 'w').write(''.join(out))
        stats[base] = sum(1 for l in out if ENTRY_RE.match(l) and '[text:' in l)
    if untagged:
        print('UNSEGMENTED entry lines:', untagged[:20], '... total', len(untagged)); sys.exit(1)

    print('OK — tags applied. per-file counts:')
    for k in sorted(stats):
        print(f'  {k}: {stats[k]}')
    print(f'units: {len(seen)}/{len(units)}  segments: {len(segs)}')

if __name__ == '__main__':
    main()
