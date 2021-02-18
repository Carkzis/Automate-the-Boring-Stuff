"""
Table Printer.
Makes an organised table from a list of lists.
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

columnWidths = [0] * len(tableData) # creates a list the length of column.
# ie the amount of lists in the tableData list.
maxWidth = 0

# A loop within a loop, to signify a list within a list.
for i in range(len(columnWidths)):
    for i2 in range(len(tableData[i])):
        widthTest = len(tableData[i][i2]) # gets the length of item in list
        if widthTest > columnWidths[i]:
            columnWidths[i] = widthTest # updates column width if highest
    if columnWidths[i] > maxWidth: 
        maxWidth = columnWidths[i] # updates max width if the item width is
        # higher than the previous one, this is for all columns

# These swap the x and y axes and print the value, justified to the right
# using the max width so that all items fit.
for i in range(4):
    for i2 in range(len(tableData)):
        print(tableData[i2][i].rjust(maxWidth), end='')

    print(end="\n")
