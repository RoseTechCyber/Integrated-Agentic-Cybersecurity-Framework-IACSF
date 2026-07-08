var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/status", () => Results.Ok(new { status = "Foundry Service running" }));
app.MapGet("/", () => "Hello from Foundry Service!");

app.Run();
