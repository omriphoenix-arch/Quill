# Quick Reference: wait() Function

## Basic Usage
```Quill
wait(1)       # Wait 1 second
wait(2.5)     # Wait 2.5 seconds
wait(0.5)     # Wait half a second
```

## Examples

### Simple Pause
```Quill
say "Loading..."
wait(2)
say "Done!"
```

### Dramatic Dialogue
```Quill
say "The door opens slowly..."
wait(2)
say "A mysterious figure appears."
```

### Countdown
```Quill
set count to 3
while count > 0 do
    say count
    wait(1)
    set count to count - 1
end
say "Go!"
```

### Variable Timing
```Quill
set delay to 1.5

say "First message"
wait(delay)
say "Second message"
wait(delay)
say "Third message"
```

## When to Use

✅ **Good Uses:**
- Creating suspense
- Pacing dialogue
- Countdown timers
- Dramatic reveals
- Giving players time to read

❌ **Avoid:**
- Very long waits (over 5 seconds)
- Too many consecutive waits
- Waits before player choices
- During repetitive loops

## Pro Tips

1. **Keep it short**: 1-2 seconds is usually enough
2. **Match the mood**: Longer waits for dramatic moments, shorter for action
3. **Test it**: What feels right to you might be too slow for others
4. **Let players skip**: Consider adding a "fast mode" option

## Example: Your Asson Game

```Quill
say " Welcome to Asson! "
wait(1.5)

say " The year is A.B.D. 2345 "
wait(1)

say " The Republic is in turmoil... "
wait(2)

say " Choose your role "
choice "Soldier" or "General" or "Senator"

wait(1)
say " Your journey begins now... "
```

See `docs/WAIT_FUNCTION.md` for complete documentation!
