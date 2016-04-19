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

def search_eventful():
    api = eventful.API('hLdVs3LKGBLbjMfd')        #activate key

    events = api.call('/events/search', keywords=parameters["eventful"]["keywords"], location=parameters["both"]["location_center"], date=parameters["both"]["date"], page_size=parameters["eventful"]["results"])
    #for event in events['events']['event']:
    #    print (("%s at %s") % (event['title'], event['venue_name']))

    return events['events']['event']

def get_results():
    eventful_results = search_eventful()
    # parse results with ye_schedule module
    schedule_maker = ScheduleMaker(eventful_results, parameters["yelp"])
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
    "keywords" : "",
    "category" : "",
    "sort_order" : "",
    "price_range" : None,
    "results" : 5
}

parameters["yelp"] = {
    "term" : "food", #(keywords, e.g. "food", "restaurants")
    #"sort" : None, #(similar to eventful sort order, e.g. "Best Matched", "Highest Rated")
    #"category_filter" : "", #(internal, based on type of activity/entertainment)
    #"price_range" : None
    "radius_filter" : None,
    "limit" : 3
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
    parameters["yelp"]["term"] = request.form['dtype'] + " food"
    parameters["both"]["date"] = request.form['date']
    #parameters["eventful"]["price_range"] = request.form['eprice']
    #parameters["yelp"]["price_range"] = request.form['dprice']
    parameters["both"]["location_center"] = request.form['location']
    parameters["yelp"]["radius_filter"] =  request.form['radius_filter']
    parameters["eventful"]["results"] = request.form['max_results']
    parameters["yelp"]["limit"] = int(request.form['mdining_results'])
    print("max dining:", parameters["yelp"]["limit"])
    
    
    possibilities = []
    #possibilities.append(sample_dict)
    
    
    #try:

    options_list = get_results()
    
    #except:
    #    return render_template("sorry.html")

    print("size of options_list = " + str(len(options_list)))

    count = 1
    for an_option in options_list:
        a_dict = {}
        a_dict['event'] = an_option.event_activity.name
        a_dict['dining'] = []
        for a_dining_option in an_option.dining_activities:
            a_dining_dict = {}
            a_dining_dict['name'] = a_dining_option.name
            a_dining_dict['address'] = a_dining_option.address
            a_dining_dict['phone'] = a_dining_option.phone 
            a_dining_dict['lat'] = a_dining_option.lat
            a_dining_dict['lng'] = a_dining_option.lng
            a_dining_dict['rating'] = a_dining_option.rating
            a_dict['dining'].append(a_dining_dict)

        a_dict['date'] = "unimplemented"
        a_dict['time'] = an_option.event_activity.start_time
        a_dict['cost'] = '?'
        a_dict['venue'] = an_option.event_activity.venue
        a_dict['address'] = "unimplemented"
        a_dict['description'] = an_option.event_activity.description
        
        # behind the scenes variables for implementing google maps
        a_dict['lat'] = an_option.event_activity.lat
        a_dict['lng'] = an_option.event_activity.lng
        scount = str(count)
        a_dict['id'] = "id" + scount
        a_dict['mapno'] = "map" + scount
        a_dict['mapprop'] = "mp" + scount
        a_dict['center'] = "center" + scount
        a_dict['info'] = "info" + scount
        #"""
        for option in a_dict['dining']:
            option['marker'] = "marker" + str(count * 2)
            option['info'] = "dinfo" + str(count * 2)
            count += 1   #count needs to increment twice to implement google maps 
        #"""
        count += 1

        possibilities.append(a_dict)
    
        print(a_dict) 

    #possibilities = get_results()   #will be based to browser and iterated over to display possible "plans". Should be a list of dictionaries.
    return render_template("results.html", possibilities=possibilities)#redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


