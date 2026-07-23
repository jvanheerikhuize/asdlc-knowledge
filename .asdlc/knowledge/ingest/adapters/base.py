"""Ingestion adapter interface — the only contract adapters must satisfy."""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Protocol, runtime_checkable


@dataclass
class IngestResult:
    """Normalized output of any adapter: markdown text plus provenance."""
    markdown: str
    media_type: str
    checksum: str
    ingested_with: str
    meta: dict = field(default_factory=dict)


@runtime_checkable
class IngestAdapter(Protocol):
    """Convert one raw artifact into markdown. Implement `accepts` + `extract`."""
    name: str

    def accepts(self, path: Path, media_type: Optional[str]) -> bool:
        """Return True if this adapter can handle the given file."""
        ...

    def extract(self, path: Path) -> IngestResult:
        """Read `path` and return an IngestResult. Must not mutate the file."""
        ...


def sha256_of(path: Path) -> str:
    """Content hash used for provenance/dedup on source pages."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()
