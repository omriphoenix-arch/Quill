"""
Icon Generator for Quill
Creates a custom .ico file for .quill files
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("PIL not available. Will create a basic icon.")

import struct

def create_quill_icon():
    """Create a modern icon for .quill files with gradient and book design"""
    
    if PIL_AVAILABLE:
        # Create a high-quality icon with PIL
        sizes = [256, 128, 64, 48, 32, 16]
        images = []
        
        for size in sizes:
            # Create image with transparent background
            img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Modern gradient book design
            margin = size // 10
            
            # Draw book spine shadow (depth effect)
            spine_offset = size // 20
            shadow_color = (30, 30, 30, 100)
            draw.rounded_rectangle(
                [margin + spine_offset, margin, size - margin + spine_offset, size - margin],
                radius=size // 20,
                fill=shadow_color
            )
            
            # Main book body with gradient effect (purple to pink)
            # Create gradient by drawing multiple rectangles
            book_left = margin
            book_right = size - margin
            book_top = margin
            book_bottom = size - margin
            
            # Gradient colors: purple -> magenta -> pink
            for i in range(book_bottom - book_top):
                ratio = i / (book_bottom - book_top)
                r = int(147 + (255 - 147) * ratio)  # 147 -> 255
                g = int(51 + (105 - 51) * ratio)     # 51 -> 105
                b = int(234 + (180 - 234) * ratio)   # 234 -> 180
                color = (r, g, b, 255)
                
                y = book_top + i
                draw.line([(book_left, y), (book_right, y)], fill=color, width=1)
            
            # Round the corners
            draw.rounded_rectangle(
                [book_left, book_top, book_right, book_bottom],
                radius=size // 20,
                outline=None
            )
            
            # Add book spine highlight
            spine_width = size // 12
            spine_color = (120, 40, 200, 255)  # Darker purple
            draw.rectangle(
                [book_left, book_top, book_left + spine_width, book_bottom],
                fill=spine_color
            )
            
            # Add decorative page lines (right side)
            page_line_color = (255, 255, 255, 150)
            line_width = max(1, size // 64)
            page_margin_h = book_left + size // 4
            page_margin_v = book_top + size // 6
            line_spacing = size // 8
            
            for i in range(4):
                y = page_margin_v + (i * line_spacing)
                if y < book_bottom - page_margin_v:
                    line_length = (book_right - page_margin_h) - (size // 16)
                    draw.rectangle(
                        [page_margin_h, y, page_margin_h + line_length, y + line_width],
                        fill=page_line_color
                    )
            
            # Add story icon/symbol - open book with "SS"
            try:
                font_size = size // 4
                # Try to use a bold system font
                try:
                    font = ImageFont.truetype("arialbd.ttf", font_size)
                except:
                    try:
                        font = ImageFont.truetype("arial.ttf", font_size)
                    except:
                        font = ImageFont.load_default()
                
                # Draw "Q" for Quill
                text = "Q"
                
                # Calculate position
                try:
                    bbox = draw.textbbox((0, 0), text, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]
                except:
                    text_width = font_size
                    text_height = font_size
                
                text_x = (size - text_width) // 2 + size // 20
                text_y = (size - text_height) // 2 + size // 20
                
                # Draw with glow effect
                glow_color = (255, 255, 255, 80)
                for offset in range(3, 0, -1):
                    draw.text((text_x + offset, text_y + offset), text, fill=glow_color, font=font)
                    draw.text((text_x - offset, text_y - offset), text, fill=glow_color, font=font)
                
                # Draw main text
                draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
            except Exception as e:
                # Fallback: draw a simple book symbol
                pass
            
            images.append(img)
        
        # Save as ICO
        images[0].save(
            'quill_icon.ico',
            format='ICO',
            sizes=[(img.width, img.height) for img in images],
            append_images=images[1:]
        )
        
        print("✓ Icon created successfully: quill_icon.ico")
        print("  Sizes included: " + ", ".join([f"{s}x{s}" for s in sizes]))
        
    else:
        # Create a simple BMP-based ICO manually
        print("Creating basic icon without PIL...")
        create_basic_icon()

def create_basic_icon():
    """Create a very basic 32x32 icon without PIL"""
    
    # Simple 32x32 icon data (blue square with white "S")
    # This is a simplified approach
    width, height = 32, 32
    
    # Create a simple blue square icon
    icon_data = []
    
    for y in range(height):
        for x in range(width):
            # Create a blue gradient with white "S" shape
            if (8 <= x <= 24 and 4 <= y <= 28):
                # Blue background
                r, g, b = 100, 150, 255
                
                # Draw white "S" (simplified)
                if ((6 <= x <= 12 and 8 <= y <= 12) or
                    (12 <= x <= 18 and 14 <= y <= 18) or
                    (18 <= x <= 24 and 20 <= y <= 24)):
                    r, g, b = 255, 255, 255
                    
                icon_data.append(bytes([b, g, r, 255]))  # BGRA format
            else:
                # Transparent
                icon_data.append(bytes([0, 0, 0, 0]))
    
    # Write ICO file
    with open('quill_icon.ico', 'wb') as f:
        # ICO header
        f.write(struct.pack('<HHH', 0, 1, 1))  # Reserved, Type, Count
        
        # Image directory entry
        f.write(struct.pack('<BBBBHHII',
                          width, height,  # Width, Height
                          0, 0,          # Colors, Reserved
                          1, 32,         # Planes, BitCount
                          len(icon_data) * len(icon_data[0]) + 40,  # Size
                          22))           # Offset
        
        # BMP header (BITMAPINFOHEADER)
        f.write(struct.pack('<IIIHHIIIIII',
                          40,                    # Header size
                          width, height * 2,     # Width, Height (doubled for mask)
                          1, 32,                 # Planes, BitCount
                          0,                     # Compression
                          len(icon_data) * len(icon_data[0]),  # Image size
                          0, 0, 0, 0))           # Other fields
        
        # Write pixel data (bottom to top)
        for row in reversed(icon_data):
            f.write(row)
    
    print("✓ Basic icon created: quill_icon.ico")

if __name__ == "__main__":
    print("=" * 50)
    print("Quill Icon Generator")
    print("=" * 50)
    print()
    
    try:
        create_quill_icon()
        print()
        print("Icon file ready for installation!")
        print()
        print("The icon will be associated with .quill files")
        print("when you run the installer.")
    except Exception as e:
        print(f"Error creating icon: {e}")
        print()
        print("You can still use Quill without a custom icon,")
        print("or manually create an icon file named 'quill_icon.ico'")
