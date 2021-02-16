"""
Gap Filler.
Finds all files with a given prefix, locates gaps in the numbering
(e.g. spam001.txt, spam003.txt) and fills them in with empty files.
Note: This was my own variant.  Probably a pointless variant, mind.
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
# Also, nest-geddon, I apologise.
for folderName, subFolders, filenames in os.walk('C:\\Users\\username\\files'):
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
            filestoAdd = numTotal - gapCheck # this checks how big the gap is
            # and therefore how many files to add
            for i in range(filestoAdd):
                # Checks if the char length of gapCheck plus i is less than
                # the char length of the post-gap filename
                # e.g. if the gap crosses a 9/10 boundary.
                # If so, need to add a 0 to the filename so its the same
                # number of characters e.g. spam009.txt
                if len(str(gapCheck + i)) < len(str(numTotal)):
                    newFile = mo.group(1) + '0' + str(gapCheck + i) + mo.group(7)
                    newName = "C:\\Users\\username\\files\\" + \
                        mo.group(1) + '0' + str(gapCheck + i) + mo.group(7)
                    print('No file for ' + newFile + \
                        ' found, new file created at ' + newName + '.')
                    p = open(f'{newName}', 'w')
                else:
                    # Puts together a new file name
                    newFile = mo.group(1) + str(gapCheck + i) + mo.group(7)
                    newName = "C:\\Users\\username\\files\\" + \
                        mo.group(1) + str(gapCheck + i) + mo.group(7)
                    print('No file for ' + newFile + \
                        ' found, new file created at ' + newName + '.')
                    p = open(f'{newName}', 'w')
            gapCheck = numTotal + 1 # increments to 1 after the filename
        else:
            gapCheck = numTotal + 1 # increments to 1 after the filename
