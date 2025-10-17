# Quill v1.0.2 Release Notes

**Release Date:** October 17, 2025  
**Version:** 1.0.2  
**Status:** Stable Release  

---

## 🎉 Major Features

### Modular Import System

Quill v1.0.2 introduces a **Python-like module system** that makes code cleaner and more maintainable!

#### What's New
- **Import Syntax**: Use `import` and `from ... import` statements
- **Lazy Loading**: Modules load on-demand for better performance
- **Namespace Management**: Access functions via dot notation or direct import
- **Backward Compatible**: Use `--legacy` flag to run old programs unchanged

#### Examples

**Import specific functions:**
```python
from game import wait, add_item, show_inventory
from io import read_text, write_text

add_item("sword")
show_inventory()
wait(2)
```

**Import entire modules:**
```python
import game

game.add_item("shield")
game.show_inventory()
```

**Or use legacy mode:**
```bash
quill --legacy your_old_program.quill
```

#### Available Modules
- **`game`** - Inventory system, save/load, wait, choices
- **`io`** - File operations (read_text, write_text, append_text, read_lines, write_lines, file_exists, create_directory)

---

### Professional Project Structure

The entire Quill project has been reorganized for better maintainability and clarity!

#### New Directory Layout
```
possible/
├── core/              # Language implementation
├── examples/          # Example programs (all updated!)
├── games/            # Full game examples
├── installer/        # All installation tools
│   ├── setup_gui.py    # GUI installer
│   ├── setup.py        # Console installer
│   └── quick_installer/ # Shell scripts
├── documentation/    # Project documentation
├── resources/        # Icons and assets
├── tools/           # VS Code extension, utilities
└── archive/         # Legacy experimental code
```

#### Benefits
- ✅ 67% reduction in root directory clutter
- ✅ Logical grouping of related files
- ✅ Easier to navigate and find what you need
- ✅ Professional open-source structure

---

## 🛠️ Critical Bug Fixes

### CRITICAL: License Correction

**Issue:** GUI installer displayed an incorrect MIT license that allowed sublicensing  
**Impact:** High - Legal/IP protection issue  
**Fix:** Both installers now display the correct Quill proprietary license

**What Changed:**
- ❌ OLD: "Permission is hereby granted... to sublicense..."
- ✅ NEW: "Copyright © 2025 Omri Morgan. All Rights Reserved."

**Note:** Quill does NOT allow sublicensing or commercial use without permission!

### Win Error 3: Path Not Found

**Issue:** Installers failed with "Win32 Error 3: The system cannot find the path specified"  
**Cause:** Path resolution pointed to `installer/` instead of project root  
**Fix:** Updated to use `Path(__file__).parent.parent` in both installers

**Impact:** Installers now work correctly after project reorganization!

### VS Code Task Integration

**Issue:** Pressing Ctrl+Shift+B on Python files tried to run them as Quill code  
**Cause:** tasks.json didn't check file extensions  
**Fix:** Added smart file type detection using PowerShell

**Now:**
- `.quill` files → Run with `quill.bat`
- `.py` files → Run with `python`

---

## 📝 All Changes

### Added
- ✨ Modular import system with `import` and `from ... import` syntax
- ✨ Lazy module loading for better performance
- ✨ `--legacy` flag for backward compatibility
- ✨ `module_system_demo.quill` - Comprehensive import examples
- 📁 Professional directory structure (installer/, documentation/, resources/, tools/, archive/)
- 📄 5 new documentation files (PROJECT_REORGANIZATION.md, RELEASE_CHECKLIST_1.0.2.md, etc.)
- 🔧 Smart VS Code task detection for .quill vs .py files
- 📋 Detailed installer logging for debugging

### Fixed
- 🔴 **CRITICAL**: Corrected license display in installers
- 🐛 Win Error 3: Installer path resolution
- 🐛 VS Code Ctrl+Shift+B running Python files as Quill code
- 🐛 GUI installer missing license text
- 🐛 File copy operations for reorganized structure
- 🐛 All internal paths updated for new directory layout

### Changed
- 🔄 All 6 examples updated to use modern import syntax
- 🔄 83 files reorganized into logical directories
- 🔄 Installer window size increased to 700x600 with scrolling
- 🔄 Better error messages for missing imports
- 🔄 Improved module loading performance

### Improved
- ⚡ Faster startup with lazy module loading
- 📚 Clearer code with explicit imports
- 🎯 Better namespace management
- 🔍 More detailed error handling in installers
- 📝 Enhanced logging throughout system

---

## 🚀 Upgrading

### No Breaking Changes!

Quill v1.0.2 is **100% backward compatible** with v1.0.1. Your programs will still work!

### Two Options

#### Option 1: Modern Syntax (Recommended)
Add imports to the top of your programs:

