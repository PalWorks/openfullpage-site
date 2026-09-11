---
# gstack: design-md-format=spec
name: OpenFullPage
description: Warm, generous, confident — a well-stocked toolbox handed over for free, with the safety built in rather than argued for.
colors:
  primary: "#FF5A1F"
  on-primary: "#17120E"
  primary-text: "#C93B06"
  primary-text-dark: "#FF7A47"
  background: "#FFF3E0"
  background-dark: "#16110D"
  surface: "#FFFDF8"
  surface-dark: "#211A14"
  surface-deep: "#0F2540"
  on-deep: "#FFFFFF"
  line: "#E6D9C4"
  line-dark: "#342A20"
  text: "#17120E"
  text-dark: "#F5EDE2"
  text-muted: "#6B5F52"
  text-muted-dark: "#A99A88"
  accent: "#FFC300"
  success: "#00A86B"
  warning: "#FFC300"
  error: "#F2507F"
typography:
  display:
    fontFamily: Bricolage Grotesque
    fontWeight: 800
    fontSize: clamp(38px, 4.9vw, 60px)
    letterSpacing: -0.022em
  body:
    fontFamily: Schibsted Grotesk
    fontSize: 1rem
    lineHeight: 1.6
  label:
    fontFamily: Spline Sans Mono
    fontSize: 0.78rem
    letterSpacing: 0.07em
  mono:
    fontFamily: Spline Sans Mono
    fontFeature: tnum
rounded:
  sm: 12px
  md: 14px
  lg: 22px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-hover:
    backgroundColor: "#E84E15"
  button-secondary:
    borderColor: "{colors.text}"
    textColor: "{colors.text}"
    rounded: "{rounded.full}"
  input:
    borderColor: "{colors.line}"
    rounded: "{rounded.sm}"
  card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.line}"
    rounded: "{rounded.lg}"
  nav-link:
    textColor: "{colors.text}"
---

# OpenFullPage design system

This file is the source of truth for every visual decision on this site. Read it
before changing anything in `index.html` or `enforced.html`. If you deviate, update
this file in the same commit and add a line to the Decisions Log.

## Overview

**Creative North Star:** A well-stocked toolbox, handed over cheerfully and for
nothing. The site's job is to make twenty capabilities feel like an unreasonably
generous gift, and to make safety feel like a property of the thing rather than a
case being argued.

**Product context:** A free, GPL-3.0 Chrome extension (Manifest V3, Chrome 116+)
that captures a full web page of any length as one image, annotates it, blurs what
should not be seen, and saves or copies it. Twenty distinct capabilities. It makes
no network requests: `connect-src 'none'` in the manifest means Chrome itself
blocks them, and five such properties fail the build if broken.

**Mode per surface:**
- `index.html` is **Persuade**. The visitor decides and installs.
- `enforced.html` is **Read**. The visitor is checking a claim and wants structure,
  not persuasion. It deliberately keeps the older, quieter treatment.

**Key characteristics, what someone notices in five seconds:**
- Warm cream ground, neither white nor dark.
- Five saturated hues as flat fills, no gradients anywhere.
- A heavyweight display face with real character.
- Twenty items shown as an uneven coloured mosaic, never a feature grid.
- Two numbers carry the pitch: **20** tools, **$0** forever.

## The argument the design has to make

The premise, in order, and it is never reversed:

1. **Abundance.** Twenty tools. The visitor should feel slightly surprised at how
   much is here.
2. **Free.** No tier, no trial, no account. The second number exists to kill the
   "what's the catch" reflex before it forms.
3. **Safe.** Reassurance, not prosecution. Named mechanism, warm language, moved on.

An earlier direction led with proof ("does all this, and sends nothing"). It was
rejected because it argued a case rather than making an offer, and it read as a
statement for a cause rather than a product site. The safety material still exists
and is still excellent, but it now lives on `enforced.html` and is linked, not led
with.

## Why this looks nothing like the competition

Researched 2026-09-11 by opening each one:

