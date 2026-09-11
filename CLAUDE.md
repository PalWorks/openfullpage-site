# openfullpage-site

The marketing site for **OpenFullPage**, a free Chrome extension that captures a
whole web page as one image, annotates it and saves it. Static HTML, no build
step, no framework, no package manager. Deployed by GitHub Pages from `main` at
the repository root, so **a push to `main` is a deploy**.

> **Note for agents.** This file describes *this repository's* facts and
> invariants only. It deliberately sets no general workflow, tool preference or
> commit convention, so it should not conflict with instructions you already
> carry. If something here contradicts a direct instruction from the user,
> the user wins; tell them which line conflicted.

## Layout

| Path | What it is |
|---|---|
| `index.html` | The landing page. Self-contained: CSS and JS are inline. |
| `enforced.html` | The privacy proof page: five rules, permissions, verification steps. Was the previous landing page, kept whole. |
| `DESIGN.md` | **The design system. Read it before any visual change.** Tokens, colour rules with measured contrast, component specs, and a decisions log. |
| `CONTENT-PLAN.md` | Section arc, the capability inventory, and the content rules. |
| `llms.txt`, `llms-full.txt` | Machine-readable summaries for language-model crawlers. |
| `robots.txt` | Allows every search and AI crawler explicitly. Nothing here is private. |
| `sitemap.xml` | Both pages. Update `lastmod` when a page changes materially. |
| `assets/fonts/` | Three self-hosted variable woff2 files. |
| `tools/build-faq-schema.py` | Regenerates the FAQ structured data from the page. |
| `tools/page-audit.js` | Pre-existing audit helper. |

## Invariants

These are not style preferences. Breaking one damages the product's core claim.

1. **The site makes zero third-party requests.** No CDN fonts, no analytics, no
   embeds, no external icons, no tag managers. The product's whole argument is
   that it never phones home; a site that does undermines it. Fonts are
   self-hosted in `assets/fonts/` for exactly this reason.
2. **Never invent social proof.** No testimonials, user counts, star ratings or
   awards. There is no evidence for them, and the fake versions elsewhere in this
   category are why nobody believes privacy claims.
3. **Claims must be checkable.** Every privacy statement on the site maps to
   something enforced in the extension's manifest or CI. If you cannot point at
   the mechanism, do not write the sentence.
4. **The repository README is the authoritative feature list.** It is updated
   more often than this site. Where they disagree, the README is right.
5. **Accessibility is measured, not eyeballed.** Contrast ratios in `DESIGN.md`
   were computed. If you introduce a colour, compute its ratio before using it.

## Visual changes

Read `DESIGN.md` first. The three rules that catch people out:

- Saturated fills carry **dark ink** text. Only the deep navy carries white.
  White on the brand orange is 3.12:1 and fails AA.
- `--brand` (`#FF5A1F`) is a **fill** colour. When orange must be the *text*
  colour, use `--brand-text`, which is darkened in light mode.
- The capability mosaic is **deliberately uneven**. Do not tidy it into columns;
  an even grid reads as a taxonomy, an uneven one reads as abundance.

## Swap points

Two placeholders are waiting on the user. Both currently point at the extension
repository so nothing is broken, but neither is the final destination.

| Where | Element | Replace with |
|---|---|---|
| `index.html`, `#cta-webstore` | "Add to Chrome, free" button | The Chrome Web Store listing URL, once published |
| `index.html`, `#cta-github` | "View the source" button | Confirm the repository URL is the one the user wants public |

When the Web Store URL lands, update it in four places: the button, the
`SoftwareApplication` JSON-LD in `index.html`, `llms.txt`, and `llms-full.txt`.

## Verifying a change

There is no test suite. Run these before pushing.

```bash
# 1. Serve. Bind to all interfaces, NOT just 127.0.0.1: the detector's headless
#    browser cannot reach a loopback-only bind and silently reports nothing.
python3 -m http.server 8788

# 2. Confirm the site still makes zero third-party requests.
#    Expected output: []
~/Documents/gstack/browse/dist/browse goto http://localhost:8788/
~/Documents/gstack/browse/dist/browse js \
  'JSON.stringify(performance.getEntriesByType("resource").map(r=>r.name).filter(n=>!n.startsWith("http://localhost")))'

# 3. Design anti-pattern scan. Append a cache-buster: the headless browser will
#    otherwise serve a stale copy and you will audit the previous version.
npx impeccable detect "http://localhost:8788/?v=$(date +%s)"

#    Two findings are expected and accepted, both verified by measurement:
#      cream-palette          deliberate choice, see DESIGN.md > Colors
#      cramped-padding .spec  false positive; the rule reads the wrapper's own
#                             padding and cannot see the 22px inset the table
#                             cells provide. Measured text inset is 23px against
#                             a 22px corner radius.
#    Anything else the detector reports should be treated as real.

# 4. If you edited any question or answer, resync the FAQ structured data.
python3 tools/build-faq-schema.py          # verifies, exits 1 if stale
python3 tools/build-faq-schema.py --write  # applies
```

## Structured data

`index.html` carries one linked JSON-LD graph: `Organization`, `WebSite`,
`WebPage`, `BreadcrumbList`, `SoftwareApplication`, `ItemList`, `HowTo`,
`FAQPage`. `enforced.html` carries `Organization`, `WebSite`,
`SoftwareApplication`, `FAQPage`, `BreadcrumbList`, `TechArticle`.

Nodes are joined by `@id`, so the publisher, the product and both pages resolve
to one entity graph. Keep it that way: a new node should reference an existing
`@id` rather than restating the entity.

**The `FAQPage` node is generated, not hand-written.** It must match the visible
text or it is invalid. Edit the page, then run `tools/build-faq-schema.py --write`.

## Deploying

```bash
git add <specific files>      # never `git add -A`; the repo has untracked scratch
git commit
git push origin main          # this deploys
gh api repos/PalWorks/openfullpage-site/pages/builds/latest --jq '{status:.status,sha:.commit}'
```

Pages serves behind a CDN, so hard-refresh when checking the live result. The
build usually reports `built` within a minute.

## Facts worth not re-deriving

- Publisher: PalWorks, <https://palworks.ai>. **The domain currently returns
  HTTP 525**, a Cloudflare SSL failure. The link is in the footer and in the
  `Organization` schema on the assumption it will be fixed.
- Extension source: <https://github.com/PalWorks/OpenFullPage---Screenshot-Annotate-Save>
- The extension is **not** on the Chrome Web Store as of 2026-09-11.
- The site says "twenty tools". The product has more; the user is mid-build and
  asked to leave the count until that work lands. Do not quietly recount.
