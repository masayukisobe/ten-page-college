# 第3巻 挿絵生成プロンプト集

## 使い方

各挿絵を生成するときは、「共通スタイルプロンプト」と各図の「個別プロンプト」をつなげて使う。

画像は `series/semicon-computer/03/images/` に保存する。ファイル名は本文順に `cover-...jpg`、`fig-00-...jpg`、`fig-01-...jpg` の形にする。

画像生成工程は、このファイルでプロンプトを固定してから始める。生成中に構図や比喩を変えた場合は、先にこのファイルへ反映してから画像を保存する。

画像内テキストは、理解を上げる短い日本語ラベルだけにする。英語ラベルを並べた図にしない。ただし「OS」は本文タイトルでも使う用語として許可する。`APP`、`FILE`、`RAM`、`STORAGE`、`SOURCE`、`COMPILE`、`DRIVER`、`PATCH` は使わない。

## 共通スタイルプロンプト

```text
Use case: scientific-educational
Asset type: 10-page-college volume 3 illustration for a Japanese adult-learning Markdown/PDF article, horizontal 16:9
Style/medium: polished semi-flat raster illustration with soft 3D depth, modern Japanese explainer book style, clean editorial composition, not SVG, not a placeholder.
Audience: adult non-engineers who use smartphones and PCs but do not yet understand apps, OS, files, events, drivers, and permissions.
Scene/backdrop: warm off-white educational paper background, quiet desk-like space, subtle shadows, generous margins.
Mood: practical, clear, "the hidden mechanism behind the familiar screen becomes visible".
Color palette: warm off-white, charcoal, deep teal, blue, muted amber, coral, pale blue-gray, with a few green accents. Avoid one-note purple, dark slate, beige-only, or orange-brown palettes.
Composition: one clear concept per image, large readable shapes, varied metaphors across figures, no repetitive box-arrow template. Use perspective shelves, workbenches, windows, gates, tickets, maps, layers, devices, and cutaways where appropriate.
Text policy: use only the Japanese labels listed in Text (verbatim). Render them large, crisp, and sparse. Do not add any other text, pseudo text, fake UI copy, brand names, English labels, or tiny annotations. "OS" is allowed only where explicitly listed.
Avoid: real company logos, real app-store logos, specific iOS/Android/Windows UI, watermarks, dense circuit boards, photorealistic stock images, dark cyberpunk, cluttered flowcharts, identical simple box-and-arrow diagrams.
```

## 扉表紙

### cover-app-os-devices.jpg

```text
Caption: OSはスマホやPCの中で何をやっているのか
Primary request: Cover image for a Japanese explainer volume about what an OS does inside smartphones and PCs.
Subject: a smartphone and laptop with transparent lifted screen layers, revealing an OS layer coordinating app icons, files, touch input, camera, speaker, and update pieces underneath.
Composition/framing: horizontal cover, device interior cutaway, OS layer visually central; open space around the illustration for the page title outside the image.
Text (verbatim): 「OS」
Avoid: readable fake UI, brand logos, English labels, dark hacker mood, only abstract gradients.
```

## はじめに

### fig-00-01-photo-edit-post-os-mediation.jpg

```text
Caption: 写真を撮り、編集し、投稿しようとするまでにOSが何度も仲介している
Primary request: A familiar smartphone flow where taking a photo, editing it, selecting it for posting, typing, permission, and update all pass through OS mediation.
Subject: one smartphone timeline with camera, photo editor, post composer, keyboard, permission gate, and update badge; a calm OS pathway connects these steps underneath.
Composition/framing: panoramic left-to-right scene with several everyday episodes connected by a subtle OS route, not a rigid flowchart.
Text (verbatim): 「撮る」 「編集」 「選ぶ」 「許可」 「更新」 「OS」
Avoid: real SNS logos, fake post text, crowded notification UI, English labels.
```

## 1ページ目

### fig-01-01-app-icon-entrance.jpg

```text
Caption: ホーム画面のアイコンはアプリ本体ではなく入口
Primary request: A home-screen icon is an entrance to the app, not the app itself.
Subject: a generic smartphone home screen; one icon opens like a doorway into a backstage room containing app parts and instructions.
Composition/framing: close view of the phone icon becoming a doorway, with the app body visible behind it.
Text (verbatim): 「入口」 「アプリ本体」
Avoid: brand app icons, flat icon-only diagram, English labels.
```

