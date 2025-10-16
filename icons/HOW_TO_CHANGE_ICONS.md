# 🎨 How to Change Your Quill Icons

## 🚀 Quick Guide (3 Steps!)

### Step 1: Choose Your Icon
```bash
cd icons
python preview_icons.py
```
This shows all 4 icon styles in a window. Look at them and decide which you like!

### Step 2: Switch to Your Favorite
```bash
python update_icon.py
```
Follow the prompts:
- Enter `1` for Gradient Book (default)
- Enter `2` for Minimalist Flat
- Enter `3` for Neon Cyberpunk
- Enter `4` for Retro Pixel

### Step 3: Apply the Changes! ⚠️
```bash
powershell -ExecutionPolicy Bypass -File apply_icon.ps1
```
This updates Windows to use your new icon. **Press Y to restart Explorer!**

---

## ✅ Done!

Your `.quill` files should now show the new icon!

### Not seeing the icon yet?

Try these:
1. **Navigate to a folder with .quill files**
2. **Press F5** to refresh
3. **Change view** to Large Icons or Medium Icons
4. **Restart your computer** if nothing else works

---

## 🎨 The 4 Icon Styles

### 1. 🌈 Gradient Book (Default)
- Purple to pink gradient
- Modern and colorful
- "SS" with glow effect

### 2. 📄 Minimalist Flat
- Clean blue design
- Professional look
- Material Design style

### 3. ⚡ Neon Cyberpunk
- Dark background
- Cyan neon glow
- Perfect for dark themes

### 4. 🎮 Retro Pixel
- 8-bit pixel art
- Amber/yellow colors
- Nostalgic gaming vibe

---

## 🔄 Want to Try Another Icon?

Just repeat the steps:
1. `python update_icon.py` - Choose different icon
2. `powershell -ExecutionPolicy Bypass -File apply_icon.ps1` - Apply it

You can change as many times as you want!

---

## 💡 Pro Tips

### See Icon in File Explorer
1. Open File Explorer
2. Navigate to your `games` folder (or any folder with .quill files)
3. Change view to **Medium icons** or **Large icons**
4. You should see your custom icon!

### Test with a New File
```bash
cd ..\games
notepad test.quill
# Type: say "Hello!"
# Save and close
# Look at test.quill in File Explorer - should have your icon!
```

### Clear Icon Cache (if stuck)
```bash
ie4uinit.exe -show
taskkill /f /im explorer.exe
start explorer.exe
```

---

## ❓ Troubleshooting

### Icons look the same after changing?
**Solution:** Run `apply_icon.ps1` - this is the critical step!

### "Execution Policy" error?
**Solution:** Use the full command:
```bash
powershell -ExecutionPolicy Bypass -File apply_icon.ps1
```

### Still showing old icon?
1. Check you're in the `icons` folder
2. Make sure `Quill_icon.ico` exists
3. Run `apply_icon.ps1` again
4. Restart Windows Explorer
5. Restart your computer

### Want to go back to default?
```bash
python update_icon.py
# Choose option 1 (Gradient Book)
powershell -ExecutionPolicy Bypass -File apply_icon.ps1
```

---

## 📝 Summary

**To change your icon:**
```bash
cd icons
python update_icon.py              # Pick your icon
powershell -ExecutionPolicy Bypass -File apply_icon.ps1   # Apply it!
```

**That's it!** Your .quill files will have your chosen icon. 🎉

---

## 🎁 Bonus: Web Gallery

Want to see all icons in your browser?
```bash
Start-Process icon_gallery.html
```

Beautiful web page showing all 4 styles!

---

**Made with 💜 for Quill users**

*Choose your style. Make it yours!* 🚀
