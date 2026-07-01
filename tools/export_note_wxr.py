from __future__ import annotations

import argparse
import html
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
    return "\n".join(lines)


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
        description="Create a WordPress WXR file for note import using hosted PNG pages."
    )
    parser.add_argument(
        "--image-dir",
        default="docs/semicon-001",
        help="Directory containing PNG pages to reference from the imported article.",
    )
    parser.add_argument(
        "--image-base-url",
        required=True,
        help="Public HTTPS URL prefix where the PNG files are hosted.",
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
        help="Only include the first N PNG files. Useful for import tests.",
    )
    parser.add_argument(
        "--test-intro",
        action="store_true",
        help="Add short test-introduction paragraphs before images.",
    )
    args = parser.parse_args()

    image_dir = Path(args.image_dir).resolve()
    out_path = Path(args.out).resolve()
    body_html = build_body_from_images(
        image_dir,
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
