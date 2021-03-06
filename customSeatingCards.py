"""
Custom Seating Cards.
Instead of creating a Word document for the invites, we will use images!
"""

import os
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Open guest file, get the amount of guests from it
guestFile = open(Path.cwd() / 'guests.txt')
guestList = guestFile.readlines()
guestNum = len(guestList)

# Set parameters and total height dependent on guest number
setWidth = 288
setHeight = 360
totalHeight = guestNum * setHeight # the total height will be the number
# of guests multiplied by the height of an individual image
background = 'flower.png' # flowers are used for the background

# Open flowery background
flowerIm = Image.open(background)
flowerIm = flowerIm.resize((setWidth,setHeight))
flowerDraw = ImageDraw.Draw(flowerIm)
flowerWidth, flowerHeight = flowerIm.size
flowerDraw.line([
    (0,0),
    (flowerWidth,0),
    (flowerWidth,flowerHeight),
    (0,flowerHeight),
    (0,0)
    ],
    'black', width=10) # outline of image (a square border)
flowerCopy = flowerIm.copy() # get a copy of the image
flowerIm.save('flowery.png') # save the image

# Get fonts to use in the images
fontsFolder = 'C:\\Windows\\Fonts'
brushFont = ImageFont.truetype(os.path.join(fontsFolder, 'BRUSHSCI.TTF'), 12)
timesFont = ImageFont.truetype(os.path.join(fontsFolder, 'times.ttf'), 16)
# A smaller times new roman font:
stimesFont = ImageFont.truetype(os.path.join(fontsFolder, 'times.ttf'), 14)

currentGuest = 0 # this is the index start point for the guests in
# guestList

# Open new file with a height allowing for every invite
im = Image.new('RGBA', (setWidth,totalHeight), 'white')
# loops through different invites of the image, by increasing by an
# single invite image height with each iteration
# then, updates invite with the relevant formatted text
for top in range(0, totalHeight, setHeight):
    # top relates to top pixel of current invite, so the text updates are
    # relative to it
    im.paste(flowerCopy, (0, top))
    draw = ImageDraw.Draw(im)
    draw.text((10,top + 20),
        'It would be a pleasure to have the company of',
        fill='black', font=brushFont)
    draw.text((10,top + 40),
        guestList[currentGuest], fill='black', font=timesFont)
    draw.text((10,top + 60),
        'at 11010 Memory Lane on the Evening of', fill='black', font=brushFont)
    draw.text((10,top + 80),
        'April 1st', fill='black', font=stimesFont)
    draw.text((10,top + 100), 'at 7 o\' clock', fill='black', font=brushFont)
    currentGuest += 1

# Save the image which will have every invite, one after the other
im.save('everything.png')