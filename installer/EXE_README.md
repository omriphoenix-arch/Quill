# Quill Installer - Executable (.exe) Build

## 📦 Pre-Built Installer

A standalone Windows `.exe` installer is available in the `dist/` folder:

- **File**: `QuillSetup-1.0.2.exe`
- **Size**: ~11 MB
- **Platform**: Windows 10/11 (64-bit)
- **Requirements**: None! (Python bundled inside)

### How to Use

Simply double-click `QuillSetup-1.0.2.exe` to install Quill. No Python installation required!

---

## 🔨 Building the .exe Installer

If you want to rebuild the installer from source:

### Prerequisites

```powershell
pip install pyinstaller
```

### Build Process

```powershell
cd installer
pyinstaller QuillSetup.spec --clean
```

The `.exe` will be created in `installer/dist/QuillSetup-1.0.2.exe`

### Build Configuration

The build is configured in `QuillSetup.spec`:
- **Icon**: `resources/icons/quill_icon.ico`
- **Type**: Windowed application (no console)
- **Bundled**: All dependencies included (single file)
- **Size**: ~11 MB (includes Python runtime + tkinter)

---

## 📋 What's Included

The `.exe` bundles:
- ✅ Complete Python 3.14 runtime
- ✅ Tkinter GUI library
- ✅ All installer dependencies
- ✅ Quill icon and branding
- ✅ LICENSE and README

---

## 🧪 Testing

Before distributing, test on:
1. **Clean Windows VM** (no Python installed)
2. **Different Windows versions** (10, 11)
3. **User Account Control** (UAC) prompts
4. **Installation paths** (C:\Program Files vs custom)

---

## 🚀 Distribution

### For GitHub Releases

Upload `QuillSetup-1.0.2.exe` as a release asset:

1. Go to: https://github.com/omriphoenix-arch/Quill/releases
2. Edit release or create new release
3. Drag and drop `QuillSetup-1.0.2.exe` into assets
4. Users can download directly without cloning repo

### Alternative Methods

- **Direct Download**: Host on website/server
- **Package Manager**: Submit to Chocolatey, Scoop, etc.
- **USB Distribution**: Copy .exe to USB drives
- **Email**: Small enough to email (11 MB)

---

## 🔧 Build Artifacts

After building, you'll see:

```
installer/
├── build/              # Temporary build files (gitignored)
│   └── QuillSetup/     # Intermediate compilation files
├── dist/               # Final output (gitignored)
│   └── QuillSetup-1.0.2.exe  # The installer!
├── QuillSetup.spec     # Build configuration
├── setup_gui.py        # Source Python installer
└── setup.py            # Source console installer
```

**Note**: `build/` and `dist/` are excluded from git (see `.gitignore`)

---

## 📝 Version Management

When releasing a new version:

1. Update version in `QuillSetup.spec`:
   ```python
   name='QuillSetup-1.0.3',  # Change here
   ```

2. Rebuild:
   ```powershell
   pyinstaller QuillSetup.spec --clean
   ```

3. Test the new .exe

4. Upload to GitHub Release

---

## ⚠️ Known Limitations

- **Windows Only**: This .exe only works on Windows
- **Size**: ~11 MB (larger than script due to bundled Python)
- **Antivirus**: May trigger false positives (common with PyInstaller)
- **Updates**: Need to rebuild for each Quill version

### For macOS Users

Use the Python installer:
```bash
python installer/setup_gui.py
```

### For Linux Users

Use the Python installer:
```bash
python3 installer/setup_gui.py
```

---

## 🎯 Future Improvements

- [ ] Code signing certificate (removes Windows SmartScreen warnings)
- [ ] Auto-updater integration
- [ ] Smaller size with UPX compression
- [ ] macOS `.dmg` installer
- [ ] Linux `.AppImage` or `.deb` packages
- [ ] Multi-language support

---

## 📊 Statistics

- **Build Time**: ~9 hours
- **Final Size**: 11.26 MB
- **Dependencies Bundled**: 969 modules
- **Python Version**: 3.14.0
- **PyInstaller Version**: 6.16.0

---

Built with ❤️ using PyInstaller
