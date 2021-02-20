"""
Spreadsheet to Files.
Takes text from a spread sheet and puts it into a text file.
The reverse of the spreadsheet to files program which is assumed to have
been done first, so we are removed some extra characters.
"""

import openpyxl, os

# Opens the spreadsheet.
wb = openpyxl.load_workbook('textFilesReverse.xlsx')
sheet = wb.active

# Loops through rows, each will give a new text file as each denotes a
# different file.
for i in range(1,4):
    # Gets text from current row
    words = sheet.cell(row=i, column=1).value
    # Remove the '[' and ']' from the ends
    words = words[2:-2]
    # Remove the characters inbetween the list items that split the lines
    # in the text document, then puts the lines in a list.  We will be
    # entering the new lines ourselves
    words = list(words.split('\\n\', \''))
    # Create a new file and open it
    currentFile = 'newtextfile' + str(i) + '.txt'
    currentFile = open(currentFile, 'w')
    # Loop through each item in the words list, denoting a new line,
    # and writes it to the current text file.
    for j in range(len(words)):
        currentline = words[j]
        currentFile.write(words[j] + '\n')
    currentFile.close()