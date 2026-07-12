# handoff

## 現在の制作対象

現在の主な制作対象は、第4巻「インターネットとクラウドが１秒間でやっていること」である。

第4巻の構成は、[series/semicon-computer/04/structure.md](/home/masayuki/ten-page-college/series/semicon-computer/04/structure.md) を正とする。

第4巻の個別ページは、`series/semicon-computer/04/abstract-0x.md`、`draft-0x.md`、`review-0x.md` を使って制作する。

## 現在の作業状態

- `series/semicon-computer/04/intro.md`、`abstract-01.md` から `abstract-10.md`、`draft-01.md` から `draft-10.md`、`review-01.md` から `review-10.md` を作成済み。
- `series/semicon-computer/04/draft.md` と `series/semicon-computer/04/preview.html` は、個別draftから再生成済み。
- `series/semicon-computer/04/final-quality-review-0707.md` に、画像生成前の final-quality-check と human review 反映ログを記録済み。
- 第4巻では、はじめにと1ページ目を導入部とし、Webサービス利用の体験からリクエスト、近くの入口、DNS、パケット、中継、HTTP/API、クラウド側の役割分担へ進む構成にしている。
- human review 反映として、効能宣言の再告知、唐突な初出語、自明なゼロuplift文、次巻予告の散在を修正済み。
- 2026-07-07 の追加指摘を受け、Wi-Fi説明の紙幅を短縮し、通信契約、プロバイダ契約、Wi-Fi機器、通信会社ネットワークの役割分担を第2ページへ反映済み。
- `project.md`、`policies/understanding-uplift-perspective.md`、`policies/reader-conviction-perspective.md`、`policies/final-quality-checklist.md` に、既知度のグラデーションと、商品名・契約名で一体に見えるものを仕組み上の役割へ分ける観点を反映済み。
- 2026-07-08 の追加指摘を受け、常識説明に専門ラベルを貼っただけの疑似upliftを検出する観点を `project.md`、`policies/understanding-uplift-perspective.md`、`policies/final-quality-checklist.md`、`policies/intellectual-delight-perspective.md` へ反映済み。
- 第4巻本文は、DNS階層とTTL、MTUとヘッダー階層、ASと経路表、TCPの再送/輻輳制御、HTTPメソッド/TLS証明書、クラウドの索引/キュー/ワーカー、CDNの鮮度管理、冗長化の状態管理へ踏み込む形に再執筆済み。
- 2026-07-08 の追加指摘を受け、否定命題で余計なハテナを作る問題を検出する観点を方針文書へ追加し、第4巻本文、abstract、structure、review の否定表現を総ざらいして肯定形へ修正済み。読者症状、HTTP状態、経路切り分け、信頼性設計の足場になる `つながらない`、`ページが開かない`、`止まる`、`詰まる`、`壊れる`、`失敗`、`エラー` は意図的に残している。
- 2026-07-08 の追加指摘を受け、専門的に踏み込んだ箇所が as-is/what/how の部品説明に寄っていた問題を修正済み。DNSは、名前を使い続けたい利用者側とサーバー場所を変えるサービス側の事情から入り、AS/経路情報、HTTP、クラウド役割分担、CDN/負荷分散も why から what/how へ進む流れへ更新済み。
- 2026-07-08 の追加指摘を受け、whyが技術側の事情から始まり読者の日常の足場が弱い問題を修正済み。方針文書には、whyを普段見る画面、設定、契約、待ち時間、トラブル、同じ操作なのに結果が違う場面から立てる観点を追加した。第4巻本文では、同じURLで開ける期待、場所や契約で入口が変わる体験、同じ画面のボタン操作、店カードや写真表示のずれ、地図画像がすぐ出る体験、セール時のアクセス集中を足場にして、DNS、AS/経路、HTTP、クラウド、CDN、冗長化へ進む形へ更新済み。

## 次に進める作業

ユーザーが、第4巻の挿絵なし全文をレビューする。

レビュー対象は、主に [series/semicon-computer/04/draft.md](/home/masayuki/ten-page-college/series/semicon-computer/04/draft.md) と [series/semicon-computer/04/preview.html](/home/masayuki/ten-page-college/series/semicon-computer/04/preview.html) である。

追加修正があれば、該当ページの `abstract-0x.md`、`draft-0x.md`、`review-0x.md`、必要に応じて `structure.md` と方針文書へ反映し、`draft.md` と `preview.html` を再生成する。

画像生成とPDF生成は、ユーザーが挿絵なし全文を確認したあとに進める。
