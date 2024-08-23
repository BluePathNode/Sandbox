#requires Pillow PIP INSTALL PILLOW 
from PIL import Image

# Open the WebP file
webp_image = Image.open('drz.webp')

# Convert to GIF
gif_image = webp_image.convert('RGBA')  # Convert to RGBA if needed
gif_image.save('output.gif', 'GIF')

print("Conversion complete. Saved as 'drz.gif'.")
