import pandas as pd
import json
def getdepartments(dataframe):
    departments_old = dataframe['department'].unique()
    departments = ['']+departments_old.tolist()
    return departments
def getlocations(dataframe):
    locations_old = dataframe['location'].unique()
    locations =['']+locations_old.tolist()
    return locations
def gettime(dataframe):
    times_old = dataframe['time'].unique()
    times =['']+times_old.tolist()
    return times

