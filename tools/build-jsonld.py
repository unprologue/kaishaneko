"""Regenerate the JSON-LD in index.html and faq/index.html from the pages themselves.

index.html : WebSite / Organization / Product graph + FAQPage (the questions shown on the top page)
faq/index.html : FAQPage (all questions shown on /faq/)

FAQ entries come from the <details class="faq-item"> blocks, so the markup always matches what
is displayed. Answers that still contain a "[...]" placeholder are left out so unconfirmed text
never reaches search results.
Run after editing the FAQ or prices: python3 tools/build-jsonld.py
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "index.html")
FAQ_PATH = os.path.join(ROOT, "faq", "index.html")
START, END = "<!-- jsonld:start -->", "<!-- jsonld:end -->"


def text(fragment):
    t = re.sub(r"<[^>]+>", "", fragment)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def faq_entries(src):
    out = []
    for q, a in re.findall(r'<details class="faq-item"[^>]*>\s*<summary[^>]*>(.*?)<span class="faq-icon".*?<div class="faq-answer">(.*?)</div>', src, re.S):
        q, a = text(q), text(a)
        q = re.sub(r"^Q\.\s*", "", q)
        a = re.sub(r"^A\.\s*", "", a)
        if re.search(r"\[[^\]]+\]", a):  # unfilled placeholder
            continue
        out.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    return out


def write_block(path, src, objects):
    block = (START + "\n"
             + "".join('    <script type="application/ld+json">\n' + json.dumps(o, ensure_ascii=False, indent=2) + "\n    </script>\n" for o in objects)
             + "    " + END)
    if START in src:
        src = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, src, flags=re.S)
    else:
        src = src.replace("  </head>", "    " + block + "\n  </head>", 1)
    open(path, "w", encoding="utf-8").write(src)


page = open(PATH, encoding="utf-8").read()
faq = faq_entries(page)

prices = re.findall(r'<tr><th scope="row">(XS|S|M|L)</th><td>(\d+)cm</td><td class="num">([\d,]+)円</td>', page)
SITE = "https://kaishaneko.net/"
# Offer url points at the order page, which shows the same price table (docs/site-plan.md 10章)
OFFER_URL = SITE + "order/"
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

write_block(PATH, page, [graph, faq_page])

faq_src = open(FAQ_PATH, encoding="utf-8").read()
faq_all = faq_entries(faq_src)
write_block(FAQ_PATH, faq_src, [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_all}])
print(f"Product offers: {len(graph['@graph'][3]['offers'])}, FAQ entries: top {len(faq)}, /faq/ {len(faq_all)}")
