import json
from typing import List
import math
import pandas as pd

"""
    Convert source statistic data (.csv) to geojson 
        Corrected boundary of China in @china_geojson_filename
"""
# %%

selected_years = [2000 + i for i in range(21)]  # years to be exported

to_remove_ls = ['Aksai Chin', 'Hong Kong', 'Macao', 'Taiwan', 'Arunachal Pradesh']

world_geojson_filename = "../pre_processed_data/boundary/world-administrative-boundaries_China_uncorrected.geojson"
china_geojson_filename = "../pre_processed_data/boundary/China_3.geojson"
# area_csv_filename = "../data/source/CountryArea/API_AG.LND.TOTL.K2_DS2_en_csv_v2_2254009.csv"
output_geojson_filename = "../pre_processed_data/ghg/co2_ghg_country_2000-2020.csv"

# source data definition
source_data_filename = "../pre_processed_data/ghg/owid-co2-data_filtered.csv"
field_correspondence = {
    'co2(million_ton)': 'co2_total',
    'co2_per_capita(ton)': 'co2_per_capita',
    'total_ghg': 'ghg_total',
    'ghg_per_capita': 'ghg_per_capita'
}
CO2_FIELD_NAME = 'co2(million_ton)'
CO2_PER_CAP_FIELD_NAME = 'co2_per_capita(ton)'
GHG_FIELD_NAME = 'total_ghg'
GHG_PER_CAP_FIELD_NAME = 'ghg_per_capita'
YEAR_FIELD_NAME = 'year'
ISO_FILED_NAME = 'iso_code'

with open(world_geojson_filename, 'r') as f:
    world_boundary_json: dict = json.load(f)

with open(china_geojson_filename, 'r') as f:
    china_boundary_json: dict = json.load(f)

emission_df = pd.read_csv(source_data_filename, header=0)

# country_area_df = pd.read_csv(area_csv_filename, header=2)

# %%
iso_ls = []
matched_iso_dict: dict = {key: [] for key in selected_years}
matched_iso_ls: List = []

i: int
feature: dict

# %% # Remove ['Aksai Chin', 'Hong Kong', 'Macao', 'Taiwan', 'Arunachal Pradesh']
temp_ls = []
for i, feature in enumerate(world_boundary_json['features']):
    assert 'properties' in feature.keys()
    name = feature['properties']['name']
    if name in to_remove_ls:
        temp_ls.append(feature)

for feature in temp_ls:
    world_boundary_json['features'].remove(feature)

# %% Add properties
for i, feature in enumerate(world_boundary_json['features']):
    assert 'properties' in feature.keys()

    area_ha = None
    iso: str = ""
    if 'iso3' in feature['properties'].keys():
        iso = feature['properties']['iso3']
        iso_ls.append(iso)
        # country area
        # area_ls = country_area_df[country_area_df['Country Code'] == iso]['2018'].values # sq.km
        # area_ha = area_ls[0] * 1e2 if len(area_ls) > 0 else None   # sq.km -> ha
    # else:  # con not skip, need to add field
    #     continue

    # change geometry of China
    if "CHN" == iso:
        feature['geometry'] = china_boundary_json['features'][0]['geometry']
        feature['properties'] = china_boundary_json['features'][0]['properties']
        # area = 9.6e6  # sq.km
        # area_ha = area * 1e2  # sq.km -> ha

    country_df = emission_df[emission_df[ISO_FILED_NAME] == iso].sort_values(YEAR_FIELD_NAME)

    for year in selected_years:
        # assign data
        if iso in emission_df[ISO_FILED_NAME].unique() and year in country_df[YEAR_FIELD_NAME].to_list():
            for from_field, to_field in field_correspondence.items():
                value = country_df[(country_df[YEAR_FIELD_NAME] == year)][from_field].values[0]
                feature['properties'][f'{to_field}_{year}'] = value if not math.isnan(value) else None
            matched_iso_dict[year].append(iso)
        else:
            for from_field, to_field in field_correspondence.items():
                feature['properties'][f'{to_field}_{year}'] = None

# %% Check field exist
for i, feature in enumerate(world_boundary_json['features']):
    name = feature['properties']['name']
    assert name not in to_remove_ls
    for year in selected_years:
        for from_field, to_field in field_correspondence.items():
            field_name = f"{to_field}_{year}"
            assert field_name in feature['properties'].keys(), f"Can't find {field_name} in {name}"

# %%
with open(output_geojson_filename, 'w+') as f:
    json.dump(world_boundary_json, f)

print(f"added {len(matched_iso_dict[2020])} out of {len(emission_df[ISO_FILED_NAME].unique())} data")

# %%


# %%
# adm_df = pd.read_csv(adm_filename, header=0)
# emission_df = pd.read_csv(source_data_filename, header=0)
#
# emission_df['adm'] = emission_df['adm1']
# emission_df['adm'] = emission_df['adm'].apply(lambda x: list(adm_df[adm_df['adm1__id'] == x]['name'])[0])
#
# name_ls = []
# data_count = 0
# for i, feature in enumerate(boundary_json['features']):
#     name = feature['properties']['name']
#     name_ls.append(name)
#     country_df = emission_df[emission_df['adm'] == name].sort_values(YEAR_FIELD_NAME)[TREE_LOSS_TAG]
#     country_df = country_df.to_list()
#
#     assert 20 == len(country_df) or 0 == len(country_df)
#     if 20 == len(country_df):
#         data_count += 1
#
#     selected_years = [2005, 2010, 2015, 2020]
#     for year in selected_years:
#         index = year - 2001
#         if index < len(country_df):
#             co2 = country_df[index]
#         else:
#             co2 = None
#         field_name = f"tree_loss_{year}"
#         feature['properties'][field_name] = co2
#     # feature['properties']['tree_loss'] = country_df
#     print(i, name, country_df)
#
# with open(output_filename, 'w+') as f:
#     json.dump(boundary_json, f)
#
# print(f"added {data_count} out of {len(emission_df['adm'].unique())} data")