| Site | Display face | Accent |
|---|---|---|
| gofullpage.com | `system-ui` | none dominant |
| getfireshot.com | `-apple-system` | `#007bff`, Bootstrap default |
| capture-full-page.com | `system-ui` | `#4f46e5`, Tailwind indigo, used 95x |
| cocoshot.net | Inter 800 | `#facc15` + `#a855f7` gradient on `#050511` |
| scribe.com | ABC Diatype | one muted blue |

Four of five have no typographic voice. The entire category competes on colour and
nobody competes on type. Two consequences drive this system:

1. **Type is the unclaimed differentiator.** A display face with character is the
   cheapest way to not look like everyone else here.
2. **The category's "vibrant" is poison for us.** Indigo-to-purple gradients on
   near-black is both the AI-generated default and the visual language that makes
   privacy claims read as marketing. CocoShot badges "Privacy First" inside a
   purple gradient funnel and nobody believes it. We go warm and light instead.

## Colors

**Strategy:** Full palette. Five saturated hues plus a deep navy, all flat. Colour
is how abundance is expressed, so it is allowed to be plentiful. What it is never
allowed to be is blended.

**Light or dark:** Light by default, decided by the use scene. People reach for this
mid-task in a bright browser window, next to the page they are capturing. A dark
marketing site next to a light working context reads as a different application.
A dark theme exists because users asked for one, but light is the design intent and
the one to get right first.

### The three colour rules

**Rule 1 — saturated fills always carry dark ink, and only the deep navy carries
white.** Verified contrast against `--on-fill` (`#17120E`), all past 4.5:1:

| Fill | vs `--on-fill` | vs white |
|---|---|---|
| `--brand` `#FF5A1F` | **5.96** | 3.12 (fails) |
| `--sun` `#FFC300` | **11.56** | 1.61 (fails) |
| `--grass` `#00A86B` | **6.03** | 3.08 (fails) |
| `--berry` `#F2507F` | **5.52** | 3.37 (fails) |
| `--deep` `#0F2540` | 1.20 (fails) | **15.45** |

White on orange is the instinct and it is wrong here. Do not reach for it.

**Rule 2 — when orange has to BE the text, it uses a different token.** `--brand`
at `#FF5A1F` is only 2.84:1 on the cream ground, which fails even the 3:1 large-text
bar. Orange text uses `--brand-text`, which is `#C93B06` in light (4.66:1) and
`#FF7A47` in dark (7.26:1). `--brand` is a fill colour. `--brand-text` is a text
colour. They are not interchangeable.

**Rule 3 — the saturated hues do not flip between themes.** `--brand`, `--sun`,
`--grass`, `--berry` and `--deep` are identical in light and dark, and so is
`--on-fill`. Only the ground, surface, text, muted and line tokens flip, via
`light-dark()`. This keeps the mosaic identical in both themes, which is correct:
the tiles are objects, not surfaces.

### What each colour is for

- `--brand` tangerine: every real call to action, and nothing else. Never a second
  button on the same screen competing with the first.
- `--accent` sun: the free-and-generous message, the second big number, the link
  out of a navy panel.
- `--deep` navy: the two reassurance blocks. This is how safety gets its own weight
  without turning the whole page cold.
- `--grass`: confirmed safety claims and the tick marks.
- `--error` berry: reserved for the blur/redaction tile. The one destructive action
  gets the one alarming colour.
- Neutrals derive from the cream ground, never from grey.

### Accepted detector finding

`npx impeccable detect` flags `cream-palette` on this site. That is a deliberate,
documented choice, not a reflex: every rival in the category is near-white or
near-black, and warm is the differentiator. The waiver is recorded as an HTML
comment near the top of `index.html`. Do not "fix" it. Every other detector finding
should be treated as real.

## Typography

Three faces, self-hosted as variable woff2 in `assets/fonts/`. Total weight 128KB.

**Bricolage Grotesque** — display. From contemporary editorial and independent
software, where a face is expected to have personality rather than disappear. It is
the single biggest differentiator available, given four of five rivals ship a system
font. Used for `h1`, `h2`, `h3` and the two big numbers. Never for body text.

**Schibsted Grotesk** — body and UI. A news-workhorse grotesque, highly legible at
17px, quiet enough to let the display face and the palette do the talking.

