import yelp
import eventful
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

class Location:
    def __init__(self, type, yelp_loc_obj=None, dictionary=None, address=None):
        #parse location data based on type
        pass

class Activity:
    def __init__(self, object, type_str):
        self.type_str = type_str

        if self.type_str == "yelp":
            self.object = object
            self.name = object.name
            self.location = Location("yelp", object.location)
            self.address = object.location.address[0] + ", " + object.location.city + ", " + object.location.state_code
            self.phone = object.display_phone[3:]
            self.rating = object.rating
            self.lat = object.location.coordinate.latitude
            self.lng = object.location.coordinate.longitude
        
        elif self.type_str == "eventful":
            #similar to above but for an eventful object
            self.object = object
            self.name = object['title']
            self.location = Location("address", dictionary=object['venue_address'])
            self.start_time = object['start_time']
            self.end_time = object['stop_time']
            self.venue = object['venue_name'] + ", " + object['venue_address'] + ", " + object['city_name'] + ", " + object['region_name']
            self.description = object['description']
            self.lat = object['latitude']
            self.lng = object['longitude']

    def __str__(self):
        return str(self.name) + ", " + str(self.location)


class EventAndDiningPair:
    def __init__(self, event_activity, dining_activities):
        self.score = 0
        self.event_activity = event_activity
        self.dining_activities = dining_activities
        self.calculateScore()

    def calculateScore(self):
        #find the score (weight)
        pass

    #somewhat obsolete, assumes a single dining option
    def __str__(self):
        return "" + str(self.activities_list[0]) + ", " + str(self.activities_list[1].name)


class ScheduleMaker:
    def __init__(self, eventful_results, num_events_listed, num_dining_opts_per_event, yelp_params):
        self.eventful_results = eventful_results
        self.options_list = []
        self.num_events_listed = num_events_listed
        self.num_dining_opts_per_event = num_dining_opts_per_event
        self.yelp_params = yelp_params
        self.findScheduleOptions()
    
    def findScheduleOptions(self):
        self.options_list = []
        #Create a pair of activities for each of the combinations of one result from yelp and one from eventful
        for i in range(self.num_events_listed):
           
            event_activity = Activity(self.eventful_results[i], "eventful")
            
            lat = self.eventful_results[i]['latitude']  #
            lng = self.eventful_results[i]['longitude']  #
            dining_activities = []
    
            auth = Oauth1Authenticator(consumer_key = "mvC1SY7wAUx_RPlVhG-fIw",consumer_secret = "vkqWVoowxsWkUu7KU0t2Pj3qY1k",token =  "syYEIdwvGt-uLGdgVmu9ZsQfE98CROe4", token_secret = "AQLQnKJA7VYw4XlVIMK7hYzSwDo") #
            client = Client(auth)  #
            
            yelp_results = client.search_by_coordinates(lat, lng, **self.yelp_params)
            for j in range(self.num_dining_opts_per_event):
                #print(location.businesses[j])
                #print(self.yelp_results.businesses[j])
                dining = Activity(yelp_results.businesses[j], "yelp")
                dining_activities.append(dining)
            self.options_list.append(EventAndDiningPair(event_activity, dining_activities))


    #Not a priority, but important
    def orderOptions(self):
        #psuedo
        #self.options_list.sort_by(score)
        pass
