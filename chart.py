import pandas as pd
import plotly_express as pe

df = pd.read_csv('data.csv')
scatterPlot = pe.scatterPlot(df, x='date', y='cases', color='country')
scatterPlot.show()