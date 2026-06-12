🔒 Security.md
Purpose
This document outlines security practices for developing and maintaining the Agentic Cybersecurity Framework (ACSF). It ensures contributors handle secrets, emulator keys, and hybrid inference responsibly.

1. Secrets Management
Never commit secrets (API keys, connection strings, tokens) to the repository.

Use .env.example to provide placeholders and document required variables.

Store real secrets in environment variables or secure vaults (e.g., Azure Key Vault, GitHub Actions secrets).

CI/CD pipelines must reference secrets via GitHub Actions secrets.* context.

2. Cosmos DB Emulator Keys
The Cosmos DB Emulator uses a development key for local testing.

This key is not secure and must never be used in production.

Replace emulator keys with production credentials when deploying to Azure Cosmos DB.

Document emulator usage clearly in README.md and infra/aspire/README.md.

3. Hybrid Inference Safeguards
Hybrid inference (Azure/OpenAI) is off by default.

To enable, set:

USE_HYBRID=true

AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY

Data privacy: Document what data is sent to cloud providers when hybrid mode is enabled.

Cost awareness: Note expected cost per request; contributors should avoid accidental large‑scale runs.

Testing: Keep retries and timeouts conservative to prevent cascading costs.

4. Model Files
Do not commit model binaries (e.g., GGML, HF weights).

Use .gitignore to exclude large files.

Provide instructions in README.md or foundry-windows-local/README.md for downloading models externally.

5. CI/CD Security
GitHub Actions workflow permissions must be set to Read & write only if automation requires branch updates.

Ensure automation accounts are added to branch protection allowlists if needed.

Run secrets scanning and linting in CI to prevent accidental leaks.

6. Contributor Guidelines
Always review PRs for accidental secrets or large files.

Include security notes in every PR body (as defined in the PR automation script).

Follow least‑privilege principles when granting access to CI/CD or orchestration environments.