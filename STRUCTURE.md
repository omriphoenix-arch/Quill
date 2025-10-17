# Quill Project Structure

This document describes the organization of the Quill programming language project.

## 📁 Directory Structure

```
Quill/
├── core/                    # Core language implementation
│   ├── lexer.py            # Tokenization and lexical analysis
│   ├── parser.py           # Abstract Syntax Tree (AST) parser
│   ├── interpreter.py      # Main interpreter and execution engine
│   ├── stdlib.py           # Standard library functions
│   ├── quill.py           # Main entry point and CLI
│   └── modules/           # Module system
│       ├── __init__.py    # Module loader
│       ├── io_module.py   # File I/O operations
│       └── game_module.py # Game development utilities
│
├── examples/               # Example Quill programs
│   ├── hello_world.quill
│   ├── example_adventure.quill
│   ├── example_mystery.quill
│   └── ...
│
├── games/                  # Full game examples
│   └── ...
│
├── tests/                  # Test suite
│   ├── test_modules.quill
│   └── ...
│
├── scripts/                # Runtime helper scripts
│   └── quill_runner.py
│
├── docs/                   # API and module documentation
│   ├── MODULE_SYSTEM.md
│   ├── core/
│   │   └── guide.md
│   └── game/
│       └── guide.md
│
├── installer/              # Installation tools
│   ├── setup.py           # Console installer (interactive)
│   ├── setup_gui.py       # GUI installer (tkinter wizard)
│   ├── install.ps1        # PowerShell quick install
│   ├── install.sh         # Bash quick install
│   ├── quick_install.ps1  # Windows one-liner
│   └── quick_install.sh   # Unix one-liner
│
├── resources/              # Project resources
│   └── icons/             # Application icons
│       ├── quill_icon.ico
│       ├── quill_icon.png
│       └── ...
│
├── tools/                  # Development and utility tools
│   ├── vscode-extension/  # VS Code extension
│   │   ├── package.json
│   │   ├── extension.js
│   │   └── quill-extension.vsix
│   ├── rebrand_icons.ps1  # Icon rebranding script
│   ├── test_examples.ps1  # Example testing script
│   └── test_output.txt    # Test results
│
├── documentation/          # Project documentation
│   ├── QUICK_START.md
│   ├── INSTALLATION_GUIDE.md
│   ├── GUI_INSTALLER_GUIDE.md
│   ├── INSTALLER_OPTIONS.md
│   ├── INSTALLER_COMPLETE.md
│   ├── MODULAR_SYSTEM_COMPLETE.md
│   ├── ROADMAP_1.0.2.md
│   ├── TESTING_RESULTS.md
│   ├── TRANSITION_SUMMARY.md
│   ├── VERSION.md
│   └── v1.0.1_RELEASE_CHECKLIST.md
│
├── archive/                # Archived/deprecated files
│   └── ...
│
├── saves/                  # Save game data directory
│   └── (user-generated saves)
│
├── .github/                # GitHub-specific files
│   └── workflows/
│
├── .vscode/                # VS Code workspace settings
│
├── quill                   # Unix launcher script
├── quill.bat              # Windows launcher script
├── README.md              # Main project README
├── LICENSE                # License file (MIT)
├── CHANGELOG.md           # Version history
├── CODE_OF_CONDUCT.md     # Community guidelines
├── CONTRIBUTING.md        # Contribution guidelines
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore rules
```

## 🎯 Directory Purposes

### Core Language (`core/`)
The heart of Quill - contains all language implementation files:
- **Lexer**: Converts source code into tokens
- **Parser**: Builds Abstract Syntax Trees from tokens
- **Interpreter**: Executes the AST
- **Standard Library**: Built-in functions
- **Module System**: Lazy-loading module architecture

### Examples & Games (`examples/`, `games/`)
- `examples/`: Short, educational Quill programs demonstrating features
- `games/`: Complete game implementations showcasing Quill's capabilities

### Installation (`installer/`)
Multiple installation methods for different user preferences:
- **GUI Installer**: Professional tkinter wizard (like Python's installer)
- **Console Installer**: Interactive CLI installer
- **Quick Install Scripts**: One-command installation for PowerShell and Bash

### Resources (`resources/`)
Non-code assets:
- **Icons**: Application icons in various formats (ICO, PNG, SVG)
- Future: Could include themes, fonts, assets

### Tools (`tools/`)
Development utilities and extensions:
- **VS Code Extension**: Syntax highlighting and language support
- **Testing Scripts**: Automated testing tools
- **Utility Scripts**: Icon rebranding, build automation, etc.

### Documentation (`documentation/`)
Project-level documentation (not API docs):
- Installation guides
- Roadmaps and changelogs
- Testing results
- Transition guides

### API Documentation (`docs/`)
Technical API and module documentation:
- Module system architecture
- Core language reference
- Module-specific guides (game, io, etc.)

### Archive (`archive/`)
Deprecated or old files kept for reference

## 🚀 Quick Start Paths

**For Users:**
1. Run installer: `python installer/setup_gui.py` or `python installer/setup.py`
2. Follow documentation: `documentation/QUICK_START.md`
3. Try examples: `examples/hello_world.quill`

**For Developers:**
1. Read: `CONTRIBUTING.md`
2. Explore: `core/` for implementation
3. Test: `tests/` for test suite

**For Contributors:**
1. Check: `documentation/ROADMAP_1.0.2.md` for planned features
2. Review: `CHANGELOG.md` for version history
3. Follow: `CODE_OF_CONDUCT.md` for community standards

## 📝 Notes

- All paths in scripts and documentation have been updated to reflect this structure
- The module system uses relative imports within `core/modules/`
- Installers automatically handle the new directory structure
- VS Code extension works with this layout out of the box

## 🔄 Migration from Old Structure

If you have an older version of Quill:
1. Back up your files
2. Pull the latest changes: `git pull origin main`
3. The new structure is automatically applied
4. Update any custom scripts that reference old paths

---

**Last Updated**: v1.0.2 reorganization (October 2025)
