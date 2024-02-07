# Checking for missing values using isnull() and notnull()

import pandas as pd

df = pd.read_csv('nba.csv')
# missing_values = df.isnull()

# print(missing_values.head(10))
# missing_values = df.notnull()
# print(missing_values.head(10))

# Filling missing values using fillna(), replace() and interpolate() :
df.fillna(0)
print(df.head(10))
# missing_values = df.notnull()

# Dropping missing values using dropna() :

# Now we apply iterrows() function in order to get a each element of rows.
# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(dict)
 
# iterating over rows using iterrows() function 
for i, j in df.iterrows():
    print(i, j)
    print()