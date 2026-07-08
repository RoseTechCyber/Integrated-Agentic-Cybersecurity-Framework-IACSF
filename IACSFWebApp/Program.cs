using Microsoft.Extensions.Hosting;
using Aspire.Hosting;

var builder = DistributedApplication.CreateBuilder(args);

// Cosmos DB Emulator
var cosmosEmulator = builder.AddContainer("cosmosdbemulator", "mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest")
    .WithHttpEndpoint(port: 8081, targetPort: 8081)
    .WithEndpoint(port: 10250, targetPort: 10250, isTcp: true)
    .WithEndpoint(port: 10251, targetPort: 10251, isTcp: true)
    .WithEndpoint(port: 10252, targetPort: 10252, isTcp: true)
    .WithEndpoint(port: 10253, targetPort: 10253, isTcp: true)
    .WithEndpoint(port: 10254, targetPort: 10254, isTcp: true)
    .WithPrivileged();

// Foundry Service (local image)
var foundryService = builder.AddContainer("foundry-service", "foundry-service:latest")
    .WithHttpEndpoint(port: 8080, targetPort: 80);

// Reasoning Agent (local image)
var reasoningAgent = builder.AddContainer("reasoning-agent", "reasoning-agent:latest")
    .WithHttpEndpoint(port: 9090, targetPort: 80)
    .WithReference(cosmosEmulator)
    .WithReference(foundryService);

builder.Build().Run();