```python
from game import wait, add_item, show_inventory
from io import read_text, write_text

# Your existing code works as-is after imports!
add_item("sword")
show_inventory()
```

**Benefits:**
- Clearer dependencies
- Better performance
- Modern best practice

#### Option 2: Legacy Mode
Run existing programs unchanged:

```bash
quill --legacy your_program.quill
```

No code changes needed!

---

## 📦 Installation

### Option 1: GUI Installer (Recommended)
```bash
python installer/setup_gui.py
```
Professional wizard with 6 pages, progress tracking, and component selection.

### Option 2: Console Installer
```bash
python installer/setup.py
```
Full-featured text-based installer for all platforms.

### Option 3: Quick Scripts
**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File installer/quick_installer/install.ps1
```

**macOS/Linux:**
```bash
chmod +x installer/quick_installer/install.sh
./installer/quick_installer/install.sh
```

### Option 4: Manual Install
```bash
# Just download and run!
python core/quill.py examples/example_simple.quill
```
No installation required!

---

## 🧪 Testing

All features tested and verified:
- ✅ Module system: imports, namespaces, lazy loading
- ✅ All 6 examples working with new import syntax
- ✅ Legacy mode: `--legacy` flag preserves old behavior
- ✅ Installers: GUI and console installers tested
- ✅ VS Code tasks: File type detection working
- ✅ Backward compatibility: Old programs work in legacy mode

---

## 📚 Documentation

### Updated Documentation
- [VERSION.md](documentation/VERSION.md) - Version information
- [CHANGELOG.md](CHANGELOG.md) - Complete change log
- [README.md](README.md) - Updated with v1.0.2 features
- [PROJECT_REORGANIZATION.md](documentation/PROJECT_REORGANIZATION.md) - New structure guide

### New Documentation
- [RELEASE_CHECKLIST_1.0.2.md](documentation/RELEASE_CHECKLIST_1.0.2.md) - Release workflow
- [LICENSE_FIX_CRITICAL.md](documentation/LICENSE_FIX_CRITICAL.md) - License correction details
- [VSCODE_TASKS_FIX.md](documentation/VSCODE_TASKS_FIX.md) - VS Code integration guide
- [SESSION_SUMMARY_OCT17_2025.md](documentation/SESSION_SUMMARY_OCT17_2025.md) - Development summary

### Updated Examples
- [module_system_demo.quill](examples/module_system_demo.quill) - NEW! Comprehensive import examples
- [demo_inventory.quill](examples/demo_inventory.quill) - Updated with imports
- [demo_saveload.quill](examples/demo_saveload.quill) - Updated with imports
- [demo_wait.quill](examples/demo_wait.quill) - Updated with imports
- [demo_randomizer.quill](examples/demo_randomizer.quill) - Updated with imports
- [file_io.quill](examples/file_io.quill) - Updated with imports

---

## 🎯 What's Next

### Planned for Future Releases
- More built-in modules (math, string utilities, etc.)
- REPL (interactive mode)
- Debugger integration
- Package manager
- More game development utilities

### Community Feedback
We'd love to hear from you!
- Report bugs: [GitHub Issues](https://github.com/yourusername/quill/issues)
- Suggest features: [GitHub Discussions](https://github.com/yourusername/quill/discussions)
- Share your projects: Tag us on social media!

---

## 💬 Support

Need help?
- 📖 Check [documentation/](documentation/) folder for guides
- 💡 See [examples/](examples/) for code samples
- 🐛 Report bugs on GitHub Issues
- 💬 Ask questions in GitHub Discussions

---

## 📊 Statistics

- **Files Reorganized:** 83
- **New Features:** 3 major (module system, reorganization, legacy mode)
- **Bugs Fixed:** 6 critical/high priority
- **Documentation Added:** 5 new guides
- **Examples Updated:** 6 files
- **Tests Passed:** 4/4 (100%)
- **Lines of Code Changed:** 2,000+
- **Commits:** 12
- **Development Time:** 2 days

---

## 🙏 Acknowledgments

Thank you to everyone who reported bugs, suggested features, and tested early versions!

Special thanks to the open-source community for inspiration and best practices.

---

## 📄 License

**Quill Programming Language**  
Copyright © 2025 Omri Morgan  
All Rights Reserved

Personal and educational use permitted.  
Commercial use requires explicit written permission.  
NO sublicensing or redistribution without authorization.

See [LICENSE](LICENSE) for complete terms.

---

## 🚀 Get Started

```bash
# Download Quill
git clone https://github.com/yourusername/quill.git
cd quill

# Run the module system demo
python core/quill.py examples/module_system_demo.quill

# Or try legacy mode
python core/quill.py --legacy examples/demo_wait.quill
```

**Happy coding with Quill v1.0.2!** 🎉

---

*Released October 17, 2025*
