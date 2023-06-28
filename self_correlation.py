# Warningsの消去
import warnings
warnings.filterwarnings('ignore')

# モジュールの読み込み
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'

# データの読み込み
fname = './data/2020413.csv'
df = pd.read_csv(fname, index_col=0, parse_dates=True, na_values='None', encoding='shift-jis')

# 例として1つ抜き出してみる
col_name = "気化器温度_PV"

acf = sm.tsa.stattools.acf(df[col_name])
print(acf)

# fig = plt.figure(figsize=(8, 5))
# ax1 = fig.add_subplot(111)
# sm.graphics.tsa.plot_acf(df.loc[::60, col_name], lags=40, ax=ax1) #グラフを自動作成
# ax1.set_xlabel('ラグ数')
# ax1.set_ylabel('自己相関')
# plt.show()
# plt.close('all')

# fig = plt.figure(figsize=(8, 5))
# ax = fig.add_subplot(111)
# ax.plot(df.index, df[col_name], label='ラグなし')
# ax.plot(df.index-timedelta(minutes=32), df[col_name], label='ラグあり')
# ax.legend()
# ax.set_xlim(datetime(2020, 4, 13, 0), datetime(2020, 4, 13, 1))
# plt.show()

col_name = '蒸留塔第5トレイ温度_PV'
fig = plt.figure(figsize=(8, 10))
fig.tight_layout()
ax1 = fig.add_subplot(211)
ax1.plot(df.index[::60], df.loc[::60, col_name])
ax1.set_title(col_name)
ax2 = fig.add_subplot(212)
sm.graphics.tsa.plot_acf(df.loc[::60, col_name], lags=60, ax=ax2)

plt.show()