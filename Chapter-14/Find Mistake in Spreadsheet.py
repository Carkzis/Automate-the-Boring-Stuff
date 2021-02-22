"""
Find the Mistake in the Spreadsheet.
Self-explanatory.
"""

import ezsheets

ss = ezsheets.Spreadsheet('SPREADSHEET') # use your Google form spreadsheet

# Get the google spreadsheet, and column C and put in colC variable
# Column C has the error we are looking for
colC = ss[0].getColumn('C')

# Search through each row on column C, and if column C is equal to
# column A * column B, move to the next cell, otherwise, tell the user
# that there was an error and on with row it was
for i in range(2, len(colC)):
    if (int(ss[0].getRow(i)[0]) *
        int(ss[0].getRow(i)[1]) == int(ss[0].getRow(i)[2])):
        continue
    else:
        print('There is a mistake at row ' + str(i))
        break
