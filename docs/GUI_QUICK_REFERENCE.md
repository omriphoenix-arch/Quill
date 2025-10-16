# Quill GUI - Quick Reference

## Basic Structure

```Quill
# 1. Create window
window "Title" size "800x600" theme dark

# 2. Add GUI elements
textbox "Hello!" at 100,50
button "Click" at 100,100

# 3. Show window
show
```

## All GUI Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `window` | Create main window | `window "Game" size "800x600" theme dark` |
| `textbox` | Display styled text | `textbox "Hello!" at 100,50 color "#00ff00" size 24` |
| `label` | Simple text label | `label "Score: 0" at 10,10 color "white"` |
| `button` | Interactive button | `button "Start" at 200,100 width 150 height 50` |
| `image` | Display image | `image "bg.png" at 0,0 width 800 height 600` |
| `input` | Text input field | `input into name at 100,100 width 200` |
| `show` | Display window | `show` |
| `hide` | Hide window | `hide` |

## Common Properties

| Property | Values | Used By |
|----------|--------|---------|
| `at X,Y` | Position coordinates | All widgets |
| `color "COLOR"` | Text/foreground color | textbox, label, button |
| `bgcolor "COLOR"` | Background color | window, textbox, button, input |
| `size NUMBER` | Font size or dimensions | textbox, label, button |
| `width NUMBER` | Width in pixels | button, input, image |
| `height NUMBER` | Height in pixels | button, input, image |
| `font "NAME"` | Font family | textbox, label, button, input |
| `theme NAME` | Color theme | window |

## Themes

- **dark** - Dark background, light text
- **light** - Light background, dark text
- **game** - Game-optimized colors

## Color Formats

- Hex: `"#ff0000"`, `"#00ff00"`, `"#0000ff"`
- Names: `"red"`, `"blue"`, `"white"`, `"black"`

## Quick Examples

### Minimal Window
```Quill
window "Test"
show
```

### Styled Title
```Quill
window "Game" size "800x600"
textbox "Welcome!" at 300,100 color "#ffd700" size 32
show
```

### Button Grid
```Quill
window "Menu" size "600x400"
button "Option 1" at 200,100 width 200 height 50
button "Option 2" at 200,170 width 200 height 50
button "Option 3" at 200,240 width 200 height 50
show
```

### Input Form
```Quill
window "Login" size "500x300"
label "Username:" at 50,50
input into username at 50,80 width 400
label "Password:" at 50,140
input into password at 50,170 width 400
button "Submit" at 175,240 width 150 height 40
show
```

## Tips

✓ Create `window` first  
✓ Add all elements  
✓ Call `show` last  
✓ Use consistent colors  
✓ Test positioning  

See `docs/GUI_COMMANDS.md` for full documentation.
