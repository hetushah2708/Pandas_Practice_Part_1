import pandas as pd

# Read data from CSV file
df=pd.read_csv(r"C:\\Users\\CHIRAG SHAH\\OneDrive\\Desktop\\pandas_practice\\sales_data_sample.csv",encoding="latin1")
print(df)
#here we read the data from csv file using  pd.read_csv() function 

#if your data is stored in the cloud, you can use gcsfs library to read the data directly from cloud storage.

