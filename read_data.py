import json
import pandas as pd

with open('data.json', 'r') as file:
    data = json.load(file)

flattened_data = []

for state_info in data:
    state = state_info['state']
    for district_info in state_info['districts']:
        district = district_info['district']
        for subdistrict_info in district_info['subDistricts']:
            subdistrict = subdistrict_info['subDistrict']
            villages = subdistrict_info['villages']
            for village in villages:
                flattened_entry = {
                    'State': state,
                    'District': district,
                    'SubDistrict': subdistrict,
                    'Village': village
                }
             
                flattened_data.append(flattened_entry)

df = pd.DataFrame(flattened_data)
