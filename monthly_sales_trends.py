import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Create the line plot
df.plot(x="Month", y="Sales Revenue", legend=False)

# Add title & labels
plt.title("Total Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

# Show  plot
plt.show()
