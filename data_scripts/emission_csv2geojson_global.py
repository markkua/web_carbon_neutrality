import json
import pandas as pd
from typing import List

"""
    Corrected boundary of China in @china_geojson_filename
"""
# %%

TREE_LOSS_TAG = 'umd_tree_cover_loss__ha'
YEAR_TAG = 'umd_tree_cover_loss__year'
selected_years = [2001 + i for i in range(20)]  # [2005, 2010, 2015, 2020]
to_remove_ls = ['Aksai Chin', 'Hong Kong', 'Macao', 'Taiwan', 'Arunachal Pradesh']

world_geojson_filename = "../data/source/RegionBoundary/China/world-administrative-boundaries_China_uncorrected.geojson"
china_geojson_filename = "../data/source/RegionBoundary/China/China_3.geojson"
output_geojson_filename = "../data/output/tree_loss_World_4geojson"
area_csv_filename = "../data/source/CountryArea/API_AG.LND.TOTL.K2_DS2_en_csv_v2_2254009.csv"

tree_loss_filename = "../data/source/TreeLoss/Global Annual Tree cover loss/treecover_loss_by_region__ha.csv"

with open(world_geojson_filename, 'r') as f:
    world_boundary_json: dict = json.load(f)

with open(china_geojson_filename, 'r') as f:
    china_boundary_json: dict = json.load(f)

tree_loss_df = pd.read_csv(tree_loss_filename, header=0)

country_area_df = pd.read_csv(area_csv_filename, header=2)

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
        area_ls = country_area_df[country_area_df['Country Code'] == iso]['2018'].values # sq.km
        area_ha = area_ls[0] * 1e2 if len(area_ls) > 0 else None   # sq.km -> ha
    # else:  # con not skip, need to add field
    #     continue

    # change geometry of China
    if "CHN" == iso:
        feature['geometry'] = china_boundary_json['features'][0]['geometry']
        feature['properties'] = china_boundary_json['features'][0]['properties']
        area = 9.6e6  # sq.km
        area_ha = area * 1e2  # sq.km -> ha

    tree_loss_data = tree_loss_df[tree_loss_df['iso'] == iso].sort_values(YEAR_TAG)

    for year in selected_years:
        field_name = f"tree_loss_{year}"
        proportion_filed_name = f"tree_loss_proportion_{year}"
        if iso in tree_loss_df['iso'].unique() and year in tree_loss_data[YEAR_TAG].to_list():
            tree_loss_area = tree_loss_data[(tree_loss_data[YEAR_TAG] == year)][TREE_LOSS_TAG].values[0]
            tree_loss_proportion = tree_loss_area / area_ha if area_ha else None
            matched_iso_dict[year].append(iso)
        else:
            tree_loss_area = None
            tree_loss_proportion = None
        feature['properties'][field_name] = tree_loss_area
        feature['properties'][proportion_filed_name] = tree_loss_proportion

# %% Check field exist
for i, feature in enumerate(world_boundary_json['features']):
    name = feature['properties']['name']
    assert name not in to_remove_ls
    for year in selected_years:
        field_name = f"tree_loss_{year}"
        assert field_name in feature['properties'].keys()

# %%
with open(output_geojson_filename, 'w+') as f:
    json.dump(world_boundary_json, f)

print(f"added {len(matched_iso_dict[2020])} out of {len(tree_loss_df['iso'].unique())} data")

# %%


# %%
# adm_df = pd.read_csv(adm_filename, header=0)
# tree_loss_df = pd.read_csv(tree_loss_filename, header=0)
#
# tree_loss_df['adm'] = tree_loss_df['adm1']
# tree_loss_df['adm'] = tree_loss_df['adm'].apply(lambda x: list(adm_df[adm_df['adm1__id'] == x]['name'])[0])
#
# name_ls = []
# data_count = 0
# for i, feature in enumerate(boundary_json['features']):
#     name = feature['properties']['name']
#     name_ls.append(name)
#     tree_loss_data = tree_loss_df[tree_loss_df['adm'] == name].sort_values(YEAR_TAG)[TREE_LOSS_TAG]
#     tree_loss_data = tree_loss_data.to_list()
#
#     assert 20 == len(tree_loss_data) or 0 == len(tree_loss_data)
#     if 20 == len(tree_loss_data):
#         data_count += 1
#
#     selected_years = [2005, 2010, 2015, 2020]
#     for year in selected_years:
#         index = year - 2001
#         if index < len(tree_loss_data):
#             tree_loss_area = tree_loss_data[index]
#         else:
#             tree_loss_area = None
#         field_name = f"tree_loss_{year}"
#         feature['properties'][field_name] = tree_loss_area
#     # feature['properties']['tree_loss'] = tree_loss_data
#     print(i, name, tree_loss_data)
#
# with open(output_filename, 'w+') as f:
#     json.dump(boundary_json, f)
#
# print(f"added {data_count} out of {len(tree_loss_df['adm'].unique())} data")
