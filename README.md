# AboutMe

ソフトウェアエンジニアとしての職歴、開発経験、技術スキルを掲載する個人プロフィールサイトです。日本語・英語の2言語に対応し、MarkdownをHTMLに変換して公開しています。

- [日本語版](https://namba3.github.io/AboutMe/)
- [英語版](https://namba3.github.io/AboutMe/index.en.html)

## ファイル構成

| ファイル | 用途 |
| --- | --- |
| `src/aboutme.md` | 日本語の本文 |
| `src/aboutme.en.md` | 英語の本文 |
| `src/site.toml` | 各ページのタイトル、表示日付、生成ファイル名、言語切替など |
| `site/style.css` | 共通のレイアウト・デザイン |
| `scripts/build_site.py` | MarkdownからHTMLへの変換処理 |
| `tests/test_build_site.py` | 生成ページと設定の検証 |

## 編集方法

本文を変更する場合は該当言語のMarkdownファイルを編集します。タイトル、サブタイトル、表示日付、出力ファイル名などは `src/site.toml` の `[[pages]]` で管理します。サイト共通の表示文言は同ファイルの `[site]` に定義しています。

生成したHTMLはGitで管理せず、ビルド時に `dist/` に出力します。

## ローカルでの確認

Python 3.12以降を使用します。

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/build_site.py --output dist
```

生成した `dist/index.html` または `dist/index.en.html` をブラウザで開いて確認できます。
