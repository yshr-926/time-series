import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import warnings
import itertools

# カテゴリ値の列や欠損値を含まないデータ
fname = './data/2020413.csv'
# カテゴリ値の列や欠損値を含むデータ
# fname = './data/2020413_raw.csv'
with warnings.catch_warnings(record=True) as w:  # データの読み込みでWarningが発生するので捕捉する
    df = pd.read_csv(fname, index_col=0, parse_dates=True, na_values=['None'], encoding='shift-jis')

def plot_figs(df):
    '''
    うけとったデータをすべてプロットする関数
    :param df: plotしたいpandas.Dataframe
    :return: 
    '''
    plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'
    color_iter = itertools.cycle(['#02A8F3', '#33B490', '#FF5151', '#B967C7'])
    n_figs = df.columns.size
    fig = plt.figure(figsize=(6, 2.0*n_figs), dpi=100)
    x = df.index
    for i in range(n_figs):
        y = df.iloc[:, i]
        title = df.columns[i]
        ax = fig.add_subplot(n_figs, 1, i+1)
        ax.plot(x, y, color=next(color_iter), linewidth=1.0)
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
        ax.set_xlim(x[0], x[-1])
        ax.set_title(title, fontsize=12)
    fig.tight_layout()
    plt.show()
    plt.close()

# 全部をプロットする余白がないので、ここでは一部をプロット
plot_list = ['気化器液面レベル_PV', '気化器液面レベル_SV', '気化器液面レベル_MV',
             'コンプレッサー出口温度_PV', 'コンプレッサー出口温度_SV', 'コンプレッサー出口温度_SV']
plot_figs(df.loc[:, plot_list])
