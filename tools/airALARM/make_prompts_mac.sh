#!/bin/bash
set -euo pipefail
OUT="${1:-$PWD/airalarm_prompts}"
mkdir -p "$OUT"
VOICE="${AIRALARM_VOICE:-Lesya}"
if ! say -v '?' | grep -Fq "$VOICE"; then
  echo "Український голос '$VOICE' не встановлено. Перевірте: say -v '?' | grep -i 'uk\\|lesya'" >&2
  echo "Встановіть український голос у macOS System Settings > Accessibility > Spoken Content > System Voice." >&2
  exit 1
fi
for spec in 'alert|Увага! Повітряна тривога!' 'clear|Увага! Відбій повітряної тривоги!'; do
  name="${spec%%|*}"
  phrase="${spec#*|}"
  say -v "$VOICE" -o "$OUT/airalarm_${name}.aiff" "$phrase"
  afconvert -f WAVE -d LEI16@16000 -c 1 "$OUT/airalarm_${name}.aiff" "$OUT/airalarm_${name}.wav"
  rm "$OUT/airalarm_${name}.aiff"
  echo "Created $OUT/airalarm_${name}.wav"
done
