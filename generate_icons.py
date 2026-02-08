#!/usr/bin/env python3
"""Generate icon PNGs matching the signature design using SVG -> PNG."""
import cairosvg
import os

OUT_DIR = "/home/user/signature/icons"
os.makedirs(OUT_DIR, exist_ok=True)

PNG_SIZE = 200

# ── Phone icon (black circle with white phone handset) ────────────
phone_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="black"/>
  <path d="M62.5,57.5 C62.5,57.5 67,53 69.5,53 C72,53 77,57.5 77,57.5
           C77,57.5 77,62 74,65 C71,68 63.5,66 57,59.5
           C50.5,53 40.5,43 34.5,37
           C28.5,31 27,24.5 30,21.5 C33,18.5 37.5,18.5 37.5,18.5
           C37.5,18.5 42,23.5 42,26 C42,28.5 37.5,33 37.5,33"
        fill="none" stroke="white" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

cairosvg.svg2png(bytestring=phone_svg.encode(), write_to=os.path.join(OUT_DIR, "phone_icon.png"),
                 output_width=PNG_SIZE, output_height=PNG_SIZE)
print("Phone icon created")

# ── Email icon (black filled envelope with V flap) ───────────────
email_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 75">
  <rect x="2" y="2" width="96" height="71" rx="3" ry="3" fill="black"/>
  <polyline points="2,2 50,42 98,2" fill="none" stroke="white" stroke-width="5" stroke-linejoin="round"/>
  <line x1="2" y1="73" x2="38" y2="40" stroke="white" stroke-width="4"/>
  <line x1="98" y1="73" x2="62" y2="40" stroke="white" stroke-width="4"/>
</svg>'''

cairosvg.svg2png(bytestring=email_svg.encode(), write_to=os.path.join(OUT_DIR, "email_icon.png"),
                 output_width=PNG_SIZE, output_height=int(PNG_SIZE * 0.75))
print("Email icon created")

# ── Globe icon (outlined globe with grid) ─────────────────────────
globe_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <!-- Outer circle -->
  <circle cx="50" cy="50" r="45" fill="none" stroke="black" stroke-width="4"/>
  <!-- Center vertical meridian -->
  <ellipse cx="50" cy="50" rx="18" ry="45" fill="none" stroke="black" stroke-width="3"/>
  <!-- Equator -->
  <line x1="5" y1="50" x2="95" y2="50" stroke="black" stroke-width="3"/>
  <!-- Upper latitude arc -->
  <ellipse cx="50" cy="50" rx="42" ry="18" fill="none" stroke="black" stroke-width="3"
           clip-path="url(#topHalf)"/>
  <!-- Top latitude line (curved) -->
  <path d="M 10,32 Q 50,18 90,32" fill="none" stroke="black" stroke-width="3"/>
  <!-- Bottom latitude line (curved) -->
  <path d="M 10,68 Q 50,82 90,68" fill="none" stroke="black" stroke-width="3"/>
</svg>'''

cairosvg.svg2png(bytestring=globe_svg.encode(), write_to=os.path.join(OUT_DIR, "globe_icon.png"),
                 output_width=PNG_SIZE, output_height=PNG_SIZE)
print("Globe icon created")

print("All icons generated successfully!")
