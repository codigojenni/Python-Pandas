import pandas as pd

#loading data
df = pd.read_csv("messy_data.csv")

#print(df["state"])

#make text entries consistent
df["state"] = df["state"].str.lower()
df["state"] = df["state"].replace({"tx":"texas"})

#printing updated changes
print(df["state"])

#save data
df.to_csv("corrected_data.csv", index=False)
