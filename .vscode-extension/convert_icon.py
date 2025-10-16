"""
Convert ICO to PNG for VS Code extension
"""

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    print("Error: Pillow not installed. Run: pip install pillow")
    exit(1)

import os

# Get paths
script_dir = os.path.dirname(os.path.abspath(__file__))
icons_source = os.path.join(os.path.dirname(script_dir), 'icons')
ico_path = os.path.join(icons_source, 'storyscript_icon.ico')
png_path = os.path.join(script_dir, 'icons', 'storyscript-icon.png')

print("Converting ICO to PNG for VS Code...")
print(f"Source: {ico_path}")
print(f"Target: {png_path}")

# Open ICO and get largest size
with Image.open(ico_path) as img:
    # ICO files contain multiple sizes, get the largest
    img.seek(0)  # Go to first (largest) image
    
    # Convert to RGBA if needed
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Resize to 128x128 for VS Code
    img_resized = img.resize((128, 128), Image.Resampling.LANCZOS)
    
    # Save as PNG
    img_resized.save(png_path, 'PNG')
    
print(f"✓ Created: {png_path}")
print(f"  Size: 128x128 PNG")
print("\nNow installing the extension...")
