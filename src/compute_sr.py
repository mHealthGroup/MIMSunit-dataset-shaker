import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], infer_datetime_format=True, parse_dates=[0])

new_df = df.groupby(pd.Grouper(key=df.columns[0], freq='60s')).count()

new_df.to_csv('./test.csv')