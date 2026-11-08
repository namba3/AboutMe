# AboutMe

Bilingual engineering profile built from Markdown and published with GitHub Actions.

- Japanese: https://namba3.github.io/AboutMe/
- English: https://namba3.github.io/AboutMe/index_english.html

## Editing and previewing

Edit `src/aboutme.md` (Japanese) or `src/aboutme.en.md` (English).
Page filenames, language codes, titles, subtitles, display dates, and navigation labels
are configured in `src/site.toml`. The first `[[pages]]` entry defines the home page.
The responsive stylesheet is `site/style.css`. Generated HTML is not committed to Git.

### Local build

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/build_site.py --output dist
```

Preview `dist/index.html` in a browser. The output URLs remain unchanged when
the English Markdown source filename changes.

## GitHub Pages deployment

The GitHub Actions workflow `.github/workflows/pages.yml` validates pull requests
and deploys the generated `dist/` site after changes are merged into `master`.
GitHub Pages must be configured to use **GitHub Actions** as its source.
The legacy manually exported HTML and LESS files have been removed.
