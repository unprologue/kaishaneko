# 会社猫サイト 改善計画（作業仕様）

提案書「会社猫 サイト改善提案書」（2026-11-16）から、実装に必要な部分をまとめたもの。

## 1. ブランドの文脈

### 定義文（変えない）
> 会社猫（かいしゃねこ）は、企業のロゴやコーポレートカラーをもとにデザインする、九谷焼の招き猫です。石川県小松市の宮創製陶所が本体をつくり、最後に社員みんなでロゴを貼って完成させます。開業・移転・周年のお祝いや、受付に飾る会社の縁起物として使えます。

### 3つの「なぜ」
- なぜ九谷焼か：360年以上続く、日本を代表する色絵磁器。会社のはじまりを、枯れずに残る本物の工芸で祝う
  - 裏付け：1655年ごろ九谷村で始まり、約100年の中断を経て再興。1975年に国の伝統的工芸品。赤・黄・緑・紫・紺青の「九谷五彩」。小松市の宮創製陶所（創業113年）が花坂陶石で素地をつくる
- なぜ招き猫か：招き猫は「人を招く」縁起物。会社にお客さま、仲間、ご縁を招く
  - 裏付け：左手は人を招き千客万来・商売繁盛、右手は金運とされる。色にも願いがある（黒＝魔除けなど）。ヒーロー写真の会社猫は左手を上げているように見える（全サイズの造形は要確認）
- なぜロゴを貼るのか：だるまの目入れと同じ「願掛けの儀式」。最後の一手をみんなで入れて、その会社だけの縁起物になる
  - 裏付け：だるまは願いを込めて片目を入れ、叶ったらもう片方を入れる。会社猫は「ロゴを貼って完成」

出典：
- 観光庁 多言語解説文「古九谷」 https://www.mlit.go.jp/tagengo-db/common/001653220.pdf
- JR西日本「陶芸の里を巡る 九谷焼」 https://www.westjr.co.jp/company/info/issue/bsignal/24_vol_203/togei/
- All About「招き猫の意味は？」 https://allabout.co.jp/gm/gc/486335/
- ANA「少林山達磨寺」 https://www.ana.co.jp/ja/jp/japan-travel-planner/gunma/0000002.html

### 使った後の5場面
1. 届く：開業・移転・周年の日に、立札と一緒に届く。胡蝶蘭と違い、片付ける日が来ない
2. 貼る：社員が手分けしてロゴを貼る。新しい拠点での「最初の共同作業」が写真と記憶に残る
3. 飾る：受付やエントランスで、来客が最初に目にする「会社の顔」になる
4. 語られる：来客との会話のきっかけになる。採用や広報のSNS、社内報の写真にも登場する
5. 残る：磁器なので何年もそこにいる。周年ごとに一匹ずつ迎える使い方も提案できる

### 2種類の買い手
- 贈る会社：取引先の開業・移転・周年・就任祝い。決め手は「枯れない」「相手の会社らしさ」「立札付き」「請求書払い」。貼り付け済み、S〜M
- 自社で飾る会社：創業・周年・移転・キックオフ・受付。決め手は「社員で貼る体験」「会社の象徴」「記念品」。自分たちで貼る、M〜L、配布用にXS

### 会社名入りのだるま（カイシャダルマ等）との違い
- 産地・素材：だるまは高崎だるま（張り子）。会社猫は九谷焼（磁器）
- 願い：だるまは七転八起・必勝・目標達成。会社猫は人とご縁を招く・商売繁盛
- 時間：だるまは一年の節目に奉納して新しいものを迎える習わし。会社猫は長く飾り続け、会社の歩みと一緒に残る
- 儀式：だるまは目を入れる。会社猫はロゴを貼る

## 2. ページ一覧

