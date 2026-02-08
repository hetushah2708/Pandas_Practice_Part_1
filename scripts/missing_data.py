import pandas as pd

data={
     "Name": ["Het",None,"Stuti","Krisha","Akshat","Chirag","Jagruti"],
     "Age": [20,None,22,21,23,24,25],
     "Salary": [50000,None,60000,55000,70000,65000,80000],
     "Performance Score": [85,None,90,78,92,87,95]
}

df=pd.DataFrame(data)
print(df)

# now if u want to check if the data is missing or not then use below:
print(df.isnull())
# if in the output it gives true that means the data is missing

# now if u want to check how many missing values are there in 1 column
print(df.isnull().sum())



