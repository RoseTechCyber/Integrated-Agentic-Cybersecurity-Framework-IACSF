📘 Implementation Guide (Aligned with Aspire PR Script)
Purpose
This guide provides concrete implementation details and step‑by‑step instructions for maintainers applying scaffolding across the repository. It aligns directly with the PR bodies defined in the automation script, ensuring consistency between local development, CI/CD, and Aspire orchestration.

Branches Covered
data-integration

agents

web-app

infra

General PR and CI Checklist
[ ] Linting: ruff/flake8 configured; CI fails PRs on lint errors.

[ ] Tests: include at least a smoke pytest job (pytest -q).

[ ] Secrets: never commit secrets; include .env.example.

[ ] Model files: do NOT commit binaries; use .gitignore.

[ ] Aspire orchestration: confirm aspire up --file Aspire.yml works locally and in CI.

[ ] PR body: must include run/test steps, security notes, and checklist.

Branch‑by‑Branch Details
Data‑Integration
Purpose: Aspire orchestration scaffold for ingestion workflows.

Key files: Aspire.yml, connectors/ingest_cosmos.py, README.md.

Local run steps:

aspire up --file Aspire.yml --non-interactive

Wait for Cosmos emulator + Foundry-local to initialize

python connectors/ingest_cosmos.py --path sample_data

Security: Cosmos emulator uses a dev key — replace before production.

CI checks: Aspire orchestration smoke test.

Agents
Purpose: Reasoning agent core, orchestrator plugins, unit tests.

Key files: agents/reasoning_agent/core.py, agents/orchestrator/runner.py, agents/tests/test_agent_basic.py, agents/requirements.txt.

Local run steps:

python -m venv .venv && source .venv/bin/activate

pip install -r agents/requirements.txt

pytest agents/tests/test_agent_basic.py

Implementation notes:

Keep AgentPlugin API minimal.

Plugins should be stateless or clearly declare state.

CI checks: pytest + linting.

Web‑App
Purpose: FastAPI backend wired to core orchestrator (agents + RAG).

Key files: web-app/backend/main.py, core.py, web-app/backend/requirements.txt, web-app/README.md.

Local run steps:

aspire up --file Aspire.yml --non-interactive

uvicorn web-app.backend.main:app --reload --host 0.0.0.0 --port 5000

Test endpoints: GET /health, POST /agents/run, POST /rag/query

Security: Environment variables (COSMOSDB_URI, COSMOSDB_KEY, FOUNDRY_URL) injected by Aspire.yml.

CI checks: lint + smoke test for /health.

Infra
Purpose: CI workflows, dev setup scripts, Aspire orchestration notes.

Key files: .github/workflows/ci.yml, scripts/dev_setup.sh, scripts/dev_setup.ps1, infra/aspire/README.md.

Local run steps:

Run scripts/dev_setup.sh (Linux) or scripts/dev_setup.ps1 (Windows).

aspire up --file Aspire.yml locally to verify orchestration.

CI checks:

Lint, test, docker‑smoke, Aspire orchestration.

Security: No credentials or secrets added.

Next Steps
Expand agent plugin examples and add E2E tests (ingestion → retrieval → response).

Add GPU server examples (vLLM/TGI) in infra/gpu.

Add security hardening: secrets scanning, pre‑commit hooks, CI gating for large files.

Maintainers
Repository owner: @RoseTechCyber

Infra & CI: @RoseTechCyber