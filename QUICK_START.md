# Quill Quick Start Guide

Get up and running with Quill in **5 minutes**! ⚡

## What is Quill?

Quill is a modern, beginner-friendly scripting language with:
- 🎯 Simple, readable syntax (like Python)
- 💡 Rich error messages with helpful hints
- 📚 40+ built-in functions for common tasks
- 🎮 Optional game development utilities

Perfect for learning programming, automation, data processing, and interactive applications!

## Step 1: Requirements

- **Python 3.7+** (that's it!)
- No external dependencies required for core language
- Optional: Pillow for GUI/image support

## Step 2: Install (1 minute)

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
```

**macOS/Linux:**
```bash
chmod +x install.sh
./install.sh
```

The installer does everything: checks Python, adds to PATH, and tests your setup.

## Step 3: Your First Program (2 minutes)

Create a file called `hello.quill`:

```python
# Use say or print (they're the same!)
print "Hello! What's your name?"
ask "Name:" into name

print "Nice to meet you, " + name + "!"
print "Let me guess your age..."

ask "Enter your age:" into age
set years_to_100 = 100 - int(age)

say "You'll be 100 in " + str(years_to_100) + " years!"
```

## Step 3: Run It! (30 seconds)

```bash
Quill hello.quill
```

That's it! You just wrote and ran your first Quill program! 🎉

## Step 4: Try a Game (1 minute)

Create `guess.quill`:

```python
set secret = randint(1, 10)
set guesses = 0
set won = false

say "I'm thinking of a number between 1 and 10..."

while not won do
    ask "Your guess:" into guess
    guesses = guesses + 1
    
    if int(guess) == secret then
        say "You got it in " + str(guesses) + " guesses!"
        won = true
    else
        if int(guess) < secret then
            say "Higher!"
        else
            say "Lower!"
        end
    end
end
```

Run it:
```bash
Quill guess.quill
```

## Step 5: Learn More (whenever you want)

Ready to learn everything? Check out:

- **[docs/TUTORIAL.md](docs/TUTORIAL.md)** - Complete 10-step tutorial (15-20 minutes)
- **[example_simple.quill](example_simple.quill)** - More examples
- **[docs/Quill_KEYWORDS_REFERENCE.md](docs/Quill_KEYWORDS_REFERENCE.md)** - Every command explained

## Common Commands Cheat Sheet

```python
# Display text
say "Hello!"

# Get input
ask "What's your name?" into name

# Variables
set x = 10
set name = "Alice"

# Math
set sum = 5 + 3
set power = 2 ** 8

# If/else
if score > 90 then
    say "A grade!"
else
    say "Keep trying!"
end

# While loop
set count = 5
while count > 0 do
    say count
    count = count - 1
end

# For loop
for i in range(1, 6) do
    say i
end

# Functions
function greet(name)
    say "Hello, " + name
end

greet("Bob")

# Lists
set items = ["sword", "shield", "potion"]
say items[0]  # First item

# Random numbers
set dice = randint(1, 6)

# Inventory (for games)
add_item("key")
if has_item("key") then
    say "You have the key!"
end

# Save/Load (for games)
save_game("slot1")
load_game("slot1")
```

## VS Code Setup (Optional but Recommended)

1. Open VS Code
2. Run:
   ```powershell
   cd .vscode-extension
   powershell -ExecutionPolicy Bypass -File install_extension.ps1
   ```
3. Restart VS Code
4. Open any `.quill` file - enjoy syntax highlighting and custom icons!

Choose your theme: **Quill Dark**, **Quill Neon**, or **Quill Light**

## Need Help?

- **[docs/ERROR_MESSAGES.md](docs/ERROR_MESSAGES.md)** - Understand error messages
- **[docs/TUTORIAL.md](docs/TUTORIAL.md)** - Step-by-step guide
- **GitHub Issues** - Report bugs or ask questions

## What Can You Build?

- 🎮 Text adventure games
- 🕹️ Interactive fiction
- 🧮 Calculators and tools
- 📝 Todo lists and organizers
- 🎲 Random generators
- 🧩 Puzzle games
- 📚 Learning exercises
- ✨ Anything you can imagine!

---

**You're ready to code!** Start with simple programs and work your way up. Check out the `example_*.quill` files for inspiration.

Happy coding! 🚀
