import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head(5))
num_view=ad_clicks.groupby(['utm_source']).user_id.count().reset_index()
print(num_view)

ad_clicks['is_click']=~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head(5))
clicks_by_source=ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)
clicks_pivot=clicks_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id'

)
print(clicks_pivot)
clicks_pivot['percent_clicked']=clicks_pivot.apply((lambda row: 100.0*row[True]/(row[False]+row[True])),axis=1)
print(clicks_pivot)
num_add=ad_clicks.groupby(['experimental_group']).user_id.count()
#print(num_add)
percent_click=ad_clicks.groupby(['experimental_group','is_click']).user_id.count()
print(percent_click)
a_click=ad_clicks[ad_clicks.experimental_group=='A']
#print(a_click)
b_click=ad_clicks[ad_clicks.experimental_group=='B']
#print(b_click)

percent_a_click_byday=a_click.groupby(['day','is_click']).user_id.count()
print(percent_a_click_byday)

percent_b_click_byday=b_click.groupby(['day','is_click']).user_id.count()
print(percent_b_click_byday)

