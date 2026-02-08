# if u want drop the missing value then
# Syntax: dropna(axis=0, inplace=True) , here axis=0 means drop rows with missing values and axis=1 drop columns with missing values


import pandas as pd
data={
     "Name": ["Het",None,"Stuti","Krisha","Akshat","Chirag","Jagruti"],
     "Age": [20,None,22,21,23,24,25],
     "Salary": [50000,None,60000,55000,70000,65000,80000],
     "Performance Score": [85,None,90,78,92,87,95]
}

df=pd.DataFrame(data)
print(df)

# df.dropna(inplace=True)
# print(df)


#fillna(), so basicaly missing values are very frrequent and we can loose our data
# so for those values we can give a different value adn then we can romove

# df.fillna(0,inplace=True)
# print(df)

# We can also fill the calculated value
df["Age"].fillna(df(['Age'].mean(),inplace=True))
print(df)