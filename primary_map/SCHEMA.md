# PRIMARY MAP — SCHEMA: how every atom gets tagged to a primary source

Session 4. The endgame: essays (subject-axis) and future text-works (text-axis) are two
queries over one tagged atom pool. This file defines the tag grammar. VAT-ANALYSIS's
standard applies: *"audio of a genius talking about a text — using their voice as the
excuse to finish analyzing a tough text."* One project = one primary source, covered.

## Tag grammar

Inline in atoms (append to unit headers / coverage A-entry label lines):

```
[text:<source-id>:<kind>]
```

Machine layer: `unit_tags.tsv` (per excavation unit), `segments.tsv` (per coverage file,
line-range → tag; A/B/C entries inherit by line ref). `tag.py` applies both idempotently.

## Kinds (the "how it attaches" axis)

| kind | meaning | trust |
|---|---|---|
| `direct` | Mark is reading/expositing THIS text in the passage (named in-transcript, verse-by-verse, "I'm reading from…") | highest |
| `root` | Doctrine/quote with a known locus in that text (Mark's own citation, or [V] banked with locator) | high |
| `method` | **Agnostic passage resolved by the method rule** (below) — best-fit text whose Sanskrit carries the method being explained | candidate, downgradeable |
| `work` | Primary reached via Mark's own book/manuscript (immediate source = his writing, not the primary itself) | channel known, primary may be gap |
| `agn` | Unanchorable: meta-teaching, humor, room, personal testimony, comparative aside, frame questions. **Explicitly unassigned so text-works can skip it honestly** | n/a |

## The agnostic rule (owner, session 4)

> "wouldn't the logic be that we need to find the primary source that depicts in
> Sanskrit the method he is explaining?"

A passage that explains a method *generally* (rebirth, karma mechanics, thread-initiation,
six-chakras) is NOT left loose: it gets the text whose Sanskrit depicts that method —
even when Mark doesn't cite it, e.g.:

- general rebirth-mechanics → `bu` (Bṛhadāraṇyaka carries the doctrine), Pāṇḍava-Buddhist
  process → `sn`; who-enjoys-fruit → `svs`/`mnd` two-birds
- golden-hook / five-knot thread → `siddhanta` (the initiation paddhati that depicts it)
- Jambudvipa karma-bhumi → `purana`; dharmaśāstra penance examples → `ds`
- six-chakra model → `purnanatha` (Śrītattvanidhi ch.6 depicts it; Woodroffe = EN vessel)

`method` tags are CANDIDATES by definition: they are the routing answer, not a verified
citation. A text-work built from a `method`-tagged passage must verify the locus against
the held text before printing it as source. If no text in registry depicts the method →
the passage stays `agn` (never invent a locus — [S]-rule from PRIMARY_LIT still governs).

## Files

| file | what |
|---|---|
| `SOURCES.md` | registry: id, text, held-how, gaps |
| `unit_tags.tsv` | 146 rows: uid, file, text, kind, note |
| `segments.tsv` | coverage line-range segments (coarse routing; unit tags are the precise layer) |
| `tag.py` | applies TSVs to atoms (idempotent), asserts full coverage, emits stats |
| `TEXT_MAP.md` | summary: stats, per-essay text derivation, agnostic resolutions, gap pull-list |

## Precision contract

- **Unit tags = precise** (one judgment per unit, verified against unit body where unsure).
- **Coverage segments = coarse routing** (dominant text per line-range; multi-text spans
  documented in the segment note; refine per-entry when building that text's work).
- **Essay files stay untouched** — essay→text derives from unit uids embedded in
  ESSAY_* headings, so the 122/122 audit is never at risk from tagging.
- Every tag application must leave `verify_cov.py` (1421) and `verify_bc.py` (122) green.
