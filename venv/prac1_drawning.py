import pandas as pd
import matplotlib.pyplot as plt
import datetime
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
from pandas_datareader import data
matplotlib.use('TkAgg')

data = pd.read_csv('usd_rubles.csv')
#x = [datetime.datetime.strptime(elem, '%d.%m.%Y') for elem in data['date']]

root = tk.Tk()

def days():
    window = tk.Tk()
    df = data
    x = [datetime.datetime.strptime(elem, '%d.%m.%Y') for elem in df['date']]
    fig = Figure(figsize=(5, 5), dpi=100)
    a = fig.add_subplot(111)
    a.plot(x, df['value'])
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.mainloop()

def weeks():
    window = tk.Tk()
    df = data
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date')
    week = df.rolling(window=7).mean()
    fig = Figure(figsize=(5, 5), dpi=100)
    a = fig.add_subplot(111)
    a.plot(week.index, week)
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.mainloop()

def months():
    window = tk.Tk()
    df = data
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date')
    week = df.rolling(window=30).mean()
    fig = Figure(figsize=(5, 5), dpi=100)
    a = fig.add_subplot(111)
    a.plot(week.index, week)
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.mainloop()

def years():
    window = tk.Tk()
    df = data
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date')
    week = df.rolling(window=356).mean()
    fig = Figure(figsize=(5, 5), dpi=100)
    a = fig.add_subplot(111)
    a.plot(week.index, week)
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.mainloop()

tk.Button(root, text="days", command=days).pack()
tk.Button(root, text="weeks", command=weeks).pack()
tk.Button(root, text="months", command=months).pack()
tk.Button(root, text="years", command=years).pack()

root.mainloop()