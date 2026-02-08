# Interpolation is a technique , its a very useful technique with the help of this we can put estimated values in missing values

# for eg: if there is a series of 10,20,Nan,40,50
# here we can detect a series , so we can stimate the missng value could be 30
#Data will be consistent, it follow a pattern , based on mathematical methods(linear interpolation, polynomial interpolation)
import pandas as pd
data={
     "Name": ["Het",None,"Stuti","Krisha","Akshat","Chirag","Jagruti"],
     "Age": [20,None,22,21,23,24,25],
     "Salary": [50000,None,60000,55000,70000,65000,80000],
     "Performance Score": [85,None,90,78,92,87,95]
}

df=pd.DataFrame(data)
print(df)

df.interpolate(method='Linear',axis=0,inplace=True) # here we are using linear method