| URL | ページ | 役割 | 主な中身 | フェーズ |
| --- | --- | --- | --- | --- |
| / | トップ | ブランドの約束と、全ページへの入口 | 3つのなぜ、使った後に起きること、用途別の入口、事例、料金の要点 | 1 |
| /story/ | 会社猫とは | 「なぜ」を語る | 3つのなぜ、立ち上げの経緯、プロデューサー、NEKOMANEKIとの関係 | 2 |
| /kutani/ | 九谷焼とつくり手 | 産地と本物の裏付け | 九谷焼の歴史と五彩、花坂陶石、宮創製陶所、工程写真、どこまでが九谷焼か | 2 |
| /scenes/opening/ | 開業祝い | 贈る人の入口 | 胡蝶蘭との比較、立札、贈り方、納期の逆算 | 2 |
| /scenes/relocation/ | 移転祝い | 贈る人の入口 | 新オフィスでの飾り方、サイズの選び方 | 3 |
| /scenes/anniversary/ | 周年記念 | 自社用・贈答の入口 | 社員で貼る式典、周年ごとに一匹 | 3 |
| /scenes/reception/ | 受付・エントランス | 自社用の入口 | 置き場所別のサイズ、来客との会話 | 3 |
| /scenes/logo-ceremony/ | ロゴ入れ体験 | 体験の価値を伝える | 進め方、所要時間、写真の撮り方、キックオフでの使い方 | 3 |
| /lineup/ | サイズ・色・仕上げ | 選ぶための情報 | 4サイズ、6色とその意味、上げている手、2つの仕上げ | 2 |
| /order/ | 料金・ご注文 | 迷わず買える | 料金表、注文の流れ、支払い、納期、請求書払い | 2 |
| /works/、/works/<slug>/ | 事例 | 実績と「その後」 | 1社1ページ。背景、デザインの意図、飾った後の声、写真 | 3 |
| /logo-guide/ | ロゴの貼り方 | 購入後の体験 | 6手順と注意点。assets/logo-guide.pdf をHTMLにする | 3 |
| /faq/ | よくある質問 | 不安の解消 | 現行18問に「シールなのに九谷焼？」「耐久性」「飾り方」を追加 | 2 |
| /contact/ | お見積り・ご相談 | 法人の相談窓口 | フォーム（用途・お祝いの日付・数量・予算・贈り先） | 2 |
| /company.html ほか | 会社概要・特商法・プライバシー | 信頼 | 既存URLのまま。OGPと構造化データを追加 | 1 |
| shop.kaishaneko.net | ショップ | 決済 | Shopifyに独自ドメインを設定し、デザインを揃える | 1 |

## 3. トップページの並び順
「何か → なぜ → どうなるか → 自分の場合は → 買い方」の順にする。
1. ヒーロー：「福とご縁を、会社へ。」に、何の商品か（企業ロゴ入りの九谷焼招き猫）を添える
2. 3つのなぜ：九谷焼・招き猫・ロゴ入れ。各カードから /story/ と /kutani/ へ
3. 使った後に起きること：5場面
4. 用途から選ぶ：「贈る」「自社で飾る」の2択から各用途ページへ
5. 事例：写真と、飾った後の一言
6. サイズ・色・仕上げと料金の要点
7. つくり手：宮創製陶所と小松市の工房の写真
8. ご注文の流れ：5ステップ
9. よくある質問：5問だけ載せ、/faq/ へ
10. プロデューサーの想い：短く。続きは /story/ へ
11. 最後の導線：「注文する」と「見積り・相談する」

グローバルナビ：会社猫とは｜九谷焼とつくり手｜用途から選ぶ｜事例｜料金・ご注文｜よくある質問、と「注文」「相談」の2つのボタン。

## 4. title と meta description

ここにある文をそのまま使う。

