# CRITICAL LICENSE FIX - October 17, 2025

## ⚠️ Issue Discovered

The GUI installer (`installer/setup_gui.py`) was displaying an **incorrect MIT License** as a fallback when the LICENSE file couldn't be found. This was a **serious error** because:

### The Problem

The fallback license text stated:
```
MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

**This is COMPLETELY WRONG!** Quill does NOT use the MIT License.

### Actual Quill License

Quill Programming Language has a **proprietary license**:

**Copyright © 2025 Omri Morgan (omriphoenix-arch)**
**All Rights Reserved**

#### PERMITTED:
- ✅ Personal use for learning and educational purposes
- ✅ Running and creating programs using Quill
- ✅ Sharing Quill programs (.quill files)
- ✅ Contributing improvements via pull requests

#### NOT PERMITTED (Without Written Permission):
- ❌ Claiming ownership of Quill language
- ❌ Creating derivative programming languages
- ❌ Redistributing modified versions
- ❌ Commercial use without permission
- ❌ **Sublicensing** (The MIT text incorrectly allowed this!)
- ❌ Removing or altering copyright notices

### Why This Matters

1. **Legal Protection**: The correct license protects your intellectual property
2. **No Sublicensing**: MIT allowed sublicensing, but Quill explicitly forbids it
3. **Attribution Required**: Quill requires attribution; MIT doesn't enforce it as strongly
4. **Commercial Control**: You maintain control over commercial use
5. **Brand Protection**: The name "Quill" and branding are protected

## ✅ Fix Applied

### Changes Made:

1. **GUI Installer** (`installer/setup_gui.py`):
   - Removed incorrect MIT License fallback text
   - Replaced with actual Quill Programming Language License
   - Clearly states "All Rights Reserved"
   - Explicitly lists what IS and IS NOT permitted
   - No sublicensing allowed

2. **License Display**:
   - Installer now correctly reads from LICENSE file first
   - If LICENSE file missing, displays correct Quill license text
   - Users must accept the ACTUAL license, not a fake one

### Code Changes:

**Before (WRONG):**
```python
license_text.insert(tk.END, """MIT License

Copyright (c) 2025 Quill Language

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software... to deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, 
distribute, sublicense, and/or sell copies of the Software...
""")
```

**After (CORRECT):**
```python
license_text.insert(tk.END, """Quill Programming Language License

Copyright (c) 2025 Omri Morgan (omriphoenix-arch)
All Rights Reserved.

THE QUILL PROGRAMMING LANGUAGE, INCLUDING ITS NAME, LOGO, INTERPRETER, 
AND ASSOCIATED DOCUMENTATION, IS THE INTELLECTUAL PROPERTY OF OMRI MORGAN.

PERMITTED USE:
- Personal use for learning and educational purposes
- Running and creating programs using the Quill language
...

NOT PERMITTED WITHOUT WRITTEN PERMISSION:
- Claiming ownership or creation of the Quill language
- Creating derivative programming languages based on Quill's design
- Redistributing modified versions under a different name
- Commercial use of the Quill interpreter or language without permission
...
""")
```

## 🔒 Legal Implications

### What Was Wrong:
- Installer implied users could sublicense Quill (they can't!)
- Implied unrestricted redistribution (not allowed!)
- Didn't protect your trademark and branding
- Could have created legal confusion

### Now Corrected:
- ✅ License clearly states "All Rights Reserved"
- ✅ Explicitly forbids sublicensing
- ✅ Protects intellectual property
- ✅ Requires attribution to Omri Morgan
- ✅ Maintains commercial control
- ✅ Protects "Quill" brand name

## 📋 Verification

To verify the fix is applied:

1. **Check Installer Code:**
   ```bash
   grep -A 5 "Quill Programming Language License" installer/setup_gui.py
   ```
   Should show correct license text

2. **Run Installer:**
   ```bash
   python installer/setup_gui.py
   ```
   Navigate to License page - should show YOUR license, not MIT

3. **Check LICENSE File:**
   ```bash
   cat LICENSE
   ```
   Should show proprietary Quill license (as attached)

## 🚨 Important Notes

1. **No MIT License**: Quill has NEVER been MIT licensed
2. **All Rights Reserved**: This is a proprietary license with specific permissions
3. **Attribution Required**: Must credit Omri Morgan as creator
4. **No Forks**: Creating derivative languages is not permitted
5. **Commercial Control**: Commercial use requires written permission

## 📝 Additional Fixes in Same Commit

While fixing the license, also corrected:

- **Path Issues**: Updated installer to use new folder structure
  - `icons/` → `resources/icons/`
  - Root docs → `documentation/`
  - Added proper error handling

- **File Copying**: Fixed Win32 path errors
  - Now handles reorganized structure correctly
  - Creates parent directories as needed
  - Better error messages

## ✅ Status

- **Fixed**: October 17, 2025
- **Commit**: deefa4d
- **Pushed**: Yes, to main branch
- **Severity**: CRITICAL (Legal/License issue)
- **Impact**: All future installations will show correct license

## 📧 Contact

For commercial licensing inquiries:
**Quill.Contact94@gmail.com**

---

**IMPORTANT**: Always ensure license text in installers matches your actual LICENSE file. Never use placeholder licenses like MIT when you have a proprietary license!

**Copyright © 2025 Omri Morgan - All Rights Reserved**
