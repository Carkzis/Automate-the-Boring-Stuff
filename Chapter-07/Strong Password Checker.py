import re
import time

"""
Strong Password Checker.
Checks a password is > 8 character, contains both upper and lowercase, has
one digit.
"""

def passwordCheck(dataInput):
    """Applies multiple regexes to argument provided by member."""
    pwRegexlength = re.compile(r'.{8,}')
    pwRegexnum = re.compile(r'[\d]+')
    pwRegexlow = re.compile(r'[a-z]+')
    pwRegexup = re.compile(r'[A-Z]+')

    mo = pwRegexlength.search(dataInput)
    mo2 = pwRegexnum.search(dataInput)
    mo3 = pwRegexlow.search(dataInput)
    mo4 = pwRegexup.search(dataInput)

    tryagain = False # sets a tryagain flag

    # If any of the regexes fail, the password doesn't meet the requirements.
    if mo == None or mo2 == None or mo3 == None or mo4 == None:
        print('Your password is not good! Try again:')
        tryagain = True # gets set to True, and the loop that calls the
        # function starts again, asking for a new password
    else:
        print('Password accepted and sent to Marc Jowett! :)')
        time.sleep(3)
        print('Just kidding...')
    return tryagain

# Entry for user provided password.
print('Enter new password (at least 8 characters with at least one\
 uppercase letter, lowercase letter and number:')
while True:
    dataInput = input()
    youShallNotPass = passwordCheck(dataInput)
    if youShallNotPass == False: # if function returns False, programme ends.
        break
