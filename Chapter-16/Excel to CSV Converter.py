"""
Excel to CSV Converter.
Convert Excel spreadsheets in a directory into CSV files!
"""

import os, openpyxl, csv

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue
    else:
        wb = openpyxl.load_workbook(excelFile)
    # Loop through every sheet in the workbook.
    for sheetName in wb.get_sheet_names():
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        excelLess = os.path.splitext(excelFile)[0]
        outputFile = open(excelLess + '_' + sheetName + '.csv', 'w', newline='')

        # Create the csv.writer object for this CSV file.
        outputWriter = csv.writer(outputFile)

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []    # append each cell to this list
            # TODO: Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)

            # Write the rowData list to the CSV file.out
            outputWriter.writerow(rowData)

        outputFile.close()
