#!/usr/bin/env bash
# For each lesson in lessons.md: how often /bgw-task-flow 2b asked it, how often it
# raised a finding, and how many asks since its last finding. A lesson asked LIMIT
# times since its last finding (or since it was added) is marked DELETE?.
# Usage: bash scripts/lesson-stats.sh [lessons-file] [analyses-folder]
#
# It reads the 2b lesson lines, one per lesson per challenge round:
#   - lesson (<source>): <finding id> - <why>
#   - lesson (<source>): does not apply - <why>
#   - lesson (<source>): not asked - <why>
# <source> is the lesson's parenthesis in lessons.md. Analysis files are read oldest
# first by modification time, lines in file order. "not asked" is not counted.

lessons=${1:-$HOME/.claude/bgw/lessons.md}
dir=${2:-$HOME/.claude/analyses}
limit=10

[ -f "$lessons" ] || { echo "No lessons file: $lessons"; exit 0; }
[ -d "$dir" ] || { echo "No analyses folder: $dir" >&2; exit 2; }

mapfile -t files < <(find "$dir" -name '*.md' -type f -printf '%T@ %p\n' | sort -n | cut -d' ' -f2-)

while IFS= read -r raw || [ -n "$raw" ]; do
  line=${raw%$'\r'}
  case $line in '- '*) ;; *) continue ;; esac

  if ! [[ $line =~ \(([^()]*)\)[[:space:]]*$ ]]; then
    echo "NO SOURCE  $line"; continue
  fi
  source=${BASH_REMATCH[1]}
  key="- lesson ($source): "

  asked=0 hits=0 since=0
  for f in "${files[@]}"; do
    while IFS= read -r hit; do
      [[ $hit == "$key"* ]] || continue
      status=${hit#"$key"}
      case $status in
        'not asked'*) ;;
        'does not apply'*) asked=$((asked + 1)); since=$((since + 1)) ;;
        *) asked=$((asked + 1)); hits=$((hits + 1)); since=0 ;;
      esac
    done < <(tr -d '\r' < "$f" | grep -F -- "$key")
  done

  mark="keep"
  [ "$since" -ge "$limit" ] && mark="DELETE?"
  printf '%-7s asked %d, hits %d, since last hit %d  (%s)\n' "$mark" "$asked" "$hits" "$since" "$source"
done < "$lessons"
