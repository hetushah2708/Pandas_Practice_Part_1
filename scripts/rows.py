'''
When u load the data set u need to understand its structure like how many rows and columns are there,
what are the data types of each column, are there any missing values, etc.
'''

# so there are 2 methods , 1st is head() and 2nd is tail() method which will give you the first 5 row
# and last 5 rows of the data set respectively. 

import pandas as pd

df=pd.read_json(r"C:\Users\CHIRAG SHAH\OneDrive\Desktop\pandas_practice\sample_Data.json",encoding="latin1")

print('Display 10 rows of the data set')
print(df.head(10)) # this will give you the first 10 rows of the data set

print('Display last 10 rows of the data set')
print(df.tail(10)) # this will give you the last 10 rows of the data set