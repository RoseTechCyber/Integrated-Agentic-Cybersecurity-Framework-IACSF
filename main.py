import os
import pytest
import json
from azure.cosmos import CosmosClient, PartitionKey
from control_operations import create_control, read_control, Control
from sentence_transformers import SentenceTransformer

# Load ISO 27001 controls JSON
with open("data/frameworks/iso27001_controls.json", "r") as f:
    controls_data = json.load(f)

# Initialize embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Cosmos Emulator
@pytest.fixture(scope="module")
def cosmos_container():
    connection_string = os.getenv("COSMOSDB_CONNECTION_STRING")
    database_id = os.getenv("COSMOSDB_DATABASE_NAME")
    container_id = os.getenv("COSMOSDB_CONTAINER_NAME")
	
 if not connection_string:
        raise ValueError("Please set COSMOSDB_CONNECTION_STRING environment variable.")

    client = CosmosClient.from_connection_string(connection_string)
    database = client.create_database_if_not_exists(id=database_id)
    container = database.create_container_if_not_exists(
        id=container_id,
        partition_key=PartitionKey(path="/id")
    )

# Ingest controls into Cosmos with embeddings
for domain, domain_data in controls_data["domains"].items():
    for control_id, control in domain_data["control"].items():
        embedding = model.encode(control["description"]).tolist()
        container.upsert_item({
            "id": control["id"],
            "title": control["title"],
            "description": control["description"],
            "embedding": embedding,
            "mappings": {
                "cis": control.get("cis_mapping", []),
                "nist": control.get("nist_csf_mapping", []),
                "cisa": control.get("cisa_mapping", [])
            }
        })

print("ISO 27001 controls ingested with embeddings.")
