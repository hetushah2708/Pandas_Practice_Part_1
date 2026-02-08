# Merging in Pnadas means , combining 2 or more thatn 2 dataframes ke rows ko combine karna based on a common key column

# Syntax:  pd.merge(df1,df2, on="Column Name", how="type of join")
# here df1 and df2 is the dataframes u want to merge
#on="Column Name" is the common column in that 2 dataframes(df1 & df2)
#how="type of join" whihc type of join u want to do(Inner, outer,left,right)


import pandas as pd

#Customer Name DataFrame (df1)
df_customers= pd.DataFrame({
    'Customer Id': [1,2,3],
    'Name': ['Ramesh','Suresh','Kalpesh']
})

#order Data frame (df2)
df_order=pd.DataFrame({
    'Customer Id': [1,2,4],
    'Order Amount': [250,450,350]
})

df_merged = pd.merge(df_customers,df_order,on="Customer Id",how='inner')
print('inner Join')
# so inner join give output if the keys match with each other 
print(df_merged)

# Outter Join
df_merged = pd.merge(df_customers,df_order,on="Customer Id",how='outer')
print('\nouter Join')
# so outer join will merge all the rows and jisme values match nahi hogi toh waha Nan likkh ke aayega
print(df_merged)

#left Join
df_merged = pd.merge(df_customers,df_order,on="Customer Id",how='left')
print('\nleft Join')
# so left join will keep the left side of the rows if it is matchig with the right ones
print(df_merged)

#right join
df_merged = pd.merge(df_customers,df_order,on="Customer Id",how='right')
print('\nrightJoin')
# so right join will keep the right side of the rows if it is matchig with the left ones
print(df_merged)