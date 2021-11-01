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
    fig = figure()
    fig.circle(x, y)
    fig.line(x, y_predicted, color='red', legend='y=' + str(round(slope, 2)) + 'x+' + str(round(intercept, 2)))
    #show(fig)

    tab = Panel(child=fig, title='scatterPlot')
    return tab