# Quill — Game Utilities Guide

Quill includes optional utilities designed for interactive fiction and text-based games. These features are completely optional and can be used when you need them.

## Features
- `choice` — Multiple choice prompts that set the `answer` variable
- `goto` / `label` — Basic state machine control
- `wait(seconds)` — Pause execution
- Inventory system: `add_item`, `remove_item`, `has_item`, `show_inventory`, `clear_inventory`
- Save/Load: `save_game`, `load_game`, `has_save`, `delete_save`

## Usage Notes
- Game utilities are part of the core runtime but considered "optional" in documentation. Use them when creating interactive scripts or prototypes.
- Save files are stored in the `saves/` folder by default.

***

For tutorials and examples, see `examples/` and the docs in `docs/`.
