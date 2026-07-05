---
name: ten-page-college
description: Use when creating, revising, reviewing, building, or quality-checking a 10-page-college volume in this repository. Runs the abstract -> draft -> review -> revise -> preview -> PDF workflow with project policies.
---

# ten-page-college

10ページ大学の巻制作、推敲、レビュー反映、HTML/PDF生成、品質確認で使う。

## 最初に読む

本文を書いたり推敲したりする前に、次を読む。

- `project.md`
- `series_plan.md`
- `handoff.md`
- `policies/draft-writing-policy.md`
- `policies/reader-conviction-perspective.md`
- `policies/intellectual-delight-perspective.md`
- `policies/final-quality-checklist.md`
- `<volume>/structure.md`

巻のテーマとページ構成は、その巻の最新 `structure.md` を正とする。

## 基本ワークフロー

1. 巻ディレクトリを特定する。例: `series/semicon-computer/02`。
2. `structure.md`、`intro.md`、既存の `abstract-0x.md`、`draft-0x.md`、`review-0x.md` を読む。
3. 各ページの `abstract-0x.md` に、骨格、説明すること、図示すること、知的快感、複雑な概念の構造分析とシーン比喩が入っているか確認する。
4. `abstract-0x.md` から `draft-0x.md` を書く、または推敲する。
5. `draft-0x.md` をレビューする。候補抽出と判定を分け、読者の納得感、知的快感、最終品質の観点を必要に応じて使う。
6. `review-0x.md` に、編集レベル、理由、abstract反映、draft反映、図対応を記録する。
7. レビュー結果は、まず `abstract-0x.md` に戻し、次に `draft-0x.md` へ反映する。
8. `draft.md` と `preview.html` を生成する。
9. `preview.html` が変わったらPDFを生成または更新する。
10. 完了報告の前に品質チェックを走らせる。

## 生成コマンド

リポジトリルートから実行する。

MarkdownとHTMLを生成する。

```bash
rtk python3 tools/build_volume.py --volume series/semicon-computer/02
```

Markdown、HTML、PDFを生成し、チェックまで実行する。

```bash
rtk python3 tools/build_volume.py \
  --volume series/semicon-computer/02 \
  --pdf output/pdf/semicon-computer-02-digital-data.pdf \
  --check
```

再生成せずチェックだけ実行する。

```bash
rtk python3 tools/check_volume_quality.py \
  --volume series/semicon-computer/02 \
  --pdf output/pdf/semicon-computer-02-digital-data.pdf \
  --require-pdf
```

PDFへの反映漏れを検出したい場合は、期待する文字列を追加する。

```bash
rtk python3 tools/check_volume_quality.py \
  --volume series/semicon-computer/02 \
  --pdf output/pdf/semicon-computer-02-digital-data.pdf \
  --require-pdf \
  --expect-pdf-text "圧縮は、くり返し、辞書、知覚を使い分ける"
```

## 完了条件

巻制作や推敲が完了したと報告する前に、次を確認する。

- `draft.md` と `preview.html` が最新のページ別draftから再生成されている。
- MarkdownとHTMLの画像参照が実在する。
- PDFが必要な場合、PDFが存在し、`preview.html` より新しい。
- 重要な追加図や追加文言がある場合、PDF内にも反映されている。
- `review-0x.md` または巻単位レビュー文書に判断ログがある。
- `git diff --check` が通る。

チェックが失敗した場合は、成果物を直すか、具体的なブロッカーを報告する。
