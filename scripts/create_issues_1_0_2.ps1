<#
Creates milestone and issues for v1.0.2 using GitHub CLI (gh).
Prereqs:
   - Install GitHub CLI: https://cli.github.com/
   - Authenticate: gh auth login
Usage:
   - From repo root, run: ./scripts/create_issues_1_0_2.ps1
   - Optionally override: ./scripts/create_issues_1_0_2.ps1 -Repo "owner/name" -Milestone "v1.0.2"
#>

param(
   [string]$Repo,
   [string]$Milestone = "v1.0.2"
)

# --- Safety checks ---
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
   Write-Error "GitHub CLI (gh) not found. Install from https://cli.github.com/ and run 'gh auth login'."
   exit 1
}

try {
   gh auth status 1>$null 2>$null
} catch {
   Write-Error "GitHub CLI is not authenticated. Run: gh auth login"
   exit 1
}

# Try to infer repo from current directory if not provided
if (-not $Repo -or $Repo.Trim() -eq "") {
   try {
      $repoInfo = gh repo view --json nameWithOwner | ConvertFrom-Json
      if ($repoInfo -and $repoInfo.nameWithOwner) { $Repo = $repoInfo.nameWithOwner }
   } catch {}
}
if (-not $Repo -or $Repo.Trim() -eq "") {
   Write-Error "Repository not set and could not be inferred. Re-run with -Repo 'owner/name' or from inside a cloned GitHub repo."
   exit 1
}

function New-Issue {
  param(
    [string]$Title,
    [string]$Body,
    [string[]]$Labels
  )
  $labelArgs = @()
  foreach ($l in $Labels) { $labelArgs += "--label"; $labelArgs += $l }
  gh issue create --repo $Repo --title $Title --body $Body --milestone $Milestone @labelArgs | Write-Host
}

# Ensure labels exist (create if missing)
$requiredLabels = @(
  # Areas
  @{ name = "area:core"; color = "1f6feb"; description = "Core language/runtime" },
  @{ name = "area:vscode"; color = "a371f7"; description = "VS Code extension" },
  @{ name = "area:packaging"; color = "fbca04"; description = "Packaging & distribution" },
  @{ name = "area:docs"; color = "0e8a16"; description = "Documentation" },
  @{ name = "area:ci"; color = "0052cc"; description = "CI / infrastructure" },
  @{ name = "area:release"; color = "d93f0b"; description = "Release management" },
  # Types
  @{ name = "type:bug"; color = "d73a4a"; description = "Something isn't working" },
  @{ name = "type:enhancement"; color = "a2eeef"; description = "New feature or request" },
  @{ name = "type:maintenance"; color = "cfd3d7"; description = "Code health / chores" },
  @{ name = "type:docs"; color = "0075ca"; description = "Docs and content" },
  @{ name = "type:performance"; color = "ffd866"; description = "Performance improvements" },
  @{ name = "design"; color = "c5def5"; description = "Design/UI/UX" },
  @{ name = "good-first-issue"; color = "7057ff"; description = "Good for newcomers" }
)

Write-Host "Ensuring labels exist..." -ForegroundColor Cyan
$existing = gh label list --repo $Repo --limit 200 --json name | ConvertFrom-Json
$existingNames = @()
if ($existing) { $existingNames = $existing.name }
foreach ($lbl in $requiredLabels) {
  if (-not ($existingNames -and $existingNames -contains $lbl.name)) {
    gh label create $lbl.name --repo $Repo --color $lbl.color --description $lbl.description 1>$null 2>$null
    Write-Host "Created label: $($lbl.name)"
  }
}

# Ensure milestone exists
$ms = gh api repos/$Repo/milestones --paginate | ConvertFrom-Json | Where-Object { $_.title -eq $Milestone }
if (-not $ms) {
  Write-Host "Creating milestone: $Milestone"
  gh api repos/$Repo/milestones -f title=$Milestone -f state=open | Out-Null
} else {
  Write-Host "Milestone exists: $Milestone"
}

