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

## 11. Session 2 (2026-10-24 late) — first-time read, spans, depth, imports
Read every essay as if first time, then harden. 20/20 todos. What changed and why:

### 11a. First-time read pass (per-essay seams)
- Method: read ESSAY_A cold, question every join, test each beat in ≤10 words, restructure in place (FLOW+ESSAY_A/B/C+SCRIPT), wire explicit handoffs 01→12 ("Next: … (Essay N)"). Stale cross-refs killed (E02's "worlds → Essay 6" was wrong; became travel/burn → Essay 3).
- Fixes worth copying: E01 dropped markji-03 speech beat (broke rebirth flow → moved to E05, permanent). E04 reordered answer→root→trace→scale→workshop (cold-open the answer first). E03 split one merged beat into karma-11 (mantra moves soul) + vyoma-05 (ladder burn) — two quotes, two AUDIO lines. E09 beat 1 had 2 quotes in one 10.3m window → split to two AUDIO lines (01:24:30→01:24:42 + 01:34:39→01:34:47), total dropped 13.0m→3.1m. Multi-quote beats ALWAYS get one window per quote, never min(start)→max(end) across a gap.
- Orphan check after restructure: `set(A-uids) − set(uids-in-final12)` caught sources-22, vyoma-06, yogini2-08 unplaced → sources-22 became E05 beat 5, vyoma-06 into E03-B, yogini2-08 stays C of E05/E19 ref. Run this check after ANY move.

### 11b. Exact spans (78→122 quotes)
- A-files: every AUDIO line now `HH:MM:SS,mmm --> HH:MM:SS,mmm` resolved from srt (head/tail fragment lookup per quote). Verified 78/78 after rewrite. Footers recomputed from actual spans (A cuts: 1.5–5.7m verbatim per essay, 49.5m total) — old "~19m windows" prose deleted; footer format = per-audio clip counts + spans + "A total Xm, land 10-20m".
- span_for rule: head and tail looked up INDEPENDENTLY across blocks; merge only if gap ≤300s else keep head-block only (prevents a 10m false window when tail matches an unrelated block).
- B/C expansion: 9 essays had empty/stub B/C (5 of 9 zero-B, 8 of 9 zero-C). Rebuilt all to one-verbatim-quote-per-beat with spans (±10s head/+15s tail for A; ±30/60 for B/C). Final: **122/122 verbatim A+B+C, 0 repeats-A, 121 windows ≈ 97m**, EXTRACTS.md per essay (per-quote windows, AUDIO/TRANSCRIPT dirs, "never from memory").
- Fix loop caught 3 real transcription-seam errors (E05 dropped period "Supreme. Para means Supreme. Sao…", E11B "he refers" not "But he calls", E11C "original format" truncated) — expand to exact sentence, never paraphrase the join.

### 11c. Audit-tool lessons (verify the verifier)
- Bug 1: source lowercased only on cache-miss → false "42/44 FAIL". Bug 2: quick-check dict missing Yogini_part1.mp3 → false "2 FAIL". True defect count was 3. BEFORE believing a red/green from your own checker: hand-test one FAIL against `grep`/substring in the raw source. Checker bugs outnumbered real bugs 42:3.
- Canonical audit now: normalize BOTH sides (`\s+→' `, lower), dict keyed by AUDIO basename (not audio/ path), per-level loop A/B/C, report per-file `ok/n`. Last run post-rebase: 122 OK / 0 BAD.

### 11d. Render proof (first real audio)
- `essays/final12/02_.../render_proof.mp3`: 4 clips cut with `ffmpeg -ss/-to -c copy`, concat list, `afade in/out 0.15s + loudnorm=I=-16:TP=-1.5:LRA=11` → 196.9s, 4.7MB. Procedure documented in `essays/RENDER_CHECKLIST.md` (pause-snap at render; trim srt trailing room-tone; chant stays out). Proof mp3 is tiny (4.7M) so it IS committed — big renders stay local.
- B/C render = same engine on the union clip list; nothing new to build.

### 11e. Git / parallel-agent protocol
- Another agent committed 7 commits to the same repo mid-session (primary-lit fetches, lit reviews, mark-voice pairings). Push rejected (non-fast-forward). Do: `git fetch` → inspect `main..origin/main` → `git pull --rebase` (clean here) → re-run verbatim audit AFTER rebase → push. Never force-push; never assume your working tree is authoritative. Post-rebase audit caught my own dict bug, not their edits (their "2 verbatim fixes" commit was fine — empty diff on the file I feared).
- Repo now PUBLIC: prx0r/tantraessays. Secrets never staged (token pastes in chat → treated compromised, never echoed/stored; .env 0600 only).

### 11f. Imports — stallshark/source-library R2 (use creds from figgsite/.env, never echo)
- Book: `A Journey in the World of the Tantras` (Dyczkowski, 316pp ABBYY) from stallshark bucket → `primary/books/` (5.9M). TOC→essay map in INVENTORY (ch2→E06, ch3→E06/E03, ch4-6 Kubjika/geography→E09/E10/E11). `.gitignore`: `primary/books/`, `*.pdf`.
- Texts: 14 files from `source-library/tantra/texts-clean/` → `primary/texts/` (18M, gitignored via `primary/texts/`): Tantraloka vol1-11, spandakarika, aphorisms-of-siva, doctrine-of-vibration (Dyczkowski's own translations). Also in R2 (not downloaded): tantrasara Sanskrit etc. per lit reviews.
- USED — [V] short-quotes with exact locators banked into 9 essays' PRIMARY_LIT (format: `[V] <book/locator>: "<short quote>"` + cite Dyczkowski/SUNY/MB + buy link + "local-only, never commit"):
  - E03: TL vol2 v197cd 81-parts + double-locator note (Mark site says TL6.228 — keep BOTH, don't merge).
  - E04: TL vol1 prārabdha "left intact…Otherwise he would die" + vol2 prārabdha/videhamukti/jīvanmukti single passage (roots vyoma-07 AND vyoma-02).
  - E06: TL vol1 upāya-structure line (Mark's lecture wording) + anupāya light-bliss descent.
  - E07: TL vol11 App E ch32 v657 meat/wine + cremation ground (Kula fundamentals, links E11).
  - E08: Spanda pulse definition + Utpaladeva ghurni verse + five signs + DV waves-on-sea.
  - E09: DV sakticakra wheel + Spanda "wave (urmi) of the ocean".
  - E11: Shiva Sutras 1.1/2.1/3.1 "Consciousness is the Self." / "The mind is Mantra." / "The mind is the Self."
  - E05 + E12: checked SILENT in shelf (no Triṃśikā/sauḥ-bīja, no Śivastotravali) — recorded as [S], do NOT invent; other-box stays.
- Bucket listing method: boto3 path-style S3 against R2 endpoint, creds from .env (STALLSHARK_*), `list_objects_v2` paginator, regex on Key. Buckets of note: stallshark, source-library (tantra/ tree), tantraloka-site (vol dups).

## 12. Current state (supersedes §8/§10 as of session-2 end)
- 12/12 essays: full A+B+C, all quotes verbatim (122/122), all A timestamps exact srt spans, EXTRACTS.md (per-quote windows, ~97m total), handoffs 01→12 wired, cuts lists written, PLAIN lines key-checked (no Sanskrit spoken).
- Render: Essay 2 proof mp3 done; checklist ported; B/C render = same concat on union lists.
- Primary: E01 PD full, E02 RV 10.10 (parallel commit), E03/E04/E06/E07/E08/E09/E11 [V] banked from local Dyczkowski texts, E05/E12 [S] honest. Parallel agent's lit reviews (Wallis/MVUT/KJnN) in per-essay PRIMARY_LIT.
- Still open: (1) record Human cold-opens/bridges + TTS key-voice (paper-ready in SPEAKERS.md, ~2-3m/essay); (2) full B/C renders (engine proven); (3) Chandogya sun-door + goldsmith full stanza PD pull; (4) E05 Triṃśikā + E12 Śivastotravali from other box; (5) 60m+ full-length render pass once voice exists.
- Repro after any edit: `python3 /tmp`-style audit (normalize both sides, AUDIO-basename dict) must read 122/122 or your edit broke verbatim; `grep -c '^### ' excavations/*.md` = 146; grades A25/B55/C66; `git ls-files primary/texts primary/books` = 0.

## 13. Session 3 (2026-10-25) — 100% transcript coverage (all 15 files, 3,951/3,951 lines)
Goal: every line of every transcript graded A/B/C for quotability, so nothing in the corpus is unmined and essays can draw from anywhere.

### 13a. What a coverage file is
- Location: `excavations/coverage/<base>.md`, one per transcript (filename without the `ā` for Sources_of_Tantrāloka). Header: `# <base>.txt — full coverage (N lines, ~W words)`, then a 1-paragraph session summary, then `Tier note:` (A/B/C = product quotability, independent of global unit grades), sections `## A — gold` / `## B — worth including` / `## C — worth mentioning / unusable`, footer `Coverage: N/N lines graded.` + quarantine list + explicit-flags + cross-file pairs.
- A entries: line ref (Lx-Ly) + label in parens (themes/E-essay hooks) + one or more verbatim `> "..."` quote blocks. B: line refs + 5-15 word prose labels (optionally a clean quote). C: line refs + why (room/garble/repetition/chant/numerals).
- Every line of the transcript must appear in at least one entry (edge double-grading across A/B/C boundaries is fine and normal).

### 13b. The audit loop (this session's core mechanic)
- Canonical verifier: `/tmp/verify_cov.py` — normalizes BOTH sides (`re.sub(r'\s+',' ',s).strip().lower()`), globs all coverage files, header regex `# (\S+?)\.txt`, reports `verbatim: N ok, M miss`. Final run this session: **1421 ok, 0 miss** across all 15 files.
- Every quote that fails gets a binary-search span diagnosis: find longest matching prefix, print 50 chars around the break from BOTH my quote and the source. This pinpointed real transcript forms in seconds. Failure taxonomy seen this session: dropped/added period at line-splits ("literature. in Vedic" not "literature in Vedic"), line-break word repeats ("in which... In which", "he was then THE judge", "the other ONE is watching"), wrong-name forms ("Kashmiri" not "Kashmir", "Shaiva Siddhant and an initiate", "consciousness IS pure"), fabricated quote-tails (a question I paraphrased that the speaker never said — delete, don't patch), comma-vs-period ("stuff like that," not "stuff like that.").
- Duplicated quotes: fixes must replace ALL occurrences (files quote the same line in A and B sometimes) — use `str.replace` with count printout, never blind sed.
- After fixes: re-run verifier until 0 miss, then update the footer (remove any "needs verify" pointer notes — L433 modern-person pointer in Karma resolved and footer edited).

### 13c. Line-count spot-check (do this before claiming done)
- For each transcript: `wc -l transcripts/*.txt` must equal the `Coverage: N/N` footer in the matching coverage file. Session-3 result: 15/15 match (19 to 651 lines each, 3,951 total).

### 13d. Coverage rubric calibration (learned across the two new big files)
- Never quote chant/hallucination lines (Sources L225 chant-line, Vyomavyapin recitation) — C + NEVER QUOTE.
- Repetition quarantines are per-file and go in the footer with counts: Kundalini_pt1 L52 "Tantric practice" x~50, L199 "Dhamra" x~40; Sources L508 "eight families" x~40, L167-169 "It is." x3, L364-369 "Okay." x5, L480-482 "Tantra..." x3. Bare-numeral lines (Kundalini L302-309/L474-477) → C.
- Explicit content: always grade B, never A, and label in the entry "EXPLICIT — summarize, never center" (Kundalini anatomy/fluids/caste lines, Sources TL-29 content, Yogini explicit blocks). Sources L46 (TL-29 meat/wine/fluids) is quotable AS-IS because he prefaces it with "I'm not advertising that. I'm just simply stating."
- Room-runs (Thank you/Okay/time-checks/book-finding) → C room; a single "Thank you." can be C without comment.
- Guided-meditation passages (Sources L582-601 heart-fire-pervasion walkthrough) are A-gold — they are the product's workshop material.
- Classroom Q&A exchanges with the audience are often A-gold (Sources deified-dead exchange, gunas answer) — grade Q and A-answers as pairs.

### 13e. Task-tool subagent failure (recorded again)
- Subagents returned empty results for coverage mining (same as earlier sessions). Do coverage work solo: read transcript fully with the Read tool (250-line chunks), write file, run verifier, diagnose, fix. 490+651-line files each took one full read + one write + one fix loop.

### 13f. State at session-3 end
- `excavations/coverage/`: 15 files, 3,951/3,951 lines graded, 1,421 verbatim quotes all passing.
- Essay verbatim audit (final12 A/B/C) untouched by this session: still 122/122.
- Karma_and_rebirth coverage written fresh this session (434 lines) + full A/B/C with 9 quote-form fixes; Kundalini_pt1 (490) and Sources_of_Tantraloka (651) written fresh, each passing after 1-2 quote fixes.
- Not yet done from §12 open list: cold-opens/TTS voice, full B/C renders, Chandogya/goldsmith PD pulls, E05/E12 other-box sources, 60m render.

## 14. Session 4 (2026-10-25) — primary-text assignment (the endgame layer)

Owner direction: stop fitting passages to essays; assign every atom to the primary
source it belongs to, using the rule *"find the primary source that depicts in Sanskrit
the method he is explaining."* Standard borrowed from `../vatulanatha` (same owner's
Baumer build): *"audio of a genius talking about a text — using their voice as the
excuse to finish analyzing a tough text"*; one project = one primary source, covered.
Vatulanatha's PROCESS_NOTES credits THIS repo (FORMULA, trika_key, excavation schema) —
the methodology came back hardened: measured-not-assigned question, Sanskrit-first
screen rule, BUILD ORDER LAW (essay 0 first; supersets never ship), speaker-order = C.

### 14a. primary_map/ — what was built
- `SCHEMA.md` (tag grammar: `direct/root/method/work/agn` + the agnostic rule),
  `SOURCES.md` (23-id registry: HELD / SPOKEN / GAP with pull paths),
  `unit_tags.tsv` (146 rows), `segments.tsv` (72 line-range segments),
  `tag.py` (idempotent applier, exits 1 on missing uid or unsegmented entry),
  `TEXT_MAP.md` (stats, per-essay derivation, agnostic resolutions, gap pull-list).
- Tags land on header/label lines ONLY: `### uid — label [A] [text:bu:root]` and
  coverage `- L24-27 (label) [text:tl:direct]:`. Quote lines, unit bodies, essay files:
  untouched — both audits stay green (1421 coverage + 122 essay).
- Coverage routing: every `- L…` entry in A/B/C inherits its file's line-range segment.
  Segments are COARSE (dominant text per range, multi-text spans noted); unit tags are
  the PRECISE layer. Refine per-entry when building a specific text-work.
- Essay→text derives from uids already embedded in ESSAY_* headings (`## 1. karma-01`):
  essays got a second axis for free, zero edits. Aliases karma-13a/13b declared in TEXT_MAP.

### 14b. Results worth knowing
- 146/146 units: root 38 · method 38 · agn 31 · direct 27 · work 12. 23 source-ids.
- 1683/1683 coverage entries: direct 517 · work 388 · method 329 · root 300 · agn 149.
- ~52% of coverage routes to HELD+SPOKEN texts (869 held + 112 spoken); 342 to gaps;
  the single largest unverifiable sink is Mark's unpublished Yogini MS (201 entries —
  lecture-witnessed only, never citable as a text).
- **[S] gaps close as SPOKEN**: Baumer clone (`/home/ubuntu/vatulanatha`, cloned this
  session) holds Śivastotrāvalī ×12 and Parātrīśikā-Vivaraṇa ×10 session srts → E12's
  and E05's "silent" texts have full audio coverage; text editions remain to pull.
- Karma file resolved as the worked example of the agnostic rule: general-dying→bu,
  Brahma-door→chd, golden-hook→siddhanta paddhati, Jambudvipa→purana, two-birds→svs/mnd
  (Mark's "Ken Upaniṣad" attribution recorded, correct to Mundaka 3.1.1+SVS 4.6 in product),
  penance→ds Manu; what stayed agn = frame questions, fieldwork testimony, humor.

### 14c. Pitfalls hit (checker bugs AGAIN)
- `verify_bc.py` was showing 42 BAD: it lowercased quotes but not the source. Patched
  (cache lowercased + A-level included) → 122 OK. Fourth instance of "verify the verifier
  before believing red" — hand-test one FAIL against raw substring first.
- TSV without header row + loader that skips row 1 = silently lost tag (anuttara-01):
  loader must assert uid-set == header-set, not just subset.
- Missing column in 12 `agn` segment rows put the NOTE in the kind position → 149
  malformed tags `[text:agn:<sentence>]`. tag.py must validate tag shape
  (`\[text:[a-z]+:[a-z]+\]`) after apply, not just count lines.
- Coordination flag: `vatulanatha/CUTTING-FORMULA.md` is a Dyczkowski @ BHU Tantrāloka
  cut plan (A/B/C/D grades, D = Sanskrit-as-translation-candidates — port that grade
  back here). Decide which repo owns BHU lectures before either builds them twice.

### 14d. Repro
```bash
python3 primary_map/tag.py                 # idempotent; 146 units, 72 segments
python3 tools/verify_cov.py                # 1421 ok, 0 miss  (scripts moved off /tmp — M12 scar)
python3 tools/verify_bc.py                 # 122 OK, 0 BAD
grep -c '\[text:' excavations/coverage/*.md | awk -F: '{s+=$2}'   # 1683
grep -c '\[text:' excavations/*.md        | awk -F: '{s+=$2}'   # 146
```
