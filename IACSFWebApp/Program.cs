using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Health check endpoint for CI readiness
app.MapGet("/status", () => Results.Ok(new { status = "Foundry Service is running" }));

// Optional root endpoint
app.MapGet("/", () => "Hello from Foundry Service!");

app.Run();
