# Run from the repository folder in PowerShell.
# First create an EMPTY repo named mw5-periphery-expansion at https://github.com/new
# (no README, license or .gitignore - they already exist here).
git init
git add .
git commit -m "Initial scaffold"
git branch -M main
git remote add origin https://github.com/TooGoooD1/mw5-periphery-expansion.git
git push -u origin main
git checkout -b develop
git push -u origin develop