# Define issues inline (keeps mapping stable vs freeform plan doc)
$issues = @(
  @{ t = "Improve error messages with line/column, code excerpt, and caret";
     b = "Implement richer errors across parser/interpreter with file:line:col, the source line, a ^ caret, and a short hint for common mistakes. Acceptance: examples + tests show improved messages.";
     l = @("area:core","type:enhancement","good-first-issue") },
  @{ t = "Harden input prompts (ask/wait) for EOF and robustness";
     b = "Ensure ask/wait paths handle EOF and invalid input without crashing; fallback messaging on Ctrl+Z/Ctrl+D.";
     l = @("area:core","type:bug") },
  @{ t = "Validate UTF-8 console I/O on Windows (emoji/accents)";
     b = "Reconfirm stdout/stderr stdin UTF-8 handling with sample scripts; document known caveats.";
     l = @("area:core","type:enhancement") },
  @{ t = "Add small stdlib helpers (clamp, random choice, trim/lower/upper)";
     b = "Add helpers and document them in Language Guide; add unit examples to comprehensive test.";
     l = @("area:core","type:enhancement","good-first-issue") },
  @{ t = "Micro-optimizations in lexer/parser (cache token kinds)";
     b = "Profile hot paths, cache token kinds/regex where safe; ensure no regressions.";
     l = @("area:core","type:performance") },
  @{ t = "Grammar tweaks for Quill keywords/operators";
     b = "Ensure keywords (if/then/else/end/while/for/function/import) and operators (and/or/not/is) are highlighted. Update tmLanguage and tests.";
     l = @("area:vscode","type:enhancement") },
  @{ t = "Theme polish and contrast audit (Dark/Light/Neon)";
     b = "Verify contrast ratios, adjust specific token colors as needed, keep brand-consistent purples.";
     l = @("area:vscode","type:enhancement","design") },
  @{ t = "Verify language icon uses neon PNG (no legacy assets)";
     b = "Confirm package.json points to PNG; ensure no SVG SS assets remain; add a check to CI.";
     l = @("area:vscode","type:maintenance") },
  @{ t = "One-liner install scripts (PowerShell + Bash)";
     b = "Provide scripts that fetch the latest release and set up associations/icons (per-user on Windows). Document in README.";
     l = @("area:packaging","type:enhancement") },
  @{ t = "Reliable Windows icon/association scripts (per-user)";
     b = "Finalize PowerShell for .quill icon + shortcut; include cache refresh.";
     l = @("area:packaging","type:enhancement") },
  @{ t = "Publish VSIX in GitHub Releases for easy install";
     b = "Attach quill-extension.vsix to release assets; add README instructions.";
     l = @("area:packaging","type:release") },
  @{ t = "Quick Start (10 minutes) - install, run, first script";
     b = "Add a concise Quick Start; include Windows + Ubuntu paths.";
     l = @("area:docs","type:docs") },
  @{ t = "Language Guide - syntax, flow, functions, built-ins";
     b = "Expand docs with examples and edge cases.";
     l = @("area:docs","type:docs") },
  @{ t = "Troubleshooting - encoding, file associations, VS Code cache";
     b = "Common issues and fixes with step-by-step remedies.";
     l = @("area:docs","type:docs") },
  @{ t = "CI: keep comprehensive test green on main";
     b = "Ensure Windows/Ubuntu jobs pass; add badges and flakes notes if any.";
     l = @("area:ci","type:maintenance") },
  @{ t = "Update release checklist for 1.0.2";
     b = "Add steps for VSIX, icon verification, and docs in the release checklist.";
     l = @("area:release","type:maintenance") }
)

Write-Host "Creating issues in $Repo for milestone $Milestone..." -ForegroundColor Cyan
$existingIssues = gh issue list --repo $Repo --milestone $Milestone --state all --limit 200 --json title | ConvertFrom-Json
$existingTitles = @()
if ($existingIssues) { $existingTitles = $existingIssues.title }
foreach ($i in $issues) {
   if ($existingTitles -and ($existingTitles -contains $i.t)) {
      Write-Host "Skip (already exists): $($i.t)" -ForegroundColor Yellow
   } else {
      New-Issue -Title $i.t -Body $i.b -Labels $i.l
   }
}

Write-Host "\nAll issues created and assigned to milestone $Milestone."
