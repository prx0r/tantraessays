# TEXT_MAP — every atom assigned to its primary source (session 4)

One pool, two axes: essays = subject-query (already shipped, untouched by tagging),
text-works = text-query (ready to build). Schema in `SCHEMA.md`, registry in `SOURCES.md`,
application in `tag.py` (idempotent, re-runnable after any atom edit).

## 1. Stats

**Units (precise layer):** 146/146 tagged, 23 source-ids used.
Kinds: `root` 38 · `method` 38 · `agn` 31 · `direct` 27 · `work` 12.
Top texts: tl 45 · agn 31 · vyom 15 · yms 9 · ss 7 · kub 7 · pt 4 · mvut 4 · bs 4 · bu 3.

**Coverage entries (coarse routing):** 1,683/1,683 entry lines tagged via 72 line-range
segments across 15 files.
Kinds: `direct` 517 · `work` 388 · `method` 329 · `root` 300 · `agn` 149.
By hold-status: **869 entries on HELD texts** (tl 500, vyom 134, bs 77, bu 53, ss 36,
mvut 21, kjn 17, rv, jitw 30, spk…) · **112 on SPOKEN-held** (sv 70, pt 13, ph 29) ·
**342 on GAP texts** (yms 201 — his unpublished Yogini MS; jy 46, kapalika 39,
siddhanta 35, kub-text, hv 16, garuda 10, sn 10, jn 10, purnanatha 8, mm 5, ds 5,
kat 4, svs 2…) · **149 agn**.

Reading: **~52% of the coverage pool routes to texts we can verify today** (held+spoken),
and the biggest single sink of unverifiable material is Mark's own unpublished Yogini
manuscript (201) — lectures are the only witness for it, ever.

## 2. Essay → texts (derived from uids in ESSAY_* headings; essay files untouched)

| essay | beats | source-ids of its atoms |
|---|---|---|
| 01 Do You Need Rebirth | 9 | bu(+) mm sn tl · agn-frame |
| 02 How Dying Was Studied | 4 | **bu chd rv** — chd = GAP (pull) |
| 03 Hook Thread Burn | 5 | **siddhanta(+) tl vyom** — siddhanta = GAP (pull) |
| 04 Why You Stay Alive | 5 | purana(+) tl — purana = GAP (karma-13a/b aliases → tl:root) |
| 05 Sauh And Seeds | 5 | pt ss tl — pt now SPOKEN-held via Baumer clone |
| 06 No Method | 4 | mvut tl |
| 07 Two Streams | 4 | kjn tl |
| 08 Energy Everywhere | 4 | mvut spk tl(+) agn |
| 09 Chakras Corrected | 4 | kub purnanatha spk tl — kub/purnanatha = GAP |
| 10 Yogini Court | 4 | tl yms — yms = unpublished MS (never citable as text) |
| 11 Roots To Rock | 5 | kapalika kub natha ss — 2× GAP |
| 12 Devotion That Knows | 5 | **sv pt** ss tl — sv/pt now SPOKEN-held (closes [S]) |

Aliases: `karma-13a`, `karma-13b` (essay-04 split beats of karma-13) → inherit
`tl:root` — not header-tagged (no such headers); declared here.

## 3. Agnostic passages — how the rule was applied

The owner's rule: *a passage that explains a method generally gets the text whose
SANSKRIT depicts that method*, even when Mark doesn't cite it → tag `kind:method`.
If no registry text depicts it → stays `agn` (never invent a locus).

**Resolved from agnostic to a method text (examples):**
- general rebirth-lab talk → `bu` (karma-02: anchor BU 4.4, held)
- Brahma-door / "I am you" → `chd` Chāndogya 8 (karma-07 — gap, PD pull)
- golden-hook + five-knot thread → `siddhanta` the initiation paddhati (karma-10, vyoma-04)
- Jambudvipa karma-bhumi → `purana` (karma-12); penance examples → `ds` Manu (Karma L267-279)
- two-birds enjoyer → `svs`/`mnd` (L264-266; note: Mark says "Ken Upaniṣad" — his
  attribution, correct to Mundaka 3.1.1 + Śvetāśvatara 4.6 in product, cite both)
- six-chakra standard model → `purnanatha` Śrītattvanidhi ch.6 (pt1-10; Woodroffe = EN vessel)
- Garuda-poison magic → `garuda`/Kriya Kalottara (pt1 L175-215); Chandali → `hv` Hevajra
- Yogini stories → `kat` Kathā Sarit Sagara (PD EN pull)

**Stays `agn` (31 units, by category — nothing lost, nothing faked):**
- frame/meta: karma-01 (objection-question), markji-00/01 (mic/bio), sources-18/19
  (Buddhism disclaimer, iconic Q&A), vr0033-01, anuttara-13
- personal testimony: karma-09 (preta fieldwork), vr0033-06/09, anuttara-01
- humor/simile: vyoma-06 (music lesson), kundalini-pt2-07/08, karma-06-adjacent asides
- comparative (other-tradition, no primary in this corpus): anuttara-10 (Dzogchen),
  yogini1-04 (Buddhist societies), yogini2-11 (Ananda-Brahman), roots-03 (emptiness;
  possible Vātūlanātha/ŚS parallel — flagged VERIFY, note the vatulanatha corpus is
  a separate owned project)
- source-unmarked chant/verse: anuttara-08, bhairava-01 (Mark: "don't know where this
  is from" — stays unassigned until the verse is identified)
- definitional theses carried by no single text: yogini2-08 (Tantra-is-method), pt1-02

Coverage side mirrors this: 149 `agn` entries sit in room-runs, Q&A, comparative
stretches — a text-work skips them and loses nothing citable.

## 4. Gap pull-list (ranked by tagged volume, details + paths in SOURCES.md)

1. `jy` Jayadratha Yamala — 46 entries (Sources L232-314 is a whole lecture on its
   transmission; TL29 draws its ch.23)
2. `kapalika` — 39 (Roots lecture + shivasutra-05 + E11)
3. `siddhanta` — 35 (essay 03's spine: Raurava + thread-paddhati; N.R. Bhatt 1961 pointer)
4. `hv` Hevajra — 16 (essay 09/11 depth); `garuda` — 10
5. `chd` Chāndogya 8 — essay 02's missing primary (PD — free, highest value/effort)
6. `ds` Manu + `svs`/`mnd` two-birds — essay 01/02 depth (PD — free)
7. `purnanatha` via Woodroffe Serpent Power (PD EN) — essay 09
8. `kat` Tawney PD EN — Yogini stories texture
9. `kub` — Kubjika texts (and his own volumes: not on disk anywhere)
10. `yms` — **unpullable** (unpublished MS); its 201 entries are lecture-witnessed only —
    text-works may USE the audio, never cite the MS as a text.

## 5. Verification & repro

```bash
python3 primary_map/tag.py        # idempotent apply; exits 1 on missing uid/segment
python3 /tmp/verify_cov.py        # 1421 ok, 0 miss   (quotes survive tagging)
python3 /tmp/verify_bc.py         # 122 OK, 0 BAD     (essays untouched)
grep -c '\[text:' excavations/coverage/*.md | awk -F: '{s+=$2} END {print s}'   # 1683
grep -c '\[text:' excavations/*.md | awk -F: '{s+=$2} END {print s}'            # 146
```

Both audits green after tagging: 1421 + 122. Tag application never touches quote lines
(`> "…"`), unit bodies, or any essay file — only header/label lines carry `[text:…]`.
