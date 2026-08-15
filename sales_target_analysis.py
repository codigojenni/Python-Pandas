import pandas as pd

#load both datasets
sales_df = pd.read_csv("sales.csv")
targets_df = pd.read_csv("sales_targets.csv")

print("Sales Data:")
print(sales_df)

print("Sales Targets Data")
print(targets_df)

#merge salesperson
merged_df = pd.merge(
    sales_df,
    targets_df,
    on="Salesperson",
    how="inner"
    )

print("Merged Data (Inner Join on Salesperson):")
print(merged_df)

#calculate difference
#difference = revenue - target revenue
merged_df["Difference"] = merged_df["Revenue"] - merged_df["Target_Revenue"]

print("With Difference Column:")
print(merged_df)

#sort by difference descending
sorted_df = merged_df.sort_values(
    by="Difference",
    ascending=False
    )

print("Sorted by Difference (Highest to Lowest):")
print(sorted_df)
