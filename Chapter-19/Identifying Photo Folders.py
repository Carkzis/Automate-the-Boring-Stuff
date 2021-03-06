"""
Identifying Photo Folders.
This will identify any folder that is more than 50% images, pngs and jpgs,
and at least 500x500 pixels in size.
"""

import os
from PIL import Image


# walk through the folders
for foldername, subfolders, filenames in os.walk('C:\\Users\\user'):
    # set the number of photo and non-photo files to zero for current
    # folder
    numPhotoFiles = 0
    numNonPhotoFiles = 0

    # loop through files in the folder
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.lower().endswith('.png') or
            filename.lower().endswith('.jpg')):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        im = Image.open(foldername + '\\' + filename)
        width, height = im.size

        # Check if width & height are larger than 500.
        if width > 100 and height > 100: # changed to capture more of them
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(foldername)
