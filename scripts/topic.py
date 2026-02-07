'''
1- How bis is your data set?
2- What are the names of columns in your data set?

'''

import pandas as pd

data={
     "Name": ["Het","Stuti","Krisha","Akshat","Chirag","Jagruti"],
     "Age": [20,22,21,23,24,25],
     "Salary": [50000,60000,55000,70000,65000,80000],
     "Performance Score": [85,90,78,92,87,95]
}
df=pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}')
print(f'Columns: {df.columns}')


