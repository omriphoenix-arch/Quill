# Quill File Icons

## Available Icon Styles

Quill comes with **4 unique icon designs** for `.quill` files. Choose the one that matches your aesthetic preference!

---

## 🎨 Icon Gallery

### 1. **Gradient Book** (Default)
**File:** `Quill_icon.ico`

**Design:**
- Modern gradient from purple to pink
- Book design with spine highlight
- "SS" lettering with glow effect
- Professional and colorful

**Best for:** Users who want a modern, colorful look with personality

---

### 2. **Minimalist Flat**
**File:** `Quill_icon_minimalist.ico`

**Design:**
- Clean flat design in blue
- Document with folded corner
- Simple horizontal text lines
- Material design inspired

**Best for:** Users who prefer clean, simple, professional aesthetics

---

### 3. **Neon Cyberpunk**
**File:** `Quill_icon_neon.ico`

**Design:**
- Dark background with cyan neon glow
- Multiple glow layers for depth
- Glowing "S" symbol
- Cyberpunk/retro-futuristic vibe

**Best for:** Users who love cyberpunk, neon aesthetics, or dark themes

---

### 4. **Retro Pixel Art**
**File:** `Quill_icon_retro.ico`

**Design:**
- Warm amber/yellow color palette
- Pixelated "S" letter
- 8-bit/retro gaming style
- Nostalgic vintage feel

**Best for:** Users who love retro gaming, pixel art, or vintage aesthetics

---

## 🔧 How to Change Your Icon

### Method 1: During Installation
1. Before running `install_Quill.bat`, choose your favorite icon style
2. Rename it to `Quill_icon.ico` (replacing the existing one)
3. Run the installer - it will use your chosen icon

### Method 2: After Installation
1. Navigate to: `icons/` folder
2. Choose your favorite icon
3. Rename it to `Quill_icon.ico`
4. Run this command:
   ```batch
   cd icons
   python update_icon.py
   ```
5. Restart Windows Explorer (or reboot) to see changes

---

## 🎯 Icon Specifications

All icons include multiple resolutions for optimal display:
- **256x256** - Large icons, high DPI displays
- **128x128** - Medium icons
- **64x64** - Standard desktop view
- **48x48** - List view
- **32x32** - Small icons
- **16x16** - Tiny icons, taskbar

**Format:** `.ico` (Windows Icon)
**Transparency:** Full alpha channel support
**Compatibility:** Windows 7, 8, 10, 11

---

## 🎨 Creating Custom Icons

Want to design your own icon? Use our icon generator!

### Using the Icon Generator

```bash
cd icons
python create_icon.py        # Modify this for custom designs
```

### Design Guidelines
- Use transparent backgrounds
- Include multiple sizes (256, 128, 64, 48, 32, 16)
- Make it recognizable at small sizes (16x16)
- Use contrasting colors for visibility
- Consider dark/light mode compatibility

### Example Custom Icon Code
```python
from PIL import Image, ImageDraw

img = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Your custom design here
draw.ellipse([20, 20, 236, 236], fill=(255, 100, 150, 255))

# Save as ICO
img.save('my_custom_icon.ico', format='ICO')
```

---

## 📦 File Association

Icons are automatically associated with `.quill` files when you run the installer:

```batch
install_Quill.bat
```

This registers:
- File extension: `.quill`
- File type: "Quill Story File"
- Icon: `Quill_icon.ico`
- Default program: Quill interpreter

---

## 🔍 Preview Your Icon

Before applying, preview your icon choice:

### Windows 10/11
1. Right-click any `.quill` file
2. Go to Properties → Change icon
3. Browse to the icon file
4. See preview before applying

### Using Icon Viewer Tools
- **IrfanView** - Free image viewer with ICO support
- **IconViewer** - Windows built-in icon preview
- **VS Code** - Install "Icon Preview" extension

---

## 🎁 Icon Pack Contents

Your `icons/` folder contains:

```
icons/
├── Quill_icon.ico              ← Default (gradient book)
├── Quill_icon_minimalist.ico   ← Flat design
├── Quill_icon_neon.ico         ← Cyberpunk
├── Quill_icon_retro.ico        ← Pixel art
├── create_icon.py                    ← Main icon generator
├── create_alternate_icon.py          ← Alternative icons generator
└── update_icon.py                    ← Icon updater utility
```

---

## 💡 Tips

### Best Practices
- Choose an icon that matches your IDE/system theme
- Test icon visibility at 16x16 size (smallest view)
- Consider colorblind-friendly color schemes
- Ensure icon works on both light and dark backgrounds

### Troubleshooting
**Icon not changing after installation?**
- Clear icon cache: `ie4uinit.exe -show`
- Restart Windows Explorer
- Reboot your computer

**Icon looks blurry?**
- Ensure you're using the `.ico` file (not PNG/JPG)
- Check that multiple resolutions are included
- Verify Windows is set to 100% DPI scaling

---

## 🌈 Color Palettes Used

### Gradient Book
- Purple: `#9333EA`
- Magenta: `#EC4899`
- Pink: `#F9A8D4`

### Minimalist
- Primary Blue: `#3498DB`
- Dark Blue: `#2980B9`
- White: `#FFFFFF`

### Neon
- Background: `#141E1E`
- Neon Cyan: `#00FFFF`
- Glow: Multiple alpha layers

### Retro
- Amber: `#FFC107`
- Orange: `#FF9800`
- Brown: `#8B4513`

---

## 🚀 Next Steps

1. **Choose your icon** from the 4 available styles
2. **Preview it** to make sure you like it
3. **Install Quill** with your chosen icon
4. **Enjoy** your beautifully styled `.quill` files!

---

**Made with** 💜 **for the Quill community**

*Want to contribute your own icon design? Submit it to the Quill repository!*
