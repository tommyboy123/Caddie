from PIL import Image, ImageDraw, ImageFont
import math

def create_golf_putting_icon_hq(size):
    """Create a high-quality putting green icon with ball, pin, and flag"""
    # Solid dark green background (no gradient)
    background = Image.new('RGBA', (size, size), (20, 80, 20, 255))
    draw = ImageDraw.Draw(background, 'RGBA')
    
    scale = size / 512
    
    # ===== PUTTING GREEN =====
    green_center_x = int(220 * scale)  # Shifted left
    green_center_y = int(350 * scale)  # Shifted down
    green_radius_x = int(180 * scale)
    green_radius_y = int(150 * scale)
    
    # Irregularly shaped putting green (polygon instead of ellipse)
    green_points = [
        (green_center_x - int(160*scale), green_center_y - int(120*scale)),  # Top left
        (green_center_x - int(180*scale), green_center_y + int(20*scale)),   # Left middle
        (green_center_x - int(140*scale), green_center_y + int(130*scale)),  # Bottom left
        (green_center_x + int(120*scale), green_center_y + int(140*scale)),  # Bottom right
        (green_center_x + int(180*scale), green_center_y + int(40*scale)),   # Right middle
        (green_center_x + int(160*scale), green_center_y - int(100*scale)),  # Top right
        (green_center_x + int(80*scale), green_center_y - int(140*scale)),   # Top middle
    ]
    draw.polygon(green_points, fill=(100, 200, 100, 255), outline=(70, 160, 70, 255))
    
    # ===== SAND BUNKERS =====
    # Upper left bunker (made bigger)
    bunker1_points = [
        (int(20*scale), int(20*scale)),    # Top left corner
        (int(10*scale), int(120*scale)),   # Left edge
        (int(180*scale), int(140*scale)),  # Bottom right
        (int(200*scale), int(80*scale)),   # Right edge
        (int(120*scale), int(30*scale)),   # Top right
    ]
    draw.polygon(bunker1_points, fill=(210, 180, 140, 255), outline=(180, 150, 110, 255))
    
    # Upper right bunker
    bunker2_points = [
        (int(380*scale), int(40*scale)),
        (int(420*scale), int(60*scale)),
        (int(480*scale), int(50*scale)),
        (int(460*scale), int(80*scale)),
        (int(400*scale), int(90*scale)),
    ]
    draw.polygon(bunker2_points, fill=(210, 180, 140, 255), outline=(180, 150, 110, 255))
    
    # ===== PIN & FLAG =====
    pin_x = int(360 * scale)
    pin_base_y = int(340 * scale)
    pin_top_y = int(120 * scale)
    
    # Pin pole (thin brown/black stick)
    pin_width = int(3 * scale)
    draw.rectangle([pin_x - pin_width, pin_top_y, pin_x + pin_width, pin_base_y],
                   fill=(60, 40, 20, 255), outline=(40, 20, 0, 255))
    
    # Flag (red triangle) - wide base attached to pole
    flag_width = int(80 * scale)
    flag_height = int(60 * scale)
    flag_points = [
        (pin_x + int(2*scale), pin_top_y),  # Top point on pole
        (pin_x + int(2*scale), pin_top_y + flag_height),  # Bottom point on pole
        (pin_x + flag_width, pin_top_y + flag_height // 2)  # Outer point
    ]
    draw.polygon(flag_points, fill=(220, 30, 30, 255), outline=(180, 20, 20, 255))
    
    # Add shine/gradient to flag
    shine_points = [
        (pin_x + int(15*scale), pin_top_y + int(15*scale)),
        (pin_x + int(50*scale), pin_top_y + flag_height // 2),
        (pin_x + int(35*scale), pin_top_y + int(35*scale))
    ]
    draw.polygon(shine_points, fill=(255, 100, 100, 100), outline=None)
    
    # White number "9" on the flag
    try:
        # Try to use a system font
        font_size = int(40 * scale)
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    text_x = int(pin_x + flag_width * 0.25)  # Moved left within flag
    text_y = int(pin_top_y + flag_height * 0.6)  # Moved down within flag
    
    # Draw white "9"
    draw.text((text_x, text_y), "9", fill=(255, 255, 255, 255), font=font, anchor="mm")
    
    # ===== GOLF BALL =====
    ball_x = int(200 * scale)
    ball_y = int(280 * scale)
    ball_radius = int(35 * scale)
    
    # White ball with shadow
    draw.ellipse([ball_x - ball_radius - int(2*scale), ball_y - ball_radius - int(2*scale),
                  ball_x + ball_radius + int(2*scale), ball_y + ball_radius + int(2*scale)],
                 fill=(100, 100, 100, 100), outline=None)
    
    # White ball
    draw.ellipse([ball_x - ball_radius, ball_y - ball_radius,
                  ball_x + ball_radius, ball_y + ball_radius],
                 fill=(255, 255, 255, 255), outline=(200, 200, 200, 100))
    
    # Ball dimples
    for angle in range(0, 360, 60):
        rad = math.radians(angle)
        dx = int(math.cos(rad) * int(20 * scale))
        dy = int(math.sin(rad) * int(20 * scale))
        dimple_r = int(3 * scale)
        draw.ellipse([ball_x + dx - dimple_r, ball_y + dy - dimple_r,
                     ball_x + dx + dimple_r, ball_y + dy + dimple_r],
                    fill=(220, 220, 220, 150), outline=None)
    
    # Highlight on ball
    highlight_r = int(10 * scale)
    draw.ellipse([ball_x - int(10*scale) - highlight_r, ball_y - int(10*scale) - highlight_r,
                  ball_x - int(10*scale) + highlight_r, ball_y - int(10*scale) + highlight_r],
                 fill=(255, 255, 255, 120), outline=None)
        # ===== LARGE TRANSPARENT "C" =====
    try:
        # Try to use a system font
        large_font_size = int(300 * scale)
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", large_font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Position "C" to fill most of the image, moved down and left to surround the ball
    c_x = int(220 * scale)  # Moved left
    c_y = int(300 * scale)  # Moved down
    
    # Draw semi-transparent "C" (white with low opacity)
    draw.text((c_x, c_y), "C", fill=(255, 255, 255, 60), font=font, anchor="mm")
    
    return background

# Generate 192x192 icon
print("Generating 192x192 icon...")
icon_192 = create_golf_putting_icon_hq(192)
icon_192.save('/Users/tom/Documents/GitHub/Caddie/icon-192.png')
print("✓ Created icon-192.png")

# Generate 512x512 icon
print("Generating 512x512 icon...")
icon_512 = create_golf_putting_icon_hq(512)
icon_512.save('/Users/tom/Documents/GitHub/Caddie/icon-512.png')
print("✓ Created icon-512.png")

print("\nIcons updated with putting green, pin, flag, and ball!")
