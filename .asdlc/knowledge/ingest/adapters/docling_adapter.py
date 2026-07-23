"""Adapter backed by IBM Docling (best structure fidelity: tables/formulas).

Lazy-imports `docling`. Prefer this for dense/academic PDFs.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from .base import IngestResult, sha256_of

HANDLED_EXT = {".pdf", ".docx", ".pptx", ".html", ".htm"}


class DoclingAdapter:
    name = "docling"

    def accepts(self, path: Path, media_type: Optional[str]) -> bool:
        return path.suffix.lower() in HANDLED_EXT

    def extract(self, path: Path) -> IngestResult:
        try:
            from docling.document_converter import DocumentConverter
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError(
                "docling backend not installed. `pip install docling` "
                "or route this file to another adapter in manifest.yaml."
            ) from exc
        doc = DocumentConverter().convert(str(path)).document
        return IngestResult(
            markdown=doc.export_to_markdown(),
            media_type=path.suffix.lstrip(".").lower(),
            checksum=sha256_of(path),
            ingested_with=self.name,
            meta={"pages": getattr(doc, "num_pages", None)},
        )
