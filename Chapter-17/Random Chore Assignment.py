import ezgmail, random, openpyxl
from datetime import date
ezgmail.init()

wb = openpyxl.load_workbook('chores.xlsx')
sheet = wb.active
slaves = []
lastAssignDict = {}
emailDict = {}

for r in range(2, sheet.max_row + 1):
    thisSlave = sheet.cell(row=r, column=1).value
    lastChore = sheet.cell(row=r, column=sheet.max_column).value
    slaves.append(thisSlave)
    lastAssignDict[thisSlave] = lastChore
    emailDict[thisSlave] = sheet.cell(row=r, column=2).value

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
choresoriginal = list(chores)
slavesoriginal = list(slaves)

newAssignDict = {}
dupChore = True

while dupChore == True:
    # randomly assign chores
    for i in range(len(chores)):
        randomChore = random.choice(chores)
        randomSlave = random.choice(slaves)
        chores.remove(randomChore) # this chore is now taken, so remove it
        slaves.remove(randomSlave)
        newAssignDict[randomSlave] = randomChore
    # test for if someone got same chore twice
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
sheet.cell(row=1, column=sheet.max_column+1).value = today.strftime("%d/%m/%Y")
for rowNum in range(2, sheet.max_row + 1):
    slaveName = sheet.cell(row=rowNum, column=1).value
    if slaveName in newAssignDict:
        sheet.cell(row=rowNum, column=sheet.max_column).value = newAssignDict[slaveName]
        email = emailDict[slaveName]
        ezgmail.send(email,'Chore Assignment!', 'Your random chore:' + newAssignDict[slaveName] + '. Please do it, slave!')
wb.save('chores.xlsx')    

# Set up task scheduler - would use Task Scheduler for windows, with a .bat file.
