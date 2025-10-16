# 🎨 Quill Icons in VS Code

## ✅ Installation Complete!

Your VS Code extension has been installed with custom icons!

---

## 🔄 How to See Your Icons

### Step 1: Restart VS Code
**IMPORTANT:** You must close and reopen VS Code for the extension to load.

1. **Close ALL VS Code windows** (File → Exit, or Alt+F4)
2. **Wait 2 seconds**
3. **Reopen VS Code**

### Step 2: Open Your Quill Project
1. In VS Code, go to: **File → Open Folder**
2. Navigate to: `C:\Users\Omri.Morgan02\Downloads\possible`
3. Click **Select Folder**

### Step 3: Check the File Explorer
1. Look at the left sidebar (Explorer panel)
2. Navigate to the `games` folder
3. You should see your `.quill` files with the **gradient book icon**! 🌈📖

---

## 🎨 Optional: Enable Icon Theme

For even better icons throughout VS Code:

1. Press **Ctrl+Shift+P** (Command Palette)
2. Type: `File Icon Theme`
3. Select: **"Preferences: File Icon Theme"**
4. Choose: **"Quill File Icons"**

This applies the custom icon theme to all `.quill` files!

---

## 📂 Where Your Extension Lives

```
C:\Users\Omri.Morgan02\.vscode\extensions\Quill-1.1.0\
├── package.json                    # Extension manifest
├── language-configuration.json     # Language settings
├── syntaxes/
│   └── Quill.tmLanguage.json # Syntax highlighting
└── icons/
    ├── Quill-icon.png        # Extension icon (128x128)
    ├── Quill-icon.svg        # File icon (SVG)
    └── Quill-icon-theme.json # Icon theme definition
```

---

## 🔍 Verify Installation

### Check if Extension is Loaded
1. Press **Ctrl+Shift+X** (Extensions panel)
2. Search for: `@installed Quill`
3. You should see: **"Quill Language Support"**

### Check if Icons Work
1. Open: `C:\Users\Omri.Morgan02\Downloads\possible\games`
2. Look at any `.quill` file in the Explorer
3. Icon should be visible next to the filename

---

## 🎨 What You Get

### In File Explorer
- Custom gradient book icon for `.quill` files
- Matches your Windows File Explorer icon
- Visible in sidebar, tabs, and breadcrumbs

### Syntax Highlighting
- Keywords highlighted in color
- Strings, numbers, comments all styled
- Easy to read and write code

---

## 🛠️ Troubleshooting

### Icons not showing?

#### 1. Restart VS Code (IMPORTANT!)
```
Close all windows → Wait 2 seconds → Reopen
```

#### 2. Reload Window
- Press **Ctrl+Shift+P**
- Type: `Reload Window`
- Press Enter

#### 3. Reinstall Extension
```bash
cd "C:\Users\Omri.Morgan02\Downloads\possible\.vscode-extension"
powershell -ExecutionPolicy Bypass -File install_extension.ps1
```

#### 4. Check Extension is Active
- Press **Ctrl+Shift+X**
- Search: `@installed`
- Look for "Quill Language Support"
- Should be **enabled** (not disabled)

### Still not working?

#### Enable Developer Tools
1. Press **Ctrl+Shift+I** (Developer Tools)
2. Check **Console** tab for errors
3. Look for messages about "Quill"

#### Check Extension Folder
```powershell
Test-Path "$env:USERPROFILE\.vscode\extensions\Quill-1.1.0"
# Should return: True
```

---

## 🎯 Quick Commands

### Reinstall Extension
```bash
cd "C:\Users\Omri.Morgan02\Downloads\possible\.vscode-extension"
powershell -ExecutionPolicy Bypass -File install_extension.ps1
```

### Update Icons (if you changed them)
```bash
cd "C:\Users\Omri.Morgan02\Downloads\possible\.vscode-extension"
python convert_icon.py
powershell -ExecutionPolicy Bypass -File install_extension.ps1
```

### Uninstall Extension
```powershell
Remove-Item "$env:USERPROFILE\.vscode\extensions\Quill-1.1.0" -Recurse -Force
```

---

## 📝 File Associations

The extension registers `.quill` files with:
- **Language ID:** `Quill`
- **Display Name:** Quill
- **Icon:** Gradient book (purple/pink)
- **Syntax Highlighting:** Full support

---

## 🎨 Customizing Icons

Want to change the icon style in VS Code?

### 1. Update the source icon
```bash
cd "C:\Users\Omri.Morgan02\Downloads\possible\icons"
python update_icon.py  # Choose different style
```

### 2. Regenerate PNG for VS Code
```bash
cd "C:\Users\Omri.Morgan02\Downloads\possible\.vscode-extension"
python convert_icon.py
```

### 3. Reinstall extension
```bash
powershell -ExecutionPolicy Bypass -File install_extension.ps1
```

### 4. Restart VS Code
Close all windows and reopen!

---

## ✨ What's Next?

### Enable Icon Theme
1. **Ctrl+Shift+P** → `File Icon Theme`
2. Select **"Quill File Icons"**
3. All `.quill` files get custom icons!

### Customize Syntax Highlighting
Edit: `.vscode-extension/syntaxes/Quill.tmLanguage.json`

### Add Code Snippets
Create: `.vscode-extension/snippets/Quill.json`

### Share Your Extension
Package it: `vsce package` (requires Node.js)

---

## 🎉 Success!

Your `.quill` files now have beautiful custom icons in VS Code! 🌈📖

**To see them:**
1. ✅ Restart VS Code
2. ✅ Open your project folder
3. ✅ Look at the Explorer sidebar
4. ✅ Enjoy your custom icons!

---

**Made with 💜 for Quill**

*Beautiful icons in both Windows and VS Code!* 🚀
