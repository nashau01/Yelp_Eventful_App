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
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


##### Called Functions #####

def search_yelp():
    with io.open('config_secret.json') as cred:       #authentication keys are stored in secret json file which is ignored in the .gitignore file
        creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

    results = client.search(parameters["both"]["location_center"], **parameters["yelp"])      #pass the params
    return results

def search_eventful():
    api = eventful.API('hLdVs3LKGBLbjMfd')        #activate key
    events = api.call('/events/search', q="music", l="San Diego")

    #for event in events['events']['event']:
    #    print (("%s at %s") % (event['title'], event['venue_name']))

    return events['events']['event']

def get_results():
    yelp_results = search_yelp()
    eventful_results = search_eventful()

    # parse results with ye_schedule module

    schedule_maker = ScheduleMaker(yelp_results, eventful_results)

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
GoogleMaps(app)

@app.route('/')
def landing_page():
    return render_template("index.html")

@app.route('/reset', methods = ['POST'])
def reset():
    return render_template("index.html")

#@app.route('more', methods = ['POST'])

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
    """
    sample_dict = {
            'event' : 'Baseball Game',
            'dining' : [{'name' : 'Waffle House', 'address' : '106 North Ave., Minneapolis, MN', 'price' : '$', 'lat' : 44.968046, 'lng' : -94.420307}, {'name' : 'Perkin\'s', 'address' :'3000 Busy Rd., Minneapolis, MN', 'price' : '$$', 'lat' : 44.33328, 'lng' : -89.132008}, {'name' : 'IHOP', 'address' : '720 Long St., Minneapolis, MN', 'price' : '$$', 'lat' : 33.755787 , 'lng' : -116.359998}, {'name' : 'Denny\'s', 'address' : '404 Error St., Minneapolis, MN', 'price' : '$$', 'lat' : 33.844843 , 'lng' : -116.54911}],
            'date' : '2016-04-15',
            'lat' : 44.92057,
            'lng' : -93.44786,
            'time' : '6:00pm',
            'cost' : '$$$',
            'venue' : 'Baseball Field',
            'city' : 'Minneapolis, MN',
            'description' : "Baseball is a bat-and-ball game played between two teams of nine players each who take turns batting and fielding.The batting team attempts to score runs by hitting a ball that is thrown by the pitcher with a bat swung by the batter, then running counter-clockwise around a series of four bases: first, second, third, and home plate. A run is scored when a player advances around the bases and returns to home plate.Players on the batting team take turns hitting against the pitcher of the fielding team, which tries to prevent runs by getting hitters out in any of several ways. A player on the batting team who reaches a base safely can later attempt to advance to subsequent bases during teammates' turns batting, such as on a hit or by other means. The teams switch between batting and fielding whenever the fielding team records three outs. One turn batting for both teams, beginning with the visiting team, constitutes an inning. A game comprises nine innings, and the team with the greater number of runs at the end of the game wins. Baseball is the only major team sport in America with no game clock, although almost all games end in the ninth inning.Evolving from older bat-and-ball games, an early form of baseball was being played in England by the mid-18th century. This game was brought by immigrants to North America, where the modern version developed. By the late 19th century, baseball was widely recognized as the national sport of the United States. Baseball is now popular in North America and parts of Central and South America, the Caribbean, and East Asia.  In the United States and Canada, professional Major League Baseball (MLB) teams are divided into the National League (NL) and American League (AL), each with three divisions: East, West, and Central. The major league champion is determined by playoffs that culminate in the World Series. The top level of play is similarly split in Japan between the Central and Pacific Leagues and in Cuba between the West League and East League."
            
            }
   
    possibilities = []
    possibilities.append(sample_dict)


    for i in range(0,19):
        possibilities.append(sample_dict.copy())
    
    count = 1
    for dict in possibilities:
        scount = str(count)
        dict['id'] = "id" + scount
        dict['mapno'] = "map" + scount
        dict['mapprop'] = "mp" + scount
        dict['center'] = "center" + scount
        dict['info'] = "info" + scount
        for item in dict['dining']:
            item['marker'] = "marker" + str(count * 2)
            item['info'] = "dinfo" + str(count * 2) 
            count += 1
        
        
        
        #print(item['mv'])
        
        count += 1
        print(count)
        print(dict['id'])
        """
    
    

#'cost' : '$$$'
# }
    possibilities = []
    #possibilities.append(sample_dict)

    options_list = get_results()

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

    #possibilities = get_results()   #will be based to browser and iterated over to display possible "plans". Should be a list of dictionaries.
    return render_template("results.html", possibilities=possibilities)#redirect('/')

if __name__ == '__main__':
    app.run(debug=True)






