"""
Scheduled Web Comic Downloader.
Downloaded comics from multiple sites on a schedule (used the Windows
scheduler for that.)
"""

#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading

os.getcwd()
os.chdir('C:\\Users\\username\\documents')
# checks if a comix folder exists, if it doesn't, it makes one
os.makedirs('comix', exist_ok=True)    # store comics in \comix

comicSites = [
    'http://www.lefthandedtoons.com/', 
    'https://www.buttersafe.com/',
    'https://www.exocomics.com/'
    ]

def downloadComic(url):
        """
        Downloads the latest comic from a range of sites.
        """
        print('Downloading page ' + url + '...')

        # Request the url, check the status
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find url of comic image, the element is unique to each of these
        # sites
        if url == 'http://www.lefthandedtoons.com/':
            comicElem = soup.select('#comicwrap > div.comicdata > img')
        elif url == 'https://www.buttersafe.com/':
            comicElem = soup.select('#comic img')
        elif url == 'https://www.exocomics.com/':
            comicElem = soup.select('img', class_='image-style-main-comic')

        # checks if element retrieve, if it is, downloads the image
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')

            # Download and save the image.
            res = requests.get(comicUrl, headers={'User-Agent': 'Mozilla/5.0'})
            res.raise_for_status()
            imageFileName = os.path.join('comix', os.path.basename(comicUrl))
            if os.path.exists(imageFileName) == True:
                print('Image ' + os.path.basename(comicUrl) +
                    ' has already been downloaded.')
            else:
                imageFile = open(os.path.join(
                    'comix',
                    os.path.basename(comicUrl)),
                    'wb'
                    )
                print('Downloading image %s...' % (comicUrl))
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

# Threading
downloadThreads = []             # a list of all the Thread objects
for i in range(len(comicSites)):    # loops through comic sites
    # when providing a list into threads, it needs a tuple so put comma at end
    downloadThread = threading.Thread(
        target=downloadComic, # this target is the downloadComic function
        args=(comicSites[i],)
        ) 
    # append the thread to a list, and start it
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end, then join them together
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
