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

# from flask import Flask, render_template
# import folium
# import random
# from datetime import datetime, timedelta
# from sklearn.cluster import KMeans
# from faker import Faker

# app = Flask(__name__)
# hospitals_data = [{'latitude': 28.58, 'longitude': 77.20, 'name': 'Hospital 1'},
#         {'latitude': 28.59, 'longitude': 77.23, 'name': 'Hospital 2'}]
# fire_stations_data = [{'latitude': 28.619, 'longitude': 77.069, 'name': 'Fire Station 1'},
#     {'latitude': 28.564, 'longitude': 77.244, 'name': 'Fire Station 2'},
#     {'latitude': 28.654, 'longitude': 77.178, 'name': 'Fire Station 3'},
#     {'latitude': 28.587, 'longitude': 77.243, 'name': 'Fire Station 4'},
#     {'latitude': 28.623, 'longitude': 77.193, 'name': 'Fire Station 5'},
#     {'latitude': 28.575, 'longitude': 77.198, 'name': 'Fire Station 6'},
#     {'latitude': 28.611, 'longitude': 77.221, 'name': 'Fire Station 7'},
#     {'latitude': 28.639, 'longitude': 77.094, 'name': 'Fire Station 8'},
#     {'latitude': 28.599, 'longitude': 77.267, 'name': 'Fire Station 9'},
#     {'latitude': 28.552, 'longitude': 77.185, 'name': 'Fire Station 10'},
#     {'latitude': 28.632, 'longitude': 77.121, 'name': 'Fire Station 11'},
#     {'latitude': 28.602, 'longitude': 77.252, 'name': 'Fire Station 12'},
#     {'latitude': 28.571, 'longitude': 77.231, 'name': 'Fire Station 13'},
#     {'latitude': 28.648, 'longitude': 77.173, 'name': 'Fire Station 14'},
#     {'latitude': 28.619, 'longitude': 77.200, 'name': 'Fire Station 15'}]
# def generate_dummy_fire_dataset_delhi(num_points, num_fire_incidents):
#     # Your existing function code remains the same
#     fake = Faker()

#     delhi_latitude_range = (28.5, 28.9)
#     delhi_longitude_range = (76.8, 77.5)

#     dataset = []

#     for _ in range(num_points - num_fire_incidents):
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

# def apply_kmeans(coordinates, num_clusters):
#     # Your existing function code remains the same
#     kmeans = KMeans(n_clusters=num_clusters, random_state=42).fit(coordinates)
#     clusters = kmeans.predict(coordinates)
#     return clusters

# def visualize_map(dummy_data, clusters, num_clusters,fire_stations_data,hospitals_data):

    

#     my_map = folium.Map(location=[28.6139, 77.2090], zoom_start=10, control_scale=True)

#     # Your existing visualization code remains the same
#     my_map = folium.Map(location=[28.6139, 77.2090], zoom_start=10, control_scale=True)

#     # Define cluster colors
#     cluster_colors = ['red', 'blue', 'green']

#     for idx, data_point in enumerate(dummy_data):
#         cluster_label = clusters[idx]
#         cluster_color = cluster_colors[cluster_label]

#         folium.Marker(
#             location=[data_point['latitude'], data_point['longitude']],
#             popup=f"Cluster: {cluster_label + 1}\nTimestamp: {data_point['timestamp']}",
#             icon=folium.Icon(color=cluster_color)
#         ).add_to(my_map)

#     #my_map.save('kmeans_map.html')
#     for fire_station in fire_stations_data:
#         folium.Marker(
#             location=[fire_station['latitude'], fire_station['longitude']],
#             popup=f"Fire Station: {fire_station['name']}",
#             icon=folium.Icon(color='black')
#         ).add_to(my_map)

#     # Add markers for hospitals
#     for hospital in hospitals_data:
#         folium.Marker(
#             location=[hospital['latitude'], hospital['longitude']],
#             popup=f"Hospital: {hospital['name']}",
#             icon=folium.Icon(color='pink')
#         ).add_to(my_map)

#     my_map.save('templates/kmeans_map.html')  # Save the map in the 'templates' folder

# @app.route('/')
# def index():
#     num_points = 100
#     num_fire_incidents = 20
#     num_clusters = 3

#     dummy_data = generate_dummy_fire_dataset_delhi(num_points, num_fire_incidents)
#     coordinates = [[data_point['latitude'], data_point['longitude']] for data_point in dummy_data]
#     clusters = apply_kmeans(coordinates, num_clusters)

#     # Print the assigned clusters for debugging
#     print("Assigned Clusters:", clusters)

