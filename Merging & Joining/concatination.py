# Concatination simply means that we need to combine the dataset tpgether by vertically or horizontally


# Syntax is: pd.concate([df1,df2],axis=0, ignore_index=True)

# df1 & df2 = alist of dataframes that u want to concatinate
# axis=0 will stack them row wise
# ignore_index=True simpy means that index ko reset kar do jo combine dataframe mera ban ne wala hai

# For Vertically
import pandas as pd

# data frame for region1
df_Region1= pd.DataFrame({
    'Cust Id': [1,2],
    'Name': ['Het','Krisha']
})

# data frame for region2
df_Region2= pd.DataFrame({
    'Cust Id': [3,4],
    'Name': ['Chirag','Stuti']
})

df_concate= pd.concat([df_Region1,df_Region2], axis=0, ignore_index=True)
print(df_concate)


# For Horizontally
df_concate=pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
print(df_concate)