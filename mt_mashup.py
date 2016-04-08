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
import ye_schedule
from flask import Flask, request, render_template, redirect


##### Called Functions #####

def search_yelp():
    with io.open('config_secret.json') as cred:       #authentication keys are stored in secret json file which is ignored in the .gitignore file
        creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

    results = client.search(parameters["both"]["location_center"], **parameters["yelp"])      #pass the params
    print(results)

def search_eventful():
    api = eventful.API('hLdVs3LKGBLbjMfd')        #activate key
    events = api.call('/events/search', q='beer', l='decorah')
    for event in events['events']['event']:
        print(event['title'], event['venue_name'])

def get_results():
    #yelp_results = search_yelp()
    #eventful_results = search_eventful()
    # add code to parse results with ye_schedule module
    # return results
    pass



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
    
    #possibilities = get_results()   #will be based to browser and iterated over to display possible "plans". Should be a list of dictionaries.
    get_results()
    return render_template("results.html", possibilities=possibilities)#redirect('/')

if __name__ == '__main__':
    app.run(debug=True)






