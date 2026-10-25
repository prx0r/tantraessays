import re, os, glob
AUDIO2TXT={
 'Vyomavyapin_mantra.mp3':'Vyomavyapin_mantra','Karma_and_rebirth.mp3':'Karma_and_rebirth',
 'Elucidation_on_Para_Vidya.mp3':'Elucidation_on_Para_Vidya','anuttara.mp3':'anuttara',
 'Sources_of_Tantrāloka.mp3':'Sources_of_Tantrāloka','Kundalini_pt1_20111101.mp3':'Kundalini_pt1_20111101',
 'Kundalini_pt2_20111117.mp3':'Kundalini_pt2_20111117','Yogini_part2.mp3':'Yogini_part2',
 'Yogini_part1.mp3':'Yogini_part1','Roots_and_Development_of_Tantras.mp3':'Roots_and_Development_of_Tantras',
 'Shiva_Sutra_Introduction.mp3':'Shiva_Sutra_Introduction','VR0033_devotion_dec_3_2011.mp3':'VR0033_devotion_dec_3_2011',
 'Markji_Intro_CIIS_2010.m4a':'Markji_Intro_CIIS_2010',
}
cache={}
def norm(s): return re.sub(r'\s+',' ',s).strip()
def txt_of(audio):
    base=AUDIO2TXT.get(audio)
    if base not in cache:
        p=f'transcripts/{base}.txt'
        cache[base]=norm(open(p,encoding='utf-8',errors='ignore').read()).lower()
    return cache[base]
ok=bad=0; badlist=[]
for lvl in ['A','B','C']:
    for eid in sorted(os.listdir('essays/final12')):
        fp=f'essays/final12/{eid}/ESSAY_{lvl}.md'
        if not os.path.exists(fp): continue
        t=open(fp).read()
        cur=None
        for m in re.finditer(r'AUDIO: (\S+)|^> "(.*?)"', t, flags=re.M|re.S):
            if m.group(1): cur=m.group(1).split('/')[-1]
            else:
                q=norm(m.group(2)).lower()
                src=txt_of(cur)
                if q in src: ok+=1
                else: bad+=1; badlist.append((lvl,eid,cur,q[:70]))
print(f'verbatim: {ok} OK, {bad} BAD')
for b in badlist: print('  MISS',b)
