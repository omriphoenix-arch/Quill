# Quill Project Structure

## 📁 Folder Organization

```
possible/
│
├── 📄 game.quill              # YOUR GAME - Your main project!
├── 📄 README.md               # Quick overview and usage
│
├── 🔧 Core Files (Don't touch these):
│   ├── Quill.py         # Main interpreter
│   ├── lexer.py              # Tokenizer
│   ├── parser.py             # Parser
│   ├── interpreter.py        # Executor
│   └── Quill.bat       # Windows launcher
│
├── 📚 docs/                   # Documentation
│   ├── GETTING_STARTED.md    # Beginner guide
│   ├── INSTALL.md            # Installation instructions
│   ├── LANGUAGE_REFERENCE.md # Complete language docs
│   └── COMMANDS.md           # Command reference
│
├── 🎮 examples/               # Example programs
│   ├── tutorial.quill        # Interactive tutorial
│   ├── example_simple.quill
│   ├── example_adventure.quill
│   ├── example_mystery.quill
│   ├── example_calculator.quill
│   ├── example_guessing_game.quill
│   ├── example_todo_list.quill
│   ├── example_full_language.quill
│   └── mygame.quill
│
└── 🔨 System folders (auto-generated):
    ├── .vscode/              # VS Code settings
    ├── .vscode-extension/    # Syntax highlighting
    └── __pycache__/          # Python cache

```

## 🎯 What Each File Does

### Your Files:
- **game.quill** - Your game about Asson! ⭐

### Core Quill Files (Don't Delete):
- **Quill.py** - The main program
- **lexer.py** - Breaks code into tokens
- **parser.py** - Understands grammar
- **interpreter.py** - Runs your code
- **Quill.bat** - Lets you run `.\Quill game.quill`

### Documentation:
- **README.md** - Quick start guide
- **docs/** - All detailed documentation

### Examples:
- **examples/** - Example programs to learn from

## 🚀 How to Use

### Run Your Game:
```bash
.\Quill game.quill
```

### Run Examples:
```bash
.\Quill examples\tutorial.quill
.\Quill examples\example_adventure.quill
```

### Create New Games:
Just create a new `.quill` file in the main folder!

## 🧹 Clean Workspace

Everything is now organized! You have:
- ✅ Your game in the main folder
- ✅ Core files for the language
- ✅ Examples in separate folder
- ✅ Documentation in separate folder
- ✅ No clutter or test files

Focus on `game.quill` - that's your project! 🎮
