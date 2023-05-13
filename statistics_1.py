import pandas as pd

def countdepartment():
    department_frequency = data['department'].value_counts()
    # convert the Pandas Series object to a DataFrame
    df_frequency_department = department_frequency.reset_index()
    # rename the columns of the DataFrame
    df_frequency_department.columns = ['department', 'count']
    print(df_frequency_department)

def countlocation():
    location_frequency = data['location'].value_counts()
    # convert the Pandas Series object to a DataFrame
    df_frequency_locations = location_frequency.reset_index()
    # rename the columns of the DataFrame
    df_frequency_locations.columns = ['location', 'count']
    print(df_frequency_locations)
    
def counttime():
    time_frequency = data['time'].value_counts()
    # convert the Pandas Series object to a DataFrame
    df_frequency_time = time_frequency.reset_index()
    # rename the columns of the DataFrame
    df_frequency_time.columns = ['time', 'count']
    print(df_frequency_time)

def filter_dataframe(data, column_names, values):
    """
    Returns the rows where the values in multiple columns are equal to specific values.
    Args:
        data: Pandas DataFrame to filter
        column_names: List of column names to filter on
        values: List of specific values to look for in each column
        
    Returns:
        A new Pandas DataFrame containing the rows where the values in the specified columns are equal to the specified values.
    """
    filter_conditions = []
    for column_name, value in zip(column_names, values):
        filter_conditions.append(data[column_name] == value)
    filter_condition = pd.concat(filter_conditions, axis=1).all(axis=1)
    return data[filter_condition]

data = pd.read_json('objects.json')