| URL | title | meta description |
| --- | --- | --- |
| / | 会社猫｜企業ロゴ入りの九谷焼招き猫｜開業・周年の法人ギフト | 会社猫（かいしゃねこ）は、企業のロゴとコーポレートカラーで仕立てる九谷焼の招き猫です。石川県小松市の工房でつくり、最後にみんなでロゴを貼って完成。開業・移転・周年のお祝いに。9,900円から、デザイン料・立札・送料込み。 |
| /story/ | 会社猫とは｜九谷焼・招き猫・ロゴ入れに込めた意味 | なぜ九谷焼で、なぜ招き猫で、なぜ最後にロゴを貼るのか。会社猫に込めた3つの意味と、飾った後に会社で起きること、会社猫が生まれたきっかけを、プロデューサー梶山悠莉彩の紹介とあわせてお伝えします。 |
| /kutani/ | 九谷焼とつくり手｜小松市・宮創製陶所の招き猫｜会社猫 | 会社猫は、創業113年の九谷焼素地メーカー・宮創製陶所（石川県小松市）が、花坂陶石を使い職人の手仕事で仕上げます。360年以上続く九谷焼の歴史と、会社猫ができるまでの工程をご紹介。 |
| /scenes/opening/ | 開業祝いに贈る、企業ロゴ入り九谷焼の招き猫｜会社猫 | 胡蝶蘭の代わりに、枯れずに残る開業祝いを。贈り先のロゴとコーポレートカラーで仕立てる九谷焼の招き猫を、立札付き・貼り付け済みでお届けします。請求書払い可。お祝いの日の2ヶ月前までのご注文がおすすめです。 |
| /scenes/relocation/ | 移転祝いに、新オフィスへ福を招く九谷焼の招き猫｜会社猫 | 移転祝いには、新しいオフィスの受付で来客を迎える一匹を。贈り先のロゴを入れた九谷焼の招き猫を、立札付きでお届けします。置き場所に合わせて、高さ6cmから30cmまでの4サイズから選べます。 |
| /scenes/anniversary/ | 周年記念に、社員みんなでロゴを貼る九谷焼の招き猫｜会社猫 | 創業記念や周年の節目に。九谷焼の招き猫に、社員みんなで願いを込めてロゴを貼って完成させます。式典やキックオフでの体験にも。会社の歩みとともに、ずっと残る記念品です。 |
| /scenes/reception/ | 受付・エントランスに飾る、会社の顔になる招き猫｜会社猫 | 来客が最初に目にする受付に、ロゴとコーポレートカラーで仕立てた九谷焼の招き猫を。受付カウンターには高さ21cm、エントランスには30cmなど、置き場所に合わせて選べます。 |
| /scenes/logo-ceremony/ | ロゴ入れ体験｜社員みんなで仕上げる会社の縁起物｜会社猫 | だるまに目を入れるように、会社猫はロゴを貼って完成します。キックオフや周年式典で、社員が手分けしてロゴを貼る体験の進め方と、きれいに貼るコツをご紹介します。 |
| /lineup/ | サイズ・色・仕上げ｜4サイズ×6色から選ぶ｜会社猫 | 会社猫は高さ6cm（9,900円）から30cm（122,000円）までの4サイズと6色。ロゴは「自分たちで貼る」「貼り付け済み」から選べます。色に込められた意味と、置き場所別の選び方もご案内します。 |
| /order/ | 料金・ご注文の流れ｜9,900円から・送料込み｜会社猫 | 会社猫の料金は9,900円（税込）から。デザイン料・立札・国内送料込みで、追加料金はありません。納期はご注文から2ヶ月以内。クレジットカード、銀行振込、法人向けの請求書払いに対応しています。 |
| /works/ | お届けした会社猫｜企業ロゴ入り招き猫の制作事例｜会社猫 | お届けした会社猫の制作事例です。ロゴやコーポレートカラーをどうデザインに落とし込んだか、どこに飾られ、どんな声をいただいたかを、写真とあわせてご紹介します。 |
| /works/seikan/ | 精管工業さまの会社猫｜歯車と配線をあしらったブルーの招き猫 | 精管工業有限会社さまのお祝いに、ブルーの会社猫を制作しました。ロゴの歯車と配線のモチーフを、正面だけでなく側面と背面にも展開しています。デザインの考え方と、お届けまでの流れをご紹介します。 |
| /logo-guide/ | ロゴの貼り方｜会社猫を6ステップで仕上げる | 会社猫に同梱のロゴシールを、きれいに貼るための6ステップ。貼る面の拭き方から、透明フィルムのはがし方、貼った後の注意点まで、写真付きで説明します。同梱の説明書（PDF）もご覧いただけます。 |
| /faq/ | よくある質問｜納期・支払い・ロゴデータ・請求書払い｜会社猫 | 会社猫のよくある質問。納期（ご注文から2ヶ月以内）、支払い方法、請求書払い、インボイス、ロゴデータの形式、修正回数、破損時の対応、海外発送などにお答えします。 |
| /contact/ | お見積り・ご相談｜法人のまとめ注文・お急ぎ便｜会社猫 | 会社猫のお見積り・ご相談の窓口です。用途、お祝いの日付、数量、ご予算をお知らせください。複数注文、ノベルティ、海外発送、お急ぎのご相談も承ります。運営：UNPROLOGUE株式会社 |
| /company.html | 会社概要｜会社猫 | 会社猫を運営するUNPROLOGUE株式会社（東京都渋谷区）の会社概要です。所在地・設立・事業内容・連絡先と、九谷焼の製造パートナーである宮創製陶所株式会社（石川県小松市）をご案内します。 |

