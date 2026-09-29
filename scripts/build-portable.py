#!/usr/bin/env python3
"""Build notre-dame-brand-portable.md at the repo root from the skill folder.

Merges SKILL.md and every file in references/ into one self-contained
Markdown file for agents that can't load folder-based skills. Links to
reference files are rewritten as in-document anchors. Deterministic:
run it after any edit to the skill and commit the result.

Usage:  python3 scripts/build-portable.py [--check]
  --check  exit 1 if the committed portable file is out of date
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / ".github" / "skills" / "notre-dame-brand"
OUT = ROOT / "notre-dame-brand-portable.md"
# Order the reference sections appear in the portable file.
REF_ORDER = ["colors", "typography", "logos", "voice"]


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit("SKILL.md is missing YAML frontmatter")
    meta = dict(
        line.split(":", 1) for line in m.group(1).splitlines() if ":" in line
    )
    return {k.strip(): v.strip() for k, v in meta.items()}, text[m.end():]


def anchor(name):
    return f"reference-{name}"


def rewrite_links(text):
    # [`references/x.md`](./references/x.md) -> [Reference: x](#reference-x)
    text = re.sub(
        r"\[`?references/(\w+)\.md`?\]\(\./references/\1\.md\)",
        lambda m: f"[the {m.group(1).capitalize()} reference](#{anchor(m.group(1))})",
        text,
    )
    # any remaining bare `references/x.md`
    return re.sub(
        r"`references/(\w+)\.md`",
        lambda m: f"[the {m.group(1).capitalize()} reference](#{anchor(m.group(1))})",
        text,
    )


def demote(text):
    # Push every heading down one level so each file nests under a section.
    return re.sub(r"^(#{1,5}) ", r"#\1 ", text, flags=re.M)


def build():
    meta, body = split_frontmatter((SKILL_DIR / "SKILL.md").read_text())
    refs = sorted(p.stem for p in (SKILL_DIR / "references").glob("*.md"))
    ordered = [r for r in REF_ORDER if r in refs] + [r for r in refs if r not in REF_ORDER]

    parts = [
        "# Notre Dame Brand — Portable Skill\n",
        "> Single-file version of the `notre-dame-brand` skill for agents that can't "
        "load folder-based skills (Gemini, ChatGPT, Copilot chat, etc.). Paste the "
        "whole file into the system prompt or context window.\n>\n"
        "> **Generated file — do not edit by hand.** Source: "
        "`.github/skills/notre-dame-brand/`. Regenerate with "
        "`python3 scripts/build-portable.py`.\n",
        f"**When to use:** {meta.get('description', '')}\n",
        "**Contents:** [Skill](#skill) · "
        + " · ".join(f"[{r.capitalize()}](#{anchor(r)})" for r in ordered)
        + "\n",
        "---\n",
        '<a id="skill"></a>\n',
        "## Skill\n",
        demote(rewrite_links(re.sub(r"^# .*\n", "", body.strip(), count=1))) + "\n",
    ]
    for r in ordered:
        text = (SKILL_DIR / "references" / f"{r}.md").read_text().strip()
        # Replace the file's own H1 with a section heading.
        text = re.sub(r"^# .*\n", "", text, count=1)
        parts += [
            "---\n",
            f'<a id="{anchor(r)}"></a>\n',
            f"## Reference: {r.capitalize()}\n",
            demote(rewrite_links(text)) + "\n",
        ]
    return "\n".join(parts)


if __name__ == "__main__":
    content = build()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text() != content:
            sys.exit("notre-dame-brand-portable.md is out of date — run scripts/build-portable.py")
        print("Portable file is up to date.")
    else:
        OUT.write_text(content)
        print(f"Wrote {OUT.relative_to(ROOT)} ({len(content.splitlines())} lines)")
