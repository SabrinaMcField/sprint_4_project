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

st.header('Price Analysis')
st.write("""
##### Lets analyze the what factor influences the price the most. We will consider how distribution of price varies depending on transmission, type, fuel and condition
""")

list_for_hist = ['transmission','type','condition', 'fuel']

selected_type = st.selectbox('Select for price distribution', list_for_hist)

fig1 = px.histogram(df, x='price', color= selected_type)
fig1.update_layout(title='<b>Split of price by {}<b>'.format(selected_type))
st.plotly_chart(fig1)

df['age'] = 2024 - df['model_year']

def age_category(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'

df['age_category'] = df['age'].apply(age_category)

list_for_scatter = ['odometer', 'days_listed']

choice_for_scatter = st.selectbox('Price dependency on', list_for_scatter)

fig2 = px.scatter(df, x='price', y=choice_for_scatter, color='age_category', hover_data=['model_year'])

st.plotly_chart(fig2)
fig2.update_layout(title='<b>Price vs {}<b>'.format(choice_for_scatter))
