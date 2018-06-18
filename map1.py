import folium
import pandas
data=pandas.read_csv('volcanoes.txt')

lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])

map=folium.Map(location=[45.49,-73.58], zoom_start=6, tiles="Mapbox Bright")
fg= folium.FeatureGroup(name='My Map')

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el) +" m", icon=folium.Icon(color='blue')))

map.add_child(fg)

map.save("Map1.html")
