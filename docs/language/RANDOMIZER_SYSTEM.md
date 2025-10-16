# Mission Randomizer System

## Overview
Create randomized outcomes for missions, events, and decisions in your games! This system uses Quill's built-in random functions to determine success or failure based on probability.

## Available Random Functions

### `random()`
Returns a random decimal number between 0 and 1.
```Quill
set chance to random()
# Result: 0.742, 0.123, 0.891, etc.
```

### `randint(min, max)`
Returns a random integer between min and max (inclusive).
```Quill
set roll to randint(1, 100)
# Result: 1, 2, 3, ... 99, 100
```

## Basic Patterns

### 1. Simple 50/50 Chance
```Quill
set coin_flip to randint(1, 2)

if coin_flip is 1 then
    say "Heads!"
else
    say "Tails!"
end
```

### 2. Percentage-Based Success
```Quill
# 70% success rate
set roll to randint(1, 100)

if roll <= 70 then
    say "✓ SUCCESS!"
else
    say "✗ FAILURE!"
end
```

### 3. Custom Probability
```Quill
# 1 in 4 chance (25%)
set roll to randint(1, 4)

if roll is 1 then
    say "You found a rare item!"
else
    say "Nothing special."
end
```

## Mission Success System

### Basic Mission Roll
```Quill
say "Attempting mission..."

set success_chance to 60  # 60% chance
set roll to randint(1, 100)

if roll <= success_chance then
    say "✓ MISSION SUCCESS!"
    say "Roll: " + str(roll) + "/" + str(success_chance)
else
    say "✗ MISSION FAILED!"
    say "Roll: " + str(roll) + "/" + str(success_chance)
end
```

### Difficulty Levels
```Quill
# Define difficulty levels
set easy to 80
set medium to 60
set hard to 40
set very_hard to 20

# Choose difficulty
set mission_difficulty to hard

# Roll for success
set roll to randint(1, 100)

if roll <= mission_difficulty then
    say "✓ SUCCESS!"
else
    say "✗ FAILURE!"
end
```

### Skill-Based Success
```Quill
# Player's skill affects success rate
set player_skill to 65
set roll to randint(1, 100)

say "Your skill: " + str(player_skill)
say "Rolling..."

if roll <= player_skill then
    say "✓ Your training paid off!"
else
    say "✗ You need more practice."
end
```

## Advanced Patterns

### Critical Success/Failure
```Quill
set roll to randint(1, 100)

if roll >= 95 then
    say "🌟 CRITICAL SUCCESS!"
    say "Beyond all expectations!"
else
    if roll >= 50 then
        say "✓ Success"
    else
        if roll >= 10 then
            say "✗ Failure"
        else
            say "💥 CRITICAL FAILURE!"
            say "Everything went wrong!"
        end
    end
end
```

### Multiple Modifiers
```Quill
# Base chance + bonuses
set base_chance to 40
set skill_bonus to 15
set equipment_bonus to 10
set total_chance to base_chance + skill_bonus + equipment_bonus

say "Base: " + str(base_chance) + "%"
say "Skill: +" + str(skill_bonus) + "%"
say "Equipment: +" + str(equipment_bonus) + "%"
say "Total: " + str(total_chance) + "%"

set roll to randint(1, 100)

if roll <= total_chance then
    say "✓ SUCCESS!"
else
    say "✗ FAILURE!"
end
```

### D20 Style (RPG Dice)
```Quill
# Roll a 20-sided die
set roll to randint(1, 20)
set difficulty to 15

say "Rolling d20..."
say "You rolled: " + str(roll)

if roll is 20 then
    say "🌟 NATURAL 20! Critical success!"
else
    if roll >= difficulty then
        say "✓ Success! (needed " + str(difficulty) + "+)"
    else
        if roll is 1 then
            say "💥 NATURAL 1! Critical failure!"
        else
            say "✗ Failed (needed " + str(difficulty) + "+)"
        end
    end
end
```

### Reusable Mission Function
```Quill
function check_mission(success_chance)
    set roll to randint(1, 100)
    
    say "Rolling... " + str(roll) + "/100"
    
    if roll <= success_chance then
        say "✓ MISSION SUCCESS!"
        return true
    else
        say "✗ MISSION FAILED!"
        return false
    end
end

# Use the function
say "Mission 1: Stealth infiltration (70% chance)"
set result to check_mission(70)

say ""
say "Mission 2: Combat assault (40% chance)"
set result to check_mission(40)
```

## Complete Examples

### Example 1: Simple Combat
```Quill
say "Enemy approaching!"
ask "Do you fight or flee? (fight/flee)"

if answer is "fight" then
    say "You draw your weapon..."
    wait(1)
    
    set combat_roll to randint(1, 100)
    
    if combat_roll <= 65 then
        say "✓ You defeated the enemy!"
        add_item("enemy loot")
    else
        say "✗ You were defeated!"
        say "You lose 10 health."
    end
end
```

