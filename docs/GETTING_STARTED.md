# Getting Started with Quill

Welcome to **Quill** - your own programming language! 🎉

## What You've Built

You now have a complete, working programming language with:

✅ **Full programming features** - Variables, loops, functions, lists
✅ **Beginner-friendly syntax** - Easy to read and write
✅ **Game-focused tools** - Perfect for text adventures
✅ **Python-like** - But simpler for beginners

## Quick Start (5 Minutes)

### 1. Your First Program

Create a file called `hello.quill`:

```python
say "Hello, World!"
ask "What's your name?" into name
say "Nice to meet you, " + name + "!"
```

Run it:
```bash
python Quill.py hello.quill
```

### 2. Try the Tutorial

```bash
python Quill.py tutorial.quill
```

This interactive tutorial teaches you everything!

### 3. Try the Examples

We've included 7 complete example programs:

```bash
python Quill.py example_simple.quill          # Learn basics
python Quill.py example_adventure.quill       # Cave adventure
python Quill.py example_mystery.quill         # Detective game
python Quill.py example_full_language.quill   # All features
python Quill.py example_calculator.quill      # Calculator app
python Quill.py example_guessing_game.quill   # Number game
python Quill.py example_todo_list.quill       # Todo manager
```

## File Structure

```
possible/
├── Quill.py          # Main interpreter (run your programs)
├── lexer.py               # Tokenizer (breaks code into pieces)
├── parser.py              # Parser (understands grammar)
├── interpreter.py         # Executor (runs your code)
│
├── README.md              # Overview and quick reference
├── LANGUAGE_REFERENCE.md  # Complete language documentation
├── GETTING_STARTED.md     # This file!
│
└── Examples:
    ├── tutorial.quill              # Interactive tutorial
    ├── example_simple.quill        # Basics
    ├── example_adventure.quill     # Text adventure
    ├── example_mystery.quill       # Detective game
    ├── example_full_language.quill # Feature showcase
    ├── example_calculator.quill    # Calculator
    ├── example_guessing_game.quill # Guessing game
    └── example_todo_list.quill     # Todo list app
```

## What Can You Do With Quill?

### 1. Learn Programming
Perfect first language - all the concepts of real programming!

### 2. Make Text Games
Built-in commands make interactive fiction easy:
- `say` - Display text
- `ask` - Get user input  
- `choice` - Multiple choice questions
- `goto` and `label` - Story branching

### 3. Build Real Programs
It's Turing-complete! You can write:
- Calculators
- Todo lists
- Quiz programs
- Simple algorithms
- Data processing

### 4. Teach Others
Great for teaching programming concepts to beginners.

## Language Features

### ✅ Core Programming

```python
# Variables
set x = 10
set name = "Alice"
set list = [1, 2, 3]

# Math
set sum = x + 5
set power = x ** 2

# Conditionals
if x > 5 then
    say "Big number!"
end

# Loops
while x > 0 do
    say x
    x = x - 1
end

for item in list do
    say item
end

# Functions
function greet(name)
    return "Hello, " + name
end
```

### ✅ Built-in Functions

```python
len(list)         # Length
str(x)            # Convert to string
int(x)            # Convert to integer
min(a, b, c)      # Minimum
max(a, b, c)      # Maximum
sum(list)         # Sum numbers
range(1, 10)      # Create list [1..9]
random()          # Random 0-1
randint(1, 100)   # Random integer
```

## Next Steps

### Learn the Language
1. ✅ Run `tutorial.quill` - Interactive lessons
2. ✅ Read `LANGUAGE_REFERENCE.md` - Complete documentation
3. ✅ Study the examples - Real working programs

### Write Your Own Programs
Start with something simple:
- A quiz program
- A choose-your-own-adventure
- A simple calculator
- A character creator for a game

### Extend the Language

Want to add features? The code is well-organized:

**lexer.py** - Add new keywords or operators
**parser.py** - Add new syntax rules
**interpreter.py** - Add new built-in functions

Ideas for new features:
- String methods (`.upper()`, `.lower()`, `.split()`)
- File I/O (read/write files)
- More list operations (`.append()`, `.remove()`)
- Dictionary/map data type
- Classes and objects
- Try/catch error handling
- Import system for modules

## Tips for Beginners

### 1. Start Small
```python
# Begin with simple programs
say "Hello!"
set x = 5
say x
```

### 2. Test Often
Run your program after every few lines to catch errors early.

### 3. Use Comments
```python
# This explains what the code does
set health = 100  # Player starts with full health
```

### 4. Copy and Modify
Look at the examples and change them to learn.

### 5. Read Error Messages
They tell you exactly what's wrong:
```
Syntax Error: Expected TokenType.END at line 10
Runtime Error: Variable 'x' is not defined
```

## Common Patterns

### Input Validation
```python
set valid = false
while not valid do
    ask "Enter 1-10:" into input
    set num = int(input)
    if num >= 1 and num <= 10 then
        valid = true
    else
        say "Invalid! Try again."
    end
end
```

### Menu System
```python
set running = true
while running do
    say "1. Play"
    say "2. Help"
    say "3. Exit"
    ask "Choose:" into choice
    
    if choice == "1" then
        say "Starting game..."
    end
    if choice == "3" then
        running = false
    end
end
```

### Score Tracking
```python
set score = 0

function add_points(points)
    score = score + points
    say "Score: " + str(score)
end

add_points(10)
add_points(25)
```

## Resources

- **README.md** - Quick overview and syntax
- **LANGUAGE_REFERENCE.md** - Complete language guide
- **tutorial.quill** - Interactive tutorial
- **example_*.quill** - Working example programs

## Get Help

### Syntax Errors
- Check for missing `end` statements
- Make sure strings use quotes: `"text"`
- Verify function calls have `()`

### Runtime Errors  
- Initialize variables before using them
- Check list indices are in range
- Ensure functions are defined before calling

### Logic Errors
- Add `say` statements to debug
- Check your conditions (`if`, `while`)
- Verify loop counters update correctly

## Share Your Creations!

Built something cool? The language is yours to use however you want!

Ideas for sharing:
- Create a GitHub repository
- Write tutorials for others
- Build a library of reusable functions
- Make game jam entries
- Teach friends to code

## Philosophy

Quill was designed with these principles:

1. **Readable** - Code should read like English
2. **Forgiving** - Clear error messages
3. **Practical** - Build real things immediately
4. **Educational** - Learn real programming concepts
5. **Fun** - Especially good for games!

---

## You're Ready! 🚀

You now have everything you need:
- ✅ A working programming language
- ✅ Complete documentation
- ✅ Example programs
- ✅ Tutorial to learn

**Now go build something amazing!**

Start with `tutorial.quill` and work your way up to creating your own programs.

Happy coding! 🎮✨

---

*Quill - Making programming accessible to everyone*
