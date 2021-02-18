import random

"""
Coin Flips Streaks.
Finds out how often a streak of six heads or six tails comes up in 100 tosses.
"""

numberOfStreaks = 0 # total number of times a streak occured in 10000 tests
horT = 0 # 0 for heads, 1 for tails
horTotal = 0 # total horT within set of 6
aStreakOccured = 0 # variable for storing if a streak occured in 100 flips

for experimentNumber in range(10000): # repeat experiement 10,000 times
    # Code to create list of 100 head or tails values
    flipResultList = []
    for coinFlip in range(100):
        flipChance = random.randint(0, 1) # 50:50 chance
        if flipChance == 0:
            flipResultList.append(0) # 0 is heads, add to list
        else:
            flipResultList.append(1) # 1 is tails, add to list

    # Code that checks if there is a streak of 6 heads or tails in a row
    for streakTest in range(100 - 5): # 100 less 5, as 95-100 is final 6 tosses
        for thisStreak in range(6):
            horT = flipResultList[streakTest + thisStreak] # set of 6
            horTotal += horT
        if horTotal == 0 or horTotal == 6: # if all heads (0) or all tails (6)
            aStreakOccured += 1 # a streak of 6 occured
        horTotal = 0 # resets horTotal
    if aStreakOccured > 0: # if in a test of 100, any amount of streaks occured
        numberOfStreaks += 1 # we are testing existence of 6 in a set of 100
        aStreakOccured = 0 # reset for next test

print('Chance of a streak: %s%%'%(numberOfStreaks/100))
print(numberOfStreaks)
