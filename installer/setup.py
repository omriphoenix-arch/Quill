"""
Quill Language Installer
Professional installation wizard for Windows, Linux, and macOS
"""

import sys
import os
import shutil
import platform
import subprocess
from pathlib import Path

class QuillInstaller:
    def __init__(self):
        self.system = platform.system()
        self.quill_dir = Path(__file__).parent.absolute()
        self.is_admin = self.check_admin()
        
    def check_admin(self):
        """Check if running with admin/sudo privileges"""
        try:
            if self.system == 'Windows':
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            else:
                return os.geteuid() == 0
        except:
            return False
    
    def print_banner(self):
        """Print welcome banner"""
        print("=" * 60)
        print(" " * 15 + "QUILL LANGUAGE INSTALLER")
        print(" " * 10 + "Modern Scripting Language Installation")
        print("=" * 60)
        print()
    
    def install_windows(self):
        """Install Quill on Windows"""
        print("🪟 Installing Quill for Windows...")
        print()
        
        # 1. Create installation directory
        if self.is_admin:
            install_dir = Path("C:/Program Files/Quill")
        else:
            install_dir = Path.home() / "Quill"
        
        print(f"📁 Installation directory: {install_dir}")
        
        if install_dir.exists():
            response = input(f"⚠  Directory exists. Overwrite? (y/n): ")
            if response.lower() != 'y':
                print("Installation cancelled.")
                return False
            shutil.rmtree(install_dir)
        
        install_dir.mkdir(parents=True, exist_ok=True)
        
        # 2. Copy files
        print("📦 Copying files...")
        
        # Core directories (required)
        shutil.copytree(self.quill_dir / "core", install_dir / "core")
        shutil.copytree(self.quill_dir / "examples", install_dir / "examples")
        shutil.copytree(self.quill_dir / "docs", install_dir / "docs")
        
        # Optional directories (copy if they exist)
        if (self.quill_dir / "icons").exists():
            shutil.copytree(self.quill_dir / "icons", install_dir / "icons")
        if (self.quill_dir / "scripts").exists():
            shutil.copytree(self.quill_dir / "scripts", install_dir / "scripts")
        if (self.quill_dir / "tests").exists():
            shutil.copytree(self.quill_dir / "tests", install_dir / "tests")
        if (self.quill_dir / "games").exists():
            shutil.copytree(self.quill_dir / "games", install_dir / "games")
        
        # Copy launcher scripts
        shutil.copy(self.quill_dir / "quill.bat", install_dir / "quill.bat")
        
        # Copy documentation files
        for doc_file in ["README.md", "documentation/QUICK_START.md", "LICENSE", "requirements.txt", "CHANGELOG.md"]:
            if (self.quill_dir / doc_file).exists():
                shutil.copy(self.quill_dir / doc_file, install_dir / doc_file)
        
        print(f"✓ Copied {len(list(install_dir.rglob('*')))} files")
        
        # 3. Add to PATH
        print("🔧 Adding to PATH...")
        try:
            if self.is_admin:
                # System-wide PATH
                self.add_to_path_windows(install_dir, system=True)
            else:
                # User PATH
                self.add_to_path_windows(install_dir, system=False)
            print("✓ Added to PATH")
        except Exception as e:
            print(f"⚠ Could not add to PATH: {e}")
            print(f"  Please manually add {install_dir} to your PATH")
        
        # 4. Register .quill file association
        print("📄 Registering .quill file association...")
        try:
            self.register_file_association_windows(install_dir)
            print("✓ .quill files associated")
        except Exception as e:
            print(f"⚠ Could not register file association: {e}")
        
        # 5. Create start menu shortcut
        if self.is_admin:
            print("📌 Creating Start Menu shortcut...")
            try:
                self.create_start_menu_shortcut(install_dir)
                print("✓ Start Menu shortcut created")
            except Exception as e:
                print(f"⚠ Could not create shortcut: {e}")
        
        print()
        print("=" * 60)
        print("✅ Installation Complete!")
        print("=" * 60)
        print()
        print("🚀 Quick Start:")
        print(f"   1. Open a NEW terminal/command prompt")
        print(f"   2. Run: quill {install_dir / 'examples' / 'calculator.quill'}")
        print(f"   3. Or double-click any .quill file!")
        print()
        print(f"📚 Documentation: {install_dir / 'README.md'}")
        print()
        
        return True
    
    def install_unix(self):
        """Install Quill on Linux/macOS"""
        system_name = "macOS" if self.system == "Darwin" else "Linux"
        print(f"🐧 Installing Quill for {system_name}...")
        print()
        
        # 1. Determine installation directory
        if self.is_admin:
            install_dir = Path("/usr/local/lib/quill")
            bin_dir = Path("/usr/local/bin")
        else:
            install_dir = Path.home() / ".local" / "lib" / "quill"
            bin_dir = Path.home() / ".local" / "bin"
        
        print(f"📁 Installation directory: {install_dir}")
        print(f"📁 Binary directory: {bin_dir}")
        
        if install_dir.exists():
            response = input(f"⚠  Directory exists. Overwrite? (y/n): ")
            if response.lower() != 'y':
                print("Installation cancelled.")
                return False
            shutil.rmtree(install_dir)
        
        install_dir.mkdir(parents=True, exist_ok=True)
        bin_dir.mkdir(parents=True, exist_ok=True)
        
        # 2. Copy files
        print("📦 Copying files...")
        
        # Core directories (required)
        shutil.copytree(self.quill_dir / "core", install_dir / "core")
        shutil.copytree(self.quill_dir / "examples", install_dir / "examples")
        shutil.copytree(self.quill_dir / "docs", install_dir / "docs")
        
        # Optional directories (copy if they exist)
        if (self.quill_dir / "icons").exists():
            shutil.copytree(self.quill_dir / "icons", install_dir / "icons")
        if (self.quill_dir / "scripts").exists():
            shutil.copytree(self.quill_dir / "scripts", install_dir / "scripts")
        if (self.quill_dir / "tests").exists():
            shutil.copytree(self.quill_dir / "tests", install_dir / "tests")
        if (self.quill_dir / "games").exists():
            shutil.copytree(self.quill_dir / "games", install_dir / "games")
        
        # Copy documentation files
        for doc_file in ["README.md", "documentation/QUICK_START.md", "LICENSE", "requirements.txt", "CHANGELOG.md"]:
            if (self.quill_dir / doc_file).exists():
                shutil.copy(self.quill_dir / doc_file, install_dir / doc_file)
        
        print(f"✓ Copied {len(list(install_dir.rglob('*')))} files")
        
        # 3. Create launcher script
        print("🔧 Creating launcher script...")
        launcher_path = bin_dir / "quill"
        with open(launcher_path, 'w') as f:
            f.write(f"""#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, '{install_dir / 'core'}')
os.chdir('{install_dir}')
from quill import main
main()
""")
        
        # Make executable
        os.chmod(launcher_path, 0o755)
        print(f"✓ Created launcher: {launcher_path}")
        
        # 4. Add to PATH (if not already)
        shell_rc = None
        if 'bash' in os.environ.get('SHELL', ''):
            shell_rc = Path.home() / ".bashrc"
        elif 'zsh' in os.environ.get('SHELL', ''):
            shell_rc = Path.home() / ".zshrc"
        
        if shell_rc and not self.is_admin:
            print(f"🔧 Adding to PATH in {shell_rc}...")
            path_line = f'\nexport PATH="{bin_dir}:$PATH"  # Quill Language\n'
            
            if shell_rc.exists():
                content = shell_rc.read_text()
                if str(bin_dir) not in content:
                    with open(shell_rc, 'a') as f:
                        f.write(path_line)
                    print(f"✓ Added to {shell_rc}")
                    print(f"  Run: source {shell_rc}")
                else:
                    print(f"✓ Already in PATH")
        
        print()
        print("=" * 60)
        print("✅ Installation Complete!")
        print("=" * 60)
        print()
        print("🚀 Quick Start:")
        print(f"   1. Restart your terminal or run: source {shell_rc}")
        print(f"   2. Run: quill {install_dir / 'examples' / 'calculator.quill'}")
        print()
        print(f"📚 Documentation: {install_dir / 'README.md'}")
        print()
        
        return True
    
    def add_to_path_windows(self, directory, system=False):
        """Add directory to Windows PATH"""
        import winreg
        
        if system:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                                r'System\CurrentControlSet\Control\Session Manager\Environment',
                                0, winreg.KEY_ALL_ACCESS)
        else:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                'Environment',
                                0, winreg.KEY_ALL_ACCESS)
        
        try:
            path_value, _ = winreg.QueryValueEx(key, 'Path')
            if str(directory) not in path_value:
                new_path = path_value + ';' + str(directory)
                winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, new_path)
        finally:
            winreg.CloseKey(key)
        
        # Broadcast environment change
        try:
            import ctypes
            HWND_BROADCAST = 0xFFFF
            WM_SETTINGCHANGE = 0x1A
            SMTO_ABORTIFHUNG = 0x0002
            ctypes.windll.user32.SendMessageTimeoutW(
                HWND_BROADCAST, WM_SETTINGCHANGE, 0, 'Environment', 
                SMTO_ABORTIFHUNG, 5000, None
            )
        except:
            pass
    
    def register_file_association_windows(self, install_dir):
        """Register .quill file association on Windows"""
        import winreg
        
        # Create file type key
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, '.quill')
        winreg.SetValue(key, '', winreg.REG_SZ, 'QuillScript')
        winreg.CloseKey(key)
        
        # Create program key
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'QuillScript')
        winreg.SetValue(key, '', winreg.REG_SZ, 'Quill Script File')
        winreg.CloseKey(key)
        
        # Set icon (if available)
        icon_path = install_dir / "icons" / "quill_icon.ico"
        if icon_path.exists():
            key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r'QuillScript\DefaultIcon')
            winreg.SetValue(key, '', winreg.REG_SZ, str(icon_path))
            winreg.CloseKey(key)
        
        # Set open command
        command = f'"{sys.executable}" "{install_dir / "core" / "quill.py"}" "%1"'
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r'QuillScript\shell\open\command')
        winreg.SetValue(key, '', winreg.REG_SZ, command)
        winreg.CloseKey(key)
    
    def create_start_menu_shortcut(self, install_dir):
        """Create Windows Start Menu shortcut"""
        try:
            import win32com.client
            shell = win32com.client.Dispatch("WScript.Shell")
            start_menu = shell.SpecialFolders("AllUsersPrograms")
            shortcut_path = os.path.join(start_menu, "Quill Language.lnk")
            
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.TargetPath = str(install_dir / "quill.bat")
            shortcut.WorkingDirectory = str(install_dir)
            shortcut.Description = "Quill Scripting Language"
            shortcut.save()
        except ImportError:
            # pywin32 not available, skip shortcut creation
            pass
    
    def uninstall(self):
        """Uninstall Quill"""
        print("🗑️  Uninstalling Quill...")
        print()
        
        # Find installation directory
        if self.system == 'Windows':
            possible_dirs = [
                Path("C:/Program Files/Quill"),
                Path.home() / "Quill"
            ]
        else:
            possible_dirs = [
                Path("/usr/local/lib/quill"),
                Path.home() / ".local" / "lib" / "quill"
            ]
        
        install_dir = None
        for dir in possible_dirs:
            if dir.exists():
                install_dir = dir
                break
        
        if not install_dir:
            print("❌ Quill installation not found")
            return False
        
        print(f"📁 Found installation: {install_dir}")
        response = input("⚠  Remove Quill? (y/n): ")
        if response.lower() != 'y':
            print("Uninstall cancelled.")
            return False
        
        # Remove files
        print("🗑️  Removing files...")
        shutil.rmtree(install_dir)
        print("✓ Files removed")
        
        # Remove from PATH (Windows)
        if self.system == 'Windows':
            print("🔧 Removing from PATH...")
            # (Implementation would go here - similar to add_to_path but removing)
        
        print()
        print("✅ Quill has been uninstalled")
        print()
        
        return True
    
    def check_requirements(self):
        """Check if system meets requirements"""
        print("🔍 Checking requirements...")
        
        # Check Python version
        if sys.version_info < (3, 7):
            print(f"❌ Python 3.7+ required, you have {sys.version.split()[0]}")
            return False
        print(f"✓ Python {sys.version.split()[0]}")
        
        # Check if core directory exists
        if not (self.quill_dir / "core").exists():
            print(f"❌ Core directory not found in {self.quill_dir}")
            print("   Make sure you're running installer/setup.py from the Quill root directory")
            return False
        print(f"✓ Core files found")
        
        # Optional: Check for PIL (not required)
        try:
            import PIL
            print(f"✓ PIL/Pillow installed (optional - enables GUI features)")
        except ImportError:
            print(f"⚠ PIL/Pillow not installed (optional - GUI features disabled)")
        
        print()
        return True
    
    def run(self):
        """Run the installer"""
        self.print_banner()
        
        print(f"System: {self.system}")
        print(f"Python: {sys.version.split()[0]}")
        print(f"Admin/Sudo: {'Yes' if self.is_admin else 'No'}")
        print()
        
        # Check requirements first
        if not self.check_requirements():
            return False
        
        print()
        
        # Show menu
        print("Choose an option:")
        print("  1. Install Quill")
        print("  2. Uninstall Quill")
        print("  3. Exit")
        print()
        
        choice = input("Enter choice (1-3): ").strip()
        print()
        
        if choice == '1':
            if self.system == 'Windows':
                return self.install_windows()
            else:
                return self.install_unix()
        elif choice == '2':
            return self.uninstall()
        elif choice == '3':
            print("Goodbye!")
            return True
        else:
            print("Invalid choice")
            return False

def main():
    """Main entry point"""
    installer = QuillInstaller()
    
    try:
        success = installer.run()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
