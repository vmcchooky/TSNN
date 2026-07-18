import os
import glob
from PIL import Image, ImageDraw

def round_image(file, rad):
    im = Image.open(file).convert("RGBA")
    
    # Create a completely black mask (transparent)
    mask = Image.new('L', im.size, 0)
    draw = ImageDraw.Draw(mask)
    
    # Draw a solid white rounded rectangle (opaque)
    # PIL's rounded_rectangle draws up to x1, y1 inclusive.
    draw.rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), radius=rad, fill=255)
    
    # Create a white background image
    bg = Image.new("RGB", im.size, (255, 255, 255))
    
    # Paste the original image onto the white background using the rounded mask
    bg.paste(im, (0, 0), mask)
    
    bg.save(file, format="PNG")

for file in glob.glob('../img/ui_*.png'):
    print(f"Processing {file}...")
    round_image(file, 24)
print("Done!")
