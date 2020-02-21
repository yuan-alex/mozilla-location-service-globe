import pandas as pd
import json
from tqdm import tqdm

compiled = []
totals = {}

# changing the percision will affect processing speed and the spacing between data points on the globe
percision = 1

def round_base(x, base=percision):
	return int(base * round(x/base))

for a in range(-90, 91, percision):
	for b in range(-180, 181, percision):
		totals[(a, b)] = 0

# make sure you have the full data downloaded and in the same directory
# you'll probably have to change the csv name to the more current one you've downloaded
for df in pd.read_csv('MLS-full-cell-export-2020-02-08T000000.csv', chunksize=10**6, usecols=['lat', 'lon', 'samples']):
	lat = df['lat']
	lon = df['lon']
	for i in tqdm(range(0, len(lat), 1)):
		c_lat = lat.iloc[i]
		c_lon = lon.iloc[i]
		totals[(round_base(c_lat), round_base(c_lon))] += 0.000009
	
for key in tqdm(totals):
	if totals[key] != 0:
		compiled.append(key[0])
		compiled.append(key[1])
		compiled.append(totals[key])
		
with open('compiled.json', 'w') as file:
	json.dump(compiled, file)