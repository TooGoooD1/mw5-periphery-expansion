#!/usr/bin/env bash
# Same as setup-git.ps1 for Git Bash / macOS / Linux.
set -e
git init
git add .
git commit -m "Initial scaffold"
git branch -M main
git remote add origin https://github.com/TooGoooD1/mw5-periphery-expansion.git
git push -u origin main
git checkout -b develop
git push -u origin develop