特商法とプライバシーポリシーは現行のまま。事例の各社ページは「{社名}さまの会社猫｜{デザインの特徴}の{色}の招き猫」の型で作る。

## 5. OGP画像
- 1200×630px、JPEG、1MB未満。ページごとに別ファイル（例：/ogp/opening.jpg）。差し替えるときはファイル名を変える
- 左に見出し（20字以内・明朝・64px以上）と補足「企業ロゴ入りの九谷焼招き猫」、九谷五彩の細い帯、左下に会社猫のロゴ。右に写真
- 上下左右に60px以上の余白
- 猫に貼るロゴは「YOUR LOGO」の見本か、掲載許諾を得た実例だけ
- 全ページに og:image、og:image:width、og:image:height、og:image:alt

| URL | 写真 | 見出し |
| --- | --- | --- |
| / | 受付に飾られた会社猫（YOUR LOGO） | 福とご縁を、会社へ。 |
| /story/ | ロゴを貼る手元 | 会社のための、世界にひとつの縁起物 |
| /kutani/ | 工房の石膏型と職人の手 | 創業113年の九谷焼の工房から |
| /scenes/opening/ | 「御祝」の立札と並ぶ会社猫 | 開業祝いに、枯れない招き猫を |
| /scenes/relocation/ | 新しいオフィスの受付 | 新しいオフィスに、福を招く一匹 |
| /scenes/anniversary/ | 社員が囲んでロゴを貼る場面 | 周年の節目を、かたちに残す |
| /scenes/reception/ | エントランスのLサイズ | 来客を迎える、会社の顔 |
| /scenes/logo-ceremony/ | ロゴを貼る手元のアップ | だるまに目を入れるように |
| /lineup/ | 6色・4サイズの並び | 4サイズ×6色から選べる |
| /order/ | 商品写真＋価格 | 9,900円から。送料・デザイン料込み |
| /works/<slug>/ | その会社の会社猫 | {社名}さまの会社猫 |
| その他 | 共通画像 | ページ名のみ |

## 6. デザインの方針
- 今の「生成り色の背景、墨色、明朝体」の上品さは残す
- 九谷五彩（赤・黄・緑・紫・紺青）を差し色に少量使う（区切り線、アイコン、6色の色見本）
- 写真は「商品単体」「使う場面」「つくる工房」の3種類をそろえる
- 「3つのなぜ」と「5つの場面」はアイコン付きの図にする
- 各セクションの最初に「結論の1文」を置く
- スマホでは画面下に「注文」「相談」を固定する
- 画像はWebPなどにして、画面幅ごとに出し分ける

## 7. AI検索について守ること
- AIの回答に効くのは、主に本文と、クロールされる状態かどうか。AI向けの特別な書き方は要らない
- robots.txt では、検索用の OAI-SearchBot、Claude-SearchBot、PerplexityBot を許可する
- 構造化データは、ページに表示している内容と一致させる
- FAQのリッチリザルトはGoogleが2026年に終了した。FAQPage のマークアップは残してよい

## 8. フェーズ1（今回の作業）
1. robots.txt と sitemap.xml を追加する（9章）
2. トップの title・meta description・H1 を差し替える（4章と9章）
3. トップのOGPに og:image:alt を足す。新しいOGP画像ができるまで、画像は今の ogp.jpg のまま
4. 会社概要・特商法・プライバシーの3ページに OGP 一式を足す
5. トップの構造化データの Product と Organization を、9章の形に置き換える。FAQPage はそのまま。Offer の url は /order/ ができるまで https://kaishaneko.net/#pricing のままにする
6. alt が空の画像（ヒーロー画像、貼り方の手順写真6枚）に alt を付ける
7. 「架空のもの」という注記の対象をはっきりさせる文案を出す（実装は確認後）
8. ブランドに合わせた 404.html を作る

## 9. 付録コード

