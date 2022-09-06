import pandas as pd

data = pd.read_csv('Hourly Load Data.csv', index_col=[0], parse_dates=[0])

print(data.describe().T)

print(data.info())

print(data.isnull().values.any())

print(data.duplicated().any())

data = data.sort_values(by= ['Datetime'], ascending=True)

duplicate = data[data.duplicated()]

# Check if there any missing date and fill it with mean of the column.
missing_datetimes = pd.date_range(start=data.index.min(), end=data.index.max()).difference(data.index)

# Save organized data as .csv file format
data.to_csv('organized_data.csv', index=True)


