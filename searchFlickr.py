"""
Image Site Downloader.
Downloads images from a site connected to a user given search term.
"""

import time, sys, os, bs4, requests

# Does a "search" on imgur by combining search term with the url.
searchTerm = input('Enter a search term for the images: ')
url = 'https://imgur.com/search?q=' + searchTerm
# Creates a directory for imgur
os.makedirs('imgur', exist_ok=True)
time.sleep(3) # Pause for effect!

# Replace spaces with + in the url
url.replace(' ', '+')

# Get the list of image urls using requests and Beautiful Soup
res = requests.get(url)
res.raise_for_status
soup = bs4.BeautifulSoup(res.text, 'html.parser')
imageElem = soup.select('.image-list-link img') # this selector selects image

# Checks if any images were returned
if imageElem == []:
    print('Could not find any images for this search term.')
else:
    # For every element in the received list, get it downloaded to the folder
    for i in range(len(imageElem)):
        # Create the url using the element
        imageUrl = 'https:' + imageElem[i].get('src')
        print('Downloading image at ' + imageUrl + '...')
        # Request the image
        res = requests.get(imageUrl)
        res.raise_for_status()
        # Open an image file in wb mode
        imageFile = open(os.path.join('imgur', os.path.basename(imageUrl)), 'wb')

        # Download image in chunks
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

print('Done.')