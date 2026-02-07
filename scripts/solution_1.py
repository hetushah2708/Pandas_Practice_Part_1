# so we made a problem.txt file  and mentoined all the problems and now below is the solution:

# Basically how to summarize the data 

import pandas as pd
# Read data from CSV file
df=pd.read_json(r"C:\Users\CHIRAG SHAH\OneDrive\Desktop\pandas_practice\sample_Data.json",encoding="latin1")

print("Displaying the info of the Data Set")
print(df.info())

# the output will be:
#  #   Column  Non-Null Count  Dtype
#  0   id      100 non-null    int64
#  1   name    100 non-null    object
#  2   age     100 non-null    int64
#  3   city    100 non-null    object
#  4   salary  100 non-null    int64

# the above is the summary of the DataFrame
