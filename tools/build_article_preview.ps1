param(
  [string]$DraftPath = "series/semicon-computer/01/draft.md",
  [string]$OutputPath = "series/semicon-computer/01/preview.html"
)

$ErrorActionPreference = "Stop"

$root = (Get-Location).Path
$draftFullPath = if ([System.IO.Path]::IsPathRooted($DraftPath)) { $DraftPath } else { Join-Path $root $DraftPath }
$outputFullPath = if ([System.IO.Path]::IsPathRooted($OutputPath)) { $OutputPath } else { Join-Path $root $OutputPath }
$outputDir = Split-Path -Parent $outputFullPath

function HtmlEncode([string]$text) {
  return [System.Net.WebUtility]::HtmlEncode($text)
}

function InlineMd([string]$text) {
  $encoded = HtmlEncode $text
  $encoded = [regex]::Replace($encoded, '`([^`]+)`', '<code>$1</code>')
  return $encoded
}

$figureMap = @{
  "小さなスイッチが集まってコンピュータになる" = "images/fig001-roadmap-switch-to-computer-ai-text.png"
  "部屋のスイッチ: オンで電気がつく / オフで消える" = "images/fig002-room-switch-off-on-ai-text.png"
  "金属=通す / ゴム=通さない / 半導体=条件で変えられる" = "images/fig003-materials-conductor-insulator-semiconductor-ai-text.png"
  "小さな電気信号で、別の電気の流れをオン・オフするトランジスタ" = "images/fig004-transistor-switch-concept-ai-text.png"
  "前のスイッチの出力信号が、次のスイッチを押す" = "images/fig004b-switch-output-drives-next-switch-ai-text.png"
  "スイッチの組み合わせでANDとNOTを作る入口" = "images/fig004c-and-not-from-switches-ai-text.png"
  "オフ=0 / オン=1" = "images/fig005-switch-off-on-zero-one-ai-text.png"
  "のれんの出ている/しまわれている状態を、人間が意味として読む" = "images/fig006-noren-state-meaning-ai-text.png"
  "10進数は0から9まで使って、次に10へ進む" = "images/fig007-decimal-0-to-10.png"
  "10進数は10種類、2進数は0と1の2種類" = "images/fig008-decimal-vs-binary.png"
  "2進数の10は、10進数の2" = "images/fig009-binary-10-is-two.png"
  "312号室は3階の12号室。数字は読むルールで意味が変わる" = "images/fig010-room-312-floor-room-ai-text.png"
  "2進数の位: 8の位・4の位・2の位・1の位" = "images/fig011-binary-place-values.png"
  "1と1を足すと、次の桁へ上がって10になる" = "images/fig012-one-plus-one-carry.png"
  "スイッチ1個で0か1を表す" = "images/fig013-one-switch-zero-one.png"
  "スイッチ2個で4通りを表せる" = "images/fig014-two-switches-four-patterns.png"
  "8+7の筆算" = "images/fig015-eight-plus-seven-carry.png"
  "一の位から十の位へ1を渡す" = "images/fig016-carry-from-ones-to-tens-ai-text.png"
  "1円玉10枚が10円玉1枚に両替される" = "images/fig017-coin-exchange-carry.png"
  "2進数の1+1で、1を次の桁へ渡す" = "images/fig018-binary-one-plus-one-carry.png"
  "2進数1桁の足し算4パターン" = "images/fig019-binary-addition-four-patterns.png"
  "人間の筆算" = "images/fig020-human-written-addition-and-circuit.png"
  "人間の筆算 と 回路の足し算" = "images/fig020-human-written-addition-and-circuit.png"
  "AとBを入れると、答えとケタ上がりが出る箱" = "images/fig021-input-a-b-output-sum-carry.png"
  "半加算器の表" = "images/fig022-half-adder-table.png"
  "AND: 両方が1のときだけ1" = "images/fig023-and-both-one.png"
  "鍵と暗証番号が両方そろったら開くAND" = "images/fig024-key-and-pin-and.png"
  "XOR: 片方だけが1のときだけ1" = "images/fig025-xor-one-side-only.png"
  "1人席に片方だけ座れるXOR" = "images/fig026-one-seat-xor.png"
  "半加算器: AとBから答えとケタ上がりを出す" = "images/fig027-half-adder-concept.png"
  "半加算器と全加算器の違い" = "images/fig028-half-vs-full-adder.png"
  "23×12の筆算" = "images/fig029-23-times-12-written-multiplication.png"
  "掛け算は、ずらしたものを足す" = "images/fig030-multiply-shift-and-add.png"
  "掛け算は偉そうに見えるが、中身はずらして足す作業" = "images/fig031-multiplication-is-shift-and-add-work.png"
  "101を左にずらすと1010になり、5が10になる" = "images/fig032-binary-101-left-shift.png"
  "左シフト=2倍、右シフト=半分" = "images/fig033-left-right-shift.png"
  "2進数の掛け算は、1の桁だけ足す" = "images/fig034-binary-multiply-add-one-bits.png"
  "筆算の途中メモと、コンピュータの記憶" = "images/fig035-notes-and-computer-memory.png"
  "表向き/裏向きの札で0と1を保つ" = "images/fig036-card-face-state-zero-one.png"
  "フリップフロップが0または1を1つ保持する" = "images/fig037-flip-flop-one-bit.png"
  "DRAMは定期的に見回って中身を保つ" = "images/fig038-dram-refresh-patrol.png"
  "フリップフロップ・SRAM・DRAM・フラッシュメモリのざっくり比較表" = "images/fig039-memory-elements-comparison.png"
  "速いが小さい / 大きいが遅い / 電源を切っても残る" = "images/fig040-memory-hierarchy.png"
  "ALU=計算係" = "images/fig041-alu-calculation-worker.png"
  "メモリ=棚、レジスター=まな板、ALU=包丁とフライパン" = "images/fig042-kitchen-memory-register-alu.png"
  "ALU・レジスター・メモリの位置関係" = "images/fig043-alu-register-memory-map.png"
  "3+5を計算するときの流れ: メモリ -> レジスター -> ALU -> レジスター -> メモリ" = "images/fig044-three-plus-five-flow.png"
  "番号付きロッカーとしてのメモリ" = "images/fig045-numbered-locker-memory.png"
  "番号がないロッカー列で困る人と、番号付きで迷わないCPU" = "images/fig046-address-numbered-vs-unnumbered-lockers.png"
  "アドレス100番を読む / アドレス200番へ書く" = "images/fig047-address-read-write.png"
  "メモリの中にデータとプログラムが並んでいる" = "images/fig048-memory-data-and-program.png"
  "人間向けの命令" = "images/fig049-human-vs-cpu-instruction.png"
  "人間向けの命令 と CPU向けの命令" = "images/fig049-human-vs-cpu-instruction.png"
  "命令も0と1の並びでできている" = "images/fig050-instruction-is-binary.png"
  "命令の0と1が、CPU内の動きに対応している" = "images/fig050b-instruction-bits-to-cpu-actions-ai-text.png"
  "食券と厨房の比喩で、命令が動きに変わる" = "images/fig050c-ticket-instruction-analogy-ai-text.png"
  "読み込み・演算・書き込み・分岐" = "images/fig051-four-instruction-types.png"
  "雨なら傘、晴れならそのまま出る分岐" = "images/fig052-rain-umbrella-branch.png"
  "命令を読む -> 解釈する -> 実行する -> 次へ進む" = "images/fig053-cpu-basic-loop.png"
  "フォンノイマン型コンピュータ: CPU・メモリ・入力・出力" = "images/fig054-von-neumann-basic-map.png"
  "同じ厨房でレシピを変えると料理が変わる。コンピュータもプログラムで仕事が変わる" = "images/fig055-recipe-program-analogy.png"
  "メモリから命令を取り出し、CPUで実行し、結果を戻す" = "images/fig056-fetch-execute-store.png"
  "同じメモリに命令とデータが入っている" = "images/fig057-same-memory-instruction-data.png"
  "半導体スイッチ -> 0と1 -> 足し算 -> 掛け算 -> 記憶 -> 命令 -> コンピュータ" = "images/fig058-summary-roadmap.png"
}