**Spline Sans Mono** — two jobs only. Literal machine output (the network panel,
`connect-src 'none'`) and small tracked labels. **If it is set in mono, it is either
something a machine printed or something you could paste into a terminal.** Never
use mono for a marketing label.

**Loading is self-hosted on purpose.** The product's claim is that it makes no
outbound requests, so the site must not make third-party ones either. The previous
version of this site loaded Google Fonts, which was a hole in its own argument.
Verified 2026-09-11: the page makes zero third-party requests. **If you add a font,
an icon set, an analytics snippet or an embed, you break the one thing this site
cannot afford to get wrong.**

**Scale:** 60 / 44 / 30 / 20 / 17.5 / 17 / 15.5 / 12.5. Display and body are
separated by more than a weight at every level.

**Headline sizing is capped for a reason.** The `h1` was 78px and consumed 38% of
the first viewport on a desktop display. It is now `clamp(38px, 4.9vw, 60px)` with
`max-width: 17ch`. If you lengthen the headline, re-check the viewport share; a long
headline at display size is the most common way this page regresses.

**Minimum text size is 12.5px**, and that floor is only for mono labels. Body copy
never goes below 15.5px.

## Layout

Single hard left margin at `min(1240px, 100% - 56px)`. Nothing is centred except
text inside a coloured pill.

**Section rhythm:** full-width content on the cream ground alternates with large
rounded colour blocks (navy for safety, sun for free). That alternation is what
gives the page rhythm. There are no divider graphics, no wavy SVGs, no blobs.

**The hero** is a 1.12 / 0.88 two-column split: copy left, the what-you-get card
right.

**The mosaic** is a flex wrap with mixed tile widths, so twenty items pack unevenly.
**The unevenness is the entire point.** An even grid makes twenty items look like a
taxonomy; an uneven one makes them look like abundance. Three tiles are deliberately
oversized (`01`, `04`, `17`) to break the rhythm. If you add a capability, add a
tile and let it land where it lands. Do not tidy the mosaic into columns.

**Breakpoint at 980px** collapses every two-column block to one and the steps to a
stack. Below 820px the section links in the masthead hide, leaving the enforced
link, the theme toggle and the install pill.

## Elevation & Depth

Depth comes from flat colour blocks on the cream ground and from 1px `--line`
borders. No shadows on cards, no glows, no frosted glass, no zero-offset halos. The
only implied layer is a rounded colour block sitting on the ground by contrast
alone.

## Shapes

- `full` (9999px) — buttons and pills only.
- `lg` (22px) — the large colour blocks and step cards.
- `md` (14px) — mosaic tiles.
- `sm` (12px) — elements nested inside a colour block.

Inner radius = outer radius minus the gap. Never the same radius on everything.

## Components

**button-primary (`.cta`)** — `--brand` fill, `--on-fill` text, `full` radius,
16px/28px padding, 17px/700. Hover darkens to `#E84E15`. Never gradient-filled,
never white-texted.

**button-secondary (`.cta.alt`)** — transparent with a 2px `--text` border; hover
inverts to solid `--text` with `--bg` label.

**nav pill (`.pill`)** — `--text` fill, `--bg` label. The one dark element in the
masthead. Hover drops opacity to .86.

**theme toggle (`.theme`)** — 34px circle, 1px `--line` border. Cycles system →
light → dark → system. System is the *absence* of `data-theme`, so cycling back to
it returns control to the OS rather than pinning the current appearance. A pre-paint
inline script in `<head>` applies the stored value before the body renders; without
it the page flashes the wrong theme. Carries an `aria-label` that updates with state
plus an `sr-only` text label.

**mosaic tile (`.t`)** — flat hue fill, `md` radius, 14px/18px padding, 17px/700.
The number is 12.5px mono at full opacity. It used to be 68% opacity, which dropped
it to about 2.2:1 against the fills; size carries the de-emphasis now, not
transparency. Three tiles take `.wide` (21px, 18px/24px padding).

**step card (`.step`)** — `--surface` on a `--line` border, `lg` radius, image
flush to the top edge with a `--line` border beneath. Images carry explicit
`width`/`height` and `loading="lazy"`.

