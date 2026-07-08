using Microsoft.Extensions.Hosting;
using Aspire.Hosting;

var builder = DistributedApplication.CreateBuilder(args);

// Cosmos DB Emulator
var cosmosEmulator = builder.AddContainer("cosmosdbemulator", "mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest")
    .WithHttpEndpoint(port: 8081, targetPort: 8081)
    .WithPrivileged();

// Foundry Service
var foundryService = builder.AddProject<IACSFWebApp>("foundry-service")
    .WithHttpEndpoint(port: 8080);

// Reasoning Agent
var reasoningAgent = builder.AddProject<IACSFApp>("reasoning-agent")
    .WithHttpEndpoint(port: 9090)
    .WithReference(cosmosEmulator)
    .WithReference(foundryService);

builder.Build().Run();
