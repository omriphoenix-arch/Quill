# Quill Language Reference

## Complete Language Guide

### Comments
```python
# This is a comment
say "Hello"  # Comments can go after code too
```

### Data Types

#### Numbers
```python
set integer = 42
set decimal = 3.14
set negative = -10
```

#### Strings
```python
set name = "Alice"
set message = 'Hello, World!'
set multiline = "Line 1\nLine 2"  # \n for newline
```

#### Booleans
```python
set is_valid = true
set is_complete = false
```

#### Lists
```python
set numbers = [1, 2, 3, 4, 5]
set mixed = [1, "hello", true, [1, 2]]
set empty = []
```

#### Null/None
```python
set nothing = null
```

### Variables

#### Declaration
```python
set x = 10              # Using 'set' keyword
x = 10                  # Direct assignment
```

#### Multiple Assignment
```python
set a = 1
set b = 2
set c = a + b
```

### Operators

#### Arithmetic
```python
a + b    # Addition
a - b    # Subtraction
a * b    # Multiplication
a / b    # Division
a % b    # Modulo (remainder)
a ** b   # Power/Exponentiation
```

#### Comparison
```python
a == b   # Equal to
a != b   # Not equal to
a > b    # Greater than
a < b    # Less than
a >= b   # Greater than or equal
a <= b   # Less than or equal
a is b   # Same as == (alternative syntax)
```

#### Logical
```python
a and b  # Logical AND
a or b   # Logical OR
not a    # Logical NOT
```

### Control Flow

#### If Statement
```python
if condition then
    # code
end

if condition then
    # code
else
    # code
end

# Nested if
if condition1 then
    # code
else
    if condition2 then
        # code
    else
        # code
    end
end
```

#### While Loop
```python
while condition do
    # code
    # Use 'break' to exit early
    # Use 'continue' to skip to next iteration
end

# Example
set i = 0
while i < 5 do
    say i
    i = i + 1
end
```

#### For Loop
```python
# Loop through a list
for item in list do
    # code
end

# Loop through a range
for i in range(start, end) do
    # code
end

# Examples
for fruit in ["apple", "banana"] do
    say fruit
end

for i in range(1, 6) do
    say i  # Prints 1, 2, 3, 4, 5
end
```

#### Break and Continue
```python
for i in range(10) do
    if i == 5 then
        break      # Exit loop
    end
    
    if i % 2 == 0 then
        continue   # Skip to next iteration
    end
    
    say i
end
```

### Functions

#### Definition
```python
# Simple function
function greet()
    say "Hello!"
end

# Function with parameters
function greet_person(name)
    say "Hello, " + name + "!"
end

# Function with return value
function add(a, b)
    return a + b
end

# Function with multiple returns
function get_stats(numbers)
    if len(numbers) == 0 then
        return 0
    end
    return sum(numbers) / len(numbers)
end
```

#### Calling Functions
```python
greet()                    # No arguments
greet_person("Alice")      # With argument
set result = add(5, 3)     # Capture return value
```

#### Recursion
```python
function factorial(n)
    if n <= 1 then
        return 1
    end
    return n * factorial(n - 1)
end

say factorial(5)  # 120
```

### Lists

#### Creation
```python
set empty = []
set numbers = [1, 2, 3, 4, 5]
set mixed = [1, "hello", true]
```

#### Indexing
```python
set first = numbers[0]      # First element
set last = numbers[4]       # Last element
```

#### Modification
```python
numbers[0] = 99            # Change element
```

#### Operations
```python
set combined = list1 + list2   # Concatenate lists
set length = len(numbers)       # Get length
```

#### Iteration
```python
for item in numbers do
    say item
end
```

### Built-in Functions

#### Type Conversion
```python
str(x)      # Convert to string
int(x)      # Convert to integer
float(x)    # Convert to float
```

#### List Functions
```python
len(list)           # Get length
sum(list)           # Sum all numbers
min(a, b, c)        # Minimum value
max(a, b, c)        # Maximum value
```

#### Math Functions
```python
abs(x)              # Absolute value
round(x)            # Round to nearest integer
round(x, n)         # Round to n decimal places
```

#### Range Function
```python
range(end)          # 0 to end-1
range(start, end)   # start to end-1
```

#### Random Functions
```python
random()            # Random float 0.0 to 1.0
randint(a, b)       # Random integer from a to b
```

#### Utility Functions
```python
type(x)             # Get type name as string
```

### Game-Specific Features

