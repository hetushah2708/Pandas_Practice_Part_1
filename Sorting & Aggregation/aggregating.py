# Aggregating simply means tocalculate sum , difference and etc

import pandas as pd
data={
    "Name": [' Het','Krisha','Stuti'],
    "Age" : [28,32,22],
    "Salary": [10000,20000,30000]
}

df=pd.DataFrame(data)
print(df)

avg_salary= df['Salary'].mean() # here .mean is used to calculate the average 
print("now it will show u avg_salary")
print(avg_salary)

