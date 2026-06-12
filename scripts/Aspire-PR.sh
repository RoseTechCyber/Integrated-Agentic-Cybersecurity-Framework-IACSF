#!/usr/bin/env bash
set -euo pipefail

REPO="RoseTechCyber/Agentic-Cybersecurity-Framework"
REVIEWER="RoseTechCyber"

TMPDIR="$(mktemp -d)"
echo "Using temp dir: $TMPDIR"

# PR bodies
cat > "$TMPDIR/data-integration.md" <<'EOF'
Adds a data-integration scaffold for Aspire orchestration.

Includes:
- Aspire.yml (Python backend, Cosmos DB emulator, Foundry-local, ServiceDefaults)
- connectors/ingest_cosmos.py (example ingestion to Cosmos emulator)
- README.md (Aspire orchestration guidance)

How to test (quick):
1. aspire up --file Aspire.yml --non-interactive
2. Wait for Cosmos emulator + Foundry-local to initialize
3. python connectors/ingest_cosmos.py --path sample_data

Security notes:
- Uses Cosmos emulator dev key for convenience; do not use this key in production.

PR checklist:
- [ ] ruff/flake8 linting passes
- [ ] pytest smoke passes
- [ ] No secrets committed (.env.example only)
- [ ] Aspire orchestration verified
EOF

cat > "$TMPDIR/agents.md" <<'EOF'
Adds a minimal reasoning agent scaffold and unit tests.

Includes:
- agents/reasoning_agent/core.py
- agents/orchestrator/runner.py (EchoPlugin demo)
- agents/tests/test_agent_basic.py
- agents/requirements.txt

How to test (quick):
1. python -m venv .venv && source .venv/bin/activate
2. pip install -r agents/requirements.txt
3. pytest agents/tests/test_agent_basic.py

PR checklist:
- [ ] ruff/flake8 linting passes
- [ ] pytest unit test(s) pass
- [ ] Requirements minimal and safe (no secrets)
EOF

cat > "$TMPDIR/web-app.md" <<'EOF'
Adds a FastAPI backend skeleton (RAG & agent endpoints) wired to core orchestrator.

Includes:
- web-app/backend/main.py (endpoints: /health, /agents/run, /rag/query)
- core.py (pipelines: run_agent_pipeline, rag_query_pipeline)
- web-app/backend/requirements.txt
- web-app/README.md

How to test (quick):
1. aspire up --file Aspire.yml --non-interactive
2. uvicorn web-app.backend.main:app --reload --host 0.0.0.0 --port 5000
3. Test endpoints: GET /health, POST /agents/run, POST /rag/query

Security notes:
- Environment variables (COSMOSDB_URI, COSMOSDB_KEY, FOUNDRY_URL) injected by Aspire.yml
- No secrets committed; use .env.example

PR checklist:
- [ ] Lint
- [ ] Unit-test smoke
- [ ] Aspire orchestration documented
EOF

cat > "$TMPDIR/infra.md" <<'EOF'
Adds infra scaffolding including CI workflow and Aspire integration.

Includes:
- .github/workflows/ci.yml (lint, test, docker-smoke, aspire-integration)
- scripts/dev_setup.sh (Linux)
- scripts/dev_setup.ps1 (Windows)
- infra/aspire/README.md (Aspire orchestration notes)

How to test (quick):
1. Run the CI on this PR to validate workflow triggers
2. aspire up --file Aspire.yml locally to verify orchestration
3. Review infra/aspire/README.md for guidance

PR checklist:
- [ ] CI workflow triggered and ran on PR
- [ ] ruff/flake8 linting step included
- [ ] No credentials or secrets added
- [ ] Documentation for Aspire orchestration validated
EOF

# Branches and titles
declare -A BRANCH_TITLE=(
  ["data-integration"]="scaffold: Aspire data-integration (Cosmos emulator, Foundry-local)"
  ["agents"]="scaffold: agents (reasoning agent core, orchestrator, tests)"
  ["web-app"]="scaffold: web-app backend wired to core orchestrator"
  ["infra"]="scaffold(infra): CI workflow + Aspire integration"
)

declare -A BRANCH_BODYFILE=(
  ["data-integration"]="$TMPDIR/data-integration.md"
  ["agents"]="$TMPDIR/agents.md"
  ["web-app"]="$TMPDIR/web-app.md"
  ["infra"]="$TMPDIR/infra.md"
)

# Create PRs
for branch in "${!BRANCH_TITLE[@]}"; do
  echo "Creating PR for branch: $branch"
  if gh api repos/"$REPO"/branches/"$branch" > /dev/null 2>&1; then
    gh pr create --repo "$REPO" --base main --head "$branch" \
      --title "${BRANCH_TITLE[$branch]}" \
      --body-file "${BRANCH_BODYFILE[$branch]}" \
      --add-reviewer "$REVIEWER" || {
      echo "gh pr create failed for $branch"
    }
  else
    echo "Remote branch $branch does not exist. Skipping."
  fi
done

echo "Done. Temp files are in $TMPDIR (remove when done)."
