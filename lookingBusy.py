"""
Looking Busy.
This will nudge the screen every 10 minutes.
"""

import pyautogui

print('Press CTRL-C to cancel the program.')

while True:
    p = pyautogui.position()
    pyautogui.sleep(600) # sleep for 10 minutes before performing a nudge
    p2 = pyautogui.position()
    if p == p2: # checks if position is the same as 10 min ago, if so, nudge
        print('You are sleepy!')
        pyautogui.move(10, 0, duration=0.25)
    else:
        print('You are energetic!')