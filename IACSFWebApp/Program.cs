using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Simple health check endpoint
app.MapGet("/status", () => Results.Ok(new { status = "Foundry Service is running" }));

// Root endpoint (optional)
app.MapGet("/", () => "Hello from Foundry Service!");

app.Run();
