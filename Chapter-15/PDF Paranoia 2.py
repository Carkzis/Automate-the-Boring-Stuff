"""
PDF Paranoia 2.
Finds all encrypted PDFs in a folder and attempts to decrypt them.
"""

import PyPDF2, os

# Gets a password to from the member that will be used to attempt decryptions
pw = input('Please enter a passcode with which to decrypt\
the any encrypted PDFs: ') # hello1 in this case

# Walk through the folder of your choice, change this
for folderName, subfolders, filenames in os.walk('C:\\Users\\username\\folder'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            # Gets reader object
            pdfReader = PyPDF2.PdfFileReader(open(os.path.join(folderName,
                filename), 'rb'))
            # If the PDF is encrypted, notifies user, otherwise moves
            # to the next file
            if pdfReader.isEncrypted == True:
                print('Found encrypted file:  ' + filename)
            else:
                continue

            # Attempts decryption
            print('Decrypting...')
            dcheck = pdfReader.decrypt(pw)

            # Notifies user if the decryption of the current file was
            # successful
            if dcheck == 0:
                print('Decryption failed...')
                continue
            else:
                print('Decrypting successful.')

            # If decryption was successful, writes PDF to a new,
            # non-encrypted PDF
            newfilename = os.path.join(folderName, filename  + '_decrypted.pdf')
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

            pdfOutputFile = open(newfilename, 'wb')
            pdfWriter.write(pdfOutputFile)

            # Close the destination file
            pdfOutputFile.close()
