# Quill v1.0.2 Roadmap (Draft)

Target window: 1–2 weeks after 1.0.1-beta
Owner: @omriphoenix-arch

## North star for 1.0.2
- Make onboarding flawless (install, icons, syntax) across Windows and VS Code.
- Stabilize core runtime with small quality-of-life features and tighter error messages.
- Ship a polished VS Code experience that matches the new Quill brand.

## Scope and themes
1) Core language/runtime
- Better error messages (show line/column, snippet caret, "did you mean" on common mistakes)
- Input robustness (EOF handling in REPL and file mode already improved — expand to ask/wait prompts)
- Windows console I/O smoothing (UTF‑8 verified; keep testing with emoji/accents)
- Small stdlib helpers (math: clamp, random choice; strings: trim/lower/upper)
- Performance: micro-optimizations in lexer/parser hot paths (cache token kinds)

Acceptance:
- All examples and `tests/comprehensive_test.quill` pass on Windows + Ubuntu
- New errors print: file:line:col, excerpt line, ^ caret, hint when applicable

2) VS Code extension
- Finalize neon icon branding (done) and remove legacy SS assets (done)
- File icon only for .quill; let other files use user’s icon theme (done)
- Grammar tweaks for Quill-specific keywords and operators
- Theme polish: ensure contrast and consistency across Dark/Light/Neon

Acceptance:
- Grammar highlights keywords: if, then, else, end, while, for, function, import, and/or/not/is
- Theme names correctly capitalized (done); visual QA on both dark and light

3) Packaging & install
- One-liner install scripts (PowerShell + Bash) to fetch latest release
- Regenerate Windows icons reliably and apply registry entries per-user
- Publish VSIX on GitHub Releases for easy install (no npm required)

Acceptance:
- README has copy-paste install blocks for Windows and Linux
- VSIX downloadable from 1.0.2 release assets

4) Documentation
- Quick Start (10 minutes): install → run → write first script
- Language guide: syntax, control flow, functions, built-ins
- Troubleshooting: common errors and fixes (encoding, file associations, VS Code)

Acceptance:
- New docs linked from README and (optional) GitHub Wiki

5) Community & quality
- Add GitHub issue templates (bug / feature / task)
- Basic CI workflow: run comprehensive test on pushes/PRs (Windows + Ubuntu)
- Release checklist update for 1.0.2

Acceptance:
- CI green on main; templates live; release checklist checked during tag

## Milestones & timeline
- M1 (days 1–2): CI + templates + doc scaffolding
- M2 (days 3–5): Core error messages + small stdlib + grammar tweaks
- M3 (days 6–7): Install scripts + VSIX artifacts + polish pass

## Backlog (nice-to-haves)
- Syntax sugar for choices/menus
- First-class arrays and maps with literals
- LSP server prototype (hover docs, diagnostics)

## Risks / mitigations
- Windows icon caching: provide a reliable refresh step in scripts
- VS Code caching: avoid SVG for language icon; use PNG and reload guidance
- Scope creep: keep 1.0.2 small; push bigger items to 1.1

## Tracking
- Convert each bullet to GitHub issues with `v1.0.2` milestone
- Keep CHANGELOG with Unreleased → 1.0.2 when shipped
