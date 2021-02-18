"""
Regex Search.
Takes a user-defined regular expression, and returns any line in any text file
with a match.
"""

from pathlib import Path
import re

# Creates a regex from a user input
userInput = input('Please enter a regular expresssion:\n')
userRegex = re.compile(userInput)

p = Path.cwd()
txtList = list(p.glob('*.txt')) # gets all .txt files in cwd

# Opens each .txt file in txtList, prints the text file and 
for fileObj in txtList:
    p = open(fileObj)
    hitLine = p.readlines() # Gets a list of lines
    print(fileObj)
    for i in hitLine: # Goes through each line in a file
        lineSearch = userRegex.search(i) # Applies user-created regex
        if lineSearch != None: # If not no match (so, is a match), prints line
            print(i)


