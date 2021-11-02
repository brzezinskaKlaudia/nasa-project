import numpy as np
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import ColumnDataSource, Panel


def scatterPlot_tab(data_frame_nasa):
    # the data
    x = data_frame_nasa['duringTime']
    y = data_frame_nasa['month']

    # determine best fit line
    par = np.polyfit(x, y, 1, full=True)
    slope = par[0][0]
    intercept = par[0][1]
    y_predicted = [slope * i + intercept for i in x]
    # plot it
    fig = figure(x_axis_label='minutes', y_axis_label='month', x_range=(0, 120), y_range=(0, 12))
    fig.circle(x, y)
    #fig.Title("test")
    #x_range, x_scale, y_range or y_scale name,
    fig.line(x, y_predicted, color='red', legend='y=' + str(round(slope, 2)) + 'x+' + str(round(intercept, 2)))

    tab = Panel(child=fig, title='scatterPlot')
    return tab
