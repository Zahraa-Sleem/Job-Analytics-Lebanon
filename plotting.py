import plotly.express as px
from statistics_1 import *
import folium
import json

def plotdepartments(dataframe):
    result=countdepartment(dataframe)
    fig = px.pie(result, names='department', values='count', title='Departments')
    return fig

# def plotlocation(dataframe):
#     # Load the GeoJSON data for country boundaries
#     geojson_data = folium.datasets.geojson.WorldCountries
#     # Create a map centered at a specific location
#     m = folium.Map(location=[0, 0], zoom_start=2)
#     # Create a Choropleth map
#     folium.Choropleth(
#         geo_data=geojson_data,
#         name='choropleth',
#         data=dataframe,
#         columns=['Country', 'Value'],
#         key_on='feature.properties.name',
#         fill_color='green',
#         fill_opacity=0.7,
#         line_opacity=0.2,
#         legend_name='Value'
#     ).add_to(m)
#     # Find the value for the specified country in the DataFrame
#     country_value = dataframe.loc[dataframe['Country'] == location, 'Value'].values[0]
#     # Add a marker to the specified country with the value as a popup
#     folium.Marker(location=[0, 0], popup=str(country_value), icon=folium.Icon(color='green')).add_to(m)
#     # Display the map
#     return m
    
def plottime(dataframe):
    result=counttime(dataframe)
    fig = px.bar(data_frame=result, x='time', y='count', title='Time')
    return fig

def plotjobtitles(dataframe):
    result=countjobs(dataframe)
    fig = px.pie(result, names='title', values='count', title='Titles')
    return fig
