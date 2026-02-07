# Describe method in Pnadas are used to generate descriptive statistics of numeric columns in a DataFrame. 


# Step 1- create a Sample DataFrame
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

print("\nDescriptive Statistics:")
print(df.describe())


# The Outout will be:
# Sample DataFrame:
#      Name  Age  Salary  Performance Score
# 0     Het   20   50000                 85
# 1   Stuti   22   60000                 90
# 2  Krisha   21   55000                 78
# 3  Akshat   23   70000                 92
# 4   Chirag   24   65000                 87
# 5  Jagruti   25   80000                 95

# Descriptive Statistics:
#              Age        Salary  Performance Score
# count   6.000000      6.000000           6.000
# mean   22.500000  63333.333333          87.833333
# std     1.870829   11180.339887           6.
# min    20.000000  50000.000000          78.000000
# 25%    21.250000  53750.000000
# 50%    22.500000  62500.000000          87.000000
# 75%    23.750000  71250.000000


# here, count is the number of non-null entries
#mean in the average value of the column
#std is the standard deviation which measures the spread of the data
#min is the minimum value in the column
#25% is the value below which 25% of the data falls
#50% is the median value which is the middle value of the sorted data
#75% is the value below which 75% of the data falls
