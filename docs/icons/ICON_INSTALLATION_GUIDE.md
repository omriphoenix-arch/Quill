# How to Install and See Your Custom Icon

## Quick Start

1. **Run the installer:**
   ```
   Double-click: INSTALL_Quill.bat
   ```

2. **Wait for completion**
   - The installer will copy the icon file
   - It will associate `.quill` files with the icon

3. **View your files:**
   - Open File Explorer
   - Navigate to your Quill folder
   - Your `.quill` files should now have the custom icon! 📘

## Step-by-Step Guide

### Before You Start
- ✅ Make sure `Quill_icon.ico` exists in your folder
- ✅ Close any open File Explorer windows
- ✅ Right-click INSTALL_Quill.bat and "Run as Administrator"

### During Installation
You'll see these steps:
```
[1/5] Creating installation directory...
[2/5] Copying Quill files...
      Icon file copied!                    ← Icon is being installed
[3/5] Adding Quill to system PATH...
[4/5] Creating Start Menu shortcuts...
[5/5] Setting up .quill file association...
      Custom icon assigned to .quill files! ← Icon is registered
```

### After Installation

1. **Open File Explorer** (Win + E)

2. **Navigate to your project folder:**
   ```
   C:\Users\YourName\Downloads\possible\
   ```

3. **Look at your .quill files:**
   - `game.quill`
   - `test_icon.quill`
   - `asson_complete.quill`
   - All files in `examples/` folder

4. **You should see:**
   - Blue book icon with white "S"
   - Icon appears at all sizes (small, medium, large, extra large views)

## If You Don't See the Icon

### Method 1: Refresh Icon Cache
```powershell
# Open PowerShell and run:
ie4uinit.exe -show
```

### Method 2: Restart Windows Explorer
```powershell
# Open PowerShell and run:
Stop-Process -Name explorer -Force
```
*Explorer will automatically restart*

### Method 3: Clear Icon Cache (Nuclear Option)
```powershell
# Open PowerShell as Admin and run:
Remove-Item "$env:LOCALAPPDATA\IconCache.db" -Force
Stop-Process -Name explorer -Force
```

### Method 4: Restart Your Computer
Sometimes Windows needs a full restart to pick up new icons.

## Viewing the Icon File Itself

Want to see what the icon looks like?

1. **Navigate to:**
   ```
   C:\Users\YourName\Downloads\possible\
   ```

2. **Double-click:** `Quill_icon.ico`

3. **Opens in:** Default image viewer or Paint

4. **You'll see:** The blue book icon with "S"

## Changing File Explorer View

To see the icon at different sizes:

1. **In File Explorer, click "View" tab**

2. **Try different views:**
   - Extra large icons ← Icon looks biggest here
   - Large icons
   - Medium icons
   - Small icons
   - List ← Icon appears small
   - Details ← Icon appears small
   - Tiles ← Icon appears medium

## Testing the Icon

Run the test file:
```powershell
.\Quill test_icon.quill
```

Then check that `test_icon.quill` has the custom icon in File Explorer.

## Comparison

### Before Installation:
```
📄 game.quill          ← Generic file icon
📄 test_icon.quill     ← Generic file icon
```

### After Installation:
```
📘 game.quill          ← Custom Quill icon!
📘 test_icon.quill     ← Custom Quill icon!
```

## Verification Checklist

✅ **Icon file exists:**
```powershell
Test-Path "C:\Program Files\Quill\Quill_icon.ico"
# Should return: True
```

✅ **Registry key set:**
```powershell
Get-ItemProperty -Path "HKCR:\Quill.File\DefaultIcon"
# Should show: C:\Program Files\Quill\Quill_icon.ico,0
```

✅ **File association works:**
```powershell
# Double-click any .quill file
# Should run with Quill (not open in notepad)
```

## Advanced: View Icon at Different Sizes

The icon file contains multiple sizes. To see them all:

1. **Open Paint or image editor**

2. **Open:** `Quill_icon.ico`

3. **You'll see one size** (usually 256×256)

4. **The icon contains:**
   - 256×256 (extra large, high DPI)
   - 128×128 (large)
   - 64×64 (medium)
   - 48×48 (normal)
   - 32×32 (small)
   - 16×16 (tiny, list view)

## Creating a Desktop Shortcut

To see the icon on your desktop:

1. **Right-click on `game.quill`**

2. **Send to → Desktop (create shortcut)**

3. **Check your desktop** - shortcut should have the icon!

## Customizing the Icon

Want to change the icon design?

1. **Edit:** `create_icon.py`

2. **Change colors, text, design**

3. **Run:** `python create_icon.py`

4. **Reinstall:** Run INSTALL_Quill.bat again

5. **Refresh:** Clear icon cache

See `docs/CUSTOM_ICON.md` for details.

---

**Tip:** The 16×16 size is most important! Make sure your design is clear at tiny sizes.

**Note:** Windows caches icons aggressively. Be patient after changes, and try the refresh methods above.

Enjoy your professional-looking Quill files! 📘✨
