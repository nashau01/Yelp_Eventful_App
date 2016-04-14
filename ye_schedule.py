import yelp
import eventful

NUM_EVENTS_LISTED = 5
NUM_DINING_OPTIONS_FOR_EACH_EVENT = 4

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


class ScheduleOption:
    def __init__(self, activities_list):
        self.score = 0
        self.activity_list = activities_list
        self.calculateScore()

    def calculateScore(self):
        #find the score (weight)
        pass

    def __str__(self):
        return "" + str(self.activities_list[0]) + ", " + str(self.activity_list[1].name)


class ScheduleMaker:
    def __init__(self, yelp_results, eventful_results):
        self.yelp_results = yelp_results
        self.eventful_results = eventful_results
        self.options_list = []
        self.findScheduleOptions(999)
        print("initialized a ScheduleMaker object")

    def findScheduleOptions(self, numOptions):
        options_list = []
        #Create a pair of activities for each of the combinations of one result from yelp and one from eventful
        for i in range(NUM_EVENTS_LISTED):
            event = Activity(self.eventful_results[i], "eventful")
            for j in range(NUM_DINING_OPTIONS_FOR_EACH_EVENT):
                dining = Activity(self.yelp_results.businesses[j], "yelp")
                activities_list = [event, dining]
                print("appending activities: " + str(activities_list[0]) + " " + str(activities_list[1]))
                options_list.append(ScheduleOption(activities_list))

    #Not a priority, but important
    def orderOptions(self):
        #psuedo
        #self.options_list.sort_by(score)
        pass
