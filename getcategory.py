import pandas as pd
import json
def getdepartments(dataframe):
    departments = dataframe['department'].unique()
    print(departments)
def getlocations(dataframe):
    locations = dataframe['location'].unique()
    print(locations)
def gettime(dataframe):
    times = dataframe['time'].unique()
    print(times)

with open('objects.json') as f:
    data = json.load(f)
dataframe= pd.read_json(json.dumps(data))

