from bokeh.models import ColumnDataSource, Panel


def explanation_tab():
    carrier_table = "test test blalbbalbla"

    tab = Panel(child=carrier_table, title='Welcome!')

    return tab
