import os
from azure.cosmos import CosmosClient

cosmos_uri = os.getenv("COSMOSDB_URI", "https://cosmosdbemulator:8081")
cosmos_key = os.getenv("COSMOSDB_KEY", "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==;")

client = CosmosClient(cosmos_uri, credential=cosmos_key)

# Example integration test setup
database = client.create_database_if_not_exists(id="IACSF-DB")
container = database.create_container_if_not_exists(
    id="Control",
    partition_key="/id",
    offer_throughput=400
)

print("Cosmos DB Emulator integration test passed!")
