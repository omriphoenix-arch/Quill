# Quill Custom Icon

## Overview
Quill files (`.quill`) now have their own custom icon! This makes it easy to identify Quill files in Windows Explorer.

## Icon Design
The Quill icon features:
- 📘 **Blue book/document** design
- **"S"** letter for "Quill"
- **Multiple sizes** (16x16 to 256x256) for crisp display at any scale
- **Professional look** that stands out in file explorers

## Installation

### Automatic (Recommended)
The icon is automatically installed when you run the Quill installer:

```powershell
.\INSTALL_Quill.bat
```

The installer will:
1. Copy the icon file to the installation directory
2. Associate `.quill` files with the custom icon
3. Update Windows registry for file type associations

### Manual Installation
If you need to manually set up the icon:

1. **Copy the icon file:**
   ```powershell
   Copy-Item Quill_icon.ico "$env:ProgramFiles\Quill\"
   ```

2. **Update registry:**
   ```powershell
   # Run PowerShell as Administrator
   $installDir = "$env:ProgramFiles\Quill"
   Set-ItemProperty -Path "HKCR:\Quill.File\DefaultIcon" -Name "(Default)" -Value "$installDir\Quill_icon.ico,0"
   ```

3. **Refresh Explorer:**
   - Press `Win + R`
   - Type `ie4uinit.exe -show`
   - Press Enter

## Creating a Custom Icon

### Using the Icon Generator
Run the included icon generator script:

```powershell
python create_icon.py
```

This will create `Quill_icon.ico` with multiple sizes.

### Requirements
- **Python 3.6+**
- **Pillow (PIL)** for high-quality icons (optional)
  ```powershell
  pip install Pillow
  ```

Without Pillow, a basic icon will still be created.

### Customizing the Icon
Edit `create_icon.py` to customize:

```python
# Change colors
page_color = (100, 150, 255, 255)  # RGBA: Blue
line_color = (255, 255, 255, 200)  # RGBA: White

# Change the letter
text = "S"  # Change to any character

# Change sizes
sizes = [256, 128, 64, 48, 32, 16]  # Icon sizes
```

## Icon Specifications

### Technical Details
- **Format:** Windows ICO
- **Sizes:** 256×256, 128×128, 64×64, 48×48, 32×32, 16×16
- **Color Depth:** 32-bit (RGBA with transparency)
- **Compression:** None (uncompressed)

### File Size
- Approximately 100-200 KB
- All sizes embedded in one file

## Using Your Own Icon

### From an Existing Image
1. **Get an image** (PNG, JPG, etc.)
2. **Convert to ICO:**
   - Use online converter: https://convertio.co/png-ico/
   - Or use `create_icon.py` as template
3. **Replace** `Quill_icon.ico`
4. **Reinstall** Quill or update registry manually

### Icon Design Tips
✅ **DO:**
- Use simple, recognizable shapes
- Make it readable at 16×16 pixels
- Use high contrast colors
- Test on both light and dark backgrounds
- Include multiple sizes

❌ **DON'T:**
- Use too many details (won't show at small sizes)
- Use low contrast (hard to see)
- Forget transparency around edges
- Use only one size

## Troubleshooting

### Icon Not Showing
1. **Refresh icon cache:**
   ```powershell
   ie4uinit.exe -show
   ```

2. **Rebuild icon cache:**
   ```powershell
   # Delete icon cache (as admin)
   Remove-Item "$env:LOCALAPPDATA\IconCache.db" -Force
   # Restart Windows Explorer
   Stop-Process -Name explorer -Force
   ```

3. **Check file association:**
   ```powershell
   # Verify registry entry
   Get-ItemProperty -Path "HKCR:\Quill.File\DefaultIcon"
   ```

### Icon File Missing
If `Quill_icon.ico` is missing:

```powershell
# Regenerate icon
python create_icon.py

# Or reinstall Quill
.\INSTALL_Quill.bat
```

### Wrong Icon Displayed
- Windows may cache old icons
- Try restarting Windows Explorer:
  ```powershell
  Stop-Process -Name explorer -Force
  ```

## Advanced Customization

### Creating Icons with Photoshop/GIMP
1. Create images at each size:
   - 256×256 (high res)
   - 128×128
   - 64×64
   - 48×48
   - 32×32
   - 16×16 (most important!)

2. Export each as PNG with transparency

3. Use ICO converter or Python script:
   ```python
   from PIL import Image
   
   img = Image.open('your_icon.png')
   img.save('Quill_icon.ico', format='ICO', sizes=[(256,256), (128,128), (64,64), (48,48), (32,32), (16,16)])
   ```

### Animated Icons (Advanced)
Windows ICO format doesn't support animation, but you can:
- Use a GIF as file thumbnail (limited support)
- Create a custom Windows Explorer column handler (C++ required)

## Icon Comparison

### Before (Python Icon)
```
🐍 game.quill  ← Uses Python icon
```

### After (Custom Icon)
```
📘 game.quill  ← Uses Quill icon
```

## Platform Support

### Windows
✅ **Full support**
- Icon displays in File Explorer
- Shows in Start Menu
- Appears in taskbar

### macOS
⚠️ **Partial support**
- Need to create `.icns` file
- Requires separate setup

### Linux
⚠️ **Varies by desktop**
- Need to create desktop entry
- Icon depends on file manager

## Files

### Included Files
- `Quill_icon.ico` - The icon file (multiple sizes)
- `create_icon.py` - Icon generator script
- `install.ps1` - Installer (sets up icon)
- `uninstall.ps1` - Uninstaller (removes icon)

## FAQ

**Q: Can I use my own icon?**  
A: Yes! Replace `Quill_icon.ico` with your own ICO file and reinstall.

**Q: Why doesn't the icon change immediately?**  
A: Windows caches icons. Refresh with `ie4uinit.exe -show` or restart Explorer.

**Q: Can I have different icons for different .quill files?**  
A: Not easily. Windows uses one icon per file extension. You'd need custom shell extensions.

**Q: The icon looks blurry at small sizes**  
A: Make sure your ICO file includes a proper 16×16 size. This is the most important size.

**Q: Can I animate the icon?**  
A: ICO format doesn't support animation. The icon is static.

---

**Version:** Quill v1.1+  
**Created:** Icon system added with custom icon support

Now your Quill files look professional! 🎨✨
