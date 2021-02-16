"""
Delete Unneeded Files.
Walks a folder, and prints any file of 100KB in size ("deletes").
"""

import os, re, shutil

print('These files are over 100KB:\n')

# Walks a folder
for folderName, subFolders, filenames in os.walk('C:\\Users\\username\\files'):
    for filename in filenames:
        checkfile = folderName + '\\' + filename
        size = os.path.getsize(checkfile)
        if size > 100000: # Checks size in bites
            print(filename + ' ' + str(size)) # print here instead of deleting
            # Unless you really want to...
