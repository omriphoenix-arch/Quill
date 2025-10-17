# Quill v1.0.2 – Issue Plan

Milestone: v1.0.2
Target window: 1–2 weeks after 1.0.1-beta

This file enumerates the issues to create from the v1.0.2 roadmap.

## Core language/runtime
1. Improve error messages with line/column, code excerpt, and caret
   - Labels: area:core, type:enhancement, good-first-issue
   - Body: Implement richer errors across parser/interpreter with `file:line:col`, the source line, a `^` caret, and a short hint for common mistakes. Acceptance: examples + tests show improved messages.

2. Harden input prompts (ask/wait) for EOF and robustness
   - Labels: area:core, type:bug
   - Body: Ensure `ask`/`wait` paths handle EOF and invalid input without crashing; fallback messaging on Ctrl+Z/Ctrl+D.

3. Validate UTF-8 console I/O on Windows (emoji/accents)
   - Labels: area:core, type:enhancement
   - Body: Reconfirm stdout/stderr stdin UTF-8 handling with sample scripts; document known caveats.

4. Add small stdlib helpers (clamp, random choice, trim/lower/upper)
   - Labels: area:core, type:enhancement, good-first-issue
   - Body: Add helpers and document them in Language Guide; add unit examples to comprehensive test.

5. Micro-optimizations in lexer/parser (cache token kinds)
   - Labels: area:core, type:performance
   - Body: Profile hot paths, cache token kinds/regex where safe; ensure no regressions.

## VS Code extension
6. Grammar tweaks for Quill keywords/operators
   - Labels: area:vscode, type:enhancement
   - Body: Ensure keywords (if/then/else/end/while/for/function/import) and operators (and/or/not/is) are highlighted. Update tmLanguage and tests.

7. Theme polish and contrast audit (Dark/Light/Neon)
   - Labels: area:vscode, type:enhancement, design
   - Body: Verify contrast ratios, adjust specific token colors as needed, keep brand-consistent purples.

8. Verify language icon uses neon PNG (no legacy assets)
   - Labels: area:vscode, type:maintenance
   - Body: Confirm `package.json` points to PNG; ensure no SVG SS assets remain; add a check to CI.

## Packaging & install
9. One-liner install scripts (PowerShell + Bash)
   - Labels: area:packaging, type:enhancement
   - Body: Provide scripts that fetch the latest release and set up associations/icons (per-user on Windows). Document in README.

10. Reliable Windows icon/association scripts (per-user)
   - Labels: area:packaging, type:enhancement
   - Body: Finalize PowerShell for .quill icon + shortcut; include cache refresh.

11. Publish VSIX in GitHub Releases for easy install
   - Labels: area:packaging, type:release
   - Body: Attach `quill-extension.vsix` to release assets; add README instructions.

## Documentation
12. Quick Start (10 minutes) – install → run → first script
   - Labels: area:docs, type:docs
   - Body: Add a concise Quick Start; include Windows + Ubuntu paths.

13. Language Guide – syntax, flow, functions, built-ins
   - Labels: area:docs, type:docs
   - Body: Expand docs with examples and edge cases.

14. Troubleshooting – encoding, file associations, VS Code cache
   - Labels: area:docs, type:docs
   - Body: Common issues and fixes with step-by-step remedies.

## Community & quality
15. CI: keep comprehensive test green on main
   - Labels: area:ci, type:maintenance
   - Body: Ensure Windows/Ubuntu jobs pass; add badges and flakes notes if any.

16. Update release checklist for 1.0.2
   - Labels: area:release, type:maintenance
   - Body: Add steps for VSIX, icon verification, and docs in the release checklist.
