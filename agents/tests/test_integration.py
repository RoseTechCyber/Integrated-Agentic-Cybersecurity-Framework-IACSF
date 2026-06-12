import os
import pytest
import httpx

# Default backend URL (Aspire exposes Python app on port 5000)
backend_url = os.getenv("BACKEND_URL", "http://localhost:5000")

@pytest.mark.asyncio
async def test_agents_run_pipeline():
    payload = {
        "agent": "summarizer",
        "input": {"task": "summarize report"}
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{backend_url}/agents/run", json=payload)
        assert response.status_code == 200, f"Unexpected status: {response.status_code}"
        data = response.json()
        # Validate structure
        assert "agent" in data
        assert "result" in data
        assert data["agent"] == "summarizer"
        # Cosmos DB + Foundry-local integration should yield dict
        assert isinstance(data["result"], dict)

@pytest.mark.asyncio
async def test_rag_query_pipeline():
    payload = {"query": "What is Aspire?"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{backend_url}/rag/query", json=payload)
        assert response.status_code == 200, f"Unexpected status: {response.status_code}"
        data = response.json()
        # Validate structure
        assert "query" in data
        assert "answer" in data
        assert "docs" in data
        assert data["query"] == "What is Aspire?"
        # Docs should be a list (from Foundry-local)
        assert isinstance(data["docs"], list)
