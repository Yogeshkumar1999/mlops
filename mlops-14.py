import pandas as pd
#prepare you won dataset and enjoy.
dataset = pd.read_excel("waterwatch_clean2.xlsx")
print dataset.info()
import folium
#newmap = folium.Map(location = [2412, 2342], zoom_start = 12)#less points in lat and log mean no accuracy will see nearby area.
place = dataset[['Latitude' ,'Longitude']]
place.values.tolist()#convert the dataframe to list.
count = 0
cmap = folium.Map(location = [], zoom_start = 10)
for i in place:
    if dataset['Oct 2017\nk1/month'][count] >= 10:
        folium.Marker(
                location = i,
                popup = dataset['suburb'][count],
                icon = folium.Icon(color = 'red', icon = 'tint', icon_color = 'white'),
                icon_color = 'red').add_to(cmap)

    count += 1
print cmap


