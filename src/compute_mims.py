
from glob import glob
import os
import re
from subprocess import call
import pandas as pd

csv_files = glob('../data/*/Derived/*.sensor.csv')
for csv in csv_files:
	pattern = re.compile('[A-Za-z0-9]+[A-Za-z]+([0-9]+)G([0-9]+)Hz')
	matcher = pattern.match(os.path.basename(csv))
	gr = matcher.group(1)
	print(gr)
	mims_output_file = csv.replace('.sensor.csv', '-mims.feature.csv')
	mims_narrow_output_file = csv.replace('.sensor.csv', '-mims_narrowband.feature.csv')
	mims_narrow_no_extrap_output_file = csv.replace('.sensor.csv', '-mims_narrowband_noextrap.feature.csv')
	mims_no_extrap_output_file = csv.replace('.sensor.csv', '-mims_noextrap.feature.csv')
	call(['Rscript', './mims-unit.R', csv, 'NULL', 'NULL', mims_output_file, gr, 'NULL', 'NULL', 'True'])
	call(['Rscript', './mims-unit.R', csv, 'NULL', 'NULL', mims_narrow_output_file, gr, '0.25', '2.5', 'True'])
	call(['Rscript', './mims-unit.R', csv, 'NULL', 'NULL', mims_narrow_no_extrap_output_file, gr, '0.25', '2.5', 'False'])
	call(['Rscript', './mims-unit.R', csv, 'NULL', 'NULL', mims_no_extrap_output_file, gr, 'NULL', 'NULL', 'False'])