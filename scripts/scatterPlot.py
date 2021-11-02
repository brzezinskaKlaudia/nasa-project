import numpy as np
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import ColumnDataSource, Panel
from bokeh.transform import factor_cmap


def scatterPlot_tab(data_frame_nasa):
    # the data
    x = data_frame_nasa['duringTime']
    y = data_frame_nasa['month']
    index_cmap = factor_cmap('class_type_simple', palette=['red', 'blue', 'green', 'yellow'],
                             factors=sorted(data_frame_nasa['class_type_simple'].unique()))
    # determine best fit line
    p = figure(plot_width=1200, plot_height=900, title="During Time for every month", toolbar_location=None,
               tools="hover")
    p.scatter('duringTime', 'month', source=data_frame_nasa, fill_color=index_cmap, fill_alpha=0.6, size=10,
              legend='class_type_simple')
    p.xaxis.axis_label = 'Minutes'
    p.yaxis.axis_label = 'Month'
    p.legend.location = "top_left"

    tab = Panel(child=p, title='scatterPlot')
    return tab
