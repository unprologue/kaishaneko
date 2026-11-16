"""Regenerate the JSON-LD (WebSite / Organization / Product graph + FAQPage) in index.html from the page itself.

FAQ entries come from the <details class="faq-item"> blocks. Answers that still contain
a "[...]" placeholder are left out so unconfirmed text never reaches search results.
Run after editing the FAQ or prices: python3 tools/build-jsonld.py
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "index.html")
START, END = "<!-- jsonld:start -->", "<!-- jsonld:end -->"


def text(fragment):
    t = re.sub(r"<[^>]+>", "", fragment)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


page = open(PATH, encoding="utf-8").read()

faq = []
for q, a in re.findall(r'<details class="faq-item"[^>]*>\s*<summary[^>]*>(.*?)<span class="faq-icon".*?<div class="faq-answer">(.*?)</div>', page, re.S):
    q, a = text(q), text(a)
    q = re.sub(r"^Q\.\s*", "", q)
    a = re.sub(r"^A\.\s*", "", a)
    if re.search(r"\[[^\]]+\]", a):  # unfilled placeholder
        continue
    faq.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})

prices = re.findall(r'<tr><th scope="row">(XS|S|M|L)</th><td>(\d+)cm</td><td class="num">([\d,]+)円</td>', page)
SITE = "https://kaishaneko.net/"
# Offer url stays on #pricing until /order/ exists (docs/site-plan.md 8章)
OFFER_URL = SITE + "#pricing"
graph = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "WebSite",
            "@id": SITE + "#website",
            "url": SITE,
            "name": "会社猫",
            "alternateName": ["かいしゃねこ", "KAISHA NEKO"],
            "inLanguage": "ja",
            "publisher": {"@id": SITE + "#org"},
        },
        {
            "@type": "Organization",
            "@id": SITE + "#org",
            "name": "UNPROLOGUE株式会社",
            "url": "https://unprologue.jp/",
            "email": "hello@unprologue.jp",
            "founder": {"@type": "Person", "name": "梶山 悠莉彩"},
            "address": {
                "@type": "PostalAddress",
                "postalCode": "150-0021",
                "addressRegion": "東京都",
                "addressLocality": "渋谷区",
                "streetAddress": "恵比寿西二丁目8番4号 EX恵比寿西ビル5階",
                "addressCountry": "JP",
            },
        },
        {
            "@type": "Organization",
            "@id": SITE + "#maker",
            "name": "宮創製陶所株式会社",
            "address": {
                "@type": "PostalAddress",
                "addressRegion": "石川県",
                "addressLocality": "小松市",
                "addressCountry": "JP",
            },
        },
        {
            "@type": "Product",
            "@id": SITE + "#product",
            "name": "会社猫（企業ロゴ入り 九谷焼の招き猫）",
            "description": "会社猫（かいしゃねこ）は、企業のロゴやコーポレートカラーをもとにデザインする、九谷焼の招き猫です。石川県小松市の宮創製陶所が本体をつくり、最後に社員みんなでロゴを貼って完成させます。",
            "image": [
                SITE + "assets/colors/black.webp",
                SITE + "assets/colors/blue.webp",
                SITE + "assets/colors/red.webp",
            ],
            "brand": {
                "@type": "Brand",
                "name": "会社猫",
                "logo": SITE + "assets/logo-horizontal.png",
                "sameAs": ["https://www.instagram.com/kaishaneko22/"],
            },
            "manufacturer": {"@id": SITE + "#maker"},
            "material": "磁器（九谷焼）",
            "countryOfOrigin": {"@type": "Country", "name": "日本"},
            "offers": [
                {"@type": "Offer", "name": f"{size}（高さ{cm}cm）", "price": price.replace(",", ""), "priceCurrency": "JPY",
                 "availability": "https://schema.org/InStock", "url": OFFER_URL, "seller": {"@id": SITE + "#org"}}
                for size, cm, price in prices
            ],
        },
    ],
}
faq_page = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq}

block = (START + "\n"
         + '    <script type="application/ld+json">\n' + json.dumps(graph, ensure_ascii=False, indent=2) + "\n    </script>\n"
         + '    <script type="application/ld+json">\n' + json.dumps(faq_page, ensure_ascii=False, indent=2) + "\n    </script>\n"
         + "    " + END)
if START in page:
    page = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, page, flags=re.S)
else:
    page = page.replace("  </head>", "    " + block + "\n  </head>", 1)
open(PATH, "w", encoding="utf-8").write(page)
print(f"Product offers: {len(graph['@graph'][3]['offers'])}, FAQ entries: {len(faq)}")
