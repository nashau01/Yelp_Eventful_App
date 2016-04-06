# Eventful API
# homepage: http://api.eventful.com
# python client library: http://api.eventful.com/libs/python/
# application key: hLdVs3LKGBLbjMfd

# Yelp API
# homepage: https://www.yelp.com/developers
# python client library: https://github.com/Yelp/yelp-python
# Keys:
"""
{
    "consumer_key": "mvC1SY7wAUx_RPlVhG-fIw",
    "consumer_secret": "vkqWVoowxsWkUu7KU0t2Pj3qY1k",
    "token": "syYEIdwvGt-uLGdgVmu9ZsQfE98CROe4",
    "token_secret": "AQLQnKJA7VYw4XlVIMK7hYzSwDo"
}
"""


#import yelp
import eventful


api = eventful.API('hLdVs3LKGBLbjMfd')

# If you need to log in:
# api.login('username', 'password')

events = api.call('/events/search', q='concert', l='Decorah')
for event in events['events']['event']:
    print (event['title'], "," , event['venue_name'], ",", event['city_name'], ",", event['start_time'])