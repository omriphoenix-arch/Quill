"""
Alternative Icon Generator for Quill
Creates alternate icon designs for .quill files
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("PIL not available. Please install: pip install pillow")
    exit(1)

import math

def create_minimalist_icon():
    """Create a minimalist flat design icon"""
    
    sizes = [256, 128, 64, 48, 32, 16]
    images = []
    
    for size in sizes:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Flat design: Simple document with folded corner
        margin = size // 8
        
        # Main document body
        doc_color = (52, 152, 219, 255)  # Flat blue
        doc_left = margin
        doc_right = size - margin
        doc_top = margin
        doc_bottom = size - margin
        
        # Document rectangle
        draw.rectangle(
            [doc_left, doc_top, doc_right, doc_bottom],
            fill=doc_color
        )
        
        # Folded corner (top right)
        fold_size = size // 5
        fold_points = [
            (doc_right - fold_size, doc_top),
            (doc_right, doc_top + fold_size),
            (doc_right - fold_size, doc_top + fold_size)
        ]
        draw.polygon(fold_points, fill=(41, 128, 185, 255))  # Darker blue
        
        # Story symbol - simple text lines
        line_color = (255, 255, 255, 255)
        line_width = max(1, size // 32)
        text_margin_h = doc_left + size // 6
        text_margin_v = doc_top + size // 4
        line_spacing = size // 10
        
        for i in range(5):
            y = text_margin_v + (i * line_spacing)
            if y < doc_bottom - size // 6:
                line_length = (doc_right - text_margin_h - size // 6) * (0.8 if i % 2 else 1.0)
                draw.rectangle(
                    [text_margin_h, y, text_margin_h + line_length, y + line_width],
                    fill=line_color
                )
        
        images.append(img)
    
    images[0].save(
        'quill_icon_minimalist.ico',
        format='ICO',
        sizes=[(img.width, img.height) for img in images],
        append_images=images[1:]
    )
    
    print("✓ Minimalist icon created: quill_icon_minimalist.ico")

def create_neon_icon():
    """Create a cyberpunk/neon style icon"""
    
    sizes = [256, 128, 64, 48, 32, 16]
    images = []
    
    for size in sizes:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Dark background with neon outline
        margin = size // 8
        
        # Dark inner rectangle
        bg_color = (20, 20, 30, 255)  # Dark background
        draw.rounded_rectangle(
            [margin, margin, size - margin, size - margin],
            radius=size // 16,
            fill=bg_color
        )
        
        # Neon glow effect - multiple layers
        neon_colors = [
            ((0, 255, 255, 50), 8),    # Outer glow
            ((0, 255, 255, 100), 6),   # Mid glow
            ((0, 255, 255, 200), 4),   # Inner glow
            ((0, 255, 255, 255), 2),   # Core
        ]
        
        for color, width in neon_colors:
            draw.rounded_rectangle(
                [margin, margin, size - margin, size - margin],
                radius=size // 16,
                outline=color,
                width=max(1, size // width // 16)
            )
        
        # Neon "S" symbol
        try:
            font_size = size // 2
            try:
                font = ImageFont.truetype("arialbd.ttf", font_size)
            except:
                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()
            
            text = "S"
            
            try:
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
            except:
                text_width = font_size
                text_height = font_size
            
            text_x = (size - text_width) // 2
            text_y = (size - text_height) // 2
            
            # Neon glow on text
            for offset in range(8, 0, -2):
                alpha = 30 + (8 - offset) * 20
                glow_color = (0, 255, 255, alpha)
                draw.text((text_x, text_y), text, fill=glow_color, font=font)
            
            # Core neon text
            draw.text((text_x, text_y), text, fill=(0, 255, 255, 255), font=font)
        except:
            pass
        
        images.append(img)
    
    images[0].save(
        'quill_icon_neon.ico',
        format='ICO',
        sizes=[(img.width, img.height) for img in images],
        append_images=images[1:]
    )
    
    print("✓ Neon icon created: quill_icon_neon.ico")

def create_retro_icon():
    """Create a retro/vintage pixel art style icon"""
    
    sizes = [256, 128, 64, 48, 32, 16]
    images = []
    
    for size in sizes:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Retro color palette
        bg_color = (255, 193, 7, 255)      # Amber/yellow
        shadow_color = (255, 152, 0, 255)   # Orange
        text_color = (139, 69, 19, 255)     # Brown
        
        margin = size // 8
        
        # Pixelated effect - use rectangles
        # Main rectangle
        draw.rectangle(
            [margin, margin, size - margin, size - margin],
            fill=bg_color
        )
        
        # Shadow/border effect
        border_width = max(1, size // 32)
        draw.rectangle(
            [margin, margin, size - margin, margin + border_width],
            fill=shadow_color
        )
        draw.rectangle(
            [margin, margin, margin + border_width, size - margin],
            fill=shadow_color
        )
        
        # Pixelated text pattern
        pixel_size = max(1, size // 16)
        grid_margin = margin + size // 6
        
        # Create "STORY" in pixel art (simplified)
        # S pattern
        s_pattern = [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 1, 0, 0],
        ]
        
        for row, line in enumerate(s_pattern):
            for col, pixel in enumerate(line):
                if pixel:
                    x = grid_margin + col * pixel_size * 2
                    y = grid_margin + row * pixel_size * 2
                    draw.rectangle(
                        [x, y, x + pixel_size, y + pixel_size],
                        fill=text_color
                    )
        
        images.append(img)
    
    images[0].save(
        'quill_icon_retro.ico',
        format='ICO',
        sizes=[(img.width, img.height) for img in images],
        append_images=images[1:]
    )
    
    print("✓ Retro icon created: quill_icon_retro.ico")

if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("Quill Alternative Icon Generator")
    print("=" * 50 + "\n")
    
    create_minimalist_icon()
    create_neon_icon()
    create_retro_icon()
    
    print("\n" + "=" * 50)
    print("All alternative icons created successfully!")
    print("=" * 50)
    print("\nChoose your favorite icon style:")
    print("  • quill_icon.ico (gradient book)")
    print("  • quill_icon_minimalist.ico (flat design)")
    print("  • quill_icon_neon.ico (cyberpunk)")
    print("  • quill_icon_retro.ico (pixel art)")
    print("\nRename your choice to 'quill_icon.ico' and run the installer!")
