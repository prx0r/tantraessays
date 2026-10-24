# PROCESS NOTES — mp3s to essays, reproducible (handover for another model)

Read this first. Everything below is learned from one full pass 2026-10-24 that took ~/dyczkowski from 15 raw mp3s to 12 finished essay packages. Follow in order. Do not skip QA gates — every shortcut we took cost a rebuild.

## 0. Starting state (what's on disk)
- `audio/`: 15 files, 844M, 16.15h, from anuttaratrikakula.org free lectures (Karma 93.9m, Kundalini pt1 114.4m, pt2 98.1m, Vyomavyapin 109m, Sources 115.3m, Yogini pt2 105.1m, VR0033 87.9m, anuttara 82.3m, Markji CIIS 36.8m m4a, Roots 27.2m, Shiva Sutra 17.8m, Elucidation 7m, Yogini pt1 8m, Bhairava lecture 60m, Bhairava recitation 6.4m) + 2 PDFs (Vyomavapin_mantra.pdf 68K, Bhairava_Stava_verses.pdf 72K). NEVER edit, never re-encode in place. Verify suspect downloads with `ffprobe -show_entries format=duration,size,bit_rate`: size ≈ dur × bitrate/8 (both 16:58 files checked out: 3597s@320k=143.9M, 6538s@320k=261.5M).
- `transcripts/`: 15 txt + 15 srt, 100,626 words. Pipeline was faster_whisper small.en (txt only) then transcribe_cf.py (Cloudflare whisper-large-v3-turbo, 90s chunks, 5 workers, initial_prompt with Shiva/Shakti/Trika terms). Token lives ONLY in ~/figgsite/.env as CF_API_TOKEN (0600, never print, never commit, never paste in chat). If 3 txt exist without srt, the old script skipped them (`if txt>1000 skip`) — back up txt to transcripts/backup_small_en/, delete originals, rerun `python3 transcribe_cf.py <Basenames...>` with 300s timeout (small) / 600s (Karma 63 chunks).
- Whisper hallucinates chant: Sanskrit recitation becomes CJK/Cyrillic/mixed junk ("Shriタaya... Ok이지... Может..."). English lecture is clean. Rule: NEVER quote chant transliteration. C-grade chant units point to PDF, no quote. This rule is load-bearing — violating it ships garbage Sanskrit.

## 1. Excavate (idea-units, not time-chunks)
- BAD (we did this): LECTURE_INDEX.md — 6 equal clock slices per lecture with first-line sample. Fast, shallow, arbitrary cuts, no quotes verified. Scrapped.
- GOOD: `excavations/_SCHEMA.md` — unit shape `{uid, timestamp HH:MM:SS-->HH:MM:SS from srt, topics (closed list 16), role (claim/simile/refutation/story/lineage/method/practice/mantra-gloss/history), quote (English verbatim ONLY from txt), context (1-2 lines), grade, essay_use}`. Stable uid `<lecture>-<nn>`, never reused. Example to copy: `excavations/karma_and_rebirth.md` (14 units). 5 parallel subagents did the rest → 114 units. Subagents need explicit: read schema first + example file + grep-verify every quote/timestamp or they return empties (see analayo HANDOFF: "Task-tool subagents returned EMPTY results 3x — work solo" — same failure mode; give them verification commands).
- Coverage QA (do not skip): chunk each txt in 5, count quote-hits per chunk. Any 0-hit span >50 lines (80 for long lectures) → read it → part2 file if gold. This found Sources tail 260 lines (chakra holes, guna initiations, body-means, Buddhist pheno, iconic Q&A), Vyoma glosses 234 lines (Vyomarupi→Yogapitha), anuttara middle 118 lines (Shambhava, 3 samaveshas, Dzogchen warning), Yogini Ananda/Visarga tail, VR0033 Kashi close. Total went 114 → 146 units (132A/9B/5C at the time).

## 2. Grade (pyramid, not participation trophy)
- BAD (we did this): 101A/9B/5C — almost everything gold. Titles lied, 4 essays had zero A on recheck.
- GOOD: A=25 gold must-use, B=55 silver should-include, C=66 mention worth-having. B > A, C largest. Rewrote 116 `### uid — title [X]` headers by script, recounted with Counter. Essay-local RANKING mirrors it (A/B/C per essay) but global grades rule assignment. If an essay has <2 global-A, merge it — orphan essays with no gold are the tell you graded wrong.

