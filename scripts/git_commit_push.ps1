#!/usr/bin/env pwsh
# PowerShell script to commit and push changes to GitHub

param (
    [Parameter(Mandatory=$true)]
    [string]$Message
)

# Detect current branch
$branch = git rev-parse --abbrev-ref HEAD

Write-Host "Adding all changes..."
git add -A

Write-Host "Committing with message: $Message"
git commit -m "$Message"

Write-Host "Pushing to origin $branch..."
git push origin $branch

Write-Host "✅ Code committed and pushed successfully to branch $branch."
