#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$ROOT_DIR/.github/skills"

if [[ ! -d "$SKILLS_DIR" ]]; then
  echo "No skills directory found at: $SKILLS_DIR"
  exit 1
fi

shopt -s nullglob
skill_files=("$SKILLS_DIR"/*/SKILL.md)
shopt -u nullglob

if [[ ${#skill_files[@]} -eq 0 ]]; then
  echo "No SKILL.md files found under $SKILLS_DIR"
  exit 1
fi

errors=0

for skill_file in "${skill_files[@]}"; do
  skill_dir="$(dirname "$skill_file")"
  folder_name="$(basename "$skill_dir")"
  first_line="$(head -n 1 "$skill_file" | tr -d '\r')"
  closing_count="$(tail -n +2 "$skill_file" | tr -d '\r' | grep -c '^---$' || true)"

  if [[ "$first_line" != '---' || "$closing_count" -lt 1 ]]; then
    echo "ERROR: Missing YAML frontmatter markers in $skill_file"
    errors=$((errors + 1))
    continue
  fi

  name_line="$(grep -E '^name:[[:space:]]*[a-z0-9-]+' "$skill_file" | head -n 1 || true)"
  desc_line="$(grep -E '^description:[[:space:]]*.+$' "$skill_file" | head -n 1 || true)"

  if [[ -z "$name_line" ]]; then
    echo "ERROR: Missing or invalid 'name' field in $skill_file"
    errors=$((errors + 1))
    continue
  fi

  if [[ -z "$desc_line" ]]; then
    echo "ERROR: Missing 'description' field in $skill_file"
    errors=$((errors + 1))
  fi

  name_value="$(echo "$name_line" | sed -E 's/^name:[[:space:]]*//' | tr -d '\r')"

  if [[ "$name_value" != "$folder_name" ]]; then
    echo "ERROR: name '$name_value' does not match folder '$folder_name' in $skill_file"
    errors=$((errors + 1))
  fi

  if [[ ! "$name_value" =~ ^[a-z0-9-]{1,64}$ ]]; then
    echo "ERROR: name '$name_value' must match ^[a-z0-9-]{1,64}$ in $skill_file"
    errors=$((errors + 1))
  fi
done

if [[ $errors -gt 0 ]]; then
  echo "Validation failed with $errors error(s)."
  exit 1
fi

echo "All skills passed validation."
