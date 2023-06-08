import plotly.express as px
from statistics_1 import *
import folium
from opencage.geocoder import OpenCageGeocode
import json

def plotdepartments(dataframe):
    custom_colors = ['#e76895', '#b557c3', '#9d57cb', '#e9b8a9','#efe7e3'] 
    result=countdepartment(dataframe)
    fig = px.bar(result, x='department', y='count', title='Departments',color='department',color_discrete_sequence=custom_colors)
    return fig

def plotlocation(dataframe):
    result = countlocation(dataframe)
    # Create a map object
    world_map = folium.Map()
    # Initialize the geocoder with your API key
    geocoder = OpenCageGeocode("001a4519b76e4c4480b90ea3643a4e31")
    # Create a dictionary to store geocoded coordinates
    coordinates = {}
    for _, row in result.iterrows():
        country_name = row['Location']
        # Check if coordinates are already geocoded
        if country_name in coordinates:
            latitude, longitude = coordinates[country_name]
        else:
            # Geocode the country name to get the coordinates
            results = geocoder.geocode(country_name)
            latitude = results[0]['geometry']['lat']
            longitude = results[0]['geometry']['lng']
            # Cache the geocoded coordinates
            coordinates[country_name] = (latitude, longitude)
        folium.Marker(location=(latitude, longitude), popup=str(row['Count'])).add_to(world_map)
    return world_map

    
def plottime(dataframe):
    custom_colors = ['#e76895', '#b557c3', '#9d57cb', '#e9b8a9','#efe7e3'] 
    result=counttime(dataframe)
    fig = px.pie(result, names='time', values='count', title='Time',color='time',color_discrete_sequence=custom_colors)
    # fig = px.bar(data_frame=result, x='time', y='count', title='Time')
    return fig

def plottags(dataframe):
    custom_colors = ['#e76895', '#b557c3', '#9d57cb', '#e9b8a9','#efe7e3'] 
    result=counttags(dataframe)
    fig = px.bar(data_frame=result, x='Frequency', y='Tag', title='Tags',orientation='h',color='Tag',
             color_discrete_sequence=custom_colors)
    # fig = px.pie(result, names='tag', values='count', title='Tags')
    return fig
