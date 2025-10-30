#!/bin/bash

TOTAL=10000
BATCH=1000

echo "🚀 Starting $TOTAL commits in batches of $BATCH..."

for ((b=1; b<=TOTAL; b++)); do
  echo "Commit number $b at $(date)" >> commit_log.txt
  git add commit_log.txt
  git commit -m "Auto commit #$b"

  # Push every 1000 commits to avoid timeout
  if (( b % BATCH == 0 )); then
    git push origin main
    echo "✅ Pushed batch $((b/BATCH)) ($b commits total)"
  fi
done

echo "✅ All $TOTAL commits done!"
git push origin main
