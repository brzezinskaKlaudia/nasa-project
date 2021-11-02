import pandas as pd
import numpy as np

from bokeh.plotting import figure
from bokeh.models import (CategoricalColorMapper, HoverTool,
                          ColumnDataSource, Panel, Column,
                          FuncTickFormatter, SingleIntervalTicker, LinearAxis)
from bokeh.models.widgets import (CheckboxGroup, Slider, RangeSlider,
                                  Tabs, CheckboxButtonGroup,
                                  TableColumn, DataTable, Select)
from bokeh.layouts import column, row
from bokeh.palettes import Category20_16


# Make plot with histogram and return tab
def histogram_for_time_high_point_tab(data_frame_nasa):
    # Function to make a dataset for histogram based on a list of carriers
    # a minimum delay, maximum delay, and histogram bin width
    def make_dataset(carrier_list, range_start=10, range_end=120, bin_width=5):
        # Dataframe to hold information
        by_class_type = pd.DataFrame(columns=['proportion', 'left', 'right',
                                           'f_proportion', 'f_interval',
                                           'class_type_simple', 'color'])

        range_extent = range_end - range_start

        # Iterate through all the carriers
        for i, carrier_name in enumerate(carrier_list):
            # Subset to the carrier
            subset = data_frame_nasa[data_frame_nasa['class_type_simple'] == carrier_name]

            # Create a histogram with 5 minute bins
            arr_hist, edges = np.histogram(subset['duringTimeHighPoint'],
                                           bins=int(range_extent / bin_width),
                                           range=[range_start, range_end])

            # Divide the counts by the total to get a proportion
            arr_df = pd.DataFrame({'proportion': arr_hist / np.sum(arr_hist), 'left': edges[:-1], 'right': edges[1:]})

            # Format the proportion
            arr_df['f_proportion'] = ['%0.5f' % proportion for proportion in arr_df['proportion']]

            # Format the interval
            arr_df['f_interval'] = ['%d to %d minutes' % (left, right) for left, right in
                                    zip(arr_df['left'], arr_df['right'])]

            # Assign the carrier for labels
            arr_df['class_type_simple'] = carrier_name

            # Color each carrier differently
            arr_df['color'] = Category20_16[i]

            # Add to the overall dataframe
            by_class_type = by_class_type.append(arr_df)
        # Overall dataframe
        by_class_type = by_class_type.sort_values(['class_type_simple', 'left'])

        return ColumnDataSource(by_class_type)

    def style(p):
        # Title
        p.title.align = 'center'
        p.title.text_font_size = '20pt'
        p.title.text_font = 'serif'

        # Axis titles
        p.xaxis.axis_label_text_font_size = '14pt'
        p.xaxis.axis_label_text_font_style = 'bold'
        p.yaxis.axis_label_text_font_size = '14pt'
        p.yaxis.axis_label_text_font_style = 'bold'

        # Tick labels
        p.xaxis.major_label_text_font_size = '12pt'
        p.yaxis.major_label_text_font_size = '12pt'

        return p

    def make_plot(src):
        # Blank plot with correct labels
        p = figure(plot_width=700, plot_height=700,
                   title='Histogram of during time to the high point by class',
                   x_axis_label='During Time', y_axis_label='Proportion')

        # Quad glyphs to create a histogram
        p.quad(source=src, bottom=0, top='proportion', left='left', right='right',
               color='color', fill_alpha=0.7, hover_fill_color='color', legend='class_type_simple',
               hover_fill_alpha=1.0, line_color='black')

        # Hover tool with vline mode
        hover = HoverTool(tooltips=[('Carrier', '@class_type_simple'),
                                    ('Delay', '@f_interval'),
                                    ('Proportion', '@f_proportion')],
                          mode='vline')

        p.add_tools(hover)
        # Styling
        p = style(p)

        return p

    def update(attr, old, new):
        class_type_to_plot = [class_type_selection.labels[i] for i in class_type_selection.active]

        new_src = make_dataset(class_type_to_plot,
                               range_start=range_select.value[0],
                               range_end=range_select.value[1],
                               bin_width=binwidth_select.value)

        src.data.update(new_src.data)

    # Carriers and colors
    available_class_type = list(set(data_frame_nasa['class_type_simple']))
    available_class_type.sort()

    airline_colors = list(Category20_16)
    airline_colors.sort()

    class_type_selection = CheckboxGroup(labels=available_class_type,
                                      active=[0, 1])
    class_type_selection.on_change('active', update)

    binwidth_select = Slider(start=1, end=30,
                             step=1, value=5,
                             title='Bin Width (min)')
    binwidth_select.on_change('value', update)

    range_select = RangeSlider(start=10, end=180, value=(10, 120),
                               step=5, title='Range of Delays (min)')
    range_select.on_change('value', update)

    # Initial carriers and data source
    initial_class_type = [class_type_selection.labels[i] for i in class_type_selection.active]

    src = make_dataset(initial_class_type,
                       range_start=range_select.value[0],
                       range_end=range_select.value[1],
                       bin_width=binwidth_select.value)
    p = make_plot(src)

    # Put controls in a single element
    controls = Column(class_type_selection, binwidth_select, range_select)

    # Create a row layout
    layout = row(controls, p)

    # Make a tab with the layout
    tab = Panel(child=layout, title='Histogram 2')

    return tab