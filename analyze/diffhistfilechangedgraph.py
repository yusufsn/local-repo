import pandas as pd
import plotly.graph_objs as go
import plotly
from plotly.offline import plot, init_notebook_mode, iplot

#%matplotlib inline

out = pd.read_csv('/Users/YusufNugroho/local-repo/analyze/diffhistfilechanged.csv')

trace1 = go.Bar(
    x=out['filename'],
    y=out['SUM #line_changed'],
    name='Sum of line changed'
)

dt = [trace1]
layout = go.Layout(
    barmode='group'
)

init_notebook_mode(connected=True)
fig = go.Figure(data=dt, layout=layout)
iplot(fig, show_link=False)