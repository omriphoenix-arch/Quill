# Quill Installation Options

Quill provides **two professional installers** to suit your preference:

## 🪟 Option 1: GUI Installer (Recommended)

**Windows-style graphical installer** with a step-by-step wizard!

```bash
python setup_gui.py
```

### Features:
- ✅ **Welcome screen** with system information
- ✅ **License agreement** page
- ✅ **Installation type** selection (Recommended/Custom)
- ✅ **Custom options**:
  - Choose installation directory
  - Select components (examples, docs, tests)
  - Toggle PATH registration
  - Toggle file associations
  - Toggle Start Menu shortcuts
- ✅ **Installation summary** before proceeding
- ✅ **Real-time progress** with detailed log
- ✅ **Completion screen** with quick start info

### Screenshots:

**Welcome Page:**
- System information display
- Python version check
- Administrator status

**Installation Options:**
- Browse for custom directory
- Checkboxes for each feature
- Live validation

**Progress Page:**
- Animated progress bar
- Detailed log output
- Status messages

## 📟 Option 2: Console Installer

**Command-line installer** for servers or headless systems.

```bash
python setup.py
```

### Features:
- ✅ Interactive menu (Install/Uninstall/Exit)
- ✅ System detection (Windows/Linux/macOS)
- ✅ Admin/sudo detection
- ✅ Automatic PATH configuration
- ✅ File association registration
- ✅ Progress messages with emoji
- ✅ Error handling and recovery

## Quick Comparison

| Feature | GUI Installer | Console Installer |
|---------|--------------|-------------------|
| **Visual Interface** | ✅ Full GUI | ❌ Text-based |
| **Step-by-Step Wizard** | ✅ Yes | ⚠️ Simple menu |
| **Custom Options** | ✅ All options | ⚠️ Basic options |
| **Progress Bar** | ✅ Animated | ❌ Text only |
| **Browse Directories** | ✅ File dialog | ❌ Manual entry |
| **Real-time Log** | ✅ Scrollable | ✅ Terminal output |
| **Works on Servers** | ❌ Needs display | ✅ Yes |
| **Requires tkinter** | ✅ Yes (built-in) | ❌ No |

## Installation Steps

### GUI Installer (setup_gui.py)

1. **Launch**:
   ```bash
   python setup_gui.py
   ```

2. **Welcome**: Review system information and click Next

3. **License**: Read and accept the license agreement

4. **Installation Type**:
   - **Recommended**: Standard installation for your system
   - **Custom**: Choose location and options

5. **Custom Options** (if selected):
   - Browse for installation directory
   - Select components:
     - ✅ Add to PATH
     - ✅ Register .quill files
     - ✅ Start Menu shortcut
     - ✅ Install examples/docs

6. **Ready to Install**: Review summary and click Install

7. **Installing**: Watch progress in real-time

8. **Complete**: Click Finish (optionally open examples folder)

### Console Installer (setup.py)

1. **Launch**:
   ```bash
   python setup.py
   ```

2. **Menu**: Choose option:
   - `1` - Install Quill
   - `2` - Uninstall Quill
   - `3` - Exit

3. **Installation**:
   - Automatic directory selection
   - Progress messages
   - System integration

4. **Complete**: Follow on-screen instructions

## Fallback Behavior

The GUI installer automatically falls back to console if:
- tkinter is not available
- `--console` flag is used
- Running in a headless environment

```bash
# Force console installer
python setup_gui.py --console
```

## System Requirements

### Both Installers
- ✅ Python 3.7 or higher
- ✅ ~2 MB disk space
- ✅ Windows, Linux, or macOS

### GUI Installer Only
- ✅ tkinter (usually built into Python)
- ✅ Display/desktop environment

**Check tkinter**:
```bash
python -c "import tkinter"
```

If tkinter is missing:
- **Ubuntu/Debian**: `sudo apt-get install python3-tk`
- **Fedora/RHEL**: `sudo dnf install python3-tkinter`
- **macOS**: Built into Python
- **Windows**: Built into Python

## What Gets Installed

Both installers install the **same components**:

### Always Installed:
- ✅ **core/** - Interpreter, modules, stdlib
- ✅ **examples/** - Sample programs
- ✅ **docs/** - Complete documentation
- ✅ **icons/** - File icons (Windows)
- ✅ **scripts/** - Utility scripts
- ✅ **tests/** - Test suite
- ✅ **games/** - Example games
- ✅ Documentation files (README, QUICK_START, LICENSE, etc.)

### System Integration:
- ✅ PATH registration
- ✅ .quill file association
- ✅ Start Menu shortcut (Windows admin)
- ✅ Shell integration (Linux/macOS)

## Post-Installation

### Verify Installation:
```bash
# Open NEW terminal
quill --help
```

### Run Example:
```bash
quill examples/calculator.quill
```

### Test Modules:
```bash
quill tests/test_modules.quill
```

## Uninstallation

### GUI Method:
```bash
python setup_gui.py
# (Future: Will include uninstall option)
```

### Console Method:
```bash
python setup.py
# Choose option 2 (Uninstall)
```

## Troubleshooting

### "tkinter not found" (GUI Installer)
- **Solution 1**: Install tkinter (see System Requirements)
- **Solution 2**: Use console installer: `python setup.py`
- **Solution 3**: Force console mode: `python setup_gui.py --console`

### "Permission denied"
- **Windows**: Run PowerShell as Administrator
- **Linux/macOS**: Use `sudo python3 setup_gui.py`

### "Python version too old"
- **Requirement**: Python 3.7+
- **Check**: `python --version`
- **Solution**: Download from [python.org](https://python.org)

### GUI doesn't launch
- Check tkinter: `python -c "import tkinter"`
- Try console installer: `python setup.py`

## Developer Mode (No Installation)

Want to run without installing?
```bash
cd /path/to/Quill
python core/quill.py script.quill
```

## Which Installer Should I Use?

**Use GUI Installer (`setup_gui.py`) if:**
- ✅ You prefer visual interfaces
- ✅ You want to customize installation options
- ✅ You want to see real-time progress
- ✅ You're on a desktop system

**Use Console Installer (`setup.py`) if:**
- ✅ You're on a server (no GUI)
- ✅ You prefer command-line tools
- ✅ Automating installation via scripts
- ✅ tkinter is not available

---

**Both installers provide a complete, professional Quill installation!** Choose the one that fits your workflow. 🚀
