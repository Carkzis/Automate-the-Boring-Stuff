"""
2048.
Play the game automatically using selenium!
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
import time, sys
# Open 2048 website with selenium
browser = webdriver.Firefox()
browser.get('https://play2048.co/')

# Find the element for the page!
htmlElem = browser.find_element_by_tag_name('html')

# Sets a start time, this sets a start time, to ensure restart button
# is clicked every so often
timestart = time.time()

# Loops many times! Just keep playing! Just not forever.
for i in range(1000000):
    timecheck = time.time() # checks the time since timestart
    if (int(timecheck - timestart) % 10) == 0: # if its divisible by 10s,
        # attempt to click the restart button, changes it to integer or it
        # needs to be REAL specific
        newgameElem = browser.find_element_by_class_name('restart-button')
        newgameElem.click()
    else:
        # Go up down left right repeatedly!
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)


