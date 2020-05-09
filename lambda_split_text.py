import codecademylib
import pandas as pd

df = pd.read_csv('employees.csv')

# Add columns here
get_last_name=lambda x: x.split(' ')[-1]
df['last_name'] = df.name.apply(get_last_name)
print(df)