## 3. Cluster (by problem, never by lecture)
- BAD: 20 essays 1:1 to lectures (Karma essay = Karma lecture). Circular — "just where we started?"
- GOOD: 12 cross-lecture essays (final12/): objection, dying, hook/thread/burn, stay-alive, seeds, no-method, two-streams, energy, chakras, court, roots, devotion. Each: primary clips + required secondaries with insertion note ("after karma-11 (thread detail)") so it plays standalone. 20 micro manifests (manifests20/) drain all 132 old-A with 0 missing — keep as coverage proof, not product.
- Move rule (user-enforced): anytime a clip breaks flow in Essay N, find its best-fit essay and move it with a moved-note (e.g. markji-03 knowing-is-speech out of Essay 1 rebirth → into Essay 5 seeds as speech-as-mantra). Don't duplicate silently; one home, secondaries by reference with reason.

## 4. Essay package shape (every one of the 12 has all 11 files)
`SPINE.md` (his words = structure, BUILD slots) → `RANKING.md` (essay-local A/B/C) → `FLOW.md` (beats: objection→authority→origin→frame→person→handoff style) → `ESSAY_A.md` (10-20m gold only) → `ESSAY_B.md` (A + depth, 20-40m, append-only) → `ESSAY_C.md` (A+B + rest, append-only) → `SCRIPT_3LAYER.md` (primary → Mark → plain per beat) → `PRIMARY_LIT.md` (primary/scholarly/area) → `FULL_SECTIONS.md` (ffmpeg -ss/-to windows, pre480/post720 merged ≈10h corpus) → `SPEAKERS.md` (Mark clips + Human ~2-3min + plain key-only) → `cutplan.json` (target/kept/timebase-srt-native/seam/grades).
A⊂B⊂C always — B starts "A plays unchanged", C starts "A+B play unchanged". Never rewrite A inside B. FORMULA.md is this contract.

## 5. Three-layer script (the product grammar — ported from analayo, adapted)
- Analayo: Nanananda verbatim pad → Analayo unlock → Fish key-only English drop + Human cold-open/bridges, bells per motif, breath/water pauses. Deterministic gloss (fish_filter.py word-boundary safe, rerun = byte-identical), verbatim audit 75/75 exact-substring, slop quarantined.
- Ours: PRIMARY (root verbatim PD/cited, or Sanskrit via PDF/Muktabodha — never whisper text) → MARK (archive, unchanged, timestamped) → PLAIN (your line, trika_key.json mapped, no Sanskrit spoken). Mark is the explainer (their Analayo seat). No Fish voice yet — plain lines are written, not yet key-filtered deterministically. If you add TTS, port their rule: key word only, max 2 drops/clip, never sentences.
- Plain-English law (both projects): viewer never needs the technical term. Sanskrit/Pali on screen as citation, never in plain voice. If a sentence needs the term to make sense, rewrite it. Our map: `plain_english/PLAIN_ENGLISH_TRIKA.md` (60 rows) + `trika_key.json` (46 keys). Blunt phrases: thread=ladder, hook=breath-hook, Karma-bhumi=only-here-you-act, I-am-you=password.
- Seam rule (theirs, adopt verbatim): block after a cut reads standalone; never mid-sentence in render (md "..." shorthand is a pointer only — expand to sentence boundaries + pause-snap at edit); no dangling "as mentioned above" unless referent is kept.
- Always-cut (adapted): chant/tech/mic-check/fan-water/room Q&A tails/bio/recap/2nd telling. Keep-rank: cold open ≤90s / spine bulk / unlock ≤6-8m / close. Budget: A 10-20 / B 20-40 (their 20-40 aim 30 adapted to essay brevity).

