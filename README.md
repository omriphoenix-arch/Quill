# Quill - A Modern Scripting Language

A lightweight, beginner-friendly scripting language with rich error messages, comprehensive standard library, and optional game development utilities. Perfect for learning to code, automation, data processing, and interactive applications!

## Why Quill?

- **🎯 Beginner-friendly** - Natural, readable syntax that's easy to understand
- **💡 Rich error messages** - Contextual errors with hints and source excerpts
- **📚 Comprehensive stdlib** - 40+ built-in functions for common tasks
- **🧹 Clean syntax** - No semicolons, Python-like readability
- **🎮 Game-ready** - Optional built-in utilities for game development
- **⚡ Fast to learn** - Start coding in minutes

## Features

### Core Language Features
- ✅ Variables and data types (numbers, strings, booleans, lists)
- ✅ Arithmetic operations (+, -, *, /, %, **)
- ✅ Comparison operators (==, !=, <, >, <=, >=)
- ✅ Boolean logic (and, or, not)
- ✅ Conditionals (if/else/elif)
- ✅ Loops (while, for)
- ✅ Functions (with parameters and return values)
- ✅ Lists and indexing
- ✅ 40+ built-in functions (math, string, list utilities)
- ✅ Comments with #

### Output & Input
- `say` / `print` - Display output
- `ask` - Get user input
- Rich formatted output with color support

### Game Development Utilities (Optional)
- `choice` - Multiple choice selections
- `goto` and `label` - State management
- `wait()` - Timed delays
- Inventory system - Item management
- Save/Load system - Persistent state

## Quick Start

### Hello World
```python
say "Hello, World!"
# or use standard print
print "Hello, World!"
```

### Variables and Math
```python
set x = 10
set y = 20
set name = "Alice"

set sum = x + y         # 30
set power = x ** 2      # 100
say "Result: " + str(sum)
```

### Working with Lists
```python
set numbers = [3, 1, 4, 1, 5]
say "Original: " + str(numbers)
say "Sorted: " + str(sort(numbers))
say "Min: " + str(min(numbers))
say "Max: " + str(max(numbers))
say "Average: " + str(average(numbers))
```

### String Processing
```python
set text = "  Hello World  "
say "Trimmed: " + trim(text)
say "Upper: " + upper(text)
say "Lower: " + lower(text)

set words = split("apple,banana,cherry", ",")
say join(words, " - ")  # "apple - banana - cherry"
```

### Conditionals
```python
if score >= 90 then
    say "Grade: A"
else
    say "Grade: B"
end
```

### Loops
```python
# While loop
set counter = 5
while counter > 0 do
    say counter
    counter = counter - 1
end

# For loop
for i in range(1, 6) do
    say "Count: " + str(i)
end

# Loop through lists
set fruits = ["apple", "banana", "cherry"]
for fruit in fruits do
    say "I like " + fruit
end
```

### Functions
```python
function greet(name)
    say "Hello, " + name + "!"
end

function calculate_area(width, height)
    return width * height
end

greet("Alice")
set area = calculate_area(10, 5)
say "Area: " + str(area)
```

### User Input
```python
ask "What's your name?" into name
say "Nice to meet you, " + name + "!"

ask "Enter a number:" into num_str
set num = int(num_str)
say "Double: " + str(num * 2)
```

## Standard Library (40+ Functions)

### Math & Numbers
- `clamp(value, min, max)` - Constrain value between min and max
- `min(...)` / `max(...)` - Find minimum/maximum
- `sum(list)` - Sum all numbers
- `average(list)` - Calculate mean
- `round(n, decimals)` - Round number
- `floor(n)` / `ceil(n)` - Round down/up
- `sqrt(n)` - Square root
- `abs(n)` - Absolute value

### Random
- `random_choice(...)` - Pick random item
- `random_int(min, max)` - Random integer
- `random_float()` - Random 0.0-1.0

### String Utilities
- `trim(s)` - Remove whitespace
- `lower(s)` / `upper(s)` - Change case
- `capitalize(s)` / `title(s)` - Capitalize
- `split(s, delim)` - Split string
- `join(list, sep)` - Join with separator
- `replace(s, old, new)` - Replace text
- `starts_with(s, prefix)` / `ends_with(s, suffix)`
- `contains(s, substring)`

### List Utilities
- `reverse(list)` - Reverse order
- `sort(list)` - Sort items
- `len(list)` - Get length

### Type Checking
- `is_number(x)` / `is_string(x)` / `is_list(x)`
- `is_empty(x)` - Check if empty
- `type(x)` - Get type name

See `tests/test_stdlib.quill` for examples of all functions!

## Rich Error Messages

Quill provides contextual error messages with source excerpts and hints:

```
✗ SyntaxError at line 4, column 10:
  Expected THEN, got NEWLINE

     4 | if x is 5
                  ✗ ^

  💡 Hint: An 'if' statement requires 'then' before the body
```

