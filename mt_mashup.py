# Eventful API
# homepage: http://api.eventful.com
# python client library: http://api.eventful.com/libs/python/
# application key: hLdVs3LKGBLbjMfd

# Yelp API
# homepage: https://www.yelp.com/developers
# python client library: https://github.com/Yelp/yelp-python
# Keys:





#import yelp
import eventful
import yelp
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io
import json


# read API keys
with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)


client = Client(auth)


api = eventful.API('hLdVs3LKGBLbjMfd')

# If you need to log in:
# api.login('username', 'password')

events = api.call('/events/search', q='concert', l='Decorah')
for event in events['events']['event']:
    print (event['title'], "," , event['venue_name'], ",", event['city_name'], ",", event['start_time'])


params = {
    'term': 'food',
    'lang': 'en'
}

response = client.search('Decorah', **params)


print(response.businesses[1].name)