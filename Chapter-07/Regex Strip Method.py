import re, time

"""
Regex Version of strip() Method.
Using regexes to strip ends of a string! Prefer strip() I have to say...
"""

def stripThis(stringy, remchar):
    """Strips characters from a string."""
    if remchar == '': # if no characters entered to be removed: 
        stripRegexStart = re.compile(r'^\s*')
        newstringy = stripRegexStart.sub('', stringy) # add whitespace to start
        stripRegexEnd = re.compile(r'\s*$')
        newstringy = stripRegexEnd.sub('', newstringy) # add whitespace to end
        return newstringy
    else:
        stripRegex = re.compile(remchar) # regex for the character to remove
        mo = stripRegex.search(stringy)
        newstringy = stripRegex.sub('', stringy) # substitutes character to
        # remove with whitespace
        return newstringy

print('Enter a string to strip:')
inputString = input()
print('Enter character to strip:')
remChar = input()
print(remChar)

result = stripThis(inputString, remChar) # calls strip function
print(result)
