#!/usr/bin/env bash

# Dev setup script (Linux)
set -euo pipefail

echo "Setting up dev environment (Linux)..."

# Install python, pip, git, docker, dotnet (instructions vary per distro)
# This script is a helper; run commands manually if you need elevated privileges.

# Example for Ubuntu/Debian
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git curl docker.io docker-compose dotnet-sdk-8.0

# Install Aspire CLI
dotnet tool install --global Microsoft.Aspire.Cli

# Python virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

# Install project requirements
pip install -r agents/requirements.txt || true
pip install -r web-app/backend/requirements.txt || true

echo "Dev environment setup complete."
echo "You can now run: aspire up --file Aspire.yml --non-interactive"