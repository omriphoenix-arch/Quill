# Quill Natural Language Syntax Reference
## All Keywords - Original + New Natural Alternatives

---

## 📢 OUTPUT COMMANDS
Display text to the console

**Original:** `say`
**Alternatives:** `speak`, `tell`, `write`, `print`

```Quill
say "Hello!"
speak "Hello!"
tell "Hello!"
write "Hello!"
print "Hello!"
```

---

## 📝 VARIABLES
Create and assign variables

**Original:** `set ... to ...`
**Alternatives:** `let ... equals ...`, `make ... to ...`, `create ... to ...`

```Quill
set score to 100
let health equals 50
make coins to 25
create lives to 3
```

---

## ❓ INPUT
Get user input from console

**Original:** `ask ... into ...`
**Alternatives:** `prompt ... into ...`, `question ... into ...`

```Quill
ask "Your name?" into player_name
prompt "Your age?" into age
question "Favorite color?" into color
```

---

## 🔀 CONDITIONALS
If/else statements

**Original:** `if ... then ... else ... end`
**Alternatives:** 
- `when ... then ... otherwise ... finish`
- `when ... then ... otherwise ... done`

```Quill
if score is 100 then
    say "Perfect!"
else
    say "Keep trying!"
end

when health is 0 then
    speak "Game Over!"
otherwise
    speak "Keep playing!"
finish
```

---

## 🎯 CHOICES
Present options to the user

**Original:** `choice ... or ...`
**Alternatives:** `choose ...`, `select ...`, `option ...`

```Quill
choice "Attack" or "Defend" or "Run"
choose "Red" or "Blue" or "Green"
select "Yes" or "No"
option "Continue" or "Quit"
```

---

## 🔄 LOOPS
While loops

**Original:** `while ... do ... end`
**Alternatives:** `repeat while ... do ... finish`

```Quill
while count is 10 do
    say "Counting..."
end

repeat while playing do
    speak "Game running..."
finish
```

---

## 🏷️ FUNCTIONS
Define reusable code

**Original:** `function name() ... return ... end`
**Alternatives:** 
- `func`, `def`, `define`
- `give` instead of `return`
- `done`, `finish` instead of `end`

```Quill
function greet()
    say "Hello!"
    return "done"
end

define calculate()
    speak "Calculating..."
    give 42
finish
```

---

## 🎮 GUI COMMANDS
Create graphical interfaces

### Window
**Original:** `window`
**Alternatives:** `screen`

```Quill
window "My Game" width 800 height 600
screen "My App" width 600 height 400
```

### Button
**Original:** `button`
**Alternatives:** `btn`

```Quill
button "Click Me" at 100,100
btn "Start" position 50,50
```

### Text Display
**Original:** `textbox`
**Alternatives:** `text`

```Quill
textbox "Welcome!" at 10,10 color "#00ff00"
text "Score: 0" pos 10,50 colour "#ffffff"
```

### Image
**Original:** `image`
**Alternatives:** `img`, `picture`

```Quill
image "hero.png" at 0,0
img "background.jpg" position 0,0
```

### Input Field
**Original:** `input`
**Alternatives:** `textfield`, `field`

```Quill
input player_name at 100,100 width 200
field email pos 50,150 width 250
```

---

## 🎨 GUI PROPERTIES

### Position
**Original:** `at`
**Alternatives:** `position`, `pos`

### Colors
**Original:** `color`, `bgcolor`
**Alternatives:** `colour`, `foreground`, `background`, `bg`

### Click Events
**Original:** `onclick`
**Alternatives:** `click`, `press`

### Identification
**Original:** `id`
**Alternatives:** `name`

### Display Control
**Original:** `show`, `hide`
**Alternatives:** `display/open`, `close`

### Updates
**Original:** `update`
**Alternatives:** `change`, `modify`

```Quill
# All of these work:
button "Test" at 10,10 color "#fff" bgcolor "#000" onclick my_func
btn "Test" pos 10,10 colour "#fff" background "#000" click my_func press my_func

textbox "Hello" at 50,50 id my_text
text "Hello" position 50,50 name my_text

update my_text to "New text"
change my_text to "New text"
modify my_text to "New text"

show
open
display
```

---

## ✨ COMPLETE EXAMPLE

```Quill
# Using all natural language keywords!

speak "Welcome to the adventure!"

prompt "What's your hero name?" into hero_name
tell "Welcome, " + hero_name + "!"

let gold equals 100
make health to 50
create experience to 0

define battle()
    speak "Entering battle!"
    make experience to experience + 10
    give "Victory!"
finish

choose "Fight Monster" or "Visit Shop" or "Rest"

when answer is "Fight Monster" then
    battle()
    write "You won!"
otherwise
    tell "You chose wisely."
finish

# Create a game screen
screen "RPG Adventure" width 800 height 600

text "Hero: " + hero_name pos 20,20 colour "#gold" size 20
text "Gold: " + str(gold) position 20,50 colour "#yellow"
text "Health: " + str(health) pos 20,80 colour "#red"

btn "Fight" at 20,150 width 120 height 50 background "#8b0000" colour "#fff" click battle

open

speak "Game window is now visible!"
```

---

## 🎯 KEY POINTS

1. **All original keywords still work** - Nothing is deprecated
2. **Mix and match** - Use `say` and `speak` in the same file
3. **More readable** - Choose keywords that make sense for your game
4. **Beginner-friendly** - Natural words like `when`, `choose`, `speak` are easier to learn

---

**Total Keywords Added: 50+ natural language alternatives!**
