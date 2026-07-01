# 10ページ大学

社会人向けの短編電子コンテンツ「10ページ大学」の制作リポジトリです。

## 第1巻

- 原稿: `series/semicon-computer/01/draft.md`
- 構成: `series/semicon-computer/01/structure.md`
- 挿絵: `series/semicon-computer/01/images/`
- note掲載用PNG: `docs/semicon-001/`

## プレビュー生成

```powershell
.\tools\build_article_preview.ps1
uv run --with playwright python .\tools\export_preview_pdf.py
```

## note通常記事用PNG生成

```powershell
.\tools\build_article_preview.ps1
uv run --with playwright python .\tools\export_preview_pdf.py --out .\series\semicon-computer\01\preview_note_article.pdf --page-width 210mm --page-height 520mm
uv run --with pymupdf python .\tools\export_pdf_pages_png.py --pdf .\series\semicon-computer\01\preview_note_article.pdf
```

## note WXR生成

`docs/semicon-001/` をGitHub Pagesで公開し、画像URLが次の形で見えるようにします。

```text
https://<user>.github.io/<repo>/semicon-001/01.png
```

その後、URLを指定してWXRを生成します。

```powershell
uv run python .\tools\export_note_wxr.py `
  --image-base-url https://<user>.github.io/<repo>/semicon-001 `
  --title "10ページ大学 情報学部 第１巻｜なぜ半導体で計算できるのか" `
  --out .\series\semicon-computer\01\note_import_wxr.xml
```

### 軽量インポート検証

note側の取り込み挙動を先に見る場合は、先頭3枚だけの軽いWXRを作ります。

```powershell
uv run python .\tools\export_note_wxr.py `
  --image-base-url https://<user>.github.io/<repo>/semicon-001 `
  --title "noteインポート検証｜10ページ大学" `
  --limit 3 `
  --test-intro `
  --out .\series\semicon-computer\01\note_import_test_wxr.xml
```
