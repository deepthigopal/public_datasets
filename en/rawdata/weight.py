import pandas as pd
import os

for file in os.listdir('.'):
	if file.endswith('.csv'):
		print file
		data = pd.read_csv(file)


		[item for item in data.columns if item not in ['index']]

		data = data.fillna('no value')

		new = data.groupby([item for item in data.columns if item not in ['index']]).count().reset_index()
		new.rename(columns={'index':'count'}, inplace=True)
		new = new.groupby([item for item in new.columns if item not in ['userid']]).count().reset_index()
		new['weight'] = new['count']/new.userid
		new = new[[item for item in new.columns if item not in ['userid','count']]]
		new = new.groupby([item for item in new.columns if item not in ['weight']]).sum().reset_index()
		
		new.to_csv('../weighted/'+file)