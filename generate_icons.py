from PIL import Image, ImageDraw
import math

def create_gradient_circle(draw, center, radius, fill_color, num_rings=20):
    """Create a radial gradient effect by drawing concentric circles"""
    r, g, b, a = fill_color
    for i in range(num_rings, 0, -1):
        ratio = i / num_rings
        # Lighten the color as we go inward
        alpha_blend = int(a * ratio)
        # Adjust brightness for gradient effect
        shade = int(255 * (1 - ratio * 0.3))  # Slight lightening towards center
        color = (min(255, r + (255-r) * (1-ratio) * 0.4), 
                 min(255, g + (255-g) * (1-ratio) * 0.4),
                 min(255, b + (255-b) * (1-ratio) * 0.4),
                 alpha_blend)
        r_i = int(radius * ratio)
        draw.ellipse([center[0]-r_i, center[1]-r_i, 
                     center[0]+r_i, center[1]+r_i], 
                    fill=color, outline=None)

def create_golf_icon_hq(size):
    """Create a high-quality golf icon with gradients and realistic proportions"""
    # Darker, richer green background
    background = Image.new('RGBA', (size, size), (25, 100, 25, 255))
    draw = ImageDraw.Draw(background, 'RGBA')
    
    # Add subtle gradient to background (darker at edges)
    gradient = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    grad_draw = ImageDraw.Draw(gradient, 'RGBA')
    for i in range(size // 2):
        alpha = int(30 * (i / (size // 2)))
        grad_draw.ellipse([i, i, size-i, size-i], 
                         outline=(0, 0, 0, alpha), width=1)
    background.paste(gradient, (0, 0), gradient)
    
    draw = ImageDraw.Draw(background, 'RGBA')
    scale = size / 512
    
    # ===== GOLF BALL =====
    ball_center_x = int(280 * scale)
    ball_center_y = int(310 * scale)
    ball_radius = int(65 * scale)
    
    # Create ball with gradient (white center, gray edges)
    create_gradient_circle(draw, (ball_center_x, ball_center_y), 
                         ball_radius, (255, 255, 255, 255), num_rings=25)
    
    # Ball dimples (concentric pattern for realism)
    dimple_radius = int(6 * scale)
    dimple_spacing = int(32 * scale)
    
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        dx = int(math.cos(rad) * dimple_spacing)
        dy = int(math.sin(rad) * dimple_spacing)
        x = ball_center_x + dx
        y = ball_center_y + dy
        # Draw multiple dimples in a pattern
        for r in [int(4*scale), int(2*scale)]:
            draw.ellipse([x-r, y-r, x+r, y+r], 
                        fill=(200, 200, 200, 180), outline=None)
    
    # Add highlight on ball for glossiness
    highlight_x = ball_center_x - int(20 * scale)
    highlight_y = ball_center_y - int(20 * scale)
    highlight_r = int(15 * scale)
    draw.ellipse([highlight_x - highlight_r, highlight_y - highlight_r,
                 highlight_x + highlight_r, highlight_y + highlight_r],
                fill=(255, 255, 255, 100), outline=None)
    
    # ===== GOLF CLUB =====
    club_start_x = int(150 * scale)
    club_start_y = int(380 * scale)
    
    # Shaft (brown with slight gradient)
    shaft_width = int(14 * scale)
    shaft_length = int(200 * scale)
    shaft_end_x = club_start_x - int(60 * scale)
    shaft_end_y = club_start_y + shaft_length
    
    # Draw shaft with shading using lines
    for i in range(int(shaft_width), 0, -1):
        alpha = int(255 * (i / shaft_width))
        shade = int(101 - 20 * ((shaft_width - i) / shaft_width))
        draw.line([(club_start_x - i//2, club_start_y), 
                  (shaft_end_x - i//2, shaft_end_y)],
                 fill=(shade, 47 + shade//4, 20, alpha), width=int(2*scale))
    
    # Draw main shaft body
    shaft_points = [
        (club_start_x, club_start_y),
        (club_start_x - shaft_width, club_start_y),
        (shaft_end_x - shaft_width, shaft_end_y),
        (shaft_end_x, shaft_end_y)
    ]
    draw.polygon(shaft_points, fill=(101, 67, 33, 255), outline=(70, 45, 20, 200))
    
    # Clubhead (steeper angle, more realistic)
    head_width = int(110 * scale)
    head_height = int(140 * scale)
    
    # Tilted clubface polygon
    head_points = [
        (club_start_x, club_start_y),
        (club_start_x + head_width, club_start_y - int(50 * scale)),
        (club_start_x + head_width - int(20*scale), club_start_y + head_height),
        (club_start_x - int(20*scale), club_start_y + head_height + int(50*scale))
    ]
    
    # Draw clubhead with gradient effect (lighter in center)
    draw.polygon(head_points, fill=(200, 160, 30, 255), outline=(140, 100, 10, 255))
    
    # Add shine/highlight on clubface
    shine_points = [
        (club_start_x + int(20*scale), club_start_y + int(20*scale)),
        (club_start_x + int(70*scale), club_start_y - int(20*scale)),
        (club_start_x + int(80*scale), club_start_y + int(40*scale)),
        (club_start_x + int(40*scale), club_start_y + int(60*scale))
    ]
    draw.polygon(shine_points, fill=(255, 230, 150, 80), outline=None)
    
    return background

# Generate 192x192 icon
print("Generating 192x192 icon...")
icon_192 = create_golf_icon_hq(192)
icon_192.save('/Users/tom/Documents/GitHub/Caddie/icon-192.png')
print("✓ Created icon-192.png")

# Generate 512x512 icon
print("Generating 512x512 icon...")
icon_512 = create_golf_icon_hq(512)
icon_512.save('/Users/tom/Documents/GitHub/Caddie/icon-512.png')
print("✓ Created icon-512.png")

print("\nIcons updated with gradients, realistic proportions, and glossy effects!")
