# Quill Installation Guide

## What Gets Installed

The Quill installer (`setup.py`) provides a **complete, professional installation** that includes:

### ✅ Core Components (Always Installed)
- **`core/`** - Quill interpreter, lexer, parser, standard library, module system
- **`examples/`** - Sample programs (calculator, games, file I/O demos)
- **`docs/`** - Complete documentation (MODULE_SYSTEM.md, tutorials, references)

### ✅ Optional Components (Installed if Present)
- **`icons/`** - Custom .quill file icons for Windows Explorer
- **`scripts/`** - Utility scripts (testing, migration, etc.)
- **`tests/`** - Test suite for validation
- **`games/`** - Example game projects

### ✅ Documentation Files
- **`README.md`** - Main documentation
- **`QUICK_START.md`** - 5-minute quick start guide
- **`LICENSE`** - Software license
- **`requirements.txt`** - Optional dependencies (PIL/Pillow)
- **`CHANGELOG.md`** - Version history

### ✅ System Integration

#### Windows
- ✅ Adds to System or User PATH (run `quill` from anywhere)
- ✅ Registers `.quill` file association (double-click to run)
- ✅ Creates Start Menu shortcut (if admin)
- ✅ Copies `quill.bat` launcher

#### Linux/macOS
- ✅ Installs to `/usr/local/lib/quill` (sudo) or `~/.local/lib/quill`
- ✅ Creates executable `quill` command in `/usr/local/bin` or `~/.local/bin`
- ✅ Updates `.bashrc` or `.zshrc` for PATH
- ✅ Sets proper executable permissions

## Installation Methods

### Method 1: Full System Installation (Recommended)

**Windows (Administrator)**:
```powershell
# Right-click PowerShell -> "Run as Administrator"
cd C:\path\to\Quill
python setup.py
# Choose option 1 (Install)
```

**Windows (User - No Admin)**:
```powershell
cd C:\path\to\Quill
python setup.py
# Choose option 1 (Install)
# Installs to: %USERPROFILE%\Quill
```

**Linux/macOS (System-wide)**:
```bash
cd /path/to/Quill
sudo python3 setup.py
# Choose option 1 (Install)
# Installs to: /usr/local/lib/quill
```

**Linux/macOS (User)**:
```bash
cd /path/to/Quill
python3 setup.py
# Choose option 1 (Install)
# Installs to: ~/.local/lib/quill
```

### Method 2: Developer Mode (No Installation)

Run directly from source:
```bash
cd /path/to/Quill
python core/quill.py script.quill
```

Good for:
- Development and testing
- Contributing to Quill
- Running without system modifications

## What You Need

### Required
- ✅ **Python 3.7+** (Tested up to Python 3.14)
- ✅ **No external dependencies!** (Pure Python standard library)

### Optional
- **PIL/Pillow** - For GUI features (images, advanced graphics)
  ```bash
  pip install pillow
  ```
- **pywin32** (Windows only) - For Start Menu shortcuts
  ```bash
  pip install pywin32
  ```

## Installation Paths

### Windows
| Mode | Install Location | PATH Location |
|------|-----------------|---------------|
| **Admin** | `C:\Program Files\Quill\` | System PATH |
| **User** | `%USERPROFILE%\Quill\` | User PATH |

### Linux/macOS
| Mode | Install Location | Binary Location |
|------|-----------------|-----------------|
| **sudo** | `/usr/local/lib/quill/` | `/usr/local/bin/quill` |
| **user** | `~/.local/lib/quill/` | `~/.local/bin/quill` |

## Post-Installation

### 1. Verify Installation
```bash
# Open a NEW terminal/command prompt
quill --help

# Should show:
# Usage: quill <filename.quill> [--legacy]
```

### 2. Run Example
```bash
quill examples/calculator.quill
```

### 3. Test Module System
```bash
quill tests/test_modules.quill
```

### 4. Create Your First Script
```quill
# hello.quill
say "Hello, World!"
say "Python version: " + str(3 + 4)
```

Run it:
```bash
quill hello.quill
```

## Troubleshooting

### "quill: command not found"
**Windows**: 
- Restart your terminal/command prompt
- If still not working, log out and log back in

**Linux/macOS**:
```bash
# If user install:
source ~/.bashrc  # or ~/.zshrc

# Check if binary exists:
ls ~/.local/bin/quill
```

### "Python version too old"
The installer checks for Python 3.7+. Update Python:
- **Windows**: Download from [python.org](https://python.org)
- **Linux**: `sudo apt install python3` or equivalent
- **macOS**: `brew install python3`

### "Module 'io' not found"
The module system requires the new file structure. Reinstall:
```bash
python setup.py
# Choose option 1 (Install)
```

### "Permission denied"
**Windows**: Run as Administrator  
**Linux/macOS**: Use `sudo python3 setup.py`

### Old scripts with game/io functions fail
Use legacy mode:
```bash
quill old_game.quill --legacy
```

Or add imports to your script:
```quill
from game import *
from io import *
# ... rest of your code
```

## Uninstallation

Run the installer again:
```bash
python setup.py
# Choose option 2 (Uninstall)
```

This removes:
- All installed files
- PATH entries
- File associations (Windows)
- Launcher scripts

## Upgrading

To upgrade to a new version:
1. Download/pull latest Quill
2. Run installer (will prompt to overwrite)
3. Your scripts remain untouched!

## Files NOT Installed

The installer **does not copy**:
- `.git/` - Git repository data
- `.github/` - GitHub Actions workflows
- `.vscode/` - VS Code settings
- Build artifacts, temporary files
- Your own `.quill` scripts outside the Quill directory

## Directory Structure After Installation

```
Windows (Admin):
C:\Program Files\Quill\
├── core\           # Interpreter, modules, stdlib
├── examples\       # Sample programs
├── docs\           # Documentation
├── icons\          # File icons
├── scripts\        # Utility scripts
├── tests\          # Test suite
├── games\          # Example games
├── quill.bat       # Windows launcher
├── README.md
├── QUICK_START.md
└── LICENSE

Linux/macOS (sudo):
/usr/local/lib/quill/
├── core/           # Interpreter, modules, stdlib
├── examples/       # Sample programs
├── docs/           # Documentation
├── tests/          # Test suite
└── ...

/usr/local/bin/
└── quill           # Executable launcher
```

## Summary

**YES**, the `setup.py` installer installs **everything necessary** for Quill:
- ✅ Complete interpreter and module system
- ✅ All examples and documentation
- ✅ System integration (PATH, file associations)
- ✅ Icons and utilities
- ✅ No external dependencies required

After installation, you can immediately run any `.quill` file from anywhere on your system! 🚀
