# Eventful API
# homepage: http://api.eventful.com
# python client library: http://api.eventful.com/libs/python/
# application key: hLdVs3LKGBLbjMfd

# Yelp API
# homepage: https://www.yelp.com/developers
# python client library: https://github.com/Yelp/yelp-python
# yelp search params: https://www.yelp.com/developers/documentation/v2/search_api

import eventful
import yelp
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io
import json


#activate eventful API with key
api = eventful.API('hLdVs3LKGBLbjMfd')

# read API keys for yelp
with io.open('config_secret.json') as cred:       #authentication keys are stored in secret json file which is ignored in the .gitignore file
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

client = Client(auth)


# If you need to log in:
# api.login('username', 'password')


#use of eventful API
events = api.call('/events/search', q='concert', l='Decorah')    #search eventful via API
for event in events['events']['event']:
    print (event['title'], "," , event['venue_name'], ",", event['city_name'], ",", event['start_time'])


#use of yelp API
params = {
    'term': 'food',
    'lang': 'en'
}

response = client.search('Decorah', **params)      #pass the params
print(response.businesses[0].name)