### fig-01-02-app-bundle.jpg

```text
Caption: アプリは命令、画面部品、素材、設定のまとまり
Primary request: An app is a bundle of instructions, screen parts, assets, and settings.
Subject: a neat app package opened on a desk, containing instruction cards, UI component tiles, image and sound chips, and a settings gear.
Composition/framing: warm product-like cutaway, each part visually distinct inside one bundle.
Text (verbatim): 「命令」 「画面部品」 「素材」 「設定」
Avoid: software-code wall, English labels.
```

### fig-01-03-input-process-output.jpg

```text
Caption: 入力からアプリの処理を通って画面や音の出力になる
Primary request: Input goes into app processing and returns as screen, sound, or saved file output.
Subject: fingers, photo, text, and location icons enter an app workshop; the app produces a screen result, speaker sound, and a file card.
Composition/framing: lively workshop metaphor with input on left, app processing in center, outputs on right.
Text (verbatim): 「入力」 「処理」 「画面」 「音」 「保存」
Avoid: generic three-box arrow chart, English labels.
```

### fig-01-04-same-app-pattern.jpg

```text
Caption: 電卓、写真、SNSも入力を処理して結果を返す同じ型
Primary request: Calculator, photo, and social apps share the same pattern: receive input, process data, return a result.
Subject: three different mini app scenes arranged in a triptych, each showing its own input and output while sharing the same hidden processing shape.
Composition/framing: three panels with different visual content but a common internal rhythm.
Text (verbatim): 「電卓」 「写真」 「投稿」 「入力」 「結果」
Avoid: making all three panels identical, English labels, real service logos.
```

### fig-01-05-volumes-connection.jpg

```text
Caption: 第1巻の命令、第2巻のデータ、第3巻のアプリがつながる
Primary request: Instructions from volume 1, data from volume 2, and apps from volume 3 connect.
Subject: three educational blocks: instruction execution, media data, and an app screen meeting in a central app-workshop scene.
Composition/framing: layered bridge composition, not a simple numbered list.
Text (verbatim): 「命令」 「データ」 「アプリ」
Avoid: book cover replicas, English labels.
```

## 2ページ目

### fig-02-01-app-store-download.jpg

```text
Caption: アプリストアからアプリのデータが端末へ届く
Primary request: App data travels from a neutral distribution shelf to a device.
Subject: a generic app catalog window sends a sealed app bundle into a smartphone storage area.
Composition/framing: diagonal movement from distribution window to phone, with data packets and a package-like bundle.
Text (verbatim): 「配布」 「端末」
Avoid: App Store or Google Play branding, payment UI, cloud-only metaphor, English labels.
```

### fig-02-02-install-register.jpg

```text
Caption: インストールは保存場所へ置き、OSに登録する
Primary request: Installing puts app parts into storage and registers them with the OS.
Subject: app package parts placed onto storage shelves while an OS desk stamps a registration card.
Composition/framing: shelf plus registration counter, showing "put in storage" and "register" as two connected actions.
Text (verbatim): 「保存」 「登録」 「OS」
Avoid: only showing a download progress bar, English labels.
```

### fig-02-03-source-compile-binary.jpg

```text
Caption: ソースコードからコンパイルを通ってバイナリになる
Primary request: Human-written source code is transformed by compilation into executable binary form.
Subject: recipe-like source cards enter a compact conversion machine and emerge as tidy executable instruction blocks for a device.
Composition/framing: machine-transformation scene with human-readable cards on left, conversion in center, device-ready blocks on right.
Text (verbatim): 「ソース」 「変換」 「実行用」
Avoid: dense real code, fake Japanese code paragraphs, English labels.
```

### fig-02-04-storage-memory-overview.jpg

```text
Caption: 保存装置とメモリの全体図に、インストールと起動を重ねる
Primary request: Show storage and memory together, with installation and launching overlaid.
Subject: lower shelf holds installed app bundles; upper workbench shows one app open and active in memory.
Composition/framing: two-level cutaway; installation path goes to shelf, launch path goes from shelf to workbench.
Text (verbatim): 「保存装置」 「メモリ」 「インストール」 「起動」
Avoid: motherboard realism, confusing many arrows, English labels.
```

