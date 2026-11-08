"""Regression tests for the TOML-driven bilingual site generator."""
from html import escape
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.build_site import CONFIG, ROOT, build, load_config, render, convert


class SiteTests(unittest.TestCase):
    def test_build_and_navigation(self):
        site, pages = load_config()
        self.assertEqual({page["source"] for page in pages}, {"aboutme.md", "aboutme.en.md"})
        self.assertEqual({page["output"] for page in pages}, {"index.html", "index.en.html"})
        with TemporaryDirectory() as directory:
            dest = Path(directory) / "site"
            build(dest)
            self.assertTrue((dest / ".nojekyll").exists())
            self.assertTrue((dest / "assets/style.css").stat().st_size > 0)
            self.assertFalse((dest / "index_english.html").exists())
            for page in pages:
                html = (dest / page["output"]).read_text(encoding="utf-8")
                self.assertIn(f'<html lang="{page["lang"]}">', html)
                self.assertIn(f'<title>{escape(page["title"])}</title>', html)
                self.assertIn(f'<p class="updated">{escape(page["date"])}</p>', html)
                self.assertIn(f'<p class="intro">{escape(page["subtitle"])}</p>', html)
                self.assertIn(f'href="{page["switch_url"]}"', html)
                self.assertIn(escape(site["brand"]), html)
                self.assertIn('<h2 id="section-1">', html)
                self.assertIn('href="#section-1"', html)
                self.assertIn("./assets/style.css", html)
                self.assertNotIn("index_english.html", html)
                self.assertNotIn("@import", html)
                self.assertNotIn('class="header"', html)
            self.assertIn("学歴・職歴", (dest / "index.html").read_text(encoding="utf-8"))
            english_html = (dest / "index.en.html").read_text(encoding="utf-8")
            for expected in ("Kakaku.com", "November 2022", "gRPC", "MTConnect",
                             "Fixstars", "10–100 GB", "WORK EXPERIENCE"):
                self.assertIn(expected, english_html)

    def test_english_matches_japanese_structure(self):
        _, ja_sections = convert(ROOT / "src/aboutme.md")
        _, en_sections = convert(ROOT / "src/aboutme.en.md")
        self.assertEqual(len(ja_sections), len(en_sections))
        self.assertEqual(
            [title for _, title in en_sections],
            ["SUMMARY", "EDUCATION AND EMPLOYMENT", "SKILLS HIGHLIGHTS",
             "WORK EXPERIENCE", "LANGUAGES", "OTHER", "PERSONAL STATEMENT"],
        )
        ja_content = (ROOT / "src/aboutme.md").read_text(encoding="utf-8")
        en_content = (ROOT / "src/aboutme.en.md").read_text(encoding="utf-8")
        self.assertEqual(ja_content.count("#### プロジェクト："), en_content.count("#### Project:"))
        for topic in ("Hammock Corporation", "Fixstars Corporation",
                      "Core Concept Technologies", "Kakaku.com"):
            self.assertIn(topic, en_content)

    def test_normalized_markdown(self):
        self.assertFalse((ROOT / "src/aboutme_english.md").exists())
        for name in ("aboutme.md", "aboutme.en.md"):
            data = (ROOT / "src" / name).read_text(encoding="utf-8")
            self.assertTrue(data.startswith("# ABOUT ME\n"))
            self.assertNotIn('@import "style.less"', data)

    def test_config_validation(self):
        self.assertTrue(CONFIG.exists())
        with TemporaryDirectory() as directory:
            invalid = Path(directory) / "site.toml"
            invalid.write_text('[site]\nbrand = "Only brand"\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "pages"):
                load_config(invalid)

    def test_metadata_change_updates_html(self):
        site, pages = load_config()
        customized = dict(pages[0], title="Custom page title", date="2027-01-01")
        html = render(customized, "<p>Example</p>", [("section-1", "Example")], site, pages)
        self.assertIn("<title>Custom page title</title>", html)
        self.assertIn('<p class="updated">2027-01-01</p>', html)


if __name__ == "__main__":
    unittest.main()
