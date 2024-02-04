# from flask import Flask, render_template
# import folium
# from faker import Faker
# from datetime import datetime, timedelta
# import random

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Generate a dummy dataset with 100 data points, including 20 fire incidents, within the Delhi region
#     dummy_data_delhi_fire = generate_dummy_fire_dataset_delhi(100, 20)

#     # Create an interactive map using Folium and Leaflet
#     my_map_delhi_fire = folium.Map(location=[28.6139, 77.2090], zoom_start=10, control_scale=True)

#     # Add markers to the map for each data point
#     for data_point in dummy_data_delhi_fire:
#         if data_point['fire_incident']:
#             # Use a different marker color for fire incidents
#             folium.Marker(
#                 location=[float(data_point['latitude']), float(data_point['longitude'])],
#                 popup=f"Fire Incident\nTimestamp: {data_point['timestamp']}",
#                 icon=folium.Icon(color='red')
#             ).add_to(my_map_delhi_fire)
#         else:
#             folium.Marker(
#                 location=[float(data_point['latitude']), float(data_point['longitude'])],
#                 popup=f"No Fire Incident\nTimestamp: {data_point['timestamp']}",
#                 icon=folium.Icon(color='blue')
#             ).add_to(my_map_delhi_fire)

#     # Save the map to a temporary HTML file
#     map_html_path = 'templates/map.html'
#     my_map_delhi_fire.save(map_html_path)

#     # Render the HTML template with the map
#     return render_template('dashboard.html')

# # Function to generate a dummy dataset within the Delhi region
# def generate_dummy_fire_dataset_delhi(num_points, num_fire_incidents):
#     fake = Faker()

#     # Define latitude and longitude range for Delhi
#     delhi_latitude_range = (28.5, 28.9)
#     delhi_longitude_range = (76.8, 77.5)

#     dataset = []

#     for _ in range(num_points - num_fire_incidents):
#         # Generate latitude and longitude within the specified range around Delhi for non-fire incidents
#         latitude = random.uniform(*delhi_latitude_range)
#         longitude = random.uniform(*delhi_longitude_range)

#         timestamp = (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat()

#         dataset.append({
#             'latitude': latitude,
#             'longitude': longitude,
#             'timestamp': timestamp,
#             'fire_incident': False
#         })

#     for _ in range(num_fire_incidents):
#         # Generate latitude and longitude within the specified range around Delhi for fire incidents
#         latitude = random.uniform(*delhi_latitude_range)
#         longitude = random.uniform(*delhi_longitude_range)

#         timestamp = (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat()

#         dataset.append({
#             'latitude': latitude,
#             'longitude': longitude,
#             'timestamp': timestamp,
#             'fire_incident': True
#         })

#     return dataset

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
import folium
import random
from datetime import datetime, timedelta
from sklearn.cluster import KMeans
from faker import Faker

app = Flask(__name__)

def generate_dummy_fire_dataset_delhi(num_points, num_fire_incidents):
    # Your existing function code remains the same
    fake = Faker()

    delhi_latitude_range = (28.5, 28.9)
    delhi_longitude_range = (76.8, 77.5)

    dataset = []

    for _ in range(num_points - num_fire_incidents):
        latitude = random.uniform(*delhi_latitude_range)
        longitude = random.uniform(*delhi_longitude_range)

        timestamp = (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat()

        dataset.append({
            'latitude': latitude,
            'longitude': longitude,
            'timestamp': timestamp,
            'fire_incident': False
        })

    for _ in range(num_fire_incidents):
        latitude = random.uniform(*delhi_latitude_range)
        longitude = random.uniform(*delhi_longitude_range)

        timestamp = (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat()

        dataset.append({
            'latitude': latitude,
            'longitude': longitude,
            'timestamp': timestamp,
            'fire_incident': True
        })

    return dataset

def apply_kmeans(coordinates, num_clusters):
    # Your existing function code remains the same
    kmeans = KMeans(n_clusters=num_clusters, random_state=42).fit(coordinates)
    clusters = kmeans.predict(coordinates)
    return clusters

def visualize_map(dummy_data, clusters, num_clusters):
    my_map = folium.Map(location=[28.6139, 77.2090], zoom_start=10, control_scale=True)

    # Your existing visualization code remains the same
    my_map = folium.Map(location=[28.6139, 77.2090], zoom_start=10, control_scale=True)

    # Define cluster colors
    cluster_colors = ['red', 'blue', 'green']

    for idx, data_point in enumerate(dummy_data):
        cluster_label = clusters[idx]
        cluster_color = cluster_colors[cluster_label]

        folium.Marker(
            location=[data_point['latitude'], data_point['longitude']],
            popup=f"Cluster: {cluster_label + 1}\nTimestamp: {data_point['timestamp']}",
            icon=folium.Icon(color=cluster_color)
        ).add_to(my_map)

    #my_map.save('kmeans_map.html')

    my_map.save('templates/kmeans_map.html')  # Save the map in the 'templates' folder

@app.route('/')
def index():
    num_points = 100
    num_fire_incidents = 20
    num_clusters = 3

    dummy_data = generate_dummy_fire_dataset_delhi(num_points, num_fire_incidents)
    coordinates = [[data_point['latitude'], data_point['longitude']] for data_point in dummy_data]
    clusters = apply_kmeans(coordinates, num_clusters)

    # Print the assigned clusters for debugging
    print("Assigned Clusters:", clusters)

    
    visualize_map(dummy_data, clusters, num_clusters)
    return render_template('kmeans_map.html')  # Render the HTML template containing the map

if __name__ == '__main__':
    app.run(debug=True)