### fig-02-05-load-to-memory-launch.jpg

```text
Caption: 保存場所からメモリへ読み込まれて起動する
Primary request: Launching reads an installed app from storage into memory so it can run.
Subject: an OS hand selects an app from a storage shelf and places active app pieces onto a lit memory workbench.
Composition/framing: shelf-to-workbench motion with the app becoming brighter on the workbench.
Text (verbatim): 「保存」 「メモリ」 「起動」 「OS」
Avoid: suggesting the app disappears from storage, English labels.
```

### fig-02-06-installed-vs-running.jpg

```text
Caption: インストール済みアプリと起動中アプリの違い
Primary request: Installed apps and running apps are different states.
Subject: left side shows quiet app bundles stored on shelves; right side shows one app open on a workbench with tools in use.
Composition/framing: clear contrast between dormant shelf and active workbench.
Text (verbatim): 「インストール済み」 「起動中」
Avoid: making installed apps look deleted or broken, English labels.
```

## 3ページ目

### fig-03-01-os-between-app-hardware.jpg

```text
Caption: アプリとハードウェアの間にOSがいる
Primary request: The OS sits between apps and hardware.
Subject: app windows above, device parts below, OS as a service counter or bridge between them.
Composition/framing: layered vertical scene with OS as the middle mediator.
Text (verbatim): 「アプリ」 「OS」 「機械」
Avoid: implying apps directly grab hardware, English labels.
```

### fig-03-02-os-manages-resources.jpg

```text
Caption: OSがCPU、メモリ、ファイル、画面、デバイスを管理する
Primary request: The OS manages processor time, memory, files, screen, and devices.
Subject: OS control room assigning tickets to a processor clock, memory workbench, file cabinet, display panel, and device ports.
Composition/framing: radial management scene with different resource icons, not identical boxes.
Text (verbatim): 「OS」 「計算」 「メモリ」 「ファイル」 「画面」 「機器」
Avoid: overcrowded dashboard, English labels.
```

### fig-03-03-api-window-request.jpg

```text
Caption: アプリがOSのAPI窓口へ依頼する
Primary request: An app asks through an OS request window.
Subject: app clerk submits a request ticket at an OS service window; behind the window are files and devices.
Composition/framing: counter/window metaphor with clear request direction.
Text (verbatim): 「アプリ」 「窓口」 「依頼」 「OS」
Avoid: legal-contract look, English labels.
```

### fig-03-04-request-and-permission.jpg

```text
Caption: 直接操作ではなく、依頼と許可で動く
Primary request: Apps work by request and permission, not direct operation.
Subject: an app reaches for a camera and file cabinet, but an OS gate checks a request ticket and opens only the allowed path.
Composition/framing: permission gate with one open path and one paused path.
Text (verbatim): 「依頼」 「許可」 「OS」
Avoid: scary security alarm mood, English labels.
```

### fig-03-05-many-apps-one-device.jpg

```text
Caption: 複数アプリがOSを通じて同じ端末を使う
Primary request: Multiple apps share the same device through the OS.
Subject: several app windows queue politely through OS routing to one screen, one camera, one speaker, and one storage area.
Composition/framing: shared-terminal scene, showing order and mediation.
Text (verbatim): 「アプリ」 「OS」 「端末」
Avoid: chaotic fight scene, brand app icons, English labels.
```

## 4ページ目

### fig-04-01-storage-to-process.jpg

```text
Caption: 保存場所のアプリが起動するとメモリ上のプロセスになる
Primary request: An installed app in storage becomes a process in memory when launched.
Subject: an app bundle on a storage shelf produces an active glowing process bubble on a memory workbench.
Composition/framing: before-and-after transformation from shelf object to active workspace.
Text (verbatim): 「保存」 「起動」 「プロセス」 「メモリ」
Avoid: implying a process is a new install, English labels.
```

### fig-04-02-shelf-workbench.jpg

