import streamlit as st
import pandas as pd
import numpy as np 
import plotly.graph_objects as go
import plotly.express as px
import os
import json

# # Load the dataset
# df_path = os.path.abspath("../data/processed/address_coordinates.csv")
# df = pd.read_csv(df_path)

# # Load the GeoJSON data
# geojson_path = os.path.abspath("../data/raw/ch-districts.geojson")
# with open(geojson_path) as f:
#     geojson_data = json.load(f)

# pop_path = os.path.abspath("../data/processed/district_pop.csv")
# df = pd.read_csv(pop_path)


pop_df = pd.read_csv('../data/processed/district_pop.csv')
# district geodata

with open('../data/raw/ch-districts.geojson') as f:
	geodata = json.load(f)



# population = powerplants.groupby(by=['canton', 'energy_source_level_2'], as_index=False) \
#     .agg({'electrical_capacity':'sum'}) \
#     .pivot(index='canton', columns='energy_source_level_2', values='electrical_capacity') \
#     .fillna(0) 

fig = px.choropleth_mapbox(
    pop_df,
    geojson=geodata,
    color='pop23',
    locations='pop23',
    featureidkey="properties.kan_name",
    color_continuous_scale=px.colors.sequential.algae,
    )

fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=6, mapbox_center = {"lon": 8.2328637, "lat": 46.7995666})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

@st.cache_data
def load_json(path:str) -> object:
    with open(path) as f:
        geodata = json.load(f)
    return geodata

geodata_raw = load_json('./data/raw/georef-switzerland-kanton.geojson')
geodata = deepcopy(geodata_raw)

