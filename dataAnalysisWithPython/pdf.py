import pandas as pd

df = pd.read_csv('nba.csv')

print(df[['Name', 'College']])
print(df.head())