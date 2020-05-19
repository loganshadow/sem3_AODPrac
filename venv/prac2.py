import pandas as pd
import matplotlib.pyplot as plt
import datetime
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
from pandas_datareader import data
matplotlib.use('TkAgg')

df = pd.read_csv('usd_rubles.csv')
x = [datetime.datetime.strptime(elem, '%d.%m.%Y') for elem in df['date']]
#df['date'] = pd.to_datetime(df['date'])
#df.set_index('date', inplace=True)

data_rolling_10 = df.rolling(window=10).mean()
data_rolling_100 = df.rolling(window=100).mean()

fig, ax = plt.subplots(figsize=(16,9))
ax.plot(x, df['value'], label='USD')
ax.plot(x, data_rolling_10, label='10')
ax.plot(x, data_rolling_100, label='100')
plt.legend()
plt.show()