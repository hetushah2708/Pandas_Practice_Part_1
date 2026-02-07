#so for eg if u are done with data manipulation and data cleaning and u want to save the data 

import pandas as pd
data={
    "Name": ["Het","Krisha","Akhshat"],
    "Age": [23,21,23],
    "City": ["Mumbai","Surat","Palitana"]
}

# now will create a dataframe using this data and then save it to a csv file
df=pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False) # the file will be saved in the current directory and index=False is used to avoid the sr.no

# if the file is excel then,
df.to_excel("output.xlsx", index=False)
# if the file is json then,
df.to_json("output.json", index=False) 