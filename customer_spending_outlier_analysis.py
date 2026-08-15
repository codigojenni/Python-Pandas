import pandas as pd
import matplotlib.pyplot as plt

# Load  dataset
df = pd.read_csv("customer_data.csv")


plt.figure()

df.boxplot(column='Annual Spending')

plt.title('Annual Spending Box Plot')

plt.tight_layout()
plt.show()


"""
Reflection:
The box plot shows that most annual spending values fall within a consistent range.
There are no extreme points far outside the whiskers, indicating no significant outliers.
Based on the EDA approach, this suggests the data is relatively stable
and does not contain unusual spending values that would require further investigation.
"""