```text
Caption: 保存場所は棚、メモリは作業机
Primary request: Storage is like a shelf; memory is like a workbench.
Subject: a shelf full of closed toolboxes next to a workbench where one toolbox is opened and tools are being used.
Composition/framing: warm analogy scene with subtle digital device context.
Text (verbatim): 「棚」 「作業机」
Avoid: making the analogy childish, English labels.
```

### fig-04-03-cpu-memory-shared.jpg

```text
Caption: 複数プロセスにOSがCPU時間とメモリを配る
Primary request: The OS distributes processor time and memory among multiple processes.
Subject: OS scheduler at a round table giving timed work slots and workbench space to several active process cards.
Composition/framing: tabletop allocation scene with timer slices and memory zones.
Text (verbatim): 「OS」 「時間」 「メモリ」 「プロセス」
Avoid: pure pie chart, real OS task manager UI, English labels.
```

### fig-04-04-memory-shortage.jpg

```text
Caption: メモリ不足で作業机が狭くなる
Primary request: When memory is short, the workbench becomes crowded.
Subject: too many active app tasks crowd a limited workbench; OS tries to organize space while a warning light appears.
Composition/framing: cramped but readable workbench scene.
Text (verbatim): 「メモリ不足」
Avoid: disaster imagery, clutter that hides the idea, English labels.
```

### fig-04-05-process-isolation.jpg

```text
Caption: 1つのアプリが固まっても区切りで他を守る
Primary request: Process boundaries help protect other apps when one app freezes.
Subject: several glass-separated work pods; one frozen app pod is paused while neighboring pods continue working.
Composition/framing: calm isolation chambers, visual separation is central.
Text (verbatim): 「区切り」 「停止」 「動作中」
Avoid: malware/security theme, English labels.
```

## 5ページ目

### fig-05-01-data-saved-as-file.jpg

```text
Caption: 第2巻のデータがファイルとして保存される
Primary request: Data from the previous volume becomes saved as files.
Subject: text, photo, audio wave, and video frame data cards being placed into file folders.
Composition/framing: media data transforming into named file cards.
Text (verbatim): 「データ」 「ファイル」
Avoid: saying files are only documents, English labels.
```

### fig-05-02-file-components.jpg

```text
Caption: ファイルはデータ、名前、形式、場所を持つ
Primary request: A file has data, name, format, and location.
Subject: one file folder shown as a cutaway with four visible parts: data stack, name tag, format badge, shelf location marker.
Composition/framing: exploded view of a single file object.
Text (verbatim): 「データ」 「名前」 「形式」 「場所」
Avoid: long labels or fake extensions, English labels.
```

### fig-05-03-folder-path-address.jpg

```text
Caption: フォルダ階層とパスは住所のようなもの
Primary request: Folder hierarchy and path are like an address.
Subject: a building-like folder tree with corridors and room plates leading to one file, paired with a simple map route.
Composition/framing: folder-as-address metaphor, clear destination.
Text (verbatim): 「フォルダ」 「パス」 「ファイル」
Avoid: detailed real filesystem paths, English labels.
```

### fig-05-04-os-open-save.jpg

```text
Caption: アプリがOSに頼んでファイルを開く、保存する
Primary request: Apps ask the OS to open and save files.
Subject: an app hands open/save request tickets to an OS librarian who retrieves or stores a file in cabinets.
Composition/framing: library/counter metaphor, two request motions.
Text (verbatim): 「アプリ」 「OS」 「開く」 「保存」
Avoid: app directly rummaging through cabinets, English labels.
```

### fig-05-05-not-found-causes.jpg

```text
Caption: 見つからないを名前、パス、権限、形式のずれで分ける
Primary request: "File not found" can come from mismatched name, path, permission, or format.
Subject: a search desk with four separate cause cards: wrong name tag, wrong route map, locked permission gate, mismatched format shape.
Composition/framing: diagnostic board with four distinct visual causes.
Text (verbatim): 「名前」 「パス」 「権限」 「形式」
Avoid: merely showing a missing-file icon, English labels.
```

## 6ページ目

### fig-06-01-button-region-promise.jpg

```text
Caption: ボタンの見た目、押せる領域、処理への約束が結びつく
Primary request: A button connects visual appearance, clickable region, and promised action.
Subject: one screen button shown in layers: visible button skin, translucent hit area, and a small action wire leading to a result.
Composition/framing: layered cutaway of a GUI button.
Text (verbatim): 「見た目」 「領域」 「処理」
Avoid: implying a physical plastic button inside the screen, English labels.
```

