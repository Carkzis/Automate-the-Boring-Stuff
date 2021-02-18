"""
Link Verification.
Attempts to download every linked page on a page.
"""

import time, sys, os, bs4, requests

# Note: will not deal with internal links, but could sort that with a RegEx...
url = input('Please enter an URL: ')

# Requests the url, and selects everything with a hyperlink and adds to list
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')

# Loops through list of links on webpage
for i in range(len(links)):
    # Checks if there is a href in the <a> tag, and if not, goes to the next
    # in list
    getHref = links[i].get('href')
    if getHref == None:
        continue
    print('Checking link: ' + getHref)
    # Checks if the href starts with https:// or http://, and if so, checks link
    # Then, prints findings
    if getHref.startswith('https://') == True or getHref.startswith('http://') == True:
        res = requests.get(getHref)
        if res.status_code == requests.codes.ok:
            print('Link seems okay!')
        elif res.status_code == 404:
            print(str(res.status_code) + ' Not Found.')
        else:
            print(str(res.status_code) + ' Problem with link.')
    else:
    # Avoids error by not attempting anything without https:// or http://
        print('This will not work...')