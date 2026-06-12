import os
import httpx
from azure.cosmos import CosmosClient

# Read Aspire-injected environment variables
cosmos_uri = os.getenv("COSMOSDB_URI", "https://localhost:8081")
cosmos_key = os.getenv("COSMOSDB_KEY", "")
foundry_url = os.getenv("FOUNDRY_URL", "http://localhost:7000")

# Cosmos DB client
cosmos_client = CosmosClient(cosmos_uri, credential=cosmos_key)

async def run_agent_pipeline(agent_name: str, input_data: dict):
    """
    Orchestrates an agent run: fetches data from Foundry-local,
    stores results in Cosmos DB.
    """
    async with httpx.AsyncClient() as client:
        foundry_resp = await client.get(f"{foundry_url}/api/data")
        foundry_data = foundry_resp.json()

    db = cosmos_client.create_database_if_not_exists(id="AgentDB")
    container = db.create_container_if_not_exists(
        id="AgentRuns",
        partition_key="/id",
        offer_throughput=400
    )
    item = {
        "id": agent_name,
        "input": input_data,
        "foundry": foundry_data,
        "status": "completed"
    }
    container.upsert_item(item)

    return {"agent": agent_name, "result": item}

async def rag_query_pipeline(query: str):
    """
    Orchestrates a RAG query: retrieves docs from Foundry-local,
    stores query and answer in Cosmos DB.
    """
    async with httpx.AsyncClient() as client:
        docs_resp = await client.get(f"{foundry_url}/api/docs?q={query}")
        docs = docs_resp.json()

    db = cosmos_client.create_database_if_not_exists(id="RAGDB")
    container = db.create_container_if_not_exists(
        id="Queries",
        partition_key="/id",
        offer_throughput=400
    )
    item = {
        "id": query,
        "docs": docs,
        "answer": "stubbed answer from LLM"
    }
    container.upsert_item(item)

    return {"query": query, "answer": item["answer"], "docs": docs}
