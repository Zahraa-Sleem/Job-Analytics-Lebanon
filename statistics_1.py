import pandas as pd

def countdepartment(data):
    department_frequency = data['department'].value_counts()
    # convert the Pandas Series object to a DataFrame
    df_frequency_department = department_frequency.reset_index()
    # rename the columns of the DataFrame
    df_frequency_department.columns = ['department', 'count']
    return df_frequency_department


def countlocation(data):
    location_frequency = data['location'].value_counts()
    # convert the Pandas Series object to a DataFrame
    df_frequency_locations = location_frequency.reset_index()
    # rename the columns of the DataFrame
    df_frequency_locations.columns = ['location', 'count']
    return df_frequency_locations
    
def counttime(data):
    time_frequency = data['time'].value_counts()
    # convert the Pandas Series object to a DataFrame
    df_frequency_time = time_frequency.reset_index()
    # rename the columns of the DataFrame
    df_frequency_time.columns = ['time', 'count']
    return df_frequency_time

def countjobs(data):
    title_frequency = data['jobtitle'].value_counts()
    # convert the Pandas Series object to a DataFrame
    df_frequency_title = title_frequency.reset_index()
    # rename the columns of the DataFrame
    df_frequency_title .columns = ['title', 'count']
    return df_frequency_title


