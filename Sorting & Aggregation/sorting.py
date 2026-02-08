# Sorting simply means that , rows ko ek dataframe mei aise arrange karna based on values of 1 or whole columns

#Sorting Data in 1 Column
#syntax: df.sort_values()by="Column Name", True/False,inplace=True)
# here True/False means the data will set in ascending(False) and decending(True)

import pandas as pd
data={
    "Name": [' Het','Krisha','Stuti'],
    "Age" : [28,32,22],
    "Salary": [10000,20000,30000]
}

df=pd.DataFrame(data)
print(df)

df.sort_values(by="Age",ascending=False,inplace=True)
# here ascending=False means AGe will be sorter in Descending order 
print("Age is in Decending Order")
print(df)

# if u want to sort multiple Columns 
df.sort_values(by=["Age", "Salary"],ascending=False,inplace=True)
print("\nAge and Salary are in Descending Order")
print(df)