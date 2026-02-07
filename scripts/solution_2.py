# Step 1: Create a Sample DataFrame
import pandas as pd
data={
     "Name": ["Het","Stuti","Krisha","Akshat","Chirag","Jagruti"],
     "Age": [20,22,21,23,24,25],
     "Salary": [50000,60000,55000,70000,65000,80000],
     "Performance Score": [85,90,78,92,87,95]
}

df=pd.DataFrame(data)
print("Sample DataFrame:")
print(df)

# Step 2: How to Select Single Column
print('Name(Single Column return Series)')
print(df["Name"]) # this will return Single Column as Series

#Step 3: How to Select Multiple Columns
subset=df[["Name", "Salary"]]
print('\nSubset with Name and Salary')
print(subset) # this will return Multiple Columns as DataFrame

# Step 4: How to Filter Rows Based on Single Condition
high_salary = df[df["Salary"] > 50000]
print("\nEmployees with Salary greater than 50000")
print(high_salary)

#Step 5: How to Filter Rows Based on Multiple Conditions
# Filtering rows Salary > 60000 & age > 22

filtered= df[(df["Age"] > 22) & (df['Salary'] > 60000)]
print(f'\nEmployee List age > 22 and Salary > 60000') # this will return rows where age is greater than 22 and salary is greater than 60000
print(filtered)