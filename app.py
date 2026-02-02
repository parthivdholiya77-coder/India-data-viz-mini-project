import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px 

st.set_page_config(layout='wide')



df = pd.read_csv('dataset/india.csv')

list_of_india = list(df['State'].unique())
list_of_india.insert(0,'Overall India')

st.sidebar.title('India Ka Data Viz')

selected_state = st.sidebar.selectbox('Select a State', list_of_india)

primary = st.sidebar.selectbox(
    'Select Primary Parameter',
    sorted(df.columns[5:])
)

secondary = st.sidebar.selectbox(
    'Select Secondary Parameter',
    sorted(df.columns[5:])
)

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size Represent Primary Parameter')
    st.text('Color Represents Secondary Parameter')
    if selected_state == 'Overall India':

        fig = px.scatter_mapbox(
            df,
            lat='Latitude',
            lon='Longitude',
            height=600,
            zoom=3,
            size=primary,
            color=secondary,
            mapbox_style='carto-positron',
            color_continuous_scale='Viridis',
            size_max=35,
            hover_name='District'
        )

        st.plotly_chart(fig, use_container_width=True,config={"scrollZoom": True})

    else:

        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(
            state_df,
            lat='Latitude',
            lon='Longitude',
            height=600,
            zoom=6,
            size=primary,
            color=secondary,
            mapbox_style='carto-positron',
            color_continuous_scale='Viridis',
            size_max=35,
            hover_name='District'
        )

        st.plotly_chart(fig, use_container_width=True,config={"scrollZoom": True})

        