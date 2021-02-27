"""
Brute Force PDF Password Breaker.
Opens up a PDF by using lots of different passwords.
Use strong passwords!
"""

from pathlib import Path
import PyPDF2

# Opens a dictionary with many different words and reads from it,
# and splits into a list separated by '\n'
dictFile = open(Path.cwd() / 'dictionary.txt')
dictList = dictFile.read()
dictList = dictList.split(sep='\n')

# Opens an encrypted PDF (example used here)
pdfReader = PyPDF2.PdfFileReader(open('meetingminutes1_encrypted.pdf', 'rb'))
# Sets whether the file has been opened yet or not
oPened = False

# First checks if the PDF is encrypted to begin with
if pdfReader.isEncrypted == False:
    print('This file is not encrypted!')
else:
    # Loops through dictList (upper case), checks if decryption is successful
    # and provides the password if so, and breaks out of the loop
    for i in dictList:
        dcheck = pdfReader.decrypt(i)
        print(i)
        if dcheck != 0:
            print('Decryption successful. Password is ' + i + '.')
            oPened = True
            break
        else:
            # tries all the lowercase versions of the passwords
            ilower = i.lower()
            print(ilower)
            dcheck = pdfReader.decrypt(ilower)
            if dcheck != 0:
                print('Decryption successful. Password is ' + ilower + '.')
                oPened = True
                break

# If oPened hasn't changed to True by this line, it hasn't been decrypted
# by the dicitonary
if oPened == False:
    print('PDF could not be decrypted using the current dictionary...')