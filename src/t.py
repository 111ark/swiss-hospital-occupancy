import streamlit as st
import plotly.express as px
import pandas as pd
import json

# Streamlit caching to load data efficiently
@st.cache_data
def load_geojson():
    with open('../data/raw/gemeinden_wus.geojson', 'r') as f:
        return json.load(f)

@st.cache_data
def load_csv_data():
    d_pop = pd.read_csv('../data/processed/pops_left.csv', encoding='utf-8')
    d_coord = pd.read_csv('../data/processed/pops_left_coords.csv', encoding='utf-8')
    h_loc = pd.read_csv('../data/processed/hospitals_collated_reduced.csv', encoding='utf-8')
    return d_pop, d_coord, h_loc

# Load data
geojson = load_geojson()
d_pop, d_coord, h_loc = load_csv_data()

# Process population data
threshold = d_pop['B19BTOT'].quantile(0.95)  # Get the 95th percentile
d_pop['quant95'] = d_pop['B19BTOT'].clip(upper=threshold)  # Cap the outliers

# Create a choropleth map
fig = px.choropleth_mapbox(
    d_coord,
    geojson=geojson,
    color='occupancy',
    locations='gemeinde_NAME',
    featureidkey='properties.gemeinde_NAME',
    color_continuous_scale=px.colors.sequential.algae,
    # hover_data={'B19BTOT': True, 'quant95': False},  # Show original values in the hover box
)

# # Create scatter mapbox trace for hospitals
# scatter_trace = px.scatter_mapbox(
#     h_loc,
#     lat="latitude",
#     lon="longitude",
#     hover_name="Inst",
#     size_max=20,
#     color_discrete_sequence=["cyan"]
# ).data[0]  # Extract the trace object

# # Add the scatter trace to the figure
# fig.add_trace(scatter_trace)

# Update the layout
fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=6,
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    mapbox_center={"lat": 46.800663, "lon": 8.22289}
)

# Streamlit UI
st.title("Population and Hospital Locations in Switzerland")
st.plotly_chart(fig)







# h_loc_sorted = h_loc.sort_values(by='bed_occupancy', ascending=True)
# lowest_value_row = h_loc_sorted.iloc[0]  # Get the uppermost row (lowest value)
# h_loc_sorted = h_loc_sorted.iloc[1:]







# lowest_value_row['hospital']

# lowest_value_row['care_days']






# # find lowest_value_row['care_days'] matches in c_coord

# c_coord['Inst'] == lowest_value_row['hospital']







# # Search closest hospital(s) to the lowest value row and add them to the list of selected hospitals (h_loc_selected) 



# # DO THIS TO CALCULATE DISTANCE BETWEEN POINTS

# Create a new column 'hospital' in the municipalities DataFrame
# municipalities['hospital'] = ''

# Iterate over each municipality
# for index, row in municipalities.dropna(subset=['coords']).iterrows():
#     # Extract the coordinates of the municipality
#     mun_lat, mun_lon = row['coords']

# Initialize the minimum distance and the closest hospital
#     min_distance = float('inf')
#     closest_hospital = ''

# Iterate over each hospital
#     for index_h, row_h in hospitals.iterrows():
#         # Extract the coordinates of the hospital
#         hosp_lat, hosp_lon = row_h['latitude'], row_h['longitude']

# Calculate the distance between the municipality and the hospital
#         try:
#             distance = geodesic((mun_lat, mun_lon), (hosp_lat, hosp_lon)).km
#         except ValueError:
#             distance = float('inf')

# Update the minimum distance and the closest hospital if necessary
#         if distance < min_distance:
#             min_distance = distance
#             closest_hospital = row_h['Inst']

# Update the 'hospital' column in the municipalities DataFrame
#     municipalities.at[index, 'hospital'] = closest_hospital

# municipalities.head()






# import streamlit as st
# import pandas as pd
# import numpy as np 
# import plotly.graph_objects as go
# import plotly.express as px
# import os
# import json

# pop_df = pd.read_csv('../data/processed/district_pop.csv')
# # district geodata

# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as f:
#   geodata = json.load(f)


# # with open('fcRailroad.geojson') as json_file:
# #     fcRailroad = json.load(json_file)



# gdf = gpd.GeoDataFrame.from_features(geojson)



# fig = px.choropleth_mapbox(
#     pop_df,
#     geojson=geodata,
#     color='pop23',
#     locations='name',
#     featureidkey="properties.NAME",
#     color_continuous_scale=px.colors.sequential.algae,
#     )

# fig.update_layout(mapbox_style="carto-positron",
#                   mapbox_zoom=6, mapbox_center = {"lon": 8.2328637, "lat": 46.7995666})
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# st.plotly_chart(fig)




# @st.cache_data
# def load_json(path:str) -> object:
#     with open(path) as f:
#         geodata = json.load(f)
#     return geodata

# geodata_raw = load_json('./data/raw/georef-switzerland-kanton.geojson')
# geodata = deepcopy(geodata_raw)


# # Load the dataset
# df_path = os.path.abspath("../data/processed/address_coordinates.csv")
# df = pd.read_csv(df_path)

# # Load the GeoJSON data
# geojson_path = os.path.abspath("../data/raw/ch-districts.geojson")
# with open(geojson_path) as f:
#     geojson_data = json.load(f)

# pop_path = os.path.abspath("../data/processed/district_pop.csv")
# df = pd.read_csv(pop_path)


# population = powerplants.groupby(by=['canton', 'energy_source_level_2'], as_index=False) \
#     .agg({'electrical_capacity':'sum'}) \
#     .pivot(index='canton', columns='energy_source_level_2', values='electrical_capacity') \
#     .fillna(0) 


# healcare cost is on rise.. we visualize how well used facilities in CH are, by giving an overview
# and simulating  current or smaller number of hospitals to see how the demamd will distribute.


