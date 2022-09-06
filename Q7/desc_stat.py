import pandas as pd
import plotly.express as px
import streamlit as st

data = pd.read_csv('organized_data.csv', index_col=[0], parse_dates=[0])

# That command will manage the Streamlit layouts
st.set_page_config(page_title="Deep Analysis", page_icon="❗", layout="wide")
hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

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
    
    X = df[['dayofweek','quarter','month','year', 'dayofyear','dayofmonth','weekofyear']]
    if label:
        y = df[label]
        return X, y
    return X

X, y = create_features(data, label='PJM_Load_MW')
data = pd.concat([X, y], axis=1)

st.write(data)

for i in data.columns[:-1]:
    df = data[[i, 'PJM_Load_MW']].copy()
    df = df.groupby([i]).mean()
    st.write(df)
    fig = px.line(x=df.index, y=df['PJM_Load_MW'])
    fig.layout.update(title_text="MEAN ------ " + i, width=800, height=600, xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

























# BOX PLOT DESCRIPTION : https://yalin-dunya.com/2020/06/19/kutu-grafigi-boxplot/#:~:text=Bir%20kutu%20grafi%C4%9Fi%20(Boxplot)%2C,s%C4%B1kl%C4%B1kla%20kullan%C4%B1lan%20bir%20grafik%20t%C3%BCr%C3%BCd%C3%BCr.