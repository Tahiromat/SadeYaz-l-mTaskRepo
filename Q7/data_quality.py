import pandas as pd

data = pd.read_csv('Hourly Load Data.csv', index_col=[0], parse_dates=[0])


data = data.sort_values(by= ['Datetime'], ascending=True)

# def create_features(df, label=None):
#     """
#     Creates time series features from datetime index.
#     """
#     df = df.copy()
#     df['date'] = df.index
#     df['hour'] = df['date'].dt.hour
#     df['dayofweek'] = df['date'].dt.dayofweek
#     df['quarter'] = df['date'].dt.quarter
#     df['month'] = df['date'].dt.month
#     df['year'] = df['date'].dt.year
#     df['dayofyear'] = df['date'].dt.dayofyear
#     df['dayofmonth'] = df['date'].dt.day
#     df['weekofyear'] = df['date'].dt.weekofyear
    
#     X = df[['hour','dayofweek','quarter','month','year',
#            'dayofyear','dayofmonth','weekofyear']]
#     if label:
#         y = df[label]
#         return X, y
#     return X

# X, y = create_features(data, label='PJM_Load_MW')
# data = pd.concat([X, y], axis=1)

# Check if there any missing date and fill it with mean of the column.
missing_datetimes = pd.date_range(start=data.index.min(), end=data.index.max()).difference(data.index)
print(missing_datetimes)

# SAve organized data as .csv file format
data.to_csv('organized_data.csv', index=True)