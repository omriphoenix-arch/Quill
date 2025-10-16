"""
VS Code Extension Icon Generator for Quill
Creates multiple icon variants optimized for VS Code marketplace and editor UI
Generates PNG files at standard VS Code sizes: 128x128 (required), plus 16x16, 32x32, 256x256
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_vscode_icon_minimal(size=128, output_name="quill_vscode_minimal.png"):
    """Clean, minimal book icon with Q - modern flat design"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Padding
    pad = max(2, size // 8)
    
    # Simple book shape - centered rectangle with pages
    book_left = pad
    book_right = size - pad
    book_top = pad
    book_bottom = size - pad
    
    # Book cover (single solid color - modern purple)
    cover_color = (138, 43, 226, 255)  # Blue-violet
    draw.rounded_rectangle(
        [book_left, book_top, book_right, book_bottom],
        radius=size // 20,
        fill=cover_color
    )
    
    # Subtle page lines on right edge (skip for very small sizes)
    if size >= 32:
        page_color = (255, 255, 255, 60)
        for i in range(3):
            offset = (i + 1) * max(1, size // 64)
            if book_bottom - offset > book_top + offset:
                draw.rounded_rectangle(
                    [book_right - offset, book_top + offset, book_right - offset + 2, book_bottom - offset],
                    radius=max(1, size // 100),
                    fill=page_color
                )
    
    # Q letter - large and clean
    try:
        font_size = int(size * 0.5)
        font = ImageFont.truetype("segoeui.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "Q"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2 - bbox[1]
    
    # White Q with subtle shadow
    shadow_offset = max(1, size // 64)
    draw.text((text_x + shadow_offset, text_y + shadow_offset), text, fill=(0, 0, 0, 80), font=font)
    draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    return img


def create_vscode_icon_gradient(size=128, output_name="quill_vscode_gradient.png"):
    """Modern gradient style with depth"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    pad = size // 8
    
    # Circular background with gradient effect (simulated)
    center_x, center_y = size // 2, size // 2
    radius = (size - pad * 2) // 2
    
    # Create gradient circles (multiple layers)
    for i in range(radius, 0, -1):
        ratio = i / radius
        # Purple to blue gradient
        r = int(138 * ratio + 65 * (1 - ratio))
        g = int(43 * ratio + 105 * (1 - ratio))
        b = int(226 * ratio + 225 * (1 - ratio))
        alpha = 255
        
        draw.ellipse(
            [center_x - i, center_y - i, center_x + i, center_y + i],
            fill=(r, g, b, alpha)
        )
    
    # Q letter
    try:
        font_size = int(size * 0.55)
        font = ImageFont.truetype("segoeuib.ttf", font_size)  # Bold
    except:
        try:
            font = ImageFont.truetype("segoeui.ttf", int(size * 0.55))
        except:
            font = ImageFont.load_default()
    
    text = "Q"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2 - bbox[1]
    
    draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    return img


def create_vscode_icon_flat(size=128, output_name="quill_vscode_flat.png"):
    """Ultra-flat modern design - VS Code marketplace style"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Simple rounded square background
    pad = size // 6
    bg_color = (106, 90, 205, 255)  # Slate blue
    
    draw.rounded_rectangle(
        [pad, pad, size - pad, size - pad],
        radius=size // 8,
        fill=bg_color
    )
    
    # Q letter - centered
    try:
        font_size = int(size * 0.5)
        font = ImageFont.truetype("segoeui.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "Q"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2 - bbox[1]
    
    draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    return img


def create_vscode_icon_book_pages(size=128, output_name="quill_vscode_book.png"):
    """Stylized open book with Q"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    pad = size // 8
    
    # Open book (two pages)
    book_top = size // 3
    book_bottom = size - pad
    
    # Left page
    left_page = [
        pad, book_top,
        size // 2 - 2, book_bottom
    ]
    draw.rounded_rectangle(left_page, radius=size // 30, fill=(72, 61, 139, 255))
    
    # Right page
    right_page = [
        size // 2 + 2, book_top,
        size - pad, book_bottom
    ]
    draw.rounded_rectangle(right_page, radius=size // 30, fill=(106, 90, 205, 255))
    
    # Center binding
    draw.rectangle([size // 2 - 2, book_top, size // 2 + 2, book_bottom], fill=(50, 40, 100, 255))
    
    # Q on the left page
    try:
        font_size = int(size * 0.35)
        font = ImageFont.truetype("segoeui.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "Q"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (size // 4) - (text_width // 2)
    text_y = (book_top + book_bottom) // 2 - text_height // 2 - bbox[1]
    
    draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    return img


def create_vscode_icon_neon(size=128, output_name="quill_vscode_neon.png"):
    """Neon glow effect - eye-catching for dark themes"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Dark circular background
    center = size // 2
    radius = (size - size // 6) // 2
    
    draw.ellipse(
        [center - radius, center - radius, center + radius, center + radius],
        fill=(30, 20, 50, 255)
    )
    
    # Q with neon glow effect (multiple layers)
    try:
        font_size = int(size * 0.55)
        font = ImageFont.truetype("segoeuib.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("segoeui.ttf", int(size * 0.55))
        except:
            font = ImageFont.load_default()
    
    text = "Q"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2 - bbox[1]
    
    # Outer glow layers
    neon_color = (138, 43, 226)  # Purple
    for offset in range(8, 0, -1):
        alpha = int(30 * (8 - offset) / 8)
        for dx in range(-offset, offset + 1):
            for dy in range(-offset, offset + 1):
                if dx * dx + dy * dy <= offset * offset:
                    draw.text(
                        (text_x + dx, text_y + dy),
                        text,
                        fill=(*neon_color, alpha),
                        font=font
                    )
    
    # Bright core
    draw.text((text_x, text_y), text, fill=(255, 100, 255, 255), font=font)
    
    return img


def create_vscode_icon_monochrome(size=128, output_name="quill_vscode_mono.png"):
    """Simple monochrome - works on any background"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Circular background
    pad = size // 6
    draw.ellipse([pad, pad, size - pad, size - pad], fill=(70, 70, 70, 255))
    
    # Q letter
    try:
        font_size = int(size * 0.5)
        font = ImageFont.truetype("segoeui.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "Q"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2 - bbox[1]
    
    draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    return img


def main():
    """Generate all VS Code icon variants"""
    print("\n" + "=" * 60)
    print("   Quill VS Code Extension Icon Generator")
    print("=" * 60 + "\n")
    
    # Create icons directory if needed
    icons_dir = os.path.dirname(os.path.abspath(__file__))
    
    # VS Code requires 128x128, but we'll generate multiple sizes
    sizes = [16, 32, 128, 256]
    
    variants = [
        ("minimal", create_vscode_icon_minimal, "Clean minimal book with Q"),
        ("gradient", create_vscode_icon_gradient, "Modern gradient circle"),
        ("flat", create_vscode_icon_flat, "Ultra-flat rounded square"),
        ("book", create_vscode_icon_book_pages, "Stylized open book pages"),
        ("neon", create_vscode_icon_neon, "Neon glow effect"),
        ("mono", create_vscode_icon_monochrome, "Simple monochrome")
    ]
    
    print("Generating icon variants:\n")
    
    for variant_name, generator_func, description in variants:
        print(f"📦 {variant_name.upper()}: {description}")
        
        for size in sizes:
            filename = f"quill_vscode_{variant_name}_{size}.png"
            filepath = os.path.join(icons_dir, filename)
            
            # Generate icon at this size
            img = generator_func(size=size)
            img.save(filepath, 'PNG')
            
            print(f"   ✓ {size}x{size} → {filename}")
        
        print()
    
    print("=" * 60)
    print("✅ All VS Code icons generated successfully!")
    print("=" * 60)
    print("\nFiles created in:", icons_dir)
    print("\nMain icon (128x128) options:")
    for variant_name, _, description in variants:
        print(f"  • quill_vscode_{variant_name}_128.png - {description}")
    
    print("\n💡 Next steps:")
    print("1. Open icons/vscode_icon_gallery.html to preview all variants")
    print("2. Choose your favorite design")
    print("3. Copy the selected 128x128 PNG to .vscode-extension/icon.png")
    print("4. Update package.json icon reference")
    print()


if __name__ == "__main__":
    main()
