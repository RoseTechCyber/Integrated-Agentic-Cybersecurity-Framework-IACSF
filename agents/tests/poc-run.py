query = "What are the policies for information security?"
query_embedding = model.encode(query).tolist()

# Vector search in Cosmos
results = iso_container.query_items(
    query="SELECT TOP 3 c.id, c.title, c.description FROM c WHERE VectorDistance(c.embedding, @embedding) < 0.3",
    parameters=[{"name": "@embedding", "value": query_embedding}],
    enable_cross_partition_query=True
)

# Pass results to Foundry generative model
context = "\n".join([f"{r['id']}: {r['title']} - {r['description']}" for r in results])
answer = foundry_model.generate(f"Question: {query}\nContext:\n{context}")
print(answer)
