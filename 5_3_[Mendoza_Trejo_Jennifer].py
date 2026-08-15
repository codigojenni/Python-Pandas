import pandas as pd
import matplotlib.pyplot as plt

# Load  dataset
df = pd.read_csv("customer_data.csv")


plt.figure()

df["Age"].plot(kind='hist', bins=8)

plt.title("Distribution of Customer Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True)

plt.tight_layout()
plt.show()

plt.figure()

df["Region"].value_counts().plot(kind='bar')

plt.title("Number of Customers by Region")
plt.xlabel("Region")
plt.ylabel("Number of Customers")
plt.grid(True)

plt.tight_layout()
plt.show()


""" Reflection:
The histogram shows that customer ages range from 22 to 53,
with many customers concentrated in their 30s and 40s.
This suggests the company serves a broad but slightly middle-aged demographic.
The bar chart shows that customer counts are evenly distributed across North, South, East, and West,
indicating balanced regional representation."""