## 6. Verbatim + audit (where we are vs them)
- Them: 75/75 excerpts exact-substring verified (whitespace+markdown normalized both sides), hand-typed beats DELETED when caught, slop/ quarantine dir, rebuildable pipeline.
- Us: timestamps grep-verified in srt (all A/B), quotes verified case-insensitive first-40-chars EXCEPT 4 shorthand ("...") trims found in audit (karma-04 split-line, karma-14 tail, karma-06 Yama, karma-13 mala). Fixed 2 to full verbatim (Yajnavalkya secret, "Yeah, I do believe in rebirth"); 2 remain as window+txt-span refs (acceptable ONLY because render cut is the full-section window, not the md line — document this per clip or you will reintroduce slop).
- Rule going forward: md quote = pointer; render cut = FULL_SECTIONS window, pause-snapped, never mid-sentence. Audit windows, not md lines. Rerun: `grep -c '^### ' excavations/*.md` (=146), grade Counter must read A25/B55/C66, every A in ≥1 manifest20 file, every timestamp's start in its srt.

## 7. Primary shelf (what's imported, what's cited)
- `primary/`: INVENTORY.md (all 12), README.md (PD vs cite rule), E01 files (caterpillar Max Muller PD verbatim, Yajnavalkya 3.2.13 PD verbatim, Gita garments Arnold PD verbatim, Sramana six cite-only). Tantric: refs + editions only (Raurava Bhatt 1961, Malinivijaya, Tantraloka 1/6/29, Kubjika 5 wheels/Urmi, Jayadratha Shatka 3, Kulanirnaya 8/Matrika 64, Kula Jnana Nirnaya/Akula Vira/Urmikaularnava, Vasugupta discovery, Spanda, PH/Vimarshini Singh cite+buy, Shivastotravali Bailley cite+buy, Bhairava Stava PDF on disk). Sanskrit/KSTS public domain OK to quote; modern trans: citation + buy link, 1-2 line fair-use max, paraphrase is yours. Other box holds the editions — notes in PRIMARY_LIT.md per essay list exactly which pages to pull.

## 8. Known gaps (don't pretend otherwise)
- Yama/Yami Rig Veda 10.10 + Chandogya sun-door full PD text not yet pulled (refs only). Markji-04 vimarsha primary (PH sutra) cited not imported. Ananda/Visarga primary (Kubjika Urmi passage) summarized from Mark, Sanskrit not extracted. B/C plain lines for Essays 04-12 are key-tags/short bridges, not finished sentences (only 01-03 have full plain). C-versions for 04-12 are stubs ("adds texture") not full clip lists — acceptable per A⊂B⊂C only if B lists are complete (they are), but don't call C done.
- 5 C chant/tech units intentionally unquoted (vyoma-10/11, recitation-01, markji-00, anuttara-08). Bhairava lecture part4 checked: interaction + transliteration, no gold — stays C.

## 9. Repro commands (copy-paste)
- Verify downloads: `ffprobe -v error -show_entries format=duration,size,bit_rate -of default=noprint_wrappers=1 FILE` → size ≈ dur×bitrate/8.
- Count work: `grep -h '^### ' excavations/*.md | wc -l` (146); grade split via header `[A]/[B]/[C]`.
- Coverage: chunk each txt in 5, count quote-hits; 0-hit span >50 lines → read it.
- Rerun-safe: transcripts/ read-only; excavations/essays/plain_english/primary/ text-only in git; audio/ + PDFs gitignored (844M, GitHub would reject 250M file anyway).
- Never commit: .env, API tokens, GitHub PATs (user pasted both in chat 2026-10-24 — treated as compromised, never echoed, never stored; revoked guidance given).

## 10. What "done" looks like (per essay)
RANKING + FLOW + ESSAY_A/B/C (A⊂B⊂C) + SCRIPT_3LAYER (primary→Mark→plain, plain key-compliant, no Sanskrit spoken) + PRIMARY_LIT (primary/scholarly/area) + FULL_SECTIONS (ffmpeg -ss/-to, pause-snap note) + SPEAKERS (Mark clips + Human ~2-3min + key-only) + cutplan.json. Essay 1 + 2 meet this. Essay 3 meets it except primary verbatims for Raurava/paddhati (cite-only, correctly — no PD English exists). Essays 04-12 meet structure + A clips + refs; plain sentences + primary verbatims where PD remain. Do not claim C done until B clip lists are explicit (01-03 are; 04-12 B files are deltas — acceptable) and every timestamp re-grepped after any edit.
