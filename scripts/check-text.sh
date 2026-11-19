#!/usr/bin/env bash
# Checks for text-only changes (skills, docs), where no test suite exists.
# Usage: bash scripts/check-text.sh <spec-file>   (paths resolve from the current directory)
#
# Spec lines, one check each; blank lines and lines starting with # are skipped:
#   =N FILE PHRASE   PHRASE occurs exactly N times in FILE. Fixed string, not a regex.
#                    FILE is read as one line: \r removed, line breaks and runs of
#                    spaces become one space, so a phrase may cross a wrapped line.
#   @N FILE TEXT     line N of FILE is exactly TEXT (\r removed).
# FILE has no spaces; a leading ~/ means $HOME. PHRASE and TEXT run to the end of the line.
# Exit code: 0 when every check passes, 1 when any fails, 2 on a bad spec.

spec=$1
[ -f "$spec" ] || { echo "usage: bash scripts/check-text.sh <spec-file>" >&2; exit 2; }

joined() { tr -d '\r' < "$1" | tr '\n' ' ' | tr -s ' '; }

pass=0 fail=0 lineno=0
while IFS= read -r raw || [ -n "$raw" ]; do
  lineno=$((lineno + 1))
  line=${raw%$'\r'}
  case $line in ''|'#'*) continue ;; esac

  kind=${line%% *}; rest=${line#* }
  file=${rest%% *}; text=${rest#* }
  case $file in '~/'*) file=$HOME/${file#'~/'} ;; esac
  n=${kind:1}

  if [ "$rest" = "$line" ] || [ "$text" = "$rest" ] || ! [[ $n =~ ^[0-9]+$ ]]; then
    echo "BAD SPEC line $lineno: $line" >&2; exit 2
  fi
  if [ ! -f "$file" ]; then
    echo "FAIL  missing file: $file"; fail=$((fail + 1)); continue
  fi

  case ${kind:0:1} in
    =)
      got=$(grep -oF -- "$text" <<< "$(joined "$file")" | wc -l | tr -d ' ')
      what="=$n $file: $text" ;;
    @)
      got_line=$(sed -n "${n}p" "$file" | tr -d '\r')
      [ "$got_line" = "$text" ] && got=$n || got="'$got_line'"
      what="@$n $file" ;;
    *) echo "BAD SPEC line $lineno: $line" >&2; exit 2 ;;
  esac

  if [ "$got" = "$n" ]; then
    echo "PASS  $what"; pass=$((pass + 1))
  else
    echo "FAIL  $what (got $got)"; fail=$((fail + 1))
  fi
done < "$spec"

echo "$pass passed, $fail failed"
[ "$fail" = 0 ]
