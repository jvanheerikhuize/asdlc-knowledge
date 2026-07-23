# Inbox — the ingestion drop-zone

Drop any file(s) here — PDFs, Word/PowerPoint/Excel, HTML, plain text, markdown —
then run one command from `.asdlc/knowledge/`:

```bash
python3 tools/kb.py ingest        # no arguments = ingest everything in this folder
```

For each file the KB will:

1. **copy** it into `raw/` (the immutable source-of-truth store),
2. **convert** it to markdown with the best available adapter
   (`plaintext` / `markitdown` / `docling`),
3. **scaffold** a draft page under `wiki/sources/`, and
4. **clear** the original out of this inbox.

You'll get a per-file progress line and a final tally. Re-running is safe:
already-ingested files are skipped.

> After ingesting, the source pages are **drafts**. Summarise them, link them to
> entity/concept pages with `[[wikilinks]]`, append a line to `log.md`, and run
> `python3 tools/kb.py lint --strict` to leave the tree green.

This folder is intentionally kept empty in git (only this README and `.gitkeep`
are tracked). Nothing you drop here is committed until it has been ingested.
