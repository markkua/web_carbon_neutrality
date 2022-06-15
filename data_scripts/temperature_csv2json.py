# encoding: utf-8
# Author: Bingxin Ke
# Created: 2022/6/15


import pandas as pd
import json
import numpy as np

input_path = "../pre_processed_data/temperature-anomaly_analysis.csv"

output_path = "../pre_processed_data/temperature_anomaly_1850-2019.json"

keys = ['Median', 'Upper', 'Lower']
colors = {
    'Median': '#ec407a',
    'Upper': '#b0bec5',
    'Lower': '#b0bec5'
}

# %%
input_df = pd.read_csv(input_path)
input_df = input_df.sort_values('Year')

out_json = {}

out_json['year'] = input_df['Year'].to_list()
out_json['temperature'] = {}

for key in keys:
    temp_dic = {}
    _data = np.round(input_df[key].to_list(), 2)
    temp_dic['data'] = list(_data)
    temp_dic['color'] = colors[key]
    out_json['temperature'].update({key: temp_dic})


# %%
with open(output_path, 'w+') as f:
    json.dump(out_json, f)


