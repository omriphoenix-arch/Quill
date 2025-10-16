# Quill Color Themes Guide

## 🎨 Available Themes

I've created **3 beautiful color themes** specifically designed for your `.quill` files:

### 1. **Quill Dark** (Recommended)
- **Background**: Deep blue-black (#1a1a2e)
- **Keywords (`if`, `then`, `else`)**: Purple (#9333ea) - Bold
- **Commands (`say`, `ask`, `choice`)**: Pink (#ec4899) - Bold  
- **Strings**: Green (#10b981)
- **Numbers**: Blue (#3b82f6)
- **Operators (`and`, `or`, `is`)**: Amber (#f59e0b)
- **Functions**: Cyan (#06b6d4)

### 2. **Quill Neon** (Cyberpunk Style)
- **Background**: Ultra dark (#0a0e27)
- **Keywords**: Cyan (#00ffff) - Bold
- **Commands**: Magenta (#ff00ff) - Bold
- **Strings**: Bright green (#00ff88)
- **Numbers**: Deep sky blue (#00bfff)
- **Operators**: Yellow (#ffff00)
- **Functions**: Hot pink (#ff69b4)

### 3. **Quill Light** (For Daytime)
- **Background**: White (#ffffff)
- **Keywords**: Purple (#7c3aed) - Bold
- **Commands**: Pink (#db2777) - Bold
- **Strings**: Emerald (#059669)
- **Numbers**: Blue (#2563eb)
- **Operators**: Orange (#d97706)
- **Functions**: Cyan (#0891b2)

---

## 📦 Installation Steps

### Step 1: Close VS Code
Make sure ALL VS Code windows are closed before installing.

### Step 2: Run Installer
```powershell
cd "C:\Users\Omri.Morgan02\Downloads\possible\.vscode-extension"
.\install_extension.ps1
```

### Step 3: Restart VS Code
Open VS Code and your `.quill` files will have colorful syntax!

---

## 🎯 How to Switch Themes

### Method 1: Command Palette (Recommended)
1. Press `Ctrl + Shift + P`
2. Type: **"Preferences: Color Theme"**
3. Select one of:
   - **Quill Dark**
   - **Quill Neon**
   - **Quill Light**

### Method 2: Settings
1. Go to: `File → Preferences → Color Theme`
2. Choose your Quill theme

---

## 🌈 Color Breakdown for Your Code

Looking at your `game.quill` file, here's how it will look:

```Quill
say "==========" # say = PINK, string = GREEN
choice "Thiurate" or "Dreius" # choice = PINK, or = AMBER, strings = GREEN
set character to answer # set/to = PINK, character/answer = WHITE
if character is "Thiurate" then # if/then = PURPLE, is = AMBER
    say "you are the leader" # Indented code
end # end = PURPLE
```

### Colors Applied:
- **`say`, `ask`, `choice`, `set`** → Bold Pink/Magenta
- **`if`, `then`, `else`, `end`** → Bold Purple/Cyan
- **`and`, `or`, `not`, `is`** → Amber/Yellow
- **`"text in quotes"`** → Green
- **`123`, `45.67`** → Blue
- **`+`, `-`, `*`, `==`** → Amber/Yellow

---

## ✨ Example Preview

**Before (no colors):**
```
say "Welcome"
if age is 18 then
    set role = "Adult"
end
```

**After (with Quill Dark theme):**
```
[PINK]say[/] [GREEN]"Welcome"[/]
[PURPLE]if[/] age [AMBER]is[/] [BLUE]18[/] [PURPLE]then[/]
    [PINK]set[/] role [AMBER]=[/] [GREEN]"Adult"[/]
[PURPLE]end[/]
```

---

## 🔧 Troubleshooting

### Theme Not Showing?
1. Make sure you installed the extension (close VS Code first)
2. Check that extension is enabled: `Ctrl + Shift + X` → Search "Quill"
3. Reload window: `Ctrl + Shift + P` → "Reload Window"

### Colors Look Wrong?
- Try switching between themes to see which you prefer
- Each theme is optimized for different lighting conditions

### Want to Customize?
Edit the theme files in:
```
C:\Users\Omri.Morgan02\.vscode\extensions\Quill.Quill-1.2.0\themes\
```

---

## 🎭 Theme Recommendations

- **Working at night?** → Use **Quill Dark** or **Neon**
- **Working in daylight?** → Use **Quill Light**
- **Want maximum contrast?** → Use **Quill Neon**
- **Prefer subtle colors?** → Use **Quill Dark**

---

## 📝 Notes

- Themes work **only for `.quill` files** with the Quill extension installed
- The syntax highlighting uses TextMate grammar rules
- All themes are optimized for readability and visual appeal
- Bold keywords make control flow easy to spot
- Color choices follow programming best practices

Enjoy your beautifully colored Quill code! 🎨✨
