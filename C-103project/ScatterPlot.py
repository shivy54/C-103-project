import pandas as pd
import plotly.express as pe

data = pd.read_csv("data.csv")
plot = pe.scatter(data,x = "date",y = "cases",color="country")
plot.show()