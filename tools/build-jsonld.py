"""Regenerate the JSON-LD (Product + FAQPage) in index.html from the page itself.

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
product = {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "会社猫",
    "description": "九谷焼の招き猫に、最後はみんなの手で願いを込めてロゴを貼る。会社のための、世界にひとつの縁起物。",
    "image": "https://kaishaneko.net/images/processed/ogp.jpg",
    "brand": {"@type": "Brand", "name": "会社猫"},
    "offers": [
        {"@type": "Offer", "name": f"{size}（高さ{cm}cm）", "price": price.replace(",", ""), "priceCurrency": "JPY",
         "availability": "https://schema.org/InStock", "url": "https://kaishaneko.net/#pricing"}
        for size, cm, price in prices
    ],
}
faq_page = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq}
organization = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "UNPROLOGUE株式会社",
    "url": "https://unprologue.jp/",
    "email": "hello@unprologue.jp",
    "address": {
        "@type": "PostalAddress",
        "postalCode": "150-0021",
        "addressRegion": "東京都",
        "addressLocality": "渋谷区",
        "streetAddress": "恵比寿西二丁目8番4号 EX恵比寿西ビル5階",
        "addressCountry": "JP",
    },
}

block = (START + "\n"
         + '    <script type="application/ld+json">\n' + json.dumps(product, ensure_ascii=False, indent=2) + "\n    </script>\n"
         + '    <script type="application/ld+json">\n' + json.dumps(faq_page, ensure_ascii=False, indent=2) + "\n    </script>\n"
         + '    <script type="application/ld+json">\n' + json.dumps(organization, ensure_ascii=False, indent=2) + "\n    </script>\n"
         + "    " + END)
if START in page:
    page = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, page, flags=re.S)
else:
    page = page.replace("  </head>", "    " + block + "\n  </head>", 1)
open(PATH, "w", encoding="utf-8").write(page)
print(f"Product offers: {len(product['offers'])}, FAQ entries: {len(faq)}")
