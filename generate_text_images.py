#!/usr/bin/env python3
"""Render name and title as PNG images using the Poppins font."""
import os
import requests
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = "/home/user/signature/icons"
FONT_DIR = "/home/user/signature/fonts"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(FONT_DIR, exist_ok=True)

# Download Poppins font files from Google Fonts
FONTS = {
    "Poppins-Regular.ttf": "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Regular.ttf",
    "Poppins-Thin.ttf": "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Thin.ttf",
}

for name, url in FONTS.items():
    path = os.path.join(FONT_DIR, name)
    if not os.path.exists(path):
        print(f"Downloading {name}...")
        r = requests.get(url)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)
        print(f"  Saved to {path}")

# ── Render "Maria M. Ashtor" in Poppins Regular ──────────────────
font_regular = ImageFont.truetype(os.path.join(FONT_DIR, "Poppins-Regular.ttf"), 72)
text_name = "Maria M. Ashtor"

bbox = font_regular.getbbox(text_name)
text_w = bbox[2] - bbox[0] + 10
text_h = bbox[3] - bbox[1] + 10

img = Image.new("RGBA", (text_w, text_h + 16), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)
draw.text((-bbox[0] + 5, -bbox[1] + 8), text_name, fill="black", font=font_regular)
img.save(os.path.join(OUT_DIR, "name_text.png"))
print(f"Name image: {text_w}x{text_h + 16}")

# ── Render "B2B Sales" in Poppins Thin with letter spacing ───────
font_thin = ImageFont.truetype(os.path.join(FONT_DIR, "Poppins-Thin.ttf"), 40)
text_title = "B2B Sales"
letter_spacing = 10

total_w = 0
for ch in text_title:
    cb = font_thin.getbbox(ch)
    total_w += (cb[2] - cb[0]) + letter_spacing
total_w -= letter_spacing
total_w += 20

title_bbox = font_thin.getbbox(text_title)
title_h = title_bbox[3] - title_bbox[1] + 20

img2 = Image.new("RGBA", (total_w, title_h + 10), (255, 255, 255, 0))
draw2 = ImageDraw.Draw(img2)

x_cursor = 10
for ch in text_title:
    cb = font_thin.getbbox(ch)
    draw2.text((x_cursor - cb[0], -title_bbox[1] + 5), ch, fill="black", font=font_thin)
    x_cursor += (cb[2] - cb[0]) + letter_spacing

img2.save(os.path.join(OUT_DIR, "title_text.png"))
print(f"Title image: {total_w}x{title_h + 10}")

print("Done! Text images generated with Poppins Regular + Thin.")
