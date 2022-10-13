import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders.head(10))

#grouping the shoes by shoe_type and checking price
pricey_shoes=orders.groupby('shoe_type').price.max()
print(pricey_shoes)
print(type(pricey_shoes))

#use of reset index
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()

print(pricey_shoes)
print(type(pricey_shoes))