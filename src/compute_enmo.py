
from glob import glob
import os
import re
from subprocess import call
import pandas as pd
import sys

enmo_script = sys.argv[1]

csv_files = glob('../data/*/Derived/*.sensor.csv')
for csv in csv_files:
	print(csv)
	pattern = re.compile('[A-Za-z0-9]+[A-Za-z]+([0-9]+)G([0-9]+)Hz')
	matcher = pattern.match(os.path.basename(csv))
	gr = matcher.group(1)
	sr = matcher.group(2)
	para_file = csv.replace('.csv', 'Calibration.csv')
	print(gr)
	print(sr)
	print(os.path.exists(para_file))

	call(['python', enmo_script, '-range', str(gr), '-sr', str(sr), '-skipCalibration', str(True), '-calibrationParaFile', para_file, csv])

	# convert to mhealth feature file
	print("convert to mhealth feature file")
	enmo_input_file = csv.replace('.csv', 'Epoch.csv')
	enmo_output_file = csv.replace('.sensor.csv', '-enmo.feature.csv')
	enmo_df = pd.read_csv(enmo_input_file)
	enmo_df = enmo_df.iloc[:,[0, 1]]
	enmo_df.columns = ['HEADER_TIME_STAMP', 'ENMO']
	enmo_df.to_csv(enmo_output_file, float_format='%.3f', index=False)
	