#     fire_stations_data = [{'latitude': 28.619, 'longitude': 77.069, 'name': 'Fire Station 1'},
#     {'latitude': 28.564, 'longitude': 76.803, 'name': 'Fire Station 2'},
#     {'latitude': 28.654, 'longitude': 77.178, 'name': 'Fire Station 3'},
#     {'latitude': 28.507, 'longitude': 76.935, 'name': 'Fire Station 4'},
#     {'latitude': 28.784, 'longitude': 77.555, 'name': 'Fire Station 5'},
#     {'latitude': 28.720, 'longitude': 77.198, 'name': 'Fire Station 6'},
#     {'latitude': 28.810, 'longitude': 77.347, 'name': 'Fire Station 7'},
#     {'latitude': 28.894, 'longitude': 77.418, 'name': 'Fire Station 8'},
#     {'latitude': 28.850, 'longitude': 76.874, 'name': 'Fire Station 9'},
#     {'latitude': 28.673, 'longitude': 76.904, 'name': 'Fire Station 10'},
#     {'latitude': 28.685, 'longitude': 77.498, 'name': 'Fire Station 11'},
#     {'latitude': 28.516, 'longitude': 77.201, 'name': 'Fire Station 12'},
#     {'latitude': 28.584, 'longitude': 77.231, 'name': 'Fire Station 13'},
#     {'latitude': 28.835, 'longitude': 77.343, 'name': 'Fire Station 14'},
#     {'latitude': 28.759, 'longitude': 76.200, 'name': 'Fire Station 15'}]

#     hospitals_data = [ {'latitude': 28.58, 'longitude': 77.20, 'name': 'Hospital 1'},
#     {'latitude': 28.59, 'longitude': 77.18, 'name': 'Hospital 2'},
#     {'latitude': 28.53, 'longitude': 77.21, 'name': 'Hospital 3'},
#     {'latitude': 28.60, 'longitude': 77.42, 'name': 'Hospital 4'},
#     {'latitude': 28.75, 'longitude': 77.39, 'name': 'Hospital 5'},
#     {'latitude': 28.65, 'longitude': 76.9, 'name': 'Hospital 6'},
#     {'latitude': 28.80, 'longitude': 77.29, 'name': 'Hospital 7'},
#     {'latitude': 28.72, 'longitude': 77.04, 'name': 'Hospital 8'},
#     {'latitude': 28.86, 'longitude': 77.45, 'name': 'Hospital 9'},
#     {'latitude': 28.83, 'longitude': 77.09, 'name': 'Hospital 10'}]
#     visualize_map(dummy_data, clusters, num_clusters,fire_stations_data,hospitals_data)
#     return render_template('kmeans_map.html')  # Render the HTML template containing the map

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template
import folium
import random
from datetime import datetime, timedelta
from sklearn.cluster import KMeans
from faker import Faker

app = Flask(__name__)
hospitals_data = [{'latitude': 28.58, 'longitude': 77.20, 'name': 'Hospital 1'},
        {'latitude': 28.59, 'longitude': 77.23, 'name': 'Hospital 2'}]
fire_stations_data = [{'latitude': 28.619, 'longitude': 77.069, 'name': 'Fire Station 1'},
    {'latitude': 28.564, 'longitude': 77.244, 'name': 'Fire Station 2'},
    {'latitude': 28.654, 'longitude': 77.178, 'name': 'Fire Station 3'},
    {'latitude': 28.587, 'longitude': 77.243, 'name': 'Fire Station 4'},
    {'latitude': 28.623, 'longitude': 77.193, 'name': 'Fire Station 5'},
    {'latitude': 28.575, 'longitude': 77.198, 'name': 'Fire Station 6'},
    {'latitude': 28.611, 'longitude': 77.221, 'name': 'Fire Station 7'},
    {'latitude': 28.639, 'longitude': 77.094, 'name': 'Fire Station 8'},
    {'latitude': 28.599, 'longitude': 77.267, 'name': 'Fire Station 9'},
    {'latitude': 28.552, 'longitude': 77.185, 'name': 'Fire Station 10'},
    {'latitude': 28.632, 'longitude': 77.121, 'name': 'Fire Station 11'},
    {'latitude': 28.602, 'longitude': 77.252, 'name': 'Fire Station 12'},
    {'latitude': 28.571, 'longitude': 77.231, 'name': 'Fire Station 13'},
    {'latitude': 28.648, 'longitude': 77.173, 'name': 'Fire Station 14'},
    {'latitude': 28.619, 'longitude': 77.200, 'name': 'Fire Station 15'}]
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

