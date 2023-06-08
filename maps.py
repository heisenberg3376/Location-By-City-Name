import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium
import requests


st.header("Select an Indian City and I will show it's Properties\n")

df = pd.read_csv('Indian Cities Database.csv')
df = df[['City','lat','lon']]

city_name = st.selectbox('''## Select any City''',(df.City.values))

df = df[df['City']==city_name]

api_key = '201af41b43acd8890a2b3fcb0cdb68a7'
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={api_key}")

#st.write(weather_data.json())

climate = (weather_data.json().get('weather','')[0].get('main',''))
desc = (weather_data.json().get('weather','')[0].get('description',''))
lat = (weather_data.json().get('coord','').get('lat',''))
lon = (weather_data.json().get('coord','').get('lon',''))
temp = (weather_data.json().get('main','').get('temp',''))
hum = (weather_data.json().get('main','').get('humidity',''))
name = (weather_data.json().get('name',''))

data = pd.DataFrame({'city':name,'Weather':[climate],'description':[desc],'latitude':[lat],'longitude':[lon],'temperature':str("{0:.3f}".format((temp - 32)*(5/9)))+' °C','humidity':str(hum)+'%'},index=['data'])
st.dataframe(data,width=900,use_container_width=True)
m = folium.Map(location=[df.iloc[[0]].lat,df.iloc[[0]].lon],zoom_start=12)
folium.Marker([df.iloc[[0]].lat,df.iloc[[0]].lon],popup =df.iloc[[0]].City,tooltip=df.iloc[[0]].City).add_to(m)
st_data = st_folium(m, width=775)











