# 🎒 Inventory System - New Feature!

## Overview

Quill now has a **complete inventory system** perfect for game development! Players can collect items, check what they have, and use items in their adventures.

---

## 📋 New Commands

### `add_item(item_name)`
Add an item to the player's inventory.

```python
add_item("sword")
add_item("health potion")
add_item("gold coin")
```

**Output:** `✓ Added 'sword' to inventory`

---

### `remove_item(item_name)`
Remove an item from inventory.

```python
remove_item("rusty key")
```

**Output:** `✓ Removed 'rusty key' from inventory`

If item doesn't exist: `✗ 'rusty key' not found in inventory`

---

### `has_item(item_name)`
Check if player has a specific item (returns `true` or `false`).

```python
if has_item("sword") then
    say "You can fight with your sword!"
end

if has_item("key") then
    say "You can unlock the door!"
else
    say "You need a key!"
end
```

---

### `show_inventory()`
Display all items in a nice formatted list.

```python
show_inventory()
```

**Output:**
```
========================================
          INVENTORY
========================================
  • sword
  • health potion
  • gold coin (x3)
========================================
Total items: 5
========================================
```

---

### `item_count()`
Get the total number of items.

```python
set total = item_count()
say "You have " + str(total) + " items"

if item_count() > 10 then
    say "Your inventory is getting full!"
end
```

---

### `clear_inventory()`
Remove all items from inventory.

```python
clear_inventory()
```

**Output:** `✓ Inventory cleared`

---

## 🎮 Example Usage

### Basic Item Collection
```python
say "You find a sword!"
add_item("sword")

say "You find a shield!"
add_item("shield")

show_inventory()
```

### Quest Items
```python
say "You need 3 gems to open the door."

add_item("red gem")
add_item("blue gem")
add_item("green gem")

if item_count() >= 3 then
    say "You have all the gems!"
end
```

### Check Before Using
```python
say "You need a key to escape."

if has_item("rusty key") then
    say "You use the key on the door..."
    remove_item("rusty key")
    say "The door opens!"
else
    say "You need to find a key first!"
end
```

### Currency System
```python
add_item("gold coin")
add_item("gold coin")
add_item("gold coin")

say "Merchant: 'That sword costs 3 gold coins.'"

if item_count() >= 3 then
    remove_item("gold coin")
    remove_item("gold coin")
    remove_item("gold coin")
    add_item("iron sword")
    say "Purchased!"
end
```

### Equipment Check
```python
say "Checking your equipment..."

set equipped = 0

if has_item("sword") then
    say "✓ Sword equipped"
    equipped = equipped + 1
end

if has_item("armor") then
    say "✓ Armor equipped"
    equipped = equipped + 1
end

if has_item("shield") then
    say "✓ Shield equipped"
    equipped = equipped + 1
end

say "Equipment level: " + str(equipped) + "/3"
```

---

## 🎯 Game Design Tips

### 1. **Inventory Limits**
```python
if item_count() >= 10 then
    say "Your inventory is full!"
else
    add_item("new item")
end
```

### 2. **Multiple Items**
Inventory automatically stacks duplicates:
```python
add_item("arrow")
add_item("arrow")
add_item("arrow")
show_inventory()  # Shows: arrow (x3)
```

### 3. **Key Items for Progression**
```python
if has_item("boss key") then
    say "You can enter the final room!"
    goto final_boss
else
    say "The door is locked."
end
```

### 4. **Consumables**
```python
if has_item("health potion") then
    choice "Use health potion?" or "Save it"
    
    if answer is "Use health potion?" then
        remove_item("health potion")
        health = 100
        say "Health restored!"
    end
end
```

---

## 💡 Pro Tips

1. **Item names are case-sensitive** - "Sword" ≠ "sword"
2. **Use descriptive names** - "iron sword" is better than "sword1"
3. **Check before removing** - Use `has_item()` first
4. **Show inventory regularly** - Let players see what they have
5. **Combine with variables** - Track special item properties

---

## 🚀 Next Steps

Now you can build:
- **RPG Games** with equipment systems
- **Adventure Games** with item collection
- **Puzzle Games** with key items
- **Shop Systems** with currency
- **Crafting Systems** (coming soon!)

---

## 📝 Complete Example Game

See `examples/demo_inventory.quill` for a full working example!

Try it:
```bash
.\Quill examples\demo_inventory.quill
```

---

**Inventory System v1.0** - Perfect for game developers! 🎮
