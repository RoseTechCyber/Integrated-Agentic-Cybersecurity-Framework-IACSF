<p align="center">
  <!-- Existing project logo -->
  <img src="/iACSF-logo.png" alt="Integrated Agentic Cybersecurity Framework" height="200" width="400">

  <!-- MSBuild logo -->
  <img src="/MSBuild.PNG" alt="Microsoft Build 2026" height="200" width="300">

  <!-- Hackathon League logo -->
  <img src="/hack-league.jpg" alt="Hackathon League 2026" height="200" width="200">
</p>

# Integrated-Agentic-Cybersecurity-Framework-IACSF
All-in-One Holistic AI Agentic Cybersecurity Framework tailored for a more proactive protection across the Information  Technology(IT) Layers covering Infrastructures, Platforms, Applications and Data.  Practical Hands-On Security Tools that must align with the  Standard  Cybersecurity Frameworks such as ISO 27001, CIS, ISO 42001, Microsoft Cybersecurity Benchmark(MCSB).

# Agentic-Cybersecurity-Research-and-Monitoring-Center
Tailoured to align with the IACSF as an Enforcer that ensures that the holistic Comtrols documented in the IACSF are implemented with the necessary Security tools for a sustainable, more resilient and more proactively  Secured Security Posture. The Security tools would be applied across the layers with necessary Agentic respomses and alerts. 

# Agentic-eLearning-Security-Management-System
Tailoured to further inspire Stakeholders, Employees, Security Policy Enforcers, End-Users, IT Professionals, Students and Clients to seamless Artificual Intelligence(AI) Agentic driven e-Learning Security Management System with necessary Certifications, Labs, Self-assessments and Certification curriculum in mind.

# The Workflow
The Agentic Security Research Center and Agentic eLearning Security Management System depend on the Integrated Agentic Cybersecurity Framework(IACSF) to run a trendy, productive  and result-oriented Agentic Security Research Center to ensure that ALL stakeholders are trained and governed with the necessary knwpledgeable tasks across the Security domains with  necessary Certifications well endorsed.

A modular framework for reasoning agents, RAG pipelines, and hybrid inference, orchestrated with **Aspire**
and the Integrated Agentic Ctversecurity Framework(IACSF) as the Main Orchestrator that must be running seamless Research Center and finally the eLearning Management System.

# Workflow Tools and Hosting Envronment
The AI Reasoning Agents such as Work IQ, Web IQ, and Foundty IQ, Azure-CosmosDB-Emulator, RAG/Vector Search, Foundry-Local, Aspire, are applied within each branch and across branches for a tightly coupled chain of Agentic Workfkows.

# Collaborators
Copilot Chat, GitHub-Copilot, Copliot Office 365.

🌐 Core Services 
Aspire Hosting Service

Acts as the orchestrator for your projects.

Manages lifecycle (start/stop) and ensures dependencies (like Cosmos Emulator) are available before WebApp runs.

Aspire Orchestration Service

Handles coordination between multiple projects (e.g., WebApp calling API).

Ensures correct startup order (Cosmos Emulator → API → WebApp).

Aspire Alerting/Monitoring Service

Triggers alerts when health checks fail, or when resource usage crosses thresholds.

Can integrate with logging providers (e.g., Application Insights, Prometheus).

⚡ Supporting Infrastructure
Foundry Service Integration

Use Aspire’s orchestration to deploy your WebApp into Foundry.

Foundry handles hosting, Aspire ensures it’s wired correctly with dependencies.

Azure Cosmos DB Emulator

Run locally in Docker.

Aspire configures connection strings for your WebApp so it points to the emulator in dev/test.

Docker Service

Aspire can orchestrate containers (WebApp + Cosmos Emulator).

Use docker-compose or Aspire’s container orchestration to spin them up together.

📂 Typical Setup Flow
Define Aspire Manifest

Register services: WebApp, CosmosEmulator, FoundryHost.

Set dependencies (WebApp depends on CosmosEmulator).

Configure alerts (e.g., if CosmosEmulator is unreachable, trigger alert).

Configure Alerts

Health checks for WebApp and API endpoints.

Resource monitoring (CPU/memory thresholds).

Integration with email/Slack/Teams for notifications.

Run Locally

Aspire spins up Docker containers.

Cosmos Emulator runs in one container, WebApp in another.

Foundry service hosts WebApp when deployed.

✅ Proof of Concept Run
Aspire orchestration: run Cosmos Emulator, WebApp, and Python agent together.

Agent ingestion: load JSON frameworks into Cosmos containers with embeddings.

User query: send a natural language question.

Vector search: Cosmos returns relevant controls.

Generative model: Foundry service produces a RAG answer using retrieved context.

This PoC shows the end‑to‑end pipeline: JSON frameworks → Cosmos NoSQL containers → embeddings → Aspire orchestration → Foundry generative model → contextual answers.

This PoC demonstrates:

JSON frameworks stored in Cosmos NoSQL containers.

Embeddings created and stored.

Vector search retrieving relevant controls.

Aspire orchestrating Cosmos + WebApp + Python agent together.

[Watch the demo video](https://www.youtube.com/watch?v=your_video_id)



## 🚀 Quick Start

### 1. Dev Setup
- On Linux: run `scripts/dev_setup.sh`
- On Windows: run `scripts/dev_setup.ps1`

This installs Python, Docker, .NET SDK, Aspire CLI, and project dependencies.

### 2. Orchestration
Spin up services with Aspire:
```bash
aspire up --file Aspire.yml --non-interactive
This starts:

Cosmos DB Emulator

Foundry-local

FastAPI backend (main.py)

ServiceDefaults

3. Running the Backend
API service (default):

bash
python web-app/backend/main.py
Endpoints:

GET /health

POST /agents/run

POST /rag/query

Demo orchestrator:

bash
python runner.py
Runs the EchoPlugin demo without API endpoints.

🔧 Choosing Between main.py and runner.py
Use main.py when you want to expose API endpoints for agents and RAG queries. This is the default entry point in Aspire.yml and CI/CD.

Use runner.py when you want to run lightweight demos or test plugins locally without the API. Aspire.yml can be switched to run runner.py by changing the command field.

📂 Project Structure
agents/ → Reasoning agent core + orchestrator plugins

web-app/backend/ → FastAPI backend (API endpoints)

core.py → Orchestrator pipelines (agent runs + RAG queries)

runner.py → Demo orchestrator (EchoPlugin example)

Aspire.yml → Service orchestration (Cosmos DB Emulator, Foundry-local, backend)

scripts/ → Dev setup scripts (Linux + Windows)

.github/workflows/ci.yml → CI/CD pipeline (lint, test, Aspire integration)

🔒 Security Notes
Cosmos DB Emulator uses a dev key — do not use in production.

No secrets or model binaries are committed. Use .env.example for environment variables.

Hybrid inference (Azure/OpenAI) is off by default. Enable by setting USE_HYBRID=true and providing AZURE_OPENAI_ENDPOINT + AZURE_OPENAI_KEY.

📘 Implementation Guide
See Implementation.md for detailed architecture, including:

Agent plugin design

RAG pipeline flow

Aspire orchestration

CI/CD integration

Code

---

## 📑 Supporting Docs

- **`web-app/README.md`** → Focused on FastAPI backend usage, endpoints, and hybrid inference client.  
- **`Security.md`** → Expanded notes on secrets management, emulator keys, and hybrid inference safeguards.  
- **`Implementation.md`** → Detailed architecture guide 

---
Proof-of-Concept
