import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

df.plot(kind='scatter', x='Advertising Budget', y='Sales Revenue')

plt.title('Advertising Budget vs Sales Revenue')
plt.xlabel('Advertising Budget')
plt.ylabel('Sales Revenue')

plt.show()