#### Say (Print)
```python
say "Hello, World!"
say message
say "Score: " + str(score)
```

#### Ask (Input)
```python
ask "What is your name?" into name
ask "Enter a number:" into num_str
set num = int(num_str)
```

#### Choice
```python
choice "Option 1" or "Option 2" or "Option 3"
# User selects, result stored in 'answer' variable

if answer is "Option 1" then
    # handle option 1
end
```

#### Labels and Goto
```python
label: start
# code
goto start  # Jump to label

label: game_over
say "Game Over!"
```

## Programming Patterns

### Pattern: Counter
```python
set count = 0
while count < 10 do
    say count
    count = count + 1
end
```

### Pattern: Accumulator
```python
set total = 0
for num in numbers do
    total = total + num
end
say "Total: " + str(total)
```

### Pattern: Find Maximum
```python
set max_val = numbers[0]
for num in numbers do
    if num > max_val then
        max_val = num
    end
end
```

### Pattern: Filter List
```python
function get_evens(numbers)
    set evens = []
    for num in numbers do
        if num % 2 == 0 then
            evens = evens + [num]
        end
    end
    return evens
end
```

### Pattern: Validation Loop
```python
set valid = false
while not valid do
    ask "Enter a number (1-10):" into input
    set num = int(input)
    
    if num >= 1 and num <= 10 then
        valid = true
        say "Valid input!"
    else
        say "Please try again."
    end
end
```

## Best Practices

### 1. Use Descriptive Names
```python
# Good
set player_health = 100
set enemy_damage = 15

# Bad
set ph = 100
set ed = 15
```

### 2. Comment Your Code
```python
# Calculate the average score
set total = sum(scores)
set average = total / len(scores)
```

### 3. Break Into Functions
```python
# Good - modular
function calculate_damage(base, multiplier)
    return base * multiplier
end

function apply_damage(health, damage)
    return health - damage
end

# Use the functions
set damage = calculate_damage(10, 1.5)
set new_health = apply_damage(100, damage)
```

### 4. Validate Input
```python
ask "Enter age:" into age_str
set age = int(age_str)

if age < 0 or age > 150 then
    say "Invalid age!"
else
    say "Age accepted: " + str(age)
end
```

### 5. Use Constants
```python
set MAX_HEALTH = 100
set DAMAGE_MULTIPLIER = 1.5
set STARTING_GOLD = 50
```

## Common Errors and Solutions

### Error: Variable not defined
```python
# Problem
say x  # Error if x not defined

# Solution
set x = 10
say x
```

### Error: Division by zero
```python
# Problem
set result = 10 / 0  # Error!

# Solution
if denominator != 0 then
    set result = numerator / denominator
else
    say "Cannot divide by zero!"
end
```

### Error: Index out of range
```python
# Problem
set item = list[100]  # Error if list too short

# Solution
if index >= 0 and index < len(list) then
    set item = list[index]
else
    say "Invalid index!"
end
```

### Error: Wrong number of arguments
```python
# Problem
function add(a, b)
    return a + b
end
add(5)  # Error! Need 2 arguments

# Solution
add(5, 3)  # Correct
```

## Advanced Topics

### Closure (Variables from outer scope)
```python
set multiplier = 2

function multiply(x)
    return x * multiplier  # Uses 'multiplier' from outer scope
end

say multiply(5)  # 10
```

### Higher-order Functions (Functions that return values)
```python
function create_adder(n)
    return n  # Simplified example
end

set five = create_adder(5)
# Note: Full closures not yet implemented
```

### List Comprehension Pattern
```python
# Create a new list with transformed values
function double_all(numbers)
    set result = []
    for num in numbers do
        result = result + [num * 2]
    end
    return result
end

set doubled = double_all([1, 2, 3, 4])
# doubled is [2, 4, 6, 8]
```

## Quick Reference Card

| Feature | Syntax |
|---------|--------|
| Variable | `set x = 10` or `x = 10` |
| String | `"text"` or `'text'` |
| List | `[1, 2, 3]` |
| If | `if cond then ... end` |
| While | `while cond do ... end` |
| For | `for x in list do ... end` |
| Function | `function name(params) ... end` |
| Return | `return value` |
| Print | `say "text"` |
| Input | `ask "prompt" into var` |
| Comment | `# comment` |
| And | `and` |
| Or | `or` |
| Not | `not` |
| Equal | `==` or `is` |
| Not Equal | `!=` |

---

**Quill** - Learn programming the easy way! 🚀
