import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium


st.header("Select a City and I will show it's Location\n")

df = pd.read_csv('Indian Cities Database.csv')
df = df[['City','lat','lon']]

city_name = st.selectbox('Select any City',(df.City.values))

df = df[df['City']==city_name]

m = folium.Map(location=[df.iloc[[0]].lat,df.iloc[[0]].lon],zoom_start=13)
folium.Marker([df.iloc[[0]].lat,df.iloc[[0]].lon],popup =df.iloc[[0]].City,tooltip=df.iloc[[0]].City).add_to(m)
st_data = st_folium(m, width=725)
st.write(st_data)


