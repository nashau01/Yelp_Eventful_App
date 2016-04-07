

class ScheduleOption:
    def __init__(self, yelp_results, eventful_results):
        yelp_results = yelp_results
        eventful_results = eventful_results
        score = 0

    def calculateScore(self):
        #find the score (weight)
        pass

class ScheduleMaker:
    def __init__(self, yelp_results, eventful_results):
        yelp_results = yelp_results
        eventful_results = eventful_results

    def findPossibleSchedules(self, numOptions):
        options_list = []
        for i in range(numOptions):
            options_list.append(findNewOption())

        return options_list

    def findNewOption(self):
        #find a new option using the results
        option = ScheduleOption(yelp_results, eventful_results)
        return option