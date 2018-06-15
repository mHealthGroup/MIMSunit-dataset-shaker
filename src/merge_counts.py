import os
from glob import glob
from padar import api as padar
import pandas as pd
import re

sessions = pd.read_csv('../data/DerivedCrossParticipants/sessions.csv', parse_dates=[0,1], infer_datetime_format=True)

csv_files = glob('../data/*/Derived/*.feature.csv')
print(csv_files)
merged_dfs = []
for csv in csv_files:
	print("Process " + csv)
	d = pd.read_csv(csv, parse_dates=[0], infer_datetime_format=True)
	count_type = os.path.basename(csv).split('.')[0].split('-')[1]
	
	pattern = re.compile('([A-Za-z0-9]+[A-Za-z]+)([0-9]+)G([0-9]+)Hz')
	matcher = pattern.match(os.path.basename(csv))
	gr = matcher.group(2)
	sr = matcher.group(3)
	device = matcher.group(1)
	readable_device_name = device + ": " + str(sr) + "Hz, " + str(gr) + "g"
	clips = []
	for index, row in sessions.iterrows():
		st = row['START_TIME'].to_datetime64()
		et = row['STOP_TIME'].to_datetime64()
		freq = row['HZ']
		print("Extract freq: " + str(freq))
		clipped = d.loc[(d.iloc[:,0] >= st) & (d.iloc[:, 0] < et),:]
		# clipped = padar.clip_dataframe(d, st, et)
		clipped.columns = ['HEADER_TIME_STAMP', 'VALUE']
		clipped.loc[:,'HZ'] = freq
		clips.append(clipped)
	cleaned_d = pd.concat(clips)
	
	cleaned_d.loc[:, 'DEVICE'] = device
	cleaned_d.loc[:, 'SR'] = sr
	cleaned_d.loc[:, 'GRANGE'] = gr
	cleaned_d.loc[:, 'NAME'] = readable_device_name
	cleaned_d.loc[:, 'TYPE'] = count_type
	merged_dfs.append(cleaned_d)

merged_df = pd.concat(merged_dfs)
merged_df.to_csv('../data/DerivedCrossParticipants/counts.feature.csv', index=False, float_format='%.9f')
		
	