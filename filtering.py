import pandas as pd

def filter_dataframe(data,columns_to_filter,values_to_filter):
    filtered_df = data.query(' and '.join(f'{col} == "{val}"' for col, val in zip(columns_to_filter, values_to_filter)))
    return filtered_df
