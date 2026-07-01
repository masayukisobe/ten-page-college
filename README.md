# 10ページ大学

社会人向けの短編電子コンテンツ「10ページ大学」の制作リポジトリです。

## 第1巻

- 原稿: `series/semicon-computer/01/draft.md`
- 構成: `series/semicon-computer/01/structure.md`
- 挿絵: `series/semicon-computer/01/images/`
- GitHub Pages公開用ページPNG: `docs/semicon-001/`
- GitHub Pages公開用挿絵PNG: `docs/semicon-001/images/`

## プレビュー生成

```powershell
.\tools\build_article_preview.ps1
uv run --with playwright python .\tools\export_preview_pdf.py
```

## note通常記事用の本文+挿絵WXR

`docs/semicon-001/images/` をGitHub Pagesで公開し、挿絵URLが次の形で見えるようにします。

```text
https://<user>.github.io/<repo>/semicon-001/images/cover-semiconductor-computation.png
```

その後、本文テキストと挿絵画像を含むWXRを生成します。

```powershell
uv run python .\tools\export_note_wxr.py `
  --mode article `
  --image-base-url https://<user>.github.io/<repo>/semicon-001/images `
  --title "10ページ大学 情報学部 第１巻｜なぜ半導体で計算できるのか" `
  --out .\series\semicon-computer\01\note_import_wxr.xml
```

### 軽量インポート検証

note側の取り込み挙動を先に見る場合は、先頭3図だけの軽いWXRを作ります。

```powershell
uv run python .\tools\export_note_wxr.py `
  --mode article `
  --image-base-url https://<user>.github.io/<repo>/semicon-001/images `
  --title "noteインポート検証｜10ページ大学｜本文と挿絵" `
  --limit 3 `
  --test-intro `
  --out .\series\semicon-computer\01\note_import_article_test_wxr.xml
```

## ページPNG方式

PDFから書き出したページPNGを縦に並べる方式も残しています。見た目固定の確認用途です。

```powershell
.\tools\build_article_preview.ps1
uv run --with playwright python .\tools\export_preview_pdf.py --out .\series\semicon-computer\01\preview_note_article.pdf --page-width 210mm --page-height 520mm
uv run --with pymupdf python .\tools\export_pdf_pages_png.py --pdf .\series\semicon-computer\01\preview_note_article.pdf
uv run python .\tools\export_note_wxr.py `
  --mode pages `
  --image-base-url https://<user>.github.io/<repo>/semicon-001 `
  --title "10ページ大学 情報学部 第１巻｜なぜ半導体で計算できるのか" `
  --out .\series\semicon-computer\01\note_import_pages_wxr.xml
```
