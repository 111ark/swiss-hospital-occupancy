import pandas as pd 

import json 

# Streamlit caching to load data efficiently
def load_geojson():
    with open('../data/raw/gemeinden_wus.geojson', 'r') as f:
        return json.load(f)

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



h_loc_sorted = h_loc.sort_values(by='bed_occupancy', ascending=True)
lowest_value_row = h_loc_sorted.iloc[0]  # Get the uppermost row (lowest value)
h_loc_sorted = h_loc_sorted.iloc[1:]







# lowest_value_row['Inst']


lowest_value_row['care_days']






# find lowest_value_row['care_days'] matches in d_coord

print(d_coord['Inst'] == lowest_value_row['Inst'])




# d_coord





# Search closest hospital(s) to the lowest value row and add them to the list of selected hospitals (h_loc_selected) 