**what-you-get card (`.get`)** and **safe panel (`.safe`)** — `--deep` navy,
`lg`/`26px` radius. Text is `--on-deep` white; secondary text is `--deep-muted`
`#9FB4C8` (7.24:1 on navy). The only place white text is correct.

**netcard (`.netcard`)** — a deliberately empty network panel. It is evidence, so it
is set entirely in mono and never styled to look designed.

**Focus** — every interactive element gets `:focus-visible` at 2px `--brand-text`,
3px offset. Do not remove it.

## Do's and Don'ts

**Do**
- Lead with what the visitor gets, then that it is free, then that it is safe.
- Use real product screenshots. The extension UI already shows `1265 × 6022 pixels`
  and "The image never leaves your computer" on screen; that is worth more than any
  copy you could write.
- Let the mosaic be visually uneven.
- Keep safety in plain, warm language. Name the mechanism once, then move on.
- Re-check contrast whenever you introduce a colour. The numbers in this file were
  computed, not eyeballed.

**Don't**
- Use a gradient anywhere: background, text, or button.
- Build a three-column icon-in-circle feature grid. The mosaic exists so that never
  happens.
- Put white text on any fill except the navy.
- Use `--brand` as a text colour. Use `--brand-text`.
- Invent testimonials, user counts, or star ratings. There is no evidence for them,
  and the category's fake versions are exactly why nobody believes privacy claims.
- Load anything from a third-party domain, fonts included.
- Let any single hue dominate. When one colour owns the page the mosaic stops
  reading as abundance.
- Set body copy below 15.5px, or any text below 12.5px.

## Motion

- **Approach:** minimal-functional.
- **Easing:** enter(ease-out) exit(ease-in) move(ease-in-out)
- **Duration:** micro(50-100ms) short(150-250ms) medium(250-400ms) long(400-700ms)
- **Currently authored:** nothing beyond hover, focus and smooth anchor scrolling.
  `prefers-reduced-motion: reduce` disables smooth scroll and all transitions.
- **If one moment is ever added,** it should be the mosaic tiles settling in on first
  view, staggered about 25ms apart, so twenty items visibly arrive rather than
  appearing at once. Nothing else on this page earns animation.

## Adding a new section

1. Decide whether it sits on the cream ground or inside a colour block. Alternate;
   never put two colour blocks back to back.
2. Use `<section><div class="wrap">…</div></section>`. Headings are `h2.h2`, intro
   copy is `p.sub`.
3. Left-align everything. No centred text.
4. If it introduces a colour, compute its contrast against `--on-fill` and the
   ground before using it, and add it to the table in Colors.
5. Run `npx impeccable detect http://localhost:PORT/` before committing. Bind the
   server to all interfaces, not just `127.0.0.1`, or the detector's browser cannot
   reach it and silently reports nothing.
6. Confirm the page still makes zero third-party requests.

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-09-11 | Initial design system created | /design-consultation, after researching five category rivals and testing three directions |
| 2026-09-11 | Rejected the press-room direction (grey ground, Redaction typeface) | Read as a statement for a cause rather than a product site for a Chrome extension |
| 2026-09-11 | Premise changed from proof-led to abundance-led | "Twenty tools, free, and safe" invites installs; "we do a lot and send nothing" argues a case |
| 2026-09-11 | Old landing page preserved as `enforced.html` | The five rules, permission table and verification steps are the best material on the site; too heavy to lead with, too good to delete |
| 2026-09-11 | All fonts self-hosted | The previous site loaded Google Fonts, contradicting the product's own no-outbound-requests claim. Verified zero third-party requests after the change |
| 2026-09-11 | Dark theme retained with a three-state toggle | Light is the design intent, but the toggle was an explicit user request and removing it would be a regression |
| 2026-09-11 | Dark ink on all saturated fills, white only on navy | White on the brand orange is 3.12:1 and fails AA at the button's size |
| 2026-09-11 | Separate `--brand-text` token | `--brand` as text is 2.84:1 on cream and fails even the large-text bar |
| 2026-09-11 | `cream-palette` detector finding accepted | Deliberate competitive choice; every rival is near-white or near-black |