### fig-06-02-gui-controls.jpg

```text
Caption: GUIはボタン、メニュー、入力欄で操作する画面
Primary request: A GUI is a screen operated through buttons, menus, and input fields.
Subject: a generic app screen with a button, menu, slider, checkbox, and text input, all cleanly arranged.
Composition/framing: friendly interface surface, not a real product UI.
Text (verbatim): 「ボタン」 「メニュー」 「入力欄」
Avoid: dense UI mockup with unreadable fake text, English labels.
```

### fig-06-03-layout-to-pixels.jpg

```text
Caption: アプリの部品配置からOSや描画処理を通ってピクセル表示になる
Primary request: App layout instructions pass through OS and rendering, then become display pixels.
Subject: app layout cards become a rendered screen through an OS/rendering layer, then a zoomed pixel grid on the display.
Composition/framing: layered rendering pipeline with final pixels large enough to see.
Text (verbatim): 「部品配置」 「OS」 「描画」 「ピクセル」
Avoid: simple arrow boxes only, English labels.
```

### fig-06-04-state-redraw.jpg

```text
Caption: 状態が変わると画面が描き直される
Primary request: When app state changes, the screen is redrawn.
Subject: a small counter or toggle state changes inside the app model, then the visible screen refreshes to a new arrangement.
Composition/framing: before/after screen panels with the hidden state card between them.
Text (verbatim): 「状態」 「描き直し」
Avoid: treating redraw as physical paint, English labels.
```

### fig-06-05-button-elements.jpg

```text
Caption: ボタンは見た目、押せる領域、役割、押されたときの処理でできている
Primary request: A button consists of appearance, hit area, role, and action when pressed.
Subject: exploded parts of one button: visible surface, invisible region, role tag, and action trigger.
Composition/framing: clean exploded technical illustration, visually different from fig-06-01 by focusing on parts.
Text (verbatim): 「見た目」 「領域」 「役割」 「処理」
Avoid: physical plastic part metaphor, English labels.
```

## 7ページ目

### fig-07-01-touch-to-event.jpg

```text
Caption: タッチパネルの変化からOSを通ってタップイベントがアプリへ届く
Primary request: A touch panel change becomes a tap event through the OS and reaches the app.
Subject: fingertip touches glass; sensor ripple becomes a small event ticket that passes through OS to an app window.
Composition/framing: tactile-to-data transformation with the event ticket as the main object.
Text (verbatim): 「タッチ」 「イベント」 「OS」 「アプリ」
Avoid: suggesting finger force enters the app directly, English labels.
```

### fig-07-02-event-fields.jpg

```text
Caption: イベントは種類、時刻、場所、対象を持つ
Primary request: An event has type, time, location, and target.
Subject: one event ticket laid out with icons for tap type, clock time, coordinate point, and target button.
Composition/framing: document/ticket metaphor, simple and readable.
Text (verbatim): 「種類」 「時刻」 「場所」 「対象」
Avoid: long form labels, fake code, English labels.
```

### fig-07-03-tap-coordinate-target.jpg

```text
Caption: タップ座標から押されたボタンを判断する
Primary request: The app uses tap coordinates to decide which button was pressed.
Subject: smartphone screen with a coordinate crosshair landing inside one button's highlighted hit area.
Composition/framing: top-down phone view with enlarged coordinate marker.
Text (verbatim): 「座標」 「ボタン」
Avoid: generic target icon detached from the UI, English labels.
```

### fig-07-04-event-loop.jpg

```text
Caption: イベントを待つ、処理する、画面を更新する流れ
Primary request: Event loop waits, processes an event, and updates the screen.
Subject: a calm circular workflow around an app desk: waiting tray, event ticket, handler tool, screen update panel.
Composition/framing: circular loop metaphor with distinct stations.
Text (verbatim): 「待つ」 「処理」 「更新」
Avoid: dense programming flowchart, English labels.
```

### fig-07-05-event-backlog.jpg

