import yelp
import eventful

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

        elif self.type_str == "eventful":
            #similar to above but for an eventful object
            self.object = object
            self.name = object['title']
            self.location = Location("address", dictionary=object['venue_address'])
            self.start_time = object['start_time']
            self.end_time = object['stop_time']

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
    def __init__(self, yelp_results, eventful_results, num_events_listed, num_dining_opts_per_event):
        self.yelp_results = yelp_results
        self.eventful_results = eventful_results
        self.options_list = []
        self.num_events_listed = num_events_listed
        self.num_dining_opts_per_event = num_dining_opts_per_event
        self.findScheduleOptions()


    def findScheduleOptions(self):
        self.options_list = []
        #Create a pair of activities for each of the combinations of one result from yelp and one from eventful
        for i in range(self.num_events_listed):
            event_activity = Activity(self.eventful_results[i], "eventful")
            dining_activities = []
            for j in range(self.num_dining_opts_per_event):
                dining = Activity(self.yelp_results.businesses[j], "yelp")
                dining_activities.append(dining)
            self.options_list.append(EventAndDiningPair(event_activity, dining_activities))

    #Not a priority, but important
    def orderOptions(self):
        #psuedo
        #self.options_list.sort_by(score)
        pass
