from __future__ import annotations

import argparse
import html
import re
from datetime import datetime, timezone
from pathlib import Path


def cdata(text: str) -> str:
    return "<![CDATA[" + text.replace("]]>", "]]]]><![CDATA[>") + "]]>"


def normalize_base_url(url: str) -> str:
    return url.rstrip("/") + "/"


def build_body_from_images(
    image_dir: Path,
    image_base_url: str,
    *,
    limit: int | None = None,
    include_test_intro: bool = False,
) -> str:
    files = sorted(image_dir.glob("*.png"))
    if not files:
        raise SystemExit(f"No PNG files found: {image_dir}")
    if limit is not None:
        files = files[:limit]

    base = normalize_base_url(image_base_url)
    lines: list[str] = []
    if include_test_intro:
        lines.extend(
            [
                "<p>Lightweight note import test page.</p>",
                "<p>This page checks whether note can fetch hosted PNG image URLs.</p>",
            ]
        )
    for file in files:
        src = base + file.name
        alt = file.stem
        lines.append(f'<p><img src="{html.escape(src)}" alt="{html.escape(alt)}"></p>')
    return "".join(lines)


def parse_figure_map(preview_script_path: Path) -> dict[str, str]:
    text = preview_script_path.read_text(encoding="utf-8")
    entries = re.findall(r'^\s*"([^"]+)"\s*=\s*"([^"]+)"', text, re.MULTILINE)
    return {caption: src for caption, src in entries}


def inline_md(text: str) -> str:
    encoded = html.escape(text)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", encoded)


def normalize_caption(caption: str) -> str:
    return caption.replace("」と「", " と ")


def image_url(src: str, image_base_url: str) -> str:
    base = normalize_base_url(image_base_url)
    if src.startswith("images/"):
        return base + src.removeprefix("images/")
    return base + src


def build_body_from_draft(
    draft_path: Path,
    figure_map_path: Path,
    image_base_url: str,
    *,
    limit_figures: int | None = None,
    include_test_intro: bool = False,
    include_captions: bool = False,
) -> str:
    figure_map = parse_figure_map(figure_map_path)
    lines = draft_path.read_text(encoding="utf-8").splitlines()
    body: list[str] = []
    paragraph_buffer: list[str] = []
    in_code = False
    code_buffer: list[str] = []
    figure_count = 0
    current_section = ""

    def flush_paragraph() -> None:
        if not paragraph_buffer:
            return
        chunks: list[str] = []
        for i in range(0, len(paragraph_buffer), 3):
            chunks.append(" ".join(inline_md(text) for text in paragraph_buffer[i : i + 3]))
        for chunk in chunks:
            body.append(f"<p>{chunk}</p>")
        paragraph_buffer.clear()

    if include_test_intro:
        body.extend(
            [
                "<p>noteインポート検証用の記事です。</p>",
                "<p>本文テキストと挿絵画像が、通常記事として自然に入るかを確認します。</p>",
            ]
        )

    for raw_line in lines:
        line = raw_line.lstrip("\ufeff").rstrip()

        if line.startswith("```"):
            flush_paragraph()
            if not in_code:
                in_code = True
                code_buffer = []
            else:
                in_code = False
                body.append(f"<pre><code>{html.escape(chr(10).join(code_buffer))}</code></pre>")
            continue

        if in_code:
            code_buffer.append(line)
            continue

        if not line.strip():
            continue

        if line.startswith("# "):
            flush_paragraph()
            continue

        image_match = re.match(r"^!\[(.+?)\]\((.+?)\)$", line)
        if image_match:
            flush_paragraph()
            alt = image_match.group(1)
            src = image_url(image_match.group(2), image_base_url)
            body.append(f'<figure><img src="{html.escape(src)}" alt="{html.escape(alt)}"></figure>')
            continue

        heading2_match = re.match(r"^##\s+(.+)$", line)
        if heading2_match:
            flush_paragraph()
            current_section = heading2_match.group(1)
            if current_section != "はじめに":
                body.append("<hr>")
            body.append(f"<h2>{inline_md(current_section)}</h2>")
            continue

        heading3_match = re.match(r"^###\s+(.+)$", line)
        if heading3_match:
            flush_paragraph()
            body.append(f"<h3>{inline_md(heading3_match.group(1))}</h3>")
            continue

        if re.match(r"^---+$", line):
            flush_paragraph()
            continue

        figure_match = re.match(r"^\[ここに「(.+)」.*\]$", line)
        if figure_match:
            flush_paragraph()
            figure_count += 1
            if limit_figures is not None and figure_count > limit_figures:
                break

            caption = normalize_caption(figure_match.group(1))
            mapped_src = figure_map.get(caption)
            if mapped_src:
                src = image_url(mapped_src, image_base_url)
                figure_html = f'<figure><img src="{html.escape(src)}" alt="{html.escape(caption)}">'
                if include_captions:
                    figure_html += f"<figcaption>図{figure_count}: {inline_md(caption)}</figcaption>"
                figure_html += "</figure>"
                body.append(figure_html)
            else:
                body.append(f"<p>図{figure_count}: {inline_md(caption)}</p>")
            continue

        bullet_match = re.match(r"^-\s+(.+)$", line)
        if bullet_match:
            flush_paragraph()
            body.append(f"<p>・{inline_md(bullet_match.group(1))}</p>")
            continue

        if current_section == "重要用語10個":
            term_match = re.match(r"^(\d+)\.\s+(.+)$", line)
            if term_match:
                flush_paragraph()
                body.append(f"<h3>{term_match.group(1)}. {inline_md(term_match.group(2))}</h3>")
                continue

        if current_section == "巻末クイズ":
            quiz_match = re.match(r"^(\d+)\.\s+(.+)$", line)
            if quiz_match:
                flush_paragraph()
                body.append(f"<p><strong>Q{quiz_match.group(1)}.</strong> {inline_md(quiz_match.group(2))}</p>")
                continue

        paragraph_buffer.append(line.strip())

    flush_paragraph()
    if in_code:
        body.append(f"<pre><code>{html.escape(chr(10).join(code_buffer))}</code></pre>")

    return "".join(body)


