# Quill Reserved Keywords

This document lists all reserved keywords in Quill v1.0.0. You **cannot** use these words as variable names, function names, or identifiers.

## ⚠️ Why This Matters

If you try to use a reserved keyword as a variable name, you'll get a syntax error like:
```
✗ Syntax Error: Expected TokenType.IDENTIFIER, got TokenType.CHOICE at line 10
```

## 📋 Complete List of Reserved Keywords

### Output Commands
- `say`
- `print`
- `speak`
- `tell`
- `write`

### Input Commands
- `ask`
- `prompt`

### Variable Declaration
- `set`
- `let`
- `make`
- `create`
- `to`
- `equals`
- `into`

### Conditionals
- `if`
- `when`
- `then`
- `else`
- `otherwise`
- `elsif`
- `elif`
- `elseif`
- `end`
- `done`
- `finish`

### Loops
- `while`
- `repeat`
- `do`
- `for`
- `each`
- `in`
- `from`

### Flow Control
- `break`
- `continue`
- `goto`
- `jump`
- `go`
- `label`

### Functions
- `function`
- `func`
- `def`
- `define`
- `return`
- `give`

### Logic & Comparison
- `and`
- `or`
- `not`
- `is`

### Special Commands
- `choice` (for multiple choice menus)
- `import`

### Boolean Values
- `true`
- `false`

### Null Values
- `null`
- `none`

## ✅ Good Variable Names (Safe to Use)

These common words are **NOT** reserved and safe to use:

```Quill
# ✅ These all work fine:
set name = "Alice"
set age = 25
set score = 100
set health = 50
set items = []
set count = 0
set total = 0
set message = "Hello"
set player = "Bob"
set enemy = "Dragon"
set damage = 10
set level = 5
set experience = 1000
set gold = 500
set position = "north"
set status = "alive"
set answer = "yes"
set result = 42
set value = 3.14
set data = [1, 2, 3]
```

## ❌ Common Mistakes

### Using 'choice' as a variable
```Quill
# ❌ WRONG - 'choice' is a reserved keyword
ask "Enter your choice:" into choice

# ✅ CORRECT - Use a different name
ask "Enter your choice:" into user_choice
ask "Enter your choice:" into selection
ask "Enter your choice:" into option_num
```

### Using 'question' as a variable
```Quill
# ❌ WRONG - 'question' was a keyword (now removed in v1.0.0)
# But avoid similar confusion

# ✅ CORRECT
ask "Do you want to continue?" into answer
ask "Do you want to continue?" into response
ask "Do you want to continue?" into user_input
```

### Using loop keywords
```Quill
# ❌ WRONG - 'repeat' is a synonym for 'while'
set repeat = 5

# ✅ CORRECT
set repeat_count = 5
set num_repeats = 5
set iterations = 5
```

## 💡 Tips for Avoiding Conflicts

1. **Be specific** - Instead of `choice`, use `user_choice`, `menu_choice`, or `selection`
2. **Add prefixes/suffixes** - `my_variable`, `variable_name`, `current_status`
3. **Use underscores** - `user_input` instead of trying `input` alone
4. **Check the list** - When in doubt, check this document!

## 🔍 How to Check if a Word is Reserved

Run this test program:

```Quill
# Test if a word is reserved
set YOUR_WORD_HERE = 1
say "Success! This word is safe to use."
```

If you get a syntax error, the word is reserved!

## 📝 Version History

### v1.0.0 (October 15, 2025)
- Removed GUI keywords (`window`, `button`, `color`, `style`, `size`, etc.)
- Removed `question` as alias for `ask`
- Removed `choose`, `select`, `option` as aliases for `choice`
- Core language keywords only

### Future Versions
GUI keywords may be re-introduced as optional extensions in v1.1.0+

## 🆘 Need Help?

If you encounter a keyword conflict:

1. **Read the error message** - It tells you which keyword caused the problem
2. **Rename your variable** - Choose a more descriptive name
3. **Check this list** - Make sure your new name isn't reserved
4. **See ERROR_MESSAGES.md** - For more debugging help

---

**Remember:** Descriptive variable names make your code easier to read anyway! `user_choice` is clearer than `choice`, and `player_health` is clearer than `health`. 💪
