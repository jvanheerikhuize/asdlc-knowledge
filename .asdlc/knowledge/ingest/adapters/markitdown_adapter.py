"""Adapter backed by Microsoft MarkItDown (fast, many formats).

Lazy-imports `markitdown` so the KB has no hard dependency on it.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from .base import IngestResult, sha256_of

HANDLED_EXT = {".pdf", ".docx", ".pptx", ".xlsx", ".html", ".htm", ".epub"}


class MarkitdownAdapter:
    name = "markitdown"

    def accepts(self, path: Path, media_type: Optional[str]) -> bool:
        return path.suffix.lower() in HANDLED_EXT

    def extract(self, path: Path) -> IngestResult:
        try:
            from markitdown import MarkItDown
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError(
                "markitdown backend not installed. `pip install markitdown` "
                "or route this file to another adapter in manifest.yaml."
            ) from exc
        result = MarkItDown().convert(str(path))
        return IngestResult(
            markdown=result.text_content,
            media_type=path.suffix.lstrip(".").lower(),
            checksum=sha256_of(path),
            ingested_with=self.name,
            meta={"title": getattr(result, "title", None)},
        )