def build_body_from_markdown(markdown_path: Path) -> str:
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    body: list[str] = []
    paragraph_buffer: list[str] = []
    list_buffer: list[str] = []

    def flush_paragraph() -> None:
        if paragraph_buffer:
            body.append(f"<p>{' '.join(inline_md(text) for text in paragraph_buffer)}</p>")
            paragraph_buffer.clear()

    def flush_list() -> None:
        if list_buffer:
            body.append("<ul>" + "".join(f"<li>{inline_md(item)}</li>" for item in list_buffer) + "</ul>")
            list_buffer.clear()

    for raw_line in lines:
        line = raw_line.lstrip("\ufeff").rstrip()

        if not line.strip():
            flush_paragraph()
            flush_list()
            continue

        if line.startswith("# "):
            flush_paragraph()
            flush_list()
            continue

        heading2_match = re.match(r"^##\s+(.+)$", line)
        if heading2_match:
            flush_paragraph()
            flush_list()
            body.append(f"<h2>{inline_md(heading2_match.group(1))}</h2>")
            continue

        heading3_match = re.match(r"^###\s+(.+)$", line)
        if heading3_match:
            flush_paragraph()
            flush_list()
            body.append(f"<h3>{inline_md(heading3_match.group(1))}</h3>")
            continue

        if re.match(r"^---+$", line):
            flush_paragraph()
            flush_list()
            body.append("<hr>")
            continue

        bullet_match = re.match(r"^-\s+(.+)$", line)
        if bullet_match:
            flush_paragraph()
            list_buffer.append(bullet_match.group(1))
            continue

        numbered_match = re.match(r"^\d+\.\s+(.+)$", line)
        if numbered_match:
            flush_paragraph()
            list_buffer.append(numbered_match.group(1))
            continue

        flush_list()
        paragraph_buffer.append(line.strip())

    flush_paragraph()
    flush_list()
    return "".join(body)


