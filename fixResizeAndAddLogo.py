"""
Fix the Resize and Add Logo Program.
Resizes all images in current working directory to fit in a 300x300 square,
and adds catlogo.png to the lower-right corner. Now has gif and png,
in multiple cases, and makes the logo in the corner proportional.
"""

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

# Open the logo and resize to 100x100.
logoIm = Image.open(LOGO_FILENAME)
logoIm = logoIm.resize((100,100))
logoWidth, logoHeight = logoIm.size # gets the width and height from the size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not ((filename.lower().endswith('.png') or
        filename.lower().endswith('.jpg') or
        filename.lower().endswith('.gif') or
        filename.lower().endswith('.bmp') or filename == LOGO_FILENAME)):
        continue # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            # if you divide 300 by the width you get a multiplier less than
            # one, as width is over 300. If you multiply this multiplier
            # by width you get 300. As height is less than width, when the
            # multiplier is multiplied by height it will
            # always be less than 300.
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        im = im.resize((width, height))

    # If the logo if more than half the width or the height of the image,
    # skip adding the logo.
    if (logoWidth * 2) > width or (logoHeight * 2) > height:
        continue

    # Add the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    # third argument shapes the paste with transparency

    # Save changes.
    im.save(os.path.join('withLogo', filename))