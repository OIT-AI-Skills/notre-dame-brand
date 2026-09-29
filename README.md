# notre-dame-brand

A portable agent skill that applies University of Notre Dame masterbrand standards — colors, typography, logos, and voice — to any visual or written deliverable connected to the University. For web pages and software UI it hands off to the `nd-web-theme` skill.

It uses the open, folder-based skill format — a directory with a `SKILL.md` (YAML frontmatter + Markdown instructions) and optional reference files — so it works with any agent or AI tool that supports skills, regardless of model provider. For tools that don't, there's a single-file version you can paste into any chat or system prompt.

Sourced from the official OnMessage guidelines (`onmessage.nd.edu`) and calibrated against the OnMessage template library (`onmessage.nd.edu/downloads/templates/`). Use it for slides, decks, posters, flyers, one-pagers, social graphics, signage, event materials, donor or alumni communications, diagrams, and reports for academic and administrative units (Keough, Mendoza, OIT, OPAC, ND Research, etc.).

## What this skill is for

Notre Dame has several brand layers. This skill covers the **University masterbrand** — the layer most communications should sit in.

| Use this skill for | Use something else for |
|---|---|
| Academic units (Keough, Mendoza, College of Arts & Letters, ND Research) | Athletics — different brand system; see `onmessage.nd.edu/athletics-branding/` |
| Administrative units (OIT, OPAC, HR, Campus Services) | AI@ND / AI Enablement — use the sibling `ai-nd-brand` skill, which inherits from this one but adds its own dark-first visual language |
| General University communications, donor & alumni materials, event materials | Web pages, nd.edu / Conductor sites, software UI — use [`nd-web-theme`](https://github.com/OIT-AI-Skills/nd-web-theme-conductor) |
| Posters, social graphics, signage, presentations, documents | Sub-brands or units with their own approved lockup |

If you're unsure, default to this skill — it's almost always correct.

## What's in here

```
nd-brand-skill/
├── README.md                          This file
├── notre-dame-brand-portable.md       Single-file (flattened) version of the skill —
│                                      generated, don't edit by hand
├── .github/
│   ├── skills/
│   │   ├── notre-dame-brand/          ← the skill
│   │   │   ├── SKILL.md               Router — when to apply, core signals, template
│   │   │   │                          look, deliverable guidance, web handoff
│   │   │   └── references/
│   │   │       ├── colors.md          Full palette + light/dark balance guidance
│   │   │       ├── typography.md      Sans-led system (Galaxie Polaris → Arial), serif
│   │   │       │                      as ceremonial accent, template type patterns
│   │   │       ├── logos.md           Academic Mark vs. Monogram vs. Seal vs. Golden
│   │   │       │                      Dome, sizing rules, hosted SVG asset URLs
│   │   │       └── voice.md           Voice attributes, sample phrases, do/don't pairs
│   │   └── skill-template/            Starter template for new skills in this repo
│   └── workflows/validate-skills.yml  CI: validates skill metadata + portable file
├── scripts/
│   ├── validate-skills.sh             Checks frontmatter / name-matches-folder rules
│   └── build-portable.py              Regenerates notre-dame-brand-portable.md
└── tests/legacy-outputs/              Sample outputs from the previous (serif-led)
                                       version of the skill, kept for comparison
```

`SKILL.md` is the entry point and links to the reference files by relative path. The reference files are deep dives — read them when the matching section of `SKILL.md` points there.

Web pages, nd.edu / Conductor sites, and software UI are handled by the companion **[`nd-web-theme`](https://github.com/OIT-AI-Skills/nd-web-theme-conductor)** skill. This skill tells the model to hand off to it (and to recommend installing it if it's missing).

## The three core signals

Notre Dame's brand boils down to three signals that should appear together in any on-brand deliverable:

1. **ND Blue (`#0c2340`) and ND Gold, with gold used sparingly.** Use Bright Gold (`#d39f10`) on screen — the metallic gold (`#ae9142`) reproduces poorly digitally. Reading surfaces are light; ND Blue fields are for covers and promotional pieces; nothing goes darker than ND Blue.
2. **Sans-serif-led type.** Galaxie Polaris (fallback **Arial** / **Arial Narrow**) for headlines and body. Garamond Premier (fallback **Georgia**) only as a ceremonial accent.
3. **Academic Mark used as a signature.** Corner placement, never centered, never wider than 25% of the deliverable's width.

If a piece carries all three, it reads as Notre Dame.

## How to install

The skill is just the folder `.github/skills/notre-dame-brand/`. Any agent that supports the `SKILL.md` format can use it; the steps are the same everywhere:

1. **Copy (or symlink) the folder** into your tool's skills directory, keeping the folder name `notre-dame-brand`. Common locations:

   | Scope | Typical path |
   |---|---|
   | Shared across agents (user-level) | `~/.agents/skills/notre-dame-brand/` |
   | Tool-specific (user-level) | `~/.<tool>/skills/notre-dame-brand/` — check your tool's docs |
   | Per-repository | `.github/skills/notre-dame-brand/` or `.agents/skills/notre-dame-brand/` in the repo you're working in |

   ```bash
   cp -R .github/skills/notre-dame-brand ~/.agents/skills/notre-dame-brand
   ```

2. **Or upload it**, for hosted chat apps that accept skills as an upload: zip the folder so `SKILL.md` sits at the root of the archive and upload it through the app's skill settings.

3. **Start a new session.** The agent discovers the skill from its frontmatter `description` and loads `SKILL.md` — and then the reference files it links to — only when a request matches.

Many tools also discover skills in `.github/skills/` automatically when you have this repository open.

## Portable single-file version

For any chat assistant, agent, or model that can't load folder-based skills, use the flattened file at the top of this repo:

**[`notre-dame-brand-portable.md`](./notre-dame-brand-portable.md)**

It merges `SKILL.md` and all four reference files into one self-contained document, with in-document anchor links replacing cross-file references. Paste the whole thing into a system prompt, custom instructions, a project/knowledge file, or the start of a conversation; it behaves the same way minus on-demand loading.

The portable file is **generated** — don't edit it by hand. After changing anything in the skill folder:

```bash
python3 scripts/build-portable.py        # regenerate
python3 scripts/build-portable.py --check  # verify it's current (CI runs this)
```

CI fails if the portable file is out of date, so the two can't drift apart.

## Quick examples of when this skill should fire

| User says | Skill applies? |
|---|---|
| "Build me an HTML mockup for a new ND research initiative landing page" | ↪️ Hands off to `nd-web-theme` |
| "Make this flyer look like Notre Dame" | ✅ Yes |
| "Draft a donor update deck for the Mendoza College" | ✅ Yes |
| "Use the ND web theme for this dashboard" | ↪️ Hands off to `nd-web-theme` |
| "Create a slide deck for the AI@ND showcase" | ❌ No — use `ai-nd-brand` |
| "Design a Notre Dame football social post" | ❌ No — athletics has a separate brand system |
| "What's a good color palette for a startup?" | ❌ No — not ND-related |

## Limitations and gaps

This skill is a *working subset* of ND's full identity system, not the complete one. It does not cover:

- Stationery, name badges, or email signatures
- Trademark licensing and merchandise approvals
- Athletic co-branding rules
- Custom unit lockups (Keough School lockup, Mendoza lockup, etc.) — these exist but are not bundled here

When something falls outside the skill's coverage, the right behavior is to (1) reason from the three core signals, (2) defer to `onmessage.nd.edu` for canonical answers, and (3) point users to Notre Dame Creative or OPAC for approval questions. Don't invent permissions or fabricate unit-specific lockups.

## Sources

- **Visual identity**: `onmessage.nd.edu/university-branding/`
- **Templates (look and feel)**: `onmessage.nd.edu/downloads/templates/` (ND sign-in required)
- **Web theme skill**: `https://github.com/OIT-AI-Skills/nd-web-theme-conductor`
- **Logo / asset downloads**: `onmessage.nd.edu/downloads/#logos`
- **Publicly hosted wordmark SVGs**: `static.nd.edu/images/marks/{blue,gold,white,gray}/ndmark.svg`

For brand questions outside this skill's coverage:

- General brand & approval questions: Office of Public Affairs and Communications (OPAC)
- Custom unit logos: Notre Dame Creative, 574-631-4636
- Trademark and licensing: `licensing.nd.edu`
- University Seal use: contact OPAC directly

## Versioning

Brand standards evolve. If `onmessage.nd.edu` updates color values, type recommendations, mark guidance, or voice attributes, update the relevant reference file under `.github/skills/notre-dame-brand/references/` and run `python3 scripts/build-portable.py`. Treat OnMessage as the source of truth; this skill is a working translation of it for AI-assisted production work.