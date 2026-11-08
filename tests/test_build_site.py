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
             "WORK EXPERIENCE", "LANGUAGES", "PERSONAL STATEMENT", "OTHER"],
        )
        ja_content = (ROOT / "src/aboutme.md").read_text(encoding="utf-8")
        en_content = (ROOT / "src/aboutme.en.md").read_text(encoding="utf-8")
        self.assertEqual(ja_content.count("#### プロジェクト："), en_content.count("#### Project:"))
        for topic in ("Hammock Corporation", "Fixstars Corporation",
                      "Core Concept Technologies", "Kakaku.com"):
            self.assertIn(topic, en_content)


    def test_summary_and_final_sections(self):
        """The two languages use a three-paragraph summary and matching order."""
        cases = (
            ("aboutme.md",
             ["概要", "学歴・職歴", "スキルハイライト", "職歴",
              "語学", "自己 PR", "その他"],
             ("産業IoT", "3Dモデルビューワー", "Rust", "API境界",
              "企画・デザイン", "個人開発")),
            ("aboutme.en.md",
             ["SUMMARY", "EDUCATION AND EMPLOYMENT", "SKILLS HIGHLIGHTS",
              "WORK EXPERIENCE", "LANGUAGES", "PERSONAL STATEMENT", "OTHER"],
             ("industrial IoT", "3D model viewers", "Rust", "API boundary",
              "product planners", "personal projects")),
        )
        for filename, expected_titles, terms in cases:
            with self.subTest(source=filename):
                markdown = (ROOT / "src" / filename).read_text(encoding="utf-8")
                sections = [line[3:] for line in markdown.splitlines()
                            if line.startswith("## ")]
                self.assertEqual(sections, expected_titles)
                intro = markdown.split("## " + sections[0] + "\n", 1)[1].split(
                    "## " + sections[1] + "\n", 1)[0].strip()
                self.assertEqual(len(intro.split("\n\n")), 3)
                for term in terms:
                    self.assertIn(term, intro)
                self.assertNotIn("IoT 関連の 3 年間", intro)
                self.assertNotIn("More than four years", intro)
                self.assertIn("## " + sections[-2] + "\n", markdown)
                self.assertIn("## " + sections[-1] + "\n", markdown)

    def test_skill_highlights_are_four_tables(self):
        """Bilingual skill sections are concise and free of per-language headings."""
        cases = (
            ("aboutme.md", "## スキルハイライト", "## 職歴",
             ("プログラミング言語", "設計・アーキテクチャ",
              "クラウドインフラ", "ツール・開発環境"),
             ("C#", "Rust", "Python", "Go", "C", "C++",
              "TypeScript / JavaScript"),
             ("API設計", "疎結合・変更容易性", "性能最適化")),
            ("aboutme.en.md", "## SKILLS HIGHLIGHTS", "## WORK EXPERIENCE",
             ("Programming Languages", "Software Design and Architecture",
              "Cloud Infrastructure", "Tools and Development Environment"),
             ("C#", "Rust", "Python", "Go", "C", "C++",
              "TypeScript / JavaScript"),
             ("API Design", "Loose Coupling and Replaceability",
              "Performance Optimization")),
        )
        for name, start, end, headings, languages, topics in cases:
            with self.subTest(file=name):
                markdown = (ROOT / "src" / name).read_text(encoding="utf-8")
                skills = markdown.split(start + "\n", 1)[1].split(end + "\n", 1)[0]
                self.assertEqual(
                    [line[4:] for line in skills.splitlines()
                     if line.startswith("### ")], list(headings))
                self.assertNotIn("\n#### ", skills)
                sections = skills.split("\n### ")[1:]
                self.assertEqual(len(sections), 4)
                for section in sections:
                    rows = [line for line in section.splitlines()
                            if line.startswith("| ")]
                    self.assertGreaterEqual(len(rows), 6)
                    self.assertEqual(rows[1], "| --- | --- |")
                language_rows = [line.split("|")[1].strip()
                                 for line in sections[0].splitlines()
                                 if line.startswith("| ")][2:]
                self.assertEqual(language_rows, list(languages))
                for topic in topics:
                    self.assertIn("| " + topic + " |", skills)
                self.assertIn("Lambda", skills)
                self.assertIn("Docker", skills)

                # Verify table rendering, not only Markdown source layout.
                html, _ = convert(ROOT / "src" / name)
                self.assertIn("<table>", html)
                self.assertIn("API", html)

    def test_company_metadata_is_bullet_list(self):
        """Keep employment metadata compact in both languages."""
        cases = (
            ("aboutme.md", "## 職歴", "## 語学", "- 在籍期間：", "- 職種：",
             ("株式会社ハンモック", "株式会社フィックスターズ",
              "株式会社コアコンセプト・テクノロジー", "株式会社カカクコム")),
            ("aboutme.en.md", "## WORK EXPERIENCE", "## LANGUAGES",
             "- Period: ", "- Role: ",
             ("Hammock Corporation", "Fixstars Corporation",
              "Core Concept Technologies Inc.", "Kakaku.com, Inc.")),
        )
        for filename, start, end, period_label, role_label, companies in cases:
            source = (ROOT / "src" / filename).read_text(encoding="utf-8")
            work = source.split(start, 1)[1].split(end, 1)[0]
            company_sections = work.split("\n### ")[1:]
            self.assertEqual(len(company_sections), len(companies))
            for section, company in zip(company_sections, companies):
                with self.subTest(filename=filename, company=company):
                    self.assertTrue(section.startswith(company))
                    self.assertIn("\n" + period_label, section)
                    self.assertIn("\n" + role_label, section)
                    self.assertNotIn("#### 在籍期間", section)
                    self.assertNotIn("#### 職種", section)
                    self.assertNotIn("#### Period", section)
                    self.assertNotIn("#### Role", section)

    def test_project_metadata_tables(self):
        """All experience metadata must use compact tables, not nested headings."""
        cases = (
            ("aboutme.md", "## 職歴", "## 語学",
             "| 項目 | 内容 |", "| 開発チームメンバー |",
             "| 開発環境 |", "| 言語・フレームワーク等 |"),
            ("aboutme.en.md", "## WORK EXPERIENCE", "## LANGUAGES",
             "| Item | Details |", "| Development Team Members |",
             "| Development Environment |", "| Languages / Frameworks |"),
        )
        for name, start, end, table, team, environment, languages in cases:
            with self.subTest(source=name):
                content = (ROOT / "src" / name).read_text(encoding="utf-8")
                section = content.split(start, 1)[1].split(end, 1)[0]
                self.assertEqual(section.count(table), 13)
                self.assertEqual(section.count(team), 11)
                self.assertEqual(section.count(environment), 12)
                self.assertEqual(section.count(languages), 13)
                self.assertNotIn("##### ", section)
                self.assertNotIn("#### 在籍期間", section)
                self.assertNotIn("#### Period", section)
                self.assertTrue(section.count("| 期間 |") == 11 if name == "aboutme.md"
                                else section.count("| Period |") == 11)

    def test_project_tables_appear_before_explanations(self):
        """Company projects must list metadata before explanatory prose."""
        cases = (
            ("aboutme.md", "## 職歴", "## 語学", "| 項目 | 内容 |"),
            ("aboutme.en.md", "## WORK EXPERIENCE", "## LANGUAGES",
             "| Item | Details |"),
        )
        for name, start, end, header in cases:
            with self.subTest(source=name):
                markdown = (ROOT / "src" / name).read_text(encoding="utf-8")
                experience = markdown.split(start, 1)[1].split(end, 1)[0]
                sections = experience.split("\n#### ")[1:]
                self.assertEqual(len(sections), 14)
                for section in sections:
                    with self.subTest(project=section.splitlines()[0]):
                        content = section.split("\n\n", 1)[1]
                        # The new renewal project has no verified period or team
                        # size yet, so do not invent a metadata table for it.
                        renewal = ("大規模リニューアル" in section.splitlines()[0]
                                   or "Major Web Application Renewal" in section.splitlines()[0])
                        if renewal:
                            self.assertFalse(content.startswith(header + "\n"))
                            self.assertTrue(content.strip())
                            continue
                        self.assertTrue(content.startswith(header + "\n"))
                        table, prose = content.split("\n\n", 1)
                        self.assertGreaterEqual(table.count("\n| "), 3)
                        self.assertTrue(prose.strip())
                        self.assertFalse(prose.lstrip().startswith("|"))

    def test_kakaku_renewal_and_main_responsibilities(self):
        """Both profiles cover cross-functional collaboration and architecture."""
        examples = (
            ("aboutme.md", "### 株式会社カカクコム", "## 語学",
             "#### プロジェクト：Webアプリケーションの大規模リニューアル",
             ("SSR", "企画", "デザイン", "単体テスト", "DI"),
             ("既存", "API", "入出力例", "責務", "インターフェース", "交換可能性")),
            ("aboutme.en.md", "### Kakaku.com, Inc.", "## LANGUAGES",
             "#### Project: Major Web Application Renewal",
             ("SSR", "product planning", "design", "unit tests", "DI"),
             ("existing", "API", "input/output examples", "responsibility",
              "interfaces", "replace")),
        )
        for name, company, next_section, project, main_words, project_words in examples:
            source = (ROOT / "src" / name).read_text(encoding="utf-8")
            section = source.split(company, 1)[1].split(next_section, 1)[0]
            self.assertEqual(section.count(project), 1)
            main, renewal = section.split(project, 1)
            for term in main_words:
                with self.subTest(file=name, part="main", term=term):
                    self.assertIn(term, main)
            for term in project_words:
                with self.subTest(file=name, part="renewal", term=term):
                    self.assertIn(term, renewal)
            self.assertEqual(section.count("| 項目 | 内容 |") +
                             section.count("| Item | Details |"), 1)

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
