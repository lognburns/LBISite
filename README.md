# Lauren Burns Interiors — Site

Static site for Lauren Burns Interiors. Content and layout are driven by `build.py`; HTML is generated into `site/`.

## Project layout

```
LBISite/
├── build.py              # Site generator — edit content, projects, and image refs here
└── site/
    ├── css/styles.css    # All styles
    ├── js/main.js        # Nav, hero slideshow, scroll reveals
    ├── images/           # All photography (downloaded from Wix CDN)
    ├── index.html        # Generated pages (re-run build.py after edits)
    ├── about.html
    ├── portfolio.html
    ├── services.html
    ├── press.html
    ├── contact.html
    └── projects/         # Individual project galleries
```

## Edit workflow

**Content & structure** — edit `build.py`:
- `PROJECTS` — portfolio projects, blurbs, and image lists
- `HERO_SLIDES`, `SERVICES`, `TEAM`, `AWARDS`, `FEATURES` — page content
- Image IDs in those lists map to files in `site/images/{id}.jpg`

**Styles** — edit `site/css/styles.css` directly.

**Behavior** — edit `site/js/main.js` directly.

**Images** — replace any file in `site/images/` (keep the same filename), or add a new image and reference its ID in `build.py`.

After changes to `build.py`, regenerate HTML:

```bash
python3 build.py
```

To re-download images from Wix (e.g. after adding new image IDs):

```bash
python3 build.py --fetch-images
```

## Preview locally

```bash
cd site && python3 -m http.server 8080
```

Open http://localhost:8080

## Live preview (GitHub Pages)

The site deploys automatically on every push to `main`.

**Client URL:** https://lognburns.github.io/LBISite/

Pages publishes the `site/` folder to the `gh-pages` branch on every push to `main`. In the repo, set **Settings → Pages → Build and deployment → Deploy from branch → `gh-pages` / `/ (root)`**.
