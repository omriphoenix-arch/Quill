# Quill Without VS Code - Quick Guide

## Yes, Quill Works Without VS Code! ✅

**You only need Python 3.8+ to run Quill programs.**

VS Code is completely optional and only provides syntax highlighting, themes, and icons.

## What You Can Do Without VS Code:

### ✅ Run All Programs
```bash
# Windows
python core\quill.py examples\example_simple.quill
quill.bat examples\example_simple.quill

# Unix/Linux/Mac
python3 core/quill.py examples/example_simple.quill
./quill examples/example_simple.quill
```

### ✅ Write Programs in Any Editor
- **Notepad** (built into Windows)
- **Notepad++** (free, popular)
- **Sublime Text** (lightweight, fast)
- **Atom** (GitHub's editor)
- **Vim / Emacs** (terminal editors)
- **nano** (simple terminal editor)
- **TextEdit** (Mac)
- **gedit** (Linux)
- **Any text editor you like!**

### ✅ All Language Features Work
- Variables, functions, loops
- Lists, math, strings
- Interactive input (`ask`)
- Games, stories, programs
- Everything in the language!

### ✅ Run Games and Examples
All example programs and games work perfectly:
```bash
python core\quill.py examples\example_guessing_game.quill
python core\quill.py examples\example_calculator.quill
python core\quill.py examples\example_adventure.quill
python core\quill.py games\game.quill
```

## What You Miss Without VS Code:

### 🟡 Editor Enhancements (Nice to Have)
- **Syntax highlighting** - Keywords colored differently
- **Themes** - Three custom color schemes
- **File icons** - Custom `.quill` file icons
- **Tasks** - Quick run with Ctrl+Shift+B
- **Debugging** - Step through code with F5
- **Auto-completion** - Suggest keywords as you type

**These are conveniences, not requirements!**

## Minimum Installation:

### Just Want to Run Quill?
1. Install Python 3.8+ from https://www.python.org/downloads/
2. Download/clone this repository
3. Run: `python core/quill.py your_program.quill`

**That's it!** No installers, no VS Code, no complex setup.

### Want Convenience Features?
Run the installer to get:
- `quill` command (instead of typing full path)
- File associations (double-click `.quill` files on Windows)
- PATH configuration

```bash
# Windows
powershell -ExecutionPolicy Bypass -File install.ps1

# Unix/Mac
chmod +x install.sh
./install.sh
```

The installer will detect if VS Code is installed and configure it automatically. If VS Code is not installed, the installer will skip that part and Quill will still work perfectly!

## Comparison:

| Feature | Without VS Code | With VS Code |
|---------|----------------|--------------|
| **Run programs** | ✅ Yes | ✅ Yes |
| **Write code** | ✅ Any editor | ✅ VS Code |
| **All language features** | ✅ Yes | ✅ Yes |
| **Interactive programs** | ✅ Yes | ✅ Yes |
| **Syntax highlighting** | ❌ Plain text | ✅ Colors |
| **Custom themes** | ❌ No | ✅ 3 themes |
| **File icons** | ❌ Default | ✅ Custom |
| **Quick run** | ❌ Type command | ✅ Ctrl+Shift+B |
| **Debugging** | ❌ Print statements | ✅ Debugger |

## Real-World Examples:

### Writing Code Without VS Code:
1. Open **Notepad** (Windows) or **TextEdit** (Mac)
2. Write your Quill program:
   ```quill
   say "Hello, World!"
   set name = ask "What's your name?"
   say "Nice to meet you, " + name + "!"
   ```
3. Save as `hello.quill`
4. Run: `python core\quill.py hello.quill`

### Writing Code With VS Code:
1. Open the workspace in VS Code
2. Create new file `hello.quill`
3. Start typing - keywords automatically colored!
4. Press Ctrl+Shift+B to run
5. Or press F5 to debug

Both methods work! VS Code just makes editing more convenient.

## Recommended Editors (Free):

### Windows:
1. **Notepad** (built-in, simple)
2. **Notepad++** (powerful, free) - https://notepad-plus-plus.org/
3. **VS Code** (best Quill support) - https://code.visualstudio.com/

### Mac:
1. **TextEdit** (built-in, simple)
2. **Sublime Text** (fast, free trial) - https://www.sublimetext.com/
3. **VS Code** (best Quill support) - https://code.visualstudio.com/

### Linux:
1. **nano** (terminal, simple) - already installed
2. **gedit** (GUI, simple) - usually pre-installed
3. **VS Code** (best Quill support) - https://code.visualstudio.com/

## FAQ:

**Q: Do I need VS Code to learn Quill?**
A: No! You only need Python and any text editor.

**Q: Will my programs work without VS Code?**
A: Yes! All Quill programs run the same way regardless of your editor.

**Q: Can I install VS Code later?**
A: Yes! Install it anytime. The extension will auto-configure when you open the workspace.

**Q: Does the installer require VS Code?**
A: No. The installer detects if VS Code is installed and configures it if found. Otherwise, it skips that step.

**Q: What if I prefer Vim/Emacs/Sublime?**
A: Perfect! Use whatever editor you're comfortable with. Quill works with all of them.

**Q: Can I use online editors like Replit?**
A: Yes! Upload the Quill files and run them with Python 3.8+.

## Summary:

✅ **Quill works perfectly without VS Code**
✅ **Only Python 3.8+ is required**
✅ **Use any text editor you like**
✅ **All language features work the same**
🟡 **VS Code adds syntax highlighting and convenience (optional)**

**Choose what works best for you!** 🚀
