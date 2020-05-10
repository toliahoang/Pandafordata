import codecademylib
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
shoe_counts=orders.groupby(['shoe_type','shoe_color']).id.count().reset_index()
print(shoe_counts)
