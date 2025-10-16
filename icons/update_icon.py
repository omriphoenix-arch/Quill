"""
Icon Updater for Quill
Changes the active icon for .quill files
"""

import os
import sys
import shutil

def get_icon_choice():
    """Let user choose which icon to use"""
    
    icons = {
        '1': ('quill_icon.ico', 'Gradient Book (Default)'),
        '2': ('quill_icon_minimalist.ico', 'Minimalist Flat Design'),
        '3': ('quill_icon_neon.ico', 'Neon Cyberpunk'),
        '4': ('quill_icon_retro.ico', 'Retro Pixel Art'),
    }
    
    print("\n" + "=" * 60)
    print("  Quill Icon Selector")
    print("=" * 60 + "\n")
    
    print("Choose your icon style:\n")
    for key, (filename, desc) in icons.items():
        status = "✓ CURRENT" if filename == 'quill_icon.ico' else ""
        print(f"  [{key}] {desc} {status}")
        print(f"      {filename}")
        print()
    
    print("=" * 60)
    choice = input("\nEnter your choice (1-4) or 'q' to quit: ").strip()
    
    if choice.lower() == 'q':
        print("\nCancelled.")
        return None
    
    if choice not in icons:
        print("\n❌ Invalid choice. Please enter 1-4.")
        return get_icon_choice()
    
    return icons[choice]

def backup_current_icon():
    """Backup the current icon before replacing"""
    
    if os.path.exists('quill_icon.ico'):
        backup_name = 'quill_icon_backup.ico'
        
        # If backup already exists, add number
        counter = 1
        while os.path.exists(backup_name):
            backup_name = f'quill_icon_backup_{counter}.ico'
            counter += 1
        
        shutil.copy2('quill_icon.ico', backup_name)
        print(f"✓ Backed up current icon to: {backup_name}")
        return backup_name
    
    return None

def update_icon(icon_file):
    """Replace the main icon with the chosen one"""
    
    if not os.path.exists(icon_file):
        print(f"\n❌ Error: {icon_file} not found!")
        print("   Run create_alternate_icon.py to generate all icons.")
        return False
    
    # Backup current
    backup = backup_current_icon()
    
    # Copy chosen icon
    try:
        shutil.copy2(icon_file, 'quill_icon.ico')
        print(f"✓ Icon updated to: {icon_file}")
        return True
    except Exception as e:
        print(f"\n❌ Error copying icon: {e}")
        
        # Restore backup if failed
        if backup:
            shutil.copy2(backup, 'quill_icon.ico')
            print("✓ Restored backup icon")
        
        return False

def update_registry():
    """Update Windows registry to use new icon"""
    
    print("\n" + "=" * 60)
    print("  Applying Icon Changes")
    print("=" * 60 + "\n")
    
    print("To apply the icon change system-wide:")
    print("\n1. Run the installer again:")
    print("   cd ..")
    print("   install_Quill.bat")
    print("\n2. Or manually refresh Windows Explorer:")
    print("   - Press Ctrl+Shift+Esc (Task Manager)")
    print("   - Find 'Windows Explorer'")
    print("   - Right-click → Restart")
    print("\n3. Or simply restart your computer")

def main():
    """Main function"""
    
    # Check if in icons directory
    if not os.path.exists('quill_icon.ico'):
        print("\n❌ Error: Not in icons directory!")
        print("   cd icons")
        print("   python update_icon.py")
        return
    
    # Get user choice
    result = get_icon_choice()
    
    if result is None:
        return
    
    icon_file, description = result
    
    # Confirm
    print("\n" + "=" * 60)
    print(f"  Switching to: {description}")
    print("=" * 60 + "\n")
    
    confirm = input("Continue? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("\nCancelled.")
        return
    
    # Update icon
    if update_icon(icon_file):
        print("\n✓ Icon successfully updated!")
        update_registry()
        
        print("\n" + "=" * 60)
        print("✓ Done! Enjoy your new icon! 🎉")
        print("=" * 60)
    else:
        print("\n❌ Icon update failed.")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
