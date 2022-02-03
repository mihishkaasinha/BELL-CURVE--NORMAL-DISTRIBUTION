import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv("data1.csv")
list = data["Avg Rating"].tolist()

show = ff.create_distplot([list], ["Avg Rating"], show_hist = False)
show.show()