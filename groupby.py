import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders.head(5))
pricey_shoes=orders.groupby('shoe_type').price.max()
print(pricey_shoes)
print(type(pricey_shoes))
