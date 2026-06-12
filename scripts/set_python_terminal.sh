#!/usr/bin/env bash
set -euo pipefail

# Path to VS Code settings.json in Codespaces
SETTINGS_PATH="$HOME/.vscode/settings.json"

# Ensure the directory exists
mkdir -p "$(dirname "$SETTINGS_PATH")"

# Add Python terminal configuration
cat > "$SETTINGS_PATH" <<'EOF'
{
    "terminal.integrated.profiles": {
        "python": {
            "path": "python",
            "args": ["-i"]
        }
    },
    "terminal.integrated.defaultProfile.linux": "python"
}
EOF

echo "✅ VS Code settings.json updated to use Python terminal by default."
