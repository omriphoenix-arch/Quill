# Quill GUI Commands - Complete Guide

## Overview

Quill now supports creating **desktop applications** with graphical user interfaces! You can build styled windows with buttons, text, images, and interactive elements.

## Table of Contents

1. [Window Creation](#window-creation)
2. [Text Elements](#text-elements)
3. [Buttons](#buttons)
4. [Images](#images)
5. [Input Fields](#input-fields)
6. [Themes & Styling](#themes--styling)
7. [Complete Examples](#complete-examples)

---

## Window Creation

### `window` - Create Main Window

Creates the main application window.

**Syntax:**
```Quill
window "Title" size "800x600" theme dark bgcolor "#1a1a2e"
```

**Properties:**
- `size "WIDTHxHEIGHT"` - Window dimensions (e.g., `"800x600"`)
- `width NUMBER` - Window width in pixels
- `height NUMBER` - Window height in pixels
- `theme THEME_NAME` - Color theme: `dark`, `light`, or `game`
- `bgcolor "COLOR"` - Background color (hex code or name)

**Examples:**
```Quill
# Basic window
window "My Game"

# Sized window with theme
window "Adventure Quest" size "1024x768" theme dark

# Custom background color
window "Mystery Game" size "800x600" bgcolor "#2c3e50"
```

---

## Text Elements

### `textbox` - Styled Text Display

Display text with custom styling.

**Syntax:**
```Quill
textbox "Your text here" at X,Y color "#ffffff" size 24 font "Arial"
```

**Properties:**
- `at X,Y` - Position (x, y coordinates)
- `color "COLOR"` - Text color
- `bgcolor "COLOR"` - Background color
- `size NUMBER` - Font size in points
- `font "FONT_NAME"` - Font family (e.g., "Arial", "Times", "Courier")
- `align ALIGNMENT` - Text alignment: `left`, `center`, `right`

**Examples:**
```Quill
# Title text
textbox "Welcome to the Game!" at 200,50 color "#00d4ff" size 32 font "Arial"

# Subtitle
textbox "Press any button to begin" at 250,100 color "#aaaaaa" size 16

# Colored message
textbox "You found a treasure!" at 100,200 color "#ffd700" size 20
```

### `label` - Simple Text Label

Similar to textbox but typically for UI labels.

**Syntax:**
```Quill
label "Score: 100" at 10,10 color "white" size 14
```

**Properties:**
Same as `textbox`

---

## Buttons

### `button` - Interactive Button

Create clickable buttons.

**Syntax:**
```Quill
button "Button Text" at X,Y width 150 height 40 bgcolor "#0e639c" color "#ffffff" size 14 onclick function_name
```

**Properties:**
- `at X,Y` - Button position
- `width NUMBER` - Button width in pixels
- `height NUMBER` - Button height in pixels
- `color "COLOR"` - Text color
- `bgcolor "COLOR"` - Button background color
- `size NUMBER` - Text size
- `font "FONT_NAME"` - Font family
- `onclick FUNCTION` - Function to call when clicked

**Examples:**
```Quill
# Start button
button "Start Game" at 300,200 width 200 height 50 bgcolor "#0e639c" color "#ffffff" size 16

# Exit button with custom colors
button "Exit" at 300,270 width 200 height 50 bgcolor "#8b0000" color "#ffffff"

# Styled action button
button "Open Inventory" at 350,400 bgcolor "#16213e" color "#00d4ff" size 14
```

---

## Images

### `image` - Display Images

Load and display image files.

**Syntax:**
```Quill
image "path/to/image.png" at X,Y width 400 height 300
```

**Properties:**
- `at X,Y` - Image position
- `width NUMBER` - Image width (resizes)
- `height NUMBER` - Image height (resizes)
- `size "WIDTHxHEIGHT"` - Combined size specification

**Supported Formats:**
- PNG
- JPG/JPEG
- GIF
- BMP

**Examples:**
```Quill
# Background image
image "backgrounds/forest.png" at 0,0 width 800 height 600

# Character portrait
image "characters/hero.png" at 50,50 width 150 height 200

# Item icon
image "items/sword.png" at 100,100 size "64x64"
```

---

## Input Fields

### `input` - Text Input Field

Create text input fields for user input.

**Syntax:**
```Quill
input into variable_name at X,Y width 200 height 30
```

**Properties:**
- `into VARIABLE` - Variable to store input value
- `at X,Y` - Input position
- `width NUMBER` - Input width
- `height NUMBER` - Input height
- `color "COLOR"` - Text color
- `bgcolor "COLOR"` - Background color
- `font "FONT_NAME"` - Font family

**Examples:**
```Quill
# Player name input
input into player_name at 300,200 width 250 height 35

# Password field
input into password at 300,250 width 250 bgcolor "#333333" color "#ffffff"

# Styled input
input into answer at 200,400 width 400 height 40 font "Arial" size 16
```

**Reading Input Values:**
```Quill
input into username at 300,200 width 200
show

# Later in your code, access the value:
say "Hello, " + username
```

---

## Control Commands

### `show` - Display Window

Makes the window visible and updates all elements.

**Syntax:**
```Quill
show
```

### `hide` - Hide Window

Hides the window temporarily.

**Syntax:**
```Quill
hide
```

**Example:**
```Quill
window "Loading..."
textbox "Please wait..." at 300,250
show
wait(2)
hide
```

---

## Themes & Styling

### Built-in Themes

Quill includes three built-in themes:

#### **Dark Theme** (default)
```Quill
window "Game" theme dark
```
- Background: `#1e1e1e`
- Text: `#ffffff`
- Button: `#0e639c`
- Input: `#3c3c3c`

#### **Light Theme**
```Quill
window "Game" theme light
```
- Background: `#ffffff`
- Text: `#000000`
- Button: `#0078d4`
- Input: `#f0f0f0`

#### **Game Theme**
```Quill
window "Game" theme game
```
- Background: `#1a1a2e`
- Text: `#eeeeee`
- Button: `#16213e`
- Input: `#0f3460`

### Color Formats

Colors can be specified as:
- **Hex codes**: `"#ff0000"`, `"#00ff00"`, `"#0000ff"`
- **Named colors**: `"red"`, `"blue"`, `"green"`, `"white"`, `"black"`

---

## Complete Examples

### Example 1: Simple Menu

```Quill
# Create window
window "Main Menu" size "600x400" theme dark

# Title
textbox "My Awesome Game" at 150,50 color "#00d4ff" size 28 font "Arial"

# Buttons
button "New Game" at 200,150 width 200 height 50 bgcolor "#0e639c" color "#ffffff" size 16
button "Load Game" at 200,220 width 200 height 50 bgcolor "#16213e" color "#ffffff" size 16
button "Exit" at 200,290 width 200 height 50 bgcolor "#8b0000" color "#ffffff" size 16

# Show window
show

say "Main menu displayed!"
```

### Example 2: Character Creation

```Quill
# Setup window
window "Create Your Character" size "800x600" theme game

# Title
textbox "Character Creation" at 250,30 color "#ffd700" size 32 font "Arial"

# Instructions
textbox "Enter your character name:" at 250,100 color "#ffffff" size 16

# Name input
input into character_name at 250,140 width 300 height 40 bgcolor "#0f3460" color "#ffffff"

# Class selection text
textbox "Choose your class:" at 250,200 color "#ffffff" size 16

# Class buttons
button "Warrior" at 100,250 width 150 height 50 bgcolor "#8b0000" color "#ffffff"
button "Mage" at 300,250 width 150 height 50 bgcolor "#4169e1" color "#ffffff"
button "Rogue" at 500,250 width 150 height 50 bgcolor "#228b22" color "#ffffff"

# Confirm button
button "Create Character" at 300,400 width 200 height 60 bgcolor "#ffd700" color "#000000" size 18

# Show the GUI
show

say "Character creator is open!"
say "Enter your name and select a class."
```

### Example 3: Game with Background

```Quill
# Create game window
window "Fantasy Adventure" size "1024x768" theme game

# Background image
image "assets/forest_background.png" at 0,0 width 1024 height 768

# Game title overlay
textbox "The Enchanted Forest" at 300,50 color "#ffd700" size 36 font "Times"

# Character image
image "assets/hero.png" at 50,400 width 150 height 250

# Dialog box
textbox "You enter a mysterious forest..." at 250,600 bgcolor "#000000" color "#ffffff" size 18

# Action buttons
button "Explore North" at 100,700 width 150 height 40
button "Check Inventory" at 300,700 width 150 height 40
button "Rest" at 500,700 width 150 height 40

# Stats display
label "HP: 100/100" at 10,10 color "#00ff00" size 14
label "MP: 50/50" at 10,30 color "#0000ff" size 14
label "Gold: 250" at 10,50 color "#ffd700" size 14

show

say "Welcome to the adventure!"
```

### Example 4: Interactive Quiz

```Quill
# Quiz window
window "Trivia Quiz" size "700x500" theme light

# Question
textbox "What is 2 + 2?" at 50,50 color "#000000" size 24

# Answer input
input into user_answer at 50,120 width 200 height 40

# Submit button
button "Submit Answer" at 50,180 width 200 height 50 bgcolor "#0078d4" color "#ffffff"

# Result display area
label "Your answer will appear here" at 50,260 color "#666666" size 16

show

say "Quiz is ready!"
```

---

## Tips & Best Practices

### 1. **Window First**
Always create the window before adding any other GUI elements:
```Quill
window "My Game" size "800x600" theme dark
# Now add buttons, text, etc.
```

### 2. **Show to Display**
Call `show` after creating all your GUI elements to display the window:
```Quill
window "Game"
button "Start" at 100,100
textbox "Welcome!" at 100,50
show  # This makes everything visible
```

### 3. **Positioning**
- Coordinates start at (0,0) in the top-left corner
- X increases to the right
- Y increases downward
- Plan your layout on paper first!

### 4. **Color Consistency**
Use consistent colors throughout your UI for a professional look:
```Quill
# Define a color scheme
# Primary: #0e639c
# Secondary: #16213e
# Accent: #00d4ff
```

### 5. **Responsive Sizes**
Make sure text and buttons are readable:
- **Titles**: 24-36pt
- **Body text**: 14-18pt
- **Buttons**: At least 40px height
- **Input fields**: At least 30px height

### 6. **Image Paths**
Use relative paths from your game's directory:
```Quill
image "assets/background.png"  # Good
image "C:\full\path\bg.png"    # Avoid absolute paths
```

---

## Combining GUI with Traditional Quill

You can mix GUI elements with traditional text-based gameplay:

```Quill
# Show GUI menu
window "Adventure" size "800x600"
button "Start" at 300,200
button "Quit" at 300,270
show

# Continue with text game
say "Welcome to the adventure!"
choice "Enter the cave" or "Go to town"

if answer is "Enter the cave" then
    # Hide GUI, switch to text mode
    hide
    say "You enter a dark cave..."
    say "You hear strange noises..."
end
```

---

## Next Steps

- Try the `gui_demo.quill` example
- Experiment with different themes and colors
- Combine GUI with your existing Quill games
- Create custom button layouts for different game screens

**Happy GUI programming!** 🎨🎮
