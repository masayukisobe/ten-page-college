# ten-page-college

10ページ大学の制作リポジトリです。

企画、読者像、執筆方針の本体は [project.md](project.md) を参照してください。シリーズ計画は [series_plan.md](series_plan.md)、現在の作業状態は [handoff.md](handoff.md) を参照してください。

## ディレクトリ構成

- `project.md`: プロジェクト全体の現在方針。
- `series_plan.md`: 情報学部のシリーズ計画。
- `handoff.md`: 現在の作業状態と引き継ぎ。
- `policies/`: 執筆・レビュー方針とレビュー観点文書。
- `series/`: 巻ごとの構成、原稿、レビュー、画像。
- `brand/`: ブランドページや共通素材。
- `docs/`: GitHub Pages公開用のHTML、ページPNG、画像。
- `tools/`: プレビュー、PDF、PNG、noteインポート用WXRの生成ツール。

## 巻ごとの作業場所

各巻は `series/<series-name>/<volume-number>/` に置きます。

主なファイル:

- `structure.md`: 巻全体の構成、ページタイトル、説明範囲。
- `intro.md`: 書き出し。
- `abstract-0x.md`: 各ページの骨格。
- `draft-0x.md`: 各ページの本文。
- `review-0x.md`: 各ページのレビュー判断ログ。
- `draft.md`: 個別ページを組み上げた確認用原稿。
- `images/`: その巻で使う画像。

本文制作とレビューの運用は [policies/draft-writing-policy.md](policies/draft-writing-policy.md) を参照してください。

## 主要ツール

- `tools/build_article_preview.ps1`: 記事プレビュー用のHTML生成。
- `tools/export_preview_pdf.py`: プレビューHTMLからPDFを生成。
- `tools/export_pdf_pages_png.py`: PDFからページPNGを生成。
- `tools/export_note_wxr.py`: noteインポート用WXRを生成。

## 代表的な実行例

プレビューPDFを生成します。

```powershell
.\tools\build_article_preview.ps1
uv run --with playwright python .\tools\export_preview_pdf.py
```

PDFからページPNGを書き出します。

```powershell
uv run --with pymupdf python .\tools\export_pdf_pages_png.py --pdf .\series\semicon-computer\01\preview_note_article.pdf
```

note通常記事用のWXRを生成します。

```powershell
uv run python .\tools\export_note_wxr.py `
  --mode article `
  --image-base-url https://<user>.github.io/<repo>/semicon-001/images `
  --title "<note記事タイトル>" `
  --out .\series\semicon-computer\01\note_import_wxr.xml
```

note側の取り込み挙動を軽く確認するときは、`--limit` を使います。

```powershell
uv run python .\tools\export_note_wxr.py `
  --mode article `
  --image-base-url https://<user>.github.io/<repo>/semicon-001/images `
  --title "<noteインポート検証タイトル>" `
  --limit 3 `
  --test-intro `
  --out .\series\semicon-computer\01\note_import_article_test_wxr.xml
```

## 公開用ファイル

`docs/` はGitHub Pages公開用です。

第1巻の公開用ページPNGと画像は、現在 `docs/semicon-001/` にあります。
