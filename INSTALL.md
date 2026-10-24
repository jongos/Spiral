# Install and update Spiral

Spiral is an instruction-only skill. Copy the entire
`skills/spiral-workflow-rehearsal` directory, including `references/`, into your
agent's supported skill directory. No API key or package installation is required
by Spiral itself. Your agent has its own runtime requirements.

## Codex local installation

From the root of a Spiral checkout, run this PowerShell example for a personal
installation. It stops if a copy already exists:

```powershell
$spiralSource = (Resolve-Path ./skills/spiral-workflow-rehearsal).Path
$spiralParent = Join-Path $HOME '.agents/skills'
$spiralTarget = Join-Path $spiralParent 'spiral-workflow-rehearsal'
if (Test-Path -LiteralPath $spiralTarget) { throw 'Already installed; follow the update steps.' }
New-Item -ItemType Directory -Force -Path $spiralParent | Out-Null
Copy-Item -LiteralPath $spiralSource -Destination $spiralTarget -Recurse
Get-ChildItem -LiteralPath $spiralTarget -Recurse -File
```

For a repository-scoped installation, set `$spiralParent` to
`<your-project>/.agents/skills` instead. Use one scope to avoid duplicate copies.
Confirm that the installed folder contains `SKILL.md` and all three Markdown
files in `references/`. Select Spiral in your skill selector, then ask it to
rehearse a small fictional workflow. If discovery has not refreshed, restart
Codex. Copy verification does not establish agent discovery or skill quality.

These locations and refresh behavior follow the
[official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills),
checked October 24, 2026. Other agents have their own installation locations.

## Update an existing installation

1. Record the installed source commit and preserve any local customizations.
2. In the source checkout, inspect `git status --short` and the incoming changes.
   On a clean `main` checkout, use `git pull --ff-only`; resolve divergence before
   continuing. Record `git rev-parse HEAD`.
3. Run `python -B -m unittest discover -s tests -v` from the checkout. Review
   [validation scope](validation/README.md); these checks are not agent efficacy tests.
4. Back up the existing installed skill outside the scanned skill directories.
   Replace the installed folder with the complete reviewed source folder. Avoid
   overlaying files: old references could otherwise survive an update.
5. Compare the installed file list and SHA-256 hashes with the source, then
   repeat the discovery and fictional-workflow smoke check above.

Updating the Git checkout alone does not update a copied installation. This guide
does not install or update anything automatically.
