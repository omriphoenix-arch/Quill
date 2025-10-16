# Quill - A Beginner-Friendly Programming Language

A complete programming language designed to help new programmers learn to code with simple, readable syntax! Perfect for beginners, text-based games, and general programming.

## Why Quill?

- **Beginner-friendly** - Natural, readable syntax that's easy to understand
- **Full-featured** - Functions, loops, lists, math, and more!
- **No semicolons** - Clean, Python-like syntax without unnecessary punctuation
- **Great error messages** - Helpful feedback when something goes wrong
- **Perfect for games** - Built-in commands make text adventures easy

## Features

### Core Language Features
- ✅ Variables and data types (numbers, strings, booleans, lists)
- ✅ Arithmetic operations (+, -, *, /, %, **)
- ✅ Comparison operators (==, !=, <, >, <=, >=)
- ✅ Boolean logic (and, or, not)
- ✅ Conditionals (if/else)
- ✅ Loops (while, for)
- ✅ Functions (with parameters and return values)
- ✅ Lists and indexing
- ✅ Built-in functions (len, min, max, sum, range, random, etc.)
- ✅ Comments with #

### Game-Focused Features
- `say` - Display messages
- `ask` - Get player input
- `choice` - Multiple choice selections
- `goto` and `label` - Story branching
- `wait()` - Pause execution for dramatic timing

## Quick Start

### Variables and Math
```python
set x = 10
set y = 20
set name = "Alice"

set sum = x + y         # 30
set power = x ** 2      # 100
say "Result: " + str(sum)
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

function add(a, b)
    return a + b
end

greet("Bob")
set result = add(10, 20)
say "Sum: " + str(result)
```

### Lists
```python
set numbers = [1, 2, 3, 4, 5]
say numbers[0]           # First element: 1
say len(numbers)         # Length: 5

# Iterate through lists
for num in numbers do
    say num
end
```

## Built-in Functions

### Core Functions
- `len(x)` - Get length of list or string
- `str(x)` - Convert to string
- `int(x)` - Convert to integer
- `float(x)` - Convert to float
- `min(...)` - Find minimum value
- `max(...)` - Find maximum value
- `sum(list)` - Sum all numbers in list
- `range(start, end)` - Create list of numbers
- `abs(x)` - Absolute value
- `random()` - Random number 0-1
- `randint(a, b)` - Random integer between a and b

### ⏱️ Timing Functions
- `wait(seconds)` - Pause for specified seconds (can use decimals like 1.5)

**Create dramatic pauses and control pacing!** See `docs/WAIT_FUNCTION.md` for details.

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
- **[QUICK_START.md](QUICK_START.md)** - Get running in 5 minutes! ⚡
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
- **[INSTALL.md](INSTALL.md)** - Installation instructions
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** - Community guidelines
- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[VERSION.md](VERSION.md)** - Current version info

## Installation

### Requirements

**Minimum (Required):**
- ✅ Python 3.8 or higher - [Download Python](https://www.python.org/downloads/)

**Optional (For Better Experience):**
- 🟡 VS Code - [Download VS Code](https://code.visualstudio.com/) (syntax highlighting, themes, icons)
- 🟡 Any text editor (Notepad++, Sublime Text, Vim, etc.)

> **Note:** Quill works perfectly without VS Code! You only need Python to run programs.

### Quick Install (Recommended)

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
```

**macOS/Linux:**
```bash
chmod +x install.sh
./install.sh
```

The installer will:
- ✅ Check Python version (requires 3.8+)
- ✅ Create launcher commands (`quill.bat` / `quill`)
- ✅ Register `.quill` file association (Windows)
- ✅ Add to PATH (optional)
- ✅ Configure VS Code extension (if VS Code is installed)
- ✅ Test your installation

### Manual Install (Without Installer)

**Minimum steps to run Quill:**
1. Download/clone this repository
2. Ensure Python 3.8+ is installed
3. Run programs:
   ```bash
   python core/quill.py examples/example_simple.quill
   ```

That's it! No VS Code, no installers, no complex setup needed.

**For more convenience:**
- Run the installer scripts above, or
- See [INSTALL.md](INSTALL.md) for detailed manual setup

## Learn More

Check out the example files to see real programs in action:
1. Start with `example_simple.quill` for basics
2. Try `example_guessing_game.quill` for interactive fun
3. Read **[docs/TUTORIAL.md](docs/TUTORIAL.md)** for step-by-step learning
4. Explore other examples to see advanced features

## Contributing

We welcome contributions! Quill's mission is to make programming accessible to beginners. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Version

**Current Version:** 1.0.0 (October 15, 2025)

See [VERSION.md](VERSION.md) for details and [CHANGELOG.md](CHANGELOG.md) for release notes.

Happy coding! 🚀
