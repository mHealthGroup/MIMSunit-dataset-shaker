import os
from glob import glob
from padar import api as padar
import pandas as pd
from subprocess import call 

sessions = pd.read_csv('../data/DerivedCrossParticipants/sessions.csv', parse_dates=[0,1], infer_datetime_format=True)

csv_files = glob('../data/*/Derived/*.sensor.csv')
print(csv_files)
for csv in csv_files:
	d = pd.read_csv(csv, parse_dates=[0], infer_datetime_format=True)
	print(d.shape)
	clips = []
	for index, row in sessions.iterrows():
		st = row['START_TIME'].to_datetime64()
		et = row['STOP_TIME'].to_datetime64()
		hz = row['HZ']
		clipped = padar.clip_dataframe(d, st, et)
		clipped.loc[:,'HZ'] = hz
		clips.append(clipped)
	cleaned_d = pd.concat(clips)
	clip_file = csv.replace('sensor.csv', 'clip.csv')
	plot_file = csv.replace('sensor.csv', 'clip.png')
	cleaned_d.to_csv(clip_file, float_format='%.3f', index=False)
	call(['Rscript', 'plot_raw.R', clip_file, plot_file])
		
	