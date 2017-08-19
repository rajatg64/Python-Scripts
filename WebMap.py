__author__ = 'RAJAT'
import folium
import geocoder
import pandas as pd
g = geocoder.ip('me')
print(g.latlng)
print(dir(folium))
map = folium.Map(location=[g.latlng[0], g.latlng[1]], zoom_start=15,  tiles='Stamen Terrain')
print(map)
print(map.save('map.html'))

folium.Marker(location=[g.latlng[0], g.latlng[1]], popup='I am here', icon=folium.Icon(color='green')).add_to(map)

folium.Marker(location=[12.851625, 77.666283], popup='But i can see you' , icon=folium.Icon(icon='cloud')).add_to(map)

map.save('map.html')


df = pd.read_csv('location.txt')

# # Take the Avg
# latmean = df['LAT'].mean()
# lonmean = df['LON'].mean()
#
# map1=folium.Map(location=[latmean, lonmean], zoom_start=15,  tiles='Stamen Terrain')

for name, lon, lat in zip(df['NAME'], df['LON'], df['LAT']):
    print(lat, lon, name)
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(icon='cloud')).add_to(map)
print('success')
map.save('map.html')