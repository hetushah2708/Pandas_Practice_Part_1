import pandas as pd
data={
    "Name": [' Het','Krisha','Stuti','Akshat','Chirag'],
    "Age" : [28,34,22,34,28],
    "Salary": [50000,60000,45000,52000,480000]
}

df=pd.DataFrame(data)
print(df)

# Now will do grouping 
grouped = df.groupby("Age")['Salary'].sum()
print(grouped)