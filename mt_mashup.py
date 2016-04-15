# Eventful API
# homepage: http://api.eventful.com
# python client library: http://api.eventful.com/libs/python/
# application key: hLdVs3LKGBLbjMfd

# Yelp API
# homepage: https://www.yelp.com/developers
# python client library: https://github.com/Yelp/yelp-python
# yelp search params: https://www.yelp.com/developers/documentation/v2/search_api


##### Imports #####

import eventful
import yelp
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io
import json
from ye_schedule import *
from flask import Flask, request, render_template, redirect


##### Called Functions #####

def search_yelp():
    with io.open('config_secret.json') as cred:       #authentication keys are stored in secret json file which is ignored in the .gitignore file
        creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

    results = client.search(parameters["both"]["location_center"], **parameters["yelp"])      #pass the params
    #print(results)
    return results

def search_eventful():
    api = eventful.API('hLdVs3LKGBLbjMfd')        #activate key
    events = api.call('/events/search', q="music", l="San Diego")

    for event in events['events']['event']:
        print (("%s at %s") % (event['title'], event['venue_name']))

    print(events['events']['event'])
    return events['events']['event']

def get_results():
    yelp_results = search_yelp()
    eventful_results = search_eventful()

    # parse results with ye_schedule module

    print("size of yelp results is: {}".format(len(yelp_results.businesses)))
    print("size of eventful results is: {}".format(len(eventful_results)))

    schedule_maker = ScheduleMaker(yelp_results, eventful_results)

    print("size of options list before returning in get_results is: {}".format(len(schedule_maker.options_list)))
    return schedule_maker.options_list


#### Initialize Parameter Dictionaries #####

parameters = {}

parameters["both"] = {
    "num_schedule_results" : 0,
    "activity_type" : "",
    "location_center" : "", #(longitude,latitude)
    "location_radius" : 0,
    "date" : None,  #date(),
    "time_frame" : (0,0) #(min_start_time, max_end_time)
}

parameters["eventful"] = {
    "keywords" : [""],
    "category" : "",
    "sort_order" : "",
    "price_range" : None
}

parameters["yelp"] = {
    "term" : "", #(keywords, e.g. "food", "restaurants")
    #"sort" : None, #(similar to eventful sort order, e.g. "Best Matched", "Highest Rated")
    #"category_filter" : "", #(internal, based on type of activity/entertainment)
    "price_range" : None
}


##### App Control #####

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template("index.html")

@app.route('/reset', methods = ['POST'])
def reset():
    return render_template("index.html")

@app.route('/search', methods = ['GET', 'POST'])
def my_form_post():
    location = request.form['location']
    parameters["eventful"]["keywords"] = request.form['etype']
    parameters["yelp"]["keywords"] = request.form['dtype']
    parameters["both"]["location_radius"] = request.form['distance']
    parameters["both"]["date"] = request.form['date']
    parameters["eventful"]["price_range"] = request.form['eprice']
    parameters["yelp"]["price_range"] = request.form['dprice']
    parameters["both"]["location_center"] = request.form['location']
    
    sample_dict = {
            'event': 'Baseball Game',
            'dining' :'Waffle House',
            'date' : '2016-04-15',
            'time' : '6:00pm',
            'cost' : '$$$'
    }
    possibilities = []
    possibilities.append(sample_dict)

    options_list = get_results()

    print("size of options_list = " + str(len(options_list)))

    for an_option in options_list:
        a_dict = {}
        a_dict['event'] = an_option.activities_list[0].name
        a_dict['dining'] = an_option.activities_list[1].name
        """ To implement date: assign the date attribute in the Activity constructor
        based on the format specified (by the API docs) for the date in a yelp/eventful result object
        """
        a_dict['date'] = "unimplemented"
        a_dict['time'] = an_option.activities_list[0].start_time
        a_dict['cost'] = '?'
        possibilities.append(a_dict)

    print("size of possibilities is: {}", len(possibilities))

    #possibilities = get_results()   #will be based to browser and iterated over to display possible "plans". Should be a list of dictionaries.
    return render_template("results.html", possibilities=possibilities)#redirect('/')

if __name__ == '__main__':
    app.run(debug=True)






