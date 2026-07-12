---
name: ten-page-college
description: Use when creating, revising, reviewing, building, illustration-planning, image-generation staging, or quality-checking a 10-page-college volume in this repository. Runs the staged workflow from abstract to draft with illustration captions, review, revise, text preview, imagegen illustration embedding, PDF, and quality checks with project policies.
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
- `policies/understanding-uplift-perspective.md`
- `policies/intellectual-delight-perspective.md`
- `policies/final-quality-checklist.md`
- `<volume>/structure.md`

巻のテーマとページ構成は、その巻の最新 `structure.md` を正とする。

## 基本ワークフロー

1. 巻ディレクトリを特定する。例: `series/semicon-computer/02`。
2. `structure.md`、`intro.md`、既存の `abstract-0x.md`、`draft-0x.md`、`review-0x.md` を読む。
3. 各ページの `abstract-0x.md` に、骨格、説明すること、図示すること、知的快感、複雑な概念の構造分析とシーン比喩が入っているか確認する。
4. `abstract-0x.md` から `draft-0x.md` を書く、または推敲する。
5. 初期制作・本文レビュー段階では、画像ファイルを生成しない。本文中には `[ここに「...」図を入れる]` の形で挿絵箇所とキャプションテキストだけを入れる。
6. `draft-0x.md` をレビューする。候補抽出と判定を分け、読者の納得感、理解上昇、知的快感、最終品質の観点を必要に応じて使う。方針違反を見つけた場合は、文言だけでなく節、図、abstract、ページの核への影響範囲を見積もる。
7. `review-0x.md` に、編集レベル、影響範囲の見積もり、理由、abstract反映、draft反映、図対応を記録する。画像未生成の場合は、図対応を「キャプション設計まで」と明記する。
8. レビュー結果は、まず `abstract-0x.md` に戻し、次に `draft-0x.md` へ反映する。
9. レビュー用成果物を作る前に、`policies/final-quality-checklist.md` で本文をセルフレビューする。採用する候補は `abstract-0x.md` と `draft-0x.md` へ反映し、判断ログを `review-0x.md` または巻単位レビュー文書に残す。
10. 本文レビュー用に `draft.md`、`preview.html`、必要ならレビュー用PDFを生成する。この段階では、挿絵箇所がキャプションテキストのまま残っていてよい。
11. ユーザーが本文レビューを終え、本文がある程度固まったあとで、画像生成・埋め込みフェーズへ進む。
12. 画像生成・埋め込みフェーズでは、まず全挿絵の生成プロンプトを `<volume>/figure_prompts.md` に書き出す。本文順のファイル名、キャプション、構図、画像内テキスト方針、避ける表現を先に固定する。
13. `figure_prompts.md` を確認して、似すぎた構図、同じ形の量産、本文とのズレ、画像内テキスト過多を直す。ここまでは画像を生成しない。
14. プロンプトが固まってから、必ず `$imagegen` スキルを使い、各キャプションに対応した個別プロンプトで画像を生成する。仮SVG、同一テンプレート図、単純な箱矢印の量産で代用しない。
15. 生成画像を本文へ埋め込んだら、再度 `policies/final-quality-checklist.md` で、画像と本文が噛み合っているかをセルフレビューする。
16. 画像と本文のレビュー反映後に、`draft.md`、`preview.html`、PDFを再生成する。
17. 完了報告の前に品質チェックを走らせる。

## 挿絵制作フェーズ

挿絵は重い工程として扱い、本文制作と分ける。

### 本文レビュー段階

- `abstract-0x.md` には、図示すること、画面に出す要素、比喩、避ける誤解を具体的に書く。
- `draft-0x.md` には、実画像へのMarkdown参照ではなく、`[ここに「...」図を入れる]` の形で挿絵箇所とキャプションテキストを置く。
- この段階では、画像ファイル、仮SVG、汎用プレースホルダー画像を作らない。
- `preview.html` とレビュー用PDFは、本文と挿絵箇所レビュー用として生成する。画像数不足の警告は、本文レビュー段階では想定内として扱う。
- レビュー用PDFを作る場合も、画像生成済みの最終PDFとは区別し、「レビュー用」「画像未生成」と報告する。
- レビュー用PDFを作る前に、`policies/final-quality-checklist.md` を使って、商品価値、内容の深さ、例と比喩、情報密度、読者の変化を確認する。
- final-quality-check で採用した修正は、先に `abstract-0x.md` に戻し、次に `draft-0x.md` へ反映する。判断ログは `review-0x.md` または巻単位レビュー文書に残す。
- 完了報告では、「本文レビュー版」「画像未生成」「挿絵はキャプション設計まで」のように、フェーズを明確に書く。

### 画像生成・埋め込み段階

- ユーザーが「画像生成へ進む」「挿絵を入れる」「最終PDFにする」などを明示したら開始する。
- 画像生成前に、全ページの挿絵キャプションを一覧化し、重複、似すぎた構図、本文とのズレを整理する。
- 各図の画像生成プロンプトを、生成作業とは分けて `<volume>/figure_prompts.md` に書き出す。
- `figure_prompts.md` には、共通スタイルプロンプト、保存先、ファイル名、本文キャプション、個別プロンプト、画像内テキスト方針、避ける表現を含める。
- プロンプト書き出し後に、本文順・ページ別の流れとして成立しているか、同じ構図が続きすぎていないか、本文の理解上昇点が絵に出ているかを確認してから画像生成へ進む。
- `$imagegen` スキルを使い、各図ごとに別の目的、構図、対象物、比喩、ラベル方針を持つプロンプトを作る。
- 同じ見た目の図を量産しない。画面、デバイス、OSの窓口、棚と机、イベントの注文票、サンドボックス、パッチなど、本文中の比喩や概念に合わせて絵柄と構図を変える。
- 画像生成AIに日本語ラベル込みで生成させる前提にする。ただし、英語ラベルを並べた図にしない。`APP`、`FILE`、`RAM`、`STORAGE` のような英語ラベルで説明した気にならず、本文の概念に沿った短い日本語ラベルを使う。
- 完全無文字指定はデフォルトにしない。ラベルがあることで理解が上がる図では、「アプリ」「保存」「起動」「メモリ」「ファイル」「許可」「更新」のような短い日本語ラベルを使う。文字崩れが出た場合は、無文字化ではなく、ラベル数、文字数、配置、構図を見直して再生成する。
- 生成後は、画像ファイルを巻ディレクトリの `images/` に保存し、`draft-0x.md` の挿絵箇所を `![キャプション](images/...)` へ置き換える。
- 画像を埋め込んだら、`draft.md`、`preview.html`、PDFを再生成し、品質チェックを行う。
- 画像生成後の最終版でも、`policies/final-quality-checklist.md` を再実行し、画像によって説明が強くなったか、本文と画像がずれていないかを確認する。
- 画像が未生成のまま、最終版・完成版として報告しない。

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
