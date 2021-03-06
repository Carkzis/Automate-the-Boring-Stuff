"""
Random Chore Assignment Emailer.
Email a random list of chores once a week, scheduled using the Windows
scheduler.
"""

import ezgmail, random, openpyxl
from datetime import date
ezgmail.init()

# The chores are stored in chores.xlsx, with the first column (A)
# being holding the names, which will go into the slaves list.
# Column B has the email addresses
# Columns C+ have the weeks
wb = openpyxl.load_workbook('chores.xlsx')
sheet = wb.active
slaves = [] # stores the individuals
lastAssignDict = {} # dictionary for individuals and their previous chore
emailDict = {} # dictionary for individuals and their emails

# Loops to get each row of individuals and their previous chore (last column)
for r in range(2, sheet.max_row + 1):
    thisSlave = sheet.cell(row=r, column=1).value
    lastChore = sheet.cell(row=r, column=sheet.max_column).value
    slaves.append(thisSlave)
    lastAssignDict[thisSlave] = lastChore
    emailDict[thisSlave] = sheet.cell(row=r, column=2).value

# Store a list of chores, and a copies of the chores and slaves lists
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
choresoriginal = list(chores)
slavesoriginal = list(slaves)

# Dictionary for new chore assignments
newAssignDict = {}
dupChore = True

# Loop for assigning chores
while dupChore == True:
    # randomly assign chores
    for i in range(len(chores)):
        randomChore = random.choice(chores)
        randomSlave = random.choice(slaves)
        chores.remove(randomChore) # this chore is now taken, so remove it
        slaves.remove(randomSlave)
        newAssignDict[randomSlave] = randomChore
    # test for if someone got same chore twice, if they have, redo the loop
    for k, v in newAssignDict.items():
        if newAssignDict[k] != lastAssignDict[k]:
            dupChore = False
        elif newAssignDict[k] == lastAssignDict[k]:
            dupChore = True
            chores = list(choresoriginal)
            slaves = list(slavesoriginal)
            break
        
# Update spreadsheet
today = date.today()
# Label the next column with the date
sheet.cell(row=1, column=sheet.max_column+1).value = today.strftime("%d/%m/%Y")
# Loop through dictionary of people with their new chore, and send
# them an email with the relevant information
for rowNum in range(2, sheet.max_row + 1):
    slaveName = sheet.cell(row=rowNum, column=1).value
    if slaveName in newAssignDict:
        sheet.cell(row=rowNum, column=sheet.max_column).value = newAssignDict[slaveName]
        email = emailDict[slaveName]
        ezgmail.send(email,'Chore Assignment!',
        'Your random chore:' + newAssignDict[slaveName] +
            '. Please do it, slave!')
wb.save('chores.xlsx')    

# Set up task scheduler, use Task Scheduler for windows, with a .bat file.
