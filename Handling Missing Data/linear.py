import pandas as pd

data={
    "Time": [1,2,3,4,5],
    "Value": [10,None,30,None,50]
    
}

df=pd.DataFrame(data)
print("before interpolation")
print(df)

df['Value']= df['Value'].interpolate(method="linear")
print("after interpolation")
print(df)

# when to use interpolation?
# when u are working with time series data(stock market, numeric data)