### Example 2: Treasure Hunt
```Quill
say "You search the ancient chest..."
wait(1)

set treasure_roll to randint(1, 100)

if treasure_roll >= 90 then
    say "🌟 LEGENDARY ITEM FOUND!"
    add_item("legendary sword")
else
    if treasure_roll >= 60 then
        say "✓ You found a rare item!"
        add_item("magic potion")
    else
        if treasure_roll >= 30 then
            say "You found some gold."
            add_item("gold coins")
        else
            say "The chest is empty."
        end
    end
end
```

### Example 3: Stealth Mission
```Quill
say "Infiltrating enemy base..."
wait(1)

# Player choices affect success
set stealth_skill to 50

ask "Do you have stealth gear? (yes/no)"

if answer is "yes" then
    set stealth_skill to stealth_skill + 20
    say "Stealth bonus: +20%"
end

ask "Take the risky shortcut? (yes/no)"

if answer is "yes" then
    set stealth_skill to stealth_skill - 15
    say "Risk penalty: -15%"
end

say "Total stealth chance: " + str(stealth_skill) + "%"
wait(1)

set roll to randint(1, 100)

if roll <= stealth_skill then
    say "✓ Infiltration successful!"
    say "You remain undetected."
else
    say "✗ You were spotted!"
    say "Guards are alerted!"
end
```

### Example 4: Multi-Stage Mission
```Quill
say "=== OPERATION: SILENT STRIKE ==="
say ""

# Stage 1: Approach
say "Stage 1: Approaching target..."
set stage1 to randint(1, 100)

if stage1 <= 80 then
    say "✓ Approach successful"
    wait(1)
    
    # Stage 2: Breach
    say "Stage 2: Breaching perimeter..."
    set stage2 to randint(1, 100)
    
    if stage2 <= 60 then
        say "✓ Breach successful"
        wait(1)
        
        # Stage 3: Objective
        say "Stage 3: Securing objective..."
        set stage3 to randint(1, 100)
        
        if stage3 <= 70 then
            say "✓ Objective secured!"
            say ""
            say "🌟 MISSION COMPLETE!"
            say "Full success bonus awarded!"
        else
            say "✗ Objective failed"
            say "Mission incomplete"
        end
    else
        say "✗ Breach failed"
        say "Mission aborted"
    end
else
    say "✗ Approach failed"
    say "Enemy detected our presence"
    say "Mission aborted"
end
```

## Probability Reference

### Common Success Rates
- **10-20%**: Very Hard / Heroic attempts
- **30-40%**: Hard / Risky actions
- **50-60%**: Moderate / Fair chance
- **70-80%**: Easy / Good odds
- **90-95%**: Very Easy / Almost certain

### Balancing Tips
1. **Too Easy (90%+)**: Not exciting, feels scripted
2. **Balanced (60-70%)**: Good challenge, rewarding
3. **Too Hard (20-30%)**: Frustrating for players
4. **Random Elements**: Keep around 50% for pure luck

### Player Experience
```Quill
# Let players see their odds
say "Success chance: 70%"
ask "Attempt mission? (yes/no)"

# Show the roll result
set roll to randint(1, 100)
say "Rolling... " + str(roll) + "/100"

# Players appreciate transparency
```

## Best Practices

### ✅ DO:
- Show players the success chance
- Display the roll result
- Balance difficulty appropriately
- Use randomness for excitement
- Give modifiers meaning

### ❌ DON'T:
- Make everything random
- Hide all probabilities
- Use unfair odds (too hard/easy)
- Randomize critical story moments
- Forget to show roll results

## Quick Templates

### Combat Template
```Quill
function combat_check(enemy_name, difficulty)
    say "Fighting " + enemy_name + "..."
    set roll to randint(1, 100)
    
    if roll <= difficulty then
        say "✓ Victory!"
        return true
    else
        say "✗ Defeat!"
        return false
    end
end
```

### Skill Check Template
```Quill
function skill_check(skill_name, skill_value)
    say "Rolling " + skill_name + "..."
    set roll to randint(1, 100)
    say "Roll: " + str(roll) + "/" + str(skill_value)
    
    return roll <= skill_value
end
```

### Loot Drop Template
```Quill
function loot_drop()
    set roll to randint(1, 100)
    
    if roll >= 95 then
        return "legendary"
    else
        if roll >= 75 then
            return "rare"
        else
            if roll >= 40 then
                return "common"
            else
                return "nothing"
            end
        end
    end
end
```

---

**Version:** Quill v1.1+  
**Functions Used:** `randint()`, `random()`

Now you can add exciting randomized missions to your games! Every playthrough will be different! 🎲
