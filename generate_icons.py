from PIL import Image, ImageDraw

def create_golf_icon(size):
    # Green background (forest green)
    img = Image.new('RGBA', (size, size), (34, 139, 34, 255))
    draw = ImageDraw.Draw(img)
    
    # Calculate scaling
    scale = size / 512
    
    # Draw golf ball (white circle with dimples)
    ball_center_x = int(256 * scale)
    ball_center_y = int(320 * scale)
    ball_radius = int(60 * scale)
    
    draw.ellipse(
        [ball_center_x - ball_radius, ball_center_y - ball_radius,
         ball_center_x + ball_radius, ball_center_y + ball_radius],
        fill=(255, 255, 255, 255),
        outline=(200, 200, 200, 255),
        width=int(2 * scale)
    )
    
    # Add dimples to golf ball
    dimple_radius = int(8 * scale)
    for dx in [-25, 0, 25]:
        for dy in [-25, 0, 25]:
            x = ball_center_x + dx * scale
            y = ball_center_y + dy * scale
            draw.ellipse(
                [x - dimple_radius, y - dimple_radius,
                 x + dimple_radius, y + dimple_radius],
                fill=(220, 220, 220, 255)
            )
    
    # Draw golf club (simple clubface)
    club_x = int(180 * scale)
    club_y = int(140 * scale)
    club_width = int(100 * scale)
    club_height = int(120 * scale)
    
    # Club head (clubface - tilted rectangle)
    club_points = [
        (club_x, club_y),
        (club_x + club_width, club_y - int(30 * scale)),
        (club_x + club_width, club_y + club_height),
        (club_x, club_y + club_height + int(30 * scale))
    ]
    draw.polygon(club_points, fill=(184, 134, 11, 255), outline=(139, 100, 0, 255))
    
    # Club shaft
    shaft_width = int(12 * scale)
    shaft_x = club_x - int(40 * scale)
    draw.rectangle(
        [shaft_x, club_y + club_height, shaft_x + shaft_width, club_y + club_height + int(150 * scale)],
        fill=(101, 67, 33, 255),
        outline=(70, 45, 20, 255)
    )
    
    return img

# Generate 192x192 icon
icon_192 = create_golf_icon(192)
icon_192.save('/Users/tom/Documents/GitHub/Caddie/icon-192.png')
print("✓ Created icon-192.png")

# Generate 512x512 icon
icon_512 = create_golf_icon(512)
icon_512.save('/Users/tom/Documents/GitHub/Caddie/icon-512.png')
print("✓ Created icon-512.png")
