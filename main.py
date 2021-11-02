# Pandas for data management
import pandas as pd
import requests
import numpy as np
# os methods for manipulating paths
from os.path import dirname, join

# Bokeh basics 
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

# Each tab is drawn by one script
#from scripts.explanation import explanation_tab
from scripts.histogramForDuringTime import histogram_for_during_time_tab
from scripts.histogramForTimeHighPoint import histogram_for_time_high_point_tab
from scripts.table import table_tab
from scripts.boxplot import boxplot_tab
from scripts.scatterPlot import scatterPlot_tab


# Read data into dataframes
response = requests.get(
    "https://api.nasa.gov/DONKI/FLR?startDate=2020-10-01&endDate=2021-10-01&api_key=zSbjNFJgVZ45n9AZcGLzR9GiNx2C8Ttd50oOf0hA")
json_data = response.json()

df = pd.json_normalize(json_data)
df['duringTime'] = (pd.to_datetime(df.endTime) - pd.to_datetime(df.beginTime)) / np.timedelta64(1, 'm')
df['duringTimeHighPoint'] = (pd.to_datetime(df.peakTime) - pd.to_datetime(df.beginTime)) / np.timedelta64(1, 'm')


data_nasa = [df["flrID"], df["duringTime"], df["duringTimeHighPoint"], df["classType"], df["sourceLocation"],
             df["activeRegionNum"]]  # create data

data_frame_nasa = pd.concat(data_nasa, axis=1)  # create data frame from data
data_frame_nasa = data_frame_nasa.dropna()
data_frame_nasa = data_frame_nasa.drop(data_frame_nasa[data_frame_nasa.duringTimeHighPoint < 0].index)
data_frame_nasa = data_frame_nasa.drop(data_frame_nasa[data_frame_nasa.duringTime < 0].index)
data_frame_nasa['class_type_simple'] = data_frame_nasa['classType'].str.slice(stop=1)
data_frame_nasa['month'] = pd.to_numeric(data_frame_nasa['flrID'].str.slice(start=5, stop=7))
data_frame_nasa.insert(0, 'secondary_id', range(0, 0 + len(data_frame_nasa)))


# Create each of the tabs
#tab0 = explanation_tab()
tab1 = table_tab(data_frame_nasa)
tab2 = histogram_for_during_time_tab(data_frame_nasa)
tab3 = histogram_for_time_high_point_tab(data_frame_nasa)
tab4 = boxplot_tab(data_frame_nasa)
tab5 = scatterPlot_tab(data_frame_nasa)

#title = Div(text='<h1 style="text-align: center">Example Header</h1>')
# Put all the tabs into one application
tabs = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5])
#layout = column(title, tabs, sizing_mode='scale_width')
# Put the tabs in the current document for display
curdoc().add_root(tabs)
