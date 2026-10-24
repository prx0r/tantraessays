# Dyczkowski excavation schema (essay-ready catalogue)

Mirrors Nibbana excavation: excavation first, compression later. Each lecture -> one file in `excavations/<id>.md`. Each file holds idea-units that can be reshuffled into a new essay.

## Idea-unit shape (every unit has all fields)
- `uid`: `<lecture>-<nn>` stable, never reused (e.g. `karma-03`)
- `timestamp`: `HH:MM:SS-->HH:MM:SS` from .srt, verbatim span for the quote
- `topics`: 1-4 tags from controlled list below
- `role`: claim | simile | refutation | story | lineage | method | practice | mantra-gloss | history
- `quote`: Mark's words verbatim from .txt (English only; never mantra Sanskrit from whisper — use PDF ref instead)
- `context`: 1-2 lines what he is answering / what comes before-after
- `grade`: A = clip/essay-ready, B = good with edit, C = do not use (chant/garbled/tech)
- `essay_use`: one line how this could be reused

## Controlled topic tags (keep closed; add only with note)
doctrine, history, kundalini, mantra, initiation, cosmology, devotion, yogini, tantra-comparative, shiva-sutras, tantraloka, praxis, lineage, death-rebirth, nonduality, ritual

## Rules (from Nibbana + this corpus)
- English lecture only for quotes. Chant/recitation (Bhairava stava, Vyomavyapin mantra runs, anuttara verses) = C, paraphrase + point to PDF, never quote whisper transliteration.
- No transcript invention: quote must appear in .txt; timestamp must exist in .srt.
- Filler kept out of quotes ("thank you", "mic check", "pat pat") unless it is the point (e.g. Markji intro tech = C with note to cut).
- Each excavation ends with: `## Reuse clusters` (3-6 buckets this lecture feeds) + `## Cross-links` (other lectures with same topic).
- Catalogue (`CATALOGUE.md`) is the reshuffle layer: topics -> uids across lectures, for essay assembly.
