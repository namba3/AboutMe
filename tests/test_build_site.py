"""Smoke tests for both languages and generated assets."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.build_site import ROOT, build


class SiteTests(unittest.TestCase):
    def test_build_and_navigation(self):
        with TemporaryDirectory() as directory:
            dest = Path(directory) / "site"
            build(dest)
            self.assertTrue((dest / ".nojekyll").exists())
            self.assertTrue((dest / "assets/style.css").stat().st_size > 0)
            for file, lang, target, expected in (
                ("index.html", "ja", "./index_english.html", "学歴・職歴"),
                ("index_english.html", "en", "./index.html", "WORK EXPERIENCE"),
            ):
                html = (dest / file).read_text(encoding="utf-8")
                self.assertIn(f'<html lang="{lang}">', html)
                self.assertIn(target, html)
                self.assertIn(expected, html)
                self.assertIn('<h2 id="section-1">', html)
                self.assertIn('href="#section-1"', html)
                self.assertIn("./assets/style.css", html)
                self.assertNotIn("@import", html)
                self.assertNotIn('class="header"', html)

    def test_normalized_markdown(self):
        for name in ("aboutme.md", "aboutme_english.md"):
            data = (ROOT / "src" / name).read_text(encoding="utf-8")
            self.assertTrue(data.startswith("# ABOUT ME\n"))
            self.assertNotIn('@import "style.less"', data)


if __name__ == "__main__":
    unittest.main()
