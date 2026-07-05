# 第2巻 挿絵生成プロンプト集

## 使い方

各挿絵を生成するときは、「共通スタイルプロンプト」と各図の「個別プロンプト」をつなげて使う。

画像は `series/semicon-computer/02/images/` に保存する。ファイル名は本文順に `fig001-...png` とする。扉画像は `cover-digital-data.png` とする。

画像内テキストは、`0`、`1`、`UTF-8`、`RGB`、`ZIP`、`JPEG` のような短い語だけにする。長い説明は本文で行う。文字が崩れた場合は、文字を減らして再生成する。

## 共通スタイルプロンプト

```text
Use case: scientific-educational
Asset type: illustration for a Japanese adult-learning Markdown article, horizontal 16:9
Style/medium: clean flat editorial illustration, thick charcoal linework, warm off-white paper background, simple shapes, generous margins, polished but not childish.
Audience: adult learners who want plain explanations of computer science concepts.
Mood: approachable, calm, practical, "the hidden mechanism becomes visible".
Color palette: warm off-white #F7F3EA, charcoal #2F2F2F, deep teal #1F7A7A, muted yellow #F2B84B, coral #E76F51, pale blue-gray #D7E3E8.
Composition: one clear concept per image, large readable shapes, 16:9 landscape, balanced empty space for article layout.
Text constraints: use only short large labels when needed. Keep any text crisp and exact. Avoid tiny Japanese labels, pseudo text, watermarks, logos, UI clutter, photorealism, dark cyberpunk, dense circuit boards.
```

## 扉表紙

### cover-digital-data.png

```text
Primary request: Cover image for the article "文字・画像・音はなぜ0と1で表せるのか".
Subject: a friendly visual chain from text, pixel image, audio waveform, and video frame into a stream of 0 and 1, then back into a smartphone screen.
Composition/framing: horizontal 16:9 cover. Title area has enough open space. Illustration flows left to right with simple icons.
Text (verbatim): 「10ページ大学 情報学部 第2巻」 「文字・画像・音はなぜ0と1で表せるのか」
Avoid: crowded infographic, small technical labels, black background, realistic computer parts.
```

## 本文挿絵

### fig001-switch-off-on-zero-one.png

```text
Primary request: A simple semiconductor switch idea: off maps to 0, on maps to 1.
Subject: two side-by-side switch icons, left off with a dim lamp and 0, right on with a warm lamp and 1.
Text (verbatim): 「OFF」 「0」 「ON」 「1」
```

### fig002-aiueo-number-table.png

```text
Primary request: A tiny "あいうえお" number table turning numbers into characters.
Subject: a small table on the left with 1=あ, 2=い, 3=う, and an arrow to a short character string on the right.
Text (verbatim): 「1=あ」 「2=い」 「3=う」
```

### fig003-bw-dot-grid-bitstream.png

```text
Primary request: A black-and-white dot picture becomes a row of 0 and 1, then folds back into a grid.
Subject: left: small black-white pixel grid; center: horizontal bit stream; right: same grid restored by row width.
Text (verbatim): 「0」 「1」
```

### fig004-same-file-two-readings.png

```text
Primary request: The same homework file opens correctly on one screen and as mojibake on another.
Subject: one document icon splitting into two laptop screens, left readable neat text blocks, right garbled symbols.
Text (verbatim): 「同じファイル」 「読める」 「文字化け」
```

### fig005-encoding-decoding-mismatch.png

```text
Primary request: Encoding and decoding promises get out of sync, causing mojibake.
Subject: left "文字" becomes 0/1 through an encoding gate, then goes through a wrong decoding gate and turns into garbled marks.
Text (verbatim): 「符号化」 「復号」 「0 1」 「?」
```

### fig006-same-bits-different-reading.png

```text
Primary request: The same 0/1 sequence is read with two different dictionaries and becomes different characters.
Subject: a single bit strip in the middle, two dictionary books below it, one produces a normal character card, the other produces garbled symbols.
Text (verbatim): 「同じ0と1」 「辞書A」 「辞書B」
```

### fig007-photo-pixels-zoom.png

```text
Primary request: A photo zooms in until it becomes visible colored pixels.
Subject: simple landscape/photo thumbnail with a magnifying glass revealing large square pixels.
Text (verbatim): 「ピクセル」
```

### fig008-rgb-values-per-pixel.png

```text
Primary request: One pixel has three color numbers: R, G, and B.
Subject: one large square pixel, split or connected to three sliders/bars for red, green, blue.
Text (verbatim): 「R」 「G」 「B」 「255」 「0」
```

### fig009-rgb-to-sepia-pixel.png

```text
Primary request: One pixel's RGB values change into sepia-toned RGB values.
Subject: left cool-colored pixel with RGB number chips, arrow, right warm sepia pixel with changed number chips.
Text (verbatim): 「RGB」 「セピア」
```

### fig010-signals-change-over-time.png

```text
Primary request: Voice, light, and temperature become changing signals over time.
Subject: three simple icons: microphone, light bulb, thermometer, each connected to a smooth line graph.
Text (verbatim): 「声」 「光」 「温度」
```

### fig011-sampling-smooth-wave.png

```text
Primary request: A smooth wave is sampled by taking dots at regular intervals.
Subject: large smooth teal wave with evenly spaced highlighted dots on it, arrow to a row of dot samples.
Text (verbatim): 「標本化」
```

