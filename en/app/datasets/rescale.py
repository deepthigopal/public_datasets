import pandas as pd
import os

files = [x for x in os.listdir('.')]
files = [x for x in files if x.endswith('.csv')]

for file in files:
	if file.endswith('.csv'):
		print file
		data = pd.read_csv(file)
		data = data.fillna('no value')
        cols = [item for item in data.columns if item not in ['index','placename','longitude','latitude']]
        for item in cols:
            if min(data[item]) < 0.01:
                data[item] = (data[item] - min(data[item]))/(max(data[item])-min(data[item]))
                data.loc[data[item]<0.01,item] = 0.01
        data.to_csv(file)
