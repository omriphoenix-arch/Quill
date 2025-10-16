# 💾 Save/Load System - New Feature!

## Overview

Quill now has a **complete save/load system** that lets players save their progress and continue later! Perfect for longer games, RPGs, and adventures.

---

## 📋 New Commands

### `save_game(filename)`
Save the current game state to a file.

```python
save_game("mysave")
save_game("slot1")
save_game("quicksave")
```

**What gets saved:**
- ✅ All variables (numbers, strings, booleans, lists)
- ✅ Complete inventory
- ✅ Player progress

**Output:** `💾 Game saved to: saves\mysave.save`

**Note:** Files are automatically saved with `.save` extension in the `saves/` folder.

---

### `load_game(filename)`
Load a previously saved game.

```python
load_game("mysave")
load_game("slot1")
```

**What gets restored:**
- ✅ All saved variables
- ✅ Complete inventory
- ✅ Player progress

**Output:** `✓ Game loaded from: saves\mysave.save`

**Returns:** `true` if successful, `false` if file not found

---

### `has_save(filename)`
Check if a save file exists (returns `true` or `false`).

```python
if has_save("mysave") then
    say "Found existing save!"
    choice "Load game" or "New game"
    
    if answer is "Load game" then
        load_game("mysave")
    end
end
```

---

### `delete_save(filename)`
Delete a save file.

```python
delete_save("mysave")
```

**Output:** `✓ Deleted save file: saves\mysave.save`

**Returns:** `true` if successful, `false` if file not found

---

## 🎮 Usage Examples

### Basic Save/Load
```python
# Save the game
say "Saving your progress..."
save_game("autosave")

# Load the game
say "Loading your save..."
load_game("autosave")
```

---

### Multiple Save Slots
```python
say "Choose a save slot:"
choice "Slot 1" or "Slot 2" or "Slot 3"

if answer is "Slot 1" then
    save_game("slot1")
end

if answer is "Slot 2" then
    save_game("slot2")
end

if answer is "Slot 3" then
    save_game("slot3")
end
```

---

### Continue or New Game Menu
```python
say "==============================="
say "    GAME TITLE"
say "==============================="
say ""

if has_save("autosave") then
    choice "Continue" or "New Game"
    
    if answer is "Continue" then
        load_game("autosave")
        say "Welcome back!"
        goto continue_game
    else
        say "Starting new game..."
        goto new_game
    end
else
    say "No save found. Starting new game..."
    goto new_game
end

label: new_game
# Initialize new game variables
set level = 1
set gold = 0
# etc...

label: continue_game
# Continue from loaded state
say "Continuing adventure..."
```

---

### Auto-Save System
```python
function autosave()
    say "Auto-saving..."
    save_game("autosave")
end

# Call after important events
say "You completed the quest!"
autosave()

say "You reached a checkpoint!"
autosave()
```

---

### Save Before Dangerous Choice
```python
say "You approach the dragon's lair..."
say "This is a point of no return!"
say ""

choice "Enter the lair" or "Turn back"

if answer is "Enter the lair" then
    say "Saving your progress first..."
    save_game("before_dragon")
    say "Good luck!"
    # Dragon fight begins
end
```

---

### Save Game Stats
```python
# Before saving
say "Saving your progress..."
say "  Level: " + str(level)
say "  Gold: " + str(gold)
say "  Location: " + location
say "  Items: " + str(item_count())

save_game("mysave")
```

---

### Load with Error Handling
```python
say "Loading save file..."

if has_save("mysave") then
    load_game("mysave")
    say "Game loaded successfully!"
else
    say "Error: Save file not found!"
    say "Starting new game instead..."
end
```

---

### Delete Old Saves
```python
say "Save Manager"
say ""

if has_save("oldsave") then
    choice "Delete old save?" or "Keep it"
    
    if answer is "Delete old save?" then
        delete_save("oldsave")
        say "Old save deleted!"
    end
end
```

---

## 💡 Advanced Patterns

### Named Save Slots
```python
ask "Enter a name for this save:" into save_name
save_game(save_name)
say "Game saved as: " + save_name
```

### Quick Save/Load
```python
# F5 = Quick Save (in menu system)
if answer is "Quick Save" then
    save_game("quicksave")
end

# F9 = Quick Load (in menu system)
if answer is "Quick Load" then
    if has_save("quicksave") then
        load_game("quicksave")
    else
        say "No quick save found!"
    end
end
```

### Checkpoint System
```python
function checkpoint(name)
    say "Checkpoint reached!"
    save_game(name)
end

# Use throughout game
checkpoint("chapter1_complete")
checkpoint("boss_defeated")
checkpoint("final_area")
```

---

## 📁 Save File Details

### Location
All save files are stored in: `saves/` folder

### Format
- Files use `.save` extension
- Stored as JSON (human-readable)
- Can be backed up/copied

### What's Saved
```json
{
  "variables": {
    "player_name": "Hero",
    "level": 10,
    "gold": 500,
    "health": 100,
    "location": "Castle"
  },
  "inventory": [
    "sword",
    "shield",
    "potion"
  ]
}
```

### What's NOT Saved
- Functions (they're part of the code)
- Labels (they're part of the code)
- System state (current line, etc.)

---

## 🎯 Game Design Tips

### 1. **Save Points**
Add save points at logical locations:
```python
say "You find a campfire. Rest here?"
choice "Rest and save" or "Continue"

if answer is "Rest and save" then
    save_game("autosave")
    health = 100  # Restore health
    say "Game saved! Health restored."
end
```

### 2. **Multiple Slots**
Let players manage multiple saves:
```python
say "Save Slots:"
say "  1. " + (has_save("slot1") and "Used" or "Empty")
say "  2. " + (has_save("slot2") and "Used" or "Empty")
say "  3. " + (has_save("slot3") and "Used" or "Empty")
```

### 3. **Permadeath Mode**
For hardcore games:
```python
if death then
    say "You died!"
    if has_save("permadeath") then
        delete_save("permadeath")
        say "Save file deleted. Game over."
    end
end
```

### 4. **Time Stamps**
Save when important events happen:
```python
save_game("before_boss_fight")
save_game("chapter_1_complete")
save_game("ending_good")
```

---

## 🚀 Best Practices

1. **Auto-save regularly** - Don't make players remember
2. **Save before danger** - Let players try risky choices
3. **Multiple slots** - Let players experiment
4. **Clear feedback** - Show when saves happen
5. **Test loading** - Make sure saves restore properly

---

## 📝 Complete Example

See `examples/demo_saveload.quill` for a full working example!

Try it:
```bash
.\Quill examples\demo_saveload.quill
```

Run it multiple times to see save/load in action!

---

## ⚠️ Important Notes

- Save files are **text files (JSON)** - don't edit them manually
- **Backup save files** for important progress
- Saves work **across game sessions** - perfect for long games
- Variables must be **simple types** (no complex objects)

---

**Save/Load System v1.0** - Make longer, better games! 💾🎮
