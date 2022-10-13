import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders.head(10))

#printing most expensive shoes
most_expensive = orders.price.max()
print(most_expensive)

#printing no.of colors only
num_colors=orders.shoe_color.nunique()
print(num_colors)