# How to add column using Pandas
import pandas as pd

data={
     "Name": ["Het","Stuti","Krisha","Akshat","Chirag","Jagruti"],
     "Age": [20,22,21,23,24,25],
     "Salary": [50000,60000,55000,70000,65000,80000],
     "Performance Score": [85,90,78,92,87,95]
}

df=pd.DataFrame(data)

# now adding column 
print(df)
df["Bonus"] = df['Salary']  * 0.1  
print(df)

# now if u want to add particular column at specific location
df.insert(0,'Employee Id', [10,20,30,40,50,60])
print(df)

df.insert(1, 'Employee Location', ['mum','bang','delhi','pune','indore','hyd'])
print(df)

# now if u want to update something
df.loc[0,"Salary"] = 55000 # this will change the salary of het from 50K to 55K
print(df)

df.insert(4,"Job Title", ["Gen AI Developer","Fashion Arts","CS","AI Engineer","IT","Accounts"])
print(df)

df.loc[2,"Salary"] = 70000 
print(df)

# now if i want to update entire column for eg if i want to update the salary of everyone with 5%

df["Salary"] =df['Salary'] *1.05
print(df)

