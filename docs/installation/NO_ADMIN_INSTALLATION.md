# Installing Without Admin Privileges

## The Problem

You want custom icons for `.quill` files, but you don't have admin rights. Meanwhile, Python and C++ files already have icons. Why?

## The Answer

**Python/C++ icons work because they were installed BY an administrator**, either:
- When the computer was set up
- By your IT department
- By whoever first installed those programs

**You're seeing existing file associations that were set up with admin rights.**

## The Solution: User-Level Installation

Good news! You CAN have custom icons without admin privileges by installing to **your user account** instead of system-wide.

### Two Installation Options

#### Option 1: Admin Installation (System-Wide)
```
File: INSTALL_Quill.bat
Installs to: C:\Program Files\Quill\
Requires: Administrator privileges
Affects: All users on the computer
```

#### Option 2: User Installation (No Admin Required!) ✅
```
File: INSTALL_Quill_USER.bat
Installs to: C:\Users\YourName\AppData\Local\Quill\
Requires: NO admin privileges
Affects: Only your user account
```

## How to Install (No Admin)

### Step 1: Run the User Installer

**Double-click:** `INSTALL_Quill_USER.bat`

That's it! No admin prompt will appear.

### Step 2: Verify Installation

```powershell
# Check installation
ls $env:LOCALAPPDATA\Quill

# Test Quill
Quill test_icon.quill
```

### Step 3: Check the Icon

1. Open File Explorer
2. Navigate to your `.quill` files
3. You should see the custom icon!

If not, run:
```powershell
ie4uinit.exe -show
```

## What's the Difference?

### System-Wide (Admin Required)
```
Location: C:\Program Files\Quill\
Registry: HKEY_CLASSES_ROOT (system)
PATH: System PATH variable
Benefits:
  ✅ Available to all users
  ✅ "Official" installation location
  ✅ Survives user account changes
Drawbacks:
  ❌ Requires admin privileges
  ❌ Might be blocked by IT
```

### User-Level (No Admin) ✅
```
Location: C:\Users\YourName\AppData\Local\Quill\
Registry: HKEY_CURRENT_USER\Software\Classes
PATH: User PATH variable
Benefits:
  ✅ No admin required!
  ✅ You have full control
  ✅ Can't break system settings
  ✅ Easy to uninstall
Drawbacks:
  ⚠️ Only works for your account
  ⚠️ Other users won't see it
```

## Technical Explanation

### Why Python Has Icons (Without Admin Prompts)

When you see Python files with icons, one of these happened:

1. **Python was installed with admin** - Whoever installed Python had admin rights and set up system-wide file associations

2. **Python was installed per-user** - Python's installer offers a "Install for current user only" option that does exactly what we're doing!

3. **Pre-installed** - Some computers come with Python pre-installed with all associations set up

### Registry Keys

**System-wide (requires admin):**
```
HKEY_CLASSES_ROOT\.py
HKEY_CLASSES_ROOT\Python.File
```

**User-level (no admin needed):**
```
HKEY_CURRENT_USER\Software\Classes\.quill
HKEY_CURRENT_USER\Software\Classes\Quill.File
```

Both work the same way! User-level keys override system ones for your account.

## Comparison Table

| Feature | Admin Install | User Install |
|---------|--------------|--------------|
| **Admin Required** | ❌ Yes | ✅ No |
| **Custom Icon** | ✅ Yes | ✅ Yes |
| **Double-click .quill** | ✅ Yes | ✅ Yes |
| **Start Menu** | ✅ Yes | ✅ Yes |
| **PATH Access** | ✅ Yes | ✅ Yes |
| **All Users** | ✅ Yes | ❌ No |
| **Easy to Try** | ❌ No | ✅ Yes |

## FAQ

### Q: Will the user install work as well as admin?
**A:** Yes! For your user account, it works identically. The only difference is other users won't see it.

### Q: Can I upgrade from user to admin later?
**A:** Yes! Just:
1. Run `uninstall_user.ps1`
2. Get admin rights
3. Run `INSTALL_Quill.bat` (admin version)

### Q: Why does Python not ask for admin on my computer?
**A:** Because it was already installed with admin privileges before. You're using existing file associations.

### Q: Can I have both versions installed?
**A:** Not recommended. Choose one:
- User install if you don't have admin
- Admin install if you do have admin

### Q: Will this break anything?
**A:** No! User-level installations are completely safe and can't affect system settings.

### Q: What if I share this computer?
**A:** User install = only you see it. Admin install = everyone sees it.

## Installation Locations Compared

### Admin Installation
```
C:\Program Files\Quill\
├── Quill.py
├── lexer.py
├── parser.py
├── interpreter.py
├── Quill_icon.ico
├── examples\
└── docs\
```

### User Installation
```
C:\Users\YourName\AppData\Local\Quill\
├── Quill.py
├── lexer.py
├── parser.py
├── interpreter.py
├── Quill_icon.ico
├── examples\
└── docs\
```

**Same files, different location!**

## Commands

### Install (No Admin)
```batch
INSTALL_Quill_USER.bat
```

### Uninstall (No Admin)
```powershell
.\uninstall_user.ps1
```

### Check Installation
```powershell
# Where is it installed?
echo $env:LOCALAPPDATA\Quill

# Is it in PATH?
$env:PATH -split ';' | Select-String "Quill"

# Test it
Quill --version
```

## Real-World Example

### How Python Does It

Python's installer has two options:

1. **"Install for all users"** 
   - Requires admin
   - Goes to `C:\Program Files\`
   - System-wide file associations

2. **"Install for current user only"** ← **This is what we're doing!**
   - No admin needed
   - Goes to `C:\Users\YourName\AppData\Local\`
   - User-level file associations

Our user installer works exactly like Python's "current user only" option!

## Bottom Line

✅ **Use `INSTALL_Quill_USER.bat`** - No admin needed!
- Custom icons work perfectly
- File associations work perfectly
- Everything works the same
- The only difference: just for your account

You don't need admin privileges to have professional-looking `.quill` files with custom icons! 🎉

---

**Recommended:** `INSTALL_Quill_USER.bat` (no admin required)

Just double-click and you're done! 📘✨
