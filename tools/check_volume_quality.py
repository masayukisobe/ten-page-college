from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMAGE_MD_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
IMAGE_HTML_RE = re.compile(r'<img\s+[^>]*src="([^"]+)"')


@dataclass
class PageStats:
    name: str
    body_lines: int
    chars: int
    images: int


def iter_page_drafts(volume_dir: Path) -> list[Path]:
    return sorted(volume_dir.glob("draft-[0-9][0-9].md"))


def collect_image_refs(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    refs = IMAGE_MD_RE.findall(text)
    refs.extend(IMAGE_HTML_RE.findall(text))
    return refs


def page_stats(path: Path) -> PageStats:
    text = path.read_text(encoding="utf-8")
    lines: list[str] = []
    in_code = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("!["):
            continue
        lines.append(stripped)
    return PageStats(
        name=path.name,
        body_lines=len(lines),
        chars=sum(len(line) for line in lines),
        images=len(IMAGE_MD_RE.findall(text)),
    )


def check_required_files(volume_dir: Path, errors: list[str], warnings: list[str]) -> None:
    for name in ["structure.md", "intro.md"]:
        if not (volume_dir / name).exists():
            errors.append(f"missing required file: {volume_dir / name}")

    drafts = iter_page_drafts(volume_dir)
    if not drafts:
        errors.append(f"no draft-0x.md files found: {volume_dir}")
        return

    for draft in drafts:
        suffix = draft.stem.removeprefix("draft-")
        abstract = volume_dir / f"abstract-{suffix}.md"
        review = volume_dir / f"review-{suffix}.md"
        if not abstract.exists():
            warnings.append(f"missing abstract for {draft.name}: {abstract.name}")
        if not review.exists():
            warnings.append(f"missing review for {draft.name}: {review.name}")


def check_image_refs(volume_dir: Path, errors: list[str]) -> None:
    files = [*iter_page_drafts(volume_dir), volume_dir / "draft.md", volume_dir / "preview.html"]
    for path in files:
        if not path.exists():
            continue
        for ref in collect_image_refs(path):
            if ref.startswith(("http://", "https://", "data:")):
                continue
            if not (path.parent / ref).exists():
                errors.append(f"missing image referenced from {path.relative_to(ROOT)}: {ref}")


def check_stats(volume_dir: Path, warnings: list[str]) -> list[PageStats]:
    stats = [page_stats(path) for path in iter_page_drafts(volume_dir)]
    for item in stats:
        if item.body_lines < 40:
            warnings.append(f"{item.name}: body lines look low ({item.body_lines})")
        if item.body_lines > 75:
            warnings.append(f"{item.name}: body lines look high ({item.body_lines})")
        if item.chars < 800:
            warnings.append(f"{item.name}: body chars look low ({item.chars})")
        if item.chars > 1650:
            warnings.append(f"{item.name}: body chars look high ({item.chars})")
        if item.images < 3:
            warnings.append(f"{item.name}: image count look low ({item.images})")
        if item.images > 6:
            warnings.append(f"{item.name}: image count look high ({item.images})")
    return stats


def run_text_extraction(pdf_path: Path) -> str | None:
    if not shutil.which("pdftotext"):
        return None
    with tempfile.TemporaryDirectory(prefix="ten-page-college-pdf-") as tmp:
        text_path = Path(tmp) / "pdf.txt"
        subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), str(text_path)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return text_path.read_text(encoding="utf-8", errors="ignore")


def check_pdf(
    volume_dir: Path,
    pdf_path: Path | None,
    require_pdf: bool,
    expect_pdf_text: list[str],
    errors: list[str],
    warnings: list[str],
) -> None:
    if pdf_path is None:
        if require_pdf:
            errors.append("--require-pdf was set but --pdf was not provided")
        return

    if not pdf_path.exists():
        target = errors if require_pdf else warnings
        target.append(f"PDF not found: {pdf_path}")
        return

    preview_path = volume_dir / "preview.html"
    if preview_path.exists() and pdf_path.stat().st_mtime < preview_path.stat().st_mtime:
        errors.append(f"PDF is older than preview.html: {pdf_path}")

    if shutil.which("pdfinfo"):
        result = subprocess.run(
            ["pdfinfo", str(pdf_path)],
            cwd=ROOT,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if line.startswith(("Pages:", "CreationDate:", "File size:")):
                    print(line)
        else:
            warnings.append(f"pdfinfo failed for {pdf_path}: {result.stderr.strip()}")

    if not expect_pdf_text:
        return

    extracted = run_text_extraction(pdf_path)
    if extracted is None:
        warnings.append("pdftotext not found; skipped --expect-pdf-text checks")
        return

    for needle in expect_pdf_text:
        if needle not in extracted:
            errors.append(f"expected text not found in PDF: {needle}")


def print_stats(stats: list[PageStats]) -> None:
    print("page,body_lines,chars,images")
    for item in stats:
        print(f"{item.name},{item.body_lines},{item.chars},{item.images}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a 10-page-college volume for build readiness.")
    parser.add_argument("--volume", required=True, help="Volume directory, for example series/semicon-computer/02.")
    parser.add_argument("--pdf", default=None, help="PDF path to check.")
    parser.add_argument("--require-pdf", action="store_true", help="Fail when --pdf is missing or absent.")
    parser.add_argument(
        "--expect-pdf-text",
        action="append",
        default=[],
        help="Text that must appear in the PDF. Can be repeated.",
    )
    args = parser.parse_args()

    volume_dir = (ROOT / args.volume).resolve() if not Path(args.volume).is_absolute() else Path(args.volume)
    pdf_path = Path(args.pdf).resolve() if args.pdf else None

    errors: list[str] = []
    warnings: list[str] = []

    if not volume_dir.exists():
        errors.append(f"volume directory not found: {volume_dir}")
    else:
        check_required_files(volume_dir, errors, warnings)
        check_image_refs(volume_dir, errors)
        stats = check_stats(volume_dir, warnings)
        print_stats(stats)
        check_pdf(volume_dir, pdf_path, args.require_pdf, args.expect_pdf_text, errors, warnings)

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
