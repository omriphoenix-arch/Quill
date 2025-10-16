# Your First Quill Program
## A Complete Beginner's Tutorial

Welcome to Quill! This tutorial will teach you programming from scratch. No experience needed!

---

## What You'll Learn

By the end of this tutorial, you'll know how to:
1. Display messages
2. Store information in variables
3. Get input from users
4. Make decisions with if/else
5. Create interactive programs
6. Build a simple game!

**Time:** 15-20 minutes  
**Difficulty:** Beginner (no experience required)

---

## Step 1: Your First Program - "Hello, World!"

Let's start with the simplest program in Quill.

### Create a new file: `hello.quill`

```Quill
say "Hello, World!"
```

### Run it:
```bash
python core/Quill.py hello.quill
```

### What you should see:
```
Hello, World!
```

**🎉 Congratulations!** You just wrote your first program!

### What's happening?
- `say` is a command that displays text
- `"Hello, World!"` is a string (text in quotes)
- The program shows the message and stops

---

## Step 2: Variables - Storing Information

Variables let you store and remember information.

### Create: `variables.quill`

```Quill
# Store your name
set name = "Alice"

# Store your age
set age = 25

# Store a yes/no value
set is_happy = true

# Display everything
say "My name is " + name
say "I am " + str(age) + " years old"
```

### What you should see:
```
My name is Alice
I am 25 years old
```

### Key Concepts:
- `set` creates a variable
- `=` assigns a value
- `+` joins strings together
- `str()` converts numbers to text (needed for joining)
- `#` starts a comment (ignored by computer)

### 🎯 Try This:
Change "Alice" to your name and 25 to your age!

---

## Step 3: Getting User Input

Let's make programs interactive!

### Create: `greeting.quill`

```Quill
# Ask for the user's name
ask "What is your name?" into name

# Ask for their age
ask "How old are you?" into age

# Greet them personally
say ""
say "Nice to meet you, " + name + "!"
say "You are " + age + " years old."
say "Welcome to Quill!"
```

### What you should see:
```
What is your name? Alice
How old are you? 25

Nice to meet you, Alice!
You are 25 years old.
Welcome to Quill!
```

### Key Concepts:
- `ask` displays a question and waits for input
- `into` stores the answer in a variable
- You can use that variable later
- `""` creates a blank line

### 🎯 Try This:
Add more questions! Ask about favorite color, hobby, etc.

---

## Step 4: Making Decisions with If/Else

Programs can make choices based on conditions.

### Create: `age_checker.quill`

```Quill
# Get age
ask "How old are you?" into age_text
set age = int(age_text)

# Check if adult
if age >= 18 then
    say "You are an adult!"
else
    say "You are a minor."
end

# Check age range
if age < 13 then
    say "You're a kid!"
elif age < 20 then
    say "You're a teenager!"
elif age < 65 then
    say "You're an adult!"
else
    say "You're a senior!"
end
```

### What you should see (example with age 25):
```
How old are you? 25
You are an adult!
You're an adult!
```

### Key Concepts:
- `int()` converts text to a number
- `if` checks a condition
- `then` starts the if-block
- `else` runs if condition is false
- `elif` checks another condition
- `end` closes the if-block
- `>=` means "greater than or equal"
- `<` means "less than"

### 🎯 Try This:
Add more age ranges or different conditions!

---

## Step 5: Multiple Choice

Let users choose from options.

### Create: `adventure.quill`

```Quill
say "You wake up in a mysterious forest."
say "There are three paths ahead."
say ""

# Present choices
choice "Take the left path" or "Take the right path" or "Go back to sleep"

# React to choice
if answer is "Take the left path" then
    say "You find a treasure chest!"
    say "You win 100 gold!"
elif answer is "Take the right path" then
    say "You encounter a friendly dragon."
    say "The dragon gives you a ride home!"
else
    say "You sleep peacefully."
    say "When you wake up, everything was a dream."
end
```

### What you should see:
```
You wake up in a mysterious forest.
There are three paths ahead.

1. Take the left path
2. Take the right path
3. Go back to sleep

Choose an option (1-3): 1

You find a treasure chest!
You win 100 gold!
```

