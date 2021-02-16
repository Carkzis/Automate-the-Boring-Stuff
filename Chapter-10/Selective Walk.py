"""
Selective Walk.
Copies any file in a directory with a user-define file extension
and puts it in a new folder.
"""


import os, re, shutil

# Create a regex for any extension with 2 or 3 characters (non-numerical)
extensionRegex = re.compile(r'\.([a-zA-Z]){2,3}')

while True:

    # Takes a user-defined file extension
    extInput = input('Please enter a file extension:\n')

    mo = extensionRegex.search(extInput)

    # Checks if a genuine file extension was given
    if mo == None:
        print('That is not a file extension!')
    else:
        print('That will do.')
        break

# Walks a folder tree
for folderName, subFolders, filenames in os.walk('C:\\Users\\username\\files'):
    print('Checking ' + folderName + ' for ' + extInput + ' files.')
    print(folderName)
    if folderName.endswith('copies'):
        continue
    for filename in filenames:
        if filename.endswith(extInput):
            copiedFile = folderName + '\\' + filename
            # Sends copied files to a new folder.
            shutil.copy(copiedFile,'C:\\Users\\username\\copies')