## Game Development Features

Quill includes optional utilities perfect for text-based games and interactive fiction:

### Multiple Choice
```python
choice "Attack" or "Defend" or "Run"
# User's selection stored in 'answer' variable
if answer is "Attack" then
    say "You strike the enemy!"
end
```

### State Management
```python
# Jump to different sections
goto town_entrance

label town_entrance
say "You arrive at the town gates."
```

### Timing & Effects
- `wait(seconds)` - Pause execution (e.g., `wait(1.5)`)

### 🎒 Inventory System
- `add_item(name)` - Add item to inventory
- `remove_item(name)` - Remove item
- `has_item(name)` - Check if have item (returns true/false)
- `show_inventory()` - Display all items
- `item_count()` - Count total items
- `clear_inventory()` - Remove all items

**Perfect for game development!** See `docs/INVENTORY_SYSTEM.md` for details.

### 💾 Save/Load System (NEW!)
- `save_game(filename)` - Save game progress
- `load_game(filename)` - Load saved game
- `has_save(filename)` - Check if save exists
- `delete_save(filename)` - Delete save file

**Save files are stored in `saves/` folder!** See `docs/SAVELOAD_SYSTEM.md` for details.

## Complete Example Programs

### Calculator
```python
function add(a, b)
    return a + b
end

ask "Enter first number:" into num1
ask "Enter second number:" into num2

set result = add(int(num1), int(num2))
say "Result: " + str(result)
```

### Guessing Game
```python
set secret = randint(1, 100)
set guessed = false

while not guessed do
    ask "Guess the number (1-100):" into guess
    
    if int(guess) == secret then
        say "You got it!"
        guessed = true
    else
        if int(guess) < secret then
            say "Too low!"
        else
            say "Too high!"
        end
    end
end
```

## Running Your Programs

### Windows (After Registration)
After running the registration script, you can execute `.quill` files directly:

```powershell
# Run using the quill launcher
quill.bat your_program.quill
quill.bat examples\example_simple.quill

# Or double-click any .quill file in File Explorer!
```

To register `.quill` files and add the `quill` command to your PATH:
```powershell
powershell -ExecutionPolicy Bypass -File scripts\register_quill.ps1
```

### Unix/Linux/Mac
```bash
# Make the launcher executable (first time only)
chmod +x quill

# Run your programs
./quill your_program.quill
./quill examples/example_simple.quill
```

### Traditional Way (Any Platform)
```bash
python core\quill.py your_program.quill
```

### Unregister (Windows)
To remove the `.quill` file association and PATH entry:
```powershell
powershell -ExecutionPolicy Bypass -File scripts\unregister_quill.ps1
```

## Example Programs Included

1. **example_simple.quill** - Learn the basics
2. **example_adventure.quill** - Text adventure game
3. **example_mystery.quill** - Detective mystery game
4. **example_full_language.quill** - Showcase all features
5. **example_calculator.quill** - Interactive calculator
6. **example_guessing_game.quill** - Number guessing game
7. **example_todo_list.quill** - Todo list manager

## Language Syntax Reference

### Variable Assignment
```python
set x = 10           # Using 'set'
x = 20              # Direct assignment
```

### Operators
- Arithmetic: `+`, `-`, `*`, `/`, `%`, `**`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`
- Logical: `and`, `or`, `not`

### Control Flow
```python
if condition then
    # code
else
    # code
end

while condition do
    # code
end

for variable in iterable do
    # code
end
```

### Functions
```python
function name(param1, param2)
    # code
    return value
