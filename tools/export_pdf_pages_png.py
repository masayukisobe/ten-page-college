from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Export each PDF page to a same-size PNG.")
    parser.add_argument(
        "--pdf",
        default="series/semicon-computer/01/preview.pdf",
        help="Path to source PDF.",
    )
    parser.add_argument(
        "--out-dir",
        default="docs/semicon-001",
        help="Directory for PNG files.",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=180,
        help="PNG rasterization DPI.",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf).resolve()
    out_dir = Path(args.out_dir).resolve()
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        import fitz
    except ImportError as exc:
        raise SystemExit(
            "PyMuPDF is not installed. Run with:\n"
            "  uv run --with pymupdf python tools/export_pdf_pages_png.py"
        ) from exc

    zoom = args.dpi / 72
    matrix = fitz.Matrix(zoom, zoom)

    with fitz.open(pdf_path) as doc:
        for index, page in enumerate(doc, start=1):
            pix = page.get_pixmap(matrix=matrix, alpha=False)
            out_path = out_dir / f"{index:02d}.png"
            pix.save(out_path)
            print(out_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
