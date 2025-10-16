# Quill Installation - What Gets Installed

This document explains exactly what files and configurations are installed when you run the Quill installer.

## Installation Methods

### Method 1: Windows Quick Install (Recommended)
```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
```

### Method 2: Unix/Linux/Mac Quick Install
```bash
chmod +x install.sh
./install.sh
```

## What Gets Installed

### 1. Core Interpreter ✅
**Location:** `core/`
**Files:**
- `quill.py` - Main interpreter entry point
- `lexer.py` - Tokenizer
- `parser.py` - AST parser
- `interpreter.py` - Execution engine
- `colors.py` - Terminal output utilities
- `gui_engine.py` - GUI framework (commented out in beta)

**Dependencies:**
- Python 3.8+ (required)
- pip (Python package manager)

### 2. Launcher Scripts ✅
**Windows:**
- `quill.bat` - Batch file launcher
- Added to user PATH via registry

**Unix/Linux/Mac:**
- `quill` - Shell script launcher
- Made executable (`chmod +x`)
- Added to shell config (~/.bashrc, ~/.zshrc, or ~/.profile)

### 3. File Association (Windows) ✅
**What's configured:**
- `.quill` file extension registered
- Double-click opens files with `quill.bat`
- Custom file icons (if available)
- Registry entry: `HKCU:\Software\Classes\.quill`

**Registration script:** `scripts/register_quill.ps1`

### 4. VS Code Extension ✅
**Location:** `.vscode-extension/`
**Components:**
- `package.json` - Extension metadata
- `syntaxes/quill.tmLanguage.json` - TextMate grammar
- `themes/` - Three color themes:
  - Quill Classic Dark
  - Quill Dark Theme
  - Quill Light Theme
- `icons/` - File icons (PNG/SVG)
- `icon-themes/` - Icon theme configuration

**Auto-installation:**
The workspace includes `.vscode/extensions.json` which tells VS Code to automatically install the local extension when you open the workspace folder.

### 5. Example Programs ✅
**Location:** `examples/`
**Included files:**
- `example_simple.quill` - Basic syntax demo
- `example_calculator.quill` - Calculator program
- `example_guessing_game.quill` - Number guessing game
- `example_todo_list.quill` - Todo list manager
- `example_adventure.quill` - Text adventure game
- `example_mystery.quill` - Detective mystery game
- `example_full_language.quill` - Complete language feature showcase

### 6. Games ✅
**Location:** `games/`
Pre-built text adventure games demonstrating Quill's capabilities.

### 7. Documentation ✅
**Location:** `docs/` and root directory
**Files:**
- `README.md` - Main project documentation
- `TUTORIAL.md` - Step-by-step learning guide
- `STORYSCRIPT_KEYWORDS_REFERENCE.md` - Complete keyword reference
- `ERROR_MESSAGES.md` - Error explanations
- `RESERVED_KEYWORDS.md` - List of reserved words
- `CONTRIBUTING.md` - Contribution guidelines
- `CODE_OF_CONDUCT.md` - Community guidelines
- `CHANGELOG.md` - Version history
- `LICENSE` - MIT License

### 8. Development Tools ✅
**Location:** `.vscode/`
**Files:**
- `settings.json` - Workspace settings (syntax highlighting rules)
- `extensions.json` - Recommended extensions
- `tasks.json` - Build/run tasks (Ctrl+Shift+B)
- `launch.json` - Debug configurations (F5)

### 9. Utility Scripts ✅
**Location:** `scripts/`
**Files:**
- `register_quill.ps1` - Register .quill files (Windows)
- `unregister_quill.ps1` - Uninstall file association (Windows)

## What Does NOT Get Installed

### Not Included in Beta:
- ❌ GUI engine (commented out - planned for future release)
- ❌ Binary executables (Python interpreter required)
- ❌ System-wide installation (installs for current user only)
- ❌ Auto-updates
- ❌ Package managers (pip install quill - coming later)

## Installation Verification

After installation, verify everything works:

### Windows:
```powershell
# Test the launcher
quill.bat examples\example_simple.quill

# Verify file association
# Double-click any .quill file in File Explorer

# Check VS Code integration
# Open workspace in VS Code and look for "Quill" in bottom-left
```

