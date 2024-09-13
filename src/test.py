import streamlit as st
import pandas as pd
import numpy as np 
import plotly.graph_objects as go
import plotly.express as px
import os
import json

# Create a DataFrame or dictionary with some sample data to map onto the geojson
# data = {
#     'BEZIRKSNUM': [1901, 1843],  # Example district number (must match "BEZIRKSNUM" in GeoJSON)
#     'EINWOHNERZ': [78305, 92000]  # Example population data to map
# }
# df = pd.DataFrame(data)

# df = pd.read_csv('../data/processed/geojson_df_including_pops.csv', encoding='utf-8')

import plotly.express as px
import json

# Load GeoJSON data
with open('../data/raw/pop_cant.geojson') as f:
    geojson_data = json.load(f)

# Create a Plotly map
fig = px.choropleth_mapbox(
    geojson=geojson_data,
    locations=[feature['properties']['NAME_1'] for feature in geojson_data['features']],  # Extract place names
    color=[feature['properties']['POPULATION'] for feature in geojson_data['features']],  # Extract population values
    geojson=geojson_data,
    featureidkey="properties.NAME_1",  # Property name in GeoJSON
    color_continuous_scale="Viridis",  # Color scale
    mapbox_style="carto-positron",
    center={"lat": 47.0, "lon": 8.0},  # Center map on Switzerland (adjust as necessary)
    zoom=7,
    title="Population by Canton"
)

fig.show()



# import json

# def extract_bezirksnum_name_mapping(geojson_file):
#     with open(geojson_file, 'r') as file:
#         geojson_data = json.load(file)
    
#     bezirksnum_name_map = {}
#     for feature in geojson_data['features']:
#         properties = feature['properties']
#         if 'BEZIRKSNUM' in properties and 'NAME' in properties:
#             bezirksnum = properties['BEZIRKSNUM']
#             name = properties['NAME']
#             bezirksnum_name_map[bezirksnum] = name
    
#     return bezirksnum_name_map

# # Usage
# bezirksnum_name_mapping = extract_bezirksnum_name_mapping('../data/raw/ch-districts.geojson')
# print(bezirksnum_name_mapping)


# def save_bezirksnum_name_to_csv(geojson_file, output_csv_file):
#     # Extract the mapping
#     bezirksnum_name_mapping = extract_bezirksnum_name_mapping(geojson_file)
    
#     # Convert to DataFrame
#     df = pd.DataFrame(list(bezirksnum_name_mapping.items()), columns=['BEZIRKSNUM', 'NAME'])
    
#     # Save to CSV
#     df.to_csv(output_csv_file, encoding='utf-8')

# # Usage
# save_bezirksnum_name_to_csv('../data/raw/ch-districts.geojson', 'bezirksnum_name_mapping.csv')



