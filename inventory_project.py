import codecademylib
import pandas as pd

inventory=pd.read_csv('inventory.csv')
staten_island=inventory.head(10)
product_request=staten_island.product_description
seed_request=inventory[((inventory.location=='Brooklyn') & (inventory.product_type=='seeds'))]
#print(seed_request)

inventory['in_stock']=inventory.quantity.apply(lambda x: 'True' if x>0 else 'False')
inventory['total_value']=inventory.apply(lambda row: row.price*row.quantity,axis=1)
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description']=inventory.apply(combine_lambda,axis=1)                     
print(inventory.head(10))



