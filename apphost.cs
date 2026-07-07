#:sdk Aspire.AppHost.Sdk@13.4.6+4f218933552e18ff2874d1b6d5dc3fe671e3b6d9

var builder = DistributedApplication.CreateBuilder(args);

// The aspireify skill will wire up your projects here.

builder.Build().Run();