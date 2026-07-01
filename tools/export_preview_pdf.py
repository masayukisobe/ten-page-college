from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Export article preview HTML to PDF.")
    parser.add_argument(
        "--html",
        default="series/semicon-computer/01/preview.html",
        help="Path to preview HTML.",
    )
    parser.add_argument(
        "--out",
        default="series/semicon-computer/01/preview.pdf",
        help="Path to output PDF.",
    )
    parser.add_argument(
        "--page-width",
        default=None,
        help='Custom page width, for example "210mm". Uses A4 when omitted.',
    )
    parser.add_argument(
        "--page-height",
        default=None,
        help='Custom page height, for example "520mm". Uses A4 when omitted.',
    )
    args = parser.parse_args()

    html_path = Path(args.html).resolve()
    out_path = Path(args.out).resolve()
    if not html_path.exists():
        raise SystemExit(f"HTML not found: {html_path}")

    out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise SystemExit(
            "Playwright is not installed. Run with:\n"
            "  uv run --with playwright python tools/export_preview_pdf.py"
        ) from exc

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 1600})
        page.goto(html_path.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        pdf_options = {
            "path": str(out_path),
            "print_background": True,
            "margin": {
                "top": "14mm",
                "right": "14mm",
                "bottom": "16mm",
                "left": "14mm",
            },
            "prefer_css_page_size": False,
        }
        if args.page_width and args.page_height:
            pdf_options["width"] = args.page_width
            pdf_options["height"] = args.page_height
        else:
            pdf_options["format"] = "A4"
        page.pdf(**pdf_options)
        browser.close()

    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
