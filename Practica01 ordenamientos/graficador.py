import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

df = pd.read_csv('salida.csv')

sample_data_table = FF.create_table(df.head())
py.iplot(sample_data_table, filename='tablaTiemposBubble')
trace1 = go.Scatter(
                    x=df['entradas'], y=df['tiempo'], # Data
                    mode='lines', name='tiempoEntradas' # Additional options
                   )
layout = go.Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1], layout=layout)

# Plot data in the notebook
py.iplot(fig, filename='simple-plot-from-csv')