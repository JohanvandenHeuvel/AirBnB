import gmplot
import googlemaps
import json
import math
import os
import requests
import warnings
import pandas as pd

df = pd.read_csv('listings.csv')

KEY = 'AIzaSyBdLO_83KDZVkS91AkiqsSQw2lf4y2u1OA'

gmaps = googlemaps.Client(key=KEY)
location_string = "Amsterdam"
geocode = gmaps.geocode(location_string)
coordinates = geocode[0].get('geometry').get('location')
latitude, longitude = (coordinates.get('lat'), coordinates.get('lng'))

gmap = gmplot.GoogleMapPlotter(latitude, 
                                longitude, 13, apikey=KEY) 

latitude_list = df['latitude']
longitude_list = df['longitude']

#gmap.scatter( latitude_list, longitude_list, '# F44242', size = 100, marker = False) 

gmap.scatter( latitude_list, longitude_list) 

gmap.draw("mymap5.html")


