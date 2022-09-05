import pandas as pd
from plotly import graph_objs as go
import plotly.express as px
import streamlit as st

data = pd.read_csv('organized_data.csv')


# That command will manage the Streamlit layouts
st.set_page_config(page_title="Deep Analysis", page_icon="❗", layout="wide")
hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


def create_time_freq_mean_plots(data):
    '''
    # 
    '''
    for i in data.columns[2:]:
        df = data[[i, 'PJM_Load_MW']].copy()
        df = df.groupby([i]).mean()
        fig = px.line(x=df.index, y=df['PJM_Load_MW'])
        fig.layout.update(title_text="MEAN ------ " + i, width=800, height=600, xaxis_rangeslider_visible=True)

        st.plotly_chart(fig)

def create_time_freq_sum_plots(data):
    '''
    # 
    '''
    for i in data.columns[2:]:
        df = data[[i, 'PJM_Load_MW']].copy()
        df = df.groupby([i]).sum()
        fig = px.line(x=df.index, y=df['PJM_Load_MW'])
        fig.layout.update(title_text="SUM ------ " + i, width=800, height=600, xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

col1, col2 = st.columns(2)

with col1:
    create_time_freq_mean_plots(data)

with col2:
    create_time_freq_sum_plots(data)





# ADD MORE GRAPHS TYPE AND FORMATS































# BOX PLOT DESCRIPTION : https://yalin-dunya.com/2020/06/19/kutu-grafigi-boxplot/#:~:text=Bir%20kutu%20grafi%C4%9Fi%20(Boxplot)%2C,s%C4%B1kl%C4%B1kla%20kullan%C4%B1lan%20bir%20grafik%20t%C3%BCr%C3%BCd%C3%BCr.