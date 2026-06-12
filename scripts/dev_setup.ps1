#!/usr/bin/env pwsh
# Dev setup script (Windows PowerShell)
# Run this script in an elevated PowerShell prompt if needed.

Write-Host "Setting up dev environment (Windows)..."

# Install dependencies via winget (requires Windows 10/11 with winget available)
# Note: Some installs may require admin privileges
winget install -e --id Python.Python.3.11
winget install -e --id Git.Git
winget install -e --id Docker.DockerDesktop
winget install -e --id Microsoft.DotNet.SDK.8

# Ensure Docker Desktop is running before continuing
Write-Host "Please start Docker Desktop manually if not already running."

# Install Aspire CLI (global dotnet tool)
dotnet tool install --global Microsoft.Aspire.Cli

# Create Python virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip

# Install project requirements
pip install -r agents/requirements.txt
pip install -r web-app/backend/requirements.txt

Write-Host "Dev environment setup complete."
Write-Host "You can now run: aspire up --file Aspire.yml --non-interactive"
