import pandas as pd
import numpy as np
import matplotlib.pylab as plt

df = pd.read_csv('listings_with_prices.csv')

from plotly.offline import plot
import plotly.graph_objs as go

print(df.columns)

# df = df.sort_values(by=['LABEL'])
# labels = df.LABEL.unique()
# values = [len(df[df.LABEL == label])  for label in labels]

# print(len(labels), len(values))

# data = [go.Bar(
#             x=labels,
#             y=values
#     )]

# plot(data, filename='basic-bar.html')

# Add returning costs to the investment

# df['yearly_returns'] = np.log(df.price * 365)
# df = df.sort_values(by=['yearly_returns'])

# values = df.yearly_returns
# df = df.loc[2000:12000]
# labels = np.arange(len(df))



# data = [go.Scatter(
#             x=labels,
#             y=values,
#             mode='markers'
#     )]

# plot(data, filename='basic-bar.html')

labels = df.room_type.unique()
values = [len(df[df.room_type == label])  for label in labels]

print(len(labels), len(values))

data = [go.Bar(
            x=labels,
            y=values
    )]

plot(data, filename='basic-bar.html')