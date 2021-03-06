"""
Prettified Stopwatch.
Using rjust() and ljust() to make a stopwatch loop better.
"""

#! python3
# stopwatch.py - A simple stopwatch program.

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. \
Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1
rowZ = []

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = format(round(time.time() -lastTime, 2), '.2f')
        totalTime = format(round(time.time() - startTime, 2), '.2f')
        # justifying the different parts of each stop of the stopwatch
        row = (('Lap #' + str(lapNum) + ':').ljust(10) +
            (str(totalTime)).ljust(10) + ('(' + str(lapTime) + ')').ljust(10))
        print(row, end='')
        lapNum += 1
        lastTime = time.time()
        lastTime = time.time() # reset the last lap time
        rowZ.append(row)
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.') # note: this won't print in Mu as it cancels it itself

# copy it all to the clipboard
rowZ = '\n'.join(rowZ)
pyperclip.copy(rowZ)
