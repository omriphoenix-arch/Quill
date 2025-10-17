# Quill Module System Architecture

## Overview
Quill uses a modular architecture where features are organized into importable modules. This keeps the core language lightweight while providing optional functionality.

## Module Structure

### Core Module (Always Loaded)
- Variables, types, operators
- Functions, loops, conditionals
- Basic I/O: `say`, `print`, `ask`
- Basic builtins: `len`, `str`, `int`, `type`, `range`, `abs`

### Standard Library Modules

#### `stdlib` (Always Available, No Import Required)
Math, string, list, and type utilities:
- Math: `clamp`, `min`, `max`, `sum`, `average`, `round`, `floor`, `ceil`, `sqrt`, `pow`
- Random: `random_choice`, `random_int`, `random_float`
- String: `trim`, `lower`, `upper`, `split`, `join`, `replace`, `contains`
- List: `reverse`, `sort`
- Type checking: `is_number`, `is_string`, `is_list`, `is_empty`

#### `io` Module
File I/O operations (import required):
```quill
import io

io.read_text("file.txt")
io.write_text("output.txt", "Hello!")
io.read_lines("data.csv")
io.write_lines("output.txt", ["line1", "line2"])
io.append_text("log.txt", "New entry")
```

#### `game` Module
Game development utilities (import required):
```quill
import game

game.choice("Attack" or "Defend" or "Run")
game.add_item("sword")
game.save_game("slot1")
game.wait(1.5)
goto town_entrance
label town_entrance
```

Submodules:
- `game.inventory`: Item management
- `game.saveload`: Save/load system
- `game.flow`: Choice, goto/label, wait

### Import Syntax

#### Basic Import
```quill
import game          # Load entire game module
import io            # Load entire io module
```

#### Namespace Access
```quill
import game
game.add_item("sword")        # Namespaced
game.inventory.show()          # Submodule
```

#### Direct Import (Import into global scope)
```quill
from game import choice, add_item, save_game
choice("Yes" or "No")          # Direct access
```

#### Wildcard Import (Not recommended, but supported)
```quill
from game import *
add_item("sword")              # All game functions available
```

## Module Registry

Modules are registered in `core/modules/registry.py`:

```python
MODULES = {
    'io': {
        'path': 'core/modules/io_module.py',
        'functions': ['read_text', 'write_text', 'append_text', 'read_lines', 'write_lines'],
        'description': 'File I/O operations'
    },
    'game': {
        'path': 'core/modules/game_module.py',
        'functions': ['choice', 'goto', 'label', 'wait', 'add_item', ...],
        'submodules': ['inventory', 'saveload', 'flow'],
        'description': 'Game development utilities'
    }
}
```

## Lazy Loading

Modules are loaded only when imported:
1. Parse encounters `import game`
2. Interpreter checks if `game` already loaded
3. If not, load from registry and cache
4. Add functions to appropriate namespace

## Backward Compatibility

### Legacy Mode (Auto-import)
For existing scripts, run with `--legacy` flag:
```bash
quill --legacy old_script.quill
# Automatically imports: game, io
```

### Migration Tool
```bash
python scripts/add_imports.py examples/*.quill
# Scans for game/io function usage, adds appropriate imports
```

## Future Modules

### `web` Module (Planned)
HTTP requests, JSON parsing:
```quill
import web
set response = web.get("https://api.example.com/data")
set data = web.json_parse(response)
```

### `math` Module (Extended math operations)
```quill
import math
set result = math.sin(1.5)
set matrix = math.matrix([[1, 2], [3, 4]])
```

### `gui` Module (GUI features)
```quill
import gui
gui.window("My App", width=800, height=600)
gui.button("Click Me", onclick="handle_click")
```

## Implementation Files

- `core/modules/__init__.py` - Module loader
- `core/modules/registry.py` - Module registry
- `core/modules/io_module.py` - I/O module
- `core/modules/game_module.py` - Game module
- `core/modules/stdlib_module.py` - Stdlib (always loaded)
- `core/parser.py` - Import statement parsing
- `core/interpreter.py` - Module loading and namespace management
