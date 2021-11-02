import pandas as pd
import numpy as np

from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import TableColumn, DataTable


def table_tab(data_frame_nasa):
    # Calculate summary stats for table
    class_type_stats = data_frame_nasa.groupby('class_type_simple')['duringTime'].describe()
    class_type_stats = class_type_stats.reset_index().rename(
        columns={'activeRegionNum': 'Number of active region', 'count': 'secondary_id', '50%': 'median'})

    # Round statistics for display
    class_type_stats['mean'] = class_type_stats['mean'].round(2)
    class_type_src = ColumnDataSource(class_type_stats)

    # Columns of table
    table_columns = [TableColumn(field='class_type_simple', title='class_type_simple'),
                     TableColumn(field='min', title='Min Delay'),
                     TableColumn(field='mean', title='Mean Delay'),
                     TableColumn(field='median', title='Median Delay'),
                     TableColumn(field='max', title='Max Delay')]

    class_type_table = DataTable(source=class_type_src,
                              columns=table_columns, width=1000)

    tab = Panel(child=class_type_table, title='Welcome')

    return tab
