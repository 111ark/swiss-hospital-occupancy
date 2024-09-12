from arcgis.gis import GIS
from arcgis.features import FeatureLayer
import requests

# Connect to ArcGIS Online
gis = GIS("home")

# Specify the item ID and layer ID (replace with the correct IDs)
item_id = 'a58386ecf0404dd09a4abc0bcd607561'  # Replace with your item ID
layer_id = '0'  # Replace with the correct sublayer ID if applicable

# Get the item
item = gis.content.get(item_id)

# Access the feature layer
feature_layer = FeatureLayer(item.layers[int(layer_id)].url)

# Define the query parameters
params = {
    'where': '1=1',  # Query all records
    'outFields': '*',  # All fields
    'f': 'geojson'  # Output format
}

# Query the feature layer
response = feature_layer.query(**params)

# Save the GeoJSON data to a file
geojson_data = response.to_geojson()
with open('data.geojson', 'w') as f:
    f.write(geojson_data)

