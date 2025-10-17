# 🎨 Quill Icons

Welcome to the Quill Icon System! Choose from **4 beautiful icon styles** for your `.quill` files.

## 🖼️ Quick Preview

Open the visual gallery in your browser:
```bash
# Windows
Start-Process icon_gallery.html

# Or double-click: icon_gallery.html
```

Or use the Python preview tool:
```bash
python preview_icons.py
```

---

## 🎯 Available Icons

| Icon | Style | Colors | Best For |
|------|-------|--------|----------|
| 🌈 **Gradient Book** | Modern gradient | Purple → Pink | Default, colorful themes |
| 📄 **Minimalist Flat** | Material Design | Blue | Professional, clean UI |
| ⚡ **Neon Cyberpunk** | Glowing neon | Cyan on dark | Dark themes, cyberpunk |
| 🎮 **Retro Pixel** | 8-bit style | Amber/Orange | Vintage, retro gaming |

---

## ⚡ Quick Commands

### Preview Icons
```bash
python preview_icons.py          # Visual gallery (recommended)
Start-Process icon_gallery.html  # Web browser gallery
```

### Switch Icons
```bash
python update_icon.py
# Follow the interactive prompts
```

### Apply Icon Changes ⚠️ IMPORTANT
```bash
powershell -ExecutionPolicy Bypass -File apply_icon.ps1
# This applies the icon to your .quill files!
```

### Generate Icons
```bash
python create_icon.py              # Default gradient book
python create_alternate_icon.py    # All 3 alternatives
```

---

## 📁 Files in This Folder

### Icon Files (.ico)
- `Quill_icon.ico` - **Gradient Book** (Default)
- `Quill_icon_minimalist.ico` - Flat Design
- `Quill_icon_neon.ico` - Cyberpunk Neon
- `Quill_icon_retro.ico` - Pixel Art

### Tools
- `preview_icons.py` - Visual icon gallery (Tkinter)
- `update_icon.py` - Interactive icon switcher
- `create_icon.py` - Generate default icon
- `create_alternate_icon.py` - Generate all alternatives

### Documentation
- `ICON_SUMMARY.md` - Complete summary of icon system
- `icon_gallery.html` - Web-based icon gallery

---

## 🔧 How to Change Your Icon

### Method 1: Interactive Tool (Recommended)
```bash
python update_icon.py
```
Select your favorite from the menu!

### Method 2: Manual Rename
```bash
# Choose your favorite (example: neon)
copy Quill_icon_neon.ico Quill_icon.ico

# Re-run installer to apply
cd ..
install_Quill.bat
```

### Method 3: Before Installation
1. Rename your favorite to `Quill_icon.ico`
2. Run `install_Quill.bat`
3. Done! Your chosen icon is applied

---

## 🎨 Icon Specifications

**Format:** Windows Icon (.ico)  
**Resolutions:** 256×256, 128×128, 64×64, 48×48, 32×32, 16×16  
**Color Depth:** 32-bit RGBA (full transparency)  
**Quality:** Anti-aliased, professional grade  

---

## 💡 Which Icon Should I Choose?

### 🌈 Gradient Book (Default)
**Choose if you:**
- ✅ Want modern, colorful aesthetics
- ✅ Like gradients and glow effects
- ✅ Use light or dark themes
- ✅ Want maximum visual appeal

### 📄 Minimalist Flat
**Choose if you:**
- ✅ Prefer clean, simple designs
- ✅ Like Material Design
- ✅ Need professional appearance
- ✅ Use light themes

### ⚡ Neon Cyberpunk
**Choose if you:**
- ✅ Love dark themes
- ✅ Want futuristic/cyberpunk vibes
- ✅ Like neon glow effects
- ✅ Use dark IDE themes

### 🎮 Retro Pixel
**Choose if you:**
- ✅ Love retro gaming
- ✅ Want 8-bit nostalgia
- ✅ Like pixel art
- ✅ Want warm, vintage colors

---

## 📚 Full Documentation

For complete documentation, see:
- `../docs/ICONS.md` - Complete icon guide
- `../docs/ICON_REFERENCE.md` - Quick reference
- `ICON_SUMMARY.md` - Summary of icon system

---

## 🎓 Creating Custom Icons

Want to design your own? Edit `create_icon.py`:

```python
# Change colors (line ~30-50)
r = int(147 + (255 - 147) * ratio)  # Red channel
g = int(51 + (105 - 51) * ratio)    # Green channel
b = int(234 + (180 - 234) * ratio)  # Blue channel

# Then regenerate
python create_icon.py
```

---

## 🐛 Troubleshooting

**Icon not changing after update?**
```bash
# Method 1: Restart Windows Explorer
# Press Ctrl+Shift+Esc → Find "Windows Explorer" → Restart

# Method 2: Clear icon cache
ie4uinit.exe -show

# Method 3: Reboot computer
shutdown /r /t 0
```

**Icon looks blurry?**
- Ensure you're using `.ico` files (not PNG)
- Check Windows DPI scaling (100% recommended)
- Verify icon contains multiple resolutions

**Preview tool doesn't work?**
```bash
# Install dependencies
pip install pillow
```

---

## 📦 Requirements

- **Python 3.6+** for tools
- **Pillow** for icon generation: `pip install pillow`
- **Windows 7+** for icon display

---

## 🚀 Quick Start Guide

### First Time Setup
```bash
# 1. Preview all icons
python preview_icons.py

# 2. Choose your favorite
python update_icon.py

# 3. Install Quill
cd ..
install_Quill.bat

# 4. Enjoy your custom icon! 🎉
```

---

## 🌟 Examples

### All 4 Icons Side-by-Side
```
┌──────────────┬──────────────┬──────────────┬──────────────┐
│   GRADIENT   │  MINIMALIST  │     NEON     │    RETRO     │
│              │              │              │              │
│     🌈📖     │     📄       │     ⚡💠     │     🎮📦     │
│      SS      │    ▬▬▬▬      │      S       │     ▚▚▚      │
│              │              │              │              │
│   Colorful   │    Clean     │   Glowing    │   Nostalgic  │
│    Modern    │ Professional │  Dark Theme  │    8-bit     │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

---

## 💬 Community

Found a bug? Want to contribute a new icon style?
- Check `../README.md` for project info
- See `../docs/` for full documentation
- Create custom variants and share!

---

## 📄 License

Part of the Quill project. Same license as main project.

---

**Choose your style. Make Quill yours!** 🎨✨

*Happy coding with beautiful icons!* 🚀
