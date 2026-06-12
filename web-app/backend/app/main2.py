import os
import httpx
from fastapi import FastAPI

app = FastAPI(title="Integrated Agentic Cybersecurity Framework Web API")

foundry_url = os.getenv("FOUNDRY_URL", "http://foundry-local:7000")

@app.get("/foundry/data")
async def get_foundry_data():
    async with httpx.AsyncClient() as client:
     try:
        response = await client.get(f"{foundry_url}/api/data")
        response.raise_for_status()
        return response.json()
     except Exception as e:
        return {"error": str(e), "service": "foundry-local"}