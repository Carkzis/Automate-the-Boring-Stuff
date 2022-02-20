"""
Instant Messenger Bot.
Use a GUI automation tool to talk to friends on Google Hangouts.
This won't check for whether someone is online, but it wouldn't take too
much extra code to check whether this is the case.
"""

import webbrowser, pyautogui, sys

# Get the recipients email address
email = input('Please enter the recipients email address: ')
message = input('Please enter the message: ')

# Opens a web browser
webbrowser.open('https://hangouts.google.com/')

# Wait for page to load
pyautogui.sleep(10) 

# Check whether the new convo button can be found on the page and clicked on
try:
    pyautogui.click('newconvo.png') # An image file for the new convo button
except:
    print('New conversation button could not be found.')
    sys.exit()

# Write out the email address, and move down 180 pixels and click to proceed
# This may not work depending on changes to the layout, or different screens
# but I am testing different ways of moving about
pyautogui.write(email,0.1)
pyautogui.move(0,180)
pyautogui.sleep(1)
pyautogui.click()
pyautogui.sleep(2)

# Check whether the message box can be found, exit if not found
try:
    pyautogui.click('mpic.png') # this clicks the message box
    # this will delete the hint that is in the message box
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('delete')
except:
    print('Message field could not be found.')
    sys.exit()

pyautogui.write(message,0.1)
pyautogui.sleep(1)

# checks to see if the send button is greyed out
try: 
    pyautogui.click('mno.png') # this is a greyed out button! 
except:   
    print('Message isn\'t typing! Check it out!')
    sys.exit()
else:
    print('Message typed.')
 
pyautogui.sleep(3)

try:
    pyautogui.click('myes.png') # clicks send button
    print('Message sent!')
except:
    print('Couldn\'t send the message.')
