import pandas as pd
import matplotlib.pyplot as plt
import datetime
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

#from wwo_hist import retrieve_hist_data
#frequency = 12
#start_date = '01-JAN-2010'
#end_date = '01-JAN-2020'
#api_key = '7130cb06e80b4bbebb9171731201304'
#location_list = ['moscow']
#hist_weather_data = retrieve_hist_data(api_key, location_list, start_date, end_date, frequency, location_label=False,
#export_csv=True, store_df=True)

data = pd.read_csv('moscow.csv')
data['date_time'] = pd.to_datetime(data['date_time'])
data.set_index('date_time', inplace=True)
data['avgtempC'] = (data['maxtempC'] + data['mintempC'])/2

root = tk.Tk()

def days():
    window = tk.Tk()
    df = data
    fig = Figure(figsize=(5, 5), dpi=100)
    a = fig.add_subplot(111)
    a.plot(df.index, df['avgtempC'])
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.mainloop()

def weeks():
    window = tk.Tk()
    df = data
    week = df.rolling(window=14).mean()
    fig = Figure(figsize=(5, 5), dpi=100)
    a = fig.add_subplot(111)
    a.plot(week.index, week['avgtempC'])
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.mainloop()

def months():
    window = tk.Tk()
    df = data
    week = df.rolling(window=60).mean()
    fig = Figure(figsize=(5, 5), dpi=100)
    a = fig.add_subplot(111)
    a.plot(week.index, week['avgtempC'])
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.mainloop()

def years():
    window = tk.Tk()
    df = data
    week = df.rolling(window=712).mean()
    fig = Figure(figsize=(5, 5), dpi=100)
    a = fig.add_subplot(111)
    a.plot(week.index, week['avgtempC'])
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.mainloop()

tk.Button(root, text="days", command=days).pack()
tk.Button(root, text="weeks", command=weeks).pack()
tk.Button(root, text="months", command=months).pack()
tk.Button(root, text="years", command=years).pack()

root.mainloop()