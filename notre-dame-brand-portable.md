# Notre Dame Brand — Portable Skill

> Single-file version of the `notre-dame-brand` skill for any AI assistant or agent that can't load folder-based skills. Paste the whole file into a system prompt, custom instructions, or the start of a conversation.
>
> **Generated file — do not edit by hand.** Source: `.github/skills/notre-dame-brand/`. Regenerate with `python3 scripts/build-portable.py`.

**When to use:** Apply University of Notre Dame masterbrand standards to any visual or written deliverable for a Notre Dame audience — slides, posters, flyers, one-pagers, social graphics, signage, event materials, donor or alumni communications, reports, diagrams — even if "brand" isn't mentioned. Also use when someone asks to "make this look like Notre Dame," references the Academic Mark, OnMessage guidelines or templates, or names an ND school, office, or initiative (Keough, Mendoza, OIT, etc.) without a more specific sub-brand. For web pages, Conductor sites, and software UI, hand off to the `nd-web-theme` skill. Not for AI@ND materials (use `ai-nd-brand`) or athletics.

**Contents:** [Skill](#skill) · [Colors](#reference-colors) · [Typography](#reference-typography) · [Logos](#reference-logos) · [Voice](#reference-voice)

---

<a id="skill"></a>

## Skill


A visual and verbal identity skill for the University of Notre Dame masterbrand, sourced from the official OnMessage guidelines (`onmessage.nd.edu`) and calibrated against the OnMessage template library (`onmessage.nd.edu/downloads/templates/` — posters, social suites, digital signage, presentations, table tents, banners, notecards, postcards, print signage). Use it for academic, administrative, and general University communications — anything that should read first as "Notre Dame," not as a specific sub-brand.

### When this skill applies vs. when something else does

Notre Dame has several brand layers. This skill is the **University masterbrand** — the layer most communications should sit in.

- **Academic units** (Keough School, Mendoza, College of Arts & Letters, ND Research, an institute or center): use this skill. The masterbrand is the starting point; if a unit has its own custom logo lockup, treat that as a layered addition on top of these standards, not a replacement.
- **Administrative units** (OIT, OPAC, HR, Campus Services): use this skill, with the same logic.
- **Web pages, nd.edu sites, and software UI**: see "Web and software UI" below — hand off to the `nd-web-theme` skill.
- **Sub-brand: AI@ND / AI Enablement**: use the separate `ai-nd-brand` skill.
- **Athletics**: do not use this skill. Athletics has its own brand system built around the leprechaun, the interlocking monogram, and spirit marks. Decline politely and point to `onmessage.nd.edu/athletics-branding/`.

If you're unsure which layer something belongs in, default to the masterbrand (this skill). It's almost always correct.

### The core idea

Notre Dame's current look — as seen across the OnMessage templates — is **clean, modern, and sans-serif-led**, with tradition carried by photography of campus architecture rather than by old-style type. Three signals carry most of the weight:

1. **ND Blue and ND Gold, with gold used sparingly.** ND Blue is the dominant brand color; gold is an accent — a thin rule, a small label, a single highlight. Around 90% of color use to highly affiliated audiences should come from the primary palette. Secondary colors complement, never substitute.

2. **A sans-serif voice.** Headlines, titles, body, labels, and UI are all set in the Galaxie Polaris family (substitute: Arial / Arial Narrow). The serif (Garamond Premier; substitute Georgia) is an **occasional accent** reserved for ceremonial or formal moments — not the default headline face.

3. **The Academic Mark as a quiet signature.** The shield-and-wordmark lockup appears small, in a corner or footer, as an endorsement — never as the centerpiece, and never wider than 25% of the piece.

If a piece carries all three — ND Blue/Gold with restrained gold, sans-led type, Academic Mark present — it reads as Notre Dame.

**Common failure modes to avoid:** Georgia/Garamond headlines on everything; heavy, near-black, or moody-gradient backgrounds; gold used on many elements at once; the Dome or Monogram standing in for the Academic Mark.

### The OnMessage template look

These patterns recur across the template library. Borrow them — they are what makes a piece feel like current ND work rather than a generic "navy and gold" design.

- **Type hierarchy.** Big headlines in **bold condensed sans** (Galaxie Polaris Condensed Bold → Arial Narrow Bold), sometimes all caps for short titles. Alternatively, very **light-weight sans** at large size for an elegant title ("Title Goes Here" set thin and airy). Subheads in light or light-italic sans. Body in regular sans at comfortable size.
- **Eyebrow labels.** A short ALL-CAPS label above the headline, in small sans, either gold text or white text on a small solid gold bar. This is one of the most consistent template signatures.
- **Hairline gold rules.** Thin (≈0.5–1pt) gold lines framing a title, dividing a header, or running diagonally/horizontally across a cover. Thin, not thick bars.
- **Shaped photo masks.** Photography cropped into architectural shapes — Gothic arches, rounded arch tops, scalloped/cloud-edged curves, stained-glass-style segmented windows, circles for headshots — often with a thin gold outline. This is the signature ND template move; use it when photos are available.
- **Photo-forward.** Campus architecture (Dome, Basilica interiors, spires, aerial campus), people, and events carry the tradition. Full-bleed photos with a solid-color text panel beside or over them are common.
- **Subtle pattern texture.** Low-contrast tonal patterns (ND Blue on slightly lighter/darker blue: diagonal lattices, shield outlines, architectural tracery) on some cards and signage. Always subtle — tone-on-tone, never busy.
- **Serif only for ceremonial pieces.** Christmas cards, "Save the Date" announcements, and one formal presentation variant use the serif (often spaced caps). That's the scope for serif display.

### Colors

Primary: **ND Blue (PMS 289)** and **ND Metallic Gold (PMS 10127)**, plus a screen-friendly Bright Gold.

- **ND Blue** `#0c2340` — the brand blue; solid cover/panel color, headings on light backgrounds
- **ND Metallic Gold** `#ae9142` — accents in print and for hairline rules/eyebrows
- **Bright Gold** `#d39f10` — screen-safe gold for highlights on slides and screens
- **White** `#ffffff` — primary reading surface; type on ND Blue

**Light vs. dark — how to balance it:**

- **Reading surfaces are light.** Document pages, report bodies, slide content pages, one-pager bodies, letterhead, and diagrams default to **white** (or Warm White `#f8f4ec`) with ND Blue headings and dark gray body text.
- **ND Blue is for brand moments.** Covers, title slides, section dividers, posters, social graphics, signage, and name cards may use a solid ND Blue field — that is how the templates present promotional pieces. Keep it a flat `#0c2340`.
- **Never go darker than ND Blue.** No black or near-black backgrounds, no navy-to-black gradients, no dark vignettes, no dim photo overlays that make the whole piece moody. If a photo needs a text overlay, use a solid ND Blue panel beside the photo rather than darkening the photo.
- **Mixed pieces are common:** a light body with an ND Blue header band or footer, or an ND Blue cover followed by white interior pages.

The full palette (secondary colors with hex, Pantone, CMYK) lives in [the Colors reference](#reference-colors).

### Typography

| Role | Official | Always-available substitute |
|---|---|---|
| Headlines, titles, display (default) | Galaxie Polaris Condensed Bold, or Galaxie Polaris Light at large sizes | **Arial Narrow Bold**, or **Arial** (regular/light-looking weight) |
| Subheads | Galaxie Polaris Light / Light Italic | **Arial** (regular or italic) |
| Body, captions, labels, UI | Galaxie Polaris | **Arial** |
| Ceremonial / formal accent only | Adobe Garamond Premier | **Georgia** |

Guidance:

- **Default every headline to sans.** Only reach for the serif when the piece is ceremonial (invitations, holiday cards, commencement, memorial, formal "Save the Date") or the user asks for it. Even then, pair it with sans body and labels.
- **Don't mix serif and sans headlines on the same piece.** Pick one display voice.
- **Eyebrow labels:** small, ALL CAPS, slightly letter-spaced sans.
- **Weight contrast does the work:** bold condensed headline + light subhead + regular body, rather than switching families.
- Default to the substitutes in any environment where the licensed fonts aren't installed (nearly every .pptx, .docx, and generated file). Don't pretend a font is loaded when it isn't.

Additional type detail lives in [the Typography reference](#reference-typography).

### Logos and marks

Notre Dame has four official marks. **Their roles are not interchangeable.**

- **Academic Mark** — the primary mark (shield + "University of Notre Dame" wordmark). Required on academic and administrative communications. Small, corner/footer placement.
- **Monogram** — the interlocking ND. *Non-academic units only* (athletics, campus services, alumni clubs, student groups). Not for academic communications.
- **University Seal** — official documents only (diplomas, presidential communications, signage).
- **Golden Dome** — a landmark, not a logo. Beautiful in photography (and frequently featured in template photo masks), but don't use it as a logo substitute or decorative icon.

Publicly hosted SVG wordmarks (wordmark only, no shield):

- `https://static.nd.edu/images/marks/blue/ndmark.svg` (navy, for light backgrounds)
- `https://static.nd.edu/images/marks/gold/ndmark.svg` (gold, for dark backgrounds)
- `https://static.nd.edu/images/marks/white/ndmark.svg` (white, for ND Blue/photo backgrounds)
- `https://static.nd.edu/images/marks/gray/ndmark.svg` (dark gray, neutral)

The full Academic Mark with shield is at `onmessage.nd.edu/downloads/#logos`. Detailed rules live in [the Logos reference](#reference-logos).

### Voice and tone

ND's voice is **focused, timeless, motivating, powerful, truthful**: clear hierarchy with one strong point on top, no trendy phrasing, copy that asks the reader to do something, bold statements over hedged ones, concrete proof points over abstractions.

Sample phrases from the official guidelines:

- "Creating the leaders the world needs."
- "Tackling the most enduring questions of our time."
- "A century-long tradition of always looking ahead."

Full guidance is in [the Voice reference](#reference-voice).

### Web and software UI → use the `nd-web-theme` skill

When the deliverable is a **web page, an nd.edu or Conductor site, a landing page, an HTML mockup meant to look like nd.edu, or a software/app UI**, this skill is not the right tool on its own. The University's web look is governed by the **Notre Dame Web Theme v4** and its component library, which the `nd-web-theme` skill covers in depth (theme components, foundation tokens, Conductor-ready HTML, and local previews).

- **If `nd-web-theme` is available**, invoke it and follow it for layout, components, and CSS. Use this skill only for voice/copy and for confirming mark usage.
- **If it isn't installed**, tell the user it exists and recommend installing it before continuing: it lives at **https://github.com/OIT-AI-Skills/nd-web-theme-conductor** and installs like any folder-based skill (copy the folder into the agent's skills directory, or zip it with `SKILL.md` at the root and upload it to an app that accepts skills). Then invoke it.
- If the user wants to proceed without it, build a clean light page (white background, ND Blue headings in sans, Bright Gold accents, Academic Mark in the header/footer, ND Blue footer) and say that the result approximates rather than implements the ND web theme.

Do not hand-invent nd.edu component classes or theme CSS from this skill.

### Layout principles

- **Generous negative space.** ND materials never feel crowded.
- **One focal point per view.** Gold anchors the single most important element — not five things.
- **Light for reading, ND Blue for brand moments** (see Colors). Nothing darker than ND Blue.
- **Photography over illustration**, ideally in an architectural shaped mask. If no photos are available, leave clearly marked space for one rather than filling with stock graphics or icons.
- **Text beside photos, not on darkened photos.** Split layouts — photo on one side, solid ND Blue or white text panel on the other — are the template default.

### Deliverable-specific guidance

#### Presentations (slide decks, .pptx, Google Slides, Keynote)
- **Title slide:** either a full-bleed campus photo with a large light-weight sans title and thin gold hairlines, or a solid ND Blue field with a bold condensed ALL-CAPS title framed by gold hairlines. Academic Mark small, bottom or corner.
- **Section dividers:** ND Blue field, sans title, gold eyebrow label.
- **Content slides:** white background, ND Blue sans title, gray (`#333`/`#555`) Arial body, gold for one focal data point, eyebrow label optional. Content slides should be light.
- **People/speaker slides:** headshot in a circle or arch mask with a thin gold outline.
- Use whatever slide tooling or presentation skill is available for the mechanics, then apply the brand on top.

#### Documents and reports (.docx, Google Docs, PDF)
- White or Warm White page, ND Blue **sans** headings (Arial, bold or regular), dark gray Arial body.
- Gold small-caps eyebrow labels above section titles; thin gold rules for section breaks.
- Academic Mark top of page 1; optional ND Blue header band on the cover page only.
- Footer: thin gray rule, unit name + contact on the left, page number on the right.

#### Posters, flyers, one-pagers
- Pick one focal element (headline, date, or photo) and let it dominate.
- Typical template layout: solid ND Blue field, photo in a shaped mask (arch, scallop, Gothic window) with a thin gold outline, bold condensed sans headline, gold eyebrow bar, short body, QR code and Academic Mark near the bottom.
- A white-background version with ND Blue type is equally valid, especially for text-heavy one-pagers.
- Gold only on the eyebrow, hairlines, and mask outline.

#### Social graphics and digital signage
- Same vocabulary as posters, adapted to the aspect ratio: photo + solid ND Blue text panel, condensed sans headline, gold eyebrow, Academic Mark small.
- Signage often has a department-name header strip with a thin gold rule beneath it.
- Keep text short and large; one message per screen.

#### Ceremonial pieces (invitations, holiday cards, save-the-dates)
- The one place the serif leads: spaced-caps Georgia/Garamond, gold or white on ND Blue, subtle tone-on-tone pattern, lots of air.

#### Diagrams (flowcharts, architecture, org charts)
- Light background, ND Blue nodes/text in sans, gray connectors, Bright Gold for the one critical path or focal node.
- Avoid rainbow palettes and dark backgrounds.

### Handling gaps and edge cases

This skill is a working subset of ND's brand system, not the whole thing. When something falls outside its coverage:

1. Reason from the three core signals (ND Blue/Gold with restrained gold, sans-led type, Academic Mark present).
2. Point the user to the relevant OnMessage section — especially `onmessage.nd.edu/downloads/templates/`, which has ready-made Box downloads for posters, social suites, signage, presentations, Zoom backgrounds, table tents, banners, notecards, postcards, and e-letterhead. If a matching template exists, suggest starting from it.
3. For unit-specific custom logos, defer to the unit's approved lockup.
4. For approval questions ("can I use the Dome on a t-shirt?"), the answer is "ask Notre Dame Creative" — don't invent permissions.

A gap honestly acknowledged is better than a fake standard confidently asserted.

---

<a id="reference-colors"></a>

## Reference: Colors


The complete University of Notre Dame color palette as published at `onmessage.nd.edu/university-branding/colors/`, with practical guidance for digital and print use.

### Primary palette

These two colors should dominate Notre Dame communications — together they account for ~90% of the color use in materials directed at highly affiliated audiences (alumni, donors, advisory councils).

| Color | Hex | Pantone | CMYK | RGB |
|---|---|---|---|---|
| **ND Blue** | `#0c2340` | PMS 289 | C99 M84 Y45 K51 | R12 G35 B64 |
| **ND Metallic Gold** | `#ae9142` | PMS 10127 | C31 M39 Y88 K5 | R174 G145 B66 |

#### A note on gold

ND Metallic Gold is a *spot ink* — it's designed to print as a single solid color, often with metallic foil. It does not reproduce well on screen, where it appears muddy or olive. For any digital deliverable (web, slides, app, social), use **Bright Gold (`#d39f10`)** from the secondary palette instead. ND's own guidelines call this out explicitly.

### Secondary palette

These extend the primary palette without competing with it. They're especially useful for charts, infographics, complex data visualization, and giving photo treatments depth. They're not mandatory — communicators can stick with primary-only — but they're sanctioned and on-brand.

#### Blues

| Color | Hex | Pantone | Notes |
|---|---|---|---|
| Medium Blue | `#143865` | PMS 2154 | Slightly lighter than ND Blue; good for surfaces inside dark sections |
| Bright Blue | `#1c4f8f` | PMS 2945 | A brighter blue for charts and secondary accents |
| Dark Sky Blue | `#c1cddd` | PMS 5376 87% | Quiet light blue; muted supporting text on ND Blue |
| Medium Sky Blue | `#e1e8f2` | PMS 650 57% | Background tint for sidebars or cards |
| Light Sky Blue | `#edf2f9` | PMS 656 40% | Very subtle background tint |

#### Golds

| Color | Hex | Pantone | Notes |
|---|---|---|---|
| Dark Gold | `#8c7535` | PMS 4495 | Use for gold text on light backgrounds where Bright Gold would be too vivid |
| **Bright Gold** | `#d39f10` | PMS 117 | The screen-safe primary gold — use this for digital |

#### Warm whites

| Color | Hex | Pantone | Notes |
|---|---|---|---|
| Warm White | `#efe9d9` | PMS 4545 28% | Slightly creamy off-white; good for academic / editorial backgrounds |
| Light Warm White | `#f8f4ec` | PMS 9064 60% | Even paler warm white; a soft light surface for documents and programs |

#### Greens

| Color | Hex | Pantone | Notes |
|---|---|---|---|
| Green | `#0a843d` | PMS 347 | Use sparingly — charts or a tertiary accent |
| Light Green | `#b3dac5` | PMS 2246 85% | Background tint for green callouts |

### Light vs. dark balance

The OnMessage templates show ND Blue as a solid field on covers, posters, social graphics, signage, and name cards — and white on letterhead and reading surfaces. Follow the same split:

- **Reading surfaces are light.** Document pages, report bodies, slide content pages, one-pager bodies, letterhead, and diagrams use white (or Light Warm White `#f8f4ec`) with ND Blue headings and dark gray body text.
- **ND Blue is for brand moments.** Covers, title slides, section dividers, posters, social, and signage may use a flat ND Blue `#0c2340` field.
- **Never go darker than ND Blue.** No black or near-black backgrounds, no navy-to-black gradients, no dark vignettes, no dimmed photos under text. Put text on a solid ND Blue or white panel beside the photo instead.
- **Subtle texture is fine:** tone-on-tone patterns using Medium Blue `#143865` on ND Blue.

### Web and software UI

For nd.edu sites, Conductor pages, HTML mockups meant to match nd.edu, and app UI, use the `nd-web-theme` skill (https://github.com/OIT-AI-Skills/nd-web-theme-conductor). It carries the Web Theme v4 color tokens, CSS variables, and light/dark handling; don't hand-build theme CSS from this file.

### Color usage guidance

#### When to use primary colors

Primary colors should be the dominant colors for highly-affiliated audiences: alumni magazines, donor reports, advisory council materials, presidential communications. The ND Blue + ND Gold pairing on these audiences makes up roughly 90% of the color use.

#### When to use secondary colors

Secondary colors add depth and creative range. They're appropriate for:

- Editorial / long-form content where pure primary palette would feel monotonous
- Data visualization where you need 5+ distinct categories
- Photo treatments and overlays
- Background tints for sections, cards, and callouts
- Muted supporting text on ND Blue fields (sky blue tints)

#### When to use Warm White vs. pure white

Warm White (`#f8f4ec`) reads as more editorial, more academic, more "bookish." It works well for journals, research reports, donor materials, and programs.

Pure white (`#ffffff`) reads as more modern, more digital, more "interface." Use it for slides, dashboards, technical materials, and anywhere you want maximum contrast.

#### Accessible color pairings

Tested color combinations that meet WCAG AA contrast (≥4.5:1 for body text):

- ND Blue (`#0c2340`) text on white background — passes AAA
- White text on ND Blue background — passes AAA
- Dark Gray (`#333`) text on Warm White (`#f8f4ec`) — passes AAA
- ND Blue (`#0c2340`) text on Sky Blue (`#e1e8f2`) — passes AA
- Bright Gold (`#d39f10`) text on ND Blue background — passes AA at 18pt+ only; do not use for body text

**Avoid** Bright Gold for body text on any background — it's an accent color, not a reading color.

---

<a id="reference-typography"></a>

## Reference: Typography


The University of Notre Dame typography system, sourced from `onmessage.nd.edu/university-branding/fonts/` and calibrated against the OnMessage template library (`onmessage.nd.edu/downloads/templates/`).

### The short version

Current ND communications are **sans-serif-led**. Headlines, titles, subheads, body, labels, and UI are set in Galaxie Polaris (substitute: Arial / Arial Narrow). The serif, Garamond Premier (substitute: Georgia), is an occasional accent for ceremonial and formal pieces — not the default headline face.

### The two official typefaces

#### Galaxie Polaris (sans-serif) — the workhorse

The primary typeface for almost everything: headlines, titles, subheads, body copy, captions, labels, navigation, and UI.

- Licensed; downloads are restricted to the ND community.
- **Galaxie Polaris Condensed** is available and is the go-to cut for bold, compact headlines in the templates.
- **Universal fallback: Arial** (and **Arial Narrow** for the condensed cut). Sanctioned by ND.

#### Adobe Garamond Premier (serif) — the ceremonial accent

Used for ceremonial and formal moments where heritage should come forward: invitations, holiday cards, "Save the Date" announcements, commencement and memorial materials, and the occasional formal presentation cover.

- Available via Adobe Fonts (Creative Cloud). Non-Adobe users may use **Adobe Garamond Pro** as an interim official option.
- **Universal fallback: Georgia.** Sanctioned by ND.

### How the templates use type

Patterns that recur across OnMessage's posters, social suites, digital signage, presentations, banners, and table tents:

| Element | Treatment | Substitute |
|---|---|---|
| Headline (punchy) | Galaxie Polaris Condensed **Bold**, sentence case or ALL CAPS for short titles, tight leading | Arial Narrow Bold |
| Headline (elegant) | Galaxie Polaris **Light** at very large size, airy | Arial (regular), large |
| Subhead | Galaxie Polaris Light or Light Italic | Arial or Arial Italic |
| Eyebrow label | Small ALL CAPS sans, slightly letter-spaced; gold text, or white text on a small gold bar | Arial, bold or regular, +0.5–1pt tracking |
| Body | Galaxie Polaris Regular/Book | Arial |
| Department / unit name strip | Small sans, often bold, above a thin gold rule | Arial Bold |
| Ceremonial display | Garamond Premier, often spaced caps | Georgia |

Rules of thumb:

- **One display voice per piece.** Don't mix a serif headline with a sans headline.
- **Contrast comes from weight, not family:** bold condensed headline + light subhead + regular body.
- **Gold type is for small things** — eyebrows and short labels — never body copy.

### Typography for non-web deliverables

#### Presentations
- Title: Arial Narrow Bold (condensed-bold look) or large Arial in a light-looking regular weight
- Section labels / eyebrows: Arial, ALL CAPS, letter-spaced, gold or gray (`#555`)
- Body: Arial, regular, dark gray (`#333`) on white
- Title color: ND Blue `#0c2340` on white; white on ND Blue
- Serif titles (Georgia) only for ceremonial or formal decks
- Keep body text at a comfortable reading size — never shrink type to fit more on a slide

#### Word / documents
- Heading 1: Arial (or Arial Narrow Bold), 24–28pt, ND Blue
- Heading 2: Arial, 16–18pt, ND Blue
- Heading 3: Arial, 13–14pt, ND Blue, bold
- Eyebrow above section titles: Arial 9–10pt, ALL CAPS, letter-spaced, Dark Gold `#8c7535`
- Body: Arial 11pt, dark gray (`#333`), 1.4–1.5 line spacing
- Footnotes / captions: Arial 9pt, gray (`#555`)

#### Ceremonial pieces
- Georgia (or Garamond Premier) for the display line, often in spaced caps
- Sans for supporting details (date, location, RSVP)

### Web and software UI

Type on nd.edu sites and in software UI is governed by the Notre Dame Web Theme v4. Use the `nd-web-theme` skill (https://github.com/OIT-AI-Skills/nd-web-theme-conductor) for web font stacks, type scale, and heading styles rather than hand-building them from this file.

### Voice/tone alignment

- Galaxie Polaris (Arial) serves the **focused**, **motivating**, and **truthful** voice attributes — clear, confident, unornamented.
- Garamond (Georgia), used sparingly, carries the **timeless** attribute for the moments that call for ceremony.

---

<a id="reference-logos"></a>

## Reference: Logos


The University of Notre Dame uses several distinct marks. They are **not interchangeable** — picking the wrong one is one of the most common brand mistakes.

### The four official marks

#### 1. Academic Mark (the primary mark)

The shield-and-wordmark lockup. The shield contains symbolic imagery (the cross, open book with "Vita, Dulcedo, Spes," six-pointed star for Mary, wavy lines for the campus lakes). The wordmark reads "University of Notre Dame."

**Use it on:** All academic and administrative communications. This is the default ND mark — when in doubt, this is the one.

**Treat it as a signature:** The Academic Mark is an *endorsing* element, not the visual centerpiece. It typically lives in a corner, in a footer, on a back cover, or as a sign-off — it doesn't compete with the headline or the photo.

**Sizing rules:**
- **Maximum width: 25%** of the communication's total width. Larger than that and it stops feeling like a signature and starts feeling like a logo splash.
- **Minimum width:** Roughly 1 inch (72px) for print legibility, somewhat smaller for screen.
- **Clear space:** Maintain a margin around the mark equal to the height of the wordmark "Notre Dame" cap-height. No other elements (text, photos, lines) should cross this clear space.

**Color variants:**
- **Two-color (blue + gold) is the default.** Use it whenever full-color reproduction is available.
- **One-color (single ink)** is acceptable when production constraints require it (newspaper, embroidery, single-spot-color print). One-color doesn't mean the rest of the piece is monochrome — it just means the mark itself is.
- **Reverse (white on dark)** for placement on photographs or dark backgrounds. Only place it over low-contrast areas of a photo where it'll remain legible.

**Don't:**
- Substitute "University of Notre Dame" with a department or unit name in the wordmark
- Alter the colors (no purple Academic Mark, no rainbow Academic Mark, no metallic effects beyond the official gold)
- Apply drop shadows, glows, bevels, or other effects
- Place the mark over a photo area that would obscure it
- Use the older / formerly-acceptable version (the previous Academic Mark, with a different shield treatment, is retired)
- Stretch or skew the mark; always scale proportionally

#### 2. Monogram (the interlocking ND)

The bold, blocky ND mark. The University's most recognizable visual symbol.

**Use it on:** Non-academic units only. Athletics, campus services, alumni clubs, student groups.

**Do NOT use it on:** Academic or administrative communications. Even though it's beloved, the Monogram is reserved for non-academic contexts. Using it on a research report or a donor letter is a brand violation.

**Why this matters:** The Academic Mark and the Monogram serve different brand layers. The Academic Mark says "this is from the University." The Monogram says "this is from a community group within Notre Dame." Mixing them blurs the brand architecture.

#### 3. University Seal

Two versions exist: the **Latin seal** (1931 design, "Sigillum Universitatis Dominae Nostrae a Lacu") and the **English seal** (evolved through the 1950s, first trademarked in January 1963).

**Use it on:** Official University documents only. Diplomas, presidential communications, contracts, certain stationery, lecterns, ceremonial invitations, academic regalia.

**Do NOT use it on:** Routine communications, marketing materials, event flyers, websites, slide decks. The Seal is for "imprimatur" use — it adds authority to formal documents and loses meaning if used casually.

The **Latin seal** has the most restricted use — primarily President's Office, official contracts, diplomas. The **English seal** has slightly wider ceremonial use but still requires authorization for most applications. When in doubt about Seal use, contact OPAC.

#### 4. The Golden Dome

The Golden Dome is **a landmark, not a logo.** It is the most recognizable symbol of Notre Dame, and depicts the statue of Mary atop the Main Building. Treat it with the respect appropriate to a religious symbol — it represents Mary, not just "the campus."

**Acceptable uses:** Photographs of the Dome in its actual setting (atop the Main Building), used as imagery on appropriate communications.

**Avoid:**
- Treating the Dome as a graphic element to be cropped, recolored, or stylized
- Using a Dome silhouette as a generic substitute for an ND logo
- Placing the Dome in jokey or commercial contexts without thoughtful consideration
- Reproducing the Dome on merchandise without licensing approval

### Publicly hosted SVG assets

Four variants of the Notre Dame *wordmark* (the "University of Notre Dame" type-only lockup, without the shield) are available as public SVGs at stable URLs:

| URL | Fill color | Use on |
|---|---|---|
| `https://static.nd.edu/images/marks/blue/ndmark.svg` | `#121C2B` (deep navy) | Light backgrounds |
| `https://static.nd.edu/images/marks/gold/ndmark.svg` | `#E0D079` (light gold) | Dark backgrounds, photographic backgrounds |
| `https://static.nd.edu/images/marks/white/ndmark.svg` | `#FFFFFF` (white) | Dark backgrounds where gold would clash |
| `https://static.nd.edu/images/marks/gray/ndmark.svg` | `#121C2B` (gray) | Footer / muted contexts |

These render at 211×50 viewBox dimensions. Embed them in HTML deliverables with:

```html
<img src="https://static.nd.edu/images/marks/blue/ndmark.svg"
     alt="University of Notre Dame"
     width="200" height="48">
```

Or inline-fetch and embed as SVG markup if you need to recolor or animate them.

**Important:** These public SVGs are the **wordmark only** — they do not include the shield. They are appropriate for use as a typographic ND signature in headers, footers, or sign-offs. They are NOT a substitute for the full Academic Mark on materials where the Academic Mark is required.

For the full Academic Mark with the shield, users need to download from `onmessage.nd.edu/downloads/#logos`. This skill should not attempt to recreate the shield in code — it's an illustrated mark with specific approved artwork, and approximating it would be a brand violation.

### A monogram PNG asset is also publicly hosted

The interlocking ND monogram is available as a hosted PNG at:
- `https://static.nd.edu/images/monogram/gold/monogram-32.png` (32×32, gold)
- `https://static.nd.edu/images/monogram/gold/monogram-96.png` (96×96, gold)
- `https://static.nd.edu/images/monogram/gold/monogram-180.png` (180×180, gold)
- `https://static.nd.edu/images/monogram/monogram.svg` (vector, gray)

**Reminder:** the monogram is for non-academic units only. Don't use it on academic or administrative deliverables even though the asset is conveniently available.

### Custom unit logos

Many ND schools, colleges, institutes, and centers have custom logo lockups (Keough School lockup, Mendoza lockup, etc.). These are approved by Public Affairs and Communications and follow specific brand standards layered on top of the masterbrand.

If a user references a unit-specific logo this skill doesn't have:

1. Acknowledge the unit logo exists and that this skill doesn't ship it
2. Suggest they obtain the official lockup from their unit's communications lead or Notre Dame Creative
3. In the meantime, fall back to the Academic Mark + the unit name in body type

Don't invent or sketch unit-specific logos.

### Approval and contact

For questions about logo use, custom lockups, or anything outside this skill's coverage:

- General brand questions: `onmessage.nd.edu` and the Office of Public Affairs and Communications (OPAC)
- Custom logos: Notre Dame Creative, 574-631-4636
- Trademark / licensing: `licensing.nd.edu`
- University Seal questions: contact Tim Legge (per the official guidelines)

---

<a id="reference-voice"></a>

## Reference: Voice


Notre Dame's voice as published at `onmessage.nd.edu/university-branding/voice/`, with practical guidance for applying it to slide titles, headlines, donor copy, web hero sections, and event materials.

### The five voice attributes

ND's official voice personality has five attributes. Strong ND copy generally exhibits at least three of these.

#### 1. Focused

The message has clear hierarchy. One strong point rises to the top. The reader knows what they're being asked to remember or do — secondary information stays secondary.

**Practical tests:**
- Can you summarize the headline in one sentence?
- If the reader only saw the largest text on the page, would they get the point?
- Is there one *thing* the page is about, or is it trying to do five things at once?

#### 2. Timeless

The writing isn't trendy. It nods to ND's rich heritage and Catholic tradition without being archaic. It avoids slang, internet-isms, and language that will feel dated in five years.

**What to avoid:** "synergy," "leverage," "10x," "game-changer," "rockstar," exclamation-point-heavy enthusiasm, internet meme phrasing, hashtag-style copy.

**What to lean into:** Plain words. Concrete nouns. Sentences that could've been written 30 years ago and will still read well 30 years from now.

#### 3. Motivating

Copy should inspire action. It should be clear what the reader is being asked to do — apply, attend, give, read, watch, register. ND voice is not passive observation; it has momentum.

**Practical tests:**
- What does the reader do next?
- Is the call to action specific and named?
- Does the headline create energy, or does it just describe?

#### 4. Powerful

Bold statements capture attention. ND voice is comfortable making strong claims — about its mission, its impact, the work of its researchers and students. It doesn't hedge.

**What to avoid:** "We hope to," "We try to," "One of the leading," "Among the most," "We believe we may."

**What to lean into:** "We do." "We are." "We will." Direct claims that ND can back up with evidence.

#### 5. Truthful

Copy is rich with proof points and emotive stories. ND voice is bold but not vague — claims come paired with specifics: numbers, names, dates, places, outcomes. The "powerful" attribute without "truthful" becomes hyperbole; together they become credible.

**Practical tests:**
- For every strong claim, is there a specific supporting detail?
- Do you name people, places, programs, dollar amounts, dates?
- Could a skeptical reader find evidence, or are you asking them to take your word?

### Sample phrases (from the official guidelines)

These are exemplars cited in the OnMessage voice guide. They show what ND voice sounds like when it's working:

- "Creating the leaders the world needs."
- "Tackling the most enduring questions of our time."
- "We believe in the power research has to advance knowledge and impact lives."
- "Research is not just about numbers, data, or properties. It's about passion, faith, and truth."
- "A century-long tradition of always looking ahead."

Notice what these have in common: short, declarative, no hedging, concrete-but-evocative, and they could not have been written by any other university. The "passion, faith, and truth" line in particular is unmistakably Notre Dame — secular peers wouldn't write it.

### Eight qualities of ND copy

The official guidelines list eight qualities to aim for. They're all short adjectives because the brief itself is supposed to be short:

> Simple. Real. Direct. Useful. Clear. Approachable. Brief. Consistent.

Use these as a checklist on any draft. If a paragraph violates two of them, rewrite.

### Application by deliverable type

#### Slide titles
- 5–9 words. Sometimes one striking word.
- Title case or sentence case both fine; pick one and stick with it through the deck.
- Avoid full-sentence titles with periods — slide titles aren't sentences.
- Lead with the *takeaway*, not the topic. Not "Research Funding," but "Research funding grew 23% this year."

#### Headlines (web, flyers, posters)
- One idea per headline.
- Mix declarative ("We do X") with provocative ("What if X?") sparingly.
- The "powerful + truthful" combo works well: bold claim + a specific number or name nearby.

#### Hero copy / lede sentences
- 1–2 sentences setting up the page or section.
- More room than a headline to land a specific story or concrete proof point.
- Should leave the reader wanting the next paragraph, not summarize it away.

#### Donor / advancement copy
- Lean heavily on **truthful** — donors care about specifics. Names, dollar amounts, outcomes, photographs of real beneficiaries.
- "Powerful" claims work, but only when paired with proof.
- Avoid abstract aspiration without grounding ("transforming lives" without saying whose, how, or what changed).

#### Event invitations and announcements
- Lead with what + when + where, in that order.
- Then the *why* — one sentence on why the reader should care.
- Then the call to action — RSVP link, registration deadline, contact for questions.
- Resist the urge to over-design or over-write. ND event copy works best when it's almost spartan.

#### Calls to action
- Verb-first. "Apply now," "Register," "Read the full report," "Give today."
- Specific, not generic. "Learn more" is the weakest possible CTA — almost any alternative is better.
- One primary CTA per page or section. Multiple competing CTAs dilute focus.

### What to avoid

A short list of habits that consistently push copy *off* ND voice:

- **Marketing-speak buzzwords.** "Leverage," "synergy," "thought leader," "best-in-class," "world-class," "premier" (when self-applied), "innovative" (when used as a self-descriptor).
- **Hedging modifiers.** "One of the," "among the," "arguably," "it could be said." These sap power.
- **Trendy phrasing.** Internet abbreviations, current memes, sports-broadcast language ("game time," "next-level"), startup voice ("we're crushing it").
- **Generic enthusiasm.** Excessive exclamation points, "exciting," "amazing," "incredible" used as filler.
- **Pretension without substance.** Long Latinate words where short Anglo-Saxon ones would do. Sentences with three commas where two would do. Academic jargon in materials directed at non-academic audiences.
- **Hyperbole without proof.** "Transforming the world" is empty; "Trained 1,200 first-generation college students last year, of whom 89% earned degrees" is grounded.

### A few do/don't pairs

**Don't:** "Notre Dame is one of the leading research universities in the world."
**Do:** "Notre Dame's faculty led $260 million in funded research last year."

**Don't:** "Our amazing student community is so passionate about service!"
**Do:** "Last year, undergraduates volunteered 410,000 hours across 60 community partners."

**Don't:** "Discover how we're leveraging cutting-edge AI to transform education."
**Do:** "Our researchers are testing AI tutoring with 800 students in South Bend public schools."

**Don't:** "Click here to learn more."
**Do:** "Read the full 2026 research report."

**Don't:** "Welcome to the Notre Dame website!"
**Do:** "Notre Dame is a Catholic research university in northern Indiana."

### When this skill writes copy alongside visuals

Slide titles, flyer headlines, hero copy, and event subtitles all count as visuals-adjacent text. When generating these, default to ND voice attributes:

1. Cut adjectives. Test every modifier — does the sentence work without it?
2. Lead with a concrete noun or verb. Avoid abstractions in the first three words.
3. Pair every strong claim with a specific. If you can't find one, soften the claim.
4. Read it out loud. ND voice should feel like a confident person speaking, not a press release being read.
