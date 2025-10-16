# Quill Keywords Reference Guide

Complete reference for all Quill keywords, commands, and operators with examples and best practices.

---

## 📋 Table of Contents

1. [Output Commands](#output-commands)
2. [Input Commands](#input-commands)
3. [Variable Commands](#variable-commands)
4. [Control Flow Keywords](#control-flow-keywords)
5. [Logical Operators](#logical-operators)
6. [Comparison Operators](#comparison-operators)
7. [Arithmetic Operators](#arithmetic-operators)
8. [Built-in Functions](#built-in-functions)
9. [Loop Keywords](#loop-keywords)
10. [Special Commands](#special-commands)

---

## Output Commands

### `say`
**Purpose:** Display text or values to the screen  
**Color:** Pink (#ec4899)

**Syntax:**
```Quill
say "message"
say variable_name
say "text" + variable_name
```

**Examples:**
```Quill
say "Hello, World!"
say "Your score is: " + str(score)
say character_name
say "=============================="
```

**Notes:**
- Use for all text output to the player
- Can concatenate strings with `+`
- Variables must be converted to strings with `str()` when concatenating

---

### `print`
**Purpose:** Alternative to `say` for displaying output  
**Color:** Pink (#ec4899)

**Syntax:**
```Quill
print "message"
print variable_name
```

**Examples:**
```Quill
print "Debug: Player health = " + str(health)
print total_score
```

**Notes:**
- Works identically to `say`
- Use whichever feels more natural for your game

---

## Input Commands

### `ask`
**Purpose:** Get text input from the player and store it in a variable  
**Color:** Pink (#ec4899)

**Syntax:**
```Quill
ask "question prompt" into variable_name
```

**Examples:**
```Quill
ask "What is your name?" into player_name
ask "Enter your age:" into age
ask "Choose a weapon:" into weapon_choice
```

**Notes:**
- Always use with `into` to specify where to store the input
- Input is stored as a string by default
- Convert to number with `int()` or `float()` if needed:
  ```Quill
  ask "How old are you?" into age_text
  set age = int(age_text)
  ```

---

### `input`
**Purpose:** Alternative to `ask` for getting player input  
**Color:** Pink (#ec4899)

**Syntax:**
```Quill
input "prompt" into variable_name
```

**Examples:**
```Quill
input "Enter password:" into password
input "Type 'yes' or 'no':" into answer
```

**Notes:**
- Works identically to `ask`
- Some prefer `input` for technical prompts, `ask` for story questions

---

### `into`
**Purpose:** Specifies the variable to store input  
**Color:** Pink (#ec4899)

**Syntax:**
```Quill
ask "question" into variable_name
input "prompt" into variable_name
```

**Examples:**
```Quill
ask "What is your quest?" into quest_name
input "Enter command:" into command
```

**Notes:**
- Required after `ask` or `input`
- Creates the variable if it doesn't exist
- Always comes after the prompt string

---

### `choice`
**Purpose:** Present multiple choice options to the player  
**Color:** Pink (#ec4899)

**Syntax:**
```Quill
choice "option1" or "option2" or "option3"
```

**Examples:**
```Quill
choice "Attack" or "Defend" or "Run"
choice "Go left" or "Go right"
choice "Yes" or "No"
```

**Notes:**
- Player's choice is automatically stored in the `answer` variable
- Use `or` to separate options (colored amber)
- After choice, check `answer` with `if` statements:
  ```Quill
  choice "Red pill" or "Blue pill"
  if answer is "Red pill" then
      say "You chose the red pill"
  end
  ```

---

## Variable Commands

### `set`
**Purpose:** Create or update a variable  
**Color:** Pink (#ec4899)

**Syntax:**
```Quill
set variable_name = value
set variable_name to value
```

**Examples:**
```Quill
set health = 100
set player_name to "Hero"
set score = score + 10
set is_alive = true
```

**Notes:**
- Use `=` or `to` (both work the same)
- Creates variable if it doesn't exist
- Overwrites existing variable if it does
- Variables are dynamically typed (can store any type)

---

### `to`
**Purpose:** Alternative assignment operator  
**Color:** Pink (#ec4899)

**Syntax:**
```Quill
set variable_name to value
```

**Examples:**
```Quill
set character to "Warrior"
set level to 1
```

**Notes:**
- More readable than `=` for some people
- Works identically to `=`
- Colored pink like other commands

---

## Control Flow Keywords

### `if`
**Purpose:** Start a conditional block  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
if condition then
    # code to execute if true
end
```

**Examples:**
```Quill
if health is 0 then
    say "Game Over!"
end

if score > 100 then
    say "High score!"
end

if player_name is "Admin" then
    say "Welcome, administrator"
end
```

**Notes:**
- Always pair with `then` and `end`
- Condition can use: `is`, `==`, `>`, `<`, `>=`, `<=`, `!=`
- Can nest if statements inside each other

---

### `then`
**Purpose:** Marks the start of the conditional code block  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
if condition then
    # code here
end
```

**Examples:**
```Quill
if age > 18 then
    say "You are an adult"
end
```

**Notes:**
- Required after every `if` statement
- Must be on the same line as `if` or immediately after

---

### `else`
**Purpose:** Execute code when `if` condition is false  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
if condition then
    # code if true
else
    # code if false
end
```

**Examples:**
```Quill
if health > 0 then
    say "You are alive"
else
    say "You are dead"
end
```

**Notes:**
- Optional (can have `if`/`then`/`end` without `else`)
- Goes between the `if` block and `end`
- Only executes if the `if` condition is false

---

### `elif` / `elsif`
**Purpose:** Check additional conditions if previous conditions were false  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
if condition1 then
    # code
elif condition2 then
    # code
else
    # code
end
```

**Examples:**
```Quill
if score >= 90 then
    say "Grade: A"
elif score >= 80 then
    say "Grade: B"
elif score >= 70 then
    say "Grade: C"
else
    say "Grade: F"
end
```

**Notes:**
- `elif` and `elsif` are identical
- Can have multiple `elif` statements
- Checked in order from top to bottom
- First true condition executes, then skips to `end`

---

### `end`
**Purpose:** Close a code block (`if`, `while`, `for`, `function`)  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
if condition then
    # code
end

while condition do
    # code
end
```

**Examples:**
```Quill
if health > 0 then
    say "Still alive"
end

while playing is true do
    say "Game continues"
end
```

**Notes:**
- Required to close all control flow blocks
- Must match the opening keyword (`if`, `while`, etc.)
- Indentation helps readability but isn't required

---

### `while`
**Purpose:** Repeat code while a condition is true  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
while condition do
    # code to repeat
end
```

**Examples:**
```Quill
set count = 0
while count < 10 do
    say "Count: " + str(count)
    set count = count + 1
end

while playing is true do
    say "Game is running..."
    # game logic here
end
```

**Notes:**
- Always use with `do` and `end`
- Condition checked before each loop iteration
- Be careful to avoid infinite loops
- Use `break` to exit early (if supported)

---

### `do`
**Purpose:** Marks the start of a loop body  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
while condition do
    # code
end

for variable in range(10) do
    # code
end
```

**Examples:**
```Quill
while health > 0 do
    say "Still fighting"
end
```

**Notes:**
- Required after `while` and `for`
- Similar to `then` for `if` statements

---

### `for`
**Purpose:** Loop over a range or collection  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
for variable in range(count) do
    # code
end
```

**Examples:**
```Quill
for i in range(5) do
    say "Loop number: " + str(i)
end

for player in players do
    say player
end
```

**Notes:**
- Iterates over numbers or collections
- Use `range(n)` to loop n times (0 to n-1)
- Loop variable is automatically created

---

### `in`
**Purpose:** Specifies the collection or range to loop over  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
for variable in collection do
    # code
end
```

**Examples:**
```Quill
for i in range(10) do
    say str(i)
end
```

**Notes:**
- Only used with `for` loops
- Collection can be a range, list, or other iterable

---

## Logical Operators

### `and`
**Purpose:** Combine conditions - both must be true  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
if condition1 and condition2 then
    # code
end
```

**Examples:**
```Quill
if health > 0 and mana > 0 then
    say "You can cast spells"
end

if age >= 18 and has_license is true then
    say "You can drive"
end
```

**Notes:**
- Both conditions must be true for the whole expression to be true
- Short-circuits: if first is false, second isn't checked
- Can chain multiple: `a and b and c`

---

### `or`
**Purpose:** Combine conditions - at least one must be true  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
if condition1 or condition2 then
    # code
end
```

**Examples:**
```Quill
if is_admin or is_moderator then
    say "You have permissions"
end

if key_found or door_unlocked then
    say "You can proceed"
end
```

**Notes:**
- Only one condition needs to be true
- Short-circuits: if first is true, second isn't checked
- Also used in `choice` to separate options
- Can chain multiple: `a or b or c`

---

### `not`
**Purpose:** Negate a condition (invert true/false)  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
if not condition then
    # code
end
```

**Examples:**
```Quill
if not game_over then
    say "Keep playing"
end

if not has_key then
    say "The door is locked"
end
```

**Notes:**
- Inverts the boolean value
- `not true` becomes `false`
- `not false` becomes `true`
- Can combine: `not (a and b)` or `not a or not b`

---

### `is`
**Purpose:** Check if two values are equal  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
if value1 is value2 then
    # code
end
```

**Examples:**
```Quill
if answer is "yes" then
    say "Confirmed!"
end

if character is "Warrior" then
    set strength = 100
end

if health is 0 then
    say "Game Over"
end
```

**Notes:**
- More readable than `==`
- Works with strings, numbers, and booleans
- Case-sensitive for strings
- Preferred over `==` in Quill

---

## Comparison Operators

### `==`
**Purpose:** Check if two values are equal  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
if value1 == value2 then
    # code
end
```

**Examples:**
```Quill
if score == 100 then
    say "Perfect score!"
end
```

**Notes:**
- Alternative to `is`
- Use `is` for better readability
- Works with all data types

---

### `!=`
**Purpose:** Check if two values are NOT equal  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
if value1 != value2 then
    # code
end
```

**Examples:**
```Quill
if health != 0 then
    say "Still alive"
end

if choice != "quit" then
    say "Continuing game"
end
```

**Notes:**
- Opposite of `==` and `is`
- Returns true when values are different
- Can also use `not (a is b)` for readability

---

### `>`
**Purpose:** Check if left value is greater than right  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
if value1 > value2 then
    # code
end
```

**Examples:**
```Quill
if score > 1000 then
    say "High score achieved!"
end

if age > 18 then
    say "Adult"
end
```

**Notes:**
- Works with numbers only
- Strings may be compared alphabetically
- Use `>=` to include equal values

---

### `<`
**Purpose:** Check if left value is less than right  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
if value1 < value2 then
    # code
end
```

**Examples:**
```Quill
if health < 20 then
    say "Warning: Low health!"
end

if lives < 1 then
    say "Game Over"
end
```

**Notes:**
- Works with numbers only
- Opposite of `>`
- Use `<=` to include equal values

---

### `>=`
**Purpose:** Check if left is greater than or equal to right  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
if value1 >= value2 then
    # code
end
```

**Examples:**
```Quill
if level >= 10 then
    say "Unlock special ability"
end

if score >= 500 then
    say "Achievement unlocked!"
end
```

**Notes:**
- True if left is greater OR equal
- Includes the boundary value
- Common for level/score thresholds

---

### `<=`
**Purpose:** Check if left is less than or equal to right  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
if value1 <= value2 then
    # code
end
```

**Examples:**
```Quill
if health <= 0 then
    say "You died"
end

if attempts <= 3 then
    say "You have " + str(3 - attempts) + " tries left"
end
```

**Notes:**
- True if left is less OR equal
- Includes the boundary value
- Useful for checking limits

---

## Arithmetic Operators

### `+`
**Purpose:** Add numbers or concatenate strings  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
result = value1 + value2
set var = var + increment
```

**Examples:**
```Quill
set total = 10 + 5          # total = 15
set score = score + 100      # increment score
say "Hello " + "World"       # string concatenation
say "Score: " + str(score)   # combine text and number
```

**Notes:**
- For numbers: performs addition
- For strings: concatenates (joins)
- Must use `str()` to convert numbers when concatenating
- Can't mix strings and numbers without conversion

---

### `-`
**Purpose:** Subtract numbers  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
result = value1 - value2
set var = var - decrement
```

**Examples:**
```Quill
set difference = 10 - 3      # difference = 7
set health = health - 20     # decrease health
set lives = lives - 1        # lose a life
```

**Notes:**
- Works with numbers only
- Can result in negative numbers
- Use for decreasing values

---

### `*`
**Purpose:** Multiply numbers  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
result = value1 * value2
```

**Examples:**
```Quill
set total = 5 * 3            # total = 15
set damage = base_damage * 2  # double damage
set area = width * height     # calculate area
```

**Notes:**
- Works with numbers only
- Can multiply integers or floats
- Result type depends on operands

---

### `/`
**Purpose:** Divide numbers  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
result = value1 / value2
```

**Examples:**
```Quill
set half = 10 / 2            # half = 5
set average = total / count   # calculate average
set percent = score / max_score  # get percentage
```

**Notes:**
- Works with numbers only
- Returns float result
- Dividing by zero may cause error
- Use `int()` to convert result to integer

---

### `%`
**Purpose:** Get remainder after division (modulo)  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
result = value1 % value2
```

**Examples:**
```Quill
set remainder = 10 % 3       # remainder = 1
set is_even = number % 2     # 0 if even, 1 if odd

# Check every 10 points
if score % 10 is 0 then
    say "Multiple of 10!"
end
```

**Notes:**
- Returns remainder of division
- Useful for checking divisibility
- Common for even/odd checks
- Pattern detection (every Nth item)

---

### `**`
**Purpose:** Raise number to a power (exponentiation)  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
result = base ** exponent
```

**Examples:**
```Quill
set squared = 5 ** 2         # squared = 25
set cubed = 2 ** 3           # cubed = 8
set damage = base_damage ** level  # exponential scaling
```

**Notes:**
- base ** exponent = base × base × ... (exponent times)
- Works with integers and floats
- Can use fractional exponents for roots: `9 ** 0.5` = 3

---

### `=`
**Purpose:** Assign a value to a variable  
**Color:** Amber (#f59e0b)

**Syntax:**
```Quill
variable = value
set variable = value
```

**Examples:**
```Quill
health = 100
score = score + 10
set name = "Player"
```

**Notes:**
- Used with `set` keyword
- Overwrites previous value
- Can use in compound operations: `x = x + 1`
- Alternative to `to` keyword

---

## Built-in Functions

### `str()`
**Purpose:** Convert value to string  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
str(value)
```

**Examples:**
```Quill
say "Your score is: " + str(score)
set age_text = str(age)
say "Health: " + str(health) + "/100"
```

**Notes:**
- Required when concatenating numbers with strings
- Works with numbers, booleans, and other types
- Returns string representation

---

### `int()`
**Purpose:** Convert value to integer  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
int(value)
```

**Examples:**
```Quill
ask "Enter your age:" into age_input
set age = int(age_input)

set rounded = int(45.7)  # rounded = 45
```

**Notes:**
- Converts strings to numbers
- Truncates decimal places (doesn't round)
- Returns error if string isn't a valid number
- `int("45")` = 45, `int(45.9)` = 45

---

### `float()`
**Purpose:** Convert value to floating-point number  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
float(value)
```

**Examples:**
```Quill
ask "Enter price:" into price_input
set price = float(price_input)

set precise = float(10)  # precise = 10.0
```

**Notes:**
- Preserves decimal places
- Converts strings and integers to float
- Use for precise calculations
- `float("3.14")` = 3.14

---

### `len()`
**Purpose:** Get length of string or collection  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
len(value)
```

**Examples:**
```Quill
set name_length = len(player_name)
say "Your name has " + str(len(name)) + " letters"

if len(password) < 8 then
    say "Password too short"
end
```

**Notes:**
- Returns number of characters in string
- Returns number of items in list/array
- Returns integer

---

### `type()`
**Purpose:** Get the type of a value  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
type(value)
```

**Examples:**
```Quill
say type(42)          # "int"
say type("hello")     # "str"
say type(3.14)        # "float"
say type(true)        # "bool"
```

**Notes:**
- Returns string describing type
- Useful for debugging
- Common types: "int", "str", "float", "bool"

---

### `range()`
**Purpose:** Generate sequence of numbers  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
range(stop)
range(start, stop)
range(start, stop, step)
```

**Examples:**
```Quill
for i in range(5) do
    say str(i)  # prints 0, 1, 2, 3, 4
end

for i in range(1, 10) do
    say str(i)  # prints 1 through 9
end

for i in range(0, 10, 2) do
    say str(i)  # prints 0, 2, 4, 6, 8
end
```

**Notes:**
- `range(n)`: 0 to n-1
- `range(start, stop)`: start to stop-1
- `range(start, stop, step)`: start to stop-1 by step
- Used primarily with `for` loops

---

### `abs()`
**Purpose:** Get absolute value (remove negative sign)  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
abs(number)
```

**Examples:**
```Quill
set distance = abs(-5)       # distance = 5
set diff = abs(score1 - score2)  # always positive
```

**Notes:**
- Returns positive version of number
- `abs(-10)` = 10, `abs(10)` = 10
- Useful for calculating distances/differences

---

### `min()`
**Purpose:** Get smallest value from arguments  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
min(value1, value2, ...)
```

**Examples:**
```Quill
set lowest = min(5, 2, 8, 1)  # lowest = 1
set health = min(health, max_health)  # cap at max
```

**Notes:**
- Returns smallest value
- Can take 2 or more arguments
- Works with numbers

---

### `max()`
**Purpose:** Get largest value from arguments  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
max(value1, value2, ...)
```

**Examples:**
```Quill
set highest = max(5, 2, 8, 1)  # highest = 8
set damage = max(0, base_damage - armor)  # at least 0
```

**Notes:**
- Returns largest value
- Can take 2 or more arguments
- Useful for ensuring minimums

---

### `sum()`
**Purpose:** Add all numbers in a collection  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
sum(collection)
```

**Examples:**
```Quill
set total = sum(scores)
set avg = sum(values) / len(values)
```

**Notes:**
- Takes list/array of numbers
- Returns single sum value
- Useful for totals and averages

---

### `round()`
**Purpose:** Round number to nearest integer or decimal places  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
round(number)
round(number, decimals)
```

**Examples:**
```Quill
set rounded = round(3.7)      # rounded = 4
set price = round(19.99, 1)   # price = 20.0
set precise = round(3.14159, 2)  # precise = 3.14
```

**Notes:**
- Default rounds to nearest integer
- Optional second argument for decimal places
- Uses standard rounding rules (0.5 rounds up)

---

### `random()`
**Purpose:** Generate random floating-point number  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
random()
```

**Examples:**
```Quill
set chance = random()  # 0.0 to 1.0

if random() < 0.5 then
    say "Heads"
else
    say "Tails"
end
```

**Notes:**
- Returns random float between 0.0 and 1.0
- Use for probability checks
- Multiply for different ranges: `random() * 100`

---

### `randint()`
**Purpose:** Generate random integer in range  
**Color:** Cyan (#06b6d4)

**Syntax:**
```Quill
randint(min, max)
```

**Examples:**
```Quill
set dice = randint(1, 6)      # roll a die
set damage = randint(10, 20)  # random damage
set choice = randint(0, 2)    # random choice (0, 1, or 2)
```

**Notes:**
- Returns random integer between min and max (inclusive)
- Both min and max are included in range
- `randint(1, 6)` can return 1, 2, 3, 4, 5, or 6

---

## Special Commands

### `function` / `func` / `def`
**Purpose:** Define a reusable function  
**Color:** Pink (#ec4899)

**Syntax:**
```Quill
function name() do
    # code
end

func name(param1, param2) do
    # code
end
```

**Examples:**
```Quill
function greet() do
    say "Hello, player!"
end

func calculate_damage(base, multiplier) do
    set result = base * multiplier
    return result
end
```

**Notes:**
- `function`, `func`, and `def` are identical
- Can take parameters
- Use `return` to send value back
- Call with function name: `greet()` or `calculate_damage(10, 2)`

---

### `return`
**Purpose:** Exit function and optionally return a value  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
return
return value
```

**Examples:**
```Quill
function get_max_health() do
    return 100
end

func check_victory() do
    if enemies is 0 then
        return true
    else
        return false
    end
end
```

**Notes:**
- Exits function immediately
- Can return a value to caller
- Without value, returns nothing/null

---

### `import`
**Purpose:** Load another Quill file  
**Color:** Pink (#ec4899)

**Syntax:**
```Quill
import "filename"
```

**Examples:**
```Quill
import "utilities"
import "game_config"
```

**Notes:**
- Loads and executes another .quill file
- Useful for organizing large projects
- Imported file's variables/functions become available

---

### `break`
**Purpose:** Exit a loop early  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
break
```

**Examples:**
```Quill
while true do
    ask "Enter 'quit' to exit:" into command
    if command is "quit" then
        break
    end
    say "You entered: " + command
end
```

**Notes:**
- Immediately exits innermost loop
- Useful for early exit conditions
- Only works inside loops (`while`, `for`)

---

### `continue`
**Purpose:** Skip rest of current loop iteration  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
continue
```

**Examples:**
```Quill
for i in range(10) do
    if i % 2 is 0 then
        continue  # skip even numbers
    end
    say str(i)  # only prints odd numbers
end
```

**Notes:**
- Skips to next iteration of loop
- Doesn't exit loop completely (use `break` for that)
- Useful for filtering

---

### `goto`
**Purpose:** Jump to a labeled section  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
goto label_name

label label_name
```

**Examples:**
```Quill
say "Start"
goto end_section

say "This is skipped"

label end_section
say "End"
```

**Notes:**
- Use sparingly (can make code hard to follow)
- Must define label with `label` keyword
- Useful for game states/scenes

---

### `label`
**Purpose:** Define a jump destination for `goto`  
**Color:** Purple (#9333ea)

**Syntax:**
```Quill
label label_name
```

**Examples:**
```Quill
label game_start
say "Welcome to the game!"

# game code here

if game_over then
    goto game_start
end
```

**Notes:**
- Marks a position in code
- Used with `goto` to jump to sections
- Good for scene transitions in games

---

## Quick Reference Color Guide

| Color | Keywords |
|-------|----------|
| **Pink (#ec4899)** | `say`, `print`, `ask`, `input`, `into`, `choice`, `set`, `to`, `function`, `func`, `def`, `import` |
| **Purple (#9333ea)** | `if`, `then`, `else`, `elif`, `elsif`, `end`, `while`, `do`, `for`, `in`, `return`, `break`, `continue`, `goto`, `label` |
| **Amber (#f59e0b)** | `and`, `or`, `not`, `is`, `==`, `!=`, `>`, `<`, `>=`, `<=`, `+`, `-`, `*`, `/`, `%`, `**`, `=` |
| **Golden Yellow (#fbbf24)** | Variables (e.g., `character`, `age`, `health`) |
| **Green (#10b981)** | Strings (e.g., `"Hello World"`) |
| **Blue (#3b82f6)** | Numbers (e.g., `42`, `3.14`) |
| **Cyan (#06b6d4)** | Functions (e.g., `str()`, `int()`, `len()`) |

---

## Common Patterns & Examples

### Input and Validation
```Quill
ask "Enter a number between 1 and 10:" into input
set number = int(input)

if number < 1 or number > 10 then
    say "Invalid input!"
else
    say "You entered: " + str(number)
end
```

### Multiple Choice with Branching
```Quill
say "You approach a fork in the road."
choice "Go left" or "Go right" or "Go back"

if answer is "Go left" then
    say "You encounter a dragon!"
elif answer is "Go right" then
    say "You find treasure!"
else
    say "You return to town."
end
```

### Loop with Counter
```Quill
set count = 0
while count < 5 do
    say "Count: " + str(count)
    set count = count + 1
end
say "Done!"
```

### Health System
```Quill
set health = 100
set max_health = 100

# Take damage
set health = health - 25
set health = max(0, health)  # don't go below 0

# Heal
set health = health + 20
set health = min(health, max_health)  # don't exceed max

# Check status
if health <= 0 then
    say "Game Over!"
elif health < 30 then
    say "Warning: Low health!"
else
    say "Health: " + str(health) + "/" + str(max_health)
end
```

### Random Events
```Quill
set chance = random()

if chance < 0.1 then
    say "Rare event! (10% chance)"
elif chance < 0.4 then
    say "Uncommon event (30% chance)"
else
    say "Common event (60% chance)"
end
```

---

## Best Practices

1. **Use meaningful variable names**
   - ✅ `player_health`, `enemy_damage`
   - ❌ `x`, `temp`, `var1`

2. **Comment your code**
   ```Quill
   # Check if player has won
   if score >= 1000 then
       say "Victory!"
   end
   ```

3. **Indent for readability**
   ```Quill
   if condition then
       if nested_condition then
           say "Indented code is easier to read"
       end
   end
   ```

4. **Use `is` instead of `==` for equality**
   - ✅ `if name is "Player" then`
   - ⚠️ `if name == "Player" then` (works but less readable)

5. **Convert types when needed**
   ```Quill
   ask "Enter age:" into input
   set age = int(input)  # Convert to number
   say "Age: " + str(age)  # Convert back to string
   ```

6. **Keep functions small and focused**
   ```Quill
   function calculate_damage() do
       # Do one thing well
       return base_damage * multiplier
   end
   ```

---

## Debugging Tips

1. **Use `say` to print variable values**
   ```Quill
   say "Debug: health = " + str(health)
   say "Debug: score = " + str(score)
   ```

2. **Check types when things go wrong**
   ```Quill
   say "Type of input: " + type(input)
   ```

3. **Test conditions one at a time**
   ```Quill
   if health > 0 then
       say "Health check passed"
       if mana > 0 then
           say "Mana check passed"
       end
   end
   ```

---

## Conclusion

This reference covers all Quill keywords and their usage. For more examples, see the `/examples` directory or check out the sample games in `/games`.

Happy coding! 🎮✨