### Key Concepts:
- `choice` presents numbered options
- `or` separates each option
- `answer` automatically stores the chosen option
- `is` checks if two values are equal

### 🎯 Try This:
Add more choices and outcomes!

---

## Step 6: Math and Calculations

Quill can do math!

### Create: `calculator.quill`

```Quill
say "=== Simple Calculator ==="
say ""

# Get two numbers
ask "Enter first number:" into num1_text
ask "Enter second number:" into num2_text

# Convert to numbers
set num1 = int(num1_text)
set num2 = int(num2_text)

# Perform calculations
set sum = num1 + num2
set difference = num1 - num2
set product = num1 * num2
set quotient = num1 / num2

# Display results
say ""
say "Results:"
say num1_text + " + " + num2_text + " = " + str(sum)
say num1_text + " - " + num2_text + " = " + str(difference)
say num1_text + " × " + num2_text + " = " + str(product)
say num1_text + " ÷ " + num2_text + " = " + str(quotient)
```

### Math Operators:
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Remainder (modulo)
- `**` Power (e.g., 2 ** 3 = 8)

### 🎯 Try This:
Add more operations like square root or percentage!

---

## Step 7: Loops - Repeating Code

Make code repeat multiple times.

### Create: `countdown.quill`

```Quill
say "Countdown starting!"
say ""

set count = 5
while count > 0 do
    say str(count) + "..."
    set count = count - 1
end

say "Blast off! 🚀"
```

### What you should see:
```
Countdown starting!

5...
4...
3...
2...
1...
Blast off! 🚀
```

### Key Concepts:
- `while` repeats code while condition is true
- `do` starts the loop body
- `end` closes the loop
- Loop runs until condition becomes false
- Must change variable inside loop (or it never stops!)

### 🎯 Try This:
Make it count from 10, or count up instead of down!

---

## Step 8: Your First Game - Number Guessing

Let's combine everything into a fun game!

### Create: `guessing_game.quill`

```Quill
say "=== Number Guessing Game ==="
say "I'm thinking of a number between 1 and 10."
say ""

# Computer picks random number
set secret_number = randint(1, 10)
set attempts = 0
set max_attempts = 3

# Game loop
while attempts < max_attempts do
    # Get player's guess
    ask "Guess the number:" into guess_text
    set guess = int(guess_text)
    set attempts = attempts + 1
    
    # Check if correct
    if guess is secret_number then
        say "🎉 Correct! You won in " + str(attempts) + " attempts!"
        break
    elif guess < secret_number then
        say "Too low! Try again."
    else
        say "Too high! Try again."
    end
    
    say ""
end

# If they ran out of attempts
if attempts >= max_attempts and guess != secret_number then
    say "💔 Game Over! The number was " + str(secret_number)
end
```

### New Concepts:
- `randint(1, 10)` picks random number from 1 to 10
- `break` exits the loop early
- `and` combines two conditions
- `!=` means "not equal"

### 🎯 Try This:
- Make the range bigger (1 to 100)
- Give unlimited attempts
- Add difficulty levels

---

## Step 9: Functions - Reusable Code

Functions let you reuse code.

### Create: `functions.quill`

```Quill
# Define a greeting function
function greet(name) do
    say "Hello, " + name + "!"
    say "Welcome to Quill!"
end

# Define a calculation function
function calculate_area(width, height) do
    set area = width * height
    return area
end

# Use the functions
greet("Alice")
say ""

set room_area = calculate_area(10, 15)
say "Room area: " + str(room_area) + " square feet"
```

### Key Concepts:
- `function` creates reusable code
- Parameters go in parentheses: `(name)`
- `return` sends a value back
- Call function with its name: `greet("Alice")`

### 🎯 Try This:
Create a function that calculates square, cube, or percentage!

---

## Step 10: Complete Example - Interactive Story

Putting it all together!

### Create: `mystery.quill`

