#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string

from twilio.rest import Client

# Preset values (use your own):
ACCOUNT_SID = 'ACCOUNT SID'
AUTH_TOKEN = 'AUTHORISATION TOKEN'
TWILIO_NO = 'YOUR TWILIO NUMBER'
MY_NO = 'YOUR NUMBER'

def textmyself(message):
    twilioCli = Client(ACCOUNT_SID, AUTH_TOKEN)
    twilioCli.messages.create(body=message, from_=TWILIO_NO, to=MY_NO)
