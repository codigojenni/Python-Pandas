import pandas as pd
df = pd.read_csv("messy_data.csv")

print("--------------First 10 rows--------------")
print(df.head(10))

print("---------------Dataset Info----------------")
print(df.info())

print("----------------Statistics------------------")
print(df.describe())




#problems in code:
#missing values NaN in several columns, which can affect the statistics
#some columns appear to have incorrect data types because some of the data types come up as strings
#data is not clean--different capitalization & types of values such as the dates it looks messy. 
