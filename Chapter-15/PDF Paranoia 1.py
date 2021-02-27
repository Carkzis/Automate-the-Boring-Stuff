"""
PDF Paranoia 1.
Goes through every PDF in a dolfer, and its subfolders, and password protects
them.
"""

import PyPDF2, os

# Password entry
pw = input('Please enter a passcode with which to encrypt the PDFs: ')

# Walk through the folder of your choice, change this
for folderName, subfolders, filenames in os.walk('C:\\Users\\username\\folder'):
    for filename in filenames:
        # Looks for pdf file names
        if filename.endswith('.pdf'):
            # Open current file (need to join folder and filenames)
            pdfFile = open(os.path.join(folderName, filename), 'rb')
            # Create pdfReader and pdfWriter objects
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            # Read each page in current pdf and add it to the writer object
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

            # encrypt the current pdfWriter object with the password
            pdfWriter.encrypt(pw)
            # open an output file, and write to it with the pdfWriter object
            pdfOutputFile = open(os.path.join(folderName,
                filename + '_encrypted.pdf'), 'wb')
            pdfWriter.write(pdfOutputFile)

            # close the encrypted file, and the original file
            pdfOutputFile.close()
            pdfFile.close()

            # Open file and check if it is encrypted
            pdfCheck = PyPDF2.PdfFileReader(open(os.path.join(folderName,
                filename + '_encrypted.pdf'), 'rb'))
            if pdfCheck.isEncrypted == True:
                if pdfCheck.decrypt(pw) == 0: # 0 means decryption failed
                    print('Decryption failed...')
                else: # delete original file if the decryption was successful
                    print('Deleting original unencrypted file... (' +
                        filename + ')')
                    os.remove(os.path.join(folderName, filename))
            else:
                print('There was an issue encrypting ' + filename + '.')
