import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.header('Used Cars Market')
st.write('Filter the data below by the ads by car model')

df = pd.read_csv('/Users/sabrinamcfield/Desktop/4_sprint_project/sprint_4_project/vehicles_us.csv')

df['model'] = df['model'].str.replace(r'[\s-]', '_', regex=True) #removes whitespace and hypens from 'model' column.
df['type'] = df['type'].str.lower() #lowercase the 'type' column
df = df.dropna().reset_index(drop=True) #drop missing values and reset the index while dropping the old index
df['date_posted'] = pd.to_datetime(df['date_posted']) #convert 'date_posted' column to datetimeIndex type
df[['model_year','odometer','cylinders']] = df[['model_year','odometer','cylinders']].astype(int)  #convert float columns to integers


car_model = sorted(df['model'].unique())

selected_menu = st.selectbox('Select a car model', car_model)

min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())

year_range = st.slider('Choose year', value=(min_year, max_year), min_value=min_year, max_value=max_year)
year_range[0]
year_range[1]

actual_range = list(range(year_range[0],year_range[1]+1))

df_filtered = df[ (df.model == selected_menu) & (df.model_year.isin(list(actual_range)))]

df_filtered