# Button Callbacks - Interactive Quill GUIs

## Overview

Buttons in Quill can execute code when clicked! Use the `onclick` property to specify which function or label to call.

## Syntax

```Quill
button "Button Text" at X,Y onclick function_name
```

## How It Works

When a button is clicked, Quill can:
1. **Call a function** - Execute a defined function
2. **Jump to a label** - Go to a specific point in your code

## Function Callbacks

### Define a Function

```Quill
function my_action()
    say "Button was clicked!"
    set score to score + 10
end
```

### Connect to Button

```Quill
button "Click Me" at 100,100 onclick my_action
```

### Complete Example

```Quill
# Initialize variables
set score to 0

# Define the callback function
function add_points()
    set score to score + 10
    say "Score: " + str(score)
end

# Create GUI
window "Game" width 400 height 300
textbox "Click to earn points!" at 100,50
button "+10 Points" at 100,100 onclick add_points
show
```

## Label Callbacks

You can also jump to a label when a button is clicked:

```Quill
# Create button that jumps to label
button "Start Game" at 100,100 onclick start_game

show

label: start_game
say "Game started!"
# ... more game code ...
```

## Multiple Buttons Example

```Quill
set health to 100
set gold to 50

function heal()
    if gold >= 10 then
        set health to health + 20
        set gold to gold - 10
        say "Healed! Health: " + str(health) + ", Gold: " + str(gold)
    else
        say "Not enough gold!"
    end
end

function buy_sword()
    if gold >= 30 then
        set gold to gold - 30
        say "Bought sword! Gold remaining: " + str(gold)
    else
        say "Not enough gold!"
    end
end

# Create shop GUI
window "Shop" width 500 height 400

textbox "Welcome to the Shop!" at 150,30 size 24
textbox "Health: 100 | Gold: 50" at 150,80 size 14

button "Heal (10 gold)" at 100,150 width 150 height 50 onclick heal
button "Buy Sword (30 gold)" at 100,220 width 150 height 50 onclick buy_sword

show
```

## Interactive Counter Example

```Quill
set counter to 0

function increment()
    set counter to counter + 1
    say "Counter: " + str(counter)
end

function decrement()
    set counter to counter - 1
    say "Counter: " + str(counter)
end

function reset()
    set counter to 0
    say "Counter reset!"
end

window "Counter App" width 400 height 350

textbox "Counter: 0" at 150,50 size 24
button "+1" at 100,120 width 80 height 50 bgcolor "#00aa00" onclick increment
button "-1" at 200,120 width 80 height 50 bgcolor "#aa0000" onclick decrement
button "Reset" at 150,200 width 100 height 40 onclick reset

show
```

## Game Menu Example

```Quill
function new_game()
    say "Starting new game..."
    # Your game initialization code
end

function load_game()
    say "Loading saved game..."
    # Load game code
end

function show_settings()
    say "Opening settings..."
    # Settings code
end

function quit_game()
    say "Thanks for playing!"
    end
end

# Create main menu
window "Game Menu" width 600 height 500 theme dark

textbox "My Epic RPG" at 200,50 color "#ffd700" size 36
button "New Game" at 200,150 width 200 height 60 onclick new_game
button "Load Game" at 200,230 width 200 height 60 onclick load_game
button "Settings" at 200,310 width 200 height 60 onclick show_settings
button "Quit" at 200,390 width 200 height 60 bgcolor "#8b0000" onclick quit_game

show
```

## Tips

### 1. **Define Functions First**
Always define your functions before creating buttons:
```Quill
# ✓ Good
function my_func()
    say "Hello!"
end
button "Click" onclick my_func

# ✗ Bad
button "Click" onclick my_func  # Error: my_func not defined yet
function my_func()
    say "Hello!"
end
```

### 2. **Functions Need Parentheses**
Even if they take no parameters:
```Quill
# ✓ Correct
function click_action()
    say "Clicked!"
end

# ✗ Wrong
function click_action  # Missing ()
    say "Clicked!"
end
```

### 3. **Use Variables for State**
Track game state with variables that functions can modify:
```Quill
set game_state to "menu"
set player_level to 1

function level_up()
    set player_level to player_level + 1
    say "Level up! Now level " + str(player_level)
end
```

### 4. **Console Output**
When buttons are clicked, `say` statements print to the console. Watch the terminal to see callback messages!

## Advanced: Updating GUI Elements

Currently, GUI elements are static (created once). To create dynamic UIs:

```Quill
set lives to 3

function lose_life()
    set lives to lives - 1
    say "Lives remaining: " + str(lives)
    
    if lives <= 0 then
        say "Game Over!"
        # Jump to game over screen
        goto game_over
    end
end

window "Game" width 500 height 400
textbox "Lives: 3" at 10,10
button "Take Damage" at 100,100 onclick lose_life
show

label: game_over
say "You died!"
```

## Debugging Callbacks

If a button doesn't work:

1. **Check function name** - Must match exactly:
   ```Quill
   function my_Function()  # Capital F
   button onclick my_function  # ✗ lowercase f - won't work!
   ```

2. **Check console** - Error messages appear in terminal

3. **Test function directly** - Call it without GUI first:
   ```Quill
   function test()
       say "Testing!"
   end
   
   test()  # Should print "Testing!"
   ```

## What You Can Do

✅ Call functions when buttons clicked  
✅ Update game variables  
✅ Display messages with `say`  
✅ Jump to labels  
✅ Execute any Quill code  
✅ Multiple buttons, multiple functions  
✅ Create interactive menus, shops, dialogs  

## Examples to Try

Run these demos:
- `interactive_demo.quill` - Button callbacks with counters
- `gui_demo.quill` - Basic GUI layout

**You can now create fully interactive GUI applications in Quill!** 🎮✨
