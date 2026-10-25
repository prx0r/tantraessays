import re, glob, os

def norm(s):
    return re.sub(r'\s+', ' ', s).strip().lower()

ok = 0
bad = []
files = sorted(glob.glob(os.path.expanduser('~/dyczkowski/excavations/coverage/*.md')))
for p in files:
    txt = open(p).read()
    m = re.search(r'# (\S+?)\.txt', txt)
    if not m:
        print('NO HEADER:', p)
        continue
    src = norm(open(os.path.expanduser('~/dyczkowski/transcripts/' + m.group(1) + '.txt')).read())
    for q in re.findall(r'^ {0,3}> "(.*?)"\s*$', txt, flags=re.M):
        nq = norm(q)
        if not nq:
            continue
        if nq in src:
            ok += 1
        else:
            bad.append((os.path.basename(p), nq[:70]))
print('verbatim: %d ok, %d miss' % (ok, len(bad)))
for b in bad:
    print('MISS', b[0], '|', b[1])
