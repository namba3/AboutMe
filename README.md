# AboutMe

Bilingual engineering profile built from Markdown and published with GitHub Actions.

- Japanese: https://namba3.github.io/AboutMe/
- English: https://namba3.github.io/AboutMe/index_english.html

## Editing and previewing

Edit the source files `src/aboutme.md` (Japanese) and `src/aboutme_english.md` (English).
The responsive styles are in `site/style.css`. Generated HTML is not committed to Git.

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/build_site.py --output dist
```

Open `dist/index.html` locally to preview the Japanese site.

## GitHub Pages deployment

The GitHub Actions workflow `.github/workflows/pages.yml` validates pull requests
and deploys the generated `dist/` site after changes are merged into `master`.
GitHub Pages must be configured to use **GitHub Actions** as its source.
The old manually exported HTML and Markdown Preview Enhanced LESS file have
been removed because they are not used by the current build.
