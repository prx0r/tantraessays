# SOURCES — primary-source registry (held / spoken-held / gap)

Status vocabulary: **HELD** = full text on disk for verification · **SPOKEN** = Mark/course
sessions cover it but the text edition is not held · **GAP** = named, needed, not held.
Cross-ref: `primary/INVENTORY.md` (pull-list detail), `/home/ubuntu/vatulanatha` (Baumer
spoken shelf), essay `PRIMARY_LIT.md` [V]/[P]/[S] bank (80/98/52).

## HELD — verifiable today

| id | text | holds |
|---|---|---|
| `bu` | Bṛhadāraṇyaka Upaniṣad | PD committed: 3.2.13 secret (yajñavalkya), 4.4 caterpillar (goldsmith partial) |
| `rv` | Ṛg Veda 10.10 Yama/Yāmi | PD committed (Griffith + Aufrecht Sanskrit) |
| `gita` | Bhagavad Gītā 2.22/2.27 | PD committed (Arnold) |
| `mvut` | Mālinīvijayottaratantra | Sanskrit 2.19–24 committed (GRETIL); quoted inside TL |
| `tl` | Tantrāloka (Abhinavagupta) | Dyczkowski trans vols 1–11 + Sanskrit, local (gitignored); [V] banked: v197cd 81-parts, prārabdha, upāya-structure, TL29 meat/wine, samanya/viśeṣa |
| `ss` | Śivasūtras (Vasugupta) | Dyczkowski trans local; [V] 1.1/2.1/3.1 |
| `spk` | Spanda Kārikā | Dyczkowski trans local; [V] pulse/urmi/ghūrṇi |
| `dv` | Doctrine of Vibration (Mark's study of the spanda source) | local text; his-book channel |
| `kjn` | Kula Jñāna Nirnaya | Sanskrit 7 vv committed (KSTS/Muktabodha, Bagchi ed.) |
| `bs` | Bhairava Stava (Abhinavagupta) | PDF `audio/Bhairava_Stava_verses.pdf` + lecture + recitation transcripts |
| `vyom` | Vyomavyāpin mantra | PDF `audio/Vyomavapin_mantra.pdf` + lecture + recitation |
| `jitw` | A Journey in the World of the Tantras (Mark's book) | PDF local (gitignored) — authored channel |
| `key` | plain_english/trika_key.json (46+46 keys) | committed — Sanskrit-term layer |

## SPOKEN-held — course sessions cover it, edition not held (closes our [S] gaps as audio)

| id | text | where |
|---|---|---|
| `sv` | Utpaladeva's Śivastotrāvalī | Baumer clone: 12 session srts → **E12 [S] closes as spoken-source** |
| `pt` | Parātrīśikā / Triṃśikā | Baumer clone: Parātrīśikā-Vivaraṇa 10 sessions → **E05 [S] closes as spoken-source** |
| `vb` | Vijñāna Bhairava | Baumer clone: 16 sessions + Lakshmanjoo trans [V] already banked (E06) |
| `ph` | Pratyabhijñā Hṛdayam | Baumer clone: 12 sessions (recognition/doctrine cross-pool) |
| `ss` | Śivasūtras | ALSO Baumer: 14 sessions on R2 (second voice for the same text) |

## GAP — named in atoms, not held (pull-list, ranked by atoms needing it)

| id | text | atoms needing | pull path |
|---|---|---|---|
| `chd` | Chāndogya Upaniṣad 8 (sun-door/Brahma-dvāra) | karma-07 + E02 | PD EN (Müller/Olivelle) — free |
| `svs` + `mnd` | Śvetāśvatara 4.6 / Mundaka 3.1.1 (two birds) | karma L264-266 | PD EN — free (note: Mark says "Ken Upaniṣad" — his attribution, correct in product) |
| `ds` | dharmaśāstra (Manu papa/puṇya, penance≠punishment) | karma L267-279, E01 depth | PD EN (Bühler) — free |
| `sn` | Sāmaññaphala Sutta (DN2, Buddha's 120 sects) | karma-04, E01 | cite-note exists; PD EN possible |
| `purana` | karma-bhumi/Jambudvipa geography (Viṣṇu/Bhāgavata) | karma-12, E03 | PD EN possible |
| `mm` | Mīmāṃsā apūrva (Kumārila/Prabhākara) | karma-08 | secondary gloss only (INVENTORY rule) |
| `siddhanta` | Raurava Agama + Siddhānta thread-paddhati (5 knots, golden hook) | karma-10, vyoma-04, E03/E04 | N.R. Bhatt 1961 ed pointer (INVENTORY) |
| `jy` | Jayadratha Yamala (Kula rite source of TL29 ch23) | Sources lecture, E07/E10 | Muktabodha? not held |
| `kub` | Kubjika Tantras (Mālinī/Kubjikā corpus) | pt1/pt2/Sources nodes | his volumes not held either; Muktabodha KSTS |
| `tsb` | Tantrasadbhava (4 of 25 Kūbhja chapters from it) | sources-04 | gap |
| `krama` | Kali Krama: Devī Pañcaśatikā, Krama Sara | Sources L232-314 block, yogini2-12 | gap |
| `purnanatha` | Śrītattvanidhi ch.6 (Pūrṇānanda, 16th c — THE six-chakra text) | pt1-10, E09 | EN via Woodroffe *Serpent Power* 1919 (PD EN, secondary vessel) |
| `hv` | Hevajra Tantra (Chandali, Anuttara Yoga) | pt1 L389-411, E09/E11 | trans exists (Snellgrove/Davidson secondary) |
| `kat` | Kathā Sarit Sagara (Soma Deva, yogini stories) | pt1 L291-300 | Tawney PD EN — free |
| `kapalika` | Dakṣiṇā Kāpālika sources (Kramādinakara etc.) | roots-01, shivasutra-05, Roots L7+ | gap (Sanderson refs) |
| `natha` | Gorakṣa corpus | roots-04 | gap |
| `garuda` | Garuda Tantras + Kriya Kalottara | pt1 L175-197, E11 | gap (Mark's student recovering — lecture says so) |
| `yms` | Mark's unpublished 400-pp Yogini manuscript | yogini1-*, yogini2-* | **exists nowhere on disk** — SPOKEN-only via lectures; do not cite as text |
| `shankara` | Śaṅkara Śivoha hymn ("I am He") | vr0033-02 | PD — trivial |

## Rules

1. `method`-tagged routing to a GAP id is allowed (the text depicts the method) but the
   text-work cannot print a locus from it until pulled — this table IS the pull-list.
2. Supplements (Lakshmanjoo/Wallis/Sanderson/Baumer) stay OUTSIDE coverage ledgers —
   they feed cross-maps, they don't excuse gaps (vatulanatha §10 law).
3. Never quote Sanskrit from whisper; Sanskrit comes from held e-texts only.
