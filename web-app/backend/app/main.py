import json
from azure.cosmos import CosmosClient
from sentence_transformers import SentenceTransformer

# Load ISO 27001 controls JSON
with open("data/frameworks/iso27001_controls.json", "r") as f:
    controls_data = json.load(f)

# Initialize embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Cosmos Emulator
client = CosmosClient("https://cosmos-emulator:8081", {"masterKey": "your-emulator-key"})
database = client.create_database_if_not_exists(id="SecurityFrameworks")
container = database.create_container_if_not_exists(id="Controls", partition_key="/id")

# Ingest controls into Cosmos with embeddings
for domain, domain_data in controls_data["domains"].items():
    for control_id, control in domain_data["controls"].items():
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
