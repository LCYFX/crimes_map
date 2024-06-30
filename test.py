import pandas as pd
import folium
from folium.plugins import HeatMap

df=pd.read_csv('dumpsites.csv')
print(df.head())
df.dropna(subset=['Population Density'],axis=0,inplace=True)

m=folium.Map(location=[df.Lat.mean(),df.Lon.mean()], zoom_start=6, control_scale=True)
map_values=df[['Lat','Lon', 'Population Density']]
data=map_values.values.tolist()
hm=HeatMap(data, gradient={0.4: 'blue', 0.65: 'lime', 1: 'red'},min_opacity=0.05,max_opacity=9,radius=25).add_to(m)
m.show_in_browser()


