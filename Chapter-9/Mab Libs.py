from pathlib import Path
import re

p = open(Path.cwd() / "MadLibs.txt") # Open text document in current working
#directory, will differ for others
adlib = p.read() # reads text file to variable

# Regex for adjective, noun and verb (in caps!)
adjRegex = re.compile(r'ADJECTIVE')
nounRegex = re.compile(r'NOUN')
verbRegex = re.compile(r'VERB')

# Checks text file for certain words, and if so, replaces with word from user
while adjRegex.search(adlib) != None:
    newadj = input('Please enter an adjective:\n')
    adlib = adjRegex.sub(newadj,adlib,1)
while nounRegex.search(adlib) != None:
    newnoun = input('Please enter a noun:\n')
    adlib = nounRegex.sub(newnoun,adlib,1)
while verbRegex.search(adlib) != None:
    newverb = input('Please enter a verb:\n')
    adlib = verbRegex.sub(newverb,adlib,1)

print(adlib)

# Writes the altered information to a new file in write mode
newFile = open('newAdLibs.txt', 'w')
newFile.write(adlib)
newFile.close()
