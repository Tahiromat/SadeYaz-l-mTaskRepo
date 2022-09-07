import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly, plot_cross_validation_metric
from prophet.diagnostics import performance_metrics, cross_validation
from sklearn.metrics import mean_squared_error, mean_absolute_error 

data = pd.read_csv('organized_data.csv', index_col=[0], parse_dates=[0])
data = data.resample('D').mean()

def create_features(df, label=None):
    """
    Creates time series features from datetime index.
    """
    df = df.copy()
    df['date'] = df.index
    # df['hour'] = df['date'].dt.hour
    df['dayofweek'] = df['date'].dt.dayofweek
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['date'].dt.day
    df['weekofyear'] = df['date'].dt.weekofyear
    
    X = df[['dayofweek','quarter','month','year',
           'dayofyear','dayofmonth','weekofyear']]
    if label:
        y = df[label]
        return X, y
    return X

X, y = create_features(data, label='PJM_Load_MW')
features_and_target = pd.concat([X, y], axis=1)

split_date = '2001-01-01'
pjme_train = data.loc[data.index <= split_date].copy()
pjme_test = data.loc[data.index > split_date].copy()

model = Prophet()
model.fit(pjme_train.reset_index().rename(columns={'Datetime':'ds', 'PJM_Load_MW':'y'}))
forecast = model.predict(df=pjme_test.reset_index().rename(columns={'Datetime':'ds'}))

st.write(features_and_target)
st.write(pjme_train)
st.write(pjme_test)
st.write(forecast)

fig = px.line(pjme_train, x=pjme_train.index, y = pjme_train['PJM_Load_MW'], title='Daily Electricity Consumption Forecast ')
fig.add_scatter(x=pjme_test.index, y= pjme_test['PJM_Load_MW'])
fig.add_scatter(x=forecast['ds'], y= forecast['yhat'])
st.plotly_chart(fig)

fig2 = plot_components_plotly(model, forecast) 
st.plotly_chart(fig2)

mse  = mean_squared_error(y_true=pjme_test['PJM_Load_MW'], y_pred=forecast['yhat'])
mae = mean_absolute_error(y_true=pjme_test['PJM_Load_MW'], y_pred=forecast['yhat'])

def mean_absolute_percentage_error(y_true, y_pred): 
    """Calculates MAPE given y_true and y_pred"""
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

mape = mean_absolute_percentage_error(y_true=pjme_test['PJM_Load_MW'], y_pred=forecast['yhat'])

st.write(mape)