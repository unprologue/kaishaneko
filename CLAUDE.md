# 会社猫（kaishaneko.net）サイト

## このリポジトリについて
- 会社猫（かいしゃねこ）は、企業ロゴ入りの九谷焼の招き猫。運営は UNPROLOGUE株式会社、製造は宮創製陶所株式会社（石川県小松市）
- 静的サイト（HTML / styles.css / script.js）。GitHub Pages で公開している
- 注文は Shopify（今は mp1vnh-e3.myshopify.com。shop.kaishaneko.net に移行予定）
- 改善計画は docs/site-plan.md。作業の前に、関係する章を必ず読む

## 公開と確認
- 公開ブランチ：main（違っていたらここを直す）。ここに入った変更が GitHub Pages で公開される
- 変更は作業用ブランチで行い、オーナーが「公開して」と言ったら公開ブランチに入れる
- 表示はローカルサーバーで確認する（例：python3 -m http.server 8000）
- GitHub Pages ではサーバー側のリダイレクトが使えない。既存URLは変えない
- CLAUDE.md、docs/、.claude/ はサイトに公開しない（_config.yml の exclude で外している）。社内用のファイルを足すときは、_config.yml の exclude にも追加する
- このリポジトリは GitHub 上で公開されている。秘密にしたい情報はリポジトリに書かない

## 進め方
- 大きな変更は、まず「変更するファイルと変更点の一覧」を出し、OKをもらってから実装する
- 1回の作業は1つのテーマに絞る
- 作業の最後に .claude/skills/seo-check/SKILL.md の基準で点検し、結果を表で報告する
- 新しく書いた文は、どこが新しいかを報告する

## ブランドの言葉
- 表記：初出は「会社猫（かいしゃねこ）」。英字は「KAISHA NEKO」
- キャッチコピー「福とご縁を、会社へ。」は残す
- 定義文（docs/site-plan.md の1章）は、指示なく変えない
- 3つの「なぜ」：九谷焼＝枯れずに残る本物／招き猫＝人とご縁を招く／ロゴを貼る＝だるまの目入れと同じ願掛け
- 使った後の5場面：届く・貼る・飾る・語られる・残る

## 書き方
- 各セクションの最初の1文で結論を書く。1文は短く
- 数字は正確に。XS 6cm 9,900円／S 15cm 55,500円／M 21cm 88,000円／L 30cm 122,000円（税込・国内送料込み）。納期はご注文から2ヶ月以内。宮創製陶所は創業113年
- 正直に書く：本体の成形・焼成・色は九谷焼の職人仕事、ロゴは最後にシールで貼る。この境目をぼかさない
- 九谷焼・招き猫・だるまの歴史や意味は、docs/site-plan.md の出典の範囲で書く。新しい事実を足すときは、出典URLをHTMLコメントで残す

## 絶対にしないこと
- 事例・お客様の声・評価・実績数を作らない。実在企業の名前やロゴは、掲載許諾があるものだけ使う
- 価格・納期・支払い条件、特商法とプライバシーポリシーの内容を、指示なく変えない
- 構造化データに、ページに表示していない情報（評価、レビュー、価格など）を書かない
- 「架空のもの」という注記は消さない。対象をはっきりさせる形でのみ直す
- 分からない事実を推測で埋めない。<!-- TODO: 確認 --> を残して報告する

## 各ページの必須項目（新規・既存とも）
- title：30字前後。「ページ固有の言葉｜会社猫」（トップだけ「会社猫｜…」）
- meta description：80〜110字。最初の50字で「何を・誰に」が分かる。本文に書いてあることだけ書く
- title と description の文は docs/site-plan.md の4章を使う
- canonical（絶対URL）
- OGP：og:type、og:site_name（会社猫）、og:locale（ja_JP）、og:url、og:title、og:description、og:image（1200×630。/ogp/ にページごとのファイル）、og:image:width、og:image:height、og:image:alt
- twitter:card は summary_large_image
- H1 は1つ。何のページかが分かる言葉を入れる
- 画像は全てに内容を表す alt を付ける（飾りだけの画像は alt=""）
- 構造化データ：トップは WebSite・Organization・Product（docs/site-plan.md の9章）。下層は BreadcrumbList。事例は Article も
- 新しいページは sitemap.xml に追加し、ナビか関係するページからリンクする

## URL構成
- 新規：/story/、/kutani/、/scenes/opening/、/scenes/relocation/、/scenes/anniversary/、/scenes/reception/、/scenes/logo-ceremony/、/lineup/、/order/、/works/、/works/<会社のslug>/、/logo-guide/、/faq/、/contact/
- 既存（URLは変えない）：/company.html、/legal/tokushoho.html、/legal/privacy.html
- 新しいページは「<フォルダ>/index.html」で作る

## 未決定（決まるまで書かない。決まったらここを更新する）
- 会社猫と NEKOMANEKI の関係
- 6色と九谷五彩の対応、各色の意味、全サイズで上げている手
- 事例の実名掲載の許諾
- 学習用AIクローラーを許可するか（robots.txt）
- お問い合わせフォームに使うサービス（静的サイトのため外部サービスが必要）
