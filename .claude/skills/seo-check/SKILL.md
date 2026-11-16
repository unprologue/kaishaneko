---
name: seo-check
description: 会社猫サイトの全HTMLページの title・description・OGP・構造化データ・alt・sitemap を点検し、表で報告する。ページの追加や変更のあと、公開前に使う。
---

サイト内のすべての .html を対象に次を確認し、ページごとの表で報告してください。このスキルでは修正しません。直すかどうかは私が決めます。

| 確認項目 | 基準 |
| --- | --- |
| title | ある。30字前後（目安20〜32字）。サイト内で重複がない |
| meta description | ある。80〜110字。重複がない |
| canonical | 絶対URLで、そのページ自身を指している |
| OGP | og:type、og:url、og:title、og:description、og:image、og:image:width、og:image:height、og:image:alt がある。og:image のファイルが実在する |
| twitter:card | summary_large_image |
| H1 | ちょうど1つ |
| 画像の alt | alt 属性が無い画像と、意味のある画像なのに alt="" のものを挙げる |
| 構造化データ | JSON として正しく読める。表示内容（価格など）と食い違わない |
| 内部リンク | リンク切れがない |
| sitemap.xml | 公開ページがすべて載っていて、存在しないURLが無い |
| robots.txt | あり、Sitemap の行がある |

- 字数は全角・半角とも1字として数える
- 点検用の短いスクリプトを書いて実行してよい。作業用のファイルはコミットしない
- 最後に、優先度（高・中・低）を付けた修正案を3〜10件にまとめる
