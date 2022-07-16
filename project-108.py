import pandas as pd
import plotly.figure_factory as ff
file = pd.read_csv("data12.csv")
fig = ff.create_distplot([file["Avg Rating"].tolist()],["average rating"])
fig.show()