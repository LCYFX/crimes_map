import pandas as pd
import plotly.express as px
import folium
from folium.plugins import HeatMap

df=pd.read_csv('robbery.csv')
print(df.head())

fig=px.density_mapbox(df,lat='Latitude',lon='Longitude', z='Beat',radius=20,
                      center=dict(lat=df.Latitude.mean(),lon=df.Longitude.mean()),
                      zoom=4,mapbox_style='open-streetmap', height=900)
fig.show()