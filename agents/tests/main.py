import os
import httpx
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict
import asyncio

# Import orchestrator functions
from core import run_agent_pipeline, rag_query_pipeline

app = FastAPI(title="ACSF Web API")

@app.get("/health")
def health():
    return {"status": "ok"}

class AgentRunRequest(BaseModel):
    agent: str
    input: Dict[str, Any]

@app.post("/agents/run")
async def run_agent(req: AgentRunRequest):
    # Call orchestrator pipeline
    result = await run_agent_pipeline(req.agent, req.input)
    return result

class RAGQuery(BaseModel):
    query: str

@app.post("/rag/query")
async def rag_query(q: RAGQuery):
    # Call orchestrator pipeline
    result = await rag_query_pipeline(q.query)
    return result
