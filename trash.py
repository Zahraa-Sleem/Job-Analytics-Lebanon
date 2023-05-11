# def countjob():
#     jobtitle_frequency = data['jobtitle'].value_counts()
#     # convert the Pandas Series object to a DataFrame
#     df_frequency_jobtitle =  jobtitle_frequency .reset_index()
#     # rename the columns of the DataFrame
#     df_frequency_jobtitle.columns = ['jobtitle', 'count']
#     print(df_frequency_jobtitle)
# def filter_dataframe(df, column_name, value):
#     """
#     Returns the rows where the values in a column are equal to a specific value.
#     Args:
#         data: Pandas DataFrame to filter
#         column_name: Name of the column to filter on
#         value: The specific value to look for in the column
#     Returns:
#         A new Pandas DataFrame containing the rows where the values in the specified column are equal to the specified value.
#     """
#     return data[data[column_name] == value]