var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/status", () => Results.Ok(new { status = "Reasoning Agent running" }));
app.MapGet("/", () => "Hello from Reasoning Agent!");

app.Run();
﻿
