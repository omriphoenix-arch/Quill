# Quill Error Messages Guide

Understanding and fixing common errors in Quill programs.

---

## 📋 Table of Contents

1. [Syntax Errors](#syntax-errors)
2. [Runtime Errors](#runtime-errors)
3. [Type Errors](#type-errors)
4. [Variable Errors](#variable-errors)
5. [Logic Errors](#logic-errors)
6. [How to Read Error Messages](#how-to-read-error-messages)
7. [Debugging Tips](#debugging-tips)

---

## How to Read Error Messages

Quill error messages follow this format:

```
Error on line 5: SyntaxError: Expected 'then' after if statement
  4 | if score > 100
  5 |     say "High score!"
      ^
```

### Parts of an Error Message:

1. **Line Number** - Where the error occurred (line 5)
2. **Error Type** - What kind of error (SyntaxError)
3. **Description** - What went wrong
4. **Code Context** - Shows the problematic line
5. **Pointer** - Arrow (^) points to the issue

---

## Syntax Errors

Syntax errors happen when code doesn't follow Quill's rules.

### Error: "Expected 'then' after if statement"

**What it means:** You wrote `if` but forgot `then`

**Example (Wrong):**
```Quill
if score > 100
    say "High score!"
end
```

**Fix:**
```Quill
if score > 100 then
    say "High score!"
end
```

---

### Error: "Expected 'end' to close block"

**What it means:** You opened an `if`, `while`, or `function` but forgot to close it

**Example (Wrong):**
```Quill
if age > 18 then
    say "Adult"
# Missing 'end'

say "Done"
```

**Fix:**
```Quill
if age > 18 then
    say "Adult"
end

say "Done"
```

---

### Error: "Expected 'do' after while/for statement"

**What it means:** Loops need `do` before their body

**Example (Wrong):**
```Quill
while count > 0
    say str(count)
    set count = count - 1
end
```

**Fix:**
```Quill
while count > 0 do
    say str(count)
    set count = count - 1
end
```

---

### Error: "Unexpected token"

**What it means:** Found something that doesn't make sense in that position

**Example (Wrong):**
```Quill
set name = Alice  # Missing quotes
```

**Fix:**
```Quill
set name = "Alice"  # Strings need quotes
```

**Common causes:**
- Missing quotes around strings
- Extra or missing parentheses
- Typos in keywords
- Wrong operators

---

### Error: "Invalid syntax"

**What it means:** General syntax problem - check for typos

**Example (Wrong):**
```Quill
iff score > 100 then  # Typo: 'iff' instead of 'if'
    say "High score"
end
```

**Fix:**
```Quill
if score > 100 then
    say "High score"
end
```

---

## Runtime Errors

Runtime errors happen while the program is running.

### Error: "Division by zero"

**What it means:** Tried to divide a number by zero

**Example (Wrong):**
```Quill
set result = 10 / 0  # Can't divide by zero!
```

**Fix:**
```Quill
set divisor = 0
if divisor is 0 then
    say "Error: Cannot divide by zero"
else
    set result = 10 / divisor
    say str(result)
end
```

---

### Error: "Index out of range"

**What it means:** Tried to access a list item that doesn't exist

**Example (Wrong):**
```Quill
set numbers = [1, 2, 3]
say numbers[5]  # Only 3 items (0, 1, 2)
```

**Fix:**
```Quill
set numbers = [1, 2, 3]
if len(numbers) > 5 then
    say numbers[5]
else
    say "Index 5 doesn't exist"
end
```

---

### Error: "Maximum recursion depth exceeded"

**What it means:** Function called itself too many times

**Example (Wrong):**
```Quill
function loop_forever() do
    loop_forever()  # Calls itself forever!
end

loop_forever()
```

**Fix:**
```Quill
function countdown(n) do
    if n <= 0 then
        return  # Stop condition!
    end
    say str(n)
    countdown(n - 1)
end

countdown(5)
```

---

### Error: "File not found"

**What it means:** Tried to import a file that doesn't exist

**Example (Wrong):**
```Quill
import "nonexistent_file"
```

**Fix:**
```Quill
import "utilities"  # Make sure file exists
```

Check:
- File name is spelled correctly
- File is in the same directory
- File has .quill extension

---

## Type Errors

Type errors happen when you use the wrong type of value.

### Error: "Cannot concatenate str and int"

**What it means:** Tried to join a string and number without converting

**Example (Wrong):**
```Quill
set score = 100
say "Score: " + score  # Can't join string and number
```

**Fix:**
```Quill
set score = 100
say "Score: " + str(score)  # Convert to string first
```

---

### Error: "Cannot convert 'abc' to int"

**What it means:** Tried to convert non-numeric text to a number

**Example (Wrong):**
```Quill
ask "Enter a number:" into input
set number = int(input)  # What if they type "hello"?
```

**Fix:**
```Quill
ask "Enter a number:" into input

# Check if it's a valid number first
set number = 0
if input is "0" or input is "1" or input is "2" then
    set number = int(input)
else
    say "That's not a valid number!"
end
```

**Better fix (with error handling):**
```Quill
ask "Enter a number:" into input
try
    set number = int(input)
    say "You entered: " + str(number)
catch
    say "Error: Please enter a valid number"
end
```

---

### Error: "Unsupported operand type"

**What it means:** Used an operator on wrong types (like multiplying strings)

**Example (Wrong):**
```Quill
set result = "hello" * "world"  # Can't multiply strings
```

**Fix:**
```Quill
set result = "hello" * 3  # Repeats string 3 times: "hellohellohello"
```

---

## Variable Errors

### Error: "Variable 'name' is not defined"

**What it means:** Used a variable that doesn't exist yet

**Example (Wrong):**
```Quill
say "Hello " + name  # 'name' doesn't exist yet
```

**Fix:**
```Quill
set name = "Alice"
say "Hello " + name
```

Or:
```Quill
ask "What's your name?" into name
say "Hello " + name
```

---

### Error: "Cannot assign to undefined variable"

**What it means:** Tried to change a variable before creating it

**Example (Wrong):**
```Quill
score = score + 10  # 'score' doesn't exist
```

**Fix:**
```Quill
set score = 0      # Create it first
score = score + 10  # Now update it
```

---

## Logic Errors

Logic errors don't cause error messages but make programs behave wrong.

### Problem: "Infinite loop"

**What it means:** Loop never ends

**Example (Wrong):**
```Quill
set count = 0
while count < 10 do
    say "Count: " + str(count)
    # Forgot to increase count!
end
```

**Fix:**
```Quill
set count = 0
while count < 10 do
    say "Count: " + str(count)
    set count = count + 1  # Increase counter
end
```

---

### Problem: "Wrong comparison"

**What it means:** Using `=` instead of `is` or `==`

**Example (Wrong):**
```Quill
if score = 100 then  # This assigns 100 to score!
    say "Perfect!"
end
```

**Fix:**
```Quill
if score is 100 then  # This checks equality
    say "Perfect!"
end
```

---

### Problem: "Order of operations"

**What it means:** Math calculated in wrong order

**Example (Wrong):**
```Quill
set result = 10 + 5 * 2  # Is it 30 or 20?
```

**Fix:**
```Quill
set result = (10 + 5) * 2  # Forces order: 30
# or
set result = 10 + (5 * 2)  # Makes it clear: 20
```

---

## Common Beginner Mistakes

### 1. Forgetting Quotes

**Wrong:**
```Quill
set name = Alice
```

**Right:**
```Quill
set name = "Alice"
```

---

### 2. Not Converting Types

**Wrong:**
```Quill
say "Age: " + age
```

**Right:**
```Quill
say "Age: " + str(age)
```

---

### 3. Missing `end` keyword

**Wrong:**
```Quill
if condition then
    say "Yes"
# Forgot 'end'
```

**Right:**
```Quill
if condition then
    say "Yes"
end
```

---

### 4. Using `=` in conditions

**Wrong:**
```Quill
if name = "Alice" then
```

**Right:**
```Quill
if name is "Alice" then
```

---

### 5. Not initializing variables

**Wrong:**
```Quill
set count = count + 1  # count doesn't exist yet
```

**Right:**
```Quill
set count = 0
set count = count + 1
```

---

## Debugging Tips

### 1. Use `say` to print values

```Quill
say "Debug: score = " + str(score)
say "Debug: name = " + name
```

### 2. Check types

```Quill
say "Type of score: " + type(score)
```

### 3. Test parts separately

Instead of:
```Quill
set result = (a + b) * (c - d) / e
```

Do:
```Quill
set sum = a + b
say "sum = " + str(sum)

set diff = c - d
say "diff = " + str(diff)

set product = sum * diff
say "product = " + str(product)

set result = product / e
say "result = " + str(result)
```

### 4. Comment out code

```Quill
# if problematic_condition then
#     do_something()
# end
```

### 5. Start simple, add complexity

Build your program step by step:
1. Get it working with simple values
2. Add variables
3. Add conditions
4. Add loops
5. Add functions

### 6. Read error messages carefully

- Note the line number
- Read the entire message
- Check the line mentioned
- Check lines before and after

### 7. Use VS Code's syntax highlighting

Colors help catch:
- Missing quotes (strings aren't green)
- Typos in keywords (wrong color)
- Mismatched brackets

---

## Getting Help

### Before asking for help:

1. **Read the error message** - It often tells you exactly what's wrong
2. **Check line number** - Look at that line and nearby lines
3. **Try the fixes above** - Many errors have simple solutions
4. **Check documentation** - [Keywords Reference](Quill_KEYWORDS_REFERENCE.md)
5. **Look at examples** - See how working programs do it

### When asking for help:

Include:
- The error message (exact text)
- The line number
- Your code (at least the relevant part)
- What you expected to happen
- What actually happened

**Good question:**
```
I'm getting "Variable 'score' is not defined" on line 10.
Here's my code:

if answer is "correct" then
    set score = score + 10  # Line 10
end

I want to increase the score when the answer is correct,
but it says 'score' doesn't exist. How do I fix this?
```

**What's good:**
- Specific error message
- Line number
- Code sample
- Clear explanation

---

## Quick Reference: Common Errors

| Error Message | Likely Cause | Quick Fix |
|--------------|--------------|-----------|
| Expected 'then' | Missing `then` after `if` | Add `then` |
| Expected 'end' | Forgot to close block | Add `end` |
| Expected 'do' | Missing `do` after loop | Add `do` |
| Variable not defined | Used before creating | Use `set` first |
| Cannot concatenate | Mixed string and number | Use `str()` |
| Division by zero | Divided by 0 | Check denominator |
| Invalid syntax | Typo in keyword | Check spelling |
| Index out of range | List index too large | Check list length |

---

## Practice Exercises

Try to find and fix the errors in these programs:

### Exercise 1:
```Quill
if score > 100
    say "High score"
end
```
<details>
<summary>Answer</summary>
Missing `then` after the condition.

**Fix:**
```Quill
if score > 100 then
    say "High score"
end
```
</details>

### Exercise 2:
```Quill
set name = Alice
say "Hello " + name
```
<details>
<summary>Answer</summary>
Missing quotes around "Alice".

**Fix:**
```Quill
set name = "Alice"
say "Hello " + name
```
</details>

### Exercise 3:
```Quill
set age = 25
say "You are " + age + " years old"
```
<details>
<summary>Answer</summary>
Need to convert age to string.

**Fix:**
```Quill
set age = 25
say "You are " + str(age) + " years old"
```
</details>

---

## Conclusion

Errors are a normal part of programming! Everyone makes them, even experienced programmers.

**Remember:**
- Read error messages carefully
- Check the line number
- Look for simple fixes first
- Use debugging techniques
- Don't hesitate to ask for help

The more you program, the better you'll get at spotting and fixing errors quickly!

Happy debugging! 🐛✨
