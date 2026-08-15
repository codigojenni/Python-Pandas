import pandas as pd

#loading data
df = pd.read_csv("messy_data.csv")

print("Missing values per column:")
print(df.isnull().sum())

#drop rows with missing values
df_dropped = df.dropna()

#save dropped value version
df_dropped.to_csv("data_dropped.csv", index=False)

#fill missing values
df_filled = df.copy()

#filling missing value w/unknown
df_filled = df_filled.fillna("Unknown")

#fill missing values with column mean
if "column_name" in df_filled.columns:
    df_filled["column_name"] = df_filled["column_name"].fillna(
        df_filled["column_name"].mean()
        )
#save cleaned data
df_filled.to_csv("data_filled.csv", index=False)

    