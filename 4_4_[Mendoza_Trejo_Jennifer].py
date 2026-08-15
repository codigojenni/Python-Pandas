import pandas as pd

df = pd.read_csv("sales.csv")

print("Original Data:")
print(df)

print("----------------Pivot Table-------------------")
pivot_table = df.pivot_table(
    index="Region",
    columns="Product",
    values="Revenue",
    aggfunc="sum"
    )
print("Total Revenue by Region and Product")
print(pivot_table)

melted_df = df.melt(
    id_vars=["Region", "Product"],
    value_vars=["Units_Sold", "Revenue"],
    var_name="Variable",
    value_name="Value"
    )

print("Melted DataFrame:")
print(melted_df)

#stack dataframe (melted)
stacked_df = melted_df.set_index(["Region", "Product", "Variable"]).stack()

print("Stacked DataFrame:")
print(stacked_df)

