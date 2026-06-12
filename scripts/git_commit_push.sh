#!/usr/bin/env bash
set -euo pipefail

# Usage: ./scripts/git_commit_push.sh "Your commit message"

if [ $# -eq 0 ]; then
  echo "Error: Please provide a commit message."
  echo "Usage: $0 \"Your commit message\""
  exit 1
fi

COMMIT_MSG="$1"

echo "Adding all changes..."
git add -A

echo "Committing with message: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

echo "Pushing to origin main..."
git push origin main

echo "✅ Code committed and pushed successfully."
