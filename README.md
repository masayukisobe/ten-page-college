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

## Codexで自動制作プロセスを使う

新しいCodexセッションでは、リポジトリルート `/home/masayuki/ten-page-college` で始めます。

このリポジトリには repo skill として `$ten-page-college` があります。巻制作、推敲、レビュー反映、HTML/PDF生成、品質確認をまとめて回したいときは、このskillを明示して依頼します。

依頼例:

```text
$ten-page-college
series/semicon-computer/03 の制作を進めてください。
project.md、series_plan.md、handoff.md、policies/、structure.md を読み、
abstract-0x.md -> draft-0x.md -> review-0x.md -> draft反映 -> draft.md/preview.html/PDF生成 -> 品質チェック
まで実行してください。
```

既存巻を推敲する場合:

```text
$ten-page-college
series/semicon-computer/02 を、policies/final-quality-checklist.md に沿って再レビューし、
必要な編集レベルをページごとに判定して、abstract、review、draftへ反映してください。
最後に draft.md、preview.html、PDFを再生成し、check_volume_quality.py で確認してください。
```

Codexは最初に次を読む想定です。

- `project.md`
- `series_plan.md`
- `handoff.md`
- `policies/draft-writing-policy.md`
- `policies/reader-conviction-perspective.md`
- `policies/intellectual-delight-perspective.md`
- `policies/final-quality-checklist.md`
- 対象巻の `structure.md`

自動生成の機械部分は、以下のコマンドで再実行できます。

```bash
rtk python3 tools/build_volume.py \
  --volume series/semicon-computer/02 \
  --pdf output/pdf/semicon-computer-02-digital-data.pdf \
  --check
```

PDFに特定の修正が入ったか確認したい場合:

```bash
rtk python3 tools/check_volume_quality.py \
  --volume series/semicon-computer/02 \
  --pdf output/pdf/semicon-computer-02-digital-data.pdf \
  --require-pdf \
  --expect-pdf-text "圧縮は、くり返し、辞書、知覚を使い分ける"
```

主な成果物:

- `series/<series>/<volume>/draft.md`: 組み上げ済みMarkdown。
- `series/<series>/<volume>/preview.html`: 確認用HTML。
- `output/pdf/*.pdf`: PDF出力。
- `review-0x.md`: ページ別レビュー判断ログ。
- `quality-check-review.md`: 巻単位の品質チェック記録。

skillが新セッションで見えない場合は、Codexを再起動します。repo skill は `.agents/skills/ten-page-college/SKILL.md` にあります。

## 主要ツール

- `tools/build_volume.py`: 巻ディレクトリの `intro.md` と `draft-0x.md` から `draft.md`、`preview.html`、必要に応じてPDFを生成。
- `tools/check_volume_quality.py`: 巻ディレクトリの画像参照、本文量、PDF陳腐化、PDF内テキストを検査。
- `tools/build_article_preview.ps1`: 記事プレビュー用のHTML生成。
- `tools/export_preview_pdf.py`: プレビューHTMLからPDFを生成。
- `tools/export_pdf_pages_png.py`: PDFからページPNGを生成。
- `tools/export_note_wxr.py`: noteインポート用WXRを生成。

## 代表的な実行例

第2巻の確認用原稿、HTML、PDFを生成し、品質チェックまで実行します。

```bash
rtk python3 tools/build_volume.py \
  --volume series/semicon-computer/02 \
  --pdf output/pdf/semicon-computer-02-digital-data.pdf \
  --check
```

PDF内に特定の反映語があるか確認します。

```bash
rtk python3 tools/check_volume_quality.py \
  --volume series/semicon-computer/02 \
  --pdf output/pdf/semicon-computer-02-digital-data.pdf \
  --require-pdf \
  --expect-pdf-text "圧縮は、くり返し、辞書、知覚を使い分ける"
```

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
