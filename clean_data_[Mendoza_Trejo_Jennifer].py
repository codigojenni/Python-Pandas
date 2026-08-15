import pandas as pd

#1: explore data
df = pd.read_csv("employee_records.csv")

print("Head of Data:")
print(df.head())

print("Info:")
print(df.info())

print("Describe:")
print(df.describe())

"""
Observed Issues:
1. Missing values in salary & hire_date columns
2. Inconsistent text entries in department & state columns
3. duplicate records found

"""
#2: clean data
#fix missing values
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["hire_date"] = df["hire_date"].ffill()

#fix inconsistent data entries
df["state"] = df["state"].str.lower()
df["state"] = df["state"].replace({
    "tx": "Texas",
    "texas": "Texas",
    "ca": "California",
    "california": "California",
    "ny": "New York"
    })
df["department"] = df["department"].str.lower().str.title()

#standardize date format
df["hire_date"] = pd.to_datetime(df["hire_date"], dayfirst=True)

#normalize salary min & max
df["salary_normalized"] = (
    (df["salary"] - df["salary"].min()) /
    (df["salary"].max() - df["salary"].min())

)
#3: analysis prep
#removing duplicate records
df = df.drop_duplicates()

#loading dept codes & merging
dept_codes = pd.read_csv("department_codes.csv")
merged = pd.merge(df, dept_codes, on="department")

#Pivot table
pivot = merged.pivot_table(
    index="department",
    values="salary",
    aggfunc="mean"
    )

#save
merged.to_csv("cleaned_employee_records.csv", indez=False)
pivot.to_csv("average_salary_by_department.csv")

                      

