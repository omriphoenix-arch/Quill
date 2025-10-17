# VS Code Tasks Configuration for Quill

## Issue: Ctrl+Shift+B Running Python Files as Quill

### Problem
When pressing **Ctrl+Shift+B** in VS Code, the build task was running **all files** through `quill.bat`, including Python files like the installer. This caused errors like:

```
✗ SyntaxError at line 1, column 3:
  Unterminated string starting at column 3

     1 | """
           ✗ ^
```

This happened because:
- `quill.bat` interprets files as Quill code
- Python files (`.py`) have different syntax
- The installer (`installer/setup_gui.py`) is Python, not Quill

### Solution

Update `.vscode/tasks.json` to automatically detect file types:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Quill Program",
      "type": "shell",
      "command": "${workspaceFolder}/quill.bat",
      "args": ["${file}"],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "presentation": {
        "reveal": "always",
        "panel": "new"
      },
      "problemMatcher": [],
      "windows": {
        "command": "powershell",
        "args": [
          "-Command",
          "if ('${fileExtname}' -eq '.quill') { & '${workspaceFolder}/quill.bat' '${file}' } elseif ('${fileExtname}' -eq '.py') { python '${file}' } else { Write-Host 'Unsupported file type: ${fileExtname}' }"
        ]
      }
    },
    {
      "label": "Run Python Script",
      "type": "shell",
      "command": "python",
      "args": ["${file}"],
      "group": "build",
      "presentation": {
        "reveal": "always",
        "panel": "new"
      },
      "problemMatcher": []
    },
    {
      "label": "Run Quill with Legacy Mode",
      "type": "shell",
      "command": "${workspaceFolder}/quill.bat",
      "args": ["--legacy", "${file}"],
      "group": "build",
      "presentation": {
        "reveal": "always",
        "panel": "new"
      },
      "problemMatcher": []
    }
  ]
}
```

### How It Works

The smart detection logic:

```powershell
if ('${fileExtname}' -eq '.quill') {
    # Run Quill files with Quill interpreter
    & '${workspaceFolder}/quill.bat' '${file}'
} elseif ('${fileExtname}' -eq '.py') {
    # Run Python files with Python
    python '${file}'
} else {
    # Unknown file type
    Write-Host 'Unsupported file type: ${fileExtname}'
}
```

### Available Tasks

After updating `tasks.json`, you'll have these tasks:

#### 1. **Run Quill Program** (Default - Ctrl+Shift+B)
- Auto-detects file type
- `.quill` → Runs with Quill interpreter
- `.py` → Runs with Python
- Smart and convenient!

#### 2. **Run Python Script**
- Forces Python execution
- Use for testing Python scripts
- Access via: Terminal → Run Task → Run Python Script

#### 3. **Run Quill with Legacy Mode**
- Runs Quill with `--legacy` flag
- Auto-imports game and io modules
- For backward compatibility with old scripts

### Usage Examples

#### Running a Quill Program
1. Open any `.quill` file (e.g., `examples/demo_inventory.quill`)
2. Press **Ctrl+Shift+B**
3. It automatically runs with `quill.bat` ✅

#### Running the Installer
1. Open `installer/setup_gui.py`
2. Press **Ctrl+Shift+B**
3. It automatically runs with `python` ✅

#### Running Python Tools
1. Open any `.py` file (e.g., `core/quill.py`, `tools/migrate_paths.py`)
2. Press **Ctrl+Shift+B**
3. It automatically runs with `python` ✅

### Manual Task Selection

You can also manually select a task:

1. Press **Ctrl+Shift+P**
2. Type "Tasks: Run Task"
3. Choose from:
   - Run Quill Program
   - Run Python Script
   - Run Quill with Legacy Mode

### Setup Instructions

If you're setting up a fresh workspace:

1. Copy the `tasks.json` content above
2. Save it to `.vscode/tasks.json` in your project root
3. Reload VS Code or restart
4. Done! Ctrl+Shift+B now works intelligently

### Linux/macOS Version

For non-Windows systems, update the task to use bash:

```json
"linux": {
  "command": "bash",
  "args": [
    "-c",
    "if [ '${fileExtname}' = '.quill' ]; then '${workspaceFolder}/quill' '${file}'; elif [ '${fileExtname}' = '.py' ]; then python3 '${file}'; else echo 'Unsupported file type: ${fileExtname}'; fi"
  ]
}
```

### Benefits

✅ **Smart Detection**: Automatically chooses the right interpreter  
✅ **No More Errors**: Python files run with Python, not Quill  
✅ **Convenient**: Single keyboard shortcut (Ctrl+Shift+B) for everything  
✅ **Multiple Options**: Can still manually choose tasks  
✅ **Backward Compatible**: Legacy mode available for old scripts  

### Troubleshooting

**Problem**: Still getting syntax errors on Python files  
**Solution**: Make sure you saved the updated `tasks.json` and reloaded VS Code

**Problem**: Task not found  
**Solution**: Create `.vscode/tasks.json` if it doesn't exist

**Problem**: Wrong interpreter used  
**Solution**: Manually select "Run Python Script" from the task list

---

**Updated**: v1.0.2 - October 17, 2025  
**Issue**: Fixed VS Code build task to support multiple file types
