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

## One-time GitHub Pages setting

In the repository's Settings > Pages > Build and deployment, set Source to GitHub Actions.
The workflow .github/workflows/pages.yml validates pull requests, and after a push to the
default master branch it builds both pages and deploys the dist directory.
It may also be run manually via Actions > Build and deploy GitHub Pages > Run workflow.
No personal access token is needed.

The existing docs directory is retained as a fallback during the transition. It is not
used by the new Actions deployment; remove it only after successful publication.

Note: The biography was last updated August 12, 2022. New deployment automation does
not update the biographical claims.
