# Installation Instructions

## Option 1: Use the Batch File (Windows - Easiest)

### Quick Setup:
The `Quill.bat` file is already created! Just add it to your PATH:

1. **Copy the full path to this folder:**
   ```
   C:\Users\Omri.Morgan02\Downloads\possible
   ```

2. **Add to PATH:**
   - Press `Windows + X` and select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "User variables", find "Path" and click "Edit"
   - Click "New" and paste the folder path
   - Click OK on all dialogs

3. **Test it:**
   Open a NEW command prompt or PowerShell and type:
   ```bash
   Quill tutorial.quill
   ```

### Alternative: Use from current folder
If you don't want to modify PATH, you can use `.\Quill.bat` from the folder:
```bash
cd C:\Users\Omri.Morgan02\Downloads\possible
.\Quill tutorial.quill
```

---

## Option 2: Create a Simple Launcher (Windows)

Create a shortcut or alias in PowerShell:

### PowerShell Alias (Temporary):
```powershell
function Quill { python "C:\Users\Omri.Morgan02\Downloads\possible\Quill.py" $args }
```

### PowerShell Profile (Permanent):
1. Open PowerShell and type:
   ```powershell
   notepad $PROFILE
   ```

2. Add this line:
   ```powershell
   function Quill { python "C:\Users\Omri.Morgan02\Downloads\possible\Quill.py" $args }
   ```

3. Save and restart PowerShell

4. Now you can use:
   ```bash
   Quill myfile.quill
   ```

---

## Option 3: Unix/Linux/Mac

If you ever move to Unix/Linux/Mac:

1. Make the script executable:
   ```bash
   chmod +x Quill
   ```

2. Add to PATH by editing `~/.bashrc` or `~/.zshrc`:
   ```bash
   export PATH="$PATH:/path/to/possible"
   ```

3. Or create a symlink:
   ```bash
   sudo ln -s /path/to/possible/Quill /usr/local/bin/Quill
   ```

---

## Recommended: Option 1 (Batch File + PATH)

This is the easiest and most "real programming language" experience!

After setup, you can just type:
```bash
Quill myprogram.quill
```

from any folder! 🚀