def visualize_map(dummy_data, clusters, num_clusters,fire_stations_data,hospitals_data):



    my_map = folium.Map(location=[28.6139, 77.2090], zoom_start=10, control_scale=True)

    # Your existing visualization code remains the same
    my_map = folium.Map(location=[28.6139, 77.2090], zoom_start=10, control_scale=True)

    # Define cluster colors
    cluster_colors = ['red', 'blue', 'green','brown','purple','gray','orange','beige']
    unique_clusters = set(clusters)
    print("Unique Clusters:", unique_clusters)
    for idx, data_point in enumerate(dummy_data):
        cluster_label = clusters[idx]
        cluster_color = cluster_colors[cluster_label]

        folium.Marker(
            location=[data_point['latitude'], data_point['longitude']],
            popup=f"Cluster: {cluster_label + 1}\nTimestamp: {data_point['timestamp']}",
            icon=folium.Icon(color=cluster_color)
        ).add_to(my_map)

    #my_map.save('kmeans_map.html')
    for fire_station in fire_stations_data:
        folium.Marker(
            location=[fire_station['latitude'], fire_station['longitude']],
            popup=f"Fire Station: {fire_station['name']}",
            icon=folium.Icon(color='black')
        ).add_to(my_map)

    # Add markers for hospitals
    for hospital in hospitals_data:
        folium.Marker(
            location=[hospital['latitude'], hospital['longitude']],
            popup=f"Hospital: {hospital['name']}",
            icon=folium.Icon(color='orange')
        ).add_to(my_map)

    my_map.save('templates/kmeans_map.html')  # Save the map in the 'templates' folder

@app.route('/')
def index():
    num_points = 100
    num_fire_incidents = 20
    num_clusters = 5

    dummy_data = generate_dummy_fire_dataset_delhi(num_points, num_fire_incidents)
    coordinates = [[data_point['latitude'], data_point['longitude']] for data_point in dummy_data]
    clusters = apply_kmeans(coordinates, num_clusters)

    # Print the assigned clusters for debugging
    print("Assigned Clusters:", clusters)

    fire_stations_data = [{'latitude': 28.619, 'longitude': 77.069, 'name': 'Fire Station 1'},
    {'latitude': 28.564, 'longitude': 76.803, 'name': 'Fire Station 2'},
    {'latitude': 28.654, 'longitude': 77.178, 'name': 'Fire Station 3'},
    {'latitude': 28.507, 'longitude': 76.935, 'name': 'Fire Station 4'},
    {'latitude': 28.784, 'longitude': 77.555, 'name': 'Fire Station 5'},
    {'latitude': 28.720, 'longitude': 77.198, 'name': 'Fire Station 6'},
    {'latitude': 28.810, 'longitude': 77.347, 'name': 'Fire Station 7'},
    {'latitude': 28.894, 'longitude': 77.418, 'name': 'Fire Station 8'},
    {'latitude': 28.850, 'longitude': 76.874, 'name': 'Fire Station 9'},
    {'latitude': 28.673, 'longitude': 76.904, 'name': 'Fire Station 10'},
    {'latitude': 28.685, 'longitude': 77.498, 'name': 'Fire Station 11'},
    {'latitude': 28.516, 'longitude': 77.201, 'name': 'Fire Station 12'},
    {'latitude': 28.584, 'longitude': 77.231, 'name': 'Fire Station 13'},
    {'latitude': 28.835, 'longitude': 77.343, 'name': 'Fire Station 14'},
    {'latitude': 28.759, 'longitude': 76.200, 'name': 'Fire Station 15'}]

    hospitals_data = [ {'latitude': 28.58, 'longitude': 77.20, 'name': 'Hospital 1'},
    {'latitude': 28.59, 'longitude': 77.18, 'name': 'Hospital 2'},
    {'latitude': 28.53, 'longitude': 77.21, 'name': 'Hospital 3'},
    {'latitude': 28.60, 'longitude': 77.42, 'name': 'Hospital 4'},
    {'latitude': 28.75, 'longitude': 77.39, 'name': 'Hospital 5'},
    {'latitude': 28.65, 'longitude': 76.9, 'name': 'Hospital 6'},
    {'latitude': 28.80, 'longitude': 77.29, 'name': 'Hospital 7'},
    {'latitude': 28.72, 'longitude': 77.04, 'name': 'Hospital 8'},
    {'latitude': 28.86, 'longitude': 77.45, 'name': 'Hospital 9'},
    {'latitude': 28.83, 'longitude': 77.09, 'name': 'Hospital 10'}]
    visualize_map(dummy_data, clusters, num_clusters,fire_stations_data,hospitals_data)
    return render_template('kmeans_map.html')  # Render the HTML template containing the map

@app.route('/update_fire_data', methods=['POST'])
def update_fire_data():
    # Simulate receiving fire detection data from geotagged cameras
    new_fire_data = request.get_json()

    # Append the new data to the global variable
    dummy_fire_data.extend(new_fire_data)

    # Re-run the clustering and visualization
    coordinates = [[data_point['latitude'], data_point['longitude']] for data_point in dummy_fire_data]
    clusters = apply_kmeans(coordinates, num_clusters=4)
    visualize_map(dummy_fire_data, clusters, fire_stations_data, hospitals_data)

    return jsonify({'message': 'Fire data updated successfully!'})

if __name__ == '__main__':
    app.run(debug=True)