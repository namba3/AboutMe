# namba3.github.io

A bilingual engineering profile built from Markdown and published through GitHub Actions.

- Japanese: https://namba3.github.io/
- English: https://namba3.github.io/index_english.html

## Editing and previewing

Edit the Markdown source in src/aboutme.md (Japanese) or src/aboutme_english.md (English).
The responsive stylesheet is site/style.css. Output is generated, not committed.

    python -m pip install -r requirements.txt
    python -m unittest discover -s tests -v
    python scripts/build_site.py --output dist

Preview dist/index.html in a browser.
