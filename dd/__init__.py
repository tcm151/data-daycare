# import flask class Flask which contatins all of the internal 
# web server logic
from flask import Flask, render_template, url_for, request
from dd.db import db
from dd.daycare.daycare import daycare
import requests, geopy.location

app = Flask(__name__) # Instantiate a copy of the Flask class called app
app.register_blueprint(daycare) # Register the daycare blueprint into the app

# def getDistance(coords1, coords2):
#     return geopy.distance.vincenty(coords1, coords2).km

# def findNearby(user_lat, user_long):
#     database = db.getDatabase()
#     nearby = [
#         {"index": -1, "distance": 99999},
#         {"index": -1, "distance": 99999},
#         {"index": -1, "distance": 99999},
#         {"index": -1, "distance": 99999},
#         {"index": -1, "distance": 99999},
#     ]
#     for daycare in database:
#         distance = getDistance( (user_lat,user_long), (daycare.location.latitude,darecare.location.latitude) )
#         if (distance < nearby[4]):
#             for (i = nearby.length; i > 0; i -= 1)
        
#     return nearby

# Our base domain page, @app.route creates a webpage at
# www.ourdomain.com/<routename> which anyone can access
@app.route('/')
# The home route
@app.route('/home')
def home(): # Function linked to the routed webpaged
    # user_ip = requests.get('https://get.geojs.io/v1/ip.json').json()['ip']
    # user_geoData = requests.get('https://get.geojs.io/v1/ip/geo/' + user_ip + '.json').json()
    # nearby = findNearby(user_geoData['latitude'], user_geoData['longitude'])

    return render_template('home.html', nearby = db.getXElements(5))
    # Return the html file to be displayed on the routed page
    # nearby variable will be availble to access inside the html file

# The map route
@app.route('/map')
def map():
    return render_template("map.html", database = db.getDatabase())
    # database variable will be accessable from within map.html

# The directory route
@app.route('/directory')
def directory():
    return render_template("directory.html", database = db.getDatabase())
    # database variable will be accessable from within directory.html

# The about route
@app.route('/about')
def about():
    return render_template('about.html')