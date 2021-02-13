"""
HORRIBLE CHESS DICTIONARY VALIDATOR
"""

valcolumns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
valrows = ['1', '2', '3', '4', '5', '6', '7', '8']
valplaces = [] # this will store a list of all the squares on the board
# This will be used to validate that the places of the pieces are real

for x in range(len(valcolumns)): #comines the rows and columns into one list
    for y in range(len(valrows)):
        valplaces.append((valrows[x] + valcolumns[y]))

# Dictionary to state how much of each piece there should be
# wking is White King, brook in Black Rook etc.
onboardpieces = {'wking': 1, 'bking': 1, 'wqueen': 1, 'bqueen': 1,
            'wbishop': 2, 'bbishop': 2, 'wknight': 2, 'bknight': 2,
            'wrook': 2, 'brook': 2, 'wpawn': 8, 'bpawn': 8}
# These are places occupied, note that they haven't all been assigned.
onboardplaces = {'wking': '1a', 'bking': '2b', 'wqueen': '3c', 'bqueen': '4d',
            'wbishop': '5e', 'bbishop': '6f', 'wknight': '7g', 'bknight': '8h',
            'wrook': '7h', 'brook': '6g' , 'wpawn': '5f', 'bpawn': '4e'}

# This lets you add some yourself.
while True:
    print('Which piece are you adding? e.g. wrook, bking \
(Or blank to continue):')
    choicepiece = input()
    if choicepiece == '':
        break
    print('What space is it on? e.g 1a, 8h (Or blank to continue):')
    choiceplace = input()
    if choiceplace == '':
        break
    if choicepiece not in onboardpieces: # checks that piece is valid
        print("Woops, not having that... so I'll go with what we already\
 have...")
        break
    onboardplaces[choicepiece] = choiceplace # adds key-value pair to dictionary
    onboardpieces[choicepiece] += 1 # increments added piece

def isValidChessBoard(onboardpieces, onboardplaces):
    """Checks we have the correct amount of pieces!."""
    while True:
        endnow = 0
        for currentplace in onboardplaces.values():
            if currentplace not in valplaces: # Checks is square valid.
                print('Invalid square entered!')
                endnow = 1
                break
        if endnow == 1:
            break
        print('Spaces seem to exist...') # Updates player, spaces exist
        checkfordupes = list(onboardplaces.values())
        if len(checkfordupes) == len(set(checkfordupes)):
            print('No space sharing either...') # Checks if spaces are unique.
        else:
            print('Cannot put two pieces on one space!')
            break
        # These all check the amounts of pieces.
        if onboardpieces.get('wpawn') > 8 or onboardpieces.get('bpawn') > 8:
            print('Too many pawns!')
            break
        elif onboardpieces.get('wrook') > 2 or onboardpieces.get('brook') > 2:
            print('Too many rooks!')
            break
        elif onboardpieces.get('wknight') > 2 or onboardpieces.get('bknight') > 2:
            print('Too many knights!')
            break
        elif onboardpieces.get('wbishop') > 2 or onboardpieces.get('bbishop') > 2:
            print('Too many bishops!')
            break
        elif onboardpieces.get('wqueen') > 1 or onboardpieces.get('bqueen') > 1:
            print('Too many queens!')
            break
        elif onboardpieces.get('wking') < 1 or onboardpieces.get('bking') < 1:
            print('Not enough Kings! Someone has won!')
            break
        else:
            print('Correct numbers! EVERYTHING LOOKS GOOD')
            return True

# Calls the function.
returned = isValidChessBoard(onboardpieces, onboardplaces)
if returned == True:
    print("That was a pain!") # Indeed it was, indeed it was.