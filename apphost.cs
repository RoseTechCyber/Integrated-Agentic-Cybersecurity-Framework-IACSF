using Microsoft.Extensions.Hosting;
using Aspire.Hosting;

var builder = DistributedApplication.CreateBuilder(args);

// Cosmos DB Emulator
var cosmosEmulator = builder.AddContainer("cosmosdbemulator", "mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest")
    .WithHttpEndpoint(port: 8081, targetPort: 8081)
    .WithPrivileged();

// Foundry Service
var foundryService = builder.AddContainer("foundry-service", "foundry-service:latest")
    .WithHttpEndpoint(port: 8080, targetPort: 80);

// Reasoning Agent
var reasoningAgent = builder.AddContainer("reasoning-agent", "reasoning-agent:latest")
    .WithHttpEndpoint(port: 9090, targetPort: 80)
    .WithReference(cosmosEmulator)
    .WithReference(foundryService);

builder.Build().Run();

