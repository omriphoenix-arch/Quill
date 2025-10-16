# Wait Function - Timing and Pacing

## Overview
The `wait()` function allows you to pause execution for a specified number of seconds. This is perfect for creating dramatic pauses, suspense, and natural pacing in your stories.

## Syntax
```Quill
wait(seconds)
```

## Parameters
- **seconds** (number): The number of seconds to pause
  - Can be an integer: `wait(1)`, `wait(3)`
  - Can be a decimal: `wait(0.5)`, `wait(2.5)`
  - Can be a variable: `wait(delay_time)`

## Return Value
- Returns `true` if the wait was successful
- Returns `false` if the input was invalid (negative or non-numeric)

## Examples

### Basic Usage
```Quill
say "The door opens..."
wait(2)
say "A figure emerges from the shadows."
```

### Variable Delays
```Quill
set pause_length to 1.5

say "Tick..."
wait(pause_length)
say "Tock..."
wait(pause_length)
say "Boom!"
```

### Countdown Timer
```Quill
say "Self-destruct sequence initiated!"
say ""

set countdown to 5
while countdown > 0 do
    say countdown
    wait(1)
    set countdown to countdown - 1
end

say "💥 BOOM! 💥"
```

### Creating Suspense
```Quill
say "You hear footsteps approaching..."
wait(2)

say "They're getting closer..."
wait(1.5)

say "The footsteps stop right outside your door."
wait(2)

say "Silence."
wait(3)

say "CRASH! The door bursts open!"
```

### Dramatic Dialogue
```Quill
say "Mysterious Stranger: 'I know who you really are.'"
wait(2)

say "You: 'What do you mean?'"
wait(1.5)

say "Mysterious Stranger: 'You're not from this world...'"
wait(2)

say "Mysterious Stranger: 'Are you?'"
```

### Pacing a Story
```Quill
say "================================================"
say "            CHAPTER 1: THE BEGINNING"
say "================================================"
wait(2)

say ""
say "Long ago, in a distant galaxy..."
wait(2)

say "There was a hero who would change everything."
wait(2)

say "That hero... was you."
wait(3)

say ""
say "But first, you had to wake up."
```

## Best Practices

### 1. Don't Overuse
```Quill
# ❌ Too many waits can be annoying
say "Hello"
wait(2)
say "How"
wait(2)
say "Are"
wait(2)
say "You?"

# ✓ Use waits strategically
say "Hello. How are you?"
wait(1)
say "I have something important to tell you."
```

### 2. Match Wait Time to Content
```Quill
# Short pauses (0.5-1 second) for quick transitions
say "Ready?"
wait(0.5)
say "Go!"

# Medium pauses (1-2 seconds) for dialogue
say "Guard: 'Halt! Who goes there?'"
wait(1.5)
say "You: 'A friend.'"

# Long pauses (2-3+ seconds) for dramatic moments
say "You open the ancient door..."
wait(3)
say "Inside is something you never expected."
```

### 3. Combine with Choices
```Quill
say "The timer is counting down!"
say "10 seconds until detonation!"
wait(2)

say "You see two wires: red and blue."
wait(1)

choice "Cut the red wire" or "Cut the blue wire" or "Run away"

if answer is "Run away" then
    say "You turn and run!"
    wait(1)
    say "Behind you, you hear..."
    wait(2)
    say "💥 BOOM! 💥"
end
```

### 4. Create Rhythm
```Quill
# Use consistent timing for rhythm
say "The clock ticks..."
wait(1)
say "Tick."
wait(1)
say "Tock."
wait(1)
say "Tick."
wait(1)
say "The mechanism stops."
```

## Common Use Cases

### Loading Screens
```Quill
say "Loading world..."
wait(1)
say "Creating characters..."
wait(1)
say "Building story..."
wait(1)
say "Ready!"
```

### Cutscenes
```Quill
say "=== CUTSCENE ==="
wait(1)

say "The kingdom is under attack."
wait(2)

say "Only you can save it."
wait(2)

say "=== END CUTSCENE ==="
```

### Suspenseful Moments
```Quill
say "You slowly reach for the doorknob..."
wait(2)

say "Your hand trembles..."
wait(1.5)

say "You turn it..."
wait(2)

say "The door creaks open."
```

### Timed Events
```Quill
say "Quick! You have 5 seconds to hide!"

set time to 5
while time > 0 do
    wait(1)
    set time to time - 1
end

say "Too late! They found you!"
```

## Tips

1. **Test Your Timing**: What feels right to you might be too fast or slow for others. Test with different people.

2. **Use Shorter Waits**: 1-2 seconds is usually enough. Longer waits can feel like the program froze.

3. **Combine with User Input**: After a long pause, give players something to do:
   ```Quill
   say "You wait for what feels like hours..."
   wait(3)
   ask "What do you do?"
   ```

4. **Variable Speed**: Let players control pacing:
   ```Quill
   set reading_speed to 1.5
   
   say "Line one"
   wait(reading_speed)
   say "Line two"
   wait(reading_speed)
   ```

5. **Skip Option**: For repeated plays, consider letting players skip waits:
   ```Quill
   ask "Enable dramatic pauses? (yes/no)"
   
   if answer is "yes" then
       set use_waits to true
   else
       set use_waits to false
   end
   
   say "The story begins..."
   if use_waits then
       wait(2)
   end
   ```

## Technical Notes

- The `wait()` function uses Python's `time.sleep()` internally
- Waits are blocking - the program pauses completely
- Minimum practical wait is about 0.1 seconds
- Very long waits (60+ seconds) should be avoided
- Wait times are approximate, not exact

## Related Functions

- `say()` - Display text
- `ask()` - Get user input
- `choice()` - Present options

## Example: Complete Dramatic Scene

```Quill
say "================================================"
say "          THE FINAL CONFRONTATION"
say "================================================"
wait(2)

say ""
say "You stand before the ancient temple."
wait(2)

say "The villain awaits inside."
wait(2)

say ""
ask "Are you ready to face your destiny? (yes/no)"

if answer is "yes" then
    say ""
    say "You take a deep breath..."
    wait(1.5)
    
    say "And step inside."
    wait(2)
    
    say ""
    say "The doors slam shut behind you."
    wait(1.5)
    
    say ""
    say "A voice echoes through the chamber..."
    wait(2)
    
    say ""
    say "Villain: 'I've been waiting for you...'"
    wait(2)
    
    say ""
    say "TO BE CONTINUED..."
else
    say ""
    say "You turn and walk away."
    wait(1.5)
    say "Some battles are not meant to be fought today."
end
```

---

**Added in Quill v1.1**

The `wait()` function gives you precise control over timing and pacing, making your stories more immersive and dramatic. Use it wisely to create memorable moments!
