"""
Text Files to Spreadsheet.
Get data from a spreadsheet, and insert it into an Excel file.
"""

import openpyxl, os

# Open a destination work book.
wb = openpyxl.load_workbook('textFiles.xlsx')
sheet = wb.active

# Loops through some textfiles (e.g. textfile3.txt)
for i in range(1, 4):
    currentFile = 'textfile' + str(i) + '.txt'
    # Gets the text from multiple lines using .readlines()
    openedFile = (open(currentFile)).readlines()
    print(openedFile)
    # Converts the list of lines to a string and inserts it into the
    # spreadsheet at the relevent row.
    stringy = str(openedFile)
    sheet.cell(row=i, column=1).value = stringy

# Save the spreadsheet, it did nothing wrong.
wb.save('textFiles.xlsx')