### トップの head

    <title>会社猫｜企業ロゴ入りの九谷焼招き猫｜開業・周年の法人ギフト</title>
    <meta name="description" content="会社猫（かいしゃねこ）は、企業のロゴとコーポレートカラーで仕立てる九谷焼の招き猫です。石川県小松市の工房でつくり、最後にみんなでロゴを貼って完成。開業・移転・周年のお祝いに。9,900円から、デザイン料・立札・送料込み。">
    <link rel="canonical" href="https://kaishaneko.net/">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="会社猫">
    <meta property="og:locale" content="ja_JP">
    <meta property="og:url" content="https://kaishaneko.net/">
    <meta property="og:title" content="会社猫｜企業ロゴ入りの九谷焼招き猫｜開業・周年の法人ギフト">
    <meta property="og:description" content="会社猫（かいしゃねこ）は、企業のロゴとコーポレートカラーで仕立てる九谷焼の招き猫です。石川県小松市の工房でつくり、最後にみんなでロゴを貼って完成。開業・移転・周年のお祝いに。9,900円から、デザイン料・立札・送料込み。">
    <meta property="og:image" content="https://kaishaneko.net/ogp/top-v2.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="受付に飾られた、企業ロゴ入りの九谷焼の招き猫「会社猫」">
    <meta name="twitter:card" content="summary_large_image">

### トップの H1

    <h1>
      <span class="catch">福とご縁を、会社へ。</span>
      <span class="sub">企業ロゴ入りの九谷焼招き猫「会社猫」</span>
    </h1>

### トップの構造化データ（Product と Organization をこれに置き換える。FAQPage はそのまま）

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "WebSite",
          "@id": "https://kaishaneko.net/#website",
          "url": "https://kaishaneko.net/",
          "name": "会社猫",
          "alternateName": ["かいしゃねこ", "KAISHA NEKO"],
          "inLanguage": "ja",
          "publisher": { "@id": "https://kaishaneko.net/#org" }
        },
        {
          "@type": "Organization",
          "@id": "https://kaishaneko.net/#org",
          "name": "UNPROLOGUE株式会社",
          "url": "https://unprologue.jp/",
          "email": "hello@unprologue.jp",
          "founder": { "@type": "Person", "name": "梶山 悠莉彩" },
          "address": {
            "@type": "PostalAddress",
            "postalCode": "150-0021",
            "addressRegion": "東京都",
            "addressLocality": "渋谷区",
            "streetAddress": "恵比寿西二丁目8番4号 EX恵比寿西ビル5階",
            "addressCountry": "JP"
          }
        },
        {
          "@type": "Organization",
          "@id": "https://kaishaneko.net/#maker",
          "name": "宮創製陶所株式会社",
          "address": {
            "@type": "PostalAddress",
            "addressRegion": "石川県",
            "addressLocality": "小松市",
            "addressCountry": "JP"
          }
        },
        {
          "@type": "Product",
          "@id": "https://kaishaneko.net/#product",
          "name": "会社猫（企業ロゴ入り 九谷焼の招き猫）",
          "description": "会社猫（かいしゃねこ）は、企業のロゴやコーポレートカラーをもとにデザインする、九谷焼の招き猫です。石川県小松市の宮創製陶所が本体をつくり、最後に社員みんなでロゴを貼って完成させます。",
          "image": [
            "https://kaishaneko.net/assets/colors/black.webp",
            "https://kaishaneko.net/assets/colors/blue.webp",
            "https://kaishaneko.net/assets/colors/red.webp"
          ],
          "brand": {
            "@type": "Brand",
            "name": "会社猫",
            "logo": "https://kaishaneko.net/assets/logo-horizontal.png",
            "sameAs": ["https://www.instagram.com/kaishaneko22/"]
          },
          "manufacturer": { "@id": "https://kaishaneko.net/#maker" },
          "material": "磁器（九谷焼）",
          "countryOfOrigin": { "@type": "Country", "name": "日本" },
          "offers": [
            { "@type": "Offer", "name": "XS（高さ6cm）", "price": "9900", "priceCurrency": "JPY", "availability": "https://schema.org/InStock", "url": "https://kaishaneko.net/order/", "seller": { "@id": "https://kaishaneko.net/#org" } },
            { "@type": "Offer", "name": "S（高さ15cm）", "price": "55500", "priceCurrency": "JPY", "availability": "https://schema.org/InStock", "url": "https://kaishaneko.net/order/", "seller": { "@id": "https://kaishaneko.net/#org" } },
            { "@type": "Offer", "name": "M（高さ21cm）", "price": "88000", "priceCurrency": "JPY", "availability": "https://schema.org/InStock", "url": "https://kaishaneko.net/order/", "seller": { "@id": "https://kaishaneko.net/#org" } },
            { "@type": "Offer", "name": "L（高さ30cm）", "price": "122000", "priceCurrency": "JPY", "availability": "https://schema.org/InStock", "url": "https://kaishaneko.net/order/", "seller": { "@id": "https://kaishaneko.net/#org" } }
          ]
        }
      ]
    }
    </script>

