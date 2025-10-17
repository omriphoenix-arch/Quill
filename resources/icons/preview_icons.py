"""
Icon Preview Tool for Quill
Shows all icon styles in a visual grid
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import tkinter as tk
    from tkinter import ttk
    PIL_AVAILABLE = True
    TK_AVAILABLE = True
except ImportError as e:
    print(f"Missing dependencies: {e}")
    print("Install with: pip install pillow")
    exit(1)

import os

class IconPreview:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quill Icon Gallery")
        self.root.geometry("900x700")
        self.root.configure(bg='#1e1e1e')
        
        self.icons = [
            ('quill_icon.ico', 'Gradient Book', 'Modern gradient\nPurple to pink\n"Q" glow effect'),
            ('quill_icon_minimalist.ico', 'Minimalist Flat', 'Clean design\nFlat blue\nFolded corner'),
            ('quill_icon_neon.ico', 'Neon Cyberpunk', 'Dark theme\nCyan glow\nFuturistic'),
            ('quill_icon_retro.ico', 'Retro Pixel Art', 'Pixel style\nAmber/yellow\nVintage feel'),
        ]
        
        self.setup_ui()
    
    def setup_ui(self):
        """Create the UI"""
        
        # Title
        title = tk.Label(
            self.root,
            text="🎨 Quill Icon Gallery",
            font=('Arial', 24, 'bold'),
            bg='#1e1e1e',
            fg='#ffffff'
        )
        title.pack(pady=20)
        
        subtitle = tk.Label(
            self.root,
            text="Choose your favorite icon style for .quill files",
            font=('Arial', 12),
            bg='#1e1e1e',
            fg='#888888'
        )
        subtitle.pack(pady=5)
        
        # Create grid frame
        grid_frame = tk.Frame(self.root, bg='#1e1e1e')
        grid_frame.pack(pady=20, fill='both', expand=True)
        
        # Configure grid
        for i in range(2):
            grid_frame.grid_columnconfigure(i, weight=1)
            grid_frame.grid_rowconfigure(i, weight=1)
        
        # Load and display icons
        row = 0
        col = 0
        
        for icon_file, name, description in self.icons:
            self.create_icon_card(grid_frame, icon_file, name, description, row, col)
            
            col += 1
            if col >= 2:
                col = 0
                row += 1
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="To change your icon:\n1. Close this window\n2. Run: python update_icon.py\n3. Choose your favorite style",
            font=('Arial', 10),
            bg='#1e1e1e',
            fg='#666666',
            justify='center'
        )
        instructions.pack(pady=20)
    
    def create_icon_card(self, parent, icon_file, name, description, row, col):
        """Create a card showing an icon"""
        
        # Card frame
        card = tk.Frame(
            parent,
            bg='#2d2d2d',
            relief='raised',
            borderwidth=2
        )
        card.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
        
        # Icon name
        name_label = tk.Label(
            card,
            text=name,
            font=('Arial', 14, 'bold'),
            bg='#2d2d2d',
            fg='#ffffff'
        )
        name_label.pack(pady=10)
        
        # Icon preview
        try:
            if os.path.exists(icon_file):
                # Load icon
                icon_img = Image.open(icon_file)
                
                # Get largest size available
                icon_img.seek(0)  # First image in ICO
                
                # Resize for display (128x128)
                icon_img = icon_img.resize((128, 128), Image.Resampling.LANCZOS)
                
                # Convert to PhotoImage
                from PIL import ImageTk
                photo = ImageTk.PhotoImage(icon_img)
                
                # Display
                icon_label = tk.Label(
                    card,
                    image=photo,
                    bg='#2d2d2d'
                )
                icon_label.image = photo  # Keep reference
                icon_label.pack(pady=10)
            else:
                missing_label = tk.Label(
                    card,
                    text="[Icon not found]\nRun create_alternate_icon.py",
                    font=('Arial', 10),
                    bg='#2d2d2d',
                    fg='#ff4444',
                    justify='center'
                )
                missing_label.pack(pady=40)
        
        except Exception as e:
            error_label = tk.Label(
                card,
                text=f"Error loading icon:\n{str(e)[:30]}",
                font=('Arial', 9),
                bg='#2d2d2d',
                fg='#ff4444',
                justify='center'
            )
            error_label.pack(pady=40)
        
        # Description
        desc_label = tk.Label(
            card,
            text=description,
            font=('Arial', 9),
            bg='#2d2d2d',
            fg='#aaaaaa',
            justify='center'
        )
        desc_label.pack(pady=10)
        
        # Filename
        file_label = tk.Label(
            card,
            text=icon_file,
            font=('Courier', 8),
            bg='#2d2d2d',
            fg='#666666'
        )
        file_label.pack(pady=5)
    
    def run(self):
        """Start the preview window"""
        self.root.mainloop()

def main():
    """Main function"""
    
    print("\n" + "=" * 60)
    print("  Quill Icon Preview")
    print("=" * 60 + "\n")
    
    print("Opening preview window...")
    print("(Close the window when done)\n")
    
    app = IconPreview()
    app.run()
    
    print("\n✓ Preview closed")
    print("\nTo change your icon, run:")
    print("  python update_icon.py")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