```text
Caption: イベント処理が詰まると反応が遅くなる
Primary request: When event processing piles up, the app response feels slow.
Subject: many event tickets stack up in a queue before an app worker, while the screen shows a delayed response indicator.
Composition/framing: queue backlog scene, not a crash scene.
Text (verbatim): 「イベント」 「待ち行列」 「遅い」
Avoid: blaming the user, angry characters, English labels.
```

## 8ページ目

### fig-08-01-app-wants-results.jpg

```text
Caption: アプリが欲しいのは写真、音、位置などの結果
Primary request: Apps want results such as a photo, sound, or location, not raw device mechanics.
Subject: an app request board showing desired outputs: photo card, audio wave, map pin, with device mechanisms hidden behind a curtain.
Composition/framing: results-first scene, app side is simple and goal-oriented.
Text (verbatim): 「アプリ」 「写真」 「音」 「位置」
Avoid: device internals as the main focus, English labels.
```

### fig-08-02-os-common-device-window.jpg

```text
Caption: アプリの依頼をOSの共通窓口が受ける
Primary request: The OS common device window receives app requests.
Subject: several app request tickets arrive at one OS device-service counter before reaching camera, microphone, speaker, and sensor.
Composition/framing: shared counter with different devices behind it.
Text (verbatim): 「アプリ」 「OS」 「共通窓口」
Avoid: showing each app speaking a different hardware language, English labels.
```

### fig-08-03-driver-translates-commands.jpg

```text
Caption: ドライバが共通の依頼を機械ごとの命令に変え、結果やエラーを戻す
Primary request: A driver translates common OS requests into device-specific commands and returns results or errors.
Subject: OS request ticket enters a driver translator booth; device-specific command cards leave toward two different cameras, with result and error cards returning.
Composition/framing: translation booth metaphor, device-specific variation is visible.
Text (verbatim): 「共通の依頼」 「ドライバ」 「機械ごとの命令」 「結果」 「エラー」
Avoid: empty bridge diagram with no translation idea, English labels.
```

### fig-08-04-shared-camera.jpg

```text
Caption: 複数アプリが同じカメラをOS経由で順番に使う
Primary request: Multiple apps use the same camera in order through the OS.
Subject: two or three app windows take turns at an OS-managed camera gate; the camera sends one photo stream at a time.
Composition/framing: orderly queue toward a single camera.
Text (verbatim): 「アプリ」 「OS」 「カメラ」 「順番」
Avoid: apps grabbing the camera simultaneously, English labels.
```

### fig-08-05-device-failure-layers.jpg

```text
Caption: 使えない原因を権限、窓口、ドライバ、デバイスで分ける
Primary request: A device may be unavailable because of permission, OS window, driver, or the device itself.
Subject: layered diagnostic stack from app to permission gate, OS service window, driver translator, and device, with one layer highlighted as a possible fault.
Composition/framing: troubleshooting layer stack with distinct icons for each layer.
Text (verbatim): 「権限」 「窓口」 「ドライバ」 「機器」
Avoid: single broken-camera icon only, English labels.
```

## 9ページ目

### fig-09-01-permission-before-access.jpg

```text
Caption: アプリが写真、カメラ、位置情報を使う前に許可を求める
Primary request: An app asks permission before using photos, camera, or location.
Subject: app window pauses before three protected resources: photo album, camera, map pin; OS permission gate asks for approval.
Composition/framing: everyday permission moment, clear protected resources.
Text (verbatim): 「写真」 「カメラ」 「位置」 「許可」 「OS」
Avoid: real OS permission dialog copy, English labels.
```

### fig-09-02-permission-key.jpg

```text
Caption: 権限は使ってよい機能やデータの鍵
Primary request: Permission is a key for functions or data the app may use.
Subject: a key ring with keys for photo, camera, and location locks; the OS hands only selected keys to an app.
Composition/framing: key-and-lock metaphor, simple and strong.
Text (verbatim): 「権限」 「写真」 「カメラ」 「位置」
Avoid: security alarm or hacker imagery, English labels.
```

### fig-09-03-sandbox-boundaries.jpg

```text
Caption: サンドボックスでアプリごとの範囲を区切る
Primary request: Sandboxes separate each app's area.
Subject: several app work areas inside transparent separated boxes; each app can use its own files while shared resources sit outside behind OS control.
Composition/framing: top-down workspace with clear boundaries.
Text (verbatim): 「アプリ」 「区切り」 「OS」
Avoid: literal beach sand, English labels.
```

