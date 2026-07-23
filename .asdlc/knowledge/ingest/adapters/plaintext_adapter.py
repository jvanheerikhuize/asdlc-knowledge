"""Zero-dependency adapter for text-like files."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from .base import IngestResult, sha256_of

TEXT_EXT = {".md", ".markdown", ".txt", ".csv", ".tsv", ".json", ".yaml", ".yml", ".log"}


class PlaintextAdapter:
    name = "plaintext"

    def accepts(self, path: Path, media_type: Optional[str]) -> bool:
        return path.suffix.lower() in TEXT_EXT or media_type == "text"

    def extract(self, path: Path) -> IngestResult:
        text = path.read_text(encoding="utf-8", errors="replace")
        # Fence non-markdown text so it renders cleanly in the wiki.
        if path.suffix.lower() in {".md", ".markdown"}:
            md = text
        else:
            md = f"```{path.suffix.lstrip('.') or 'text'}\n{text}\n```"
        return IngestResult(
            markdown=md,
            media_type="text",
            checksum=sha256_of(path),
            ingested_with=self.name,
            meta={"chars": len(text)},
        )
