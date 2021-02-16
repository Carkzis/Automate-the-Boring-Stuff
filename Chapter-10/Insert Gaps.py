"""
Insert Gaps.
Insert a gap at a position of the users choosing (e.g. spam001, gap, spam003).
There was almost certainly an easier way to do this... Week one programming
for you.  Keeping it as it anyway, it was good practice actually working out
what I was thinking!
"""

import os, re, shutil

extInput = input('Please confirm the name of the file for\
where you would like to introduce a gap:\n') # for inputting the file name

# Regex to be used on the file names
prefixRegex = re.compile((r'([a-zA-Z]*)([0])*(([1-9])(\d)*)(\.([a-zA-Z]){2,3})+$'))

# Gets the prefix of the filename before the number (e.g. spam) or None if
# no prefix
sImput = prefixRegex.search(extInput)
if sImput != None:
    prefix = sImput.group(1)
else:
    prefix = None

# Regex using the prefix stored in the prefix variable
totRegex = re.compile(r'^(%s)([0]*)(([1-9])(\d)*)(\.([a-zA-Z]){2,3})+$'%prefix)

# Set up some variables.
isFound = False # is false if there is no such file
fileList = [] # list for storing files with the prefix

# Goes through files until the filename is found, appends any found file to
# a list
for folderName, subFolders, filenames in os.walk('C:\\Users\\username\\files'):
    for filename in filenames:
        mo = totRegex.search(filename)
        if mo != None:
            fileList.append(filename)
        if filename == extInput:
            isFound = True # flag gets changed as file is found
            print('Found! Space made available for ' + extInput)

if isFound == False:
    print('No such file exists...') # Displays if file does not exist
else:
    for i in fileList[::-1]: # file exists, run through list backwards
        # so that we don't overwrite the subsequently numbered files
        # after renaming
        mo = totRegex.search(i)
        num = int(mo.group(3)) # gets group 3, the item number, from file
        num2 = num + 1 # this will be for files moved up by one, after
        # the gap
        oldName = "C:\\Users\\username\\files\\" + i
        newName = "C:\\Users\\username\\files\\" +\
             mo.group(1) + mo.group(2) + str(num2) + mo.group(6) # construct
             # new name
        if len(str(oldName)) < len(str(newName)): # accounts for when a filename
            # is moving from one digit to 2, e.g spam009 to spam010
            newName = "C:\\Users\\username\\files\\" +\
                 mo.group(1) + '0' + str(num2) + mo.group(6)
        shutil.copy(oldName, newName) # copies the file using a numbered
        # name that is one higher.
        print('New file created: ' + newName)
        if extInput == i: # if, after changed the name, the old filename
            # was for that where wanted a gap, we can delete the old file
            # (as it has been copied) and then break out of the loop
            os.unlink(oldName)
            break
