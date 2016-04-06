# Eventful API
# homepage: http://api.eventful.com
# python client library: http://api.eventful.com/libs/python/
# application key: hLdVs3LKGBLbjMfd

# Yelp API
# homepage: https://www.yelp.com/developers
# python client library: https://github.com/Yelp/yelp-python
# Keys:
yelp_api_keys = {
    "consumer_key": "mvC1SY7wAUx_RPlVhG-fIw",
    "consumer_secret": "vkqWVoowxsWkUu7KU0t2Pj3qY1k",
    "token": "syYEIdwvGt-uLGdgVmu9ZsQfE98CROe4",
    "token_secret": "AQLQnKJA7VYw4XlVIMK7hYzSwDo"
}

#
#Eventul Usage
#
import eventful

api = eventful.API('hLdVs3LKGBLbjMfd')

# If you need to log in:
# api.login('username', 'password')

events = api.call('/events/search', keywords='shows', l='Saint Paul')
for event in events['events']['event']:
    print("%s at %s on %s" % (event['title'], event['venue_name'], event['start_time']))


#
#Yelp Usage
#
print("\n")
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key=yelp_api_keys['consumer_key'],
    consumer_secret=yelp_api_keys['consumer_secret'],
    token=yelp_api_keys['token'],
    token_secret=yelp_api_keys['token_secret']
)

client = Client(auth)

params = {
    'term': 'italian food',
}

response = client.search('Twin Cities', **params)
for aBusiness in response.businesses:
    print(aBusiness.name)