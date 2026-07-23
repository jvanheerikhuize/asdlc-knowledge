# Ingestion Layer

Binaries and documents never enter `wiki/` directly. They are converted to
markdown text at this boundary by a **pluggable adapter**. This keeps the wiki
pure markdown (human-readable, diffable, greppable) while supporting any input
format.

## The interface

Every adapter implements `adapters/base.py::IngestAdapter`:

```python
class IngestAdapter(Protocol):
    name: str
    def accepts(self, path: Path, media_type: str | None) -> bool: ...
    def extract(self, path: Path) -> IngestResult: ...   # -> markdown + metadata
```

`IngestResult` carries the extracted `markdown`, a detected `media_type`, the
`sha256` checksum of the raw bytes, and adapter-specific `meta`.

## Dispatch

`tools/ingest.py` walks the adapters listed in `manifest.yaml -> ingest.adapters`
in priority order and picks the first whose `accepts()` returns True. Order and
default are configuration, not code.

## Shipped adapters

| Adapter      | Backend                    | Best for | Dependency |
|--------------|----------------------------|----------|------------|
| `plaintext`  | stdlib                     | .md .txt .csv .json | none |
| `markitdown` | Microsoft **MarkItDown**   | fast, many formats  | `markitdown` |
| `docling`    | IBM **Docling**            | tables, formulas, multi-column PDFs | `docling` |

The optional backends are lazy-imported: the KB works with zero dependencies for
plaintext, and degrades gracefully with a clear message if a backend is missing.

## Adding an adapter

Drop a module in `adapters/` exposing a subclass of `IngestAdapter`, then add its
`name` to `manifest.yaml -> ingest.adapters`. No other code changes required.
