import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head(10))
print(cart.head(10))
print(checkout.head(10))
print(purchase.head(10))  

visit_cart=pd.merge(visits,cart,how='left')
#print(visit_cart.user_id.count())
print(visit_cart)
print(len(visit_cart))
number_null=visit_cart[visit_cart.cart_time.isnull()]
number_nan=number_null.user_id.count()
print(number_nan)
number_visit=visit_cart[visit_cart.visit_time.isnull()]
number_visit_1=number_visit.user_id.count()
print(number_visit_1)

cart_checkout=pd.merge(cart,checkout,how='left')
print('len cart_checkout',len(cart_checkout))
null_checkout=cart_checkout[cart_checkout.checkout_time.isnull()]
null_checkout_num=null_checkout.user_id.count()
print(null_checkout_num)
all_data=visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')
print(all_data.head())

print('length of alldata',len(all_data))
num_check_out_time=all_data[all_data.checkout_time.isnull()]
num_check_out_time_1=num_check_out_time.user_id.count()
print(num_check_out_time_1)

num_purchase_time=all_data[all_data.purchase_time.isnull()]
num_purchase_time_1=num_purchase_time.user_id.count()
print(num_purchase_time_1)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.time_to_purchase) 
print(all_data.time_to_purchase.mean()) 


