"""
Debugging Coin Toss.
Just a way of debugging the coin toss, see the comments for the changes.
"""

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # this can disable the debugging
logging.debug('Start of program')

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug(guess)
toss = random.randint(0, 1) # 0 is tails, 1 is heads
# Need to assign toss to heads of tails!
if toss == 0: 
    toss = 'heads'
else:
    toss = 'tails'
logging.debug(toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # Need to spell guess with two 's', not three!
    guess = input()
    logging.debug(guess)
    # Need to assign a new toss to the coin, not use the same as before!
    toss = random.randint(0, 1)
    logging.debug(toss)
    if toss == 0:
        toss = 'heads'
    else:
        toss = 'tails'
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')