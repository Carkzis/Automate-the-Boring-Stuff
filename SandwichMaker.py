"""
Sandwich Maker.
Make a sandwich, and gives you the price! And checks your entries.
"""

import pyinputplus as pyip

# Creates a dictionary with the sandwich items and their prices.
prices = {'wheat': 1.50, 'white': 1.00, 'sourdough': 2.00,
        'chicken': 3.50, 'turkey': 4.50, 'ham': 1.50, 'tofu': 2.00,
        'cheddar': 3.00, 'Swiss': 4.00, 'mozzarella': 2.50,
        'mayo': 0.25, 'mustard': 0.20, 'lettuce': 0.15, 'tomato': 0.35}

print("---Marc Jowett's Sandwich Maker---")
sandwichList = [] # Creates a list to hold the items in your sandwich.

# The following asks for your input regarding different items.
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'],\
    'Please choose a bread:\n')
sandwichList.append(bread)

protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu', 'none'], \
    prompt='Please choose a protein:\n', limit=1, default='none')
print(protein.title() + ' it is.')
sandwichList.append(protein)

cheeseYesNo = pyip.inputYesNo('Would you like cheese:\n', limit=1, default='no')
if cheeseYesNo == 'yes':
    print('I bet you would.')
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella', 'none'],\
         prompt='Please choose a cheese:\n', limit=1, default='none')
    print(cheese.title() + ' it is.')
    sandwichList.append(cheese)
else:
    print('No cheese it is.')
    sandwichList.append('none')

mayoYesNo = pyip.inputYesNo('Mayo?\n', limit=1, default='no')
if mayoYesNo == 'yes':
    sandwichList.append('mayo')
else:
    print('No mayo it is.')
    sandwichList.append('none')

mustardYesNo = pyip.inputYesNo('Mustard?\n', limit=1, default='no')
if mustardYesNo == 'yes':
    sandwichList.append('mustard')
else:
    print('No mustard it is.')
    sandwichList.append('none')

lettuceYesNo = pyip.inputYesNo('Lettuce?\n', limit=1, default='no')
if lettuceYesNo == 'yes':
    sandwichList.append('lettuce')
else:
    print('No lettuce it is.')
    sandwichList.append('none')

tomatoYesNo = pyip.inputYesNo('Tomato?\n', limit=1, default='no')
if tomatoYesNo == 'yes':
    sandwichList.append('tomato')
else:
    print('No tomato it is.')
    sandwichList.append('none')

# Asks how many sandwiches, a multiple of what you asked for.
sandwichNo = pyip.inputInt(prompt='How many delicious sandwiches?\n', min=1)

totalPrice = 0.00
finalwich = [] # this will store a sandwich without any "none" items

# Goes through items in the sandwich list
for i in range(len(sandwichList)):
    if sandwichList[i] == 'none': # note: string of none, not boolean
        continue
    else:
        totalPrice += prices[sandwichList[i]] # searches dict, adds relevant
        # price to total
        finalwich.append(sandwichList[i])

totalPrice *= sandwichNo # multiplies price by sandwhich number

# Final output of items in the sandiwch, and the total cost.
print('So you asked for a sandwich with:')
for i in range(len(finalwich)):
    print(finalwich[i].title())
print('This comes to £' + "{:.2f}".format(totalPrice) + '. Pay now, or else.')