### fig012-quantization-nearest-step.png

```text
Primary request: Real measured values are rounded to the nearest step on a vertical scale.
Subject: smooth value points next to a ruler-like stepped scale; arrows snap points to nearest steps.
Text (verbatim): 「量子化」
```

### fig013-sampling-vs-quantization-axes.png

```text
Primary request: Compare horizontal sampling and vertical quantization on a wave graph.
Subject: one graph, horizontal direction shows denser time dots, vertical direction shows grid steps; use colored arrows for horizontal and vertical.
Text (verbatim): 「横: 標本化」 「縦: 量子化」
```

### fig014-finer-sampling-more-data.png

```text
Primary request: Measuring more finely increases the amount of data.
Subject: top row sparse dots with short bit strip; bottom row dense dots with long bit strip.
Text (verbatim): 「少ない」 「多い」
```

### fig015-audio-wave-to-number-list.png

```text
Primary request: An audio waveform sampled at intervals becomes a list of numbers.
Subject: microphone to waveform, dots on waveform, arrows down to simple numbered tiles.
Text (verbatim): 「波形」 「数字」
```

### fig016-fast-playback-wave-compressed.png

```text
Primary request: The same waveform squeezed into a shorter time has closer peaks and sounds higher.
Subject: two waveforms stacked, top normal length, bottom compressed horizontally with peaks closer together.
Text (verbatim): 「通常」 「早回し」
```

### fig017-low-high-fps-motion.png

```text
Primary request: Low fps looks choppy, high fps looks smoother.
Subject: two strips of bouncing ball frames, top with few frames and big jumps, bottom with many frames and smooth movement.
Text (verbatim): 「少ないfps」 「多いfps」
```

### fig018-video-audio-subtitle-timeline.png

```text
Primary request: Video frames, audio waveform, and subtitles align on the same timeline.
Subject: horizontal timeline with three tracks: frame thumbnails, audio waveform, subtitle blocks.
Text (verbatim): 「映像」 「音声」 「字幕」
```

### fig019-format-needed-to-read-bits.png

```text
Primary request: A raw 0/1 bit string cannot be understood until a file format tells how to read it.
Subject: bit strip going into a question mark, then a format card unlocks icons for text, image, audio.
Text (verbatim): 「0 1」 「形式」
```

### fig020-app-supports-format.png

```text
Primary request: Only an app that knows the file format can open it correctly.
Subject: file icon with a format badge, one app window opens it correctly, another app window shows a closed lock or question mark.
Text (verbatim): 「開ける」 「?」
```

### fig021-codec-decodes-media.png

```text
Primary request: A codec decodes compressed video and audio into frames and waveform.
Subject: compressed box enters a codec machine, output becomes video frame cards and audio waveform.
Text (verbatim): 「codec」 「映像」 「音声」
```

### fig022-mp4-container-codec.png

```text
Primary request: An MP4 container box holds video, audio, and timing information; codec restores video and audio.
Subject: open MP4 box with three cards inside: video, audio, timing; nearby codec tool unpacks video/audio.
Text (verbatim): 「MP4」 「映像」 「音声」 「時刻」 「codec」
```

### fig023-large-media-compressed.png

```text
Primary request: Large photo and video data become smaller through compression.
Subject: oversized photo/video stack squeezed through a compression press into a smaller file.
Text (verbatim): 「圧縮」
```

### fig024-run-length-shorter-expression.png

```text
Primary request: A repeated character string is represented more shortly as a count.
Subject: long row of identical character tiles becoming one tile plus a count marker.
Text (verbatim): 「あ×10」
```

### fig025-lossless-compression-returns.png

```text
Primary request: Lossless compression makes data smaller and then returns it exactly.
Subject: document goes into small zipper file, then comes back as identical document with check mark.
Text (verbatim): 「可逆」 「完全に戻る」
```

### fig026-lossless-vs-lossy-two-columns.png

```text
Primary request: Two-column comparison of lossless and lossy compression.
Subject: left column: exact restore with document; right column: photo/music becomes smaller by removing hard-to-notice details.
Text (verbatim): 「可逆」 「非可逆」 「戻る」 「軽い」
```

### fig027-markup-makes-heading.png

```text
Primary request: Markup characters turn plain text into a heading or emphasized text.
Subject: left plain text with # mark, arrow to right rendered heading card with bold title style.
Text (verbatim): 「# 見出し」 「見出し」
```

### fig028-html-to-browser-page.png

```text
Primary request: HTML role marks are read by a browser to build a page.
Subject: left code-like blocks with heading/link/image icons, arrow to browser window with heading, paragraph, link, image placeholder.
Text (verbatim): 「HTML」 「ブラウザ」
```

### fig029-bits-plus-rules-become-data.png

```text
Primary request: 0 and 1 plus reading rules become readable text, image, audio, and video data.
Subject: central bit stream, around it rule cards labeled UTF-8, RGB, sampling, format, arrows to text/image/audio/video icons.
Text (verbatim): 「0 1」 「UTF-8」 「RGB」 「形式」
```

### fig030-multimedia-combination.png

```text
Primary request: A web page or social media post combines text, image, audio, and video.
Subject: clean smartphone/web page mockup with text blocks, photo tile, play button, small music note.
Text (verbatim): 「文字」 「画像」 「音」 「動画」
```