```Quill
say "=== The Mysterious Library ==="
say ""

# Introduction
ask "What is your name, detective?" into name
say ""
say "Welcome, Detective " + name + "!"
say "A valuable book has been stolen from the library."
say "There are three suspects..."
say ""

# Clue gathering
set clues_found = 0

say "Let's investigate!"
say ""

# First clue
choice "Question the librarian" or "Search the reading room" or "Check security footage"

if answer is "Question the librarian" then
    say "The librarian says they saw someone in a red coat."
    set clues_found = clues_found + 1
elif answer is "Search the reading room" then
    say "You find a torn page from the book!"
    set clues_found = clues_found + 1
else
    say "The footage shows someone entering at midnight."
    set clues_found = clues_found + 1
end

say ""

# Second clue
choice "Interview witnesses" or "Examine the crime scene" or "Review suspect alibis"

if answer is "Interview witnesses" then
    say "A witness saw someone running away with a bag."
    set clues_found = clues_found + 1
elif answer is "Examine the crime scene" then
    say "You find muddy footprints leading outside."
    set clues_found = clues_found + 1
else
    say "One suspect has no alibi for last night!"
    set clues_found = clues_found + 1
end

say ""

# Solve the case
say "You've gathered " + str(clues_found) + " clues."
say "Time to make an accusation!"
say ""

choice "It was the janitor" or "It was the student" or "It was the professor"

say ""
set correct_answer = "It was the professor"

if answer is correct_answer then
    say "🎉 Correct! The professor confesses!"
    say "They needed the rare book for their research."
    say "Case solved, Detective " + name + "!"
else
    say "❌ Wrong! The real thief escapes!"
    say "Better luck next time, Detective " + name + "."
end
```

---

## 🎓 Congratulations!

You've learned the fundamentals of programming with Quill!

### What You've Learned:
✅ Displaying output with `say`  
✅ Storing data in variables with `set`  
✅ Getting user input with `ask`  
✅ Making decisions with `if`/`else`  
✅ Presenting choices with `choice`  
✅ Performing calculations  
✅ Repeating code with `while`  
✅ Creating functions  
✅ Building interactive programs  

### Next Steps:

1. **Read More Documentation:**
   - [Keywords Reference](Quill_KEYWORDS_REFERENCE.md) - Every keyword explained
   - [Language Reference](LANGUAGE_REFERENCE.md) - Complete language guide
   - [Getting Started](GETTING_STARTED.md) - Installation and setup

2. **Try Example Programs:**
   - Check the `examples/` folder for more programs
   - Study how they work
   - Modify them to learn

3. **Build Your Own Projects:**
   - Text adventure games
   - Quiz programs
   - Simple calculators
   - Todo list managers
   - Interactive stories

4. **Join the Community:**
   - Share your programs
   - Ask questions
   - Help other beginners

---

## Common Mistakes and Solutions

### Mistake 1: Forgetting `str()` when joining
```Quill
# ❌ Wrong
say "Age: " + age

# ✅ Correct
say "Age: " + str(age)
```

### Mistake 2: Forgetting `int()` for math
```Quill
# ❌ Wrong (age is text)
ask "Age?" into age
if age > 18 then
    # This won't work!
end

# ✅ Correct
ask "Age?" into age_text
set age = int(age_text)
if age > 18 then
    # This works!
end
```

### Mistake 3: Forgetting `end`
```Quill
# ❌ Wrong
if score > 100 then
    say "High score!"
# Missing end!

# ✅ Correct
if score > 100 then
    say "High score!"
end
```

### Mistake 4: Using `=` instead of `is`
```Quill
# ❌ Confusing (sets variable)
if name = "Alice" then

# ✅ Clear (checks equality)
if name is "Alice" then
```

---

## Quick Reference Card

### Output
```Quill
say "message"
```

### Input
```Quill
ask "question?" into variable
```

### Variables
```Quill
set name = "Alice"
set age = 25
```

### If Statement
```Quill
if condition then
    # code
else
    # code
end
```

### Choice
```Quill
choice "A" or "B" or "C"
# answer now has the choice
```

### While Loop
```Quill
while condition do
    # code
end
```

### Functions
```Quill
function name(param) do
    # code
    return value
end
```

---

## Need Help?

- 📖 Read the [full documentation](../docs/)
- 💡 Check [example programs](../examples/)
- 🐛 [Report bugs](https://github.com/yourusername/Quill/issues)
- 💬 [Ask questions](https://github.com/yourusername/Quill/discussions)

---

**Happy coding!** 🎉✨

You're now ready to create amazing programs with Quill!