### fig-09-04-file-picker-selected-only.jpg

```text
Caption: ファイル選択画面で選んだファイルだけ渡す
Primary request: A file picker hands only the selected file to the app.
Subject: OS file picker tray shows many files; one highlighted file is passed through a narrow slot to the app.
Composition/framing: selection gate, emphasize one chosen item.
Text (verbatim): 「選ぶ」 「このファイルだけ」 「OS」
Avoid: app seeing the whole cabinet, English labels.
```

### fig-09-05-convenience-security-tradeoff.jpg

```text
Caption: 自由すぎる便利さと区切る安全性のトレードオフ
Primary request: There is a tradeoff between unrestricted convenience and bounded safety.
Subject: a balance scale: one side has many open doors and fast shortcuts, the other has fences, keys, and controlled paths; OS keeps the scale balanced.
Composition/framing: balanced metaphor, neither side looks evil.
Text (verbatim): 「便利」 「安全」 「OS」
Avoid: fear-based cybercrime imagery, English labels.
```

## 10ページ目

### fig-10-01-update-replace-parts.jpg

```text
Caption: アップデートでアプリやOSの部品を入れ替える
Primary request: Updates replace parts of apps or the OS.
Subject: a maintenance desk swaps old app and OS component tiles for new matching tiles while the device remains recognizable.
Composition/framing: repair-and-replacement scene, not a download bar only.
Text (verbatim): 「更新」 「入れ替え」
Avoid: implying updates always change the whole device, English labels.
```

### fig-10-02-update-types.jpg

```text
Caption: 新機能追加、不具合修正、セキュリティ修正を分ける
Primary request: Separate feature additions, bug fixes, and security fixes.
Subject: three maintenance cards: new tool added, misaligned gear corrected, weak lock reinforced.
Composition/framing: three visually different repair types in one balanced scene.
Text (verbatim): 「新機能」 「不具合修正」 「安全修正」
Avoid: three identical boxes, English labels.
```

### fig-10-03-bug-vulnerability.jpg

```text
Caption: バグと脆弱性の違い
Primary request: A bug and a vulnerability are different kinds of software problems.
Subject: left: a miswired app mechanism causing wrong behavior inside the app; right: a weak door in the software boundary that could be exploited from outside.
Composition/framing: side-by-side comparison with distinct cause shapes.
Text (verbatim): 「バグ」 「脆弱性」
Avoid: insect imagery as the main idea, English labels.
```

### fig-10-04-virus-effects.jpg

```text
Caption: ウイルスの典型的な被害をファイル、画面、デバイス、権限で見る
Primary request: Typical virus damage can affect files, screens, devices, and permissions.
Subject: a device scene with four affected areas: scrambled file cabinet, distorted screen overlay, camera/speaker misuse, permission keys being misused.
Composition/framing: diagnostic overview, controlled and educational, not frightening.
Text (verbatim): 「ファイル」 「画面」 「機器」 「権限」
Avoid: skulls, horror style, hacker figure, English labels.
```

### fig-10-05-patch-closes-hole.jpg

```text
Caption: パッチが弱点をふさぐ
Primary request: A patch closes a weak spot.
Subject: a software wall or shield with a small crack; a patch tile is fitted over it and the route is sealed.
Composition/framing: close-up repair metaphor with satisfying closure.
Text (verbatim): 「パッチ」 「弱点」
Avoid: antivirus product branding, English labels.
```

### fig-10-06-summary-to-network.jpg

```text
Caption: アプリからOS、画面、入力、ファイル、デバイス、次はネットワークへ
Primary request: Summarize app, OS, screen, input, files, devices, then point to networking next.
Subject: a connected map inside one device: app, OS, screen, input event, file cabinet, camera/speaker; an outgoing path leads toward a distant network cloud for the next volume.
Composition/framing: final roadmap, device interior on left and network horizon on right.
Text (verbatim): 「アプリ」 「OS」 「画面」 「入力」 「ファイル」 「機器」 「ネットワーク」
Avoid: explaining internet details in this volume, English labels.
```
