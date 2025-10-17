"""
Quill Language - GUI Installer
Professional installation wizard with graphical interface
"""

import sys
import os
import shutil
import platform
import subprocess
import threading
from pathlib import Path

# Try to import tkinter
try:
    import tkinter as tk
    from tkinter import ttk, messagebox, scrolledtext
    HAS_GUI = True
except ImportError:
    HAS_GUI = False
    print("⚠ tkinter not available. Falling back to console installer.")
    print("  Install tkinter: sudo apt-get install python3-tk (Linux)")

class QuillInstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quill Language Installer")
        self.root.geometry("700x600")  # Increased size
        self.root.resizable(True, True)  # Allow resizing
        self.root.minsize(650, 550)  # Minimum size to keep UI usable
        
        # Center window on screen
        self.root.update_idletasks()
        width = 700
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Installer state
        self.system = platform.system()
        # Get project root (parent of installer directory)
        self.quill_dir = Path(__file__).parent.parent.absolute()
        self.install_dir = None
        self.current_page = 0
        
        # Check admin status
        self.is_admin = self.check_admin()
        
        # Create UI
        self.create_widgets()
        self.show_welcome_page()
    
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
    
    def create_widgets(self):
        """Create main UI layout"""
        # Header
        header_frame = tk.Frame(self.root, bg="#4A148C", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="Quill Language Installer",
            font=("Arial", 20, "bold"),
            bg="#4A148C",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Main content area with scrollbar
        content_container = tk.Frame(self.root, bg="white")
        content_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create canvas and scrollbar for scrollable content
        self.canvas = tk.Canvas(content_container, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(content_container, orient=tk.VERTICAL, command=self.canvas.yview)
        self.content_frame = tk.Frame(self.canvas, bg="white")
        
        # Configure scrolling
        self.content_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Bind canvas width to content frame width
        self.canvas.bind('<Configure>', lambda e: self.canvas.itemconfig(self.canvas_frame, width=e.width))
        
        # Pack scrollbar and canvas
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Bind mouse wheel for scrolling
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Footer with buttons
        footer_frame = tk.Frame(self.root, bg="#f0f0f0", height=80)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)
        
        # Buttons
        button_frame = tk.Frame(footer_frame, bg="#f0f0f0")
        button_frame.pack(side=tk.RIGHT, padx=20, pady=10)
        
        self.back_button = tk.Button(
            button_frame,
            text="< Back",
            command=self.go_back,
            width=12,
            height=2,
            state=tk.DISABLED,
            font=("Arial", 10),
            relief=tk.RAISED,
            bd=2
        )
        self.back_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = tk.Button(
            button_frame,
            text="Next >",
            command=self.go_next,
            width=12,
            height=2,
            bg="#6A1B9A",  # Lighter purple for better visibility
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            bd=2,
            activebackground="#8E24AA",  # Even lighter when clicked
            activeforeground="white",
            cursor="hand2"
        )
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        self.cancel_button = tk.Button(
            button_frame,
            text="Cancel",
            command=self.cancel_install,
            width=12,
            height=2,
            font=("Arial", 10),
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        )
        self.cancel_button.pack(side=tk.LEFT, padx=5)
    
    def clear_content(self):
        """Clear content frame"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_welcome_page(self):
        """Show welcome screen"""
        self.clear_content()
        self.current_page = 0
        self.back_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL, text="Next >")
        
        # Welcome message
        welcome_label = tk.Label(
            self.content_frame,
            text="Welcome to the Quill Language Setup Wizard",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        welcome_label.pack(pady=20)
        
        # Description
        desc_text = """This wizard will guide you through the installation of Quill, 
a modern scripting language with rich error messages and 
comprehensive standard library.

Quill includes:
• Full interpreter with module system
• 40+ built-in utility functions
• File I/O and game development modules
• Complete documentation and examples
• Zero external dependencies

Click Next to continue."""
        
        desc_label = tk.Label(
            self.content_frame,
            text=desc_text,
            font=("Arial", 10),
            bg="white",
            justify=tk.LEFT
        )
        desc_label.pack(pady=10, padx=20)
        
        # System info
        info_frame = tk.LabelFrame(self.content_frame, text="System Information", bg="white")
        info_frame.pack(pady=20, padx=20, fill=tk.X)
        
        tk.Label(info_frame, text=f"Operating System: {self.system}", bg="white", anchor="w").pack(fill=tk.X, padx=10, pady=2)
        tk.Label(info_frame, text=f"Python Version: {sys.version.split()[0]}", bg="white", anchor="w").pack(fill=tk.X, padx=10, pady=2)
        tk.Label(info_frame, text=f"Administrator: {'Yes' if self.is_admin else 'No'}", bg="white", anchor="w").pack(fill=tk.X, padx=10, pady=2)
    
    def show_license_page(self):
        """Show license agreement"""
        self.clear_content()
        self.current_page = 1
        self.back_button.config(state=tk.NORMAL)
        
        tk.Label(
            self.content_frame,
            text="License Agreement",
            font=("Arial", 14, "bold"),
            bg="white"
        ).pack(pady=10)
        
        # License text
        license_text = scrolledtext.ScrolledText(
            self.content_frame,
            wrap=tk.WORD,
            width=60,
            height=15,
            font=("Courier", 9)
        )
        license_text.pack(pady=10, padx=20)
        
        # Read LICENSE file if exists
        license_file = self.quill_dir / "LICENSE"
        if license_file.exists():
            with open(license_file, 'r', encoding='utf-8') as f:
                license_text.insert(tk.END, f.read())
        else:
            # Quill Programming Language License
            license_text.insert(tk.END, """Quill Programming Language License

Copyright (c) 2025 Omri Morgan (omriphoenix-arch)
All Rights Reserved.

THE QUILL PROGRAMMING LANGUAGE, INCLUDING ITS NAME, LOGO, INTERPRETER, 
AND ASSOCIATED DOCUMENTATION, IS THE INTELLECTUAL PROPERTY OF OMRI MORGAN.

PERMITTED USE:
- Personal use for learning and educational purposes
- Running and creating programs using the Quill language
- Sharing programs written in Quill (.quill files)
- Contributing improvements via pull requests (contributions become part of this project)

NOT PERMITTED WITHOUT WRITTEN PERMISSION:
- Claiming ownership or creation of the Quill language
- Creating derivative programming languages based on Quill's design
- Redistributing modified versions under a different name
- Commercial use of the Quill interpreter or language without permission
- Removing or altering copyright notices

ATTRIBUTION:
Any use of Quill must include clear attribution to Omri Morgan as the original creator.
The name "Quill" and associated branding remain the property of Omri Morgan.

DISCLAIMER:
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For commercial licensing inquiries, please contact: 
Quill.Contact94@gmail.com

Copyright © 2025 Omri Morgan All Rights Reserved
""")
        
        license_text.config(state=tk.DISABLED)
        
        # Acceptance checkbox
        self.accept_var = tk.BooleanVar()
        accept_check = tk.Checkbutton(
            self.content_frame,
            text="I accept the terms in the License Agreement",
            variable=self.accept_var,
            bg="white",
            command=self.check_license_acceptance
        )
        accept_check.pack(pady=10)
        
        self.next_button.config(state=tk.DISABLED)
    
    def check_license_acceptance(self):
        """Enable/disable next button based on license acceptance"""
        if self.accept_var.get():
            self.next_button.config(state=tk.NORMAL)
        else:
            self.next_button.config(state=tk.DISABLED)
    
    def show_installation_type_page(self):
        """Show installation type selection"""
        self.clear_content()
        self.current_page = 2
        
        tk.Label(
            self.content_frame,
            text="Choose Installation Type",
            font=("Arial", 14, "bold"),
            bg="white"
        ).pack(pady=20)
        
        self.install_type_var = tk.StringVar(value="recommended")
        
        # Recommended installation
        recommended_frame = tk.LabelFrame(
            self.content_frame,
            text="Recommended Installation",
            bg="white",
            font=("Arial", 10, "bold")
        )
        recommended_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Radiobutton(
            recommended_frame,
            text="Install for all users (requires administrator)" if self.is_admin else "Install for current user only",
            variable=self.install_type_var,
            value="recommended",
            bg="white",
            font=("Arial", 10)
        ).pack(anchor=tk.W, padx=10, pady=5)
        
        if self.system == 'Windows':
            default_path = "C:\\Program Files\\Quill" if self.is_admin else str(Path.home() / "Quill")
        else:
            default_path = "/usr/local/lib/quill" if self.is_admin else str(Path.home() / ".local" / "lib" / "quill")
        
        tk.Label(
            recommended_frame,
            text=f"Install to: {default_path}",
            bg="white",
            fg="gray"
        ).pack(anchor=tk.W, padx=30, pady=2)
        
        tk.Label(
            recommended_frame,
            text="• Adds to PATH\n• File associations\n• Start menu shortcuts",
            bg="white",
            fg="gray",
            justify=tk.LEFT
        ).pack(anchor=tk.W, padx=30, pady=5)
        
        # Custom installation
        custom_frame = tk.LabelFrame(
            self.content_frame,
            text="Custom Installation",
            bg="white",
            font=("Arial", 10, "bold")
        )
        custom_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Radiobutton(
            custom_frame,
            text="Choose installation location and options",
            variable=self.install_type_var,
            value="custom",
            bg="white",
            font=("Arial", 10)
        ).pack(anchor=tk.W, padx=10, pady=5)
    
    def show_custom_options_page(self):
        """Show custom installation options"""
        self.clear_content()
        self.current_page = 3
        
        tk.Label(
            self.content_frame,
            text="Custom Installation Options",
            font=("Arial", 14, "bold"),
            bg="white"
        ).pack(pady=20)
        
        # Installation path
        path_frame = tk.LabelFrame(self.content_frame, text="Installation Directory", bg="white")
        path_frame.pack(pady=10, padx=20, fill=tk.X)
        
        path_entry_frame = tk.Frame(path_frame, bg="white")
        path_entry_frame.pack(fill=tk.X, padx=10, pady=10)
        
        if self.system == 'Windows':
            default_path = "C:\\Program Files\\Quill" if self.is_admin else str(Path.home() / "Quill")
        else:
            default_path = "/usr/local/lib/quill" if self.is_admin else str(Path.home() / ".local" / "lib" / "quill")
        
        self.install_path_var = tk.StringVar(value=default_path)
        tk.Entry(
            path_entry_frame,
            textvariable=self.install_path_var,
            width=50
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            path_entry_frame,
            text="Browse...",
            command=self.browse_install_dir
        ).pack(side=tk.LEFT)
        
        # Options
        options_frame = tk.LabelFrame(self.content_frame, text="Installation Options", bg="white")
        options_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.add_to_path_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            options_frame,
            text="Add Quill to PATH (run 'quill' from anywhere)",
            variable=self.add_to_path_var,
            bg="white"
        ).pack(anchor=tk.W, padx=10, pady=5)
        
        self.file_association_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            options_frame,
            text="Register .quill file association",
            variable=self.file_association_var,
            bg="white"
        ).pack(anchor=tk.W, padx=10, pady=5)
        
        if self.system == 'Windows' and self.is_admin:
            self.start_menu_var = tk.BooleanVar(value=True)
            tk.Checkbutton(
                options_frame,
                text="Create Start Menu shortcut",
                variable=self.start_menu_var,
                bg="white"
            ).pack(anchor=tk.W, padx=10, pady=5)
        
        self.install_examples_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            options_frame,
            text="Install examples and documentation",
            variable=self.install_examples_var,
            bg="white"
        ).pack(anchor=tk.W, padx=10, pady=5)
    
    def browse_install_dir(self):
        """Open directory browser"""
        from tkinter import filedialog
        directory = filedialog.askdirectory(initialdir=self.install_path_var.get())
        if directory:
            self.install_path_var.set(directory)
    
    def show_ready_page(self):
        """Show ready to install page"""
        self.clear_content()
        self.current_page = 4
        self.next_button.config(text="Install")
        
        tk.Label(
            self.content_frame,
            text="Ready to Install",
            font=("Arial", 14, "bold"),
            bg="white"
        ).pack(pady=20)
        
        tk.Label(
            self.content_frame,
            text="The installer is ready to begin installation.",
            font=("Arial", 10),
            bg="white"
        ).pack(pady=10)
        
        # Summary
        summary_frame = tk.LabelFrame(self.content_frame, text="Installation Summary", bg="white")
        summary_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Determine install path
        if hasattr(self, 'install_path_var'):
            install_path = self.install_path_var.get()
        else:
            if self.system == 'Windows':
                install_path = "C:\\Program Files\\Quill" if self.is_admin else str(Path.home() / "Quill")
            else:
                install_path = "/usr/local/lib/quill" if self.is_admin else str(Path.home() / ".local" / "lib" / "quill")
        
        self.install_dir = Path(install_path)
        
        summary_text = f"""Installation Location:
  {install_path}

Components to Install:
  • Quill Interpreter (core runtime)
  • Module System (io, game modules)
  • Standard Library (40+ functions)
  • Examples and Documentation
  • Test Suite

Disk Space Required: ~2 MB

System Integration:
  • {'✓' if getattr(self, 'add_to_path_var', tk.BooleanVar(value=True)).get() else '✗'} Add to PATH
  • {'✓' if getattr(self, 'file_association_var', tk.BooleanVar(value=True)).get() else '✗'} File association (.quill)
  • {'✓' if self.system == 'Windows' and self.is_admin else '✗'} Start Menu shortcut

Click Install to begin installation."""
        
        tk.Label(
            summary_frame,
            text=summary_text,
            bg="white",
            justify=tk.LEFT,
            font=("Courier", 9)
        ).pack(padx=20, pady=20, anchor=tk.W)
    
    def show_installing_page(self):
        """Show installation progress"""
        self.clear_content()
        self.current_page = 5
        self.back_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)
        self.cancel_button.config(state=tk.DISABLED)
        
        tk.Label(
            self.content_frame,
            text="Installing Quill Language...",
            font=("Arial", 14, "bold"),
            bg="white"
        ).pack(pady=20)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            self.content_frame,
            variable=self.progress_var,
            maximum=100,
            length=400,
            mode='determinate'
        )
        self.progress_bar.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(
            self.content_frame,
            text="Preparing installation...",
            bg="white",
            font=("Arial", 10)
        )
        self.status_label.pack(pady=10)
        
        # Log output
        self.log_text = scrolledtext.ScrolledText(
            self.content_frame,
            wrap=tk.WORD,
            width=60,
            height=10,
            font=("Courier", 8)
        )
        self.log_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Start installation in thread
        install_thread = threading.Thread(target=self.perform_installation)
        install_thread.daemon = True
        install_thread.start()
    
    def log(self, message):
        """Add message to log"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def update_status(self, message, progress):
        """Update status and progress"""
        self.status_label.config(text=message)
        self.progress_var.set(progress)
        self.root.update()
    
    def perform_installation(self):
        """Perform the actual installation"""
        try:
            # Import setup logic
            from setup import QuillInstaller
            installer = QuillInstaller()
            
            self.update_status("Creating installation directory...", 10)
            self.log(f"Source directory: {self.quill_dir}")
            self.log(f"Installation directory: {self.install_dir}")
            
            # Verify source directory exists
            if not self.quill_dir.exists():
                raise FileNotFoundError(f"Source directory not found: {self.quill_dir}")
            
            # Create install directory
            if self.install_dir.exists():
                self.log(f"Removing existing installation at {self.install_dir}")
                shutil.rmtree(self.install_dir)
            
            self.log(f"Creating directory: {self.install_dir}")
            self.install_dir.mkdir(parents=True, exist_ok=True)
            
            # Copy core files
            self.update_status("Copying core files...", 20)
            core_src = self.quill_dir / "core"
            core_dst = self.install_dir / "core"
            self.log(f"Copying: {core_src} -> {core_dst}")
            if not core_src.exists():
                raise FileNotFoundError(f"Core directory not found: {core_src}")
            shutil.copytree(core_src, core_dst)
            self.log("✓ Core files copied")
            
            # Copy examples
            self.update_status("Copying examples...", 40)
            examples_src = self.quill_dir / "examples"
            examples_dst = self.install_dir / "examples"
            self.log(f"Copying: {examples_src} -> {examples_dst}")
            if not examples_src.exists():
                raise FileNotFoundError(f"Examples directory not found: {examples_src}")
            shutil.copytree(examples_src, examples_dst)
            self.log("✓ Examples copied")
            
            # Copy API documentation
            self.update_status("Copying API documentation...", 50)
            docs_src = self.quill_dir / "docs"
            if docs_src.exists():
                try:
                    self.log(f"Copying: {docs_src} -> {self.install_dir / 'docs'}")
                    shutil.copytree(docs_src, self.install_dir / "docs")
                    self.log("✓ API documentation copied")
                except Exception as e:
                    self.log(f"⚠ Could not copy API docs: {e}")
            else:
                self.log("⊘ API documentation not found, skipping")
            
            # Copy project documentation
            self.update_status("Copying project documentation...", 55)
            doc_src = self.quill_dir / "documentation"
            if doc_src.exists():
                try:
                    self.log(f"Copying: {doc_src} -> {self.install_dir / 'documentation'}")
                    shutil.copytree(doc_src, self.install_dir / "documentation")
                    self.log("✓ Project documentation copied")
                except Exception as e:
                    self.log(f"⚠ Could not copy project docs: {e}")
            else:
                self.log("⊘ Project documentation not found, skipping")
            
            # Optional components
            self.update_status("Copying optional components...", 60)
            optional_components = {
                "resources": "Resources",
                "scripts": "Scripts",
                "tests": "Tests",
                "games": "Games",
                "installer": "Installer"
            }
            
            for component, display_name in optional_components.items():
                src = self.quill_dir / component
                dst = self.install_dir / component
                if src.exists():
                    try:
                        self.log(f"Copying: {src} -> {dst}")
                        shutil.copytree(src, dst)
                        self.log(f"✓ {display_name} copied")
                    except Exception as e:
                        self.log(f"⚠ Could not copy {display_name}: {e}")
                else:
                    self.log(f"⊘ {display_name} not found, skipping")
            
            self.update_status("Copying root files...", 70)
            root_files = ["README.md", "LICENSE", "requirements.txt", "CHANGELOG.md", 
                         "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "STRUCTURE.md",
                         "quill.bat", "quill"]
            for doc_file in root_files:
                src = self.quill_dir / doc_file
                if src.exists():
                    try:
                        dest = self.install_dir / doc_file
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy(src, dest)
                    except Exception as e:
                        self.log(f"⚠ Could not copy {doc_file}: {e}")
            self.log("✓ Root files copied")
            
            # System integration
            if getattr(self, 'add_to_path_var', tk.BooleanVar(value=True)).get():
                self.update_status("Adding to PATH...", 80)
                try:
                    if self.system == 'Windows':
                        installer.add_to_path_windows(self.install_dir, system=self.is_admin)
                    self.log("✓ Added to PATH")
                except Exception as e:
                    self.log(f"⚠ Could not add to PATH: {e}")
            
            if getattr(self, 'file_association_var', tk.BooleanVar(value=True)).get() and self.system == 'Windows':
                self.update_status("Registering file association...", 90)
                try:
                    installer.register_file_association_windows(self.install_dir)
                    self.log("✓ File association registered")
                except Exception as e:
                    self.log(f"⚠ Could not register file association: {e}")
            
            self.update_status("Installation complete!", 100)
            self.log("\n✓ Installation completed successfully!")
            
            # Show completion page
            self.root.after(1000, self.show_complete_page)
            
        except Exception as e:
            self.log(f"\n❌ Installation failed: {e}")
            messagebox.showerror("Installation Error", f"Installation failed:\n{e}")
            self.next_button.config(state=tk.NORMAL, text="Retry")
            self.cancel_button.config(state=tk.NORMAL)
    
    def show_complete_page(self):
        """Show installation complete page"""
        self.clear_content()
        self.current_page = 6
        self.next_button.config(state=tk.NORMAL, text="Finish")
        self.cancel_button.config(state=tk.DISABLED)
        
        tk.Label(
            self.content_frame,
            text="✓ Installation Complete!",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="green"
        ).pack(pady=30)
        
        completion_text = f"""Quill Language has been successfully installed!

Installation Location:
  {self.install_dir}

To get started:
  1. Open a NEW terminal/command prompt
  2. Run: quill examples/calculator.quill
  3. Or double-click any .quill file!

Documentation:
  {self.install_dir / 'README.md'}
  {self.install_dir / 'documentation/QUICK_START.md'}

Thank you for installing Quill!"""
        
        tk.Label(
            self.content_frame,
            text=completion_text,
            bg="white",
            justify=tk.LEFT,
            font=("Arial", 10)
        ).pack(pady=20, padx=30)
        
        # Launch examples checkbox
        self.launch_examples_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            self.content_frame,
            text="View examples folder",
            variable=self.launch_examples_var,
            bg="white"
        ).pack(pady=10)
    
    def go_back(self):
        """Go to previous page"""
        if self.current_page == 1:
            self.show_welcome_page()
        elif self.current_page == 2:
            self.show_license_page()
        elif self.current_page == 3:
            self.show_installation_type_page()
        elif self.current_page == 4:
            if hasattr(self, 'install_type_var') and self.install_type_var.get() == "custom":
                self.show_custom_options_page()
            else:
                self.show_installation_type_page()
    
    def go_next(self):
        """Go to next page"""
        if self.current_page == 0:
            # Check requirements
            if sys.version_info < (3, 7):
                messagebox.showerror(
                    "Requirements Not Met",
                    f"Python 3.7+ required\nYou have {sys.version.split()[0]}"
                )
                return
            self.show_license_page()
        elif self.current_page == 1:
            self.show_installation_type_page()
        elif self.current_page == 2:
            if hasattr(self, 'install_type_var') and self.install_type_var.get() == "custom":
                self.show_custom_options_page()
            else:
                self.show_ready_page()
        elif self.current_page == 3:
            self.show_ready_page()
        elif self.current_page == 4:
            self.show_installing_page()
        elif self.current_page == 6:
            # Finish - open examples if requested
            if hasattr(self, 'launch_examples_var') and self.launch_examples_var.get():
                examples_dir = self.install_dir / "examples"
                if self.system == 'Windows':
                    os.startfile(examples_dir)
                elif self.system == 'Darwin':  # macOS
                    subprocess.run(['open', examples_dir])
                else:  # Linux
                    subprocess.run(['xdg-open', examples_dir])
            self.root.quit()
    
    def cancel_install(self):
        """Cancel installation"""
        if messagebox.askokcancel("Cancel Installation", "Are you sure you want to cancel the installation?"):
            self.root.quit()

def main_gui():
    """Main entry point for GUI installer"""
    root = tk.Tk()
    app = QuillInstallerGUI(root)
    root.mainloop()

def main():
    """Main entry point - choose GUI or console"""
    if HAS_GUI and '--console' not in sys.argv:
        # Use GUI installer
        main_gui()
    else:
        # Fallback to console installer
        from setup import QuillInstaller
        installer = QuillInstaller()
        installer.run()

if __name__ == "__main__":
    main()
