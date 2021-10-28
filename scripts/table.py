import pandas as pd
import numpy as np

from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import TableColumn, DataTable


def table_tab(data_frame_nasa):
    # Calculate summary stats for table
    carrier_stats = data_frame_nasa.groupby('class_type_simple')['duringTime'].describe()
    carrier_stats = carrier_stats.reset_index().rename(
        columns={'activeRegionNum': 'Number of active region', 'count': 'secondary_id', '50%': 'median'})

    # Round statistics for display
    carrier_stats['mean'] = carrier_stats['mean'].round(2)
    carrier_src = ColumnDataSource(carrier_stats)

    # Columns of table
    table_columns = [TableColumn(field='class_type_simple', title='class_type_simple'),
                     #TableColumn(field='activeRegionNum', title='activeRegionNum'),
                     TableColumn(field='min', title='Min Delay'),
                     TableColumn(field='mean', title='Mean Delay'),
                     TableColumn(field='median', title='Median Delay'),
                     TableColumn(field='max', title='Max Delay')]

    carrier_table = DataTable(source=carrier_src,
                              columns=table_columns, width=1000)

    tab = Panel(child=carrier_table, title='Summary Table')

    return tab
