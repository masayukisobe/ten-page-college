from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


CSS = """
:root { --paper:#f7f3ea; --ink:#2f2f2f; --teal:#1f7a7a; --mustard:#f2b84b; --coral:#e76f51; --mist:#d7e3e8; --white:#fffdf7; }
* { box-sizing:border-box; }
@page { size:A4; margin:14mm 14mm 16mm; }
body { margin:0; background:var(--paper); color:var(--ink); font-family:"Noto Sans JP","Yu Gothic","Meiryo",system-ui,sans-serif; line-height:1.9; letter-spacing:0; }
.wrap { width:min(860px, calc(100% - 32px)); margin:0 auto; padding:42px 0 84px; }
.article-header { padding:34px 0 24px; border-bottom:4px solid var(--ink); margin-bottom:34px; }
.series { color:var(--teal); font-weight:800; margin:0 0 10px; }
h1 { font-size:52px; line-height:1.16; margin:0 0 14px; font-weight:900; }
.subtitle { font-size:23px; font-weight:800; margin:0 0 4px; color:#444; }
section { margin:0 0 42px; }
.page-section, .intro-section { background:var(--white); border:2px solid rgba(47,47,47,.16); border-radius:8px; padding:34px 38px; box-shadow:0 10px 28px rgba(47,47,47,.055); break-inside:auto; break-before:page; }
.intro-section { border-color:rgba(31,122,122,.24); }
h2 { font-size:30px; line-height:1.35; margin:0 0 24px; font-weight:900; }
h3 { font-size:20px; line-height:1.45; margin:30px 0 14px; font-weight:900; color:var(--teal); }
p { font-size:18px; margin:0 0 17px; }
blockquote { margin:22px 0 26px; padding:18px 22px; border-left:6px solid var(--teal); background:#fffaf0; border-radius:8px; }
blockquote p { margin:0 0 12px; font-size:17px; }
blockquote p:last-child { margin-bottom:0; }
code { background:#f1ede3; border:1px solid rgba(47,47,47,.12); border-radius:4px; padding:.05em .3em; font-family:"Cascadia Mono",Consolas,monospace; font-size:.92em; }
pre { background:#292929; color:#fff8e8; padding:18px 20px; border-radius:8px; overflow-x:auto; line-height:1.55; margin:22px 0; }
pre code { background:transparent; border:0; padding:0; color:inherit; font-size:16px; }
.figure { margin:26px 0 30px; break-inside:avoid; }
.figure img, .cover-figure img { display:block; width:100%; border-radius:8px; border:2px solid rgba(47,47,47,.16); background:var(--paper); }
.page-section:last-of-type p { margin-bottom:12px; }
.page-section:last-of-type .figure { margin:22px 0 24px; }
.intro-section { padding:28px 34px; }
.intro-section p { margin-bottom:12px; }
.intro-section blockquote { margin:14px 0 16px; padding:12px 18px; }
.intro-section blockquote p { font-size:16px; margin-bottom:8px; }
.intro-section .figure { margin:14px 0 16px; }
.intro-section .figure img { max-height:360px; object-fit:contain; }
.cover-figure { margin:6px 0 40px; break-inside:avoid; }
figcaption { margin-top:9px; color:#5a5a5a; font-size:14px; line-height:1.5; font-weight:700; }
@media print { body { background:white; } .wrap { width:100%; padding:0; } .page-section, .intro-section { box-shadow:none; } }
""".strip()


IMAGE_RE = re.compile(r"^!\[(.*?)\]\((.*?)\)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip() + "\n"


def extract_bold_after_heading(markdown: str, heading: str) -> str | None:
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if line.strip() != heading:
            continue
        for candidate in lines[index + 1 :]:
            stripped = candidate.strip()
            if stripped.startswith("## "):
                return None
            if not stripped:
                continue
            bold = re.match(r"^\*\*(.+)\*\*$", stripped)
            return bold.group(1) if bold else stripped.strip("# ")
    return None


def infer_series_label(volume_dir: Path) -> str:
    volume_name = volume_dir.name
    try:
        number = int(volume_name)
    except ValueError:
        return f"10ページ大学 {volume_name}"
    return f"10ページ大学 情報学部 第{number}巻"


def infer_cover(volume_dir: Path) -> str | None:
    images = volume_dir / "images"
    if not images.exists():
        return None
    candidates = sorted(images.glob("cover*.png")) + sorted(images.glob("cover*.jpg"))
    if candidates:
        return str(candidates[0].relative_to(volume_dir))
    return None


def demote_headings(markdown: str) -> str:
    out: list[str] = []
    in_code = False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if not in_code and line.startswith("#"):
            out.append("#" + line)
        else:
            out.append(line)
    return "\n".join(out).strip() + "\n"


def inline(markdown: str) -> str:
    parts = markdown.split("`")
    rendered: list[str] = []
    for index, part in enumerate(parts):
        if index % 2:
            rendered.append("<code>" + html.escape(part) + "</code>")
        else:
            rendered.append(html.escape(part))
    return "".join(rendered)


def render_blocks(markdown: str) -> str:
    lines = markdown.strip().splitlines()
    out: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue

        if line.startswith("```"):
            code_lines: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code_lines.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
            continue

        if line.startswith(">"):
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].startswith(">"):
                text = lines[index][1:]
                if text.startswith(" "):
                    text = text[1:]
                quote_lines.append(text)
                index += 1
            paragraphs: list[str] = []
            current: list[str] = []
            for quote_line in quote_lines:
                if quote_line == "":
                    if current:
                        paragraphs.append(" ".join(current))
                        current = []
                else:
                    current.append(quote_line)
            if current:
                paragraphs.append(" ".join(current))
            out.append(
                "<blockquote>"
                + "".join(f"<p>{inline(paragraph)}</p>" for paragraph in paragraphs)
                + "</blockquote>"
            )
            continue

        heading = HEADING_RE.match(line)
        if heading:
            level = min(len(heading.group(1)), 6)
            out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
            index += 1
            continue

        image = IMAGE_RE.match(line)
        if image:
            alt, src = image.groups()
            out.append(
                f'<figure class="figure"><img src="{html.escape(src)}" alt="{html.escape(alt)}">'
                f"<figcaption>{inline(alt)}</figcaption></figure>"
            )
            index += 1
            continue

        out.append(f"<p>{inline(line)}</p>")
        index += 1
    return "\n".join(out)


