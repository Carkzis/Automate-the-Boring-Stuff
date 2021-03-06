"""
Umbrella Reminder.
Checks a weather website and texts you if it is raining.
"""

import requests, bs4, time, datetime, textMyself # text myself needs
# your own details adding to it

# Requests url
url = 'https://weather.com/en-GB/weather/today/l/0686a91b1d358b3b51a3e8afdb37eda3d1a214b4b537eccba697666ab69ac9e7'
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Finds the element in the weather site with the weather conditions
weatherElem = soup.find("div", class_="CurrentConditions--phraseValue--2xXSr")

# Will say if it is raining or not by text
if "Rain" in str(weatherElem.text):
    textMyself.textmyself('It gonna rain!')
else:
    print("It is not raining...")

# Set up task scheduler - would use Task Scheduler for windows, with a .bat file