---
name: new-page
description: 会社猫サイトに新しいページを1つ追加する。docs/site-plan.md のページ一覧・title／description・OGP画像の案に沿って作る。
argument-hint: "[URL 例: /kutani/]"
disable-model-invocation: true
---

新しいページ $ARGUMENTS を追加します。

## 手順
1. docs/site-plan.md を読み、$ARGUMENTS について次を確認する
   - 2章：役割と主な中身
   - 4章：title と description
   - 5章：OGP画像の写真と見出し
2. 作るファイル、変更するファイル、本文の見出し構成（各節の要点つき）を一覧にして出す。私のOKを待つ
3. 既存の index.html のヘッダー・フッター・CSSを流用して、$ARGUMENTS の index.html を作る
4. head には CLAUDE.md の「各ページの必須項目」をすべて入れる。title と description は site-plan.md の文をそのまま使う
5. 本文は「主な中身」に沿って書く。事実が足りない箇所は推測で埋めず、<!-- TODO: 確認 --> を残す
6. BreadcrumbList の構造化データを入れる
7. sitemap.xml に追加し、グローバルナビか関係するページからリンクする
8. OGP画像が無ければ、/ogp/ のファイル名だけ決めて TODO として報告する
9. .claude/skills/seo-check/SKILL.md の基準でこのページを点検する

## 最後に報告すること
- 変更したファイルの一覧
- 新しく書いた文（私が確認するため）
- 残った TODO
