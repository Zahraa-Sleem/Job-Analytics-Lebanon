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