def discover_pages(volume_dir: Path) -> list[Path]:
    pages = sorted(volume_dir.glob("draft-[0-9][0-9].md"))
    if not pages:
        raise SystemExit(f"No draft-0x.md files found: {volume_dir}")
    return pages


def build_markdown(
    series_label: str,
    title: str,
    subtitle: str,
    cover: str | None,
    intro_md: str,
    page_mds: list[str],
) -> str:
    parts = [f"# {series_label}", "", title, "", subtitle]
    if cover:
        parts.extend(["", f"![扉表紙]({cover})"])
    parts.extend(["", "---", "", intro_md.strip()])
    for page_md in page_mds:
        parts.extend(["", "---", "", page_md.strip()])
    return "\n".join(parts).rstrip() + "\n"


def build_html(
    series_label: str,
    title: str,
    subtitle: str,
    cover: str | None,
    intro_md: str,
    page_mds: list[str],
) -> str:
    intro_html = render_blocks(intro_md)
    page_htmls = [render_blocks(page_md) for page_md in page_mds]
    sections = [f'<section class="intro-section">\n{intro_html}\n</section>']
    sections.extend(f'<section class="page-section">\n{body}\n</section>' for body in page_htmls)
    cover_html = (
        f'<figure class="cover-figure"><img src="{html.escape(cover)}" alt="扉表紙"></figure>'
        if cover
        else ""
    )
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(series_label)} - Preview</title>
<style>
{CSS}
</style>
</head>
<body>
<main class="wrap">
<header class="article-header">
<p class="series">{html.escape(series_label)}</p>
<h1>{html.escape(title)}</h1>
<p class="subtitle">{html.escape(subtitle)}</p>
</header>
{cover_html}
{chr(10).join(sections)}
</main>
</body>
</html>
"""


def run_pdf_export(preview_html: Path, pdf_path: Path) -> None:
    export_script = ROOT / "tools" / "export_preview_pdf.py"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    uv = shutil.which("uv")
    if uv:
        command = [
            uv,
            "run",
            "--with",
            "playwright",
            "python",
            str(export_script),
            "--html",
            str(preview_html),
            "--out",
            str(pdf_path),
        ]
    else:
        command = [
            sys.executable,
            str(export_script),
            "--html",
            str(preview_html),
            "--out",
            str(pdf_path),
        ]
    subprocess.run(command, cwd=ROOT, check=True)


def run_quality_check(volume_dir: Path, pdf_path: Path | None) -> None:
    command = [
        sys.executable,
        str(ROOT / "tools" / "check_volume_quality.py"),
        "--volume",
        str(volume_dir),
    ]
    if pdf_path:
        command.extend(["--pdf", str(pdf_path), "--require-pdf"])
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a 10-page-college volume draft and preview.")
    parser.add_argument("--volume", required=True, help="Volume directory, for example series/semicon-computer/02.")
    parser.add_argument("--series-label", default=None, help="Header series label.")
    parser.add_argument("--title", default=None, help="Volume title. Defaults to structure.md 巻タイトル.")
    parser.add_argument("--subtitle", default=None, help="Volume subtitle. Defaults to structure.md サブタイトル案.")
    parser.add_argument("--cover", default=None, help="Cover image path relative to the volume directory.")
    parser.add_argument("--pdf", default=None, help="Optional output PDF path.")
    parser.add_argument("--check", action="store_true", help="Run tools/check_volume_quality.py after building.")
    args = parser.parse_args()

    volume_dir = (ROOT / args.volume).resolve() if not Path(args.volume).is_absolute() else Path(args.volume)
    if not volume_dir.exists():
        raise SystemExit(f"Volume directory not found: {volume_dir}")

    structure_path = volume_dir / "structure.md"
    intro_path = volume_dir / "intro.md"
    if not intro_path.exists():
        raise SystemExit(f"intro.md not found: {intro_path}")

    structure_md = structure_path.read_text(encoding="utf-8") if structure_path.exists() else ""
    title = args.title or extract_bold_after_heading(structure_md, "## 巻タイトル") or volume_dir.name
    subtitle = args.subtitle or extract_bold_after_heading(structure_md, "## サブタイトル案") or ""
    series_label = args.series_label or infer_series_label(volume_dir)
    cover = args.cover if args.cover is not None else infer_cover(volume_dir)

    intro_md = read_text(intro_path)
    page_mds = [demote_headings(read_text(path)) for path in discover_pages(volume_dir)]

    draft_path = volume_dir / "draft.md"
    preview_path = volume_dir / "preview.html"
    draft_path.write_text(
        build_markdown(series_label, title, subtitle, cover, intro_md, page_mds),
        encoding="utf-8",
    )
    preview_path.write_text(
        build_html(series_label, title, subtitle, cover, intro_md, page_mds),
        encoding="utf-8",
    )
    print(draft_path)
    print(preview_path)

    pdf_path = Path(args.pdf).resolve() if args.pdf else None
    if pdf_path:
        run_pdf_export(preview_path, pdf_path)

    if args.check:
        run_quality_check(volume_dir, pdf_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
