import re
import time

"""
Date Checker.
Checks that a date is valid, in the format DD/MM/YYYY,
"""

# Requests the date.
print('Enter date (MMDDYYYY):')
dataInput = input()
thirties = ['04', '06', '09', '11']

# Sets the regex.
dateDetectRegex = re.compile(r'([0-2][1-9]|[1-3][0-1])/([0][1-9]\|[1][1-2])/([1-2][0-9][0-9][0-9])')
mo = dateDetectRegex.search(dataInput)
if mo != None: # If it's not none, the date fits, however extra checks needed...
    print('Date entered, validating...')
    time.sleep(3) # Pause for effect :P.
    # Check february has the correct number of days!
    # Assumes leap years is every multiple of four years
    if str(mo[2]) == '02':
        if int(mo[1]) > 29 and int(mo[3]) % 4 == 0:
            print('February only has 29 days in a leap year!')
        elif int(mo[1]) > 28 and int(mo[3]) % 4 != 0:
            print('February only has 28 days in a non-leap year!')
            print(mo[3])
        else:
            print('Congratulations, date validated!!!')
    # Check these months have the correct number of days!
    elif str(mo[2]) in thirties and int(mo[1]) > 30:
        print('This month should only have 30 days!!!')
        print(mo[2])
    else:
        print('Congratulations, date validated!!!')
else:
    print('That is not a date...')