### Unix/Linux/Mac:
```bash
# Test the launcher
./quill examples/example_simple.quill

# Verify PATH
quill examples/example_simple.quill  # (if added to PATH)

# Check VS Code integration
code .  # Open workspace in VS Code
```

## File Structure After Installation

```
quill/
├── core/                      # Interpreter (Python)
│   ├── quill.py              ✅ Main entry point
│   ├── lexer.py              ✅ Tokenizer
│   ├── parser.py             ✅ Parser
│   ├── interpreter.py        ✅ Executor
│   ├── colors.py             ✅ Terminal utilities
│   └── gui_engine.py         ⚠️ GUI (disabled in beta)
│
├── examples/                  # Sample programs
│   ├── example_simple.quill  ✅
│   ├── example_*.quill       ✅ (7 examples)
│   └── ...
│
├── games/                     # Full games
│   └── *.quill               ✅
│
├── docs/                      # Documentation
│   ├── TUTORIAL.md           ✅
│   ├── ERROR_MESSAGES.md     ✅
│   └── ...
│
├── .vscode/                   # VS Code workspace config
│   ├── settings.json         ✅ Syntax colors
│   ├── extensions.json       ✅ Auto-install extension
│   ├── tasks.json            ✅ Run tasks
│   └── launch.json           ✅ Debug config
│
├── .vscode-extension/         # VS Code extension
│   ├── package.json          ✅
│   ├── syntaxes/             ✅ Grammar
│   ├── themes/               ✅ Color themes
│   └── icons/                ✅ File icons
│
├── scripts/                   # Utility scripts
│   ├── register_quill.ps1    ✅ File association
│   └── unregister_quill.ps1  ✅ Uninstall
│
├── quill.bat                 ✅ Windows launcher
├── quill                     ✅ Unix launcher
├── install.ps1               ✅ Windows installer
├── install.sh                ✅ Unix installer
├── README.md                 ✅ Main docs
├── LICENSE                   ✅ MIT License
└── CHANGELOG.md              ✅ Version history
```

## Minimal Installation (Manual)

If you want to install manually without the installer:

### Minimum Required:
1. Python 3.8+
2. `core/` folder (all .py files)
3. At least one `.quill` example file to test

### To run:
```bash
python core/quill.py your_program.quill
```

### Recommended Additions:
4. Create a launcher script (`quill.bat` or `quill`)
5. Install VS Code extension from `.vscode-extension/`
6. Read `README.md` for full documentation

## Troubleshooting

### Windows: "Cannot execute .quill files"
**Solution:** Run the registration script:
```powershell
powershell -ExecutionPolicy Bypass -File scripts\register_quill.ps1
```

### Unix: "Permission denied: ./quill"
**Solution:** Make launcher executable:
```bash
chmod +x quill
```

### VS Code: "Language shows as 'Plain Text'"
**Solution:** 
1. Open the workspace folder (not individual files)
2. Reload VS Code window (Ctrl+Shift+P → "Developer: Reload Window")
3. Check `.vscode/extensions.json` exists

### Python: "Module not found"
**Solution:** Ensure Python 3.8+ is installed:
```bash
python --version  # Windows
python3 --version # Unix/Mac
```

## Uninstallation

### Windows:
```powershell
# Remove file association and PATH
powershell -ExecutionPolicy Bypass -File scripts\unregister_quill.ps1

# Delete folder
Remove-Item -Recurse -Force "C:\path\to\quill"
```

### Unix/Linux/Mac:
```bash
# Remove PATH entry from shell config
# Edit ~/.bashrc, ~/.zshrc, or ~/.profile and remove the Quill lines

# Delete folder
rm -rf /path/to/quill
```

## Summary

✅ **The installer downloads/configures:**
- Core Python interpreter
- Launcher scripts
- File associations (Windows)
- VS Code extension (auto-install)
- Example programs
- Documentation
- Development tools

✅ **What you need separately:**
- Python 3.8+ (must be installed first)
- VS Code (optional, but recommended)
- Git (optional, for contributing)

🎉 **After installation, you can:**
- Run `.quill` programs from the command line
- Double-click `.quill` files (Windows)
- Edit with syntax highlighting in VS Code
- Debug programs with VS Code (F5)
- Use the `quill` command globally (if added to PATH)
