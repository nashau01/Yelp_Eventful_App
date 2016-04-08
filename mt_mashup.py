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
import ye_schedule
from flask import Flask, request, render_template, redirect

def search_yelp(location, dtype):
    with io.open('config_secret.json') as cred:       #authentication keys are stored in secret json file which is ignored in the .gitignore file
        creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

    params = {
    
    'term': dtype,
    'lang': 'en',
    }
    
    return client.search(location, **params)      #pass the params


parameters = {}

parameters["both"] = {
    "num_schedule_results" : 0,
    "activity_type" : "",
    "location_center" : (0,0), #(longitude,latitude)
    "location_radius" : 0,
    "date" : None,  #date(),
    "time_frame" : (0,0) #(min_start_time, max_end_time)
}

parameters["eventful"] = {
    "keywords" : [""],
    "category" : "",
    "sort_order" : ""
}

parameters["yelp"] = {
    "term" : "", #(keywords, e.g. "food", "restaurants")
    "sort" : None, #(similar to eventful sort order, e.g. "Best Matched", "Highest Rated")
    "category_filter" : "" #(internal, based on type of activity/entertainment)
}

def search_eventful(etype, location):
    api = eventful.API('hLdVs3LKGBLbjMfd')
    return api.call('/events/search', q=etype, l=location)    #search eventful via API
    for event in events['events']['event']:
        print("here", event['title'], "," , event['venue_name'], ",", event['city_name'], ",", event['start_time'])

def get_results(location, dtype, etype, date, distance, eprice, dprice):
    yelp_results = search_yelp(location, dtype)
    eventful_results = search_eventful(etype, location)
    print(yelp_results)
    print(eventful_results)

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
    etype = request.form['etype']
    dtype = request.form['dtype']
    distance = request.form['distance']
    date = request.form['date']
    eprice = request.form['eprice']
    dprice = request.form['dprice']
    #results = get_results(location, dtype, etype, date, distance, eprice, dprice)
    print(location, etype, dtype, distance, date, eprice, dprice)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
