# Quill — Core Language Guide

This guide covers the core features of Quill intended for general-purpose scripting.

## Getting Started

- Variables, types (numbers, strings, booleans, lists)
- Functions, loops, conditionals
- Input/Output: `say`/`print`, `ask`

## Standard Library
Quill provides a standard library for common tasks including math, random, string manipulation, list utilities, and file I/O.

Key functions:
- `read_text(path)`, `write_text(path, content)`, `append_text(path, content)`
- `read_lines(path)`, `write_lines(path, lines)`
- `trim`, `lower`, `upper`, `split`, `join`, `replace`
- `clamp`, `min`, `max`, `sum`, `average`, `sqrt`

See `examples/file_io.quill` for a quick demonstration of file operations.

## Best Practices
- Keep scripts small and focused
- Use the stdlib for common tasks to avoid reimplementation
- Prefer `read_lines`/`write_lines` for simple line-based files

***

This document contains the essentials — more detailed tutorials are available in `docs/TUTORIAL.md` and the language reference files.
