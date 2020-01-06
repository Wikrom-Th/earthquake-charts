import requests
import csv
import datetime
from time import sleep

# url for usgs
api_url = "https://earthquake.usgs.gov/fdsnws/event/1/"

# metadata / info about the data
data_format = "geojson"


# this start and end is the whole range; however, the usgs api only supports 20,000 earthquake data at one request instance.
"""
starttime = "1970-01-01"
endtime = "2019-12-31"
"""

# latitude and longitude of the whole pan-asia
minlat = "-11.5"
maxlat = "46.5"
minlong = "68"
maxlong = "155"

# magnitude of interest
minmag = "4"
maxmag = "10"


# for looping to get data in one-year intervals
total_earthquakes = 0

# these 3 things are relevant to the project
unformatted_place = []
mag = []
unformatted_time = []

for i in range(50):
    year = 1970 + i
    starttime = f"{year}-01-01"
    endtime = f"{year}-12-31"
    
    count_url = f"{api_url}count?format={data_format}&starttime={starttime}&endtime={endtime}&minlatitude={minlat}&maxlatitude={maxlat}&minlongitude={minlong}&maxlongitude={maxlong}&minmagnitude={minmag}&maxmagnitude={maxmag}"
    data_url = f"{api_url}query?format={data_format}&starttime={starttime}&endtime={endtime}&minlatitude={minlat}&maxlatitude={maxlat}&minlongitude={minlong}&maxlongitude={maxlong}&minmagnitude={minmag}&maxmagnitude={maxmag}"
    
    count_response = requests.get(count_url)
    data_response = requests.get(data_url)

    count = count_response.json()
    data = data_response.json()

    print(count)
    total_earthquakes += count['count']

    # add place, magnitude, and time of the earthquakes to our list
    for i in range(lens(data['features']))
        unformatted_place.append(data['features'][i]['properties']['place'])
        mag.append(data['features'][i]['properties']['mag'])
        unformatted_time.append(data['features'][i]['properties']['time'])

    # print(data)

print(f"Total earthquakes in pan-asia over the past 50 years: {total_earthquakes}")

# TODO: Format the places (as country), and the time (as year, month, day)