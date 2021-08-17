import pandas as pd
import os

files = [x for x in os.listdir('.')]
files = [x for x in files if x.endswith('.csv')]

for file in files:
	if file.endswith('.csv'):
		print file
		data = pd.read_csv(file)
        print data.columns
        data.columns = data.columns.str.replace(' ', '_')
        print data.columns
        data.to_csv(file)
