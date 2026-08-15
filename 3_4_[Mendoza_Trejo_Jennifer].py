import pandas as pd

#loading data
df = pd.read_csv("messy_data.csv")

#text standardization
df["state"] = df["state"].str.lower()

#date standardization-consistent format
df["date_joined"] = df["date_joined"].replace({
    "01/15/2022": "2022-01-15",
    "Feb 1, 2022": "2022-02-01",
    "March 5 2022": "2022-03-05",
    "2022/03/01": "2022-03-01"
    })
#date standardization 
df["date_joined"] = pd.to_datetime(df["date_joined"])

#numerical normalization
df["normalized"] = (
    (df["score"]-df["score"].min()) /
    (df["score"].max() - df["score"].min())
    )

#save
df.to_csv("standardized_data.csv", index=False)
