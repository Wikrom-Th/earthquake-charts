# earthquake-charts

Use USGS Earthquake Catalog API to gather earthquake data and visualize them using matplotlib

The code in this is project is originally used to collect data on earthquakes in pan-asia during the 50 year range of 1970-2019

## Installation

git clone this project

`pip install -r requirements.txt`

## Description of files in this project

`get_data_usgs.py` takes the data from usgs API and change the place of the earthquake to the countries in the list accordingly

`assign_countries_to_place.py` is used to manually assign country to the regions that are not detect in `get_data_usgs.py`

`eq_data` folder contains two files:

- `pan_asia_eqs.csv` is used to store earthquakes in pan-asia; these are either added automatically 
through `get_data_usgs.py` or moved manually from `other_eqs.csv` using `assign_countries_to_place.py`  

- `other_eqs.csv` is used to store other earthquakes that were queried along with from `get_data_usgs.py`