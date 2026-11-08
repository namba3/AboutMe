#!/usr/bin/env python3
"""Render Markdown profiles using metadata in src/site.toml."""
import argparse
from html import escape, unescape
from pathlib import Path
import re
import tomllib

import mistune

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "src" / "site.toml"
SITE_FIELDS = ("brand", "eyebrow", "language_label", "footer", "back_to_top")
PAGE_FIELDS = (
    "source", "output", "lang", "title", "subtitle", "date",
    "toc", "switch", "switch_url", "skip",
)


def load_config(path=CONFIG):
    """Load and validate the site/page definitions from TOML."""
    with path.open("rb") as stream:
        config = tomllib.load(stream)
    site = config.get("site")
    pages = config.get("pages")
    if not isinstance(site, dict):
        raise ValueError(f"{path}: missing [site] metadata")
    if not isinstance(pages, list) or not pages:
        raise ValueError(f"{path}: expected at least one [[pages]] section")

    for field in SITE_FIELDS:
        if not isinstance(site.get(field), str) or not site[field].strip():
            raise ValueError(f"{path}: site.{field} must be a non-empty string")

    outputs = set()
    sources = set()
    languages = set()
    for page in pages:
        if not isinstance(page, dict):
            raise ValueError(f"{path}: each page must be a TOML table")
        for field in PAGE_FIELDS:
            if not isinstance(page.get(field), str) or not page[field].strip():
                raise ValueError(f"{path}: pages.{field} must be a non-empty string")
        for field, suffix in (("source", ".md"), ("output", ".html")):
            name = page[field]
            if Path(name).name != name or not name.endswith(suffix) or name in (".", ".."):
                raise ValueError(f"{path}: pages.{field} must be a simple {suffix} filename")
        if not re.fullmatch(r"[a-z]{2}(?:-[A-Za-z0-9]+)*", page["lang"]):
            raise ValueError(f"{path}: invalid language code: {page['lang']}")
        if page["source"] in sources or page["output"] in outputs or page["lang"] in languages:
            raise ValueError(f"{path}: page sources, outputs and languages must be unique")
        sources.add(page["source"])
        outputs.add(page["output"])
        languages.add(page["lang"])

    for page in pages:
        if page["switch_url"] not in {f"./{name}" for name in outputs}:
            raise ValueError(f"{path}: {page['switch_url']} is not a configured page")
    return site, pages


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
    content = mistune.create_markdown(renderer=renderer, plugins=["table"])("\n".join(lines[1:]))
    if not renderer.sections:
        raise ValueError(f"No section headings in {source}")
    return content, renderer.sections


def render(page, content, sections, site, pages):
    links = "\n".join(
        f'<a href="#{escape(anchor)}">{escape(label)}</a>' for anchor, label in sections
    )
    alternates = "\n".join(
        f'  <link rel="alternate" hreflang="{escape(other["lang"], quote=True)}" '
        f'href="./{escape(other["output"], quote=True)}">'
        for other in pages
    )
    lang = escape(page["lang"], quote=True)
    title = escape(page["title"])
    subtitle = escape(page["subtitle"])
    date = escape(page["date"])
    toc = escape(page["toc"])
    switch = escape(page["switch"])
    switch_url = escape(page["switch_url"], quote=True)
    skip = escape(page["skip"])
    brand = escape(site["brand"])
    eyebrow = escape(site["eyebrow"])
    language_label = escape(site["language_label"], quote=True)
    footer = escape(site["footer"])
    back_to_top = escape(site["back_to_top"])
    home_url = "./" + escape(pages[0]["output"], quote=True)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <meta name="description" content="{subtitle}">
  <title>{title}</title>
  <link rel="stylesheet" href="./assets/style.css">
{alternates}
</head>
<body id="top">
  <a class="skip-link" href="#content">{skip}</a>
  <div class="shell">
    <header class="topbar">
      <a class="brand" href="{home_url}"><span class="brand-mark">N.</span><span>{brand}</span></a>
      <nav class="language" aria-label="{language_label}"><span aria-current="page">{lang.upper()}</span><a href="{switch_url}">{switch}</a></nav>
    </header>
    <div class="layout">
      <aside class="sidebar" aria-label="{toc}">
        <div class="toc-label">{toc}</div>
        <nav class="toc">{links}</nav>
      </aside>
      <main id="content" class="main">
        <header class="hero">
          <div class="eyebrow">{eyebrow}</div>
          <h1>{title}</h1>
          <p class="intro">{subtitle}</p>
          <p class="updated">{date}</p>
        </header>
        <article class="prose">
{content}
        </article>
        <footer><span>{footer}</span><a href="#top">{back_to_top}</a></footer>
      </main>
    </div>
  </div>
</body>
</html>
"""


def build(destination):
    site, pages = load_config()
    output = destination.resolve()
    if output == ROOT:
        raise ValueError("Refusing to build into the repository root")
    (output / "assets").mkdir(parents=True, exist_ok=True)
    (output / "assets" / "style.css").write_text(
        (ROOT / "site" / "style.css").read_text(encoding="utf-8"), encoding="utf-8"
    )
    for page in pages:
        content, sections = convert(ROOT / "src" / page["source"])
        (output / page["output"]).write_text(
            render(page, content, sections, site, pages), encoding="utf-8"
        )
    (output / ".nojekyll").touch()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    build(parser.parse_args().output)
