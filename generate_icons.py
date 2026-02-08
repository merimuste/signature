#!/usr/bin/env python3
"""Generate icon PNGs using Google Material Icons font."""
import os
import requests
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = "/home/user/signature/icons"
FONT_DIR = "/home/user/signature/fonts"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(FONT_DIR, exist_ok=True)

# Download Google Material Icons font (filled variant)
MATERIAL_URL = "https://github.com/google/material-design-icons/raw/master/font/MaterialIcons-Regular.ttf"
MATERIAL_OUTLINED_URL = "https://github.com/google/material-design-icons/raw/master/font/MaterialIconsOutlined-Regular.otf"

for url, name in [(MATERIAL_URL, "MaterialIcons-Regular.ttf"),
                  (MATERIAL_OUTLINED_URL, "MaterialIconsOutlined-Regular.otf")]:
    path = os.path.join(FONT_DIR, name)
    if not os.path.exists(path):
        print(f"Downloading {name}...")
        r = requests.get(url)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)
        print(f"  Saved to {path}")

# Material Icons codepoints:
# phone        = \ue0cd
# mail         = \ue158
# language     = \ue894 (globe icon)

SIZE = 200
font_filled = ImageFont.truetype(os.path.join(FONT_DIR, "MaterialIcons-Regular.ttf"), 160)
font_outlined = ImageFont.truetype(os.path.join(FONT_DIR, "MaterialIconsOutlined-Regular.otf"), 160)

icons = {
    "phone_icon.png": ("\ue0cd", font_filled, True),    # phone in filled circle
    "email_icon.png": ("\ue158", font_filled, False),    # mail/envelope
    "globe_icon.png": ("\ue894", font_outlined, False),  # language/globe outlined
}

for filename, (char, font, needs_circle) in icons.items():
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if needs_circle:
        # Draw black circle background for phone icon
        draw.ellipse([4, 4, SIZE - 4, SIZE - 4], fill="black")
        # Render white phone icon centered
        bbox = font.getbbox(char)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (SIZE - w) / 2 - bbox[0]
        y = (SIZE - h) / 2 - bbox[1]
        draw.text((x, y), char, fill="white", font=font)
    else:
        # Render black icon centered
        bbox = font.getbbox(char)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (SIZE - w) / 2 - bbox[0]
        y = (SIZE - h) / 2 - bbox[1]
        draw.text((x, y), char, fill="black", font=font)

    img.save(os.path.join(OUT_DIR, filename))
    print(f"Created {filename}")

print("All Google Material Icons generated!")
