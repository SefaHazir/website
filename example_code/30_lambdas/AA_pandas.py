import pandas as pd

df = pd.read_csv('example_data.csv', delimiter = ',')
print(df.head())

df['animal'] = df['animal'].apply(lambda x: x.capitalize())
print(df.head())