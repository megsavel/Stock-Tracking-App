from pandas_datareader import data
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd


from bokeh.io import output_notebook

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
import numpy as np

# function for pulling all the info about a particular stock
def getstockdata(ticker):
    start = dt.datetime(2017,3,26)
    end = dt.datetime(2019,3,25)
    return (web.DataReader(ticker, "iex", start, end).reset_index())


# Metric and company info

def getstockplot(co,metric):
    stockinfo = getstockdata(co)
    return getplot(stockinfo, metric, co)


# function to plot the stock info
def getplot(stockinfo, metric, co):
    # formatting the title correctly
    def title():
        if metric == 'open':
            return f"Stock {metric.title()}ing Price"
        elif metric == 'close':
            return "Stock Closing Price"
        elif metric == 'volume':
            return "Number of Shares"
        else:
            return f"{metric.title()}est Daily Price"

    p = figure(x_axis_type="datetime", title=title())
    p.grid.grid_line_alpha = 0.3
    p.xaxis.axis_label = 'Date'

    # Formatting Axis Labels
    label = 'Price'
    if metric == 'volume':
        label = 'Number of Shares'
    p.yaxis.axis_label = label

    stockinfo.date = pd.to_datetime(stockinfo.date)

    p.line(stockinfo['date'], stockinfo[metric], color='#1f77b4', legend=co)

    return p
