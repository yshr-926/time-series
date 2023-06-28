import warnings
warnings.filterwarnings('ignore')

import datetime
import numpy as np
import pandas as pd

FILE_PATH = './data/2020413_raw.csv'
df = pd.read_csv(FILE_PATH, index_col=0, parse_dates=True, encoding='cp932')
print(df.head())

print(df.describe())  # df.describe(include=['number']) と等価
print(df.describe(include=['object']))
try:
    df.describe(include=['datetime'])
except Exception as e:
    print(f'{type(e)}: {e}' )

print(df.index.to_series().describe())