end
```

## Requirements

- Python 3.6 or higher
- No external dependencies!

## Custom Icons 🎨

Quill comes with **4 beautiful icon styles** for `.quill` files! Choose your favorite:

### Icon Styles
- **Gradient Book** (Default) - Modern purple-to-pink gradient with "SS" glow
- **Minimalist Flat** - Clean blue design with folded corner
- **Neon Cyberpunk** - Dark theme with cyan neon glow effect
- **Retro Pixel Art** - Vintage amber/yellow pixel style

### Preview, Change & Apply Icons
```bash
cd icons
python preview_icons.py    # See all 4 styles in a visual gallery
python update_icon.py      # Switch between icon styles
powershell -ExecutionPolicy Bypass -File apply_icon.ps1    # Apply changes!
```

When you install Quill:
- `.quill` files display your chosen icon
- Easy to identify in File Explorer
- Professional appearance for your projects

### VS Code Integration
```bash
cd .vscode-extension
powershell -ExecutionPolicy Bypass -File install_extension.ps1
```
After installation, restart VS Code to see custom icons in the file explorer!

See `docs/ICONS.md` for complete icon documentation and customization options.

## Documentation

### Getting Started
- **[documentation/QUICK_START.md](documentation/QUICK_START.md)** - Get running in 5 minutes! ⚡
- **Core Language Guide** - **[docs/core/guide.md](docs/core/guide.md)**
- **Game Utilities Guide** - **[docs/game/guide.md](docs/game/guide.md)** (optional game features)
- **[TUTORIAL.md](docs/TUTORIAL.md)** - Complete beginner's guide (start here!)
- **[ERROR_MESSAGES.md](docs/ERROR_MESSAGES.md)** - Error reference and debugging tips
- **[Quill_KEYWORDS_REFERENCE.md](docs/Quill_KEYWORDS_REFERENCE.md)** - Every keyword explained
- **[RESERVED_KEYWORDS.md](docs/RESERVED_KEYWORDS.md)** - Words you can't use as variable names

### Features & Systems
- **[INVENTORY_SYSTEM.md](docs/INVENTORY_SYSTEM.md)** - Inventory management for games
- **[SAVELOAD_SYSTEM.md](docs/SAVELOAD_SYSTEM.md)** - Save and load game progress
- **[WAIT_FUNCTION.md](docs/WAIT_FUNCTION.md)** - Timing and dramatic pauses
- **[ICONS.md](docs/ICONS.md)** - Custom file icons guide

### Development
- **[STRUCTURE.md](STRUCTURE.md)** - Project organization
- **[documentation/documentation/INSTALLATION_GUIDE.md](documentation/documentation/INSTALLATION_GUIDE.md)** - Installation instructions
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** - Community guidelines
- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[documentation/documentation/VERSION.md](documentation/documentation/VERSION.md)** - Current version info

## Installation

### Requirements

**Minimum (Required):**
- ✅ Python 3.7 or higher - [Download Python](https://www.python.org/downloads/)

**Optional (For Better Experience):**
- 🟡 VS Code - [Download VS Code](https://code.visualstudio.com/) (syntax highlighting, themes, icons)
- 🟡 Any text editor (Notepad++, Sublime Text, Vim, etc.)

> **Note:** Quill works perfectly without VS Code! You only need Python to run programs.

### Option 1: GUI Installer (Recommended)
Professional installer with visual wizard (like Python's installer):
```bash
python installer/installer/setup_gui.py
```
- ✅ Easy step-by-step wizard
- ✅ Custom installation options
- ✅ Progress tracking
- ✅ Automatic PATH setup
- ✅ File association registration

### Option 2: Console Installer
Interactive command-line installer:
```bash
python installer/installer/setup.py
```
- ✅ Full-featured installation
- ✅ Works without GUI
- ✅ Custom component selection
- ✅ Uninstaller included

### Option 3: Quick Install Scripts

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File installer/quick_installer/install.ps1
```

**macOS/Linux:**
```bash
chmod +x installer/quick_installer/install.sh
./installer/quick_installer/install.sh
```

### Option 4: Manual Install (No Installer)

**Minimum steps to run Quill:**
1. Download/clone this repository
2. Ensure Python 3.7+ is installed
3. Run programs:
   ```bash
   python core/quill.py examples/example_simple.quill
   ```

That's it! No installers, no complex setup needed.

**For detailed installation instructions**, see:
- [documentation/documentation/QUICK_START.md](documentation/documentation/QUICK_START.md) - Get started quickly
- [documentation/documentation/INSTALLATION_GUIDE.md](documentation/documentation/INSTALLATION_GUIDE.md) - Complete guide
- [documentation/documentation/INSTALLER_OPTIONS.md](documentation/documentation/INSTALLER_OPTIONS.md) - Compare installers

## Project Structure

For a detailed overview of the project organization, see [STRUCTURE.md](STRUCTURE.md).

Quick reference:
- `core/` - Language implementation (lexer, parser, interpreter)
- `examples/` - Example programs
- `games/` - Full game examples
- `installer/` - Installation tools (GUI, console, scripts)
- `docs/` - API documentation
- `documentation/` - Guides and project docs
- `tools/` - Development utilities and VS Code extension
- `resources/` - Icons and assets

## Learn More

Check out the example files to see real programs in action:
1. Start with `examples/example_simple.quill` for basics
2. Try `examples/example_guessing_game.quill` for interactive fun
3. Read **[docs/TUTORIAL.md](docs/TUTORIAL.md)** for step-by-step learning
4. Explore other examples to see advanced features
5. See [documentation/documentation/QUICK_START.md](documentation/documentation/QUICK_START.md) for quick reference

## Contributing

We welcome contributions! Quill's mission is to make programming accessible to beginners. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Version

**Current Version:** 1.0.2 (October 17, 2025)

See [documentation/documentation/VERSION.md](documentation/documentation/VERSION.md) for details and [CHANGELOG.md](CHANGELOG.md) for release notes.

Happy coding! 🚀
