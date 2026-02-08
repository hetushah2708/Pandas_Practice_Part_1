import pandas as pd

data={
     "Name": ["Het","Stuti","Krisha","Akshat","Chirag","Jagruti"],
     "Age": [20,22,21,23,24,25],
     "Salary": [50000,60000,55000,70000,65000,80000],
     "Performance Score": [85,90,78,92,87,95]
}
df=pd.DataFrame(data)
print(df)

# now if u want to delete any data or drop any data of rows and columns then,
# Syntax is : df.drop(columns=["Colunm Name"], inplace=True)
# here inplace means it will modify the data without giving new one

print("\nModified Data")
df.drop(columns=["Performance Score","Age"], inplace=True) # this will drop/dlete the Prformance and Age column
print(df)
