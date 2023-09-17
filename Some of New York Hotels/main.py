import folium
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('newyork.csv')

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

loc=folium.Map(location=[data['latitude'].mean(),data['longitude'].mean()],zoom_start=12)
loc.get_root().header.add_child(folium.Element(popup_style))
   
for index, row in data.iterrows():
    name=row['name']
    lat=row['latitude']
    lng=row['longitude']
    neighbourhood=row['neighbourhood']
    price=row['price']
    neighbourhood_group=row['neighbourhood_group']
    host_id=row['host_id']
    host_name=row['host_name']
    review_count = row['number_of_reviews']

    popup_content = f"""
        <div class="popup-content">
            <div class="popup-title">{name}</div>
            <b>Neighbourhood :</b> {neighbourhood}<br>
            <b>Neighbourhood Group :</b> {neighbourhood_group}<br>
            <b>Price :</b> {price}$<br>
            <b>Host Name :</b> {host_name}<br>
            <b>Host Id :</b> {host_id}<br>
            <b>Lat :</b> {lat}<br>
            <b>Lng :</b> {lng}
        </div>
    """

    popup=folium.Popup(popup_content,max_width=400)
    folium.Marker(location=[lat,lng],popup=popup).add_to(loc)

loc.save('map.html')

grouped_data = data.groupby('neighbourhood_group')['number_of_reviews'].sum().reset_index()
total_reviews = grouped_data['number_of_reviews'].sum()
grouped_data['percentage'] = (grouped_data['number_of_reviews'] / total_reviews) * 100

threshold_percentage = 2  
filtered_data = grouped_data[grouped_data['percentage'] >= threshold_percentage]

plt.figure(figsize=(8, 8))
plt.pie(filtered_data['number_of_reviews'], labels=filtered_data['neighbourhood_group'], autopct='%1.1f%%')
plt.title('Total Number of Reviews by Neighbourhood Group (Threshold: %2 and above)')
plt.legend(filtered_data['neighbourhood_group'], title="Neighbourhood Group", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()