def build_wxr(title: str, body_html: str, post_date: datetime) -> str:
    pub_date = post_date.strftime("%a, %d %b %Y %H:%M:%S +0000")
    post_date_text = post_date.strftime("%Y-%m-%d %H:%M:%S")
    slug = "semiconductor-computation-001"

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
  xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:wfw="http://wellformedweb.org/CommentAPI/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:wp="http://wordpress.org/export/1.2/">
  <channel>
    <title>10 Page University</title>
    <link>https://note.com/</link>
    <description>10 Page University import file</description>
    <pubDate>{pub_date}</pubDate>
    <language>ja</language>
    <wp:wxr_version>1.2</wp:wxr_version>
    <item>
      <title>{html.escape(title)}</title>
      <link>https://note.com/</link>
      <pubDate>{pub_date}</pubDate>
      <dc:creator>{cdata("10 Page University")}</dc:creator>
      <guid isPermaLink="false">{slug}</guid>
      <description></description>
      <content:encoded>{cdata(body_html)}</content:encoded>
      <excerpt:encoded>{cdata("")}</excerpt:encoded>
      <wp:post_id>1</wp:post_id>
      <wp:post_date>{post_date_text}</wp:post_date>
      <wp:post_date_gmt>{post_date_text}</wp:post_date_gmt>
      <wp:comment_status>closed</wp:comment_status>
      <wp:ping_status>closed</wp:ping_status>
      <wp:post_name>{slug}</wp:post_name>
      <wp:status>draft</wp:status>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>0</wp:menu_order>
      <wp:post_type>post</wp:post_type>
      <wp:post_password></wp:post_password>
      <wp:is_sticky>0</wp:is_sticky>
    </item>
  </channel>
</rss>
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a WordPress WXR file for note import."
    )
    parser.add_argument(
        "--mode",
        choices=["pages", "article", "markdown"],
        default="pages",
        help="pages: import hosted page PNGs. article: import draft text and hosted illustration PNGs. markdown: import a plain Markdown article.",
    )
    parser.add_argument(
        "--draft",
        default="series/semicon-computer/01/draft.md",
        help="Markdown draft used when --mode article is selected.",
    )
    parser.add_argument(
        "--figure-map",
        default="tools/build_article_preview.ps1",
        help="Preview script containing the caption-to-image map used when --mode article is selected.",
    )
    parser.add_argument(
        "--image-dir",
        default="docs/semicon-001",
        help="Directory containing PNG pages to reference when --mode pages is selected.",
    )
    parser.add_argument(
        "--image-base-url",
        required=True,
        help="Public HTTPS URL prefix where the PNG files are hosted. For --mode article, point this to the illustration image directory.",
    )
    parser.add_argument(
        "--title",
        default="10 Page University Vol.1 - Why semiconductors can compute",
        help="Imported note article title.",
    )
    parser.add_argument(
        "--out",
        default="series/semicon-computer/01/note_import_wxr.xml",
        help="Output WXR XML file.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="For --mode pages, only include the first N PNG files. For --mode article, stop after N figures.",
    )
    parser.add_argument(
        "--test-intro",
        action="store_true",
        help="Add short test-introduction paragraphs before images.",
    )
    parser.add_argument(
        "--captions",
        action="store_true",
        help="Add figcaptions under illustration images in article mode.",
    )
    args = parser.parse_args()

    out_path = Path(args.out).resolve()
    if args.mode == "markdown":
        body_html = build_body_from_markdown(Path(args.draft).resolve())
    elif args.mode == "article":
        body_html = build_body_from_draft(
            Path(args.draft).resolve(),
            Path(args.figure_map).resolve(),
            args.image_base_url,
            limit_figures=args.limit,
            include_test_intro=args.test_intro,
            include_captions=args.captions,
        )
    else:
        body_html = build_body_from_images(
            Path(args.image_dir).resolve(),
            args.image_base_url,
            limit=args.limit,
            include_test_intro=args.test_intro,
        )
    wxr = build_wxr(args.title, body_html, datetime.now(timezone.utc))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(wxr, encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
