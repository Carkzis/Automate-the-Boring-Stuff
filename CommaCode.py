"""
Comma Code.
Takes a list, returns string separated by commas.
"""

spam = [] # Insert list here.

def seppy(inspam):
    "Function to turn a list into a formatted string."
    # Tells you off if the list is empty.
    if (len(spam)) == 0:
        print("List is empty!")

    for item in range(len(inspam)):
        if item == len(inspam) - 1: # So it is the last one (use item[-1]!)
            print(inspam[item] + '.') # Last item gets a fullstop.
        elif item == len(inspam) - 2: # So it is the second last.
            print(inspam[item] + ' and ',end='') # Last item gets an and.
        else:
            print(inspam[item] + ', ',end='') # The rest get commas.

seppy(spam) # Calls the function.
