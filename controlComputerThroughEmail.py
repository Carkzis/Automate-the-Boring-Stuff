"""
Controlling Your Computer Through Email.
This will check your email account for any instructions for downloading
something using qBittorrent.
"""

import subprocess, ezgmail, re, datetime, time
import logging
logging.basicConfig(
    filename='myProgramLog.txt',
    level=logging.DEBUG,
    format='%(asctime)s -  %(levelname)s -  %(message)s'
    )
ezgmail.init()

# This is where the program resides
program = 'C:\\Program Files\\qBittorrent\\qbittorrent.exe'

# This searches your email account for unread emails that have a particular
# code, in this case YHAFMARQS47620 (I do not actually use this code anywhere
# so I wouldn't try anything immoral! :P)
# This is so that we know the emails have the intent of setting up a download
resultThreads = ezgmail.search(
    'YHAFMARQS47620 AND from:your.email@gmail.com AND label:UNREAD'
    )

# Get the current date
now = str(datetime.datetime.now())

# I fancied logging the amount of threads returned
logging.debug('Search results retrieved at ' + now + '. Returned ' +
    str(len(resultThreads)) + ' results.')  

# Loop through list of threads obtained
for i in range(0, len(resultThreads)):

    # Get the body of a message and split it in a list based on carriage returns
    emailstring = str(resultThreads[i].messages[0].body)
    logging.debug('Body of email returned: ' + emailstring)
    emaillist = emailstring.split('\r')
    logging.debug('Body of email split as follows: ')
    logging.debug(emaillist)

    # This will stay as 'Missing' if the email body has no magnet
    stripEmail = 'Missing'

    # Find the magnet in the email body (it will start with magnet),
    # and strips the \n because we need the magnet itself
    for i2 in emaillist:
        if i2.startswith('\nmagnet'):
            print('Found magnet.')
            stripEmail = i2.strip('\n')

    # Will go to the next email thread if no magnet is found
    if stripEmail == 'Missing':
        continue

    logging.debug('Magnet link stripped to: ' + stripEmail)

    # starts the download in qBittorrent using the program and the magnet
    qbProcess = subprocess.Popen([program, stripEmail])
    # qbProcess.wait() does not work when the program is used this way,
    # will use an email after a time period instead.

    # Note: if the magnet is incorrect, may stop the next magnets from being
    # tried by qb.

    resultThreads[i].messages[0].markAsRead()

# Sleep for 1 hour
time.sleep(3600)

# Send email confirming torrents downloaded.
ezgmail.send('py.marc.jowett@gmail.com', 'Download Complete',
    'Let us assume the download(s) have completed.')

# A task scheduler can be set up to repeat this every 15 minutes.