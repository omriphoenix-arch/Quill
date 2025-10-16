# Changelog

All notable changes to Quill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

---

## [1.0.1-beta] - 2025-10-16

### 🐛 Bug Fixes
- Fixed crash when input ends unexpectedly (EOF error) in `ask` commands and choice menus
- Programs now exit gracefully with a helpful message instead of crashing
- Fixed Unicode encoding error on Windows (added UTF-8 stdout wrapper)
- Fixed example file `natural_syntax_demo.quill` using disabled keyword
- Fixed `games/test.quill` using incorrect capitalization (`Wait` → `wait`)

### 📝 Documentation
- Added comprehensive testing results documentation
- Created test suite for automated testing
- Updated CHANGELOG with all bug fixes

### 🔧 Improvements
- Better error handling for interactive programs
- More user-friendly exit messages
- Windows Unicode support now works correctly

### ✅ Testing
- 15 files tested with 100% pass rate
- All core features verified working
- Save/load system tested and working
- Tutorial verified complete and functional

### 🎯 Community Feedback
- (Add changes based on Reddit/GitHub feedback here)

---

## [1.0.0] - 2025-10-15

### 🎉 Initial Public Release

The first stable release of Quill - a beginner-friendly programming language!

### Added

#### Core Language Features
- **Variables and Data Types**
  - Numbers (integers and floats)
  - Strings with escape sequences
  - Booleans (true/false)
  - Lists and indexing
  - Dynamic typing

- **Operators**
  - Arithmetic: `+`, `-`, `*`, `/`, `%`, `**`
  - Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`
  - Logical: `and`, `or`, `not`
  - Assignment: `=`, `to`

- **Control Flow**
  - `if`/`then`/`else`/`elif` conditionals
  - `while` loops with `do`/`end`
  - `for` loops with `in` and `range()`
  - `break` and `continue` statements
  - `goto` and `label` for story branching

- **Functions**
  - Function definitions with `function`, `func`, or `def`
  - Parameters and return values
  - Nested function calls
  - Recursion support

- **Built-in Functions**
  - Type conversion: `str()`, `int()`, `float()`
  - String/List operations: `len()`, `type()`
  - Math: `abs()`, `min()`, `max()`, `sum()`, `round()`
  - Random: `random()`, `randint()`
  - Iteration: `range()`

- **Game-Focused Commands**
  - `say` and `print` - Display output
  - `ask` and `input` - Get user input with `into`
  - `choice` - Multiple choice with `or` separator
  - `wait()` - Pause execution
  - Automatic `answer` variable for choices

- **Comments**
  - Single-line comments with `#`

#### Development Tools

- **Command-Line Interpreter**
  - Run `.quill` files from terminal
  - Interactive REPL mode (coming soon)
  - Clear error messages with line numbers

- **VS Code Extension** (v1.2.1)
  - Syntax highlighting for `.quill` files
  - Custom file icons (4 styles: Gradient, Minimalist, Neon, Retro)
  - 3 color themes:
    - Quill Dark (purple/pink)
    - Quill Neon (cyberpunk cyan/magenta)
    - Quill Light (daytime-friendly)
  - Auto-indentation and bracket matching
  - Code folding
  - Language configuration

- **Installation Scripts**
  - Windows: PowerShell installer
  - Cross-platform Python setup
  - VS Code extension auto-installer
  - Icon registry for Windows Explorer

#### Documentation

- **Getting Started Guide** - Step-by-step first program
- **Keywords Reference** - Complete keyword documentation with examples
- **Language Reference** - Full language specification
- **GUI Commands Guide** - GUI features documentation
- **Color Themes Guide** - VS Code theme setup
- **Installation Guide** - Multiple installation methods

#### Examples

- `example_simple.quill` - Hello World and basics
- `example_guessing_game.quill` - Number guessing game
- `example_calculator.quill` - Simple calculator
- `example_adventure.quill` - Text adventure game
- `example_mystery.quill` - Mystery solving game
- `example_todo_list.quill` - Todo list manager
- `demo_wait.quill` - Timing and pauses
- `demo_randomizer.quill` - Random number generation
- `demo_saveload.quill` - Save/load functionality
- `tutorial.quill` - Interactive language tutorial

#### GUI Features (Experimental)

- Window creation with `window()`
- Buttons with `button()` and callbacks
- Text labels with `label()`
- Text input fields with `textbox()`
- Event loop with `show()`
- Custom colors support

### Technical Details

- **Language**: Python 3.8+ required
- **Dependencies**: 
  - Pillow (for icon generation)
  - tkinter (for GUI, usually pre-installed)
- **File Extension**: `.quill`
- **Encoding**: UTF-8
- **Line Endings**: Cross-platform support

### Known Limitations

- No classes or objects (yet)
- No file I/O operations (coming soon)
- No network/HTTP support (planned)
- GUI features are experimental
- Performance not optimized for large programs

### Platform Support

- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux (Ubuntu, Debian, Fedora)
- ✅ VS Code 1.60+

---

## Version History Format

### Types of Changes
- **Added** - New features
- **Changed** - Changes to existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Security vulnerability fixes

### Version Numbering
Quill follows [Semantic Versioning](https://semver.org/):
- **MAJOR** version (1.x.x) - Incompatible API changes
- **MINOR** version (x.1.x) - New backwards-compatible features
- **PATCH** version (x.x.1) - Backwards-compatible bug fixes

---

## [0.9.0] - 2025-10-01 (Beta)

### Added
- Initial beta release for testing
- Core language features implemented
- Basic error handling
- Simple examples

### Known Issues
- Syntax highlighting not working in VS Code
- Variable colors not displaying correctly
- Icons not applying to files
- Theme not loading properly

### Fixed in 1.0.0
- ✅ All syntax highlighting issues resolved
- ✅ Variable and keyword colors working
- ✅ File icons displaying in both Windows and VS Code
- ✅ Themes loading correctly with proper scopes

---

## How to Upgrade

### From 0.9.x to 1.0.0
1. Back up your `.quill` files
2. Uninstall old VS Code extension
3. Run the new installer
4. Install new VS Code extension
5. Select "Quill Dark" theme

No breaking changes to language syntax - all 0.9.x code is compatible!

---

## Reporting Issues

Found a bug? Please report it:
1. Check if it's already reported in [Issues](https://github.com/yourusername/Quill/issues)
2. If not, create a new issue with:
   - Quill version
   - Operating system
   - Steps to reproduce
   - Expected vs actual behavior
   - Sample code

---

## Future Roadmap

### v1.1.0 (Planned - Q4 2025)
- [ ] Interactive REPL mode
- [ ] File I/O operations (`read`, `write`)
- [ ] JSON parsing and generation
- [ ] More string methods
- [ ] Improved error messages

### v1.2.0 (Planned - Q1 2026)
- [ ] Package manager (import from URL)
- [ ] Standard library of common functions
- [ ] Dictionary/map data type
- [ ] List comprehensions
- [ ] Module system

### v2.0.0 (Future)
- [ ] Object-oriented programming
- [ ] Async/await support
- [ ] Web framework for making games/apps
- [ ] Compiled executables
- [ ] Native mobile support

---

**Stay tuned for updates!** Follow the project on GitHub for the latest news.
