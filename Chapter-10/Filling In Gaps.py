"""
Gap Filler.
Finds all files with a given prefix, locates gaps in the numbering
(e.g. spam001.txt, spam003.txt) and fills them in by renaming them.
"""

import os, re, shutil

# for the user to input the prefix
extInput = input('Please provide the prefix to the numbered files:\n') 

# Regex to be used on the file names, which is te prefix, then numbers, then ext
prefixRegex = re.compile(r'^((%s)([0])*)(([1-9])(\d)*)(\.([a-zA-Z]){2,3})+$'%extInput)

gapCheck = 0 # set this to zero.  Basically, if this is less than the current
# file number in the following loop, there is a gap, so the appropriate
# action is taken.

# Walks the folder with your numbered files!
for folderName, subFolders, filenames in os.walk('C:\\Users\\username'):
    for filename in filenames:
        # Checks filename for prefix, if its a match, stores the number
        # at group 4 and converts to an int
        mo = prefixRegex.search(filename)
        if mo != None:
            numTotal = int(mo.group(4))
        else:
            continue # goes to next file if no match

        if gapCheck == 0: 
            gapCheck = numTotal # updates variable to current number on first
            # run through the loop

        if numTotal > gapCheck: # this means there is a gap
            # Checks if the char length of gapCheck plus i is less than
            # the char length of the post-gap filename
            # e.g. if the gap crosses a 9/10 boundary.
            # If so, need to add a 0 to the filename so its the same
            # number of characters e.g. spam009.txt
            if len(str(gapCheck)) < len(str(numTotal)):
                newFile = mo.group(1) + '0' + str(gapCheck) + mo.group(7)
                newName = "C:\\Users\\username\\" + \
                    mo.group(1) + '0' + str(gapCheck) + mo.group(7)
                print('No file for ' + newFile + \
                    ' found, file renamed to ' + newName + '.')
                shutil.move(os.path.abspath(filename), newName)
            else:
                # Puts together a new file name
                newFile = mo.group(1) + str(gapCheck) + mo.group(7)
                newName = "C:\\Users\\username\\" + \
                    mo.group(1) + str(gapCheck) + mo.group(7)
                print('No file for ' + newFile + \
                    ' found, file renamed to ' + newName + '.')
                shutil.move(os.path.abspath(filename), newName)
            gapCheck += 1 # increments to 1 after the filename
        else:
            gapCheck += 1 # increments to 1 after the filename
