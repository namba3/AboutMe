#!/usr/bin/env python3
"""Render the bilingual Markdown profile into a static GitHub Pages site."""
import argparse
from html import escape, unescape
from pathlib import Path
import re

import mistune

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    dict(source="aboutme.md", output="index.html", lang="ja", title="技術プロフィール",
         subtitle="ソフトウェア設計・開発の経験と技術的な取り組み", date="2022年8月12日時点の記録",
         toc="目次", switch="English", switch_url="./index_english.html", skip="本文へ移動"),
    dict(source="aboutme_english.md", output="index_english.html", lang="en",
         title="Engineering Profile", subtitle="Software engineering experience and projects",
         date="Originally documented August 12, 2022", toc="Contents",
         switch="日本語", switch_url="./index.html", skip="Skip to content"),
]


class OutlineRenderer(mistune.HTMLRenderer):
    def __init__(self):
        super().__init__(escape=False)
        self.sections = []

    def heading(self, text, level, **attrs):
        if level == 2:
            anchor = "section-" + str(len(self.sections) + 1)
            label = unescape(re.sub(r"<[^>]+>", "", text))
            self.sections.append((anchor, label))
            return f'<h2 id="{anchor}">{text}</h2>\n'
        return f"<h{level}>{text}</h{level}>\n"


def convert(source):
    lines = source.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "# ABOUT ME":
        raise ValueError(f"Unexpected Markdown header: {source}")
    if any(line.lstrip().startswith("@import") for line in lines):
        raise ValueError(f"Legacy Markdown Preview Enhanced directive in {source}")
    renderer = OutlineRenderer()
    text = mistune.create_markdown(renderer=renderer, plugins=["table"])("\n".join(lines[1:]))
    if not renderer.sections:
        raise ValueError(f"No section headings in {source}")
    return text, renderer.sections


def render(page, content, sections):
    links = "\n".join(
        f'<a href="#{escape(anchor)}">{escape(label)}</a>' for anchor, label in sections
    )
    lang = escape(page["lang"])
    title = escape(page["title"])
    subtitle = escape(page["subtitle"])
    date = escape(page["date"])
    toc = escape(page["toc"])
    switch = escape(page["switch"])
    switch_url = escape(page["switch_url"], quote=True)
    skip = escape(page["skip"])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <meta name="description" content="{subtitle}">
  <title>{title}</title>
  <link rel="stylesheet" href="./assets/style.css">
  <link rel="alternate" hreflang="ja" href="./index.html">
  <link rel="alternate" hreflang="en" href="./index_english.html">
</head>
<body id="top">
  <a class="skip-link" href="#content">{skip}</a>
  <div class="shell">
    <header class="topbar">
      <a class="brand" href="./index.html"><span class="brand-mark">N.</span><span>Engineering / Profile</span></a>
      <nav class="language" aria-label="Language"><span aria-current="page">{lang.upper()}</span><a href="{switch_url}">{switch}</a></nav>
    </header>
    <div class="layout">
      <aside class="sidebar" aria-label="{toc}">
        <div class="toc-label">{toc}</div>
        <nav class="toc">{links}</nav>
      </aside>
      <main id="content" class="main">
        <header class="hero">
          <div class="eyebrow">PORTFOLIO / ENGINEERING</div>
          <h1>{title}</h1>
          <p class="intro">{subtitle}</p>
          <p class="updated">{date}</p>
        </header>
        <article class="prose">
{content}
        </article>
        <footer><span>Built from Markdown · GitHub Pages</span><a href="#top">↑ Top</a></footer>
      </main>
    </div>
  </div>
</body>
</html>
"""


def build(destination):
    output = destination.resolve()
    if output == ROOT:
        raise ValueError("Refusing to build into the repository root")
    (output / "assets").mkdir(parents=True, exist_ok=True)
    (output / "assets" / "style.css").write_text(
        (ROOT / "site" / "style.css").read_text(encoding="utf-8"), encoding="utf-8"
    )
    for page in PAGES:
        content, sections = convert(ROOT / "src" / page["source"])
        (output / page["output"]).write_text(render(page, content, sections), encoding="utf-8")
    (output / ".nojekyll").touch()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    build(parser.parse_args().output)
