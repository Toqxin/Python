import folium
import pandas as pd

data = pd.read_csv('deutsch.csv')

m = folium.Map(location=[data['lat'].mean(), data['lng'].mean()], zoom_start=6)

popup_style = """
    <style>
        .popup-content {
            font-size: 16px;
        }
        .popup-title {
            font-size: 18px;
            font-weight: bold;
        }
    </style>
"""

m.get_root().header.add_child(folium.Element(popup_style))

for index, row in data.iterrows():
    city = row['city']
    lat = row['lat']
    lng = row['lng']
    country = row['country']
    population = row['population']

    popup_content = f"""
        <div class="popup-content">
            <div class="popup-title"><b>City:</b> {city}</div>
            <b>Country:</b> {country}<br>
            <b>Population:</b> {population}<br>
            <b>Lat:</b> {lat}<br>
            <b>Lng:</b> {lng}
        </div>
    """

    popup = folium.Popup(popup_content, max_width=200)
    folium.Marker(location=[lat, lng], popup=popup).add_to(m)

m.save('map.html')  

