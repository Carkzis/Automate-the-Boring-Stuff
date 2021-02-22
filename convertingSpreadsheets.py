"""
Converting Google Speadsheets.
Convert excel spreadsheet and download into other formats.
"""

import ezsheets

# Keeps you updated on what the program is doing.
print('Uploading...')
# Upload spreadsheet to Google sheets
ss = ezsheets.upload('C:\\Users\\username\\spreadsheet.xlsx')

# Download spreadsheet into other formats.
print('Downloading as Excel file...')
ss.downloadAsExcel()
print('Downloading as ODS file...')
ss.downloadAsODS()
print('Downloading as CSV file...')
ss.downloadAsCSV()
print('Downloading as TSV file...')
ss.downloadAsTSV()
print('Downloading as PDF file...')
ss.downloadAsPDF()
print('Downloading as HTML file...')
ss.downloadAsHTML()

# Another update!
print('Downloaded as all the formats!')