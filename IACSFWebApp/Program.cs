using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Azure.Cosmos;
using System.Net.Http;
using System.Threading.Tasks;

var builder = WebApplication.CreateBuilder(args);

// Add controllers
builder.Services.AddControllers();

// Register Cosmos client (pointing to emulator)
builder.Services.AddSingleton<CosmosClient>(sp =>
{
    var endpointUri = "https://localhost:8081";
    var primaryKey = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+...=="; // emulator default key
    return new CosmosClient(endpointUri, primaryKey);
});

   var foundryService = builder.AddContainer("foundry-service", acr)
    .WithImage("foundry-service")
    .WithTag("latest")
    .WithRegistry(acr)
    .WithHttpEndpoint(port: 8080, targetPort: 80);


// Register HTTP client for Foundry Service (port 8080)
builder.Services.AddHttpClient("foundry-service", client =>
{
    client.BaseAddress = new Uri("http://localhost:8080"); 
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseRouting();
app.UseAuthorization();

app.MapControllers();

// Example endpoint: query Cosmos and call Foundry Service
app.MapGet("/reason", async (CosmosClient cosmos, IHttpClientFactory httpClientFactory) =>
{
    var db = cosmos.GetDatabase("ReasoningDb");
    var container = db.GetContainer("JsonData");

    var query = new QueryDefinition("SELECT * FROM c");
    var iterator = container.GetItemQueryIterator<dynamic>(query);

    var results = new List<dynamic>();
    while (iterator.HasMoreResults)
    {
        foreach (var item in await iterator.ReadNextAsync())
        {
            results.Add(item);
        }
    }

    // Call Foundry Service for additional processing
    var client = httpClientFactory.CreateClient("FoundryService");
    var response = await client.GetStringAsync("/process"); // adjust path to Foundry API
    return Results.Ok(new { cosmosCount = results.Count, foundryResponse = response });
});

// Run on port 9090
app.Run("http://0.0.0.0:9090");
