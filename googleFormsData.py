"""
Downloding Google Forms Data.
Collect a list of email address from a Google spreadsheet.
""""

import ezsheets

ss = ezsheets.Spreadsheet('SPREADSHEET') # use your Google form spreadsheet
# ID here
# Get the google spreadsheet, and rows
sheet = ss[0]
rows = sheet.getRows()
print(rows)

# Get the 3rd column, that contains the emils
columnThree = sheet.getColumn(3)
print(columnThree)

# if the cell is empty, or it says "Email" meaning it is the title column,
# skip to the next cell in the column, else, print the email
for i in columnThree:
    if i == '' or i == 'Email':
        continue
    else:
        print(i)
