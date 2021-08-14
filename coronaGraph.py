import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.line(df,x="country",y = "cases",color = "date",title = "Cases")

fig.show()