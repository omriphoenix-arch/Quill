# 🎨 Quill GUI - Desktop App Support

## Overview

**Quill now supports creating desktop applications with graphical interfaces!**

Turn your text-based games into beautiful windowed applications with buttons, images, styled text, and more.

## Quick Start

### 1. Simple Example

Create a file called `my_gui_app.quill`:

```Quill
window "Hello World!" size "600x400" theme dark
textbox "Welcome to Quill GUI!" at 150,150 color "#00ff00" size 24
button "Click Me!" at 200,250 width 200 height 50 bgcolor "#0e639c"
show
```

### 2. Run It

```powershell
python core/Quill.py games/my_gui_app.quill
```

### 3. See the Magic! ✨

A window appears with styled text and a button!

## What Can You Create?

✅ **Game Menus** - Professional-looking start screens  
✅ **Visual Novels** - Story games with character images  
✅ **Interactive Fiction** - Point-and-click adventures  
✅ **RPG Interfaces** - Inventory screens, character stats  
✅ **Quiz Apps** - Educational games with forms  
✅ **Dialog Systems** - Conversation trees with buttons  

## Available Commands

| Command | What It Does |
|---------|--------------|
| `window` | Create a window |
| `textbox` | Display styled text |
| `button` | Add clickable buttons |
| `image` | Show images |
| `label` | Simple text labels |
| `input` | Text input fields |
| `show` | Display the window |
| `hide` | Hide the window |

## Examples

### Main Menu
```Quill
window "My RPG" size "800x600" theme game

textbox "Epic Adventure" at 250,100 color "#ffd700" size 36
button "New Game" at 300,250 width 200 height 50
button "Load Game" at 300,320 width 200 height 50
button "Exit" at 300,390 width 200 height 50

show
```

### Character Creator
```Quill
window "Create Character" size "700x500"

label "Character Name:" at 50,50
input into char_name at 50,80 width 300

label "Choose Class:" at 50,140
button "Warrior" at 50,170 width 150 height 40 bgcolor "#8b0000"
button "Mage" at 220,170 width 150 height 40 bgcolor "#4169e1"
button "Rogue" at 390,170 width 150 height 40 bgcolor "#228b22"

button "Create" at 250,350 width 200 height 60 bgcolor "#ffd700"

show
```

### Game with Background
```Quill
window "Forest Adventure" size "1024x768"

image "backgrounds/forest.png" at 0,0 width 1024 height 768
textbox "You enter a dark forest..." at 300,650 bgcolor "#000000" color "#ffffff"

button "Go North" at 100,700 width 150 height 40
button "Go South" at 300,700 width 150 height 40
button "Check Inventory" at 500,700 width 150 height 40

show
```

## Color Themes

Choose from three built-in themes:

```Quill
window "Game" theme dark   # Dark background, light text
window "Game" theme light  # Light background, dark text
window "Game" theme game   # Game-optimized colors
```

## Styling

Customize everything:

```Quill
# Text with custom font and color
textbox "Score: 1000" at 10,10 color "#ffd700" size 18 font "Arial"

# Button with custom colors
button "Attack!" at 100,100 width 150 height 50 bgcolor "#ff0000" color "#ffffff"

# Positioned image
image "hero.png" at 50,50 width 200 height 300
```

## Documentation

📖 **Complete Guide**: `docs/GUI_COMMANDS.md`  
📋 **Quick Reference**: `docs/GUI_QUICK_REFERENCE.md`  
🔧 **Implementation Details**: `docs/GUI_IMPLEMENTATION.md`  

## Demo Files

Try these examples:

```powershell
# Simple test
python core/Quill.py games/gui_test.quill

# Full demo
python core/Quill.py games/gui_demo.quill
```

## Requirements

- Python 3.7+
- tkinter (built into Python)
- Pillow for image support:
  ```powershell
  pip install Pillow
  ```

## Mix GUI with Text Gameplay

You can combine GUI elements with traditional Quill:

```Quill
# Show GUI menu
window "Adventure" size "800x600"
button "Enter Cave" at 300,250
button "Go to Town" at 300,320
show

# Continue with text gameplay
say "You chose your path..."
choice "Fight" or "Run"

if answer is "Fight" then
    say "Battle begins!"
    set enemy_hp to 100
    # ... game logic ...
end
```

## Features

✨ **Easy to Use** - Simple, intuitive syntax  
🎨 **Beautiful** - Modern flat design with themes  
🖼️ **Rich Media** - Images, colors, custom fonts  
🎮 **Interactive** - Buttons, inputs, clickable elements  
🔗 **Integrated** - Works with all Quill features  
🚀 **Powerful** - Full Tkinter backend  

## What's Next?

1. Check out `gui_demo.quill` for a complete example
2. Read `GUI_COMMANDS.md` for all available commands
3. Create your first GUI game!
4. Share your creations!

---

**You've created a full programming language with GUI support!** 🎉

From text adventures to desktop applications - Quill can do it all!