### 下層ページのパンくず（例：/kutani/）

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "会社猫", "item": "https://kaishaneko.net/" },
        { "@type": "ListItem", "position": 2, "name": "九谷焼とつくり手", "item": "https://kaishaneko.net/kutani/" }
      ]
    }
    </script>

### robots.txt

    # 会社猫 robots.txt
    User-agent: *
    Allow: /

    # AI検索（回答での引用）用のクローラーは明示的に許可
    User-agent: OAI-SearchBot
    Allow: /

    User-agent: Claude-SearchBot
    Allow: /

    User-agent: PerplexityBot
    Allow: /

    # 学習用クローラーを止める場合は、下の行の先頭の # を外す
    # User-agent: GPTBot
    # Disallow: /
    # User-agent: ClaudeBot
    # Disallow: /
    # User-agent: Google-Extended
    # Disallow: /

    Sitemap: https://kaishaneko.net/sitemap.xml

### sitemap.xml（今ある4ページ。ページを足したら追記する）

    <?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url><loc>https://kaishaneko.net/</loc></url>
      <url><loc>https://kaishaneko.net/company.html</loc></url>
      <url><loc>https://kaishaneko.net/legal/tokushoho.html</loc></url>
      <url><loc>https://kaishaneko.net/legal/privacy.html</loc></url>
    </urlset>

## 10. このあとの進め方

### 進み具合（2026-11-16 時点）
- 公開済み：フェーズ1の全項目、/contact/（メール。フォームはサービスが決まってから）、/story/、/kutani/、/order/、/faq/、/logo-guide/、/scenes/opening/、/scenes/relocation/、/scenes/anniversary/、/scenes/reception/、トップの並び替え、ページごとのOGP画像（/ogp/）
- 材料待ち：/lineup/（6色の意味・上げている手）、/scenes/logo-ceremony/（所要時間など）、/works/（掲載許諾）、FAQ追加3問（耐久性・飾り方・シールでも九谷焼か）、用途別ページの直送・立札の文字・のし、/kutani/ の焼成・色付けの工程

### フェーズ1の続き
- Shopify の独自ドメインが使えるようになったら：サイト内の mp1vnh-e3.myshopify.com へのリンクを、https://shop.kaishaneko.net に差し替える
- 新しいOGP画像を ogp/ に置いたら：各ページの og:image と og:image:alt を5章に合わせて差し替える

### フェーズ2（1〜2か月）
- /new-page /kutani/（工房の写真がそろってから）
- /new-page /story/
- /new-page /lineup/（6色の意味と上げている手が決まってから）
- /new-page /order/（できたら、構造化データの Offer の url を /order/ に変える）
- トップを3章の並び順に組み替える。新しく必要な文は、先に案を見せる
- /new-page /faq/（トップのよくある質問は5問だけにして、/faq/ へリンクする）
- /new-page /contact/（フォームのサービスが決まってから）
- /new-page /scenes/opening/

### フェーズ3（3か月目以降）
- /add-case 会社名 slug（掲載許諾をもらってから）
- /new-page /scenes/relocation/、/new-page /scenes/anniversary/、/new-page /scenes/reception/、/new-page /scenes/logo-ceremony/
- /new-page /logo-guide/
- 月に1回 /seo-check

### Claude Code の外でやること（オーナー）
- 公開後、Google Search Console に登録し、sitemap.xml を送信する
- Shopify で shop.kaishaneko.net を接続し、ドメイン管理会社で DNS を設定する
- Shopify の Google & YouTube アプリで Merchant Center に連携する
- OGP画像を作る
- 工房での写真撮影、事例の掲載許諾
- CLAUDE.md の「未決定」を決めて更新する
- Instagram と Shopify の紹介文を定義文にそろえる
