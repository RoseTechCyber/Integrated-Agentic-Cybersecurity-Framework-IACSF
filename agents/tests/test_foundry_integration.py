import os
import pytest
import httpx

# Read the backend URL from Aspire environment
backend_url = os.getenv("BACKEND_URL", "http://localhost:5000")

@pytest.mark.asyncio
async def test_foundry_data_endpoint():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{backend_url}/foundry/data")
        assert response.status_code == 200, f"Unexpected status: {response.status_code}"
        data = response.json()
        # Basic validation: ensure we got JSON back
        assert isinstance(data, dict), "Response is not a JSON object"
        # Check for either valid data or an error message
        assert "error" in data or "result" in data or "service" in data or len(data) > 0
