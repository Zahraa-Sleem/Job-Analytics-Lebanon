import folium
from opencage.geocoder import OpenCageGeocode
import json 
from statistics_1 import *

with open('objects.json') as f:
    data = json.load(f)

dataframe = pd.read_json(json.dumps(data))


result = countlocation(dataframe)

# Create a map object
world_map = folium.Map()

# Initialize the geocoder with your API key
geocoder = OpenCageGeocode("001a4519b76e4c4480b90ea3643a4e31")  # Replace "YOUR_API_KEY" with your actual API key


for _, row in result.iterrows():
    # Specify the country name
    country_name = row['Location'] 
    # Geocode the country name to get the coordinates
    results = geocoder.geocode(country_name)
    latitude = results[0]['geometry']['lat']
    longitude = results[0]['geometry']['lng']
    # Add a marker for the specific country
    country_coordinates = (latitude, longitude)
    folium.Marker(location=country_coordinates, popup=str(row['Count'])).add_to(world_map)

# Display the map
world_map.save('world_map.html')
