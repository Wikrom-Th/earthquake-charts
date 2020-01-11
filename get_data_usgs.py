import requests
import csv
import datetime

# countries that is considered in this project (in pan-asia)
countries = ["China", "Taiwan", "Japan", "South Korea", "Brunei", "Cambodia", "Indonesia", "Laos", "Malaysia", 
            "Myanmar/Burma", "Philippines", "Singapore", "Thailand", "Timor-Leste", "Vietnam", "Bangladesh", 
            "Bhutan", "India", "Nepal", "Sri Lanka", "Micronesia", "Papua New Guinea"]

# url for usgs
api_url = "https://earthquake.usgs.gov/fdsnws/event/1/"

# metadata / info about the data
data_format = "geojson"
eventtype = "earthquake"

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
place = []
mag = []
time = []
felt = []
cdi = []
mmi = []
sig = []

other_place = []
other_mag = []
other_time = []
other_felt = []
other_cdi = []
other_mmi = []
other_sig = []

# time formatting function
def format_time(unformatted_time):
    dt = datetime.datetime.fromtimestamp(unformatted_time/1000)
    return dt

for i in range(50):
    year = 1970 + i
    starttime = f"{year}-01-01"
    endtime = f"{year}-12-31"

    count_url = f"{api_url}count?format={data_format}&starttime={starttime}&endtime={endtime}&minlatitude={minlat}&maxlatitude={maxlat}&minlongitude={minlong}&maxlongitude={maxlong}&minmagnitude={minmag}&maxmagnitude={maxmag}&eventtype={eventtype}"
    data_url = f"{api_url}query?format={data_format}&starttime={starttime}&endtime={endtime}&minlatitude={minlat}&maxlatitude={maxlat}&minlongitude={minlong}&maxlongitude={maxlong}&minmagnitude={minmag}&maxmagnitude={maxmag}&eventtype={eventtype}"
    
    count_response = requests.get(count_url)
    data_response = requests.get(data_url)

    count = count_response.json()
    data = data_response.json()

    print(count)
    total_earthquakes += count['count']

    # add place, magnitude, and time of the earthquakes to our list

    for i in range(len(data['features'])):

        # temporary put the each properties of data into variables
        data_place = data['features'][i]['properties']['place'].strip()
        data_mag = data['features'][i]['properties']['mag']
        data_time = format_time(data['features'][i]['properties']['time'])
        data_felt = data['features'][i]['properties']['felt']
        data_cdi = data['features'][i]['properties']['cdi']
        data_mmi = data['features'][i]['properties']['mmi']
        data_sig = data['features'][i]['properties']['sig']

        # boolean to check if the data will be in others or not
        other = True

        for country in countries:

            # check if it's the special case (Myanmar/Burma, East Timor, and [Insert Country Here] Region) 
            # create temp_place variable accordingly if it is
            # otherwise, temp_place will just be the substring of the length in the country we're considering

            if data_place[-7:].lower() == "myanmar" or data_place[-5:].lower() == "burma":
                temp_place = "myanmar/burma"

            elif data_place[-10:].lower() == "east timor":
                temp_place = "timor-leste"

            elif data_place[-7:].lower() == " region":
                temp = data_place[:-7].lower()
                if temp[-len(country):] == country.lower():
                    temp_place = temp[-len(country):]

            else:
                temp_place = data_place[-len(country):].lower()

            # add the datas to our lists if it's the country we want
            if country.lower() == temp_place:

                place.append(country)
                mag.append(data_mag)
                time.append(data_time)
                felt.append(data_felt)
                cdi.append(data_cdi)
                mmi.append(data_mmi)
                sig.append(data_sig)

                other = False
                break

        if other:
            
            other_place.append(data_place)
            other_mag.append(data_mag)
            other_time.append(data_time)
            other_felt.append(data_felt)
            other_cdi.append(data_cdi)
            other_mmi.append(data_mmi)
            other_sig.append(data_sig)

    # print(data)

print(f"Total earthquakes in this region over the past 50 years: {total_earthquakes}")

# export data as csv files

with open('pan_asia_eqs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['place', 'mag', 'time', 'felt', 'cdi', 'mmi', 'sig']
    writer.writerow(header)
    writer.writerows(zip(place, mag, time, felt, cdi, mmi, sig))

with open('other_eqs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['place', 'mag', 'time', 'felt', 'cdi', 'mmi', 'sig']
    writer.writerow(header)
    writer.writerows(zip(other_place, other_mag, other_time, other_felt, other_cdi, other_mmi, other_sig))