$lines = Get-Content -LiteralPath $draftFullPath -Encoding UTF8
$body = New-Object System.Collections.Generic.List[string]
$inCode = $false
$codeBuffer = New-Object System.Collections.Generic.List[string]
$figureIndex = 0
$currentSection = ""

foreach ($line in $lines) {
  if ($line -match '^```') {
    if (-not $inCode) {
      $inCode = $true
      $codeBuffer.Clear()
    } else {
      $inCode = $false
      $body.Add("<pre><code>$((HtmlEncode ($codeBuffer -join "`n")))</code></pre>")
    }
    continue
  }

  if ($inCode) {
    $codeBuffer.Add($line)
    continue
  }

  if ([string]::IsNullOrWhiteSpace($line)) {
    continue
  }

  if ($line -match '^# (.+)$') {
    $body.Add("<header class=`"article-header`"><p class=`"series`">$(InlineMd $Matches[1])</p><h1>なぜ半導体で計算できるのか</h1><p class=`"lead`">ニュースで聞く半導体が、0と1の仕組みにつながる</p></header>")
    continue
  }

  if ($line -match '^!\[(.+)\]\((.+)\)$') {
    $alt = $Matches[1]
    $src = $Matches[2]
    $body.Add("<figure class=`"cover-figure`"><img src=`"$(HtmlEncode $src)`" alt=`"$(HtmlEncode $alt)`"></figure>")
    continue
  }

  if ($line -match '^## (.+)$') {
    $title = $Matches[1]
    $currentSection = $title
    $appendixTitles = @("まとめ", "重要用語10個", "巻末クイズ", "ChatGPTで深掘りするためのプロンプト", "さいごに")
    if ($title -match '^\d+ページ目') {
      $body.Add("<section class=`"page-section`">")
      $body.Add("<h2>$(InlineMd $title)</h2>")
    } elseif ($title -eq "はじめに") {
      $body.Add("<section class=`"page-section intro-section`">")
      $body.Add("<h2>$(InlineMd $title)</h2>")
    } elseif ($appendixTitles -contains $title) {
      $body.Add("<section class=`"appendix-section`">")
      $body.Add("<h2>$(InlineMd $title)</h2>")
    } else {
      $body.Add("<section class=`"plain-section`">")
      $body.Add("<h2>$(InlineMd $title)</h2>")
    }
    continue
  }

  if ($line -match '^### (.+)$') {
    $body.Add("<h3>$(InlineMd $Matches[1])</h3>")
    continue
  }

  if ($line -match '^---+$') {
    $body.Add("</section>")
    continue
  }

  if ($line -match '^-\s+(.+)$') {
    $body.Add("<p class=`"bullet`">・$(InlineMd $Matches[1])</p>")
    continue
  }

  if ($currentSection -eq "重要用語10個" -and $line -match '^(\d+)\.\s+(.+?)\s*$') {
    $body.Add("<p class=`"term-heading`"><span class=`"term-number`">$($Matches[1])</span><span class=`"term-name`">$(InlineMd $Matches[2].Trim())</span></p>")
    continue
  }

  if ($currentSection -eq "重要用語10個" -and $line -match '^\s+(.+)$') {
    $body.Add("<p class=`"term-description`">$(InlineMd $Matches[1].Trim())</p>")
    continue
  }

  if ($currentSection -eq "巻末クイズ" -and $line -match '^(\d+)\.\s+(.+)$') {
    $body.Add("<p class=`"quiz-item`"><span class=`"quiz-number`">Q$($Matches[1])</span><span class=`"quiz-text`">$(InlineMd $Matches[2].Trim())</span></p>")
    continue
  }

  if ($line -match '^\[ここに「(.+)」.*\]$') {
    $figureIndex += 1
    $caption = $Matches[1].Replace('」と「', ' と ')
    if ($figureMap.ContainsKey($caption)) {
      $src = $figureMap[$caption]
      $body.Add("<figure class=`"figure figure-real`"><img src=`"$src`" alt=`"$(HtmlEncode $caption)`"><figcaption>図${figureIndex}: $(InlineMd $caption)</figcaption></figure>")
    } else {
      $body.Add("<figure class=`"figure figure-placeholder`"><div class=`"placeholder-icon`">図$figureIndex</div><figcaption>$(InlineMd $caption)</figcaption><p>ここに図解を挿入予定</p></figure>")
    }
    continue
  }

  $body.Add("<p>$(InlineMd $line)</p>")
}

if ($inCode) {
  $body.Add("<pre><code>$((HtmlEncode ($codeBuffer -join "`n")))</code></pre>")
}

$html = @"
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>10ページ大学 情報学部 第１巻 - Preview</title>
  <style>
    :root {
      --paper: #f7f3ea;
      --ink: #2f2f2f;
      --teal: #1f7a7a;
      --mustard: #f2b84b;
      --coral: #e76f51;
      --mist: #d7e3e8;
      --white: #fffdf7;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--paper);
      color: var(--ink);
      font-family: "Noto Sans JP", "Yu Gothic", "Meiryo", system-ui, sans-serif;
      line-height: 1.95;
      letter-spacing: 0;
    }
    .wrap {
      width: min(860px, calc(100% - 32px));
      margin: 0 auto;
      padding: 48px 0 96px;
    }
    .article-header {
      padding: 40px 0 28px;
      border-bottom: 4px solid var(--ink);
      margin-bottom: 40px;
    }
    .series {
      color: var(--teal);
      font-weight: 800;
      margin: 0 0 10px;
    }
    h1 {
      font-size: clamp(34px, 7vw, 64px);
      line-height: 1.15;
      margin: 0;
      font-weight: 900;
    }
    .lead {
      font-size: 18px;
      margin: 22px 0 0;
      color: #505050;
    }
    section {
      margin: 0 0 44px;
    }
    .page-section {
      background: var(--white);
      border: 2px solid rgba(47, 47, 47, 0.18);
      border-radius: 8px;
      padding: clamp(22px, 4vw, 44px);
      box-shadow: 0 10px 30px rgba(47, 47, 47, 0.06);
    }
    .plain-section {
      padding: 4px 0;
    }
    .appendix-section {
      background: var(--white);
      border: 2px solid rgba(31, 122, 122, 0.22);
      border-radius: 8px;
      padding: clamp(22px, 4vw, 44px);
      box-shadow: 0 10px 30px rgba(47, 47, 47, 0.05);
    }
    h2 {
      font-size: clamp(24px, 4vw, 34px);
      line-height: 1.35;
      margin: 0 0 26px;
      font-weight: 900;
    }
    h3 {
      font-size: 20px;
      line-height: 1.45;
      margin: 30px 0 14px;
      font-weight: 900;
      color: var(--teal);
    }
    p {
      font-size: 18px;
      margin: 0 0 18px;
    }
    .bullet {
      padding-left: 0.25em;
      font-weight: 700;
    }
    .term-heading {
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 22px 0 6px;
    }
    .term-number,
    .quiz-number {
      flex: 0 0 auto;
      display: inline-grid;
      place-items: center;
      min-width: 42px;
      height: 34px;
      border-radius: 999px;
      background: var(--teal);
      color: white;
      font-size: 15px;
      line-height: 1;
      font-weight: 900;
      font-family: "Cascadia Mono", Consolas, monospace;
    }
    .term-name {
      color: var(--ink);
      font-size: 21px;
      line-height: 1.35;
      font-weight: 900;
    }
    .term-description {
      margin: 0 0 18px 54px;
      padding: 0 0 16px 16px;
      border-left: 4px solid rgba(31, 122, 122, 0.22);
      color: #494949;
      font-size: 17px;
    }
    .quiz-item {
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 12px;
      align-items: start;
      margin: 14px 0;
      padding: 14px 16px;
      border: 1px solid rgba(47,47,47,0.12);
      border-radius: 8px;
      background: #fffaf0;
    }
    .quiz-number {
      background: var(--coral);
    }
    .quiz-text {
      font-weight: 800;
      line-height: 1.65;
    }
    code {
      background: #f1ede3;
      border: 1px solid rgba(47,47,47,0.12);
      border-radius: 4px;
      padding: 0.05em 0.3em;
      font-family: "Cascadia Mono", Consolas, monospace;
      font-size: 0.92em;
    }
    pre {
      background: #292929;
      color: #fff8e8;
      padding: 18px 20px;
      border-radius: 8px;
      overflow-x: auto;
      line-height: 1.55;
      margin: 22px 0;
    }
    pre code {
      background: transparent;
      border: 0;
      padding: 0;
      color: inherit;
      font-size: 16px;
    }
    .figure {
      margin: 28px 0 32px;
    }
    .figure img {
      display: block;
      width: 100%;
      border-radius: 8px;
      border: 2px solid rgba(47,47,47,0.16);
      background: var(--paper);
    }
    .cover-figure {
      margin: -12px 0 44px;
    }
    .cover-figure img {
      display: block;
      width: 100%;
      border-radius: 8px;
      border: 2px solid rgba(47,47,47,0.16);
      background: var(--paper);
    }
    figcaption {
      margin-top: 10px;
      color: #5a5a5a;
      font-size: 14px;
      line-height: 1.5;
      font-weight: 700;
    }
    .figure-placeholder {
      min-height: 230px;
      border: 2px dashed rgba(31,122,122,0.55);
      border-radius: 8px;
      background:
        linear-gradient(135deg, rgba(215,227,232,0.45), rgba(255,253,247,0.75));
      padding: 28px;
      display: grid;
      align-content: center;
      justify-items: center;
      text-align: center;
    }
    .figure-placeholder .placeholder-icon {
      width: 92px;
      height: 92px;
      border-radius: 999px;
      background: var(--teal);
      color: white;
      display: grid;
      place-items: center;
      font-size: 22px;
      font-weight: 900;
      margin-bottom: 14px;
    }
    .figure-placeholder figcaption {
      color: var(--ink);
      font-size: 17px;
      margin: 0;
    }
    .figure-placeholder p {
      color: #777;
      margin: 8px 0 0;
      font-size: 14px;
    }
    @media print {
      body { background: white; }
      .wrap { width: 100%; padding: 0; }
      .page-section { box-shadow: none; break-inside: avoid; }
      .appendix-section {
        box-shadow: none;
        break-before: page;
        break-inside: avoid;
      }
    }
  </style>
</head>
<body>
  <main class="wrap">
    $($body -join "`n    ")
  </main>
</body>
</html>
"@

$utf8Bom = New-Object System.Text.UTF8Encoding($true)
[System.IO.File]::WriteAllText($outputFullPath, $html, $utf8Bom)
Write-Output $outputFullPath
