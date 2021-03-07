"""
Read a Text Field.
Use pyautogui to copy text from an open notepad file
and print it in the program.
"""

import pyautogui, pyperclip

notepad = pyautogui.getWindowsWithTitle('Notepad') # finds notepad window
ntop = notepad[0].top # gets top coordinate
nleft = notepad[0].left # gets left coordinate

# moves to text area of notepad
pyautogui.moveTo(nleft + 200, ntop + 200, duration=0.25)
notepad[0].activate()

pyautogui.hotkey('ctrl', 'a') # highlights all text
pyautogui.hotkey('ctrl', 'c') # copies text to clipboard
pastey = pyperclip.paste() # gets text
print(pastey) # prints text in the program
